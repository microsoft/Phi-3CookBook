# Navzkrižna platforma za inferenco z Rustom

Ta vodič nas bo popeljal skozi postopek izvajanja inference z uporabo Rusta in [Candle ML ogrodja](https://github.com/huggingface/candle) iz HuggingFace. Uporaba Rusta za inferenco ponuja številne prednosti, še posebej v primerjavi z drugimi programskimi jeziki. Rust je znan po svoji visoki zmogljivosti, ki je primerljiva s C in C++. Zaradi tega je odlična izbira za naloge, ki zahtevajo veliko računske moči, kot je inferenca. To je predvsem posledica njegovih abstrakcij brez stroškov in učinkovitega upravljanja pomnilnika brez obremenitev zaradi zbiranja odpadkov. Rustove zmogljivosti za delovanje na različnih platformah omogočajo razvoj kode, ki deluje na različnih operacijskih sistemih, vključno z Windows, macOS in Linux, pa tudi na mobilnih operacijskih sistemih, brez večjih sprememb kode.

Predpogoj za sledenje temu vodiču je [namestitev Rusta](https://www.rust-lang.org/tools/install), ki vključuje Rustov prevajalnik in Cargo, Rustov upravljalnik paketov.

## 1. korak: Ustvarite nov Rustov projekt

Za ustvarjanje novega Rustovega projekta zaženite naslednji ukaz v terminalu:

```bash
cargo new phi-console-app
```

To ustvari začetno strukturo projekta z datoteko `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## 2. korak: Konfigurirajte osnovne parametre

Znotraj datoteke main.rs bomo nastavili začetne parametre za našo inferenco. Za enostavnost bodo vsi parametri vnaprej določeni, vendar jih lahko po potrebi prilagodimo.

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

- **temperature**: Nadzira naključnost procesa vzorčenja.
- **sample_len**: Določa največjo dolžino generiranega besedila.
- **top_p**: Uporablja se za vzorčenje z jedrom (nucleus sampling), da omeji število obravnavanih tokenov pri vsakem koraku.
- **repeat_last_n**: Nadzira število tokenov, ki jih je treba upoštevati za uporabo kazni za preprečevanje ponavljajočih se zaporedij.
- **repeat_penalty**: Vrednost kazni, ki odvrača ponavljajoče se tokene.
- **seed**: Naključni začetni ključ (za boljšo ponovljivost lahko uporabimo konstantno vrednost).
- **prompt**: Začetno besedilo, ki sproži generiranje. Opazite, da modelu naročimo, naj ustvari haiku o hokeju na ledu, in ga ovijemo s posebnimi tokeni, ki označujejo dele pogovora med uporabnikom in pomočnikom. Model bo nato dokončal besedilo s haikujem.
- **device**: V tem primeru uporabljamo CPU za izračune. Candle podpira izvajanje na GPU-jih z uporabo CUDA in Metal.

## 3. korak: Prenesite/pripravite model in tokenizator

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

Uporabljamo datoteko `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` za tokenizacijo našega vhodnega besedila. Ko je model prenesen, se predpomni, zato bo prva izvedba počasnejša (ker prenese 2,4 GB modela), nadaljnje izvedbe pa bodo hitrejše.

## 4. korak: Naložite model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Naložimo uteži kvantiziranega modela v pomnilnik in inicializiramo model Phi-3. Ta korak vključuje branje uteži modela iz datoteke `gguf` in pripravo modela za inferenco na izbrani napravi (v tem primeru CPU).

## 5. korak: Obdelajte poziv in pripravite na inferenco

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

V tem koraku tokeniziramo vhodni poziv in ga pripravimo na inferenco s pretvorbo v zaporedje ID-jev tokenov. Prav tako inicializiramo vrednosti `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Vsak token se pretvori v tenzor in pošlje skozi model za pridobitev logitov.

Zanka obdela vsak token v pozivu, posodobi procesor logitov in pripravi naslednje generiranje tokena.

## 6. korak: Inferenca

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

V zanki za inferenco generiramo tokene enega za drugim, dokler ne dosežemo želene dolžine vzorca ali naletimo na končni token zaporedja. Naslednji token se pretvori v tenzor in pošlje skozi model, medtem ko se logiti obdelajo za uporabo kazni in vzorčenja. Nato se naslednji token vzorči, dekodira in doda v zaporedje. 

Da bi se izognili ponavljajočemu se besedilu, se kazen uporabi za ponavljajoče se tokene glede na parametra `repeat_last_n` and `repeat_penalty`.

Nazadnje se generirano besedilo sproti izpiše, ko se dekodira, kar omogoča pretočni izhod v realnem času.

## 7. korak: Zaženite aplikacijo

Za zagon aplikacije zaženite naslednji ukaz v terminalu:

```bash
cargo run --release
```

To bi moralo natisniti haiku o hokeju na ledu, ki ga je generiral model Phi-3. Nekaj takega:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ali

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Zaključek

Z upoštevanjem teh korakov lahko generiramo besedilo z uporabo modela Phi-3 z Rustom in Candle v manj kot 100 vrsticah kode. Koda obravnava nalaganje modela, tokenizacijo in inferenco, pri čemer uporablja tenzorje in obdelavo logitov za generiranje koherentnega besedila na podlagi vhodnega poziva.

Ta konzolna aplikacija lahko deluje na Windows, Linux in Mac OS. Zaradi prenosljivosti Rusta lahko kodo prilagodimo tudi knjižnici, ki bi delovala znotraj mobilnih aplikacij (konzolnih aplikacij tam ne moremo zagnati).

## Dodatek: celotna koda

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

Opomba: za zagon te kode na aarch64 Linux ali aarch64 Windows dodajte datoteko z imenom `.cargo/config` z naslednjo vsebino:

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

> Obiščete lahko uradni repozitorij [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) za več primerov, kako uporabljati model Phi-3 z Rustom in Candle, vključno z alternativnimi pristopi k inferenci.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo strojnih storitev umetne inteligence za prevajanje. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.