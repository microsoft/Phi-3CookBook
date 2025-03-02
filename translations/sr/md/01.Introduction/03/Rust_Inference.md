# Крос-платформска инференција са Rust-ом

Овај водич ће нас провести кроз процес извођења инференције користећи Rust и [Candle ML framework](https://github.com/huggingface/candle) од HuggingFace-а. Коришћење Rust-а за инференцију нуди бројне предности, посебно у поређењу са другим програмским језицима. Rust је познат по својим високим перформансама, упоредивим са C и C++. Ово га чини одличним избором за задатке инференције, који могу бити рачунарски захтевни. Посебно, ово је омогућено захваљујући апстракцијама без трошкова и ефикасном управљању меморијом, које нема оптерећење од сакупљача отпада. Крос-платформске могућности Rust-а омогућавају развој кода који ради на различитим оперативним системима, укључујући Windows, macOS и Linux, као и мобилне оперативне системе, без значајних промена у бази кода.

Предуслов за праћење овог водича је [инсталација Rust-а](https://www.rust-lang.org/tools/install), која укључује Rust компајлер и Cargo, Rust-ов менаџер пакета.

## Корак 1: Креирање Новог Rust Пројекта

Да бисте креирали нови Rust пројекат, покрените следећу команду у терминалу:

```bash
cargo new phi-console-app
```

Ово генерише почетну структуру пројекта са `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` датотеком:

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

## Корак 2: Конфигурисање Основних Параметара

Унутар `main.rs` датотеке, подесићемо почетне параметре за нашу инференцију. Сви ће бити хардкодовани ради једноставности, али их можемо модификовати по потреби.

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

- **temperature**: Контролише насумичност процеса узорковања.
- **sample_len**: Одређује максималну дужину генерисаног текста.
- **top_p**: Користи се за nucleus sampling како би се ограничио број токена који се разматрају у сваком кораку.
- **repeat_last_n**: Контролише број токена који се узимају у обзир приликом примене казне за спречавање понављања секвенци.
- **repeat_penalty**: Вредност казне која обесхрабрује понављање токена.
- **seed**: Насумични seed (можемо користити константну вредност за бољу репродуктивност).
- **prompt**: Почетни текст који покреће генерисање. Приметићете да тражимо од модела да генерише хаику о хокеју на леду и да га окружујемо специјалним токенима који означавају делове разговора корисника и асистента. Модел ће затим завршити prompt са хаикуом.
- **device**: У овом примеру користимо CPU за рачунање. Candle подржава извршавање на GPU-у са CUDA и Metal-ом.

## Корак 3: Преузимање/Припремање Модела и Tokenizer-а

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

Користимо `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` датотеку за токенизацију нашег улазног текста. Када се модел преузме, он се кешира, тако да ће прво извршавање бити спорије (јер преузима 2.4GB модела), али ће сва наредна извршавања бити бржа.

## Корак 4: Учитавање Модела

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Учитавамо квантоване тежине модела у меморију и иницијализујемо Phi-3 модел. Овај корак укључује читање тежина модела из `gguf` датотеке и припрему модела за инференцију на одређеном уређају (у овом случају CPU).

## Корак 5: Обрада Prompt-а и Припрема за Инференцију

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

У овом кораку, токенизујемо улазни prompt и припремамо га за инференцију претварајући га у секвенцу ID-ева токена. Такође иницијализујемо `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` вредности. Сваки токен се претвара у тензор и пролази кроз модел како би се добили logits.

Петља обрађује сваки токен у prompt-у, ажурирајући процесор логита и припремајући се за генерисање следећег токена.

## Корак 6: Инференција

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

У петљи за инференцију, генеришемо токене један по један док не достигнемо жељену дужину или не наиђемо на токен који означава крај секвенце. Следећи токен се претвара у тензор и пролази кроз модел, док се логити обрађују како би се примениле казне и узорковање. Затим се узоркује следећи токен, декодира и додаје секвенци.
Да бисмо избегли понављајући текст, примењује се казна за поновљене токене на основу параметара `repeat_last_n` and `repeat_penalty`.

На крају, генерисани текст се приказује како се декодира, обезбеђујући стримовани реал-тим излаз.

## Корак 7: Покретање Апликације

Да бисте покренули апликацију, извршите следећу команду у терминалу:

```bash
cargo run --release
```

Ово би требало да испише хаику о хокеју на леду који је генерисао Phi-3 модел. Нешто попут:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

или

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Закључак

Пратећи ове кораке, можемо извршити генерисање текста користећи Phi-3 модел са Rust-ом и Candle-ом у мање од 100 линија кода. Код обрађује учитавање модела, токенизацију и инференцију, користећи тензоре и обраду логита за генерисање кохерентног текста на основу улазног prompt-а.

Ова конзолна апликација може да ради на Windows-у, Linux-у и Mac OS-у. Захваљујући преносивости Rust-а, код се такође може прилагодити у библиотеку која би радила унутар мобилних апликација (на крају крајева, не можемо покретати конзолне апликације на мобилним уређајима).

## Додатак: комплетан код

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

Напомена: како бисте покренули овај код на aarch64 Linux-у или aarch64 Windows-у, додајте датотеку под именом `.cargo/config` са следећим садржајем:

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

> Можете посетити званични [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) репозиторијум за више примера како да користите Phi-3 модел са Rust-ом и Candle-ом, укључујући алтернативне приступе инференцији.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованог на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неразумевања која могу проистећи из коришћења овог превода.