# Utoaji wa Majukwaa Mbalimbali kwa kutumia Rust

Mafunzo haya yatatuongoza katika mchakato wa kufanya utoaji (inference) kwa kutumia Rust na [Mfumo wa Candle ML](https://github.com/huggingface/candle) kutoka HuggingFace. Kutumia Rust kwa ajili ya utoaji kuna faida kadhaa, hasa ikilinganishwa na lugha nyingine za programu. Rust inajulikana kwa utendaji wake wa hali ya juu, unaolinganishwa na ule wa C na C++. Hii inafanya kuwa chaguo bora kwa kazi za utoaji, ambazo mara nyingi huhitaji rasilimali kubwa za kompyuta. Hasa, hii inatokana na ufanisi wa Rust katika usimamizi wa kumbukumbu na "zero-cost abstractions," ambayo haina mzigo wa ukusanyaji taka. Uwezo wa Rust wa kufanya kazi kwenye majukwaa mbalimbali huwezesha maendeleo ya msimbo unaoweza kuendeshwa kwenye mifumo mbalimbali ya uendeshaji, ikiwa ni pamoja na Windows, macOS, na Linux, pamoja na mifumo ya uendeshaji ya simu bila mabadiliko makubwa kwenye msimbo.

Sharti la kufuata mafunzo haya ni [kufunga Rust](https://www.rust-lang.org/tools/install), ambayo inajumuisha kiunzi cha Rust na Cargo, msimamizi wa pakiti wa Rust.

## Hatua ya 1: Unda Mradi Mpya wa Rust

Ili kuunda mradi mpya wa Rust, endesha amri ifuatayo kwenye terminal:

```bash
cargo new phi-console-app
```

Hii itazalisha muundo wa awali wa mradi wenye faili `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Hatua ya 2: Sanidi Vigezo vya Msingi

Ndani ya faili ya main.rs, tutaweka vigezo vya awali kwa ajili ya utoaji wetu. Vigezo vyote vitakuwa vimeandikwa moja kwa moja kwa urahisi, lakini tunaweza kuvitengeneza kama tunavyohitaji.

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

- **temperature**: Hudhibiti nasibu ya mchakato wa sampuli.
- **sample_len**: Hueleza urefu wa juu zaidi wa maandishi yanayozalishwa.
- **top_p**: Hutumika kwa sampuli ya nucleus ili kupunguza idadi ya tokeni zinazozingatiwa kwa kila hatua.
- **repeat_last_n**: Hudhibiti idadi ya tokeni zinazozingatiwa kwa kutumia adhabu ili kuzuia marudio ya mfuatano.
- **repeat_penalty**: Thamani ya adhabu inayotumika kuzuia tokeni zinazojirudia.
- **seed**: Mbegu ya nasibu (tunaweza kutumia thamani isiyobadilika kwa urahisi wa kurudia matokeo).
- **prompt**: Maandishi ya awali ya kuanzisha kizazi. Angalia kuwa tunaomba mfano kuzalisha haiku kuhusu mchezo wa hockey ya barafu, na tunazungushia maandishi haya na tokeni maalum kuonyesha sehemu za mtumiaji na msaidizi wa mazungumzo. Mfano utaendeleza prompt kwa haiku.
- **device**: Katika mfano huu, tunatumia CPU kwa ajili ya hesabu. Candle inasaidia kuendesha kwenye GPU kwa kutumia CUDA na Metal pia.

## Hatua ya 3: Pakua/Andaa Mfano na Tokenizer

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

Tunatumia faili `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` kwa ajili ya kugawa maandishi yetu ya kuingiza. Mara baada ya kupakuliwa, mfano unahifadhiwa, hivyo utekelezaji wa kwanza utakuwa wa polepole (kwa sababu unapakua mfano wa 2.4GB) lakini utekelezaji wa baadaye utakuwa wa haraka zaidi.

## Hatua ya 4: Pakia Mfano

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Tunapakia uzito wa mfano uliokadiriwa kwenye kumbukumbu na kuanzisha mfano wa Phi-3. Hatua hii inahusisha kusoma uzito wa mfano kutoka faili ya `gguf` na kuandaa mfano kwa ajili ya utoaji kwenye kifaa kilichobainishwa (CPU katika mfano huu).

## Hatua ya 5: Shughulikia Prompt na Andaa kwa Utoaji

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

Katika hatua hii, tunagawa prompt ya kuingiza na kuandaa kwa ajili ya utoaji kwa kuibadilisha kuwa mlolongo wa vitambulisho vya tokeni. Pia tunaanzisha `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Kila tokeni inabadilishwa kuwa tensor na kupitishwa kwenye mfano ili kupata logits.

Mzunguko hushughulikia kila tokeni katika prompt, kusasisha mchakato wa logits na kujiandaa kwa kizazi cha tokeni kinachofuata.

## Hatua ya 6: Utoaji

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

Katika mzunguko wa utoaji, tunazalisha tokeni moja baada ya nyingine hadi tufikie urefu wa sampuli uliotakiwa au tukutane na tokeni ya mwisho wa mlolongo. Tokeni inayofuata inabadilishwa kuwa tensor na kupitishwa kwenye mfano, huku logits zikichakatwa ili kutumia adhabu na sampuli. Kisha tokeni inayofuata inachaguliwa, kufasiriwa, na kuongezwa kwenye mlolongo.

Ili kuepuka maandishi yanayojirudia, adhabu inatumika kwa tokeni zilizorudiwa kulingana na vigezo vya `repeat_last_n` and `repeat_penalty`.

Hatimaye, maandishi yanayozalishwa yanachapishwa mara yanapofasiriwa, kuhakikisha matokeo yanatolewa papo hapo.

## Hatua ya 7: Endesha Programu

Ili kuendesha programu, tekeleza amri ifuatayo kwenye terminal:

```bash
cargo run --release
```

Hii inapaswa kuchapisha haiku kuhusu mchezo wa hockey ya barafu uliotolewa na mfano wa Phi-3. Inaweza kuwa kitu kama:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

au

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Hitimisho

Kwa kufuata hatua hizi, tunaweza kufanya kizazi cha maandishi kwa kutumia mfano wa Phi-3 na Rust pamoja na Candle kwa chini ya mistari 100 ya msimbo. Msimbo hushughulikia upakiaji wa mfano, ugawaji, na utoaji, ukitumia tensors na uchakataji wa logits kuzalisha maandishi yenye maana kulingana na prompt ya kuingiza.

Programu hii ya console inaweza kuendeshwa kwenye Windows, Linux, na Mac OS. Kwa sababu ya uwezo wa Rust wa kufanya kazi kwenye majukwaa mbalimbali, msimbo unaweza pia kubadilishwa kuwa maktaba inayoweza kuendeshwa ndani ya programu za simu (hatuwezi kuendesha programu za console huko, baada ya yote).

## Kiambatisho: msimbo kamili

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

Kumbuka: ili kuendesha msimbo huu kwenye Linux ya aarch64 au Windows ya aarch64, ongeza faili iitwayo `.cargo/config` yenye maudhui yafuatayo:

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

> Unaweza kutembelea [Mifano rasmi ya Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) kwa mifano zaidi ya jinsi ya kutumia mfano wa Phi-3 na Rust pamoja na Candle, ikijumuisha njia mbadala za utoaji.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotumia mashine. Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.