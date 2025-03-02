# ਰਸਟ ਨਾਲ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਇਨਫਰੈਂਸ

ਇਹ ਟਿਊਟੋਰੀਅਲ ਸਾਨੂੰ ਰਸਟ ਅਤੇ [Candle ML ਫਰੇਮਵਰਕ](https://github.com/huggingface/candle) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਫਰੈਂਸ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦਿਖਾਵੇਗਾ। ਰਸਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਫਰੈਂਸ ਕਰਨ ਦੇ ਕਈ ਫਾਇਦੇ ਹਨ, ਖਾਸ ਕਰਕੇ ਹੋਰ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਨਾਲ ਤੁਲਨਾ ਕਰਨ ਤੇ। ਰਸਟ ਆਪਣੀ ਉੱਚ ਪ੍ਰਦਰਸ਼ਨਸ਼ੀਲਤਾ ਲਈ ਪ੍ਰਸਿੱਧ ਹੈ, ਜੋ ਕਿ C ਅਤੇ C++ ਦੇ ਸਮਾਨ ਹੈ। ਇਹ ਇਨਫਰੈਂਸ ਟਾਸਕ ਲਈ ਸ਼ਾਨਦਾਰ ਚੋਣ ਬਣਦਾ ਹੈ, ਜੋ ਕਿ ਕਾਫ਼ੀ ਗਣਨਾਤਮਕ ਤੌਰ 'ਤੇ ਭਾਰੀ ਹੋ ਸਕਦੇ ਹਨ। ਇਹ ਖਾਸ ਤੌਰ 'ਤੇ ਜ਼ੀਰੋ-ਕੋਸਟ ਐਬਸਟ੍ਰੈਕਸ਼ਨ ਅਤੇ ਕੁਸ਼ਲ ਮੈਮੋਰੀ ਮੈਨੇਜਮੈਂਟ ਕਾਰਨ ਸੰਭਵ ਹੈ, ਜਿਸ ਵਿੱਚ ਗਾਰਬੇਜ ਕਲੇਕਸ਼ਨ ਦਾ ਕੋਈ ਝੰਝਟ ਨਹੀਂ ਹੁੰਦਾ। ਰਸਟ ਦੀ ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਸਮਰੱਥਾ ਅਜਿਹੀ ਕੋਡ ਲਿਖਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ ਜੋ ਵੱਖ-ਵੱਖ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ, ਜਿਵੇਂ ਕਿ Windows, macOS, Linux, ਅਤੇ ਮੋਬਾਈਲ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ 'ਤੇ ਬਿਨਾਂ ਕਿਸੇ ਵੱਡੇ ਬਦਲਾਅ ਦੇ ਚੱਲ ਸਕੇ।

ਇਸ ਟਿਊਟੋਰੀਅਲ ਨੂੰ ਫਾਲੋ ਕਰਨ ਲਈ ਪੂਰਵ ਸ਼ਰਤ ਹੈ ਕਿ ਤੁਸੀਂ [Rust ਇੰਸਟਾਲ ਕਰੋ](https://www.rust-lang.org/tools/install), ਜਿਸ ਵਿੱਚ Rust ਕੰਪਾਇਲਰ ਅਤੇ Cargo, ਰਸਟ ਪੈਕੇਜ ਮੈਨੇਜਰ ਸ਼ਾਮਲ ਹਨ।

## ਕਦਮ 1: ਨਵਾਂ ਰਸਟ ਪ੍ਰਾਜੈਕਟ ਬਣਾਓ

ਨਵਾਂ ਰਸਟ ਪ੍ਰਾਜੈਕਟ ਬਣਾਉਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕਮਾਂਡ ਚਲਾਓ:

```bash
cargo new phi-console-app
```

ਇਹ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਪ੍ਰਾਜੈਕਟ ਸਟਰੱਕਚਰ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ਫਾਈਲ ਹੁੰਦੀ ਹੈ:

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

## ਕਦਮ 2: ਬੁਨਿਆਦੀ ਪੈਰਾਮੀਟਰ ਸੈਟ ਕਰੋ

`main.rs` ਫਾਈਲ ਦੇ ਅੰਦਰ, ਅਸੀਂ ਇਨਫਰੈਂਸ ਲਈ ਸ਼ੁਰੂਆਤੀ ਪੈਰਾਮੀਟਰ ਸੈਟ ਕਰਾਂਗੇ। ਇਹ ਸਧਾਰਣਤਾ ਲਈ ਹਾਰਡਕੋਡ ਕੀਤੇ ਜਾਣਗੇ, ਪਰ ਜ਼ਰੂਰਤ ਪੈਂਦੀ ਤਾਂ ਅਸੀਂ ਇਹਨਾਂ ਨੂੰ ਬਦਲ ਸਕਦੇ ਹਾਂ।

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

- **temperature**: ਸੈਂਪਲਿੰਗ ਪ੍ਰਕਿਰਿਆ ਦੀ ਰੈਨਡਮਨੈਸ ਨੂੰ ਕਨਟਰੋਲ ਕਰਦਾ ਹੈ।
- **sample_len**: ਬਣਾਈ ਗਈ ਲਿਖਤ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ।
- **top_p**: ਨਿਊਕਲਿਅਸ ਸੈਂਪਲਿੰਗ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਹਰ ਕਦਮ ਲਈ ਗਿਣੇ ਜਾਣ ਵਾਲੇ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਸੀਮਿਤ ਕੀਤੀ ਜਾ ਸਕੇ।
- **repeat_last_n**: ਦੁਹਰਾਏ ਗਏ ਕ੍ਰਮਾਂਕ ਨੂੰ ਰੋਕਣ ਲਈ ਪੈਨਲਟੀ ਲਗਾਉਣ ਲਈ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੂੰ ਕਨਟਰੋਲ ਕਰਦਾ ਹੈ।
- **repeat_penalty**: ਦੁਹਰਾਏ ਗਏ ਟੋਕਨ ਨੂੰ ਹਤਾਸ਼ ਕਰਨ ਲਈ ਪੈਨਲਟੀ ਦਾ ਮੁੱਲ।
- **seed**: ਇੱਕ ਰੈਂਡਮ ਸੀਡ (ਅਸੀਂ ਵਧੀਆ ਦੁਹਰਾਏ ਜਾ ਸਕਣ ਯੋਗਤਾ ਲਈ ਇੱਕ ਸਥਿਰ ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ)।
- **prompt**: ਜਨਰੇਸ਼ਨ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਸ਼ੁਰੂਆਤੀ ਟੈਕਸਟ। ਧਿਆਨ ਦਿਓ ਕਿ ਅਸੀਂ ਮਾਡਲ ਨੂੰ ਆਈਸ ਹਾਕੀ ਬਾਰੇ ਇੱਕ ਹਾਇਕੂ ਬਣਾਉਣ ਲਈ ਕਹਿੰਦੇ ਹਾਂ ਅਤੇ ਇਸ ਨੂੰ ਖਾਸ ਟੋਕਨ ਨਾਲ ਲਪੇਟਦੇ ਹਾਂ ਜੋ ਉਪਭੋਗਤਾ ਅਤੇ ਸਹਾਇਕ ਦੇ ਹਿੱਸਿਆਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਮਾਡਲ ਫਿਰ ਪ੍ਰਾਂਪਟ ਨੂੰ ਪੂਰਾ ਕਰੇਗਾ।
- **device**: ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਅਸੀਂ ਗਣਨਾ ਲਈ CPU ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ। Candle GPU 'ਤੇ CUDA ਅਤੇ Metal ਨਾਲ ਚਲਾਉਣ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।

## ਕਦਮ 3: ਮਾਡਲ ਅਤੇ ਟੋਕਨਾਈਜ਼ਰ ਡਾਊਨਲੋਡ/ਤਿਆਰ ਕਰੋ

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

ਅਸੀਂ `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` ਫਾਈਲ ਨੂੰ ਆਪਣੀ ਇਨਪੁਟ ਲਿਖਤ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਨ ਲਈ ਵਰਤਦੇ ਹਾਂ। ਇੱਕ ਵਾਰ ਡਾਊਨਲੋਡ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਮਾਡਲ ਕੈਸ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਇਸ ਲਈ ਪਹਿਲੀ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਧੀਮੀ ਹੋਵੇਗੀ (ਕਿਉਂਕਿ ਇਹ 2.4GB ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ) ਪਰ ਅਗਲੇ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਤੇਜ਼ ਹੋਣਗੇ।

## ਕਦਮ 4: ਮਾਡਲ ਲੋਡ ਕਰੋ

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ਅਸੀਂ ਮਾਡਲ ਦੇ ਕਵਾਂਟਾਈਜ਼ਡ ਵੇਟਸ ਨੂੰ ਮੈਮੋਰੀ ਵਿੱਚ ਲੋਡ ਕਰਦੇ ਹਾਂ ਅਤੇ Phi-3 ਮਾਡਲ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ। ਇਹ ਕਦਮ `gguf` ਫਾਈਲ ਤੋਂ ਮਾਡਲ ਵੇਟਸ ਨੂੰ ਪੜ੍ਹਨ ਅਤੇ ਨਿਰਧਾਰਤ ਡਿਵਾਈਸ (ਇਸ ਮਾਮਲੇ ਵਿੱਚ CPU) 'ਤੇ ਇਨਫਰੈਂਸ ਲਈ ਮਾਡਲ ਨੂੰ ਸੈਟਅੱਪ ਕਰਨ ਦੀ ਸ਼ਾਮਲ ਹੈ।

## ਕਦਮ 5: ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸ ਕਰੋ ਅਤੇ ਇਨਫਰੈਂਸ ਲਈ ਤਿਆਰ ਕਰੋ

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

ਇਸ ਕਦਮ ਵਿੱਚ, ਅਸੀਂ ਇਨਪੁਟ ਪ੍ਰਾਂਪਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਇਨਫਰੈਂਸ ਲਈ ਤਿਆਰ ਕਰਦੇ ਹਾਂ, ਇਸਨੂੰ ਟੋਕਨ IDਜ਼ ਦੇ ਕ੍ਰਮ ਵਿੱਚ ਤਬਦੀਲ ਕਰਕੇ। ਅਸੀਂ `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ਮੁੱਲਾਂ ਨੂੰ ਵੀ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ। ਹਰ ਟੋਕਨ ਨੂੰ ਟੈਂਸਰ ਵਿੱਚ ਤਬਦੀਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਮਾਡਲ ਵਿੱਚ ਲੰਘਾਇਆ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਲੋਗਿਟਸ ਮਿਲ ਸਕਣ।

ਲੂਪ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਹਰ ਟੋਕਨ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਦਾ ਹੈ, ਲੋਗਿਟਸ ਪ੍ਰੋਸੈਸਰ ਨੂੰ ਅਪਡੇਟ ਕਰਦਾ ਹੈ ਅਤੇ ਅਗਲੇ ਟੋਕਨ ਜਨਰੇਸ਼ਨ ਲਈ ਤਿਆਰ ਕਰਦਾ ਹੈ।

## ਕਦਮ 6: ਇਨਫਰੈਂਸ

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

ਇਨਫਰੈਂਸ ਲੂਪ ਵਿੱਚ, ਅਸੀਂ ਟੋਕਨ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਜਨਰੇਟ ਕਰਦੇ ਹਾਂ ਜਦ ਤੱਕ ਅਸੀਂ ਚਾਹੀਦੀ ਸੈਂਪਲ ਲੰਬਾਈ ਤੱਕ ਨਹੀਂ ਪਹੁੰਚ ਜਾਂਦੇ ਜਾਂ ਅੰਤ-ਕ੍ਰਮ ਟੋਕਨ ਨਹੀਂ ਮਿਲਦਾ। ਅਗਲਾ ਟੋਕਨ ਟੈਂਸਰ ਵਿੱਚ ਤਬਦੀਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਮਾਡਲ ਵਿੱਚ ਲੰਘਾਇਆ ਜਾਂਦਾ ਹੈ, ਜਦਕਿ ਲੋਗਿਟਸ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਜੋ ਪੈਨਲਟੀ ਅਤੇ ਸੈਂਪਲਿੰਗ ਲਾਗੂ ਕੀਤੀ ਜਾ ਸਕੇ। ਫਿਰ ਅਗਲਾ ਟੋਕਨ ਸੈਂਪਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਡਿਕੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਅਤੇ ਕ੍ਰਮ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। 

ਦੁਹਰਾਏ ਗਏ ਟੈਕਸਟ ਤੋਂ ਬਚਣ ਲਈ, `repeat_last_n` and `repeat_penalty` ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਦੁਹਰਾਏ ਗਏ ਟੋਕਨ ਲਈ ਇੱਕ ਪੈਨਲਟੀ ਲਗਾਈ ਜਾਂਦੀ ਹੈ।

ਆਖਰਕਾਰ, ਬਣਾਈ ਗਈ ਲਿਖਤ ਨੂੰ ਡਿਕੋਡ ਕਰਦੇ ਸਮੇਂ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜੋ ਰੀਅਲ-ਟਾਈਮ ਸਟ੍ਰੀਮਡ ਆਉਟਪੁੱਟ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ।

## ਕਦਮ 7: ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਓ

ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕਮਾਂਡ ਚਲਾਓ:

```bash
cargo run --release
```

ਇਹ ਆਈਸ ਹਾਕੀ ਬਾਰੇ Phi-3 ਮਾਡਲ ਦੁਆਰਾ ਬਣਾਈ ਗਈ ਹਾਇਕੂ ਪ੍ਰਿੰਟ ਕਰੇਗਾ। ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ਜਾਂ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## ਨਿਸ਼ਕਰਸ਼

ਇਹਨਾਂ ਕਦਮਾਂ ਨੂੰ ਫਾਲੋ ਕਰਕੇ, ਅਸੀਂ ਰਸਟ ਅਤੇ Candle ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ Phi-3 ਮਾਡਲ ਨਾਲ ਲਿਖਤ ਜਨਰੇਸ਼ਨ ਕਰ ਸਕਦੇ ਹਾਂ, ਸਿਰਫ 100 ਲਾਈਨਾਂ ਤੋਂ ਘੱਟ ਕੋਡ ਵਿੱਚ। ਕੋਡ ਮਾਡਲ ਲੋਡਿੰਗ, ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ, ਅਤੇ ਇਨਫਰੈਂਸ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ, ਟੈਂਸਰ ਅਤੇ ਲੋਗਿਟਸ ਪ੍ਰੋਸੈਸਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇਨਪੁਟ ਪ੍ਰਾਂਪਟ ਦੇ ਅਧਾਰ 'ਤੇ ਸੰਗਠਿਤ ਲਿਖਤ ਜਨਰੇਟ ਕਰਦਾ ਹੈ।

ਇਹ ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ Windows, Linux ਅਤੇ Mac OS 'ਤੇ ਚੱਲ ਸਕਦੀ ਹੈ। ਰਸਟ ਦੀ ਪੋਰਟੇਬਿਲਿਟੀ ਕਾਰਨ, ਕੋਡ ਨੂੰ ਇੱਕ ਲਾਇਬ੍ਰੇਰੀ ਵਿੱਚ ਅਡਾਪਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਜੋ ਮੋਬਾਈਲ ਐਪਸ ਵਿੱਚ ਚੱਲ ਸਕੇ (ਅਸੀਂ ਉਥੇ ਕਨਸੋਲ ਐਪਸ ਨਹੀਂ ਚਲਾ ਸਕਦੇ, ਆਖਰਕਾਰ)।

## ਐਪੈਂਡਿਕਸ: ਪੂਰਾ ਕੋਡ

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

ਨੋਟ: aarch64 Linux ਜਾਂ aarch64 Windows 'ਤੇ ਇਸ ਕੋਡ ਨੂੰ ਚਲਾਉਣ ਲਈ, `.cargo/config` ਨਾਮਕ ਫਾਈਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਸਮੱਗਰੀ ਹੋਵੇ:

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

> ਤੁਸੀਂ ਅਧਿਕਾਰਕ [Candle Examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) ਰਿਪੋਜ਼ਟਰੀ 'ਤੇ ਜਾ ਸਕਦੇ ਹੋ ਹੋਰ ਉਦਾਹਰਨਾਂ ਲਈ ਕਿ ਕਿਵੇਂ Phi-3 ਮਾਡਲ ਨੂੰ ਰਸਟ ਅਤੇ Candle ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਇਨਫਰੈਂਸ ਲਈ ਵਿੱਕਲਪਕ ਪਹੁੰਚ ਸ਼ਾਮਲ ਹੈ।

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਨਿਸ਼ਚਿਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਲਿਖਿਆ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।