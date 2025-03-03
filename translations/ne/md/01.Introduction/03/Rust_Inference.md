# Rust प्रयोग गरेर क्रस-प्ल्याटफर्म इनफेरेन्स

यो ट्युटोरियलले हामीलाई Rust र HuggingFace को [Candle ML framework](https://github.com/huggingface/candle) प्रयोग गरी इनफेरेन्स गर्ने प्रक्रियामा मार्गदर्शन गर्नेछ। इनफेरेन्सका लागि Rust प्रयोग गर्दा केही महत्त्वपूर्ण फाइदाहरू प्राप्त हुन्छन्, विशेष गरी अन्य प्रोग्रामिङ भाषाहरूको तुलनामा। Rust आफ्नो उच्च प्रदर्शनको लागि परिचित छ, जुन C र C++ को स्तरमा छ। यो इनफेरेन्स जस्ता कम्प्युटेसनल रूपमा गहन कार्यहरूको लागि उत्कृष्ट विकल्प बनाउँछ। यसलाई मुख्य रूपमा शून्य लागतका अब्स्ट्र्याक्सन र प्रभावकारी मेमोरी व्यवस्थापनले सम्भव बनाएको हो, जसले कुनै पनि गार्बेज कलेक्शन ओभरहेड उत्पन्न गर्दैन। Rust को क्रस-प्ल्याटफर्म क्षमताले कोडलाई विभिन्न अपरेटिङ सिस्टमहरू (जस्तै Windows, macOS, Linux, र मोबाइल अपरेटिङ सिस्टमहरू) मा उल्लेखनीय परिवर्तन नगरी चलाउन सक्षम बनाउँछ।

यस ट्युटोरियललाई पछ्याउन [Rust इन्स्टल गर्नुहोस्](https://www.rust-lang.org/tools/install) जसमा Rust कम्पाइलर र Cargo (Rust को प्याकेज म्यानेजर) समावेश छ।

## चरण १: नयाँ Rust प्रोजेक्ट बनाउनुहोस्

नयाँ Rust प्रोजेक्ट बनाउन टर्मिनलमा निम्न कमाण्ड चलाउनुहोस्:

```bash
cargo new phi-console-app
```

यसले `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` फाइलसहित प्रारम्भिक प्रोजेक्ट संरचना सिर्जना गर्दछ:

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

## चरण २: आधारभूत प्यारामिटरहरू कन्फिगर गर्नुहोस्

`main.rs` फाइल भित्र, हामी इनफेरेन्सका लागि प्रारम्भिक प्यारामिटरहरू सेटअप गर्नेछौं। यी सबैलाई सरलताको लागि हार्डकोड गरिनेछ, तर आवश्यकताअनुसार परिमार्जन गर्न सकिन्छ।

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

- **temperature**: स्याम्पलिङ प्रक्रियाको र्यान्डमनेसलाई नियन्त्रण गर्छ।
- **sample_len**: उत्पन्न हुने पाठको अधिकतम लम्बाइ निर्दिष्ट गर्छ।
- **top_p**: न्यूक्लियस स्याम्पलिङका लागि प्रत्येक चरणमा विचार गरिने टोकनहरूको संख्या सीमित गर्न प्रयोग गरिन्छ।
- **repeat_last_n**: दोहोरिने क्रमहरू रोक्न टोकनहरूमा पेनाल्टी लागू गर्न विचार गरिने टोकनहरूको संख्या नियन्त्रण गर्छ।
- **repeat_penalty**: दोहोरिने टोकनहरूलाई निरुत्साहित गर्नको लागि पेनाल्टी मान।
- **seed**: एक र्यान्डम सिड (बेहतर पुनरुत्पादकताको लागि स्थिर मान प्रयोग गर्न सकिन्छ)।
- **prompt**: पाठ उत्पन्न गर्न सुरूवातको प्रारम्भिक प्रोम्प्ट। यहाँ हामी मोडेललाई आइस हक्कीको बारेमा हाइकु सिर्जना गर्न सोध्छौं, र प्रयोगकर्ता र सहायकको वार्तालापको भाग संकेत गर्न विशेष टोकनहरूमा यसलाई र्याप गर्छौं। त्यसपछि मोडेलले प्रोम्प्टलाई पूरा गर्नेछ।
- **device**: यस उदाहरणमा हामी CPU प्रयोग गर्छौं। Candle GPU मा CUDA र Metal सहित चलाउन समर्थन गर्दछ।

## चरण ३: मोडेल र टोकनाइजर डाउनलोड/तयार गर्नुहोस्

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

हामी `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` फाइललाई इनपुट पाठ टोकनाइज गर्न प्रयोग गर्छौं। मोडेल एकपटक डाउनलोड भएपछि, यो क्यास गरिन्छ, त्यसैले पहिलो पटक चलाउँदा (२.४GB मोडेल डाउनलोड हुने भएकाले) ढिलो हुन्छ तर त्यसपछि छिटो चल्छ।

## चरण ४: मोडेल लोड गर्नुहोस्

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

हामी क्वान्टाइज्ड मोडेल वजनहरू मेमोरीमा लोड गर्छौं र Phi-3 मोडेल सुरु गर्छौं। यस चरणमा `gguf` फाइलबाट मोडेल वजनहरू पढ्ने र निर्दिष्ट डिभाइस (यस अवस्थामा CPU) मा इनफेरेन्सका लागि मोडेल सेटअप गर्ने समावेश छ।

## चरण ५: प्रोम्प्ट प्रक्रिया गर्नुहोस् र इनफेरेन्सका लागि तयार गर्नुहोस्

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

यस चरणमा, हामी इनपुट प्रोम्प्टलाई टोकनाइज गर्छौं र यसलाई टोकन IDहरूको अनुक्रममा रूपान्तरण गरेर इनफेरेन्सका लागि तयार गर्छौं। हामी `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` मानहरू पनि सुरु गर्छौं। प्रत्येक टोकनलाई टेन्सरमा रूपान्तरण गरी मोडेलमा पास गरिन्छ, जसले गर्दा logits प्राप्त हुन्छ।

लूपले प्रोम्प्टका प्रत्येक टोकनलाई प्रक्रिया गर्छ, logits प्रोसेसर अपडेट गर्छ, र अर्को टोकन उत्पन्न गर्न तयारी गर्छ।

## चरण ६: इनफेरेन्स

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

इनफेरेन्स लूपमा, हामी टोकनहरू एक-एक गरेर उत्पन्न गर्छौं जबसम्म चाहिएको नमूना लम्बाइमा पुग्दैन वा अन्त्य-क्रम टोकन भेटिँदैन। अर्को टोकनलाई टेन्सरमा रूपान्तरण गरी मोडेलमा पास गरिन्छ, जबकि logits प्रोसेस गरेर पेनाल्टी र स्याम्पलिङ लागू गरिन्छ। त्यसपछि अर्को टोकन स्याम्पल गरिन्छ, डिकोड गरिन्छ, र अनुक्रममा थपिन्छ।
दोहोरिने पाठ रोक्न, `repeat_last_n` and `repeat_penalty` प्यारामिटरहरूको आधारमा दोहोरिने टोकनहरूमा पेनाल्टी लागू गरिन्छ।

अन्ततः, उत्पन्न पाठलाई डिकोड गर्दै प्रिन्ट गरिन्छ, रियल-टाइम आउटपुट सुनिश्चित गर्दै।

## चरण ७: एप्लिकेसन चलाउनुहोस्

एप्लिकेसन चलाउन, टर्मिनलमा निम्न कमाण्ड कार्यान्वयन गर्नुहोस्:

```bash
cargo run --release
```

यसले Phi-3 मोडेलद्वारा उत्पन्न आइस हक्कीको बारेमा हाइकु प्रिन्ट गर्नुपर्छ। उदाहरणका लागि:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

वा

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## निष्कर्ष

यी चरणहरू पछ्याएर, हामी Rust र Candle प्रयोग गरेर Phi-3 मोडेलद्वारा पाठ उत्पन्न गर्न सक्छौं, त्यो पनि १०० लाइनभन्दा कम कोडमा। यो कोडले मोडेल लोडिंग, टोकनाइजेशन, र इनफेरेन्सलाई सम्हाल्छ, टेन्सरहरू र logits प्रोसेसिङ प्रयोग गरेर इनपुट प्रोम्प्टमा आधारित सुसंगत पाठ उत्पन्न गर्दछ।

यो कन्सोल एप्लिकेसन Windows, Linux, र Mac OS मा चल्न सक्छ। Rust को पोर्टेबिलिटीका कारण, यसलाई मोबाइल एपहरू भित्र चल्ने लाइब्रेरीमा रूपान्तरण गर्न पनि सकिन्छ (कन्सोल एप्स त्यहाँ चलाउन सकिँदैन)।

## परिशिष्ट: पूर्ण कोड

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

नोट: यो कोड `aarch64 Linux` वा `aarch64 Windows` मा चलाउन, `.cargo/config` नामक फाइलमा निम्न सामग्री थप्नुहोस्:

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

> तपाईं आधिकारिक [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपोजिटरीमा Phi-3 मोडेलसँग Rust र Candle प्रयोग गर्ने अन्य उदाहरणहरूको लागि जान सक्नुहुन्छ, जसमा इनफेरेन्सका वैकल्पिक दृष्टिकोणहरू समावेश छन्।

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।