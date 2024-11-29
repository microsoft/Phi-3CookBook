# Inférence multiplateforme avec Rust

Ce tutoriel nous guidera à travers le processus d'inférence en utilisant Rust et le [Candle ML framework](https://github.com/huggingface/candle) de HuggingFace. Utiliser Rust pour l'inférence offre plusieurs avantages, en particulier par rapport à d'autres langages de programmation. Rust est connu pour ses hautes performances, comparables à celles du C et du C++. Cela en fait un excellent choix pour les tâches d'inférence, qui peuvent être intensives en calcul. En particulier, cela est dû aux abstractions sans coût et à la gestion efficace de la mémoire, sans surcharge de collecte des ordures. Les capacités multiplateformes de Rust permettent de développer du code qui fonctionne sur divers systèmes d'exploitation, y compris Windows, macOS et Linux, ainsi que sur les systèmes d'exploitation mobiles, sans modifications significatives du code.

La condition préalable pour suivre ce tutoriel est d'[installer Rust](https://www.rust-lang.org/tools/install), qui inclut le compilateur Rust et Cargo, le gestionnaire de packages Rust.

## Étape 1 : Créer un nouveau projet Rust

Pour créer un nouveau projet Rust, exécutez la commande suivante dans le terminal :

```bash
cargo new phi-console-app
```

Cela génère une structure de projet initiale avec un fichier `Cargo.toml` file and a `src` directory containing a `main.rs` file.

Next, we will add our dependencies - namely the `candle`, `hf-hub` and `tokenizers` crates - to the `Cargo.toml` :

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

## Étape 2 : Configurer les paramètres de base

À l'intérieur du fichier main.rs, nous allons configurer les paramètres initiaux pour notre inférence. Ils seront tous codés en dur pour plus de simplicité, mais nous pourrons les modifier au besoin.

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

- **temperature** : Contrôle la randomisation du processus d'échantillonnage.
- **sample_len** : Spécifie la longueur maximale du texte généré.
- **top_p** : Utilisé pour l'échantillonnage de noyau pour limiter le nombre de tokens considérés pour chaque étape.
- **repeat_last_n** : Contrôle le nombre de tokens considérés pour appliquer une pénalité afin d'éviter les séquences répétitives.
- **repeat_penalty** : La valeur de la pénalité pour décourager les tokens répétés.
- **seed** : Une graine aléatoire (nous pourrions utiliser une valeur constante pour une meilleure reproductibilité).
- **prompt** : Le texte initial pour commencer la génération. Remarquez que nous demandons au modèle de générer un haïku sur le hockey sur glace, et que nous l'encadrons avec des tokens spéciaux pour indiquer les parties utilisateur et assistant de la conversation. Le modèle complétera ensuite l'invite avec un haïku.
- **device** : Nous utilisons le CPU pour le calcul dans cet exemple. Candle prend également en charge l'exécution sur GPU avec CUDA et Metal.

## Étape 3 : Télécharger/Préparer le modèle et le tokenizer

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

Nous utilisons le fichier `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` pour tokeniser notre texte d'entrée. Une fois téléchargé, le modèle est mis en cache, donc la première exécution sera lente (car elle télécharge les 2,4 Go du modèle) mais les exécutions suivantes seront plus rapides.

## Étape 4 : Charger le modèle

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Nous chargeons les poids du modèle quantifié en mémoire et initialisons le modèle Phi-3. Cette étape implique la lecture des poids du modèle à partir du fichier `gguf` et la configuration du modèle pour l'inférence sur le dispositif spécifié (CPU dans ce cas).

## Étape 5 : Traiter l'invite et préparer l'inférence

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

À cette étape, nous tokenisons l'invite d'entrée et la préparons pour l'inférence en la convertissant en une séquence d'IDs de tokens. Nous initialisons également les valeurs `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Chaque token est converti en tenseur et passé à travers le modèle pour obtenir les logits.

La boucle traite chaque token dans l'invite, mettant à jour le processeur de logits et se préparant pour la génération du token suivant.

## Étape 6 : Inférence

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

Dans la boucle d'inférence, nous générons des tokens un par un jusqu'à atteindre la longueur d'échantillon souhaitée ou rencontrer le token de fin de séquence. Le token suivant est converti en tenseur et passé à travers le modèle, tandis que les logits sont traités pour appliquer des pénalités et un échantillonnage. Ensuite, le token suivant est échantillonné, décodé et ajouté à la séquence.
Pour éviter un texte répétitif, une pénalité est appliquée aux tokens répétés en fonction des paramètres `repeat_last_n` and `repeat_penalty`.

Enfin, le texte généré est imprimé au fur et à mesure de son décodage, assurant une sortie en temps réel.

## Étape 7 : Exécuter l'application

Pour exécuter l'application, exécutez la commande suivante dans le terminal :

```bash
cargo run --release
```

Cela devrait imprimer un haïku sur le hockey sur glace généré par le modèle Phi-3. Quelque chose comme :

```
Puck glides swiftly,  
Blades on ice dance and clash—peace found 
in the cold battle.
```

ou

```
Glistening puck glides in,
On ice rink's silent stage it thrives—
Swish of sticks now alive.
```

## Conclusion

En suivant ces étapes, nous pouvons générer du texte en utilisant le modèle Phi-3 avec Rust et Candle en moins de 100 lignes de code. Le code gère le chargement du modèle, la tokenisation et l'inférence, en utilisant des tenseurs et le traitement des logits pour générer un texte cohérent basé sur l'invite d'entrée.

Cette application console peut fonctionner sur Windows, Linux et Mac OS. En raison de la portabilité de Rust, le code peut également être adapté à une bibliothèque qui fonctionnerait à l'intérieur des applications mobiles (nous ne pouvons pas exécuter d'applications console là-bas, après tout).

## Annexe : code complet

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

Note : pour exécuter ce code sur Linux aarch64 ou Windows aarch64, ajoutez un fichier nommé `.cargo/config` avec le contenu suivant :

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

> Vous pouvez visiter le dépôt officiel des [exemples Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) pour plus d'exemples sur la façon d'utiliser le modèle Phi-3 avec Rust et Candle, y compris des approches alternatives pour l'inférence.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations cruciales, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.