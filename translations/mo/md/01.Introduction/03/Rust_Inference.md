# Rust-ээр олон платформд дүгнэлт хийх

Энэхүү заавар нь Rust болон HuggingFace-ийн [Candle ML framework](https://github.com/huggingface/candle)-ийг ашиглан дүгнэлт хийх үйл явцыг танилцуулна. Rust-ийг дүгнэлт хийхэд ашиглах нь бусад програмчлалын хэлтэй харьцуулахад хэд хэдэн давуу талтай. Rust нь өндөр гүйцэтгэлтэй гэдгээрээ алдартай бөгөөд C болон C++ хэлтэй өрсөлдөхүйц түвшинд хүрдэг. Энэ нь тооцооллын хувьд ихээхэн нөөц шаарддаг дүгнэлт хийх ажилд маш сайн сонголт болдог. Ялангуяа энэ нь зардалгүй хийсвэрлэл, үр ашигтай санах ойн менежменттэй холбоотой бөгөөд хог цэвэрлэгчийн нэмэлт ачаалалгүйгээр ажилладаг. Rust-ийн олон платформд нийцтэй байдал нь Windows, macOS, Linux зэрэг үйлдлийн системүүд дээр мөн гар утасны үйлдлийн системүүд дээр кодыг ихээхэн өөрчлөлтгүйгээр ажиллуулах боломжийг олгодог.

Энэ зааврыг дагахаас өмнө Rust-ийг суулгасан байх шаардлагатай. Rust нь Rust компилятор болон багц менежер болох Cargo-г багтаана: [Rust суулгах](https://www.rust-lang.org/tools/install).

## 1-р алхам: Шинэ Rust төсөл үүсгэх

Шинэ Rust төсөл үүсгэхийн тулд терминал дээр дараах командыг ажиллуулна уу:

```bash
cargo new phi-console-app
```

Энэ нь дараах бүтэцтэй эхний төслийг үүсгэнэ: `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## 2-р алхам: Үндсэн параметрүүдийг тохируулах

`main.rs` файл дотор бид дүгнэлт хийхэд шаардлагатай анхны параметрүүдийг тохируулна. Эдгээрийг энгийн байдлаар кодонд оруулсан байх боловч шаардлагатай үед өөрчлөх боломжтой.

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

- **temperature**: Дээж авах үйл явцын санамсаргүй байдлыг удирдана.
- **sample_len**: Үүсгэгдэх текстийн хамгийн дээд уртыг заана.
- **top_p**: Нуклеус дээж авахад ашиглагддаг бөгөөд энэ нь алхам тутамд авч үзэх токенуудын тоог хязгаарлана.
- **repeat_last_n**: Давтагдсан дарааллыг багасгахын тулд шийтгэл өгдөг токенуудын тоог удирдана.
- **repeat_penalty**: Давтагдсан токенуудыг багасгах шийтгэлийн утга.
- **seed**: Санамсаргүй байдлын үрийг тогтооно (давтагдах боломжтой үр дүн гаргахын тулд тогтмол утга ашиглаж болно).
- **prompt**: Генерацийн эхлэл текст. Энэ жишээнд бид мөсөн хоккейн тухай хайку үүсгэхийг загварт даалгаж, ярианы хэрэглэгч болон туслах хэсгүүдийг заах тусгай токенуудаар хүрээлсэн байна.
- **device**: Энэ жишээнд бид CPU ашиглаж байна. Candle нь CUDA болон Metal-тай GPU-г дэмждэг.

## 3-р алхам: Загвар болон токенжуулагч татаж бэлтгэх

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

`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` файл нь оролтын текстийг токенжуулахад ашиглагдана. Загварыг татаж авсны дараа кэшлэгддэг тул эхний гүйцэтгэл удаан байх боловч дараагийн гүйцэтгэлүүд хурдан байна (загвар нь 2.4GB хэмжээтэй).

## 4-р алхам: Загвар ачаалах

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Квантазчилсан загварын жинг санах ойд ачаалж, Phi-3 загварыг эхлүүлнэ. Энэ алхамд `gguf` файл дахь жинг уншиж, сонгосон төхөөрөмж дээр (энэ жишээнд CPU) дүгнэлт хийхэд тохируулна.

## 5-р алхам: Prompt боловсруулж дүгнэлтэд бэлтгэх

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

Энэ алхамд бид оруулсан prompt-ийг токенжуулж, токен ID-уудын дараалалд хувиргана. Мөн `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` утгуудыг эхлүүлнэ. Токен бүрийг тензор болгон хувиргаж, загвараар дамжуулж logits-ийг авна.

Цикл нь prompt-ийн токен бүрийг боловсруулж, logits процессорыг шинэчилж, дараагийн токен үүсгэхэд бэлтгэнэ.

## 6-р алхам: Дүгнэлт хийх

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

Дүгнэлтийн циклд хүссэн дээжний уртад хүрэх эсвэл дарааллын төгсгөлийн токен гарч иртэл нэг нэгээр нь токен үүсгэнэ. Дараагийн токен тензор болгон хувиргаж, загвараар дамжуулан logits боловсруулж шийтгэл болон дээж авах үйл явцыг хэрэгжүүлнэ. Дараа нь дараагийн токен сонгогдож, тайлбарлагдан дараалалд нэмэгдэнэ.

Давтагдсан текстээс зайлсхийхийн тулд `repeat_last_n` and `repeat_penalty` параметрүүдийн дагуу шийтгэл өгдөг.

Эцэст нь, үүсгэсэн текстийг тайлбарлан бодит цагийн урсгалтай байдлаар хэвлэнэ.

## 7-р алхам: Програм ажиллуулах

Програмыг ажиллуулахын тулд терминал дээр дараах командыг гүйцэтгэнэ:

```bash
cargo run --release
```

Энэ нь Phi-3 загвараар үүсгэсэн мөсөн хоккейн тухай хайкуг хэвлэх болно. Жишээлбэл:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

эсвэл

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Дүгнэлт

Эдгээр алхмуудыг дагаснаар Rust болон Candle ашиглан Phi-3 загвараар текст үүсгэх боломжтой. Код нь загвар ачаалах, токенжуулалт, дүгнэлт хийх зэрэг үйлдлүүдийг гүйцэтгэж, оролтын prompt-д үндэслэн уялдаа холбоотой текст үүсгэнэ.

Энэхүү консол програм нь Windows, Linux болон Mac OS дээр ажиллах боломжтой. Rust-ийн зөөврийн шинж чанараас шалтгаалан кодыг гар утасны апп-д ашиглах номын сан болгон өөрчлөх боломжтой (консол апп-ууд гар утсанд ажиллахгүй гэдгийг санаарай).

## Хавсралт: Бүрэн код

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

Тэмдэглэл: aarch64 Linux эсвэл aarch64 Windows дээр энэ кодыг ажиллуулахын тулд `.cargo/config` нэртэй файл үүсгэж, дараах агуулгыг оруулна уу:

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

> Phi-3 загварыг Rust болон Candle ашиглан хэрхэн хэрэгжүүлэх талаар илүү олон жишээг [Candle жишээ](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)-ээс үзнэ үү.

It seems like "mo" might refer to a specific language or abbreviation, but it's not clear which one you're referring to. Could you clarify the language or provide more context? For example, "mo" could potentially refer to Maori, Montenegrin, or another language. Let me know, and I'll assist you accordingly!