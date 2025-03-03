# Suy luận đa nền tảng với Rust

Hướng dẫn này sẽ giúp chúng ta thực hiện suy luận sử dụng Rust và [Candle ML framework](https://github.com/huggingface/candle) từ HuggingFace. Việc sử dụng Rust để suy luận mang lại nhiều lợi ích, đặc biệt khi so sánh với các ngôn ngữ lập trình khác. Rust nổi tiếng với hiệu suất cao, tương đương với C và C++. Điều này làm cho nó trở thành một lựa chọn tuyệt vời cho các tác vụ suy luận, vốn có thể rất nặng về tính toán. Đặc biệt, điều này được thúc đẩy bởi các trừu tượng không tốn chi phí và quản lý bộ nhớ hiệu quả, không có chi phí thừa của bộ thu gom rác. Khả năng đa nền tảng của Rust cho phép phát triển mã chạy trên nhiều hệ điều hành khác nhau, bao gồm Windows, macOS, và Linux, cũng như các hệ điều hành di động, mà không cần thay đổi đáng kể trong mã nguồn.

Yêu cầu tiên quyết để theo dõi hướng dẫn này là [cài đặt Rust](https://www.rust-lang.org/tools/install), bao gồm trình biên dịch Rust và Cargo, trình quản lý gói của Rust.

## Bước 1: Tạo một dự án Rust mới

Để tạo một dự án Rust mới, chạy lệnh sau trong terminal:

```bash
cargo new phi-console-app
```

Lệnh này sẽ tạo ra một cấu trúc dự án ban đầu với tệp `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Bước 2: Cấu hình các tham số cơ bản

Bên trong tệp main.rs, chúng ta sẽ thiết lập các tham số ban đầu cho suy luận. Tất cả sẽ được cố định để đơn giản, nhưng có thể thay đổi khi cần.

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

- **temperature**: Điều chỉnh mức độ ngẫu nhiên của quá trình lấy mẫu.
- **sample_len**: Xác định độ dài tối đa của văn bản được tạo ra.
- **top_p**: Được sử dụng cho nucleus sampling để giới hạn số lượng token được xem xét trong mỗi bước.
- **repeat_last_n**: Điều chỉnh số lượng token được xem xét để áp dụng hình phạt nhằm ngăn chặn các chuỗi lặp lại.
- **repeat_penalty**: Giá trị hình phạt để giảm thiểu việc lặp lại token.
- **seed**: Một giá trị ngẫu nhiên (có thể sử dụng giá trị cố định để đảm bảo khả năng tái hiện).
- **prompt**: Văn bản gợi ý ban đầu để bắt đầu quá trình tạo. Lưu ý rằng chúng ta yêu cầu mô hình tạo một bài haiku về môn khúc côn cầu trên băng và bọc nó bằng các token đặc biệt để biểu thị phần của người dùng và trợ lý trong cuộc hội thoại. Mô hình sau đó sẽ hoàn thành gợi ý bằng một bài haiku.
- **device**: Trong ví dụ này, chúng ta sử dụng CPU để tính toán. Candle hỗ trợ chạy trên GPU với CUDA và Metal.

## Bước 3: Tải xuống/Chuẩn bị Mô hình và Bộ mã hóa

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

Chúng ta sử dụng tệp `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` để mã hóa văn bản đầu vào. Khi đã tải xuống, mô hình sẽ được lưu trữ trong bộ nhớ đệm, vì vậy lần thực thi đầu tiên sẽ chậm (do tải xuống 2.4GB dữ liệu mô hình), nhưng các lần thực thi sau sẽ nhanh hơn.

## Bước 4: Tải Mô hình

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Chúng ta tải trọng số mô hình đã được lượng tử hóa vào bộ nhớ và khởi tạo mô hình Phi-3. Bước này bao gồm việc đọc trọng số mô hình từ tệp `gguf` và thiết lập mô hình để suy luận trên thiết bị được chỉ định (trong trường hợp này là CPU).

## Bước 5: Xử lý Gợi ý và Chuẩn bị cho Suy luận

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

Trong bước này, chúng ta mã hóa gợi ý đầu vào và chuẩn bị nó cho suy luận bằng cách chuyển đổi nó thành một chuỗi các ID token. Chúng ta cũng khởi tạo các giá trị `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Mỗi token được chuyển đổi thành một tensor và được truyền qua mô hình để nhận logits.

Vòng lặp xử lý từng token trong gợi ý, cập nhật bộ xử lý logits và chuẩn bị cho việc tạo token tiếp theo.

## Bước 6: Suy luận

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

Trong vòng lặp suy luận, chúng ta tạo token từng cái một cho đến khi đạt được độ dài mẫu mong muốn hoặc gặp phải token kết thúc chuỗi. Token tiếp theo được chuyển đổi thành tensor và truyền qua mô hình, trong khi logits được xử lý để áp dụng các hình phạt và lấy mẫu. Sau đó, token tiếp theo được lấy mẫu, giải mã và thêm vào chuỗi.

Để tránh văn bản lặp lại, một hình phạt được áp dụng cho các token lặp lại dựa trên các tham số `repeat_last_n` and `repeat_penalty`.

Cuối cùng, văn bản được tạo ra sẽ được in ra khi nó được giải mã, đảm bảo đầu ra thời gian thực.

## Bước 7: Chạy Ứng dụng

Để chạy ứng dụng, thực thi lệnh sau trong terminal:

```bash
cargo run --release
```

Điều này sẽ in ra một bài haiku về môn khúc côn cầu trên băng được tạo bởi mô hình Phi-3. Có thể là:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

hoặc

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Kết luận

Bằng cách làm theo các bước này, chúng ta có thể thực hiện tạo văn bản bằng mô hình Phi-3 với Rust và Candle trong chưa đầy 100 dòng mã. Mã này xử lý việc tải mô hình, mã hóa, và suy luận, tận dụng tensor và xử lý logits để tạo ra văn bản mạch lạc dựa trên gợi ý đầu vào.

Ứng dụng console này có thể chạy trên Windows, Linux và Mac OS. Nhờ tính di động của Rust, mã này cũng có thể được điều chỉnh thành một thư viện chạy bên trong các ứng dụng di động (vì chúng ta không thể chạy ứng dụng console ở đó).

## Phụ lục: mã đầy đủ

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

Lưu ý: để chạy mã này trên Linux aarch64 hoặc Windows aarch64, thêm một tệp tên `.cargo/config` với nội dung sau:

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

> Bạn có thể truy cập kho [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) chính thức để xem thêm các ví dụ về cách sử dụng mô hình Phi-3 với Rust và Candle, bao gồm các phương pháp tiếp cận thay thế để suy luận.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.