# Keresztplatformos következtetés Rusttal

Ez az útmutató bemutatja, hogyan végezhetünk következtetést Rust és a HuggingFace által készített [Candle ML keretrendszer](https://github.com/huggingface/candle) segítségével. A Rust használata következtetéshez számos előnnyel jár, különösen más programozási nyelvekkel összehasonlítva. A Rust híres a magas teljesítményéről, amely összehasonlítható a C és C++ nyelvekével. Ez kiváló választássá teszi a számításigényes következtetési feladatokhoz. Ezt különösen a költségmentes absztrakciók és a hatékony memóriakezelés teszi lehetővé, amely nem jár szemétgyűjtési többletköltséggel. A Rust keresztplatformos képességei lehetővé teszik olyan kód fejlesztését, amely különböző operációs rendszereken, például Windows, macOS és Linux, valamint mobil operációs rendszereken is fut, jelentős kódbázis-módosítás nélkül.

Az útmutató követéséhez előfeltétel a [Rust telepítése](https://www.rust-lang.org/tools/install), amely tartalmazza a Rust fordítót és a Cargo-t, a Rust csomagkezelőt.

## 1. lépés: Hozz létre egy új Rust projektet

Új Rust projekt létrehozásához futtasd a következő parancsot a terminálban:

```bash
cargo new phi-console-app
```

Ez létrehoz egy kezdeti projektstruktúrát egy `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` fájllal:

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

## 2. lépés: Alapvető paraméterek beállítása

A `main.rs` fájlban beállítjuk a következtetéshez szükséges alapvető paramétereket. Ezeket egyszerűség kedvéért kódba égetjük, de igény szerint módosíthatók.

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

- **temperature**: Szabályozza a mintavételi folyamat véletlenszerűségét.
- **sample_len**: Meghatározza a generált szöveg maximális hosszát.
- **top_p**: Nukleusz-mintavételhez használatos, hogy korlátozza az egyes lépésekben figyelembe vett tokenek számát.
- **repeat_last_n**: Meghatározza, hány tokent vegyünk figyelembe ismétlődési büntetés alkalmazásához.
- **repeat_penalty**: Az ismétlődő tokenek büntetésének mértéke.
- **seed**: Egy véletlenszám-generátor magja (állandó értéket használhatunk a jobb reprodukálhatóság érdekében).
- **prompt**: A szöveg-generálás kezdő szövege. Észrevehető, hogy egy jégkorongról szóló haikut kérünk a modelltől, amelyet speciális tokenekkel zárunk be, hogy jelezzük a felhasználó és az asszisztens párbeszédének részeit. A modell ezután a promptot egy haikuval egészíti ki.
- **device**: Ebben a példában a CPU-t használjuk számításra. A Candle támogatja a GPU használatát CUDA és Metal segítségével.

## 3. lépés: Modell és tokenizáló letöltése/előkészítése

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

A `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` fájlt a bemeneti szöveg tokenizálására használjuk. Miután letöltöttük, a modell gyorsítótárba kerül, így az első futtatás lassabb lesz (mivel letölti a modell 2,4 GB-os fájlját), de a következő futtatások gyorsabbak lesznek.

## 4. lépés: Modell betöltése

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Betöltjük a kvantált modell súlyait a memóriába, és inicializáljuk a Phi-3 modellt. Ez a lépés magában foglalja a `gguf` fájlból származó modell-súlyok beolvasását és a modell előkészítését következtetésre a megadott eszközön (jelen esetben CPU).

## 5. lépés: Prompt feldolgozása és előkészítése következtetésre

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

Ebben a lépésben tokenizáljuk a bemeneti promptot, és előkészítjük következtetésre úgy, hogy tokenazonosítók sorozatává alakítjuk. Emellett inicializáljuk a `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` értékeket. Minden tokent tensorrá alakítunk, majd a modellen keresztülhaladva megkapjuk a logits értékeket.

A ciklus feldolgozza a prompt minden tokenjét, frissíti a logits processzort, és előkészíti a következő token generálását.

## 6. lépés: Következtetés

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

A következtetési ciklusban egyenként generáljuk a tokeneket, amíg el nem érjük a kívánt mintavételi hosszúságot, vagy meg nem találjuk a szekvencia végét jelző tokent. A következő tokent tensorrá alakítjuk, és a modellen keresztülhaladva feldolgozzuk a logits értékeket, hogy alkalmazzuk a büntetéseket és a mintavételt. Ezután a következő tokent kiválasztjuk, dekódoljuk, és hozzáadjuk a szekvenciához. 

Az ismétlődő szöveg elkerülése érdekében büntetést alkalmazunk az ismétlődő tokenekre a `repeat_last_n` and `repeat_penalty` paraméterek alapján.

Végül a generált szöveget valós időben kiírjuk, ahogy dekódoljuk.

## 7. lépés: Az alkalmazás futtatása

Az alkalmazás futtatásához használd a következő parancsot a terminálban:

```bash
cargo run --release
```

Ez kiír egy jégkorongról szóló haikut, amelyet a Phi-3 modell generált. Például:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

vagy

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Összegzés

Ezeket a lépéseket követve kevesebb mint 100 sor kóddal végezhetünk szöveggenerálást a Phi-3 modell segítségével Rust és Candle környezetben. A kód kezeli a modell betöltését, a tokenizálást és a következtetést, tensorokat és logits feldolgozást használva koherens szöveg generálásához a bemeneti prompt alapján.

Ez a konzolalkalmazás futtatható Windows, Linux és Mac OS rendszereken. A Rust hordozhatóságának köszönhetően a kód átalakítható egy olyan könyvtárrá is, amely mobilalkalmazásokban fut (hiszen konzolalkalmazásokat ott nem futtathatunk).

## Függelék: teljes kód

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

Megjegyzés: ahhoz, hogy ezt a kódot aarch64 Linux vagy aarch64 Windows rendszeren futtassuk, adjunk hozzá egy `.cargo/config` nevű fájlt a következő tartalommal:

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

> További példákért, hogyan használjuk a Phi-3 modellt Rust és Candle segítségével, látogass el a hivatalos [Candle példák](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) tárházába, amely alternatív megközelítéseket is tartalmaz a következtetéshez.

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal készült fordítást tartalmaz. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.