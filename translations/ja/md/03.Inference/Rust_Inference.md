# Rustを使ったクロスプラットフォーム推論

このチュートリアルでは、RustとHuggingFaceの[Candle MLフレームワーク](https://github.com/huggingface/candle)を使用して推論を行うプロセスを説明します。Rustを使用した推論には、特に他のプログラミング言語と比較していくつかの利点があります。RustはCやC++と同等の高いパフォーマンスで知られており、計算量の多い推論タスクに最適です。これは主にゼロコスト抽象化と効率的なメモリ管理（ガベージコレクションのオーバーヘッドがない）によるものです。Rustのクロスプラットフォーム機能により、Windows、macOS、Linux、およびモバイルオペレーティングシステムなど、さまざまなオペレーティングシステムでコードを大きな変更なしに実行できます。

このチュートリアルを進める前に、[Rustをインストール](https://www.rust-lang.org/tools/install)する必要があります。これにはRustコンパイラとパッケージマネージャであるCargoが含まれます。

## ステップ1: 新しいRustプロジェクトを作成する

新しいRustプロジェクトを作成するには、ターミナルで以下のコマンドを実行します。

```bash
cargo new phi-console-app
```

これにより、`Cargo.toml`ファイルと`main.rs`ファイルを含む`src`ディレクトリを持つ初期プロジェクト構造が生成されます。

次に、`Cargo.toml`ファイルに`candle`、`hf-hub`、`tokenizers`クレートを依存関係として追加します。

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

## ステップ2: 基本的なパラメータを設定する

`main.rs`ファイル内で、推論のための初期パラメータを設定します。これらは簡単のためにハードコーディングされますが、必要に応じて変更できます。

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

- **temperature**: サンプリングプロセスのランダム性を制御します。
- **sample_len**: 生成されるテキストの最大長を指定します。
- **top_p**: 各ステップで考慮されるトークンの数を制限するための核サンプリングに使用されます。
- **repeat_last_n**: 繰り返しシーケンスを防ぐためにペナルティを適用するトークンの数を制御します。
- **repeat_penalty**: 繰り返しトークンを抑制するためのペナルティ値。
- **seed**: ランダムシード（再現性を高めるために定数値を使用することもできます）。
- **prompt**: 生成を開始するための初期プロンプトテキスト。モデルにアイスホッケーについての俳句を生成させるように要求し、会話のユーザーとアシスタント部分を示す特別なトークンでラップしています。モデルはこのプロンプトを完了して俳句を生成します。
- **device**: この例ではCPUを使用します。CandleはCUDAやMetalを使用してGPU上での実行もサポートしています。

## ステップ3: モデルとトークナイザーのダウンロード/準備

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

`hf_hub` APIを使用して、Hugging Faceモデルハブからモデルとトークナイザーファイルをダウンロードします。`gguf`ファイルには量子化されたモデルの重みが含まれており、`tokenizer.json`ファイルは入力テキストをトークナイズするために使用されます。ダウンロードされたモデルはキャッシュされるため、最初の実行は遅く（モデルの2.4GBをダウンロードするため）なりますが、次回以降の実行は速くなります。

## ステップ4: モデルの読み込み

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

量子化されたモデルの重みをメモリに読み込み、Phi-3モデルを初期化します。このステップでは、`gguf`ファイルからモデルの重みを読み込み、指定されたデバイス（この場合はCPU）での推論のためにモデルを設定します。

## ステップ5: プロンプトの処理と推論の準備

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

このステップでは、入力プロンプトをトークナイズし、トークンIDのシーケンスに変換して推論の準備をします。また、与えられた`temperature`と`top_p`の値に基づいてサンプリングプロセス（語彙に対する確率分布）を処理するために`LogitsProcessor`を初期化します。各トークンはテンソルに変換され、モデルに渡されてロジットが取得されます。

ループはプロンプト内の各トークンを処理し、ロジットプロセッサを更新して次のトークン生成の準備をします。

## ステップ6: 推論

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

推論ループでは、指定されたサンプル長に達するか、シーケンス終了トークンに遭遇するまでトークンを一つずつ生成します。次のトークンはテンソルに変換され、モデルに渡され、ロジットが処理されてペナルティとサンプリングが適用されます。次にサンプリングされたトークンがシーケンスに追加され、デコードされます。
繰り返しテキストを避けるために、`repeat_last_n`と`repeat_penalty`のパラメータに基づいて繰り返しトークンにペナルティが適用されます。

最後に、生成されたテキストはデコードされるとリアルタイムで出力されます。

## ステップ7: アプリケーションの実行

アプリケーションを実行するには、ターミナルで以下のコマンドを実行します。

```bash
cargo run --release
```

これにより、Phi-3モデルによって生成されたアイスホッケーについての俳句が表示されます。例えば、次のようなものです。

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

または

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## 結論

これらのステップに従うことで、RustとCandleを使用してPhi-3モデルでテキスト生成を行うことができます。モデルの読み込み、トークナイズ、推論を処理し、入力プロンプトに基づいて一貫したテキストを生成するためにテンソルとロジット処理を活用しています。

このコンソールアプリケーションはWindows、Linux、Mac OSで実行できます。Rustのポータビリティのおかげで、コードはモバイルアプリ内で実行されるライブラリに適応させることもできます（コンソールアプリは実行できませんが）。

## 付録: 完全なコード

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

Note: in order to run this code on aarch64 Linux or aarch64 Windows, add a file named `.cargo/config` with the following content:

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

> You can visit the official [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository for more examples on how to use the Phi-3 model with Rust and Candle, including alternative approaches to inference.

免責事項: この翻訳はAIモデルによって元の言語から翻訳されたものであり、完全ではない可能性があります。 出力を確認し、必要な修正を行ってください。