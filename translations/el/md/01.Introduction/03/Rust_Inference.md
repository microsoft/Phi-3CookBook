# Διπλής πλατφόρμας inference με Rust

Αυτό το tutorial θα μας καθοδηγήσει στη διαδικασία εκτέλεσης inference χρησιμοποιώντας Rust και το [Candle ML framework](https://github.com/huggingface/candle) από το HuggingFace. Η χρήση του Rust για inference προσφέρει αρκετά πλεονεκτήματα, ιδιαίτερα σε σύγκριση με άλλες γλώσσες προγραμματισμού. Το Rust είναι γνωστό για την υψηλή του απόδοση, συγκρίσιμη με αυτή της C και C++. Αυτό το καθιστά εξαιρετική επιλογή για απαιτητικές υπολογιστικά εργασίες inference. Ειδικότερα, αυτό οφείλεται στις μηδενικού κόστους αφαιρέσεις και την αποτελεσματική διαχείριση μνήμης, χωρίς επιβάρυνση από garbage collection. Οι δυνατότητες διπλής πλατφόρμας του Rust επιτρέπουν την ανάπτυξη κώδικα που εκτελείται σε διάφορα λειτουργικά συστήματα, όπως Windows, macOS, Linux, αλλά και κινητά λειτουργικά συστήματα, χωρίς σημαντικές αλλαγές στον κώδικα.

Προαπαιτούμενο για την παρακολούθηση αυτού του tutorial είναι να [εγκαταστήσετε το Rust](https://www.rust-lang.org/tools/install), το οποίο περιλαμβάνει τον compiler του Rust και το Cargo, τον διαχειριστή πακέτων του Rust.

## Βήμα 1: Δημιουργία Νέου Έργου Rust

Για να δημιουργήσουμε ένα νέο έργο Rust, εκτελούμε την παρακάτω εντολή στο τερματικό:

```bash
cargo new phi-console-app
```

Αυτό δημιουργεί μια αρχική δομή έργου με ένα αρχείο `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Βήμα 2: Ρύθμιση Βασικών Παραμέτρων

Μέσα στο αρχείο main.rs, θα ρυθμίσουμε τις αρχικές παραμέτρους για το inference. Όλες θα είναι σκληροκωδικοποιημένες για απλότητα, αλλά μπορούμε να τις τροποποιήσουμε ανάλογα με τις ανάγκες μας.

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

- **temperature**: Ελέγχει την τυχαιότητα της διαδικασίας δειγματοληψίας.
- **sample_len**: Καθορίζει το μέγιστο μήκος του παραγόμενου κειμένου.
- **top_p**: Χρησιμοποιείται για nucleus sampling, περιορίζοντας τον αριθμό των tokens που εξετάζονται σε κάθε βήμα.
- **repeat_last_n**: Καθορίζει τον αριθμό των tokens που λαμβάνονται υπόψη για την εφαρμογή ποινής ώστε να αποφεύγονται επαναλαμβανόμενες ακολουθίες.
- **repeat_penalty**: Η τιμή ποινής για την αποθάρρυνση επαναλαμβανόμενων tokens.
- **seed**: Ένας τυχαίος σπόρος (μπορούμε να χρησιμοποιήσουμε σταθερή τιμή για καλύτερη αναπαραγωγιμότητα).
- **prompt**: Το αρχικό κείμενο που ξεκινά τη δημιουργία. Σημειώστε ότι ζητάμε από το μοντέλο να δημιουργήσει ένα χαϊκού για το χόκεϊ στον πάγο, και το τυλίγουμε με ειδικούς δείκτες για να υποδείξουμε τα μέρη της συνομιλίας του χρήστη και του βοηθού. Το μοντέλο θα ολοκληρώσει το prompt με ένα χαϊκού.
- **device**: Χρησιμοποιούμε την CPU για υπολογισμούς σε αυτό το παράδειγμα. Το Candle υποστηρίζει εκτέλεση σε GPU με CUDA και Metal επίσης.

## Βήμα 3: Λήψη/Προετοιμασία Μοντέλου και Tokenizer

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

Χρησιμοποιούμε το αρχείο `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` για την τοκενιζοποίηση του εισαγόμενου κειμένου. Αφού κατεβεί το μοντέλο, αποθηκεύεται στην προσωρινή μνήμη, οπότε η πρώτη εκτέλεση θα είναι πιο αργή (καθώς κατεβάζει τα 2.4GB του μοντέλου), αλλά οι επόμενες εκτελέσεις θα είναι ταχύτερες.

## Βήμα 4: Φόρτωση Μοντέλου

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Φορτώνουμε τα quantized βάρη του μοντέλου στη μνήμη και αρχικοποιούμε το μοντέλο Phi-3. Αυτό το βήμα περιλαμβάνει την ανάγνωση των βαρών του μοντέλου από το αρχείο `gguf` και την προετοιμασία του μοντέλου για inference στη συγκεκριμένη συσκευή (CPU σε αυτή την περίπτωση).

## Βήμα 5: Επεξεργασία Prompt και Προετοιμασία για Inference

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

Σε αυτό το βήμα, τοκενιζούμε το εισαγόμενο prompt και το προετοιμάζουμε για inference μετατρέποντάς το σε ακολουθία ID tokens. Επίσης, αρχικοποιούμε τα `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Κάθε token μετατρέπεται σε tensor και περνά μέσα από το μοντέλο για να πάρουμε τα logits.

Ο βρόχος επεξεργάζεται κάθε token στο prompt, ενημερώνοντας τον logits processor και προετοιμάζοντας για τη δημιουργία του επόμενου token.

## Βήμα 6: Inference

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

Στον βρόχο inference, δημιουργούμε tokens ένα προς ένα μέχρι να φτάσουμε στο επιθυμητό μήκος δείγματος ή να συναντήσουμε το token τέλους ακολουθίας. Το επόμενο token μετατρέπεται σε tensor και περνά μέσα από το μοντέλο, ενώ τα logits επεξεργάζονται για την εφαρμογή ποινών και δειγματοληψίας. Στη συνέχεια, το επόμενο token δειγματοληπτείται, αποκωδικοποιείται και προστίθεται στην ακολουθία.
Για να αποφύγουμε επαναλαμβανόμενο κείμενο, εφαρμόζεται ποινή στα επαναλαμβανόμενα tokens βάσει των παραμέτρων `repeat_last_n` and `repeat_penalty`.

Τέλος, το παραγόμενο κείμενο εκτυπώνεται καθώς αποκωδικοποιείται, διασφαλίζοντας ροή σε πραγματικό χρόνο.

## Βήμα 7: Εκτέλεση Εφαρμογής

Για να εκτελέσουμε την εφαρμογή, τρέχουμε την παρακάτω εντολή στο τερματικό:

```bash
cargo run --release
```

Αυτό θα πρέπει να εκτυπώσει ένα χαϊκού για το χόκεϊ στον πάγο που δημιουργήθηκε από το μοντέλο Phi-3. Κάτι σαν:

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ή

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Συμπέρασμα

Ακολουθώντας αυτά τα βήματα, μπορούμε να πραγματοποιήσουμε δημιουργία κειμένου χρησιμοποιώντας το μοντέλο Phi-3 με Rust και Candle σε λιγότερο από 100 γραμμές κώδικα. Ο κώδικας διαχειρίζεται τη φόρτωση του μοντέλου, την τοκενιζοποίηση και το inference, αξιοποιώντας tensors και επεξεργασία logits για να παραγάγει συνεκτικό κείμενο βάσει του εισαγόμενου prompt.

Αυτή η εφαρμογή κονσόλας μπορεί να εκτελεστεί σε Windows, Linux και Mac OS. Χάρη στη φορητότητα του Rust, ο κώδικας μπορεί επίσης να προσαρμοστεί σε βιβλιοθήκη που θα εκτελείται μέσα σε εφαρμογές για κινητά (δε μπορούμε να τρέξουμε εφαρμογές κονσόλας εκεί, τελικά).

## Παράρτημα: Πλήρης Κώδικας

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

Σημείωση: για να εκτελέσετε αυτόν τον κώδικα σε aarch64 Linux ή aarch64 Windows, προσθέστε ένα αρχείο με όνομα `.cargo/config` με το παρακάτω περιεχόμενο:

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

> Μπορείτε να επισκεφθείτε το επίσημο αποθετήριο [Candle examples](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) για περισσότερα παραδείγματα σχετικά με τη χρήση του μοντέλου Phi-3 με Rust και Candle, συμπεριλαμβανομένων εναλλακτικών προσεγγίσεων για inference.

**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μηχανικής μετάφρασης με βάση την τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη σας ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.