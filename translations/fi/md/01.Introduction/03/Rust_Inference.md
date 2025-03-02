# Ristikkäisalustainen päättely Rustilla

Tässä opetusohjelmassa käymme läpi, miten suorittaa päättelyä käyttämällä Rustia ja [Candle ML -kehystä](https://github.com/huggingface/candle) HuggingFacelta. Rustin käyttäminen päättelyyn tarjoaa useita etuja, erityisesti verrattuna muihin ohjelmointikieliin. Rust tunnetaan korkeasta suorituskyvystään, joka on verrattavissa C:hen ja C++:aan. Tämä tekee siitä erinomaisen valinnan päättelytehtäviin, jotka voivat olla laskennallisesti raskaita. Tämä perustuu erityisesti kustannuksiltaan nollaan meneviin abstraktioihin ja tehokkaaseen muistin hallintaan, jossa ei ole roskankeruun aiheuttamaa kuormitusta. Rustin ristiin toimivat ominaisuudet mahdollistavat koodin kehittämisen, joka toimii useissa käyttöjärjestelmissä, kuten Windowsissa, macOS:ssa ja Linuxissa, sekä mobiilikäyttöjärjestelmissä ilman merkittäviä muutoksia koodiin.

Tämän opetusohjelman seuraamisen edellytys on [Rustin asentaminen](https://www.rust-lang.org/tools/install), joka sisältää Rust-kääntäjän ja Cargo-pakettienhallinnan.

## Vaihe 1: Luo uusi Rust-projekti

Luo uusi Rust-projekti suorittamalla seuraava komento terminaalissa:

```bash
cargo new phi-console-app
```

Tämä luo alkuperäisen projektirakenteen, jossa on `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` tiedosto:

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

## Vaihe 2: Määritä perusparametrit

Main.rs-tiedoston sisällä asetamme päättelyn alkuparametrit. Ne kovakoodataan yksinkertaisuuden vuoksi, mutta niitä voidaan muokata tarpeen mukaan.

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

- **temperature**: Kontrolloi näytteenoton satunnaisuutta.
- **sample_len**: Määrittää tuotetun tekstin maksimipituuden.
- **top_p**: Käytetään "nucleus sampling" -menetelmässä rajoittamaan kussakin vaiheessa huomioon otettavien tokenien määrää.
- **repeat_last_n**: Määrittää, kuinka monta viimeistä tokenia otetaan huomioon rangaistuksen soveltamiseksi toistuvien sekvenssien estämiseksi.
- **repeat_penalty**: Rangaistuskerroin, joka estää toistuvia tokeneita.
- **seed**: Satunnaissiementä (voimme käyttää vakioarvoa paremman toistettavuuden saavuttamiseksi).
- **prompt**: Alustava kehoteteksti, jolla tekstin generointi aloitetaan. Huomaa, että pyydämme mallia luomaan haikun jääkiekosta ja että ympäröimme sen erityisillä käyttäjän ja avustajan vuoropuhelua kuvaavilla tokeneilla. Malli täydentää kehotteen haikulla.
- **device**: Tässä esimerkissä käytämme laskentaan CPU:ta. Candle tukee myös GPU:ta CUDA:n ja Metalin avulla.

## Vaihe 3: Lataa/valmistele malli ja tokenisaattori

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

Käytämme `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` tiedostoa syötteen tokenisointiin. Kun malli on ladattu, se välimuistitetaan, joten ensimmäinen suoritus on hidas (koska malli, kooltaan 2,4 GB, ladataan), mutta seuraavat suoritukset ovat nopeampia.

## Vaihe 4: Lataa malli

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Lataamme kvantisoidut mallipainot muistiin ja alustamme Phi-3-mallin. Tämä vaihe sisältää mallipainojen lukemisen `gguf`-tiedostosta ja mallin asettamisen päättelyä varten määritetylle laitteelle (tässä tapauksessa CPU).

## Vaihe 5: Esikäsittele kehotus ja valmistele päättelyä varten

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

Tässä vaiheessa tokenisoimme syötekehotteen ja valmistelemme sen päättelyä varten muuntamalla sen token-ID-sekvenssiksi. Lisäksi alustamme `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` arvot. Jokainen token muunnetaan tensoriksi ja syötetään malliin logiittien saamiseksi.

Silmukka käsittelee jokaisen kehotteen tokenin, päivittää logiittiprosessorin ja valmistautuu seuraavan tokenin generointiin.

## Vaihe 6: Päättely

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

Päättelysilmukassa generoidaan tokeneita yksi kerrallaan, kunnes saavutetaan haluttu näytteen pituus tai kohdataan sekvenssin päättävä token. Seuraava token muunnetaan tensoriksi ja syötetään malliin, samalla kun logiitteja käsitellään rangaistusten ja näytteenoton soveltamiseksi. Tämän jälkeen seuraava token valitaan, dekoodataan ja lisätään sekvenssiin.
Toistuvan tekstin välttämiseksi toistuville tokeneille sovelletaan rangaistusta `repeat_last_n` and `repeat_penalty` parametrien mukaisesti.

Lopuksi generoitu teksti tulostetaan dekoodattuna, mikä varmistaa reaaliaikaisen suoratoiston.

## Vaihe 7: Suorita sovellus

Suorita sovellus antamalla seuraava komento terminaalissa:

```bash
cargo run --release
```

Tämän pitäisi tulostaa Phi-3-mallin generoima haiku jääkiekosta. Esimerkiksi:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

tai

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Yhteenveto

Noudattamalla näitä vaiheita voimme suorittaa tekstin generointia Phi-3-mallilla Rustin ja Candlen avulla alle 100 koodirivillä. Koodi hoitaa mallin lataamisen, tokenisoinnin ja päättelyn hyödyntäen tensoreita ja logiittien käsittelyä luodakseen johdonmukaista tekstiä syötteen perusteella.

Tämä konsolisovellus toimii Windowsissa, Linuxissa ja Mac OS:ssa. Rustin siirrettävyyden ansiosta koodi voidaan myös mukauttaa kirjastoksi, joka toimii mobiilisovelluksissa (konsolisovelluksia ei voida käyttää siellä).

## Liite: koko koodi

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

Huom: Jos haluat suorittaa tämän koodin aarch64 Linuxilla tai aarch64 Windowsilla, lisää tiedosto nimeltä `.cargo/config`, jossa on seuraava sisältö:

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

> Voit vierailla virallisessa [Candlen esimerkkikoodien](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) arkistossa saadaksesi lisää esimerkkejä Phi-3-mallin käytöstä Rustin ja Candlen kanssa, mukaan lukien vaihtoehtoisia lähestymistapoja päättelyyn.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisten tekoälyyn perustuvien käännöspalveluiden avulla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.