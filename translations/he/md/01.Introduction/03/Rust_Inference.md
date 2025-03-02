# הסקה חוצת פלטפורמות עם Rust

המדריך הזה ילווה אותנו בתהליך של ביצוע הסקה באמצעות Rust ומסגרת [Candle ML](https://github.com/huggingface/candle) מבית HuggingFace. השימוש ב-Rust לביצוע הסקה מציע יתרונות רבים, במיוחד בהשוואה לשפות תכנות אחרות. Rust ידועה בביצועים הגבוהים שלה, שמשתווים לאלו של C ו-C++. זה הופך אותה לבחירה מצוינת למשימות הסקה, שיכולות להיות עתירות חישוב. יתרונות אלו נובעים בעיקר ממבנים מופשטים חסרי עלות וניהול זיכרון יעיל ללא עלויות של איסוף זבל (Garbage Collection). יכולות החוצות פלטפורמות של Rust מאפשרות פיתוח קוד שרץ על מערכות הפעלה שונות, כמו Windows, macOS, Linux, וגם מערכות הפעלה למובייל, בלי צורך בשינויים משמעותיים בקוד.

הדרישה המקדימה למדריך הזה היא [התקנת Rust](https://www.rust-lang.org/tools/install), הכוללת את הקומפיילר של Rust ואת Cargo, מנהל החבילות של Rust.

## שלב 1: יצירת פרויקט Rust חדש

כדי ליצור פרויקט Rust חדש, הריצו את הפקודה הבאה בטרמינל:

```bash
cargo new phi-console-app
```

הפקודה הזו יוצרת מבנה פרויקט ראשוני עם קובץ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## שלב 2: הגדרת פרמטרים בסיסיים

בתוך הקובץ main.rs, נגדיר את הפרמטרים הראשוניים עבור ההסקה. הפרמטרים יהיו קבועים לצורך הפשטות, אך ניתן לשנות אותם לפי הצורך.

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

- **temperature**: שולט באקראיות של תהליך הדגימה.
- **sample_len**: מציין את האורך המקסימלי של הטקסט המיוצר.
- **top_p**: משמש לדגימת גרעין (Nucleus Sampling) כדי להגביל את מספר הטוקנים שנשקלים בכל שלב.
- **repeat_last_n**: שולט במספר הטוקנים שנשקלים לצורך הטלת עונש כדי למנוע חזרות.
- **repeat_penalty**: ערך העונש שמטרתו להרתיע חזרות על טוקנים.
- **seed**: ערך אקראי (ניתן להשתמש בערך קבוע לשם שחזור טוב יותר).
- **prompt**: הטקסט הראשוני שמתחיל את תהליך היצירה. שימו לב שאנחנו מבקשים מהמודל לייצר הייקו על הוקי קרח, ועוטפים אותו בטוקנים מיוחדים כדי לציין את חלקי השיחה של המשתמש והעוזר. המודל ישלים את הטקסט עם הייקו.
- **device**: בדוגמה זו נשתמש במעבד (CPU) לצורך החישוב. Candle תומכת גם בהרצה על GPU עם CUDA ו-Metal.

## שלב 3: הורדה/הכנת מודל וטוקנייזר

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

אנחנו משתמשים בקובץ `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` לצורך טוקניזציה של הטקסט הקלט. לאחר ההורדה, המודל נשמר במטמון, כך שההרצה הראשונה תהיה איטית (כי היא מורידה 2.4GB של מודל), אבל ההרצות הבאות יהיו מהירות יותר.

## שלב 4: טעינת המודל

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

בשלב זה, נטען את משקלי המודל הכמותיים (quantized) לזיכרון ונאתחל את מודל Phi-3. שלב זה כולל קריאת המשקלים מקובץ ה-`gguf` והכנת המודל לביצוע הסקה על המכשיר הנבחר (במקרה זה, CPU).

## שלב 5: עיבוד הפרומפט והכנה להסקה

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

בשלב הזה, אנו מבצעים טוקניזציה לפרומפט הקלט ומכינים אותו להסקה על ידי המרתו לרצף של מזהי טוקנים. בנוסף, נאתחל את ערכי `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. כל טוקן מומר לטנסור ומועבר דרך המודל כדי לקבל את ה-logits.

הלולאה מעבדת כל טוקן בפרומפט, מעדכנת את ה-logits processor ומכינה את המודל ליצירת הטוקן הבא.

## שלב 6: הסקה

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

בלולאת ההסקה, אנו מייצרים טוקנים אחד אחרי השני עד שנגיע לאורך הדגימה הרצוי או נפגוש טוקן סוף רצף. הטוקן הבא מומר לטנסור ומועבר דרך המודל, תוך שה-logits מעובדים כדי להחיל עונשים ודגימה. לאחר מכן, הטוקן הבא נדגם, מפוענח ונוסף לרצף.

כדי להימנע מטקסט חוזר, מוחל עונש על טוקנים חוזרים בהתבסס על הפרמטרים `repeat_last_n` and `repeat_penalty`.

לבסוף, הטקסט שנוצר מודפס תוך כדי פענוח, ומוצג בזמן אמת.

## שלב 7: הרצת האפליקציה

כדי להריץ את האפליקציה, בצעו את הפקודה הבאה בטרמינל:

```bash
cargo run --release
```

זה אמור להדפיס הייקו על הוקי קרח שנוצר על ידי מודל Phi-3. לדוגמה:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

או

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## סיכום

על ידי ביצוע השלבים הללו, ניתן לבצע יצירת טקסט באמצעות מודל Phi-3 עם Rust ו-Candle בפחות מ-100 שורות קוד. הקוד מטפל בטעינת המודל, טוקניזציה והסקה, תוך שימוש בטנסורים ועיבוד logits ליצירת טקסט קוהרנטי בהתבסס על פרומפט הקלט.

אפליקציית הקונסולה הזו יכולה לרוץ על Windows, Linux ו-macOS. בגלל הניידות של Rust, ניתן גם להתאים את הקוד לספרייה שתפעל בתוך אפליקציות מובייל (אפליקציות קונסולה אינן רלוונטיות שם, כמובן).

## נספח: קוד מלא

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

הערה: כדי להריץ את הקוד הזה על Linux או Windows בתצורת aarch64, הוסיפו קובץ בשם `.cargo/config` עם התוכן הבא:

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

> ניתן לבקר במאגר הרשמי של [דוגמאות Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) כדי למצוא דוגמאות נוספות לשימוש במודל Phi-3 עם Rust ו-Candle, כולל גישות חלופיות להסקה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.