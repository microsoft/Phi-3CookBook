# रस्टसह क्रॉस-प्लॅटफॉर्म इनफरन्स

हा ट्युटोरियल आपल्याला रस्ट आणि [Candle ML फ्रेमवर्क](https://github.com/huggingface/candle) वापरून इनफरन्स करण्याच्या प्रक्रियेतून मार्गदर्शन करेल. इनफरन्ससाठी रस्ट वापरण्याचे अनेक फायदे आहेत, विशेषतः इतर प्रोग्रामिंग भाषांशी तुलना करता. रस्ट त्याच्या उच्च कार्यक्षमतेसाठी ओळखले जाते, जे C आणि C++ इतकेच आहे. हे इनफरन्ससाठी एक उत्कृष्ट निवड बनवते, कारण ही प्रक्रिया जास्त गणनात्मक संसाधने वापरणारी असते. यामागचे कारण म्हणजे झिरो-कॉस्ट अब्स्ट्रॅक्शन्स आणि कार्यक्षम मेमरी व्यवस्थापन, ज्यामध्ये गार्बेज कलेक्शनचा अडथळा नसतो. रस्टचे क्रॉस-प्लॅटफॉर्म वैशिष्ट्य वेगवेगळ्या ऑपरेटिंग सिस्टम्सवर (जसे Windows, macOS, Linux आणि मोबाईल ऑपरेटिंग सिस्टम्स) कोड चालवणे शक्य करते, कोडबेसमध्ये मोठ्या बदलांशिवाय.

हा ट्युटोरियल फॉलो करण्यासाठी [रस्ट इन्स्टॉल](https://www.rust-lang.org/tools/install) करणे आवश्यक आहे, ज्यामध्ये रस्ट कंपायलर आणि Cargo (रस्ट पॅकेज मॅनेजर) समाविष्ट आहे.

## पायरी 1: नवीन रस्ट प्रोजेक्ट तयार करा

नवीन रस्ट प्रोजेक्ट तयार करण्यासाठी, टर्मिनलमध्ये खालील कमांड चालवा:

```bash
cargo new phi-console-app
```

यामुळे प्रारंभिक प्रोजेक्ट स्ट्रक्चर तयार होईल, ज्यामध्ये `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` फाइल असेल:

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

## पायरी 2: प्राथमिक पॅरामिटर्स कॉन्फिगर करा

`main.rs` फाइलमध्ये, आपण इनफरन्ससाठी प्रारंभिक पॅरामिटर्स सेट करू. साधेपणासाठी ते सर्व हार्डकोड केले जातील, परंतु आवश्यक असल्यास आपण ते बदलू शकतो.

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

- **temperature**: सॅम्पलिंग प्रक्रियेतील रँडमनेस नियंत्रित करते.
- **sample_len**: तयार केलेल्या टेक्स्टची जास्तीत जास्त लांबी निर्दिष्ट करते.
- **top_p**: न्यूक्लियस सॅम्पलिंगसाठी वापरले जाते, ज्यामुळे प्रत्येक टप्प्यासाठी विचारात घेतलेल्या टोकन्सची संख्या मर्यादित केली जाते.
- **repeat_last_n**: पुनरावृत्ती टाळण्यासाठी लागू केलेल्या दंडासाठी विचारात घेतलेल्या टोकन्सची संख्या नियंत्रित करते.
- **repeat_penalty**: पुनरावृत्ती टाळण्यासाठी लागू केलेल्या दंडाचे मूल्य.
- **seed**: एक रँडम सीड (चांगल्या पुनरुत्पादनक्षमतेसाठी आपण एक स्थिर मूल्य वापरू शकतो).
- **prompt**: टेक्स्ट जनरेशन सुरू करण्यासाठी प्रारंभिक प्रॉम्प्ट टेक्स्ट. येथे आपण मॉडेलला "आइस हॉकी" वर हायकू तयार करण्यास सांगतो, आणि संभाषणातील वापरकर्ता आणि सहाय्यक भाग दर्शवण्यासाठी विशेष टोकन्सने याला वेढले आहे. मॉडेल नंतर प्रॉम्प्ट पूर्ण करून हायकू तयार करेल.
- **device**: या उदाहरणात आपण CPU वापरतो. Candle GPUवर CUDA आणि Metal सह चालवणे समर्थित करते.

## पायरी 3: मॉडेल आणि टोकनायझर डाउनलोड/तयार करा

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

आम्ही `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` फाइल इनपुट टेक्स्ट टोकनाइझ करण्यासाठी वापरतो. एकदा डाउनलोड केल्यावर मॉडेल कॅश केले जाते, त्यामुळे पहिल्यांदा चालवताना वेळ लागतो (कारण 2.4GB मॉडेल डाउनलोड होते), परंतु नंतरच्या वेळेस जलद कार्य होते.

## पायरी 4: मॉडेल लोड करा

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

आम्ही क्वांटाइझ्ड मॉडेलचे वेट्स मेमरीमध्ये लोड करतो आणि Phi-3 मॉडेल इनिशियलाइज करतो. या टप्प्यात `gguf` फाइलमधून मॉडेल वेट्स वाचणे आणि निर्दिष्ट डिव्हाइसवर (या उदाहरणात CPU) इनफरन्ससाठी मॉडेल तयार करणे समाविष्ट आहे.

## पायरी 5: प्रॉम्प्ट प्रोसेस करा आणि इनफरन्ससाठी तयार करा

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

या टप्प्यात, आम्ही इनपुट प्रॉम्प्ट टोकनाइझ करतो आणि टोकन आयडीच्या सिक्वेन्समध्ये रूपांतरित करून इनफरन्ससाठी तयार करतो. आम्ही `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` मूल्ये देखील इनिशियलाइज करतो. प्रत्येक टोकनला टेन्सरमध्ये रूपांतरित केले जाते आणि लॉजिट्स मिळवण्यासाठी मॉडेलमधून पास केले जाते.

लूप प्रत्येक टोकन प्रक्रिया करतो, लॉजिट्स प्रोसेसर अपडेट करतो आणि पुढील टोकन जनरेशनसाठी तयारी करतो.

## पायरी 6: इनफरन्स

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

इनफरन्स लूपमध्ये, आम्ही टोकन एकेक करून तयार करतो जोपर्यंत नमुना लांबी गाठली जात नाही किंवा एंड-ऑफ-सीक्वेन्स टोकन सापडत नाही. पुढील टोकन टेन्सरमध्ये रूपांतरित केले जाते आणि मॉडेलमधून पास केले जाते, तर लॉजिट्सवर दंड आणि सॅम्पलिंग लागू केले जाते. नंतर पुढील टोकन सॅम्पल केला जातो, डिकोड केला जातो आणि सिक्वेन्समध्ये जोडला जातो. 

पुनरावृत्ती टाळण्यासाठी, `repeat_last_n` and `repeat_penalty` पॅरामिटर्सनुसार पुनरावृत्ती टोकन्सवर दंड लागू केला जातो.

शेवटी, तयार केलेला टेक्स्ट डिकोड केल्यानंतर प्रिंट केला जातो, जो रिअल-टाइममध्ये पाहता येतो.

## पायरी 7: ॲप्लिकेशन चालवा

ॲप्लिकेशन चालवण्यासाठी, टर्मिनलमध्ये खालील कमांड चालवा:

```bash
cargo run --release
```

हे Phi-3 मॉडेलद्वारे तयार केलेले "आइस हॉकी" हायकू प्रिंट करेल. काहीतरी असे:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

किंवा

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## निष्कर्ष

या पायर्‍या फॉलो करून, आपण Phi-3 मॉडेल वापरून रस्ट आणि Candleच्या सहाय्याने 100 ओळींच्या आत टेक्स्ट जनरेशन करू शकतो. हा कोड मॉडेल लोडिंग, टोकनायझेशन आणि इनफरन्स हाताळतो, टेन्सर्स आणि लॉजिट्स प्रोसेसिंगचा वापर करून इनपुट प्रॉम्प्टच्या आधारावर सुसंगत टेक्स्ट तयार करतो.

हे कन्सोल ॲप्लिकेशन Windows, Linux, आणि Mac OS वर चालवता येते. रस्टच्या पोर्टेबिलिटीमुळे, हा कोड मोबाईल ॲप्ससाठी लायब्ररीमध्ये रुपांतरित केला जाऊ शकतो (कारण कन्सोल ॲप्स तिथे चालवता येत नाहीत).

## परिशिष्ट: संपूर्ण कोड

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

टीप: aarch64 Linux किंवा aarch64 Windows वर हा कोड चालवण्यासाठी `.cargo/config` नावाची फाइल खालील सामग्रीसह जोडा:

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

> आपण अधिक उदाहरणांसाठी अधिकृत [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रेपॉजिटरीला भेट देऊ शकता, जिथे Phi-3 मॉडेल रस्ट आणि Candle सह कसे वापरायचे याचे पर्यायी दृष्टिकोन देखील दिले आहेत.

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित एआय अनुवाद सेवा वापरून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.