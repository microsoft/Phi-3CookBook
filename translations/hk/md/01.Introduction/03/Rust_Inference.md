# 用 Rust 進行跨平台推理

本教學將帶大家了解如何使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 進行推理。使用 Rust 進行推理有很多好處，特別是與其他程式語言相比。Rust 以其高效能著稱，與 C 和 C++ 相當，這使其成為執行計算密集型推理任務的絕佳選擇。這主要得益於零成本抽象和高效的記憶體管理，沒有垃圾回收的額外負擔。此外，Rust 的跨平台特性讓開發者可以撰寫能在 Windows、macOS、Linux，以及行動作業系統上執行的程式碼，而無需對程式碼庫進行重大修改。

學習本教學的前提是先[安裝 Rust](https://www.rust-lang.org/tools/install)，其中包含 Rust 編譯器和 Rust 套件管理工具 Cargo。

## 第 1 步：建立一個新的 Rust 專案

在終端機中執行以下指令來建立一個新的 Rust 專案：

```bash
cargo new phi-console-app
```

這會產生一個初始的專案結構，其中包含 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` 檔案：

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

## 第 2 步：設定基本參數

在 main.rs 檔案中，我們將設置推理所需的初始參數。為了簡化，我們會直接硬編碼這些參數，但可以根據需求進行修改。

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

- **temperature**：控制抽樣過程的隨機性。
- **sample_len**：指定生成文本的最大長度。
- **top_p**：用於核抽樣，限制每步考慮的 token 數量。
- **repeat_last_n**：控制用於防止重複序列的 token 數量。
- **repeat_penalty**：用於抑制重複 token 的懲罰值。
- **seed**：隨機種子（可以使用常數值以便於重現結果）。
- **prompt**：用於生成的初始提示文本。注意，我們請模型生成一首關於冰上曲棍球的俳句，並用特殊的 token 包裹提示，以表示使用者與助手的對話部分。模型接著會補全提示生成俳句。
- **device**：在此範例中，我們使用 CPU 進行運算。Candle 也支援使用 CUDA 和 Metal 在 GPU 上執行。

## 第 3 步：下載/準備模型和分詞器

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

我們使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 檔案來對輸入文本進行分詞。模型下載後會被快取，因此第一次執行會較慢（需要下載 2.4GB 的模型），但之後的執行速度會快得多。

## 第 4 步：載入模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化的模型權重載入記憶體，並初始化 Phi-3 模型。這一步包括從 `gguf` 檔案讀取模型權重，並在指定的裝置（此範例為 CPU）上設置模型以進行推理。

## 第 5 步：處理提示並準備推理

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

在這一步，我們將輸入的提示進行分詞，並轉換為 token ID 序列以準備推理。我們還初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 值。每個 token 都會被轉換為 tensor，並傳遞給模型以獲取 logits。

迴圈會處理提示中的每個 token，更新 logits 處理器，並準備下一個 token 的生成。

## 第 6 步：推理

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

在推理迴圈中，我們逐一生成 token，直到達到指定的樣本長度或遇到序列結束的 token。下一個 token 會被轉換為 tensor，傳遞給模型，並對 logits 進行處理以應用懲罰和抽樣。然後，下一個 token 會被抽樣、解碼，並附加到序列中。

為了避免重複文本，會根據 `repeat_last_n` and `repeat_penalty` 參數對重複的 token 應用懲罰。

最後，生成的文本會在解碼後打印出來，確保即時的流式輸出。

## 第 7 步：執行應用程式

在終端機中執行以下指令來執行應用程式：

```bash
cargo run --release
```

這應該會打印出由 Phi-3 模型生成的一首關於冰上曲棍球的俳句。例如：

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

透過這些步驟，我們可以使用 Phi-3 模型與 Rust 和 Candle 在不到 100 行程式碼中實現文本生成。程式碼處理了模型載入、分詞和推理，利用 tensor 和 logits 處理生成基於輸入提示的連貫文本。

此命令列應用程式可在 Windows、Linux 和 Mac OS 上執行。由於 Rust 的可移植性，程式碼也可以調整為能在行動應用程式內執行的函式庫（畢竟我們無法在行動裝置上執行命令列應用程式）。

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

注意：若要在 aarch64 Linux 或 aarch64 Windows 上執行此程式碼，請新增一個名為 `.cargo/config` 的檔案，內容如下：

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

> 您可以瀏覽官方的 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 資源庫，了解更多關於使用 Rust 和 Candle 進行 Phi-3 模型推理的範例，包括其他推理方法。

**免責聲明**:  
本文件經由機器人工智能翻譯服務翻譯而成。我們致力於追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文語言的文件作為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。