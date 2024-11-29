# 使用 Rust 进行跨平台推理

本教程将引导我们使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 进行推理。使用 Rust 进行推理具有多种优势，尤其是与其他编程语言相比。Rust 以其高性能而闻名，性能可与 C 和 C++ 相媲美。这使其成为计算密集型推理任务的绝佳选择。特别是，Rust 的零成本抽象和高效的内存管理，没有垃圾回收的开销。Rust 的跨平台功能使得可以开发在各种操作系统上运行的代码，包括 Windows、macOS 和 Linux 以及移动操作系统，而无需对代码库进行重大更改。

要跟随本教程，首先需要 [安装 Rust](https://www.rust-lang.org/tools/install)，其中包括 Rust 编译器和包管理器 Cargo。

## 第一步：创建一个新的 Rust 项目

在终端中运行以下命令来创建一个新的 Rust 项目：

```bash
cargo new phi-console-app
```

这将生成一个初始项目结构，其中包含一个 `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## 第二步：配置基本参数

在 main.rs 文件中，我们将设置推理的初始参数。为了简单起见，这些参数都将硬编码，但我们可以根据需要进行修改。

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
- **repeat_last_n**：控制应用惩罚以防止重复序列时考虑的 token 数量。
- **repeat_penalty**：惩罚值，用于抑制重复的 token。
- **seed**：一个随机种子（我们可以使用一个常量值以提高可重复性）。
- **prompt**：用于开始生成的初始提示文本。请注意，我们要求模型生成一首关于冰球的俳句，并用特殊标记包装它以指示对话的用户和助手部分。然后模型将用一首俳句完成提示。
- **device**：在本例中，我们使用 CPU 进行计算。Candle 也支持使用 CUDA 和 Metal 在 GPU 上运行。

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

我们使用 `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 文件来对输入文本进行分词。下载后模型会被缓存，因此第一次执行可能会很慢（因为需要下载 2.4GB 的模型），但后续执行将会更快。

## 第四步：加载模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我们将量化的模型权重加载到内存中并初始化 Phi-3 模型。这一步涉及从 `gguf` 文件中读取模型权重并在指定设备（在本例中为 CPU）上设置模型进行推理。

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

在这一步中，我们对输入提示进行分词，并将其转换为 token ID 序列以准备推理。我们还初始化 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 值。每个 token 被转换为张量并通过模型传递以获取 logits。

循环处理提示中的每个 token，更新 logits 处理器并为下一个 token 生成做准备。

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

在推理循环中，我们逐个生成 token，直到达到所需的样本长度或遇到序列结束 token。下一个 token 被转换为张量并通过模型传递，同时对 logits 进行处理以应用惩罚和采样。然后，下一个 token 被采样、解码并附加到序列中。
为了避免重复文本，根据 `repeat_last_n` and `repeat_penalty` 参数对重复的 token 施加惩罚。

最后，生成的文本在解码时被打印出来，确保实时输出。

## 第七步：运行应用程序

在终端中执行以下命令以运行应用程序：

```bash
cargo run --release
```

这将打印出由 Phi-3 模型生成的关于冰球的俳句。类似于：

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

## 结论

通过遵循这些步骤，我们可以在不到 100 行代码中使用 Rust 和 Candle 进行文本生成。代码处理模型加载、分词和推理，利用张量和 logits 处理生成基于输入提示的连贯文本。

此控制台应用程序可以在 Windows、Linux 和 Mac OS 上运行。由于 Rust 的可移植性，代码还可以适应为在移动应用程序中运行的库（毕竟我们无法在移动设备上运行控制台应用程序）。

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

注意：要在 aarch64 Linux 或 aarch64 Windows 上运行此代码，请添加一个名为 `.cargo/config` 的文件，内容如下：

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

> 您可以访问官方的 [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 仓库，了解更多关于如何使用 Rust 和 Candle 进行 Phi-3 模型推理的示例，包括推理的替代方法。

**免责声明**：
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误释，我们概不负责。