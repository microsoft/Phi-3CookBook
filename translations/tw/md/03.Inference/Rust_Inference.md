# 使用 Rust 進行跨平台推理

本教程將引導我們使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 進行推理。使用 Rust 進行推理有多種優勢，尤其是與其他編程語言相比。Rust 以其高性能著稱，可媲美 C 和 C++，這使其成為計算密集型推理任務的理想選擇。這主要得益於其零成本抽象和高效的內存管理，沒有垃圾回收的開銷。Rust 的跨平台能力允許我們開發能在多種操作系統（包括 Windows、macOS 和 Linux 以及移動操作系統）上運行的代碼，而無需對代碼庫進行重大更改。

要跟隨本教程，首先需要 [安裝 Rust](https://www.rust-lang.org/tools/install)，這包括 Rust 編譯器和包管理器 Cargo。

## 第一步：創建一個新的 Rust 項目

要創建一個新的 Rust 項目，在終端中運行以下命令：

```bash
cargo new phi-console-app
```

這將生成一個初始項目結構，包含 `Cargo.toml` 文件和 `src/main.rs` 文件：

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

## 第二步：配置基本參數

在 main.rs 文件中，我們將設置推理的初始參數。為了簡化起見，這些參數都將被硬編碼，但我們可以根據需要進行修改。

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
- **sample_len**：指定生成文本的最大長度。
- **top_p**：用於核採樣以限制每一步考慮的標記數量。
- **repeat_last_n**：控制應用懲罰以防止重複序列時考慮的標記數量。
- **repeat_penalty**：用於懲罰重複標記的值。
- **seed**：隨機種子（我們可以使用常數值以提高可重現性）。
- **prompt**：生成開始的初始提示文本。注意我們請模型生成一首關於冰球的俳句，並用特殊標記包裹以指示用戶和助手的對話部分。模型將完成提示生成俳句。
- **device**：在本示例中我們使用 CPU 進行計算。Candle 支持使用 CUDA 和 Metal 在 GPU 上運行。

## 第三步：下載/準備模型和分詞器

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

我們使用 `hf_hub` 來下載模型文件。模型文件是量化的 `gguf` 文件，而 `tokenizer.json` 文件則用於分詞輸入文本。模型下載後會被緩存，因此首次執行會較慢（因為需要下載 2.4GB 的模型），但隨後的執行會更快。

## 第四步：加載模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我們將量化的模型權重加載到內存中並初始化 Phi-3 模型。這一步涉及從 `gguf` 文件中讀取模型權重並設置模型在指定設備（在本例中為 CPU）上進行推理。

## 第五步：處理提示並準備推理

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

在這一步中，我們將輸入提示進行分詞並準備推理，將其轉換為標記 ID 序列。我們還初始化 `LogitsProcessor` 以設置 `temperature` 和 `top_p` 值。每個標記都被轉換為張量並通過模型獲取 logits。

循環處理提示中的每個標記，更新 logits 處理器並準備生成下一個標記。

## 第六步：推理

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

在推理循環中，我們一個一個地生成標記，直到達到所需的樣本長度或遇到序列結束標記。下一個標記被轉換為張量並通過模型處理，同時對 logits 進行處理以應用懲罰和採樣。然後下一個標記被採樣、解碼並附加到序列中。
為了避免重複文本，根據 `repeat_last_n` 和 `repeat_penalty` 參數對重複標記應用懲罰。

最後，生成的文本在解碼後即時打印，確保實時輸出。

## 第七步：運行應用程序

要運行應用程序，在終端中執行以下命令：

```bash
cargo run --release
```

這應該會打印出由 Phi-3 模型生成的一首關於冰球的俳句。類似於：

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

通過這些步驟，我們可以在不到 100 行代碼中使用 Rust 和 Candle 進行文本生成。該代碼處理模型加載、分詞和推理，利用張量和 logits 處理生成基於輸入提示的連貫文本。

此控制台應用程序可以在 Windows、Linux 和 Mac OS 上運行。由於 Rust 的可移植性，代碼也可以適配為在移動應用程序內運行的庫（畢竟，我們無法在那裡運行控制台應用程序）。

## 附錄：完整代碼

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

注意：為了在 aarch64 Linux 或 aarch64 Windows 上運行此代碼，添加一個名為 `.cargo/config` 的文件，內容如下：

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

> 您可以訪問官方 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 存儲庫，獲取更多關於如何使用 Rust 和 Candle 進行 Phi-3 模型推理的示例，包括替代推理方法。

**免責聲明**:
本文件使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的文件為權威來源。對於關鍵信息，建議進行專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀不承擔責任。