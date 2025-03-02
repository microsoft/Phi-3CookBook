# Cross-platform inferentie met Rust

Deze tutorial begeleidt ons door het proces van inferentie uitvoeren met behulp van Rust en het [Candle ML-framework](https://github.com/huggingface/candle) van HuggingFace. Het gebruik van Rust voor inferentie biedt verschillende voordelen, vooral in vergelijking met andere programmeertalen. Rust staat bekend om zijn hoge prestaties, vergelijkbaar met die van C en C++. Dit maakt het een uitstekende keuze voor inferentietaken, die vaak veel rekenkracht vereisen. Dit wordt met name mogelijk gemaakt door de zero-cost abstractions en efficiënte geheugenbeheer, zonder de overhead van garbage collection. Dankzij de cross-platform mogelijkheden van Rust kan code worden ontwikkeld die werkt op verschillende besturingssystemen, waaronder Windows, macOS en Linux, evenals mobiele besturingssystemen, zonder dat er aanzienlijke aanpassingen aan de code nodig zijn.

De vereiste om deze tutorial te volgen, is om [Rust te installeren](https://www.rust-lang.org/tools/install), inclusief de Rust-compiler en Cargo, de pakketbeheerder van Rust.

## Stap 1: Maak een nieuw Rust-project aan

Om een nieuw Rust-project aan te maken, voer je het volgende commando uit in de terminal:

```bash
cargo new phi-console-app
```

Dit genereert een initiële projectstructuur met een `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` bestand:

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

## Stap 2: Stel basisparameters in

In het bestand main.rs stellen we de initiële parameters in voor onze inferentie. Deze worden voor de eenvoud hardcoded, maar kunnen naar wens worden aangepast.

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

- **temperature**: Bepaalt de willekeurigheid van het samplingproces.
- **sample_len**: Geeft de maximale lengte van de gegenereerde tekst aan.
- **top_p**: Wordt gebruikt voor nucleus sampling om het aantal tokens te beperken dat bij elke stap wordt overwogen.
- **repeat_last_n**: Bepaalt het aantal tokens dat in aanmerking wordt genomen voor het toepassen van een straf om herhalende sequenties te voorkomen.
- **repeat_penalty**: De strafwaarde om herhaalde tokens te ontmoedigen.
- **seed**: Een willekeurige seed (we kunnen een constante waarde gebruiken voor betere reproduceerbaarheid).
- **prompt**: De initiële prompttekst om de generatie te starten. Merk op dat we het model vragen een haiku over ijshockey te genereren, en dat we het omgeven met speciale tokens om de delen van de gebruiker en de assistent in het gesprek aan te geven. Het model zal vervolgens de prompt aanvullen met een haiku.
- **device**: In dit voorbeeld gebruiken we de CPU voor berekeningen. Candle ondersteunt ook gebruik op GPU met CUDA en Metal.

## Stap 3: Download/Prepareer Model en Tokenizer

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

We gebruiken het `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` bestand voor het tokeniseren van onze invoertekst. Nadat het model is gedownload, wordt het in cache opgeslagen. De eerste uitvoering kan daardoor traag zijn (omdat het model van 2,4 GB wordt gedownload), maar latere uitvoeringen zullen sneller zijn.

## Stap 4: Laad Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

We laden de gekwantiseerde modelgewichten in het geheugen en initialiseren het Phi-3 model. Deze stap omvat het lezen van de modelgewichten uit het `gguf` bestand en het klaarmaken van het model voor inferentie op het opgegeven apparaat (in dit geval de CPU).

## Stap 5: Verwerk Prompt en Bereid Voor op Inferentie

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

In deze stap tokeniseren we de invoerprompt en maken we deze klaar voor inferentie door deze om te zetten in een reeks token-ID's. We initialiseren ook de `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` waarden. Elk token wordt omgezet in een tensor en door het model gehaald om de logits te verkrijgen.

De lus verwerkt elk token in de prompt, werkt de logits-processor bij en bereidt zich voor op de generatie van het volgende token.

## Stap 6: Inferentie

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

In de inferentielus genereren we tokens één voor één totdat we de gewenste samplelengte bereiken of het einde-van-sequentie-token tegenkomen. Het volgende token wordt omgezet in een tensor en door het model gehaald, terwijl de logits worden verwerkt om straffen en sampling toe te passen. Vervolgens wordt het volgende token gesampled, gedecodeerd en aan de sequentie toegevoegd.  
Om herhalende tekst te voorkomen, wordt een straf toegepast op herhaalde tokens op basis van de `repeat_last_n` and `repeat_penalty` parameters.

Tot slot wordt de gegenereerde tekst afgedrukt terwijl deze wordt gedecodeerd, wat zorgt voor een realtime uitvoer.

## Stap 7: Voer de Applicatie Uit

Om de applicatie uit te voeren, voer je het volgende commando uit in de terminal:

```bash
cargo run --release
```

Dit zou een haiku over ijshockey moeten genereren met behulp van het Phi-3 model. Bijvoorbeeld:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

of

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusie

Door deze stappen te volgen, kunnen we tekstgeneratie uitvoeren met het Phi-3 model met Rust en Candle in minder dan 100 regels code. De code behandelt het laden van het model, tokenisatie en inferentie, waarbij tensors en logits-verwerking worden gebruikt om samenhangende tekst te genereren op basis van de invoerprompt.

Deze console-applicatie kan draaien op Windows, Linux en Mac OS. Dankzij de draagbaarheid van Rust kan de code ook worden aangepast tot een bibliotheek die binnen mobiele apps zou kunnen draaien (we kunnen daar immers geen console-apps uitvoeren).

## Appendix: volledige code

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

Opmerking: om deze code uit te voeren op aarch64 Linux of aarch64 Windows, voeg een bestand genaamd `.cargo/config` toe met de volgende inhoud:

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

> Je kunt de officiële [Candle voorbeelden](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository bezoeken voor meer voorbeelden over hoe je het Phi-3 model kunt gebruiken met Rust en Candle, inclusief alternatieve benaderingen voor inferentie.

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, moet u zich ervan bewust zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.