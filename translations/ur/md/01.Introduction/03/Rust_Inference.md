# رَسٹ کے ساتھ کراس-پلیٹ فارم انفیرینس

یہ ٹیوٹوریل ہمیں رَسٹ اور [Candle ML فریم ورک](https://github.com/huggingface/candle) کا استعمال کرتے ہوئے انفیرینس کرنے کے عمل سے گزرنے میں مدد کرے گا۔ رَسٹ کا استعمال انفیرینس کے لیے کئی فوائد فراہم کرتا ہے، خاص طور پر جب دیگر پروگرامنگ زبانوں کے ساتھ موازنہ کیا جائے۔ رَسٹ اپنی اعلیٰ کارکردگی کے لیے مشہور ہے، جو سی اور سی++ کے برابر ہے۔ یہ اسے انفیرینس کے کاموں کے لیے ایک بہترین انتخاب بناتا ہے، جو کہ عموماً کمپیوٹیشنل طور پر بھاری ہوتے ہیں۔ خاص طور پر، یہ صفر لاگت کی ایبسٹریکشنز اور موثر میموری مینجمنٹ کی وجہ سے ممکن ہوتا ہے، جس میں گاربیج کلیکشن کا کوئی اضافی بوجھ نہیں ہوتا۔ رَسٹ کی کراس-پلیٹ فارم صلاحیتیں ایسے کوڈ کی تخلیق کو ممکن بناتی ہیں جو مختلف آپریٹنگ سسٹمز، جیسے ونڈوز، میک او ایس، اور لینکس، کے ساتھ ساتھ موبائل آپریٹنگ سسٹمز پر بھی بغیر کسی بڑی تبدیلی کے چل سکتا ہے۔

اس ٹیوٹوریل کو فالو کرنے کی شرط یہ ہے کہ آپ کو [رَسٹ انسٹال](https://www.rust-lang.org/tools/install) کرنا ہوگا، جس میں رَسٹ کمپائلر اور کارگو، رَسٹ کا پیکیج مینیجر، شامل ہیں۔

## مرحلہ 1: نیا رَسٹ پروجیکٹ بنائیں

نیا رَسٹ پروجیکٹ بنانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo new phi-console-app
```

یہ ایک ابتدائی پروجیکٹ اسٹرکچر بناتا ہے جس میں `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` فائل شامل ہوتی ہے:

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

## مرحلہ 2: بنیادی پیرامیٹرز کنفیگر کریں

`main.rs` فائل کے اندر، ہم اپنے انفیرینس کے لیے ابتدائی پیرامیٹرز سیٹ اپ کریں گے۔ سادگی کے لیے یہ سب ہارڈ کوڈ کیے جائیں گے، لیکن ہم انہیں اپنی ضرورت کے مطابق تبدیل کر سکتے ہیں۔

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

- **temperature**: سیمپلنگ کے عمل کی بے ترتیبی کو کنٹرول کرتا ہے۔
- **sample_len**: جنریٹ کیے گئے ٹیکسٹ کی زیادہ سے زیادہ لمبائی کی وضاحت کرتا ہے۔
- **top_p**: نیوکلیئس سیمپلنگ کے لیے استعمال ہوتا ہے تاکہ ہر مرحلے میں غور کیے جانے والے ٹوکنز کی تعداد کو محدود کیا جا سکے۔
- **repeat_last_n**: ان ٹوکنز کی تعداد کو کنٹرول کرتا ہے جن پر ریپیٹیشن سے بچنے کے لیے جرمانہ لگایا جاتا ہے۔
- **repeat_penalty**: بار بار آنے والے ٹوکنز کو روکنے کے لیے جرمانے کی ویلیو۔
- **seed**: ایک رینڈم سیڈ (بہتر ریپروڈیسیبلٹی کے لیے ہم مستقل ویلیو استعمال کر سکتے ہیں)۔
- **prompt**: ابتدائی پرامپٹ ٹیکسٹ جو جنریشن شروع کرنے کے لیے استعمال ہوتا ہے۔ نوٹ کریں کہ ہم ماڈل سے آئس ہاکی پر ایک ہائیکو جنریٹ کرنے کے لیے کہتے ہیں، اور اسے خاص ٹوکنز کے ساتھ لپیٹتے ہیں تاکہ گفتگو کے یوزر اور اسسٹنٹ کے حصے کی نشاندہی ہو۔ ماڈل پھر پرامپٹ کو ہائیکو کے ساتھ مکمل کرے گا۔
- **device**: اس مثال میں ہم کمپیوٹیشن کے لیے CPU استعمال کرتے ہیں۔ Candle GPU کے ساتھ CUDA اور Metal پر چلانے کو بھی سپورٹ کرتا ہے۔

## مرحلہ 3: ماڈل اور ٹوکنائزر ڈاؤنلوڈ/تیار کریں

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

ہم `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` فائل کو اپنے ان پٹ ٹیکسٹ کو ٹوکنائز کرنے کے لیے استعمال کرتے ہیں۔ ایک بار ڈاؤنلوڈ ہونے کے بعد ماڈل کیش ہو جاتا ہے، لہذا پہلی بار عمل درآمد سست ہوگا (کیونکہ یہ ماڈل کے 2.4GB کو ڈاؤنلوڈ کرتا ہے) لیکن بعد کے عمل تیز ہوں گے۔

## مرحلہ 4: ماڈل لوڈ کریں

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

ہم ماڈل کے کوانٹائزڈ ویٹس کو میموری میں لوڈ کرتے ہیں اور Phi-3 ماڈل کو انیشیالائز کرتے ہیں۔ اس مرحلے میں `gguf` فائل سے ماڈل ویٹس کو پڑھنا اور انفیرینس کے لیے ماڈل کو مخصوص ڈیوائس (اس مثال میں CPU) پر سیٹ اپ کرنا شامل ہے۔

## مرحلہ 5: پرامپٹ کو پروسیس کریں اور انفیرینس کے لیے تیار کریں

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

اس مرحلے میں، ہم ان پٹ پرامپٹ کو ٹوکنائز کرتے ہیں اور اسے انفیرینس کے لیے تیار کرتے ہیں، یعنی اسے ٹوکن آئی ڈیز کی ایک ترتیب میں تبدیل کرتے ہیں۔ ہم `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ویلیوز کو بھی انیشیالائز کرتے ہیں۔ ہر ٹوکن کو ٹینسر میں تبدیل کیا جاتا ہے اور ماڈل کے ذریعے لوگٹس حاصل کرنے کے لیے پاس کیا جاتا ہے۔

یہ لوپ پرامپٹ میں ہر ٹوکن کو پروسیس کرتا ہے، لوگٹس پروسیسر کو اپ ڈیٹ کرتا ہے اور اگلے ٹوکن جنریٹ کرنے کے لیے تیار کرتا ہے۔

## مرحلہ 6: انفیرینس

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

انفیرینس لوپ میں، ہم ٹوکنز کو ایک ایک کر کے جنریٹ کرتے ہیں جب تک کہ مطلوبہ سیمپل لمبائی تک نہ پہنچ جائیں یا اختتام-سیکوئنس ٹوکن نہ مل جائے۔ اگلے ٹوکن کو ٹینسر میں تبدیل کیا جاتا ہے اور ماڈل کے ذریعے پاس کیا جاتا ہے، جبکہ لوگٹس پروسیس کیے جاتے ہیں تاکہ جرمانے اور سیمپلنگ کو لاگو کیا جا سکے۔ پھر اگلا ٹوکن سیمپل کیا جاتا ہے، ڈیکوڈ کیا جاتا ہے، اور سیکوئنس میں شامل کیا جاتا ہے۔

ریپیٹیشن سے بچنے کے لیے، بار بار آنے والے ٹوکنز پر `repeat_last_n` and `repeat_penalty` پیرامیٹرز کی بنیاد پر جرمانہ لگایا جاتا ہے۔

آخر میں، جنریٹ کیے گئے ٹیکسٹ کو ڈیکوڈ کرتے ہوئے پرنٹ کیا جاتا ہے، تاکہ ریئل ٹائم آؤٹ پٹ دکھائی دے۔

## مرحلہ 7: ایپلیکیشن چلائیں

ایپلیکیشن چلانے کے لیے، ٹرمینل میں درج ذیل کمانڈ چلائیں:

```bash
cargo run --release
```

یہ آئس ہاکی پر ایک ہائیکو پرنٹ کرے گا جو Phi-3 ماڈل نے جنریٹ کیا ہوگا۔ کچھ اس طرح:

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

## نتیجہ

ان مراحل کو فالو کر کے، ہم Phi-3 ماڈل کے ساتھ رَسٹ اور Candle کا استعمال کرتے ہوئے 100 لائنز سے کم کوڈ میں ٹیکسٹ جنریشن کر سکتے ہیں۔ یہ کوڈ ماڈل لوڈنگ، ٹوکنائزیشن، اور انفیرینس کو ہینڈل کرتا ہے، اور ٹینسرز اور لوگٹس پروسیسنگ کا فائدہ اٹھا کر ان پٹ پرامپٹ کی بنیاد پر مربوط ٹیکسٹ جنریٹ کرتا ہے۔

یہ کنسول ایپلیکیشن ونڈوز، لینکس اور میک او ایس پر چل سکتی ہے۔ رَسٹ کی پورٹیبلٹی کی وجہ سے، کوڈ کو لائبریری میں بھی تبدیل کیا جا سکتا ہے جو موبائل ایپس کے اندر چل سکے (کیونکہ ہم وہاں کنسول ایپس نہیں چلا سکتے)۔

## ضمیمہ: مکمل کوڈ

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

نوٹ: اگر آپ یہ کوڈ aarch64 لینکس یا aarch64 ونڈوز پر چلانا چاہتے ہیں، تو `.cargo/config` نامی ایک فائل درج ذیل مواد کے ساتھ شامل کریں:

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

> آپ [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) کی آفیشل ریپوزٹری پر مزید مثالیں دیکھ سکتے ہیں کہ رَسٹ اور Candle کے ساتھ Phi-3 ماڈل کو کیسے استعمال کیا جا سکتا ہے، جن میں انفیرینس کے متبادل طریقے شامل ہیں۔

**ڈس کلیمر**:  
یہ دستاویز مشین پر مبنی اے آئی ترجمہ سروسز کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز، جو اس کی مقامی زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔