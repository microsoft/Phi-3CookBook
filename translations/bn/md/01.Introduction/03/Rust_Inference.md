# রাস্ট ব্যবহার করে ক্রস-প্ল্যাটফর্ম ইনফারেন্স

এই টিউটোরিয়ালে আমরা রাস্ট এবং HuggingFace-এর [Candle ML ফ্রেমওয়ার্ক](https://github.com/huggingface/candle) ব্যবহার করে ইনফারেন্স করার প্রক্রিয়া শিখব। ইনফারেন্সের জন্য রাস্ট ব্যবহার করলে বেশ কিছু সুবিধা পাওয়া যায়, বিশেষ করে অন্যান্য প্রোগ্রামিং ভাষার তুলনায়। রাস্ট তার উচ্চ পারফরম্যান্সের জন্য পরিচিত, যা C এবং C++-এর সমতুল্য। এটি ইনফারেন্সের মতো জটিল গণনামূলক কাজের জন্য একটি দুর্দান্ত পছন্দ। বিশেষ করে, এটি সম্ভব হয়েছে রাস্টের জিরো-কস্ট অ্যাবস্ট্রাকশন এবং কার্যকর মেমরি ম্যানেজমেন্টের জন্য, যা কোনো গার্বেজ কালেকশনের ওভারহেড ছাড়াই কাজ করে। রাস্টের ক্রস-প্ল্যাটফর্ম ক্ষমতা কোড এমনভাবে উন্নয়ন করতে সক্ষম করে, যা উইন্ডোজ, ম্যাকওএস, লিনাক্সসহ মোবাইল অপারেটিং সিস্টেমে উল্লেখযোগ্য পরিবর্তন ছাড়াই চলতে পারে।

এই টিউটোরিয়াল অনুসরণ করার পূর্বশর্ত হলো [রাস্ট ইন্সটল করা](https://www.rust-lang.org/tools/install), যা রাস্ট কম্পাইলার এবং কার্গো (রাস্টের প্যাকেজ ম্যানেজার) অন্তর্ভুক্ত করে।

## ধাপ ১: একটি নতুন রাস্ট প্রজেক্ট তৈরি করুন

একটি নতুন রাস্ট প্রজেক্ট তৈরি করতে, টার্মিনালে নিচের কমান্ডটি চালান:

```bash
cargo new phi-console-app
```

এটি একটি প্রাথমিক প্রজেক্ট স্ট্রাকচার তৈরি করবে, যেখানে একটি `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ফাইল থাকবে:

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

## ধাপ ২: মৌলিক প্যারামিটার কনফিগার করুন

`main.rs` ফাইলের ভিতরে আমরা ইনফারেন্সের জন্য প্রাথমিক প্যারামিটার সেট করব। সহজতার জন্য এগুলো হার্ডকোড করা হবে, তবে প্রয়োজনে পরিবর্তন করা যেতে পারে।

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

- **temperature**: স্যাম্পলিং প্রক্রিয়ার র্যান্ডমনেস নিয়ন্ত্রণ করে।
- **sample_len**: জেনারেট করা টেক্সটের সর্বাধিক দৈর্ঘ্য নির্ধারণ করে।
- **top_p**: নিউক্লিয়াস স্যাম্পলিংয়ের জন্য ব্যবহৃত হয়, যা প্রতিটি ধাপে বিবেচিত টোকেনের সংখ্যা সীমাবদ্ধ করে।
- **repeat_last_n**: পুনরাবৃত্তি রোধ করতে টোকেনগুলোর ওপর পেনাল্টি প্রয়োগের জন্য বিবেচিত টোকেনের সংখ্যা নিয়ন্ত্রণ করে।
- **repeat_penalty**: পুনরাবৃত্তি হওয়া টোকেনগুলোর জন্য নিরুৎসাহিত করতে পেনাল্টি ভ্যালু।
- **seed**: একটি র‍্যান্ডম সিড (ভাল পুনরুত্পাদনযোগ্যতার জন্য আমরা একটি কনস্ট্যান্ট ভ্যালু ব্যবহার করতে পারি)।
- **prompt**: জেনারেশন শুরু করার জন্য প্রাথমিক প্রম্পট টেক্সট। এখানে আমরা মডেলকে আইস হকি সম্পর্কে একটি হাইকু তৈরি করতে বলি এবং এটি বিশেষ টোকেন দিয়ে ঘিরে রাখি, যা কথোপকথনের ব্যবহারকারী এবং অ্যাসিস্ট্যান্ট অংশ নির্দেশ করে। মডেল প্রম্পটটি সম্পন্ন করে একটি হাইকু তৈরি করবে।
- **device**: এই উদাহরণে আমরা CPU ব্যবহার করি। Candle GPU-তে CUDA এবং Metal সাপোর্ট করে।

## ধাপ ৩: মডেল এবং টোকেনাইজার ডাউনলোড/প্রস্তুত করুন

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

আমরা `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` ফাইলটি আমাদের ইনপুট টেক্সট টোকেনাইজ করার জন্য ব্যবহার করি। একবার ডাউনলোড করার পর মডেলটি ক্যাশ করা হয়, তাই প্রথমবার চালানোর সময় এটি ধীর হতে পারে (কারণ এটি ২.৪ জিবি মডেল ডাউনলোড করে), তবে পরবর্তী চালনাগুলো দ্রুত হবে।

## ধাপ ৪: মডেল লোড করুন

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

আমরা কোয়ান্টাইজড মডেল ওজনগুলো মেমরিতে লোড করি এবং Phi-3 মডেলটি ইনিশিয়ালাইজ করি। এই ধাপে মডেলের ওজন `gguf` ফাইল থেকে পড়া হয় এবং নির্দিষ্ট ডিভাইসে (এই ক্ষেত্রে CPU) ইনফারেন্সের জন্য সেটআপ করা হয়।

## ধাপ ৫: প্রম্পট প্রক্রিয়া করুন এবং ইনফারেন্সের জন্য প্রস্তুত করুন

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

এই ধাপে আমরা ইনপুট প্রম্পট টোকেনাইজ করি এবং এটি ইনফারেন্সের জন্য প্রস্তুত করি, যা একটি টোকেন আইডি সিকোয়েন্সে রূপান্তরিত হয়। আমরা `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ভ্যালুগুলোও ইনিশিয়ালাইজ করি। প্রতিটি টোকেন একটি টেনসরে রূপান্তরিত হয় এবং মডেলের মধ্য দিয়ে পাঠানো হয়, যাতে লগিটস পাওয়া যায়।

লুপটি প্রম্পটের প্রতিটি টোকেন প্রক্রিয়া করে, লগিটস প্রসেসর আপডেট করে এবং পরবর্তী টোকেন জেনারেশনের জন্য প্রস্তুত করে।

## ধাপ ৬: ইনফারেন্স

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

ইনফারেন্স লুপে আমরা একটি একটি করে টোকেন জেনারেট করি যতক্ষণ না আমরা কাঙ্ক্ষিত স্যাম্পল দৈর্ঘ্যে পৌঁছাই বা এন্ড-অফ-সিকোয়েন্স টোকেন পাই। পরবর্তী টোকেন একটি টেনসরে রূপান্তরিত হয় এবং মডেলের মধ্য দিয়ে পাঠানো হয়, যেখানে লগিটস প্রসেস করা হয় পেনাল্টি এবং স্যাম্পলিং প্রয়োগ করতে। এরপর পরবর্তী টোকেন স্যাম্পল, ডিকোড এবং সিকোয়েন্সে যুক্ত করা হয়। 

পুনরাবৃত্তি টেক্সট এড়াতে, `repeat_last_n` and `repeat_penalty` প্যারামিটার অনুযায়ী পুনরাবৃত্ত টোকেনগুলোর ওপর পেনাল্টি প্রয়োগ করা হয়।

শেষে, জেনারেট করা টেক্সটটি ডিকোড হওয়ার সাথে সাথে প্রিন্ট করা হয়, যা রিয়েল-টাইম আউটপুট নিশ্চিত করে।

## ধাপ ৭: অ্যাপ্লিকেশন চালান

অ্যাপ্লিকেশন চালানোর জন্য, টার্মিনালে নিচের কমান্ডটি চালান:

```bash
cargo run --release
```

এটি Phi-3 মডেলের দ্বারা জেনারেট করা একটি আইস হকি সম্পর্কিত হাইকু প্রিন্ট করবে। যেমন:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

অথবা

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## উপসংহার

এই ধাপগুলো অনুসরণ করে, আমরা রাস্ট এবং Candle ব্যবহার করে Phi-3 মডেলের মাধ্যমে ১০০ লাইনের নিচে কোডে টেক্সট জেনারেশন করতে পারি। এই কোড মডেল লোডিং, টোকেনাইজেশন এবং ইনফারেন্স পরিচালনা করে, টেনসর এবং লগিটস প্রসেসিং ব্যবহার করে ইনপুট প্রম্পটের ভিত্তিতে অর্থবহ টেক্সট জেনারেট করে।

এই কনসোল অ্যাপ্লিকেশনটি উইন্ডোজ, লিনাক্স এবং ম্যাকওএস-এ চালানো যায়। রাস্টের পোর্টেবিলিটির কারণে, কোডটি এমন একটি লাইব্রেরিতে রূপান্তর করা যায় যা মোবাইল অ্যাপে চলবে (কারণ মোবাইলে কনসোল অ্যাপ চালানো যায় না)।

## পরিশিষ্ট: সম্পূর্ণ কোড

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

দ্রষ্টব্য: এই কোডটি aarch64 Linux বা aarch64 Windows-এ চালানোর জন্য `.cargo/config` নামে একটি ফাইল তৈরি করুন এবং এর মধ্যে নিচের বিষয়বস্তু লিখুন:

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

> আপনি রাস্ট এবং Candle ব্যবহার করে Phi-3 মডেলের ইনফারেন্সের জন্য বিকল্প পদ্ধতিসহ আরো উদাহরণ দেখতে অফিসিয়াল [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) রিপোজিটরি পরিদর্শন করতে পারেন।

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক কৃত্রিম বুদ্ধিমত্তা অনুবাদ পরিষেবা ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে জেনে রাখুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা আসল নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের সুপারিশ করা হয়। এই অনুবাদ ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।