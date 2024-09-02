# Rustを使用したクロスプラットフォーム推論

このチュートリアルでは、RustとHuggingFaceの[Candle MLフレームワーク](https://github.com/huggingface/candle)を使用して推論を行う方法を説明します。Rustを使用して推論を行うことには、他のプログラミング言語と比較していくつかの利点があります。Rustは高性能で知られており、CやC++に匹敵します。これにより、計算集約型の推論タスクに最適な選択肢となります。特に、ゼロコストの抽象化と効率的なメモリ管理により、ガベージコレクションのオーバーヘッドがないことが挙げられます。Rustのクロスプラットフォーム機能により、Windows、macOS、Linuxなどのさまざまなオペレーティングシステム、およびモバイルオペレーティングシステムで実行できるコードを開発できます。

このチュートリアルを進めるための前提条件は、RustコンパイラとRustパッケージマネージャーであるCargoを含む[Rustのインストール](https://www.rust-lang.org/tools/install)です。

## ステップ1: 新しいRustプロジェクトを作成する

新しいRustプロジェクトを作成するには、ターミナルで次のコマンドを実行します:

```bash
cargo new phi-console-app
```

これにより、`Cargo.toml`ファイルと`main.rs`ファイルを含む`src`ディレクトリを持つ初期プロジェクト構造が生成されます。

次に、依存関係を追加します。具体的には、`Cargo.toml`ファイルに`candle`、`hf-hub`、および`tokenizers`クレートを追加します:

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

## ステップ2: 基本パラメータの設定

`main.rs`ファイル内で、推論の初期パラメータを設定します。簡単のために、これらのパラメータはすべてハードコーディングされますが、必要に応じて変更できます。

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
- **top_p**: 各ステップで考慮されるトークンの数を制限するために使用されます。
- **repeat_last_n**: 繰り返しシーケンスを防ぐために適用されるペナルティを制御します。
- **repeat_penalty**: 繰り返しトークンを抑制するためのペナルティ値。
- **seed**: ランダムシード（再現性を高めるために一定の値を使用することもできます）。
- **prompt**: 生成を開始するための初期プロンプトテキスト。モデルにアイスホッケーについての俳句を生成するように依頼し、ユーザーとアシスタントの会話部分を示す特殊なトークンでラップします。モデルはプロンプトを完了し、俳句を生成します。
- **device**: この例では、計算にCPUを使用します。CandleはCUDAおよびMetalを使用してGPUでの実行もサポートしています。

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

`hf_hub` APIを使用して、Hugging Faceモデルハブからモデルとトークナイザーファイルをダウンロードします。`gguf`ファイルには量子化されたモデルの重みが含まれており、`tokenizer.json`ファイルは入力テキストのトークン化に使用されます。モデルがダウンロードされるとキャッシュされるため、最初の実行は遅くなりますが（モデルの2.4GBをダウンロードするため）、後続の実行は高速になります。

## ステップ4: モデルの読み込み

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

量子化されたモデルの重みをメモリにロードし、Phi-3モデルを初期化します。このステップでは、`gguf`ファイルからモデルの重みを読み取り、指定されたデバイス（この場合はCPU）で推論のためにモデルを設定します。

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

このステップでは、入力プロンプトをトークン化し、トークンIDのシーケンスに変換して推論の準備を行います。また、`LogitsProcessor`を初期化して、指定された`temperature`および`top_p`値に基づいてサンプリングプロセス（語彙全体の確率分布）を処理します。各トークンはテンソルに変換され、モデルを通じてロジットを取得します。

ループはプロンプト内の各トークンを処理し、ロジットプロセッサを更新して次のトークン生成の準備を行います。

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

推論ループでは、所望のサンプル長に達するか、シーケンス終了トークンに遭遇するまで、トークンを1つずつ生成します。次のトークンはテンソルに変換され、モデルを通じてロジットが処理され、ペナルティとサンプリングが適用されます。次のトークンがサンプリングされ、デコードされ、シーケンスに追加されます。
繰り返しのテキストを避けるために、`repeat_last_n`および`repeat_penalty`パラメータに基づいて繰り返しトークンにペナルティが適用されます。

最後に、生成されたテキストはデコードされるときにリアルタイムで出力されます。

## ステップ7: アプリケーションの実行

アプリケーションを実行するには、ターミナルで次のコマンドを実行します:

```bash
cargo run --release
```

これにより、Phi-3モデルによって生成されたアイスホッケーに関する俳句が出力されます。例えば:

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

これらの手順に従うことで、RustとCandleを使用してPhi-3モデルを使用したテキスト生成を100行未満のコードで実行できます。コードはモデルの読み込み、トークン化、および推論を処理し、テンソルとロジット処理を活用して入力プロンプトに基づいて一貫したテキストを生成します。

このコンソールアプリケーションは、Windows、Linux、およびMac OSで実行できます。Rustの移植性により、このコードはモバイルアプリ内で実行されるライブラリに適応させることもできます（モバイルアプリではコンソールアプリを実行できないため）。

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

注意: このコードをaarch64 Linuxまたはaarch64 Windowsで実行するには、次の内容の`.cargo/config`ファイルを追加します:

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

> RustとCandleを使用してPhi-3モデルを使用する方法についての詳細な例については、公式の[Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)リポジトリを参照してください。
