# Rust ile Platformlar Arası Çıkarım

Bu eğitim, HuggingFace'in [Candle ML framework'ünü](https://github.com/huggingface/candle) kullanarak Rust ile çıkarım yapma sürecini adım adım anlatacaktır. Rust ile çıkarım yapmak, diğer programlama dillerine kıyasla birçok avantaj sunar. Rust, C ve C++ ile kıyaslanabilir yüksek performansıyla tanınır. Bu, özellikle hesaplama açısından yoğun olan çıkarım görevleri için mükemmel bir seçimdir. Bu avantaj, sıfır maliyetli soyutlamalar ve çöp toplayıcı yükü olmadan etkili bellek yönetimi sayesinde sağlanır. Rust'ın platformlar arası yetenekleri, kod tabanında önemli değişiklikler yapmadan Windows, macOS, Linux ve mobil işletim sistemleri dahil olmak üzere çeşitli işletim sistemlerinde çalışan kodlar geliştirilmesine olanak tanır.

Bu eğitimi takip etmek için [Rust'ı yüklemek](https://www.rust-lang.org/tools/install) gereklidir. Bu, Rust derleyicisini ve Rust paket yöneticisi Cargo'yu içerir.

## Adım 1: Yeni Bir Rust Projesi Oluşturma

Yeni bir Rust projesi oluşturmak için terminalde aşağıdaki komutu çalıştırın:

```bash
cargo new phi-console-app
```

Bu komut, `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` dosyasını içeren bir başlangıç proje yapısı oluşturur:

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

## Adım 2: Temel Parametreleri Yapılandırma

main.rs dosyasının içinde, çıkarım için başlangıç parametrelerini ayarlayacağız. Basitlik adına tüm parametreler sabit olarak tanımlanacak, ancak gerektiğinde değiştirilebilir.

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

- **temperature**: Örnekleme sürecinin rastgeleliğini kontrol eder.
- **sample_len**: Üretilen metnin maksimum uzunluğunu belirtir.
- **top_p**: Her adımda dikkate alınan token sayısını sınırlamak için nucleus sampling kullanılır.
- **repeat_last_n**: Tekrarlayan dizileri önlemek için ceza uygulanacak token sayısını kontrol eder.
- **repeat_penalty**: Tekrarlayan tokenları caydırmak için kullanılan ceza değeri.
- **seed**: Rastgele bir tohum (daha iyi yeniden üretilebilirlik için sabit bir değer kullanabiliriz).
- **prompt**: Metin oluşturma işlemini başlatacak başlangıç metni. Modelden buz hokeyi hakkında bir haiku oluşturmasını istiyoruz ve bunu, konuşmanın kullanıcı ve asistan kısımlarını belirten özel tokenlarla çevreliyoruz. Model daha sonra prompt'u bir haiku ile tamamlayacaktır.
- **device**: Bu örnekte hesaplama için CPU kullanıyoruz. Candle, CUDA ve Metal ile GPU üzerinde çalışmayı da destekler.

## Adım 3: Model ve Tokenizer İndirme/Hazırlama

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

Girdi metnimizi tokenize etmek için `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` dosyasını kullanıyoruz. Model indirildikten sonra önbelleğe alınır, bu nedenle ilk çalıştırma yavaş olacaktır (modelin 2.4GB'ını indirir), ancak sonraki çalıştırmalar daha hızlı olacaktır.

## Adım 4: Model Yükleme

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Kuantize edilmiş model ağırlıklarını belleğe yükler ve Phi-3 modelini başlatırız. Bu adım, `gguf` dosyasından model ağırlıklarını okumayı ve belirli cihaz (bu durumda CPU) üzerinde çıkarım için modeli kurmayı içerir.

## Adım 5: Prompt'u İşleme ve Çıkarıma Hazırlık

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

Bu adımda, giriş prompt'unu tokenize eder ve çıkarım için bir token kimlikleri dizisine dönüştürürüz. Ayrıca `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` değerlerini başlatırız. Her bir token bir tensöre dönüştürülür ve modelden logits almak için işlenir.

Döngü, prompt'taki her bir tokenı işler, logits işlemcisini günceller ve bir sonraki token oluşturma için hazırlar.

## Adım 6: Çıkarım

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

Çıkarım döngüsünde, istenen örnek uzunluğuna ulaşana veya bir dizinin sonu tokenına ulaşana kadar tokenlar birer birer üretilir. Sonraki token bir tensöre dönüştürülür ve modele geçirilir, logits işlenir ve cezalar ve örnekleme uygulanır. Ardından sonraki token örneklenir, çözümlenir ve dizine eklenir.
Tekrarlayan metinleri önlemek için `repeat_last_n` and `repeat_penalty` parametrelerine dayalı olarak tekrarlanan tokenlara bir ceza uygulanır.

Son olarak, oluşturulan metin gerçek zamanlı çıktı sağlamak için çözülerek yazdırılır.

## Adım 7: Uygulamayı Çalıştırma

Uygulamayı çalıştırmak için terminalde aşağıdaki komutu çalıştırın:

```bash
cargo run --release
```

Bu, Phi-3 modeli tarafından oluşturulan buz hokeyi hakkında bir haiku yazdırmalıdır. Örneğin:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

veya

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Sonuç

Bu adımları takip ederek, Rust ve Candle ile Phi-3 modelini kullanarak 100 satırdan daha az kodla metin oluşturma işlemi gerçekleştirebiliriz. Kod, model yükleme, tokenizasyon ve çıkarımı ele alır ve giriş prompt'una dayalı olarak tutarlı metinler oluşturmak için tensörler ve logits işlemeyi kullanır.

Bu konsol uygulaması Windows, Linux ve Mac OS üzerinde çalışabilir. Rust'ın taşınabilirliği sayesinde kod, mobil uygulamalar içinde çalışacak bir kütüphaneye de uyarlanabilir (sonuçta konsol uygulamalarını mobilde çalıştıramayız).

## Ek: Tam Kod

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

Not: Bu kodu aarch64 Linux veya aarch64 Windows üzerinde çalıştırmak için `.cargo/config` adında bir dosya oluşturup aşağıdaki içeriği ekleyin:

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

> Phi-3 modelini Rust ve Candle ile kullanmanın alternatif yaklaşımları dahil olmak üzere daha fazla örnek için resmi [Candle örnekleri](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) deposunu ziyaret edebilirsiniz.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.