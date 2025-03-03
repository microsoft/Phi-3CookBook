# 使用 Rust 进行跨平台推理

本教程将带领我们通过 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 使用 Rust 执行推理任务。使用 Rust 进行推理有许多优势，特别是与其他编程语言相比。Rust 以其高性能著称，性能可与 C 和 C++ 媲美。这使其成为计算密集型推理任务的绝佳选择。特别是因为 Rust 提供零成本抽象和高效的内存管理，没有垃圾回收的开销。此外，Rust 的跨平台特性使得开发的代码可以在包括 Windows、macOS、Linux，以及移动操作系统等各种操作系统上运行，而无需对代码库进行重大修改。

学习本教程的前提是[安装 Rust](https://www.rust-lang.org/tools/install)，其中包括 Rust 编译器和 Rust 包管理工具 Cargo。

## 第一步：创建一个新的 Rust 项目

在终端中运行以下命令以创建一个新的 Rust 项目：

```bash
cargo new phi-console-app
```

这将生成一个初始的项目结构，其中包含 `Cargo.toml` 文件和 `src/main.rs` 文件。我们还需要添加以下依赖项：`candle`、`hf-hub` 和 `tokenizers`。更新后的 `Cargo.toml` 文件如下：

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

## 第二步：配置基本参数

在 `main.rs` 文件中，我们将设置推理所需的初始参数。为了简单起见，这些参数将被硬编码，但我们可以根据需要修改它们。

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

- **temperature**：控制采样过程的随机性。
- **sample_len**：指定生成文本的最大长度。
- **top_p**：用于核采样，限制每一步考虑的 token 数量。
- **repeat_last_n**：控制为防止重复序列而施加惩罚时所考虑的 token 数量。
- **repeat_penalty**：用于抑制重复 token 的惩罚值。
- **seed**：随机种子（可以使用一个固定值以提高可重复性）。
- **prompt**：生成文本的初始提示。注意，我们要求模型生成一首关于冰球的俳句，并使用特殊的标记包装提示，以表示用户和助手之间的对话部分。模型随后将完成提示，生成俳句。
- **device**：本示例中使用 CPU 进行计算。Candle 也支持在 CUDA 和 Metal 的 GPU 上运行。

## 第三步：下载/准备模型和分词器

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

我们使用 `hf_hub` 下载模型文件，并加载 `gguf` 格式的量化模型权重。同时，我们需要一个 `tokenizer.json` 文件来对输入文本进行分词。一旦下载完成，模型会被缓存，因此首次执行可能较慢（需要下载 2.4GB 的模型文件），但后续执行会更快。

## 第四步：加载模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我们将量化的模型权重加载到内存中，并初始化 Phi-3 模型。这一步涉及从 `gguf` 文件中读取模型权重，并在指定的设备（本例中为 CPU）上设置推理模型。

## 第五步：处理提示并准备推理

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

在这一步中，我们对输入的提示进行分词，并将其转换为 token ID 序列，为推理做准备。同时，我们初始化 `LogitsProcessor`，并设置 `temperature` 和 `top_p` 参数。每个 token 都会被转换为张量，并传递给模型以获得 logits。

循环会处理提示中的每个 token，更新 logits 处理器，并为下一个 token 的生成做准备。

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

在推理循环中，我们逐个生成 token，直到达到指定的文本长度或遇到序列结束标记为止。下一个 token 会被转换为张量并传递给模型，同时 logits 会被处理以应用惩罚和采样。然后，采样出的下一个 token 会被解码并追加到序列中。

为了避免重复的文本，会根据 `repeat_last_n` 和 `repeat_penalty` 参数对重复的 token 施加惩罚。

最后，生成的文本会被解码并实时打印输出。

## 第七步：运行应用程序

在终端中执行以下命令以运行应用程序：

```bash
cargo run --release
```

这将生成一首关于冰球的俳句，使用 Phi-3 模型生成的结果可能类似于：

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

## 总结

通过以上步骤，我们可以使用 Rust 和 Candle 在不到 100 行代码中完成基于 Phi-3 模型的文本生成。代码涵盖了模型加载、分词和推理，利用张量和 logits 处理器生成基于输入提示的连贯文本。

该控制台应用程序可以在 Windows、Linux 和 macOS 上运行。由于 Rust 的可移植性，代码也可以被改编为一个库，以便在移动应用程序中运行（毕竟，我们无法在移动设备上运行控制台应用程序）。

## 附录：完整代码

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

注意：如果要在 aarch64 Linux 或 aarch64 Windows 上运行此代码，请添加一个名为 `.cargo/config` 的文件，内容如下：

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

> 您可以访问官方 [Candle 示例](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 仓库，了解更多关于使用 Rust 和 Candle 的 Phi-3 模型的示例，包括推理的替代方法。

**免责声明**：  
本文件通过基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议使用专业的人类翻译服务。我们对于因使用本翻译而导致的任何误解或误读不承担责任。