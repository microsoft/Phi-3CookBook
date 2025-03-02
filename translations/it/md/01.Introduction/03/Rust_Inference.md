# Inferenza cross-platform con Rust

Questo tutorial ci guiderà attraverso il processo di esecuzione dell'inferenza utilizzando Rust e il [framework Candle ML](https://github.com/huggingface/candle) di HuggingFace. Usare Rust per l'inferenza offre diversi vantaggi, soprattutto rispetto ad altri linguaggi di programmazione. Rust è noto per le sue alte prestazioni, paragonabili a quelle di C e C++. Questo lo rende una scelta eccellente per attività di inferenza, che possono essere computazionalmente intensive. In particolare, ciò è possibile grazie alle astrazioni a costo zero e alla gestione efficiente della memoria, senza overhead dovuti al garbage collection. Le capacità cross-platform di Rust permettono di sviluppare codice che può essere eseguito su vari sistemi operativi, inclusi Windows, macOS e Linux, oltre che su sistemi operativi mobili, senza apportare modifiche significative al codice.

Il prerequisito per seguire questo tutorial è [installare Rust](https://www.rust-lang.org/tools/install), che include il compilatore Rust e Cargo, il gestore di pacchetti di Rust.

## Passo 1: Creare un Nuovo Progetto Rust

Per creare un nuovo progetto Rust, esegui il seguente comando nel terminale:

```bash
cargo new phi-console-app
```

Questo comando genera una struttura iniziale del progetto con un file `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Passo 2: Configurare i Parametri di Base

All'interno del file main.rs, configureremo i parametri iniziali per l'inferenza. Saranno tutti hardcoded per semplicità, ma potremo modificarli secondo necessità.

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

- **temperature**: Controlla la casualità del processo di campionamento.
- **sample_len**: Specifica la lunghezza massima del testo generato.
- **top_p**: Utilizzato per il campionamento a nucleo (nucleus sampling) per limitare il numero di token considerati a ogni passaggio.
- **repeat_last_n**: Controlla il numero di token considerati per applicare una penalità che previene sequenze ripetitive.
- **repeat_penalty**: Il valore della penalità per scoraggiare i token ripetuti.
- **seed**: Un seme casuale (possiamo usare un valore costante per una migliore riproducibilità).
- **prompt**: Il testo iniziale per avviare la generazione. Nota che chiediamo al modello di generare un haiku sull'hockey su ghiaccio e che lo racchiudiamo con token speciali per indicare le parti dell'utente e dell'assistente nella conversazione. Il modello completerà quindi il prompt con un haiku.
- **device**: In questo esempio utilizziamo la CPU per il calcolo. Candle supporta anche l'esecuzione su GPU con CUDA e Metal.

## Passo 3: Scaricare/Preparare il Modello e il Tokenizer

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

Utilizziamo il file `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` per tokenizzare il nostro testo di input. Una volta scaricato, il modello viene memorizzato nella cache, quindi la prima esecuzione sarà lenta (poiché scarica i 2,4 GB del modello), ma le esecuzioni successive saranno più veloci.

## Passo 4: Caricare il Modello

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Carichiamo i pesi quantizzati del modello in memoria e inizializziamo il modello Phi-3. Questo passaggio comporta la lettura dei pesi del modello dal file `gguf` e la configurazione del modello per l'inferenza sul dispositivo specificato (in questo caso la CPU).

## Passo 5: Elaborare il Prompt e Prepararlo per l'Inferenza

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

In questo passaggio, tokenizziamo il prompt di input e lo prepariamo per l'inferenza convertendolo in una sequenza di ID token. Inizializziamo anche i valori `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Ogni token viene convertito in un tensore e passato attraverso il modello per ottenere i logits.

Il ciclo elabora ogni token nel prompt, aggiornando il logits processor e preparando il token successivo per la generazione.

## Passo 6: Inferenza

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

Nel ciclo di inferenza, generiamo i token uno alla volta fino a raggiungere la lunghezza desiderata o incontrare il token di fine sequenza. Il token successivo viene convertito in un tensore e passato attraverso il modello, mentre i logits vengono elaborati per applicare penalità e campionamento. Successivamente, il token seguente viene campionato, decodificato e aggiunto alla sequenza.
Per evitare testi ripetitivi, viene applicata una penalità ai token ripetuti in base ai parametri `repeat_last_n` and `repeat_penalty`.

Infine, il testo generato viene stampato man mano che viene decodificato, garantendo un output in tempo reale.

## Passo 7: Eseguire l'Applicazione

Per eseguire l'applicazione, utilizza il seguente comando nel terminale:

```bash
cargo run --release
```

Questo dovrebbe stampare un haiku sull'hockey su ghiaccio generato dal modello Phi-3. Ad esempio:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

oppure

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusione

Seguendo questi passaggi, possiamo generare testo utilizzando il modello Phi-3 con Rust e Candle in meno di 100 righe di codice. Il codice gestisce il caricamento del modello, la tokenizzazione e l'inferenza, sfruttando tensori e elaborazione dei logits per generare testo coerente basato sul prompt di input.

Questa applicazione console può essere eseguita su Windows, Linux e macOS. Grazie alla portabilità di Rust, il codice può anche essere adattato a una libreria che potrebbe essere eseguita all'interno di app mobili (dato che le app console non possono essere eseguite lì, ovviamente).

## Appendice: codice completo

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

Nota: per eseguire questo codice su Linux aarch64 o Windows aarch64, aggiungi un file denominato `.cargo/config` con il seguente contenuto:

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

> Puoi visitare il repository ufficiale degli [esempi di Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) per ulteriori esempi su come utilizzare il modello Phi-3 con Rust e Candle, incluse approcci alternativi per l'inferenza.

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.