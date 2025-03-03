# الاستدلال عبر الأنظمة الأساسية باستخدام Rust

هذا الدليل سيرشدنا خلال عملية تنفيذ الاستدلال باستخدام لغة Rust وإطار العمل [Candle ML](https://github.com/huggingface/candle) من HuggingFace. يوفر استخدام Rust للاستدلال عدة مزايا، خاصة عند مقارنته بلغات البرمجة الأخرى. تُعرف Rust بأدائها العالي الذي يُقارن بأداء C وC++. وهذا يجعلها خيارًا ممتازًا لمهام الاستدلال التي قد تكون كثيفة الحسابات. يعود ذلك بشكل خاص إلى التجريدات منخفضة التكلفة وإدارة الذاكرة الفعالة، حيث لا يوجد أي تكلفة إضافية لجمع القمامة. تتيح قدرات Rust عبر الأنظمة الأساسية تطوير كود يعمل على أنظمة تشغيل مختلفة، بما في ذلك Windows وmacOS وLinux، بالإضافة إلى أنظمة تشغيل الأجهزة المحمولة، دون الحاجة إلى تغييرات كبيرة في قاعدة الكود.

الشرط الأساسي لمتابعة هذا الدليل هو [تثبيت Rust](https://www.rust-lang.org/tools/install)، والذي يتضمن مترجم Rust ومدير الحزم Cargo.

## الخطوة 1: إنشاء مشروع Rust جديد

لإنشاء مشروع Rust جديد، قم بتنفيذ الأمر التالي في الطرفية:

```bash
cargo new phi-console-app
```

سيتم إنشاء هيكل مشروع ابتدائي يحتوي على ملف `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`:

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

## الخطوة 2: تكوين المعلمات الأساسية

داخل ملف main.rs، سنقوم بإعداد المعلمات الابتدائية للاستدلال. سيتم تحديدها بشكل ثابت للتبسيط، لكن يمكن تعديلها حسب الحاجة.

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

- **temperature**: يتحكم في عشوائية عملية التوليد.
- **sample_len**: يحدد الطول الأقصى للنص المُنتَج.
- **top_p**: يُستخدم لأخذ العينات النواة لتحديد عدد الرموز التي يتم أخذها في الاعتبار في كل خطوة.
- **repeat_last_n**: يتحكم في عدد الرموز التي يتم أخذها في الاعتبار لتطبيق عقوبة تمنع التكرار.
- **repeat_penalty**: قيمة العقوبة لتقليل تكرار الرموز.
- **seed**: قيمة عشوائية (يمكننا استخدام قيمة ثابتة لضمان القابلية للتكرار).
- **prompt**: النص الأولي الذي نبدأ به عملية التوليد. لاحظ أننا نطلب من النموذج إنشاء هايكو عن رياضة هوكي الجليد، ونقوم بتغليفه برموز خاصة لتحديد أجزاء المحادثة بين المستخدم والمساعد. سيقوم النموذج بعد ذلك بإكمال النص بكتابة هايكو.
- **device**: نستخدم وحدة المعالجة المركزية (CPU) للحساب في هذا المثال. يدعم Candle التشغيل على GPU باستخدام CUDA وMetal كذلك.

## الخطوة 3: تنزيل/تحضير النموذج والمحلل اللغوي

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

نستخدم ملف `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` لتحليل النص المدخل. بمجرد تنزيل النموذج، يتم تخزينه مؤقتًا، لذلك ستكون أول عملية تنفيذ بطيئة (نظرًا لتنزيل النموذج بحجم 2.4 جيجابايت)، لكن عمليات التنفيذ اللاحقة ستكون أسرع.

## الخطوة 4: تحميل النموذج

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

نقوم بتحميل أوزان النموذج المُكمَّم إلى الذاكرة ونهيئ نموذج Phi-3. تتضمن هذه الخطوة قراءة أوزان النموذج من ملف `gguf` وإعداد النموذج للاستدلال على الجهاز المحدد (وحدة المعالجة المركزية في هذه الحالة).

## الخطوة 5: معالجة النص المدخل والتحضير للاستدلال

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

في هذه الخطوة، نقوم بتحليل النص المدخل وتحضيره للاستدلال عن طريق تحويله إلى تسلسل من معرفات الرموز. كما نقوم بتهيئة قيم `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. يتم تحويل كل رمز إلى Tensor ويمر عبر النموذج للحصول على النتائج.

تعمل الحلقة على معالجة كل رمز في النص المدخل، وتحديث معالج النتائج، والتحضير لتوليد الرمز التالي.

## الخطوة 6: الاستدلال

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

في حلقة الاستدلال، نقوم بتوليد الرموز واحدًا تلو الآخر حتى نصل إلى الطول المطلوب أو نصادف رمز نهاية التسلسل. يتم تحويل الرمز التالي إلى Tensor ويمر عبر النموذج، بينما تتم معالجة النتائج لتطبيق العقوبات وأخذ العينات. ثم يتم أخذ العينة للرمز التالي، فك تشفيره، وإضافته إلى التسلسل.

لتجنب النصوص المتكررة، يتم تطبيق عقوبة على الرموز المكررة بناءً على معلمات `repeat_last_n` and `repeat_penalty`.

أخيرًا، يتم طباعة النص المُنتَج أثناء فك تشفيره، مما يضمن عرض النتائج في الوقت الفعلي.

## الخطوة 7: تشغيل التطبيق

لتشغيل التطبيق، قم بتنفيذ الأمر التالي في الطرفية:

```bash
cargo run --release
```

يجب أن يتم طباعة هايكو عن رياضة هوكي الجليد تم إنشاؤه بواسطة نموذج Phi-3. قد يكون شيئًا مثل:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

أو

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## الخاتمة

باتباع هذه الخطوات، يمكننا تنفيذ توليد النصوص باستخدام نموذج Phi-3 مع Rust وCandle في أقل من 100 سطر من الكود. يعالج الكود تحميل النموذج، التحليل اللغوي، والاستدلال، مستفيدًا من Tensors ومعالجة النتائج لتوليد نصوص متماسكة بناءً على النص المدخل.

يمكن لهذا التطبيق الذي يعمل عبر الطرفية أن يعمل على Windows وLinux وMac OS. وبفضل قابلية Rust للنقل، يمكن أيضًا تكييف الكود ليعمل كأحد المكتبات التي تُستخدم داخل تطبيقات الأجهزة المحمولة (نظرًا لأننا لا نستطيع تشغيل تطبيقات الطرفية هناك).

## الملحق: الكود الكامل

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

ملاحظة: لتشغيل هذا الكود على أنظمة aarch64 Linux أو aarch64 Windows، أضف ملفًا باسم `.cargo/config` بالمحتوى التالي:

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

> يمكنك زيارة مستودع [أمثلة Candle الرسمي](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) للحصول على المزيد من الأمثلة حول كيفية استخدام نموذج Phi-3 مع Rust وCandle، بما في ذلك أساليب بديلة للاستدلال.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.