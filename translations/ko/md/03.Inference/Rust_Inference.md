# Rust로 크로스 플랫폼 추론하기

이 튜토리얼은 HuggingFace의 [Candle ML 프레임워크](https://github.com/huggingface/candle)를 사용하여 Rust로 추론을 수행하는 과정을 안내합니다. Rust를 사용한 추론은 여러 가지 장점을 제공합니다. 특히 다른 프로그래밍 언어와 비교했을 때 그렇습니다. Rust는 C와 C++에 필적하는 높은 성능을 자랑합니다. 이는 계산 집약적인 추론 작업에 적합합니다. 특히, 이는 비용이 들지 않는 추상화와 효율적인 메모리 관리 덕분입니다. Rust는 가비지 컬렉션 오버헤드가 없습니다. Rust의 크로스 플랫폼 기능은 Windows, macOS, Linux 뿐만 아니라 모바일 운영 체제에서도 코드베이스의 큰 변경 없이 실행할 수 있는 코드를 개발할 수 있게 해줍니다.

이 튜토리얼을 따르기 위한 전제 조건은 [Rust 설치](https://www.rust-lang.org/tools/install)입니다. 여기에는 Rust 컴파일러와 Cargo(패키지 관리자)가 포함됩니다.

## 1단계: 새로운 Rust 프로젝트 생성

새로운 Rust 프로젝트를 생성하려면 터미널에서 다음 명령어를 실행합니다:

```bash
cargo new phi-console-app
```

이 명령어는 `Cargo.toml` 파일과 `main.rs` 파일이 포함된 `src` 디렉토리를 가진 초기 프로젝트 구조를 생성합니다.

다음으로 `Cargo.toml` 파일에 `candle`, `hf-hub`, `tokenizers` 크레이트를 추가합니다:

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

## 2단계: 기본 매개변수 설정

`main.rs` 파일 안에서 추론을 위한 초기 매개변수를 설정합니다. 이들은 간단하게 하드코딩되지만, 필요에 따라 수정할 수 있습니다.

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

- **temperature**: 샘플링 과정의 무작위성을 제어합니다.
- **sample_len**: 생성된 텍스트의 최대 길이를 지정합니다.
- **top_p**: 핵심 샘플링을 위해 각 단계에서 고려되는 토큰의 수를 제한합니다.
- **repeat_last_n**: 반복적인 시퀀스를 방지하기 위해 페널티를 적용할 토큰의 수를 제어합니다.
- **repeat_penalty**: 반복 토큰을 방지하기 위한 페널티 값입니다.
- **seed**: 랜덤 시드(재현성을 위해 일정한 값을 사용할 수 있습니다).
- **prompt**: 텍스트 생성을 시작하기 위한 초기 프롬프트 텍스트입니다. 모델이 하키에 대한 하이쿠를 생성하도록 요청하고, 사용자와 어시스턴트 부분을 나타내기 위해 특수 토큰으로 감쌉니다. 모델은 이 프롬프트를 완성합니다.
- **device**: 이 예제에서는 CPU를 사용합니다. Candle은 CUDA와 Metal을 사용하여 GPU에서도 실행할 수 있습니다.

## 3단계: 모델 및 토크나이저 다운로드/준비

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

`hf_hub` API를 사용하여 Hugging Face 모델 허브에서 모델과 토크나이저 파일을 다운로드합니다. `gguf` 파일은 양자화된 모델 가중치를 포함하고 있으며, `tokenizer.json` 파일은 입력 텍스트를 토크나이징하는 데 사용됩니다. 모델이 한 번 다운로드되면 캐시되므로 첫 실행은 느릴 수 있지만(모델 2.4GB 다운로드) 이후 실행은 더 빠릅니다.

## 4단계: 모델 로드

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

양자화된 모델 가중치를 메모리에 로드하고 Phi-3 모델을 초기화합니다. 이 단계에서는 `gguf` 파일에서 모델 가중치를 읽고 지정된 장치(CPU)에 모델을 설정합니다.

## 5단계: 프롬프트 처리 및 추론 준비

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

이 단계에서는 입력 프롬프트를 토크나이징하여 토큰 ID 시퀀스로 변환하고, 주어진 `temperature`와 `top_p` 값을 기반으로 샘플링 과정을 처리하기 위해 `LogitsProcessor`를 초기화합니다. 각 토큰을 텐서로 변환하고 모델을 통해 로짓을 얻습니다.

루프는 프롬프트의 각 토큰을 처리하여 로짓 프로세서를 업데이트하고 다음 토큰 생성을 준비합니다.

## 6단계: 추론

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

추론 루프에서는 원하는 샘플 길이에 도달하거나 시퀀스 종료 토큰을 만날 때까지 하나씩 토큰을 생성합니다. 다음 토큰은 텐서로 변환되어 모델을 통과하며, 로짓은 페널티와 샘플링을 적용하여 처리됩니다. 그런 다음 다음 토큰이 샘플링되고, 디코딩되어 시퀀스에 추가됩니다.
반복적인 텍스트를 방지하기 위해 `repeat_last_n`과 `repeat_penalty` 매개변수를 기반으로 페널티가 적용됩니다.

마지막으로, 생성된 텍스트는 디코딩되면서 실시간으로 출력됩니다.

## 7단계: 애플리케이션 실행

애플리케이션을 실행하려면 터미널에서 다음 명령어를 실행합니다:

```bash
cargo run --release
```

이 명령어는 Phi-3 모델이 생성한 하키에 대한 하이쿠를 출력합니다. 예를 들어:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

또는

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 결론

이 단계를 따라가면 100줄 미만의 코드로 Rust와 Candle을 사용하여 Phi-3 모델을 통해 텍스트 생성을 수행할 수 있습니다. 이 코드는 모델 로딩, 토크나이징 및 추론을 처리하며, 텐서와 로짓 처리를 활용하여 입력 프롬프트를 기반으로 일관된 텍스트를 생성합니다.

이 콘솔 애플리케이션은 Windows, Linux 및 Mac OS에서 실행할 수 있습니다. Rust의 휴대성 덕분에 이 코드는 모바일 앱 내부에서 실행되는 라이브러리로도 변환할 수 있습니다(콘솔 앱은 실행할 수 없으므로).

## 부록: 전체 코드

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
    // 1. 기본 매개변수 설정
    let temperature: f64 = 1.0;
    let sample_len: usize = 100;
    let top_p: Option<f64> = None;
    let repeat_last_n: usize = 64;
    let repeat_penalty: f32 = 1.2;
    let mut rng = rand::thread_rng();
    let seed: u64 = rng.gen();
    let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";

    // CPU에서만 실행합니다.
    let device = Device::Cpu;

    // 2. 모델 및 토크나이저 다운로드/준비
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

    // 3. 모델 로드
    let mut file = std::fs::File::open(&model_path)?;
    let model_content = gguf_file::Content::read(&mut file)?;
    let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;

    // 4. 프롬프트 처리 및 추론 준비
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

        // 프롬프트의 마지막 토큰에 대해서만 다음 토큰을 샘플링합니다.
        if pos == tokens.len() - 1 {
            next_token = logits_processor.sample(&logits)?;
            all_tokens.push(next_token);
        }
    }

    // 5. 추론
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

        // 현재 시퀀스의 토큰을 디코딩합니다.
        let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

        // 디코딩된 텍스트의 새로운 부분만 출력합니다.
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

참고: aarch64 Linux 또는 aarch64 Windows에서 이 코드를 실행하려면 `.cargo/config` 파일을 다음 내용으로 추가합니다:

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

> Rust와 Candle을 사용하여 Phi-3 모델을 사용하는 다른 예제는 공식 [Candle 예제](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 저장소를 참조하세요.

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것으로 완벽하지 않을 수 있습니다. 
출력 내용을 검토하시고 필요한 수정을 해주시기 바랍니다.