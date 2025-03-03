# Krydsplatform-inferens med Rust

Denne vejledning guider os gennem processen med at udføre inferens ved hjælp af Rust og [Candle ML-rammen](https://github.com/huggingface/candle) fra HuggingFace. At bruge Rust til inferens giver flere fordele, især sammenlignet med andre programmeringssprog. Rust er kendt for sin høje ydeevne, som kan sammenlignes med C og C++. Dette gør det til et fremragende valg til inferensopgaver, der ofte er beregningstunge. Specielt skyldes dette de omkostningsfrie abstraktioner og den effektive hukommelsesstyring, der ikke har nogen overhead fra garbage collection. Rusts krydsplatform-egenskaber gør det muligt at udvikle kode, der kan køre på forskellige operativsystemer, herunder Windows, macOS og Linux, samt mobile operativsystemer, uden væsentlige ændringer i kodebasen.

Forudsætningen for at følge denne vejledning er at [installere Rust](https://www.rust-lang.org/tools/install), som inkluderer Rust-kompilatoren og Cargo, Rusts pakkemanager.

## Trin 1: Opret et nyt Rust-projekt

For at oprette et nyt Rust-projekt skal du køre følgende kommando i terminalen:

```bash
cargo new phi-console-app
```

Dette genererer en grundlæggende projektstruktur med en `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`-fil:

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

## Trin 2: Konfigurer grundlæggende parametre

Inde i main.rs-filen opsætter vi de indledende parametre for vores inferens. Disse vil være hardkodede for enkelhedens skyld, men vi kan tilpasse dem efter behov.

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

- **temperature**: Styrer tilfældigheden i udvælgelsesprocessen.
- **sample_len**: Angiver den maksimale længde af den genererede tekst.
- **top_p**: Bruges til nucleus sampling for at begrænse antallet af tokens, der overvejes for hvert trin.
- **repeat_last_n**: Styrer antallet af tokens, der overvejes for at anvende en straf for at undgå gentagelser.
- **repeat_penalty**: Strafværdien, der skal forhindre gentagne tokens.
- **seed**: En tilfældig seed (vi kan bruge en konstant værdi for bedre reproducerbarhed).
- **prompt**: Den indledende prompttekst, der starter genereringen. Bemærk, at vi beder modellen om at generere et haiku om ishockey, og at vi omslutter det med specielle tokens for at indikere bruger- og assistentdele af samtalen. Modellen vil derefter fuldføre prompten med et haiku.
- **device**: Vi bruger CPU til beregning i dette eksempel. Candle understøtter også GPU med CUDA og Metal.

## Trin 3: Download/forbered model og tokenizer

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

Vi bruger `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json`-filen til at tokenisere vores inputtekst. Når modellen er downloadet, caches den, så den første udførelse vil være langsom (da den downloader modellens 2,4 GB), men efterfølgende udførelser vil være hurtigere.

## Trin 4: Indlæs model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Vi indlæser de kvantiserede modelvægte i hukommelsen og initialiserer Phi-3-modellen. Dette trin indebærer at læse modelvægtene fra `gguf`-filen og opsætte modellen til inferens på den specificerede enhed (CPU i dette tilfælde).

## Trin 5: Behandl prompt og forbered til inferens

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

I dette trin tokeniserer vi inputprompten og forbereder den til inferens ved at konvertere den til en sekvens af token-ID'er. Vi initialiserer også `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`-værdier. Hvert token konverteres til en tensor og sendes gennem modellen for at få logits.

Løkken behandler hvert token i prompten, opdaterer logits-processoren og forbereder sig på genereringen af det næste token.

## Trin 6: Inferens

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

I inferensløkken genererer vi tokens ét ad gangen, indtil vi når den ønskede tekstlængde eller støder på slut-på-sekvens-tokenet. Det næste token konverteres til en tensor og sendes gennem modellen, mens logits behandles for at anvende straf og sampling. Derefter samples det næste token, dekodes og tilføjes til sekvensen.  
For at undgå gentagelser anvendes en straf på gentagne tokens baseret på `repeat_last_n` and `repeat_penalty`-parametrene.

Til sidst udskrives den genererede tekst, mens den dekodes, hvilket sikrer realtidsstreaming.

## Trin 7: Kør applikationen

For at køre applikationen skal du udføre følgende kommando i terminalen:

```bash
cargo run --release
```

Dette skulle udskrive et haiku om ishockey genereret af Phi-3-modellen. Noget som:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

eller

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Konklusion

Ved at følge disse trin kan vi udføre tekstgenerering ved hjælp af Phi-3-modellen med Rust og Candle på under 100 linjer kode. Koden håndterer modelloading, tokenisering og inferens, hvor den udnytter tensorer og logits-processering til at generere sammenhængende tekst baseret på inputprompten.

Denne konsolapplikation kan køre på Windows, Linux og Mac OS. På grund af Rusts portabilitet kan koden også tilpasses til et bibliotek, der kan køre inde i mobilapps (vi kan trods alt ikke køre konsolapps der).

## Appendiks: fuld kode

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

Bemærk: For at køre denne kode på aarch64 Linux eller aarch64 Windows, tilføj en fil med navnet `.cargo/config` med følgende indhold:

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

> Du kan besøge det officielle [Candle-eksempler](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)-repository for flere eksempler på, hvordan du bruger Phi-3-modellen med Rust og Candle, herunder alternative tilgange til inferens.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.