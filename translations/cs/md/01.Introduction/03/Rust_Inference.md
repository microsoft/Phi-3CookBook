# Křížová inference s Rustem

Tento tutoriál nás provede procesem provádění inference pomocí Rustu a [Candle ML frameworku](https://github.com/huggingface/candle) od HuggingFace. Použití Rustu pro inferenci nabízí několik výhod, zejména ve srovnání s jinými programovacími jazyky. Rust je známý svou vysokou výkonností, srovnatelnou s C a C++. Díky tomu je skvělou volbou pro úlohy inference, které mohou být výpočetně náročné. To je dáno především zero-cost abstrakcemi a efektivním řízením paměti, které nevyžaduje garbage collection. Schopnost Rustu pracovat napříč platformami umožňuje vývoj kódu, který běží na různých operačních systémech, včetně Windows, macOS a Linuxu, stejně jako na mobilních operačních systémech, aniž by bylo nutné provádět významné změny v kódu.

Předpokladem pro sledování tohoto tutoriálu je [instalace Rustu](https://www.rust-lang.org/tools/install), která zahrnuje Rust kompilátor a Cargo, správce balíčků pro Rust.

## Krok 1: Vytvoření nového Rust projektu

Pro vytvoření nového Rust projektu spusťte následující příkaz v terminálu:

```bash
cargo new phi-console-app
```

Tím se vygeneruje základní struktura projektu s `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` souborem:

```toml
[package]
name = "phi-console-app"
version = "0.1.0"
edition = "2021"

[dependencies]
candle-core = { version = "0.6.0" }
candle-transformers = { version = "0.6.0" }
hf-hub = { version = "0.3.2", features = ["tokio"] }
rand = "0.8"
tokenizers = "0.15.2"
```

## Krok 2: Nastavení základních parametrů

Uvnitř souboru `main.rs` nastavíme počáteční parametry pro naši inferenci. Pro jednoduchost budou všechny parametry pevně zakódované, ale můžeme je podle potřeby upravit.

```rust
let temperature: f64 = 1.0;
let sample_len: usize = 100;
let top_p: Option<f64> = None;
let repeat_last_n: usize = 64;
let repeat_penalty: f32 = 1.2;
let mut rng = rand::thread_rng();
let seed: u64 = rng.gen();
let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";
let device = Device::Cpu;
```

- **temperature**: Ovládá náhodnost procesu vzorkování.
- **sample_len**: Určuje maximální délku generovaného textu.
- **top_p**: Používá se pro nucleus sampling k omezení počtu tokenů, které se berou v úvahu při každém kroku.
- **repeat_last_n**: Ovládá počet tokenů, které se zohledňují při aplikaci penalizace, aby se zabránilo opakujícím se sekvencím.
- **repeat_penalty**: Hodnota penalizace, která odrazuje od opakování tokenů.
- **seed**: Náhodné semeno (můžeme použít konstantní hodnotu pro lepší reprodukovatelnost).
- **prompt**: Počáteční textový prompt, který zahájí generování. Všimněte si, že model požádáme, aby vytvořil haiku o ledním hokeji, a že ho obalíme speciálními tokeny, které označují části konverzace uživatele a asistenta. Model pak prompt doplní haiku.
- **device**: V tomto příkladu používáme CPU pro výpočty. Candle podporuje běh na GPU s CUDA a Metalem.

## Krok 3: Stažení/Příprava modelu a tokenizéru

```rust
let api = hf_hub::api::sync::Api::new()?;
let model_path = api
    .repo(hf_hub::Repo::with_revision(
        "microsoft/Phi-3-mini-4k-instruct-gguf".to_string(),
        hf_hub::RepoType::Model,
        "main".to_string(),
    ))
    .get("Phi-3-mini-4k-instruct-q4.gguf")?;

let tokenizer_path = api
    .model("microsoft/Phi-3-mini-4k-instruct".to_string())
    .get("tokenizer.json")?;
let tokenizer = Tokenizer::from_file(tokenizer_path).map_err(|e| e.to_string())?;
```

Používáme soubor `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` pro tokenizaci našeho vstupního textu. Po stažení je model uložen do cache, takže první spuštění bude pomalé (protože se stahuje 2,4GB model), ale následující spuštění budou rychlejší.

## Krok 4: Načtení modelu

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Načteme kvantizované váhy modelu do paměti a inicializujeme model Phi-3. Tento krok zahrnuje čtení vah modelu ze souboru `gguf` a nastavení modelu pro inferenci na zvoleném zařízení (v tomto případě CPU).

## Krok 5: Zpracování promptu a příprava na inferenci

```rust
let tokens = tokenizer.encode(prompt, true).map_err(|e| e.to_string())?;
let tokens = tokens.get_ids();
let to_sample = sample_len.saturating_sub(1);
let mut all_tokens = vec![];

let mut logits_processor = LogitsProcessor::new(seed, Some(temperature), top_p);

let mut next_token = *tokens.last().unwrap();
let eos_token = *tokenizer.get_vocab(true).get("").unwrap();
let mut prev_text_len = 0;

for (pos, &token) in tokens.iter().enumerate() {
    let input = Tensor::new(&[token], &device)?.unsqueeze(0)?;
    let logits = model.forward(&input, pos)?;
    let logits = logits.squeeze(0)?;

    if pos == tokens.len() - 1 {
        next_token = logits_processor.sample(&logits)?;
        all_tokens.push(next_token);
    }
}
```

V tomto kroku tokenizujeme vstupní prompt a připravíme ho na inferenci konverzí na sekvenci ID tokenů. Také inicializujeme hodnoty `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Každý token je převeden na tensor a předán modelu, aby byly získány logits.

Smyčka zpracovává každý token v promptu, aktualizuje logits processor a připravuje se na generování dalšího tokenu.

## Krok 6: Inference

```rust
for index in 0..to_sample {
    let input = Tensor::new(&[next_token], &device)?.unsqueeze(0)?;
    let logits = model.forward(&input, tokens.len() + index)?;
    let logits = logits.squeeze(0)?;
    let logits = if repeat_penalty == 1. {
        logits
    } else {
        let start_at = all_tokens.len().saturating_sub(repeat_last_n);
        candle_transformers::utils::apply_repeat_penalty(
            &logits,
            repeat_penalty,
            &all_tokens[start_at..],
        )?
    };

    next_token = logits_processor.sample(&logits)?;
    all_tokens.push(next_token);

    let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

    if decoded_text.len() > prev_text_len {
        let new_text = &decoded_text[prev_text_len..];
        print!("{new_text}");
        std::io::stdout().flush()?;
        prev_text_len = decoded_text.len();
    }

    if next_token == eos_token {
        break;
    }
}
```

Ve smyčce inference generujeme tokeny jeden po druhém, dokud nedosáhneme požadované délky vzorku nebo nenarazíme na konečný token sekvence. Další token je převeden na tensor a předán modelu, zatímco logits jsou zpracovány pro aplikaci penalizací a vzorkování. Poté je další token vzorkován, dekódován a připojen k sekvenci.
Aby se zabránilo opakujícímu se textu, je na opakované tokeny aplikována penalizace na základě parametrů `repeat_last_n` and `repeat_penalty`.

Nakonec je generovaný text vytištěn během dekódování, čímž je zajištěn průběžný výstup v reálném čase.

## Krok 7: Spuštění aplikace

Pro spuštění aplikace zadejte následující příkaz v terminálu:

```bash
cargo run --release
```

Mělo by se zobrazit haiku o ledním hokeji, které vygeneroval model Phi-3. Například:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

nebo

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Závěr

Dodržením těchto kroků můžeme provádět generování textu pomocí modelu Phi-3 s Rustem a Candle v méně než 100 řádcích kódu. Kód zvládá načítání modelu, tokenizaci a inferenci, využívá tensory a zpracování logits pro generování koherentního textu na základě vstupního promptu.

Tato konzolová aplikace může běžet na Windows, Linuxu a macOS. Díky přenositelnosti Rustu lze kód také přizpůsobit do knihovny, která by běžela uvnitř mobilních aplikací (konzolové aplikace tam přece nemůžeme spustit).

## Dodatek: kompletní kód

```rust
use candle_core::{quantized::gguf_file, Device, Tensor};
use candle_transformers::{
    generation::LogitsProcessor, models::quantized_phi3::ModelWeights as Phi3,
};
use rand::Rng;
use std::io::Write;
use tokenizers::Tokenizer;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    // 1. configure basic parameters
    let temperature: f64 = 1.0;
    let sample_len: usize = 100;
    let top_p: Option<f64> = None;
    let repeat_last_n: usize = 64;
    let repeat_penalty: f32 = 1.2;
    let mut rng = rand::thread_rng();
    let seed: u64 = rng.gen();
    let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";

    // we will be running on CPU only
    let device = Device::Cpu;

    // 2. download/prepare model and tokenizer
    let api = hf_hub::api::sync::Api::new()?;
    let model_path = api
        .repo(hf_hub::Repo::with_revision(
            "microsoft/Phi-3-mini-4k-instruct-gguf".to_string(),
            hf_hub::RepoType::Model,
            "main".to_string(),
        ))
        .get("Phi-3-mini-4k-instruct-q4.gguf")?;

    let tokenizer_path = api
        .model("microsoft/Phi-3-mini-4k-instruct".to_string())
        .get("tokenizer.json")?;
    let tokenizer = Tokenizer::from_file(tokenizer_path).map_err(|e| e.to_string())?;

    // 3. load model
    let mut file = std::fs::File::open(&model_path)?;
    let model_content = gguf_file::Content::read(&mut file)?;
    let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;

    // 4. process prompt and prepare for inference
    let tokens = tokenizer.encode(prompt, true).map_err(|e| e.to_string())?;
    let tokens = tokens.get_ids();
    let to_sample = sample_len.saturating_sub(1);
    let mut all_tokens = vec![];

    let mut logits_processor = LogitsProcessor::new(seed, Some(temperature), top_p);

    let mut next_token = *tokens.last().unwrap();
    let eos_token = *tokenizer.get_vocab(true).get("<|end|>").unwrap();
    let mut prev_text_len = 0;

    for (pos, &token) in tokens.iter().enumerate() {
        let input = Tensor::new(&[token], &device)?.unsqueeze(0)?;
        let logits = model.forward(&input, pos)?;
        let logits = logits.squeeze(0)?;

        // Sample next token only for the last token in the prompt
        if pos == tokens.len() - 1 {
            next_token = logits_processor.sample(&logits)?;
            all_tokens.push(next_token);
        }
    }

    // 5. inference
    for index in 0..to_sample {
        let input = Tensor::new(&[next_token], &device)?.unsqueeze(0)?;
        let logits = model.forward(&input, tokens.len() + index)?;
        let logits = logits.squeeze(0)?;
        let logits = if repeat_penalty == 1. {
            logits
        } else {
            let start_at = all_tokens.len().saturating_sub(repeat_last_n);
            candle_transformers::utils::apply_repeat_penalty(
                &logits,
                repeat_penalty,
                &all_tokens[start_at..],
            )?
        };

        next_token = logits_processor.sample(&logits)?;
        all_tokens.push(next_token);

        // decode the current sequence of tokens
        let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

        // only print the new part of the decoded text
        if decoded_text.len() > prev_text_len {
            let new_text = &decoded_text[prev_text_len..];
            print!("{new_text}");
            std::io::stdout().flush()?;
            prev_text_len = decoded_text.len();
        }

        if next_token == eos_token {
            break;
        }
    }

    Ok(())
}
```

Poznámka: aby tento kód fungoval na aarch64 Linuxu nebo aarch64 Windows, přidejte soubor s názvem `.cargo/config` s následujícím obsahem:

```toml
[target.aarch64-pc-windows-msvc]
rustflags = [
    "-C", "target-feature=+fp16"
]

[target.aarch64-unknown-linux-gnu]
rustflags = [
    "-C", "target-feature=+fp16"
]
```

> Můžete navštívit oficiální [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitář pro více příkladů, jak používat model Phi-3 s Rustem a Candle, včetně alternativních přístupů k inferenci.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.