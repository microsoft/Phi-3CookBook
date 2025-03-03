# Rust로 크로스 플랫폼 추론하기

이 튜토리얼에서는 HuggingFace의 [Candle ML 프레임워크](https://github.com/huggingface/candle)를 사용하여 Rust로 추론을 수행하는 과정을 안내합니다. Rust를 사용한 추론은 특히 다른 프로그래밍 언어와 비교했을 때 여러 가지 이점을 제공합니다. Rust는 높은 성능으로 잘 알려져 있으며, 이는 C와 C++에 필적합니다. 이는 계산 집약적인 추론 작업에 적합한 선택이 됩니다. 특히, 이는 비용 없는 추상화와 효율적인 메모리 관리(가비지 컬렉션 오버헤드 없음) 덕분입니다. Rust의 크로스 플랫폼 기능은 코드베이스를 크게 변경하지 않고도 Windows, macOS, Linux뿐만 아니라 모바일 운영 체제에서도 실행 가능한 코드를 개발할 수 있게 해줍니다.

이 튜토리얼을 따라가기 위한 사전 조건은 [Rust 설치](https://www.rust-lang.org/tools/install)입니다. 여기에는 Rust 컴파일러와 Rust 패키지 관리자(Cargo)가 포함됩니다.

## 1단계: 새로운 Rust 프로젝트 생성

새로운 Rust 프로젝트를 생성하려면 터미널에서 다음 명령을 실행하세요:

```bash
cargo new phi-console-app
```

이 명령은 초기 프로젝트 구조를 생성하며, `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` 파일을 포함합니다:

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

`main.rs` 파일 내에서 추론을 위한 초기 매개변수를 설정합니다. 단순화를 위해 모든 매개변수는 하드코딩되지만, 필요에 따라 수정할 수 있습니다.

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
- **sample_len**: 생성될 텍스트의 최대 길이를 지정합니다.
- **top_p**: 뉴클리어스 샘플링에 사용되며, 각 단계에서 고려할 토큰 수를 제한합니다.
- **repeat_last_n**: 반복적인 시퀀스를 방지하기 위해 패널티를 적용할 토큰 수를 제어합니다.
- **repeat_penalty**: 반복 토큰을 억제하기 위한 패널티 값입니다.
- **seed**: 랜덤 시드(재현성을 위해 상수 값을 사용할 수 있습니다).
- **prompt**: 텍스트 생성을 시작하기 위한 초기 프롬프트입니다. 여기서는 아이스하키에 관한 하이쿠를 생성하도록 모델에 요청하며, 사용자와 어시스턴트 간 대화를 나타내기 위해 특수 토큰으로 감쌉니다. 모델은 프롬프트를 완성하여 하이쿠를 생성합니다.
- **device**: 이 예제에서는 CPU를 사용하여 계산합니다. Candle은 CUDA와 Metal을 사용하여 GPU에서도 실행을 지원합니다.

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

`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` 파일은 입력 텍스트를 토크나이징하는 데 사용됩니다. 모델을 다운로드하면 캐시에 저장되므로 첫 실행은 느릴 수 있지만(모델 2.4GB 다운로드) 이후 실행은 더 빠릅니다.

## 4단계: 모델 로드

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

양자화된 모델 가중치를 메모리에 로드하고 Phi-3 모델을 초기화합니다. 이 단계는 `gguf` 파일에서 모델 가중치를 읽고 지정된 디바이스(CPU)에서 추론을 위해 모델을 설정하는 작업을 포함합니다.

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

이 단계에서는 입력 프롬프트를 토크나이징하고, 이를 토큰 ID 시퀀스로 변환하여 추론을 준비합니다. 또한 `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` 값을 초기화합니다. 각 토큰은 텐서로 변환되어 모델을 통과하며 로짓을 생성합니다.

루프는 프롬프트의 각 토큰을 처리하며, 로짓 프로세서를 업데이트하고 다음 토큰 생성을 준비합니다.

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

추론 루프에서는 샘플 길이에 도달하거나 종료 토큰을 만날 때까지 한 번에 하나씩 토큰을 생성합니다. 다음 토큰은 텐서로 변환되어 모델을 통과하며, 로짓은 패널티와 샘플링을 적용하기 위해 처리됩니다. 그런 다음 다음 토큰이 샘플링되고 디코딩되어 시퀀스에 추가됩니다.
반복적인 텍스트를 방지하기 위해 `repeat_last_n` and `repeat_penalty` 매개변수를 기반으로 패널티가 적용됩니다.

마지막으로, 생성된 텍스트는 디코딩되며 실시간 스트리밍 출력으로 표시됩니다.

## 7단계: 애플리케이션 실행

애플리케이션을 실행하려면 터미널에서 다음 명령을 실행하세요:

```bash
cargo run --release
```

이 명령은 Phi-3 모델이 생성한 아이스하키 하이쿠를 출력합니다. 예를 들어:

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

이 단계를 따라가면 Rust와 Candle을 사용하여 Phi-3 모델로 텍스트 생성을 수행할 수 있으며, 100줄 미만의 코드로 가능합니다. 이 코드는 모델 로드, 토크나이징, 추론을 처리하며, 텐서와 로짓 처리를 활용하여 입력 프롬프트 기반으로 일관된 텍스트를 생성합니다.

이 콘솔 애플리케이션은 Windows, Linux, Mac OS에서 실행할 수 있습니다. Rust의 이식성 덕분에 코드는 모바일 앱 내에서 실행될 라이브러리로도 쉽게 변환될 수 있습니다(모바일 앱에서는 콘솔 애플리케이션을 실행할 수 없으므로).

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

참고: aarch64 Linux 또는 aarch64 Windows에서 이 코드를 실행하려면 `.cargo/config`라는 파일을 생성하고 다음 내용을 추가하세요:

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

> Rust와 Candle을 사용하여 Phi-3 모델로 추론하는 방법에 대한 더 많은 예제를 보려면 공식 [Candle 예제](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) 리포지토리를 방문하세요. 여기에는 추론을 위한 대체 접근법도 포함되어 있습니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 형태로 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.