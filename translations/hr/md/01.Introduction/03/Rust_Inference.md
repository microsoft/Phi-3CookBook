# Križno-platformsko zaključivanje s Rustom

Ovaj vodič će vas provesti kroz proces izvođenja zaključivanja koristeći Rust i [Candle ML okvir](https://github.com/huggingface/candle) iz HuggingFacea. Korištenje Rusta za zaključivanje nudi nekoliko prednosti, osobito u usporedbi s drugim programskim jezicima. Rust je poznat po svojoj visokoj izvedbi, usporedivoj s C i C++. To ga čini izvrsnim izborom za zadatke zaključivanja, koji mogu biti računalno zahtjevni. Posebno se ističe zbog apstrakcija bez troškova i učinkovitog upravljanja memorijom, bez opterećenja od smeća. Rustove križno-platformske mogućnosti omogućuju razvoj koda koji se može pokretati na različitim operativnim sustavima, uključujući Windows, macOS i Linux, kao i mobilne operativne sustave, bez značajnih promjena u kodnoj bazi.

Preduvjet za praćenje ovog vodiča je [instalacija Rusta](https://www.rust-lang.org/tools/install), koja uključuje Rustov kompajler i Cargo, Rustov upravitelj paketa.

## Korak 1: Kreirajte novi Rust projekt

Za kreiranje novog Rust projekta, pokrenite sljedeću naredbu u terminalu:

```bash
cargo new phi-console-app
```

Ovo generira početnu strukturu projekta s datotekama `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`:

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

## Korak 2: Konfigurirajte osnovne parametre

Unutar datoteke `main.rs`, postavit ćemo početne parametre za naše zaključivanje. Svi će biti unaprijed definirani radi jednostavnosti, ali ih možemo prilagoditi po potrebi.

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

- **temperature**: Kontrolira nasumičnost procesa uzorkovanja.
- **sample_len**: Određuje maksimalnu duljinu generiranog teksta.
- **top_p**: Koristi se za uzorkovanje jezgre kako bi se ograničio broj razmatranih tokena u svakom koraku.
- **repeat_last_n**: Određuje broj tokena koji se uzimaju u obzir za primjenu kazne kako bi se spriječilo ponavljanje sekvenci.
- **repeat_penalty**: Vrijednost kazne koja obeshrabruje ponavljanje tokena.
- **seed**: Nasumično sjeme (možemo koristiti konstantnu vrijednost za bolju reproducibilnost).
- **prompt**: Početni tekst koji pokreće generiranje. Obratite pažnju da tražimo od modela da generira haiku o hokeju na ledu i da ga omotamo posebnim tokenima kako bismo označili dijelove razgovora između korisnika i asistenta. Model će zatim dovršiti prompt s haikuom.
- **device**: U ovom primjeru koristimo CPU za izračune. Candle podržava pokretanje na GPU-ima s CUDA i Metal tehnologijama.

## Korak 3: Preuzimanje/Priprema modela i tokenizatora

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

Koristimo datoteku `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` za tokenizaciju ulaznog teksta. Nakon preuzimanja, model se pohranjuje u privremenu memoriju, pa će prvo pokretanje biti sporije (jer preuzima 2,4 GB modela), ali će kasnija pokretanja biti brža.

## Korak 4: Učitavanje modela

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Učitavamo kvantizirane težine modela u memoriju i inicijaliziramo model Phi-3. Ovaj korak uključuje čitanje težina modela iz `gguf` datoteke i pripremu modela za zaključivanje na specificiranom uređaju (u ovom slučaju CPU).

## Korak 5: Obrada prompta i priprema za zaključivanje

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

U ovom koraku, tokeniziramo ulazni prompt i pripremamo ga za zaključivanje pretvaranjem u sekvencu ID-ova tokena. Također inicijaliziramo `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` vrijednosti. Svaki token se pretvara u tenzor i prosljeđuje kroz model kako bi se dobili logiti.

Petlja obrađuje svaki token u promptu, ažurira procesor logita i priprema se za generiranje sljedećeg tokena.

## Korak 6: Zaključivanje

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

U petlji za zaključivanje generiramo tokene jedan po jedan dok ne postignemo željenu duljinu uzorka ili ne naiđemo na token za kraj sekvence. Sljedeći token se pretvara u tenzor i prosljeđuje kroz model, dok se logiti obrađuju za primjenu kazni i uzorkovanja. Zatim se sljedeći token uzorkuje, dekodira i dodaje sekvenci.  
Kako bismo izbjegli ponavljajući tekst, kazna se primjenjuje na ponovljene tokene na temelju parametara `repeat_last_n` and `repeat_penalty`.

Na kraju, generirani tekst se ispisuje dok se dekodira, osiguravajući izlaz u stvarnom vremenu.

## Korak 7: Pokretanje aplikacije

Za pokretanje aplikacije, izvršite sljedeću naredbu u terminalu:

```bash
cargo run --release
```

Ovo bi trebalo ispisati haiku o hokeju na ledu generiran od strane modela Phi-3. Nešto poput:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ili

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Zaključak

Slijedeći ove korake, možemo generirati tekst koristeći model Phi-3 s Rustom i Candleom u manje od 100 linija koda. Kod obuhvaća učitavanje modela, tokenizaciju i zaključivanje, koristeći tenzore i obradu logita za generiranje koherentnog teksta na temelju ulaznog prompta.

Ova konzolna aplikacija može se pokretati na Windowsu, Linuxu i macOS-u. Zbog Rustove prenosivosti, kod se također može prilagoditi za knjižnicu koja bi se mogla pokretati unutar mobilnih aplikacija (budući da konzolne aplikacije tamo ne možemo pokretati).

## Dodatak: cjelokupni kod

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

Napomena: kako biste pokrenuli ovaj kod na aarch64 Linuxu ili aarch64 Windowsu, dodajte datoteku nazvanu `.cargo/config` sa sljedećim sadržajem:

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

> Možete posjetiti službeni [Candle primjeri](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repozitorij za više primjera kako koristiti model Phi-3 s Rustom i Candleom, uključujući alternativne pristupe zaključivanju.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluga za strojno prevođenje. Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.