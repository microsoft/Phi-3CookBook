# Inferensi Lintas Platform dengan Rust

Tutorial ini akan memandu kita melalui proses melakukan inferensi menggunakan Rust dan [Candle ML framework](https://github.com/huggingface/candle) dari HuggingFace. Menggunakan Rust untuk inferensi menawarkan beberapa keuntungan, terutama jika dibandingkan dengan bahasa pemrograman lainnya. Rust dikenal dengan performanya yang tinggi, setara dengan C dan C++. Hal ini menjadikannya pilihan yang sangat baik untuk tugas inferensi yang sering kali memerlukan komputasi intensif. Secara khusus, ini didorong oleh abstraksi tanpa biaya tambahan dan manajemen memori yang efisien tanpa overhead garbage collection. Kemampuan lintas platform Rust memungkinkan pengembangan kode yang dapat berjalan di berbagai sistem operasi, termasuk Windows, macOS, dan Linux, serta sistem operasi seluler, tanpa perubahan signifikan pada basis kode.

Prasyarat untuk mengikuti tutorial ini adalah [menginstal Rust](https://www.rust-lang.org/tools/install), yang mencakup compiler Rust dan Cargo, manajer paket Rust.

## Langkah 1: Buat Proyek Rust Baru

Untuk membuat proyek Rust baru, jalankan perintah berikut di terminal:

```bash
cargo new phi-console-app
```

Ini akan menghasilkan struktur proyek awal dengan file `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Langkah 2: Konfigurasikan Parameter Dasar

Di dalam file `main.rs`, kita akan mengatur parameter awal untuk inferensi. Semuanya akan di-hardcode untuk kesederhanaan, tetapi kita dapat memodifikasinya sesuai kebutuhan.

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

- **temperature**: Mengontrol tingkat keacakan dalam proses sampling.
- **sample_len**: Menentukan panjang maksimum teks yang dihasilkan.
- **top_p**: Digunakan untuk nucleus sampling untuk membatasi jumlah token yang dipertimbangkan pada setiap langkah.
- **repeat_last_n**: Mengontrol jumlah token yang dipertimbangkan untuk menerapkan penalti agar mencegah urutan yang berulang.
- **repeat_penalty**: Nilai penalti untuk mencegah token yang berulang.
- **seed**: Sebuah seed acak (kita dapat menggunakan nilai konstan untuk reproduksibilitas yang lebih baik).
- **prompt**: Teks prompt awal untuk memulai generasi. Perhatikan bahwa kita meminta model untuk membuat haiku tentang hoki es, dan kita membungkusnya dengan token khusus untuk menunjukkan bagian pengguna dan asisten dalam percakapan. Model kemudian akan melengkapi prompt dengan haiku.
- **device**: Kita menggunakan CPU untuk komputasi dalam contoh ini. Candle mendukung penggunaan GPU dengan CUDA dan Metal juga.

## Langkah 3: Unduh/Persiapkan Model dan Tokenizer

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

Kita menggunakan file `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` untuk melakukan tokenisasi teks input kita. Setelah diunduh, model akan disimpan dalam cache, sehingga eksekusi pertama mungkin lambat (karena mengunduh model sebesar 2.4GB), tetapi eksekusi berikutnya akan lebih cepat.

## Langkah 4: Muat Model

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Kita memuat bobot model yang telah di-kuantisasi ke dalam memori dan menginisialisasi model Phi-3. Langkah ini melibatkan membaca bobot model dari file `gguf` dan menyiapkan model untuk inferensi pada perangkat yang ditentukan (dalam hal ini CPU).

## Langkah 5: Proses Prompt dan Persiapkan untuk Inferensi

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

Pada langkah ini, kita melakukan tokenisasi pada prompt input dan mempersiapkannya untuk inferensi dengan mengonversinya menjadi urutan ID token. Kita juga menginisialisasi `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Setiap token dikonversi menjadi tensor dan dilewatkan melalui model untuk mendapatkan logits.

Loop ini memproses setiap token dalam prompt, memperbarui logits processor, dan mempersiapkan generasi token berikutnya.

## Langkah 6: Inferensi

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

Dalam loop inferensi, kita menghasilkan token satu per satu hingga mencapai panjang sampel yang diinginkan atau menemukan token akhir urutan. Token berikutnya dikonversi menjadi tensor dan dilewatkan melalui model, sementara logits diproses untuk menerapkan penalti dan sampling. Kemudian token berikutnya diambil sampelnya, diterjemahkan, dan ditambahkan ke urutan.

Untuk menghindari teks yang berulang, penalti diterapkan pada token yang diulang berdasarkan parameter `repeat_last_n` and `repeat_penalty`.

Akhirnya, teks yang dihasilkan dicetak saat diterjemahkan, memastikan output real-time yang ter-streaming.

## Langkah 7: Jalankan Aplikasi

Untuk menjalankan aplikasi, eksekusi perintah berikut di terminal:

```bash
cargo run --release
```

Ini akan mencetak haiku tentang hoki es yang dihasilkan oleh model Phi-3. Sesuatu seperti:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

atau

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Kesimpulan

Dengan mengikuti langkah-langkah ini, kita dapat melakukan generasi teks menggunakan model Phi-3 dengan Rust dan Candle dalam kurang dari 100 baris kode. Kode ini menangani pemuatan model, tokenisasi, dan inferensi, memanfaatkan tensor dan pemrosesan logits untuk menghasilkan teks yang koheren berdasarkan prompt input.

Aplikasi konsol ini dapat dijalankan di Windows, Linux, dan Mac OS. Karena portabilitas Rust, kode ini juga dapat disesuaikan menjadi pustaka yang dapat berjalan di dalam aplikasi seluler (karena kita tidak dapat menjalankan aplikasi konsol di sana).

## Lampiran: kode lengkap

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

Catatan: untuk menjalankan kode ini pada Linux aarch64 atau Windows aarch64, tambahkan file bernama `.cargo/config` dengan konten berikut:

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

> Anda dapat mengunjungi repositori resmi [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) untuk contoh lain tentang cara menggunakan model Phi-3 dengan Rust dan Candle, termasuk pendekatan alternatif untuk inferensi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berusaha untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.