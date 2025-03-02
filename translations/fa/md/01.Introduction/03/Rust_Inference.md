# اجرای استنتاج چندسکویی با Rust

این آموزش شما را با فرآیند انجام استنتاج با استفاده از زبان برنامه‌نویسی Rust و [چارچوب Candle ML](https://github.com/huggingface/candle) از HuggingFace آشنا می‌کند. استفاده از Rust برای استنتاج مزایای زیادی دارد، به‌ویژه در مقایسه با زبان‌های برنامه‌نویسی دیگر. Rust به دلیل عملکرد بالا، که قابل مقایسه با C و C++ است، شناخته شده است. این ویژگی آن را به انتخابی عالی برای وظایف استنتاج، که معمولاً به محاسبات سنگین نیاز دارند، تبدیل می‌کند. به‌ویژه، این امر به دلیل انتزاعات بدون هزینه اضافی و مدیریت کارآمد حافظه است که سربار جمع‌آوری زباله ندارد. قابلیت‌های چندسکویی Rust به توسعه کدی که می‌تواند روی سیستم‌عامل‌های مختلف از جمله ویندوز، مک‌او‌اس و لینوکس و همچنین سیستم‌عامل‌های موبایل اجرا شود، بدون تغییرات عمده در کد، کمک می‌کند.

پیش‌نیاز دنبال کردن این آموزش، [نصب Rust](https://www.rust-lang.org/tools/install) است که شامل کامپایلر Rust و Cargo، مدیر بسته Rust، می‌شود.

## مرحله ۱: ایجاد یک پروژه جدید Rust

برای ایجاد یک پروژه جدید Rust، دستور زیر را در ترمینال اجرا کنید:

```bash
cargo new phi-console-app
```

این دستور یک ساختار پروژه اولیه با فایل‌های `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ایجاد می‌کند:

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

## مرحله ۲: پیکربندی پارامترهای اولیه

در فایل main.rs، پارامترهای اولیه برای استنتاج را تنظیم می‌کنیم. برای ساده‌سازی، همه این پارامترها به صورت ثابت تعریف می‌شوند، اما می‌توانیم در صورت نیاز آن‌ها را تغییر دهیم.

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

- **temperature**: میزان تصادفی بودن فرآیند نمونه‌گیری را کنترل می‌کند.
- **sample_len**: حداکثر طول متن تولیدشده را مشخص می‌کند.
- **top_p**: برای نمونه‌گیری هسته‌ای استفاده می‌شود تا تعداد توکن‌های موردنظر برای هر مرحله محدود شود.
- **repeat_last_n**: تعداد توکن‌هایی را که برای اعمال جریمه به منظور جلوگیری از تکرار متوالی در نظر گرفته می‌شوند، کنترل می‌کند.
- **repeat_penalty**: مقدار جریمه برای جلوگیری از تکرار توکن‌ها.
- **seed**: یک مقدار تصادفی ثابت (برای بازتولیدپذیری بهتر می‌توان از یک مقدار ثابت استفاده کرد).
- **prompt**: متن اولیه‌ای که تولید متن را آغاز می‌کند. توجه کنید که از مدل می‌خواهیم یک هایکو درباره هاکی روی یخ تولید کند و این متن را با توکن‌های خاصی می‌پیچیم تا بخش‌های کاربر و دستیار مکالمه را مشخص کنیم. سپس مدل، متن را با یک هایکو کامل می‌کند.
- **device**: در این مثال از CPU برای محاسبات استفاده می‌کنیم. Candle از اجرای روی GPU با CUDA و Metal نیز پشتیبانی می‌کند.

## مرحله ۳: دانلود/آماده‌سازی مدل و توکنایزر

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

ما از فایل `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` برای توکنایز کردن متن ورودی استفاده می‌کنیم. پس از دانلود، مدل در حافظه کش ذخیره می‌شود، بنابراین اجرای اولیه ممکن است کند باشد (زیرا ۲.۴ گیگابایت از مدل دانلود می‌شود)، اما اجراهای بعدی سریع‌تر خواهند بود.

## مرحله ۴: بارگذاری مدل

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ما وزن‌های مدل کوانتیزه‌شده را به حافظه بارگذاری کرده و مدل Phi-3 را مقداردهی اولیه می‌کنیم. این مرحله شامل خواندن وزن‌های مدل از فایل `gguf` و آماده‌سازی مدل برای استنتاج روی دستگاه مشخص‌شده (در اینجا CPU) است.

## مرحله ۵: پردازش پرامپت و آماده‌سازی برای استنتاج

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

در این مرحله، پرامپت ورودی توکنایز شده و برای استنتاج آماده می‌شود. این کار با تبدیل آن به دنباله‌ای از شناسه‌های توکن انجام می‌شود. همچنین مقادیر `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` مقداردهی اولیه می‌شوند. هر توکن به یک تنسور تبدیل شده و از مدل عبور می‌کند تا logits به‌دست آید.

حلقه هر توکن در پرامپت را پردازش کرده و LogitsProcessor را به‌روزرسانی کرده و برای تولید توکن بعدی آماده می‌کند.

## مرحله ۶: استنتاج

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

در حلقه استنتاج، توکن‌ها یکی‌یکی تولید می‌شوند تا زمانی که به طول نمونه موردنظر برسیم یا به توکن پایان دنباله برخورد کنیم. توکن بعدی به یک تنسور تبدیل شده و از مدل عبور می‌کند، در حالی که logits پردازش شده و جریمه‌ها و نمونه‌گیری اعمال می‌شوند. سپس توکن بعدی نمونه‌گیری، رمزگشایی و به دنباله اضافه می‌شود. 

برای جلوگیری از متن‌های تکراری، یک جریمه به توکن‌های تکراری بر اساس پارامترهای `repeat_last_n` and `repeat_penalty` اعمال می‌شود.

در نهایت، متن تولیدشده به‌صورت رمزگشایی‌شده چاپ می‌شود و خروجی در زمان واقعی نمایش داده می‌شود.

## مرحله ۷: اجرای برنامه

برای اجرای برنامه، دستور زیر را در ترمینال اجرا کنید:

```bash
cargo run --release
```

این دستور باید یک هایکو درباره هاکی روی یخ که توسط مدل Phi-3 تولید شده است، چاپ کند. چیزی شبیه به:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

یا

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## نتیجه‌گیری

با دنبال کردن این مراحل، می‌توانیم متن را با استفاده از مدل Phi-3 و با کمک Rust و Candle در کمتر از ۱۰۰ خط کد تولید کنیم. این کد بارگذاری مدل، توکنایز کردن و استنتاج را مدیریت می‌کند و با استفاده از تنسورها و پردازش logits، متن‌های منسجم بر اساس پرامپت ورودی تولید می‌کند.

این برنامه کنسولی می‌تواند روی ویندوز، لینوکس و مک‌او‌اس اجرا شود. به دلیل قابلیت حمل Rust، این کد همچنین می‌تواند به یک کتابخانه تبدیل شود که در برنامه‌های موبایل اجرا شود (چرا که نمی‌توان برنامه‌های کنسولی را در آنجا اجرا کرد).

## پیوست: کد کامل

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

توجه: برای اجرای این کد روی لینوکس aarch64 یا ویندوز aarch64، یک فایل با نام `.cargo/config` با محتوای زیر اضافه کنید:

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

> می‌توانید برای مثال‌های بیشتر در مورد نحوه استفاده از مدل Phi-3 با Rust و Candle، از جمله رویکردهای جایگزین برای استنتاج، به مخزن رسمی [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) مراجعه کنید.

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.