# 使用 Rust 進行跨平台推理

本教學將帶領我們使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 進行推理操作。使用 Rust 進行推理有多項優勢，特別是與其他程式語言相比時。Rust 以其高效能著稱，效能可與 C 和 C++ 相媲美，這使其成為處理計算密集型推理任務的絕佳選擇。這主要得益於零成本抽象和高效的記憶體管理，且沒有垃圾回收的負擔。此外，Rust 的跨平台能力允許開發的程式碼能在 Windows、macOS 和 Linux 等多種作業系統，以及行動作業系統上執行，而無需對程式碼進行重大更改。

學習本教學的前提是 [安裝 Rust](https://www.rust-lang.org/tools/install)，其中包括 Rust 編譯器和 Rust 套件管理工具 Cargo。

## 步驟 1：建立一個新的 Rust 專案

在終端機中執行以下指令來建立一個新的 Rust 專案：

```bash
cargo new phi-console-app
```

這會生成一個初始的專案結構，包含 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` 文件：

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

## 步驟 2：設定基本參數

在 main.rs 文件中，我們將設定推理所需的初始參數。為了簡單起見，這些參數將以硬編碼的方式設定，但我們可以根據需求進行修改。

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

- **temperature**：控制採樣過程的隨機性。
- **sample_len**：指定生成文字的最大長度。
- **top_p**：用於核採樣，限制每一步考慮的 token 數量。
- **repeat_last_n**：控制應用懲罰以避免重複序列時考慮的 token 數量。
- **repeat_penalty**：懲罰值，用於抑制重複的 token。
- **seed**：隨機種子（可以使用固定值以提高重現性）。
- **prompt**：生成的初始提示文字。我們要求模型生成一首關於冰球的俳句，並使用特殊標記包裹提示，表示對話中使用者和助手的部分。模型將根據提示補全俳句。
- **device**：在本範例中，我們使用 CPU 進行計算。Candle 支援使用 CUDA 和 Metal 在 GPU 上運行。

## 步驟 3：下載/準備模型和分詞器

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

我們使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 文件來對輸入文字進行分詞。模型下載後會被快取，因此第一次執行時會較慢（因為需要下載 2.4GB 的模型），但之後的執行速度會更快。

## 步驟 4：載入模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化的模型權重載入記憶體並初始化 Phi-3 模型。此步驟包括從 `gguf` 文件中讀取模型權重，並在指定的設備（此例為 CPU）上設置模型以進行推理。

## 步驟 5：處理提示並準備推理

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

在這一步中，我們對輸入的提示進行分詞，並將其轉換為 token ID 序列以準備推理。我們也初始化了 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 值。每個 token 都會被轉換為張量，並通過模型獲取 logits。

這個循環會處理提示中的每個 token，更新 logits 處理器並為下一個 token 的生成做準備。

## 步驟 6：推理

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

在推理迴圈中，我們逐個生成 token，直到達到指定的樣本長度或遇到序列結束的 token。下一個 token 會被轉換為張量並通過模型處理，同時對 logits 應用懲罰和採樣。然後下一個 token 被抽樣、解碼並附加到序列中。

為了避免重複的文字，根據 `repeat_last_n` and `repeat_penalty` 參數對重複的 token 施加懲罰。

最後，生成的文字會在解碼後即時輸出。

## 步驟 7：執行應用程式

在終端機中執行以下指令以運行應用程式：

```bash
cargo run --release
```

這應該會生成一首關於冰球的俳句，由 Phi-3 模型生成。例如：

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

或

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 結論

透過這些步驟，我們可以使用 Rust 和 Candle 在不到 100 行程式碼中實現 Phi-3 模型的文字生成。程式碼涵蓋了模型載入、分詞和推理，利用張量和 logits 處理生成基於輸入提示的連貫文字。

這個終端應用程式可以在 Windows、Linux 和 Mac OS 上運行。由於 Rust 的可移植性，這段程式碼也可以改造成一個庫，用於在行動應用中執行（畢竟我們無法在行動設備上執行終端應用）。

## 附錄：完整程式碼

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

注意：若要在 aarch64 Linux 或 aarch64 Windows 上運行此程式碼，需新增一個名為 `.cargo/config` 的文件，內容如下：

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

> 您可以造訪官方的 [Candle 範例](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 資源庫，瞭解更多關於使用 Rust 和 Candle 進行 Phi-3 模型推理的範例，包括其他推理方法。

**免責聲明**：  
本文件是使用機器翻譯人工智慧服務進行翻譯的。我們雖然努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。