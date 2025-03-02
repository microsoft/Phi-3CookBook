# Cross-platform inference gamit ang Rust

Ang tutorial na ito ay magtuturo sa atin kung paano magsagawa ng inference gamit ang Rust at ang [Candle ML framework](https://github.com/huggingface/candle) mula sa HuggingFace. Ang paggamit ng Rust para sa inference ay may maraming benepisyo, lalo na kung ikukumpara sa ibang programming languages. Kilala ang Rust para sa mataas nitong performance, na maihahambing sa C at C++. Ginagawa nitong angkop ang Rust para sa inference tasks na madalas nangangailangan ng mataas na computational power. Partikular itong naisasagawa dahil sa zero-cost abstractions at mahusay na memory management na walang overhead mula sa garbage collection. Ang kakayahan ng Rust na maging cross-platform ay nagbibigay-daan sa paggawa ng code na tumatakbo sa iba't ibang operating systems tulad ng Windows, macOS, at Linux, pati na rin sa mga mobile operating systems, nang hindi nangangailangan ng malaking pagbabago sa codebase.

Ang kinakailangan para masundan ang tutorial na ito ay ang [pag-install ng Rust](https://www.rust-lang.org/tools/install), na kasama ang Rust compiler at Cargo, ang package manager ng Rust.

## Hakbang 1: Gumawa ng Bagong Rust Project

Upang makagawa ng bagong Rust project, patakbuhin ang sumusunod na command sa terminal:

```bash
cargo new phi-console-app
```

Magkakaroon ito ng paunang project structure na may `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` na file:

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

## Hakbang 2: I-configure ang Pangunahing Parameters

Sa loob ng main.rs file, itatakda natin ang mga paunang parameters para sa inference. Ang mga ito ay magiging hardcoded para sa kasimplehan, ngunit maaari natin itong baguhin kung kinakailangan.

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

- **temperature**: Kinokontrol ang randomness ng sampling process.
- **sample_len**: Nagtatakda ng maximum na haba ng generated na teksto.
- **top_p**: Ginagamit para sa nucleus sampling upang limitahan ang bilang ng tokens na isinasaalang-alang sa bawat hakbang.
- **repeat_last_n**: Kinokontrol ang bilang ng tokens na isinasaalang-alang para mag-apply ng penalty upang maiwasan ang paulit-ulit na sequences.
- **repeat_penalty**: Ang halaga ng penalty para pigilan ang pag-uulit ng mga tokens.
- **seed**: Isang random seed (maaari tayong gumamit ng constant value para sa mas reproducible na resulta).
- **prompt**: Ang paunang prompt na teksto upang simulan ang generation. Pansinin na hinihingi natin sa model na gumawa ng haiku tungkol sa ice hockey, at ini-wrap natin ito ng espesyal na tokens para ipakita ang bahagi ng user at assistant sa usapan. Kukumpletuhin ng model ang prompt gamit ang isang haiku.
- **device**: Ginagamit natin ang CPU para sa computation sa halimbawang ito. Sinusuportahan ng Candle ang pagtakbo sa GPU gamit ang CUDA at Metal.

## Hakbang 3: I-download/Ihanda ang Model at Tokenizer

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

Ginagamit natin ang `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` file para sa pag-tokenize ng ating input text. Kapag na-download na, naka-cache ang model, kaya ang unang execution ay maaaring mabagal (dahil ida-download nito ang 2.4GB ng model) ngunit ang mga susunod na executions ay magiging mas mabilis.

## Hakbang 4: I-load ang Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Ilo-load natin ang quantized model weights sa memory at i-initialize ang Phi-3 model. Ang hakbang na ito ay kinabibilangan ng pagbabasa ng model weights mula sa `gguf` file at pag-setup ng model para sa inference sa tinukoy na device (CPU sa kasong ito).

## Hakbang 5: Iproseso ang Prompt at Ihanda para sa Inference

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

Sa hakbang na ito, ang input prompt ay tinotokenize at inihahanda para sa inference sa pamamagitan ng pag-convert nito sa isang sequence ng token IDs. Ini-initialize din natin ang `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` values. Ang bawat token ay kino-convert sa tensor at pinapasa sa model upang makuha ang logits.

Ang loop ay nagpoproseso ng bawat token sa prompt, ina-update ang logits processor, at inihahanda para sa susunod na token generation.

## Hakbang 6: Inference

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

Sa inference loop, gumagawa tayo ng tokens isa-isa hanggang maabot ang nais na sample length o makatagpo ng end-of-sequence token. Ang susunod na token ay kino-convert sa tensor at pinapasa sa model, habang ang logits ay pinoproseso upang mag-apply ng penalties at sampling. Ang susunod na token ay sinasample, dine-decode, at idinadagdag sa sequence. 

Upang maiwasan ang paulit-ulit na teksto, ang penalty ay ina-apply sa mga repeated tokens batay sa `repeat_last_n` and `repeat_penalty` parameters.

Sa wakas, ang generated na teksto ay ipinapakita habang ito ay dine-decode, na nagbibigay ng streamed real-time output.

## Hakbang 7: Patakbuhin ang Application

Upang patakbuhin ang application, isagawa ang sumusunod na command sa terminal:

```bash
cargo run --release
```

Dapat nitong ipakita ang isang haiku tungkol sa ice hockey na ginawa ng Phi-3 model. Halimbawa:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

o

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Konklusyon

Sa pagsunod sa mga hakbang na ito, maaari tayong magsagawa ng text generation gamit ang Phi-3 model sa Rust at Candle sa ilalim ng 100 linya ng code. Ang code ay humahawak sa model loading, tokenization, at inference, gamit ang tensors at logits processing upang makabuo ng coherent na teksto base sa input prompt.

Ang console application na ito ay maaaring tumakbo sa Windows, Linux, at Mac OS. Dahil sa portability ng Rust, ang code ay maaari ding i-adapt sa isang library na tatakbo sa loob ng mga mobile apps (hindi kasi puwedeng tumakbo ang console apps doon).

## Appendix: Buong Code

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

Tandaan: upang patakbuhin ang code na ito sa aarch64 Linux o aarch64 Windows, magdagdag ng file na pinangalanang `.cargo/config` na may sumusunod na nilalaman:

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

> Maaari mong bisitahin ang opisyal na [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) repository para sa mas maraming halimbawa kung paano gamitin ang Phi-3 model gamit ang Rust at Candle, kabilang ang mga alternatibong paraan ng inference.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI-based na pagsasalin. Bagama't sinisikap naming maging wasto, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling ginawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.