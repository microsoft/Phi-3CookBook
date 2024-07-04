# Cross-platform inference with Rust

This tutorial will guide us through the process of performing inference using Rust and the [Candle ML framework](https://github.com/huggingface/candle) from HuggingFace. Using Rust for inference offers several advantages, particularly when compared to other programming languages. Rust is known for its high performance, comparable to that of C and C++. This makes it an excellent choice for inference tasks, which can be computationally intensive. In particular, this is driven by the zero-cost abstractions and efficient memory management, which has no garbage collection overhead. Rust's cross-platform capabilities enable development of code that run on various operating systems, including Windows, macOS, and Linux, as well as mobile operating systems, without significant changes to the codebase.

The prerequisite to follow this tutorial is to [install Rust](https://www.rust-lang.org/tools/install), which includes the Rust compiler and Cargo, the Rust package manager.

## Step 1: Create a New Rust Project

To create a new Rust project, run the following command in the terminal:

```bash
cargo new phi-console-app
```

This generates an initial project structure with a `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` file:

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

Inside the main.rs file, we will set up the initial parameters for our inference. They are all going to be hardcoded for simplicity, but we can modify them as needed.

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
- **top_p**: Used for nucleus sampling to limit the number of tokens considered for each step.
- **repeat_last_n**: Controls the number of tokens considered for applying a penalty to prevent repetitive sequences.
- **repeat_penalty**: The penalty value to discourage repeated tokens.
- **seed**: A random seed (we could use a constant value for better reproducibility).
- **prompt**: The initial prompt text to start the generation. Notice that we ask the model to generate a haiku about ice hockey, and that we wrap it with special tokens to indicate the user and assistant parts of the conversation. The model will then complete the prompt with a haiku.
- **device**: We use the CPU for computation in this example. Candle supports running on GPU with CUDA and Metal as well.

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

We use the `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` file is used for tokenizing our input text. Once downloaded the model is cached, so the first execution would be slow (as it downloads the 2.4GB of the model) but subsequent executions would be faster.

## Step 4: Load Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

We load the quantized model weights into memory and initialize the Phi-3 model. This step involves reading the model weights from the `gguf` file and setting up the model for inference on the specified device (CPU in this case).

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

In this step, we tokenize the input prompt and prepare it for inference by converting it into a sequence of token IDs. We also initialize the `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` values. Each token is converted into a tensor and passed through the model to get the logits.

The loop processes each token in the prompt, updating the logits processor and preparing for the next token generation.

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

In the inference loop, we generate tokens one by one until we reach the desired sample length or encounter the end-of-sequence token. The next token is converted to a tensor and passed through the model, while the logits are processed to apply penalties and sampling. Then the next token is sampled, decoded, and appended to the sequence.
To avoid repetitive text, a penalty is applied to repeated tokens based on the `repeat_last_n` and `repeat_penalty` parameters.

Finally, the generated text is printed as it's decoded, ensuring streamed real-time output.

## Step 7: Run the Application

To run the application, execute the following command in the terminal:

```bash
cargo run --release
```

This should print a haiku about ice hockey generated by the Phi-3 model. Something like:

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

By following these steps, we can perform text generation using the Phi-3 model with Rust and Candle in under 100 lines of code. The code handles model loading, tokenization, and inference, leveraging tensors and logits processing to generate coherent text based on the input prompt.

This console application can run on Windows, Linux and Mac OS. Becuase of Rust's portability, the code can also be adapted to a library that would run inside mobile apps (we can't run console apps there, after all).

## Appendix: full code

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

Note: in order to run this code on aarch64 Linux or aarch64 Windows, add a file named `.cargo/config` with the following content:

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

> You can visit the official [Candle examples](https://github.com/huggingface/candle/tree/main/candle-examples/examples/quantized-phi3) repository for more examples on how to use the Phi-3 model with Rust and Candle, including alternative approaches to inference.