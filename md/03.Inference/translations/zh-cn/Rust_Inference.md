# 使用 Rust 进行跨平台推理

本教程将指导我们使用 Rust 和 HuggingFace 的 [Candle ML 框架](https://github.com/huggingface/candle) 进行推理。与其他编程语言相比，使用Rust进行推理具有诸多优势。Rust以其高性能而闻名，可与C和C++相媲美。这使得Rust成为执行计算密集型推理任务的理想选择。特别指出的是，这归功于零成本抽象和高效的内存管理，使其没有垃圾收集开销。Rust的跨平台功能使得可以开发在各种操作系统上运行的代码，包括Windows、macOS和Linux，以及移动操作系统，而无需对代码库进行重大更改。

要遵循本教程的先决条件是 [安装 Rust](https://www.rust-lang.org/tools/install), 其中包括Rust编译器和Cargo，Rust的包管理器。

## Step 1: 创建一个新的 Rust 项目

要创建一个新的Rust项目，在终端运行以下命令:

```bash
cargo new phi-console-app
```

这将生成一个初始项目结构，具有 `Cargo.toml` 文件和一个 `src` 目录，包含了名为 `main.rs` 的文件.

接下来，我们将添加依赖 - 也就是给 `Cargo.toml` 文件添加 `candle`、 `hf-hub` 和 `tokenizers`:

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

## Step 2: 配置基本参数

在 `main.rs` 文件中，我们将为推理设置初始参数。为简单起见，这些参数都将被硬编码，但我们可以根据需要修改它们。

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

- **temperature**: 控制采样过程的随机性。
- **sample_len**: 规定了生成文本的最大长度。
- **top_p**: 用于核采样，以限制每一步考虑的令牌数量。
- **repeat_last_n**: 控制token的数量，使用该惩罚机制来防止重复内容的产生。
- **repeat_penalty**: 阻止产生重复 token 的惩罚值。
- **seed**: 一个随机数的种子(为了更好的再现性，我们可以使用一个常数值)。
- **prompt**: 初始提示文本，用于开始本文的生成。请注意，我们要求模型生成关于冰球的短诗，并用特殊的token将其包裹起来以表示对话中的用户和助手部分。然后，模型将用短诗来回应用户的提示。
- **device**: 在此示例中，我们使用CPU进行计算。Candle还支持使用CUDA和Metal在GPU上运行。

## Step 3: 下载/准备 模型和分词器

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

我们使用 `hf_hub` API 来从 Hugging Face 的模型中心下载模型和分词器文件。 `gguf` 文件包含量化的模型权重，而 `tokenizer.json` 文件用于对输入文本进行分词操作。一旦下载了模型，它就会被缓存，因此第一次执行速度会较慢（因为需要下载2.4GB的模型），但后续执行速度会更快。

## Step 4: 加载模型

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

我们将量化的模型权重加载到内存中，并初始化Phi-3模型。这个步骤包括从 `gguf` 文件中读取模型权重，并在指定的设备上（在本例中为CPU）设置模型以进行推理。

## Step 5: 处理提示词并准备推理

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

在这一步中，我们对输入的提示进行分词，并通过将其转换为一系列token ID来准备好进行推理。我们还初始化 `LogitsProcessor` 以处理基于给定的 `temperature` 和 `top_p` 值的采样过程（词汇表上的概率分布）。每个token都被转换为一个张量，并通过模型获得logits。

这个循环处理提示中的每个token，更新logits处理器并为下一个token生成做准备。

## Step 6: 推理

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

在推理循环中，我们逐个生成token，直到达到所需的样本长度或遇到序列结束的token。下一个token被转换为张量并通过模型传递，同时处理logits以应用惩罚和采样。然后，对下一个token进行采样、解码并将其追加到序列中。
为了避免重复的文本，根据 `repeat_last_n` 和 `repeat_penalty` 参数对重复的token应用惩罚。

最后，生成的文本在解码时打印出来，确保实时的流式输出。

## Step 7: 运行应用程序

要运行应用程序，请在终端中执行以下命令:

```bash
cargo run --release
```

运行该命令后，将会输出由 Phi-3 模型生成的关于冰球的短诗，例如:

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

## 总结

通过遵循这些步骤，我们可以使用不到100行代码实现Rust和Candle的Phi-3模型进行文本生成。代码处理模型加载、分词化（tokenization）和推理，利用张量和logits处理来根据输入提示生成连贯的文本。

这个控制台应用程序可以在Windows、Linux和Mac OS上运行。由于Rust的可移植性，这段代码也可以被应用到一个可以在移动应用程序中运行的库（毕竟在移动设备上我们无法运行控制台应用程序）。

## 附录: 完整代码

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

注意: 为了在aarch64 Linux或aarch64 Windows上运行此代码，添加一个名为 `.cargo/config` 的文件，包含以下代码:

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

> 您可以访问官方的 [Candle 示例](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 代码库获得更多的信息，学习如何使用 Rust 和 Candle 接入 Phi-3 模型，其中包含了可供选择的推理方法。
