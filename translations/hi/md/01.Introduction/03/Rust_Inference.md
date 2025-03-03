# रस्ट के साथ क्रॉस-प्लेटफॉर्म इंफेरेंस

यह ट्यूटोरियल हमें रस्ट और [Candle ML फ्रेमवर्क](https://github.com/huggingface/candle) का उपयोग करके इंफेरेंस करने की प्रक्रिया के माध्यम से मार्गदर्शन करेगा। इंफेरेंस के लिए रस्ट का उपयोग कई फायदे प्रदान करता है, खासकर अन्य प्रोग्रामिंग भाषाओं की तुलना में। रस्ट अपनी उच्च प्रदर्शन क्षमता के लिए जाना जाता है, जो C और C++ के बराबर है। यह इसे उन कार्यों के लिए एक उत्कृष्ट विकल्प बनाता है जो कम्प्यूटेशनल रूप से गहन हो सकते हैं। विशेष रूप से, यह शून्य-लागत अमूर्तता और कुशल मेमोरी प्रबंधन द्वारा संचालित है, जिसमें गार्बेज कलेक्शन का कोई ओवरहेड नहीं है। रस्ट की क्रॉस-प्लेटफॉर्म क्षमताएं कोड को विभिन्न ऑपरेटिंग सिस्टम जैसे Windows, macOS, और Linux के साथ-साथ मोबाइल ऑपरेटिंग सिस्टम पर भी चलाने की अनुमति देती हैं, बिना कोडबेस में बड़े बदलाव किए।

इस ट्यूटोरियल को फॉलो करने के लिए यह आवश्यक है कि आप [रस्ट इंस्टॉल करें](https://www.rust-lang.org/tools/install), जिसमें रस्ट कंपाइलर और Cargo, रस्ट का पैकेज मैनेजर शामिल है।

## चरण 1: नया रस्ट प्रोजेक्ट बनाएं

नया रस्ट प्रोजेक्ट बनाने के लिए, टर्मिनल में निम्नलिखित कमांड चलाएं:

```bash
cargo new phi-console-app
```

यह एक प्रारंभिक प्रोजेक्ट संरचना उत्पन्न करता है जिसमें `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` फ़ाइल शामिल है:

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

## चरण 2: बुनियादी पैरामीटर सेट करें

`main.rs` फ़ाइल के अंदर, हम इंफेरेंस के लिए प्रारंभिक पैरामीटर सेट करेंगे। सरलता के लिए, ये सभी हार्डकोडेड होंगे, लेकिन आवश्यकता अनुसार इन्हें संशोधित किया जा सकता है।

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

- **temperature**: सैंपलिंग प्रक्रिया की रैंडमनेस को नियंत्रित करता है।
- **sample_len**: उत्पन्न टेक्स्ट की अधिकतम लंबाई निर्दिष्ट करता है।
- **top_p**: न्यूक्लियस सैंपलिंग के लिए उपयोग किया जाता है ताकि प्रत्येक चरण के लिए विचार किए जाने वाले टोकन की संख्या सीमित हो सके।
- **repeat_last_n**: उन टोकनों की संख्या को नियंत्रित करता है जिन पर दोहराव रोकने के लिए पेनल्टी लगाई जाती है।
- **repeat_penalty**: दोहराए गए टोकनों को हतोत्साहित करने के लिए पेनल्टी मान।
- **seed**: एक रैंडम बीज (बेहतर पुनरुत्पादन के लिए हम एक स्थिर मान का उपयोग कर सकते हैं)।
- **prompt**: टेक्स्ट जनरेशन शुरू करने के लिए प्रारंभिक प्रॉम्प्ट। ध्यान दें कि हम मॉडल से बर्फ हॉकी पर एक हाइकु उत्पन्न करने के लिए कहते हैं, और इसे विशेष टोकनों से लपेटते हैं ताकि उपयोगकर्ता और सहायक बातचीत के भाग को इंगित किया जा सके। मॉडल फिर प्रॉम्प्ट को एक हाइकु के साथ पूरा करेगा।
- **device**: इस उदाहरण में हम गणना के लिए CPU का उपयोग करते हैं। Candle GPU पर CUDA और Metal के साथ चलाने का समर्थन करता है।

## चरण 3: मॉडल और टोकनाइज़र डाउनलोड/तैयार करें

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

हम `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` फ़ाइल का उपयोग हमारे इनपुट टेक्स्ट को टोकनाइज़ करने के लिए करते हैं। एक बार डाउनलोड होने के बाद, मॉडल कैश हो जाता है, इसलिए पहली बार निष्पादन धीमा होगा (क्योंकि यह 2.4GB मॉडल डाउनलोड करता है), लेकिन बाद के निष्पादन तेज होंगे।

## चरण 4: मॉडल लोड करें

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

हम क्वांटाइज्ड मॉडल वेट्स को मेमोरी में लोड करते हैं और Phi-3 मॉडल को इनिशियलाइज़ करते हैं। इस चरण में `gguf` फ़ाइल से मॉडल वेट्स को पढ़ना और निर्दिष्ट डिवाइस (इस मामले में CPU) पर इंफेरेंस के लिए मॉडल सेटअप करना शामिल है।

## चरण 5: प्रॉम्प्ट को प्रोसेस करें और इंफेरेंस के लिए तैयार करें

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

इस चरण में, हम इनपुट प्रॉम्प्ट को टोकनाइज़ करते हैं और इसे इंफेरेंस के लिए तैयार करते हैं, इसे टोकन आईडी की एक श्रृंखला में बदलकर। हम `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p` मान भी इनिशियलाइज़ करते हैं। प्रत्येक टोकन को एक टेंसर में बदल दिया जाता है और मॉडल के माध्यम से लॉजिट्स प्राप्त करने के लिए पास किया जाता है।

लूप प्रत्येक टोकन को प्रॉम्प्ट में प्रोसेस करता है, लॉजिट्स प्रोसेसर को अपडेट करता है और अगले टोकन जनरेशन के लिए तैयार करता है।

## चरण 6: इंफेरेंस

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

इंफेरेंस लूप में, हम एक-एक करके टोकन जनरेट करते हैं जब तक कि हम वांछित सैंपल लंबाई तक न पहुँच जाएं या एंड-ऑफ-सीक्वेंस टोकन का सामना न करें। अगला टोकन एक टेंसर में परिवर्तित होता है और मॉडल के माध्यम से पास किया जाता है, जबकि लॉजिट्स को पेनल्टी और सैंपलिंग लागू करने के लिए प्रोसेस किया जाता है। फिर अगला टोकन सैंपल किया जाता है, डिकोड किया जाता है, और सीक्वेंस में जोड़ा जाता है। 

दोहराव वाले टेक्स्ट से बचने के लिए, `repeat_last_n` and `repeat_penalty` पैरामीटर के आधार पर दोहराए गए टोकनों पर पेनल्टी लगाई जाती है।

अंत में, उत्पन्न टेक्स्ट को डिकोड करते समय प्रिंट किया जाता है, जिससे रीयल-टाइम आउटपुट स्ट्रीम किया जा सके।

## चरण 7: एप्लिकेशन चलाएं

एप्लिकेशन चलाने के लिए, टर्मिनल में निम्नलिखित कमांड निष्पादित करें:

```bash
cargo run --release
```

यह बर्फ हॉकी पर Phi-3 मॉडल द्वारा जनरेट किया गया एक हाइकु प्रिंट करेगा। कुछ इस तरह:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

या

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## निष्कर्ष

इन चरणों का पालन करके, हम Phi-3 मॉडल का उपयोग करके रस्ट और Candle के साथ टेक्स्ट जनरेशन कर सकते हैं, वह भी 100 लाइनों से कम कोड में। कोड मॉडल लोडिंग, टोकनाइज़ेशन, और इंफेरेंस को संभालता है, टेंसर और लॉजिट्स प्रोसेसिंग का उपयोग करके इनपुट प्रॉम्प्ट के आधार पर सुसंगत टेक्स्ट उत्पन्न करता है।

यह कंसोल एप्लिकेशन Windows, Linux, और Mac OS पर चल सकता है। रस्ट की पोर्टेबिलिटी के कारण, इस कोड को एक ऐसी लाइब्रेरी में भी अनुकूलित किया जा सकता है जो मोबाइल ऐप्स के अंदर चले (क्योंकि हम वहां कंसोल ऐप्स नहीं चला सकते)।

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

नोट: यदि आप इस कोड को aarch64 Linux या aarch64 Windows पर चलाना चाहते हैं, तो `.cargo/config` नामक एक फ़ाइल निम्नलिखित सामग्री के साथ जोड़ें:

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

> आप आधिकारिक [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) रिपॉजिटरी पर जाकर अधिक उदाहरण देख सकते हैं कि Phi-3 मॉडल को रस्ट और Candle के साथ कैसे उपयोग किया जाए, जिसमें इंफेरेंस के वैकल्पिक दृष्टिकोण शामिल हैं।

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।