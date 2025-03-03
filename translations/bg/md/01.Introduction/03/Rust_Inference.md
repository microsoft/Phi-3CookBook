# Кросплатформен инференс с Rust

Този урок ще ни преведе през процеса на извършване на инференс с помощта на Rust и [Candle ML framework](https://github.com/huggingface/candle) от HuggingFace. Използването на Rust за инференс предлага няколко предимства, особено в сравнение с други програмни езици. Rust е известен със своята висока производителност, сравнима с тази на C и C++. Това го прави отличен избор за задачи, които изискват интензивни изчисления. Това се дължи основно на абстракциите с нулева цена и ефективното управление на паметта, без допълнителни разходи за garbage collection. Кросплатформените възможности на Rust позволяват разработването на код, който работи на различни операционни системи, включително Windows, macOS и Linux, както и на мобилни операционни системи, без значителни промени в кода.

Предпоставка за следване на този урок е [инсталирането на Rust](https://www.rust-lang.org/tools/install), което включва компилатора на Rust и Cargo, мениджъра на пакети на Rust.

## Стъпка 1: Създаване на нов проект на Rust

За да създадем нов проект на Rust, изпълнете следната команда в терминала:

```bash
cargo new phi-console-app
```

Това ще генерира начална структура на проекта с файл `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Стъпка 2: Конфигуриране на основни параметри

Във файла `main.rs` ще зададем началните параметри за нашия инференс. Те ще бъдат зададени статично за простота, но можем да ги променяме при необходимост.

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

- **temperature**: Контролира случайността в процеса на семплиране.
- **sample_len**: Определя максималната дължина на генерирания текст.
- **top_p**: Използва се за nucleus sampling, за да ограничи броя на разглежданите токени на всяка стъпка.
- **repeat_last_n**: Определя броя на токените, които се разглеждат за прилагане на наказание с цел избягване на повторения.
- **repeat_penalty**: Стойността на наказанието, което обезкуражава повторенията на токени.
- **seed**: Случайно число за seed (можем да използваме константна стойност за по-добра възпроизводимост).
- **prompt**: Началният текст за генериране. Забележете, че искаме от модела да създаде хайку за хокей на лед и че го обграждаме със специални токени, за да обозначим частите на потребителя и асистента в разговора. Моделът ще допълни началния текст с хайку.
- **device**: В този пример използваме CPU за изчисления. Candle поддържа работа на GPU с CUDA и Metal.

## Стъпка 3: Изтегляне/Подготовка на модел и токенизатор

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

Използваме файла `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` за токенизиране на входния текст. След като моделът бъде изтеглен, той се кешира, така че първото изпълнение ще бъде по-бавно (тъй като изтегля модела с размер 2.4GB), но следващите изпълнения ще бъдат по-бързи.

## Стъпка 4: Зареждане на модела

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Зареждаме квантизираните тегла на модела в паметта и инициализираме модела Phi-3. Тази стъпка включва четене на теглата на модела от файла `gguf` и настройка на модела за инференс на избраното устройство (в случая CPU).

## Стъпка 5: Обработка на prompt и подготовка за инференс

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

На тази стъпка токенизираме входния prompt и го подготвяме за инференс, като го преобразуваме в последователност от токен ID-та. Също така инициализираме стойностите за `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Всеки токен се преобразува в тензор и се подава през модела, за да се получат logits.

Цикълът обработва всеки токен от prompt-а, актуализира процесора на logits и подготвя следващото генериране на токен.

## Стъпка 6: Инференс

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

В цикъла за инференс генерираме токени един по един, докато достигнем желаната дължина на текста или срещнем токен за край на последователността. Следващият токен се преобразува в тензор и се подава през модела, докато logits се обработват за прилагане на наказания и семплиране. След това следващият токен се избира, декодира и добавя към последователността.
За да избегнем повтарящ се текст, се прилага наказание върху повторените токени според параметрите `repeat_last_n` and `repeat_penalty`.

Накрая, генерираният текст се отпечатва в реално време, докато се декодира.

## Стъпка 7: Стартиране на приложението

За да стартирате приложението, изпълнете следната команда в терминала:

```bash
cargo run --release
```

Това трябва да отпечата хайку за хокей на лед, генерирано от модела Phi-3. Например:

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

## Заключение

Следвайки тези стъпки, можем да извършим генериране на текст с модела Phi-3, използвайки Rust и Candle, в по-малко от 100 реда код. Кодът обработва зареждането на модела, токенизацията и инференса, използвайки тензори и обработка на logits, за да генерира смислен текст на базата на входния prompt.

Това конзолно приложение може да се изпълнява на Windows, Linux и Mac OS. Благодарение на преносимостта на Rust, кодът може също да бъде адаптиран към библиотека, която да работи в мобилни приложения (все пак не можем да стартираме конзолни приложения там).

## Приложение: пълен код

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

Забележка: за да стартирате този код на aarch64 Linux или aarch64 Windows, добавете файл с име `.cargo/config` със следното съдържание:

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

> Можете да посетите официалното [репо с примери за Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) за повече примери как да използвате модела Phi-3 с Rust и Candle, включително алтернативни подходи за инференс.

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Ние не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, възникнали в резултат на използването на този превод.