# การใช้งาน Cross-platform inference ด้วย Rust

บทแนะนำนี้จะพาเราผ่านกระบวนการทำ inference ด้วย Rust และ [Candle ML framework](https://github.com/huggingface/candle) จาก HuggingFace การใช้ Rust สำหรับ inference มีข้อดีหลายประการ โดยเฉพาะเมื่อเปรียบเทียบกับภาษาโปรแกรมอื่นๆ Rust มีชื่อเสียงในเรื่องประสิทธิภาพสูง ซึ่งใกล้เคียงกับ C และ C++ ทำให้เหมาะสมอย่างยิ่งสำหรับงาน inference ที่ต้องใช้การคำนวณหนักๆ จุดเด่นนี้เกิดจากการใช้ zero-cost abstractions และการจัดการหน่วยความจำที่มีประสิทธิภาพ โดยไม่มี overhead จาก garbage collection นอกจากนี้ ความสามารถในการทำงานข้ามแพลตฟอร์มของ Rust ยังช่วยให้เราพัฒนาซอฟต์แวร์ที่สามารถรันบนระบบปฏิบัติการต่างๆ เช่น Windows, macOS, Linux รวมถึงระบบปฏิบัติการบนมือถือ โดยไม่ต้องแก้ไขโค้ดมากนัก

สิ่งที่ต้องมีเพื่อทำตามบทแนะนำนี้คือ [ติดตั้ง Rust](https://www.rust-lang.org/tools/install) ซึ่งรวมถึง Rust compiler และ Cargo (ตัวจัดการแพ็กเกจของ Rust)

## ขั้นตอนที่ 1: สร้างโปรเจกต์ Rust ใหม่

สร้างโปรเจกต์ Rust ใหม่โดยรันคำสั่งต่อไปนี้ใน terminal:

```bash
cargo new phi-console-app
```

คำสั่งนี้จะสร้างโครงสร้างโปรเจกต์เริ่มต้นที่มีไฟล์ `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` ดังนี้:

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

## ขั้นตอนที่ 2: กำหนดค่าพารามิเตอร์พื้นฐาน

ในไฟล์ main.rs เราจะตั้งค่าพารามิเตอร์เริ่มต้นสำหรับการทำ inference โดยค่าทั้งหมดจะถูกกำหนดแบบฮาร์ดโค้ดเพื่อความเรียบง่าย แต่สามารถปรับเปลี่ยนได้ตามความต้องการ

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

- **temperature**: ควบคุมความสุ่มของกระบวนการสุ่มตัวอย่าง
- **sample_len**: กำหนดความยาวสูงสุดของข้อความที่สร้างขึ้น
- **top_p**: ใช้สำหรับ nucleus sampling เพื่อลดจำนวน token ที่พิจารณาในแต่ละขั้นตอน
- **repeat_last_n**: ควบคุมจำนวน token ที่นำมาพิจารณาเพื่อใช้ penalty ป้องกันการเกิดข้อความซ้ำ
- **repeat_penalty**: ค่าปรับเพื่อป้องกันการเกิด token ซ้ำ
- **seed**: ค่า seed แบบสุ่ม (สามารถใช้ค่าคงที่เพื่อให้ได้ผลลัพธ์ที่ reproducible)
- **prompt**: ข้อความเริ่มต้นที่ใช้เป็นตัวกระตุ้นให้โมเดลสร้างข้อความ ในตัวอย่างนี้ เราขอให้โมเดลสร้างบทกวีไฮกุเกี่ยวกับกีฬาฮอกกี้น้ำแข็ง และห่อข้อความด้วย token พิเศษเพื่อระบุบทสนทนาของผู้ใช้และผู้ช่วย โมเดลจะเติมข้อความต่อจาก prompt เพื่อสร้างไฮกุ
- **device**: ในตัวอย่างนี้ เราใช้ CPU สำหรับการคำนวณ Candle ยังรองรับการทำงานบน GPU ด้วย CUDA และ Metal

## ขั้นตอนที่ 3: ดาวน์โหลด/เตรียมโมเดลและ Tokenizer

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

เราใช้ไฟล์ `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` สำหรับการแปลงข้อความอินพุตเป็น token เมื่อดาวน์โหลดแล้ว โมเดลจะถูกแคชไว้ ดังนั้นการรันครั้งแรกอาจใช้เวลานาน (เนื่องจากต้องดาวน์โหลดไฟล์ขนาด 2.4GB) แต่การรันครั้งถัดไปจะเร็วขึ้น

## ขั้นตอนที่ 4: โหลดโมเดล

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

เราจะโหลดน้ำหนักโมเดลที่ผ่านการ quantized เข้าสู่หน่วยความจำ และเริ่มต้นโมเดล Phi-3 ขั้นตอนนี้เกี่ยวข้องกับการอ่านน้ำหนักโมเดลจากไฟล์ `gguf` และตั้งค่าโมเดลให้พร้อมสำหรับ inference บนอุปกรณ์ที่ระบุ (ในกรณีนี้คือ CPU)

## ขั้นตอนที่ 5: ประมวลผล Prompt และเตรียมสำหรับ Inference

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

ในขั้นตอนนี้ เราจะแปลง prompt อินพุตเป็น token ID และเตรียมพร้อมสำหรับ inference โดยแปลงเป็นลำดับของ token ID จากนั้นเราจะตั้งค่า `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` ค่าแต่ละ token จะถูกแปลงเป็น tensor และส่งผ่านโมเดลเพื่อรับ logits

ลูปนี้จะประมวลผลแต่ละ token ใน prompt อัปเดต logits processor และเตรียมสำหรับการสร้าง token ถัดไป

## ขั้นตอนที่ 6: การทำ Inference

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

ในลูป inference เราจะสร้าง token ทีละตัวจนกว่าจะถึงความยาวที่ต้องการ หรือพบ token สิ้นสุดลำดับ (end-of-sequence) token ถัดไปจะถูกแปลงเป็น tensor และส่งผ่านโมเดล โดย logits จะถูกประมวลผลเพื่อใช้ penalties และสุ่มตัวอย่าง จากนั้น token ถัดไปจะถูกสุ่ม แปลงกลับเป็นข้อความ และเพิ่มเข้าไปในลำดับ

เพื่อหลีกเลี่ยงข้อความซ้ำ จะมีการใช้ penalty กับ token ที่ซ้ำตามพารามิเตอร์ `repeat_last_n` and `repeat_penalty`

สุดท้าย ข้อความที่สร้างขึ้นจะถูกพิมพ์ออกมาในขณะที่ถูกแปลงกลับเป็นข้อความ เพื่อแสดงผลแบบเรียลไทม์

## ขั้นตอนที่ 7: รันแอปพลิเคชัน

เพื่อรันแอปพลิเคชัน ให้ใช้คำสั่งต่อไปนี้ใน terminal:

```bash
cargo run --release
```

คำสั่งนี้จะสร้างบทกวีไฮกุเกี่ยวกับกีฬาฮอกกี้น้ำแข็งจากโมเดล Phi-3 ซึ่งอาจมีหน้าตาประมาณนี้:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

หรือ

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## สรุป

เมื่อทำตามขั้นตอนเหล่านี้ เราสามารถสร้างข้อความด้วยโมเดล Phi-3 โดยใช้ Rust และ Candle ในโค้ดที่มีความยาวไม่เกิน 100 บรรทัด โค้ดนี้จัดการการโหลดโมเดล การแปลงข้อความเป็น token และการ inference โดยใช้ tensors และการประมวลผล logits เพื่อสร้างข้อความที่สมเหตุสมผลตาม prompt อินพุต

แอปพลิเคชันนี้สามารถรันได้บน Windows, Linux และ macOS ด้วยความสามารถในการพกพาของ Rust โค้ดยังสามารถปรับเปลี่ยนเป็นไลบรารีที่รันในแอปพลิเคชันบนมือถือได้ (เนื่องจากเราไม่สามารถรันแอปคอนโซลบนมือถือได้)

## ภาคผนวก: โค้ดทั้งหมด

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

หมายเหตุ: หากต้องการรันโค้ดนี้บน aarch64 Linux หรือ aarch64 Windows ให้เพิ่มไฟล์ชื่อ `.cargo/config` ที่มีเนื้อหาดังนี้:

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

> สามารถเยี่ยมชม [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) อย่างเป็นทางการเพื่อดูตัวอย่างเพิ่มเติมเกี่ยวกับการใช้งานโมเดล Phi-3 กับ Rust และ Candle รวมถึงวิธีการ inference แบบอื่นๆ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติที่ใช้ AI แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้มากที่สุด สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้