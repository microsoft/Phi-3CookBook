# Plattformübergreifende Inferenz mit Rust

Dieses Tutorial führt uns durch den Prozess der Inferenz mit Rust und dem [Candle ML-Framework](https://github.com/huggingface/candle) von HuggingFace. Die Verwendung von Rust für Inferenz bietet mehrere Vorteile, insbesondere im Vergleich zu anderen Programmiersprachen. Rust ist bekannt für seine hohe Leistung, vergleichbar mit der von C und C++. Das macht es zu einer ausgezeichneten Wahl für rechenintensive Inferenzaufgaben. Insbesondere liegt dies an den Zero-Cost-Abstraktionen und der effizienten Speicherverwaltung, die ohne Overhead durch Garbage Collection auskommt. Die plattformübergreifenden Fähigkeiten von Rust ermöglichen die Entwicklung von Code, der auf verschiedenen Betriebssystemen wie Windows, macOS und Linux sowie mobilen Betriebssystemen läuft, ohne dass wesentliche Änderungen am Code erforderlich sind.

Die Voraussetzung für dieses Tutorial ist die [Installation von Rust](https://www.rust-lang.org/tools/install), die den Rust-Compiler und Cargo, den Paketmanager von Rust, umfasst.

## Schritt 1: Neues Rust-Projekt erstellen

Um ein neues Rust-Projekt zu erstellen, führen Sie den folgenden Befehl im Terminal aus:

```bash
cargo new phi-console-app
```

Dies generiert eine anfängliche Projektstruktur mit einer `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`-Datei:

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

## Schritt 2: Grundlegende Parameter konfigurieren

In der Datei main.rs legen wir die Anfangsparameter für unsere Inferenz fest. Diese werden aus Einfachheitsgründen fest codiert, können aber nach Bedarf angepasst werden.

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

- **temperature**: Steuert die Zufälligkeit des Sampling-Prozesses.
- **sample_len**: Gibt die maximale Länge des generierten Textes an.
- **top_p**: Wird für das Nucleus-Sampling verwendet, um die Anzahl der für jeden Schritt berücksichtigten Tokens zu begrenzen.
- **repeat_last_n**: Legt fest, wie viele Tokens berücksichtigt werden, um eine Strafe für wiederholte Sequenzen anzuwenden.
- **repeat_penalty**: Der Strafwert, um wiederholte Tokens zu entmutigen.
- **seed**: Ein zufälliger Seed (wir könnten einen konstanten Wert verwenden, um die Reproduzierbarkeit zu verbessern).
- **prompt**: Der anfängliche Eingabetext, um die Generierung zu starten. Beachten Sie, dass wir das Modell bitten, ein Haiku über Eishockey zu generieren, und dass wir es mit speziellen Tokens umschließen, um die Benutzer- und Assistentenrollen im Gespräch anzugeben. Das Modell wird dann das Haiku vervollständigen.
- **device**: In diesem Beispiel verwenden wir die CPU für die Berechnungen. Candle unterstützt auch die Ausführung auf GPUs mit CUDA und Metal.

## Schritt 3: Modell und Tokenizer herunterladen/vorbereiten

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

Wir verwenden die Datei `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json`, um unseren Eingabetext zu tokenisieren. Sobald das Modell heruntergeladen ist, wird es zwischengespeichert. Die erste Ausführung könnte daher langsam sein (da 2,4 GB des Modells heruntergeladen werden), aber nachfolgende Ausführungen sind schneller.

## Schritt 4: Modell laden

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Wir laden die quantisierten Modellgewichte in den Speicher und initialisieren das Phi-3-Modell. Dieser Schritt umfasst das Lesen der Modellgewichte aus der `gguf`-Datei und die Einrichtung des Modells für die Inferenz auf dem angegebenen Gerät (in diesem Fall die CPU).

## Schritt 5: Prompt verarbeiten und für Inferenz vorbereiten

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

In diesem Schritt tokenisieren wir den Eingabe-Prompt und bereiten ihn für die Inferenz vor, indem wir ihn in eine Sequenz von Token-IDs umwandeln. Wir initialisieren auch die `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`-Werte. Jedes Token wird in einen Tensor umgewandelt und durch das Modell geleitet, um die Logits zu erhalten.

Die Schleife verarbeitet jedes Token im Prompt, aktualisiert den Logits-Processor und bereitet das nächste Token für die Generierung vor.

## Schritt 6: Inferenz

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

In der Inferenzschleife generieren wir Tokens einzeln, bis wir die gewünschte Länge erreicht haben oder das End-of-Sequence-Token auftritt. Das nächste Token wird in einen Tensor umgewandelt und durch das Modell geleitet, während die Logits verarbeitet werden, um Strafen und Sampling anzuwenden. Anschließend wird das nächste Token gesampelt, dekodiert und an die Sequenz angehängt. 

Um sich wiederholenden Text zu vermeiden, wird eine Strafe auf wiederholte Tokens basierend auf den Parametern `repeat_last_n` and `repeat_penalty` angewendet.

Schließlich wird der generierte Text während des Decodierens ausgegeben, um eine gestreamte Echtzeitausgabe zu gewährleisten.

## Schritt 7: Anwendung ausführen

Um die Anwendung auszuführen, führen Sie den folgenden Befehl im Terminal aus:

```bash
cargo run --release
```

Dies sollte ein Haiku über Eishockey ausgeben, das vom Phi-3-Modell generiert wurde. Zum Beispiel:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

oder

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Fazit

Durch die Befolgung dieser Schritte können wir mit dem Phi-3-Modell Textgenerierung mit Rust und Candle in weniger als 100 Zeilen Code durchführen. Der Code behandelt das Laden des Modells, die Tokenisierung und die Inferenz, indem er Tensoren und Logits-Prozesse nutzt, um kohärenten Text basierend auf dem Eingabe-Prompt zu generieren.

Diese Konsolenanwendung kann unter Windows, Linux und macOS ausgeführt werden. Aufgrund der Portabilität von Rust kann der Code auch an eine Bibliothek angepasst werden, die in mobilen Apps läuft (da wir dort keine Konsolenanwendungen ausführen können).

## Anhang: Vollständiger Code

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

Hinweis: Um diesen Code auf aarch64 Linux oder aarch64 Windows auszuführen, fügen Sie eine Datei mit dem Namen `.cargo/config` mit folgendem Inhalt hinzu:

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

> Besuchen Sie das offizielle [Candle-Beispiele](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)-Repository, um weitere Beispiele zur Verwendung des Phi-3-Modells mit Rust und Candle zu finden, einschließlich alternativer Ansätze für die Inferenz.

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.