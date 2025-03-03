# Cross-platform inference with Rust

This tutorial walks you through the process of performing inference using Rust and the [Candle ML framework](https://github.com/huggingface/candle) from HuggingFace. Rust offers several advantages for inference tasks, particularly when compared to other programming languages. Known for its high performance, comparable to C and C++, Rust is an excellent choice for computationally intensive inference tasks. This is largely due to its zero-cost abstractions and efficient memory management, which operates without the overhead of garbage collection. Rust's cross-platform capabilities also allow you to develop code that runs on a variety of operating systems, including Windows, macOS, Linux, and even mobile platforms, without requiring significant changes to the codebase.

Before starting this tutorial, make sure to [install Rust](https://www.rust-lang.org/tools/install), which includes the Rust compiler and Cargo, the Rust package manager.

## Step 1: Create a New Rust Project

To create a new Rust project, execute the following command in the terminal:

```bash
cargo new phi-console-app
```

This will generate an initial project structure with a `Cargo.toml` file and a `src/main.rs` file. We will also include dependencies like `candle`, `hf-hub`, and `tokenizers` in the `Cargo.toml` file:

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

## Step 2: Configure Basic Parameters

In the `main.rs` file, we'll define the initial parameters for our inference. These parameters will be hardcoded for simplicity but can be adjusted as needed.

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

- **temperature**: Controls the randomness of the sampling process.
- **sample_len**: Specifies the maximum length of the generated text.
- **top_p**: Used for nucleus sampling to limit the number of tokens considered at each step.
- **repeat_last_n**: Determines how many tokens are considered when applying a penalty to discourage repetitive sequences.
- **repeat_penalty**: The penalty value to reduce the likelihood of repeated tokens.
- **seed**: A random seed (a fixed value can be used for reproducibility).
- **prompt**: The initial text prompt to start the generation. In this example, the prompt asks the model to generate a haiku about ice hockey, wrapped with special tokens to represent the user and assistant parts of the conversation. The model will complete the prompt with a haiku.
- **device**: In this example, we use the CPU for computation. Candle also supports GPU acceleration with CUDA and Metal.

## Step 3: Download/Prepare Model and Tokenizer

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

We use the `hf_hub` library to download the model and tokenizer. The `gguf` file contains the quantized model weights, while the `tokenizer.json` file is used for tokenizing the input text. The model is cached after downloading, so the first execution may take longer (as it downloads the 2.4GB model), but subsequent runs will be faster.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Here, we load the quantized model weights into memory and initialize the Phi-3 model. This involves reading the weights from the `gguf` file and preparing the model for inference on the specified device (CPU in this case).

## Step 5: Process Prompt and Prepare for Inference

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

In this step, the input prompt is tokenized and converted into a sequence of token IDs for inference. We also initialize the `LogitsProcessor` with the `temperature` and `top_p` values. Each token is transformed into a tensor and passed through the model to compute the logits.

The loop processes each token in the prompt, updating the logits processor and preparing for the next token to be generated.

## Step 6: Inference

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

During inference, tokens are generated one by one until the desired sample length is reached or an end-of-sequence token is encountered. Each token is converted into a tensor and passed through the model. The logits are processed to apply penalties and sampling, after which the next token is selected, decoded, and appended to the sequence.

To prevent repetitive text, penalties are applied to repeated tokens based on the `repeat_last_n` and `repeat_penalty` parameters.

The generated text is printed in real time as it is decoded.

## Step 7: Run the Application

To execute the application, run the following command in the terminal:

```bash
cargo run --release
```

This will generate and print a haiku about ice hockey using the Phi-3 model. For example, the output might look like:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

or

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

By following these steps, you can generate text using the Phi-3 model with Rust and Candle in under 100 lines of code. The code handles model loading, tokenization, and inference, leveraging tensors and logits processing to produce coherent text based on the input prompt.

This console application can run on Windows, Linux, and macOS. Thanks to Rust's portability, the code can also be adapted into a library for use in mobile apps (since console applications cannot run on mobile platforms).

## Appendix: Full Code

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

Note: To run this code on aarch64 Linux or aarch64 Windows, add a file named `.cargo/config` with the following content:

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

> For more examples of how to use the Phi-3 model with Rust and Candle, including alternative inference methods, visit the official [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.