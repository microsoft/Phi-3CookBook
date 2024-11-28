# Rustを使ったクロスプラットフォーム推論

このチュートリアルでは、HuggingFaceの[Candle MLフレームワーク](https://github.com/huggingface/candle)を使用してRustで推論を行う手順を紹介します。Rustを使用することで、他のプログラミング言語と比較していくつかの利点があります。RustはCやC++に匹敵する高いパフォーマンスで知られており、計算量の多い推論タスクに適しています。特に、ゼロコスト抽象化と効率的なメモリ管理により、ガベージコレクションのオーバーヘッドがないことが大きな要因です。Rustのクロスプラットフォーム機能により、Windows、macOS、Linux、さらにはモバイルOSなど、さまざまなオペレーティングシステムで動作するコードを大きな変更なしに開発することができます。

このチュートリアルを進めるための前提条件として、[Rustをインストール](https://www.rust-lang.org/tools/install)する必要があります。これにはRustコンパイラとパッケージマネージャであるCargoが含まれます。

## ステップ1: 新しいRustプロジェクトを作成する

新しいRustプロジェクトを作成するには、ターミナルで以下のコマンドを実行します。

```bash
cargo new phi-console-app
```

これにより、`Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml`ファイルを含む初期プロジェクト構造が生成されます。

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

main.rsファイル内で、推論のための初期パラメータを設定します。これらは簡単のためにハードコードされていますが、必要に応じて変更することができます。

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
- **repeat_last_n**: 繰り返しのシーケンスを防ぐためにペナルティを適用するトークンの数を制御します。
- **repeat_penalty**: 繰り返しトークンを抑制するためのペナルティ値です。
- **seed**: ランダムシード（再現性を高めるために一定の値を使用できます）。
- **prompt**: 生成を開始するための初期プロンプトテキストです。アイスホッケーについての俳句を生成するようモデルに指示し、会話のユーザーとアシスタントの部分を示す特別なトークンで囲みます。モデルはプロンプトを完了し、俳句を生成します。
- **device**: この例では計算にCPUを使用します。CandleはCUDAおよびMetalを使用してGPU上での実行もサポートしています。

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

`hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json`ファイルは、入力テキストのトークン化に使用されます。ダウンロード後、モデルはキャッシュされるため、最初の実行は遅くなりますが（2.4GBのモデルをダウンロードするため）、その後の実行は速くなります。

## ステップ4: モデルのロード

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

量子化されたモデルの重みをメモリにロードし、Phi-3モデルを初期化します。このステップでは、`gguf`ファイルからモデルの重みを読み込み、指定されたデバイス（この場合はCPU）で推論を行うためのモデルを設定します。

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

このステップでは、入力プロンプトをトークン化し、トークンIDのシーケンスに変換して推論の準備を行います。また、`LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`の値を初期化します。各トークンはテンソルに変換され、モデルを通じてロジットを取得します。

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

推論ループでは、指定されたサンプル長に達するか、シーケンスの終了トークンに出会うまで、トークンを1つずつ生成します。次のトークンはテンソルに変換され、モデルを通じてロジットが処理され、ペナルティとサンプリングが適用されます。その後、次のトークンがサンプリングされ、デコードされ、シーケンスに追加されます。
繰り返しのテキストを避けるために、`repeat_last_n` and `repeat_penalty`パラメータに基づいて繰り返しトークンにペナルティが適用されます。

最後に、生成されたテキストがデコードされると同時にリアルタイムで出力されます。

## ステップ7: アプリケーションの実行

アプリケーションを実行するには、ターミナルで以下のコマンドを実行します。

```bash
cargo run --release
```

これにより、Phi-3モデルによって生成されたアイスホッケーに関する俳句が出力されます。例えば：

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

これらの手順に従うことで、100行未満のコードでRustとCandleを使用してPhi-3モデルを用いたテキスト生成を行うことができます。このコードはモデルのロード、トークン化、推論を処理し、入力プロンプトに基づいて一貫したテキストを生成します。

このコンソールアプリケーションは、Windows、Linux、およびMac OSで動作します。Rustのポータビリティにより、このコードはモバイルアプリ内で実行されるライブラリに適応することもできます（コンソールアプリは実行できないため）。

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

注：aarch64 Linuxまたはaarch64 Windowsでこのコードを実行するには、次の内容のファイル `.cargo/config` を追加します。

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

> 公式の[Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs)リポジトリには、RustとCandleを使用してPhi-3モデルを使用する方法の他の例が掲載されています。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご理解ください。元の言語で記載された原文が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈について、当社は一切の責任を負いかねます。