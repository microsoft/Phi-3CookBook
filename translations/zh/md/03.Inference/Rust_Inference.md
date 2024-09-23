# 使用 Rust 进行跨平台推理

本教程将引导我们使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 进行推理。使用 Rust 进行推理有很多优势，尤其是与其他编程语言相比。Rust 以其高性能而闻名，性能可与 C 和 C++ 相媲美。这使得它成为计算密集型推理任务的绝佳选择。特别是由于零成本抽象和高效的内存管理，没有垃圾回收开销。Rust 的跨平台能力使得代码可以在包括 Windows、macOS 和 Linux 在内的各种操作系统上运行，甚至是移动操作系统，而无需对代码库进行重大更改。

在开始本教程之前，需要 [安装 Rust](https://www.rust-lang.org/tools/install)，这包括 Rust 编译器和包管理器 Cargo。

## 步骤 1：创建一个新的 Rust 项目

在终端中运行以下命令以创建一个新的 Rust 项目：

```bash
cargo new phi-console-app
```

这将生成一个初始项目结构，包括一个 `Cargo.toml` 文件和一个包含 `main.rs` 文件的 `src` 目录。

接下来，我们将把 `candle`、`hf-hub` 和 `tokenizers` crates 添加到 `Cargo.toml` 文件中：

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

## 步骤 2：配置基本参数

在 `main.rs` 文件中，我们将设置推理的初始参数。为了简化起见，这些参数将全部硬编码，但我们可以根据需要进行修改。

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
- **top_p**：用于核采样，以限制每一步考虑的 token 数量。
- **repeat_last_n**：控制应用惩罚以防止重复序列的 token 数量。
- **repeat_penalty**：惩罚值，以防止重复的 token。
- **seed**：一个随机种子（我们可以使用一个常量值以提高可重复性）。
- **prompt**：生成文本的初始提示。请注意，我们要求模型生成关于冰球的俳句，并使用特殊的 token 来表示用户和助手的对话部分。模型将根据提示完成俳句。
- **device**：在本例中我们使用 CPU 进行计算。Candle 还支持使用 CUDA 和 Metal 在 GPU 上运行。

## 步骤 3：下载/准备模型和分词器

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

我们使用 `hf_hub` API 从 Hugging Face 模型库中下载模型和分词器文件。`gguf` 文件包含量化后的模型权重，而 `tokenizer.json` 文件用于分词我们的输入文本。下载后模型会被缓存，因此第一次执行会比较慢（因为需要下载 2.4GB 的模型），但后续执行会更快。

## 步骤 4：加载模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我们将量化后的模型权重加载到内存中，并初始化 Phi-3 模型。这一步涉及从 `gguf` 文件中读取模型权重，并在指定设备（在本例中为 CPU）上设置模型以进行推理。

## 步骤 5：处理提示并准备推理

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

在这一步中，我们将输入提示进行分词，并将其转换为一系列 token ID 以准备推理。我们还初始化了 `LogitsProcessor` 以根据给定的 `temperature` 和 `top_p` 值处理采样过程（对词汇表的概率分布）。每个 token 都被转换为张量并传递给模型以获取 logits。

循环处理提示中的每个 token，更新 logits 处理器并为下一个 token 生成做准备。

## 步骤 6：推理

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

在推理循环中，我们一个一个地生成 token，直到达到所需的样本长度或遇到序列结束 token。下一个 token 被转换为张量并传递给模型，同时对 logits 进行处理以应用惩罚和采样。然后下一个 token 被采样、解码并附加到序列中。
为了避免重复文本，会根据 `repeat_last_n` 和 `repeat_penalty` 参数对重复的 token 进行惩罚。

最后，生成的文本在解码时被打印出来，确保实时输出。

## 步骤 7：运行应用程序

在终端中执行以下命令以运行应用程序：

```bash
cargo run --release
```

这应该会打印出由 Phi-3 模型生成的关于冰球的俳句。例如：

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

或者

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 结论

通过遵循这些步骤，我们可以使用 Rust 和 Candle 在不到 100 行代码中进行文本生成。代码处理模型加载、分词和推理，利用张量和 logits 处理生成基于输入提示的连贯文本。

这个控制台应用程序可以在 Windows、Linux 和 Mac OS 上运行。由于 Rust 的可移植性，代码还可以适配为在移动应用程序中运行的库（毕竟我们不能在移动设备上运行控制台应用程序）。

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
    // 1. 配置基本参数
    let temperature: f64 = 1.0;
    let sample_len: usize = 100;
    let top_p: Option<f64> = None;
    let repeat_last_n: usize = 64;
    let repeat_penalty: f32 = 1.2;
    let mut rng = rand::thread_rng();
    let seed: u64 = rng.gen();
    let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";

    // 我们将仅在 CPU 上运行
    let device = Device::Cpu;

    // 2. 下载/准备模型和分词器
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

    // 3. 加载模型
    let mut file = std::fs::File::open(&model_path)?;
    let model_content = gguf_file::Content::read(&mut file)?;
    let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;

    // 4. 处理提示并准备推理
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

        // 仅为提示中的最后一个 token 采样下一个 token
        if pos == tokens.len() - 1 {
            next_token = logits_processor.sample(&logits)?;
            all_tokens.push(next_token);
        }
    }

    // 5. 推理
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

        // 解码当前的 token 序列
        let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

        // 仅打印解码文本的新部分
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

> 您可以访问官方 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 仓库，了解更多关于如何使用 Rust 和 Candle 进行 Phi-3 模型推理的示例，包括其他推理方法。

免责声明：此翻译由AI模型从原文翻译而来，可能并不完美。请审阅输出内容并进行必要的修改。