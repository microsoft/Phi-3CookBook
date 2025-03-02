# Inferência Multiplataforma com Rust

Este tutorial nos guiará pelo processo de realizar inferência usando Rust e o [Candle ML framework](https://github.com/huggingface/candle) da HuggingFace. Utilizar Rust para inferência oferece várias vantagens, especialmente quando comparado a outras linguagens de programação. Rust é conhecido por seu alto desempenho, comparável ao de C e C++. Isso o torna uma excelente escolha para tarefas de inferência, que podem ser intensivas em termos computacionais. Em particular, isso se deve às abstrações de custo zero e ao gerenciamento eficiente de memória, sem a sobrecarga de coleta de lixo. As capacidades multiplataforma de Rust permitem o desenvolvimento de código que roda em diversos sistemas operacionais, incluindo Windows, macOS e Linux, bem como sistemas operacionais móveis, sem mudanças significativas na base de código.

O pré-requisito para seguir este tutorial é [instalar o Rust](https://www.rust-lang.org/tools/install), que inclui o compilador Rust e o Cargo, o gerenciador de pacotes do Rust.

## Passo 1: Criar um Novo Projeto Rust

Para criar um novo projeto Rust, execute o seguinte comando no terminal:

```bash
cargo new phi-console-app
```

Isso gera uma estrutura inicial de projeto com um arquivo `Cargo.toml` file and a `src` directory containing a `main.rs` file.

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

## Passo 2: Configurar Parâmetros Básicos

Dentro do arquivo main.rs, configuraremos os parâmetros iniciais para a inferência. Eles serão todos codificados diretamente para simplificar, mas podemos modificá-los conforme necessário.

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

- **temperature**: Controla o grau de aleatoriedade no processo de amostragem.
- **sample_len**: Especifica o comprimento máximo do texto gerado.
- **top_p**: Usado para amostragem nucleus, limitando o número de tokens considerados em cada etapa.
- **repeat_last_n**: Controla o número de tokens considerados para aplicar uma penalidade que evita sequências repetitivas.
- **repeat_penalty**: O valor da penalidade para desencorajar tokens repetidos.
- **seed**: Uma semente aleatória (podemos usar um valor constante para melhor reprodutibilidade).
- **prompt**: O texto inicial para começar a geração. Note que pedimos ao modelo para gerar um haiku sobre hóquei no gelo e o envolvemos com tokens especiais para indicar as partes do usuário e do assistente na conversa. O modelo então completará o prompt com um haiku.
- **device**: Usamos a CPU para computação neste exemplo. O Candle suporta execução em GPU com CUDA e Metal também.

## Passo 3: Baixar/Preparar o Modelo e o Tokenizer

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

Usamos o arquivo `hf_hub` API to download the model and tokenizer files from the Hugging Face model hub. The `gguf` file contains the quantized model weights, while the `tokenizer.json` para tokenizar nosso texto de entrada. Uma vez baixado, o modelo é armazenado em cache, então a primeira execução será lenta (pois baixa os 2,4 GB do modelo), mas as execuções subsequentes serão mais rápidas.

## Passo 4: Carregar o Modelo

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Carregamos os pesos do modelo quantizado na memória e inicializamos o modelo Phi-3. Este passo envolve ler os pesos do modelo a partir do arquivo `gguf` e configurar o modelo para inferência no dispositivo especificado (CPU neste caso).

## Passo 5: Processar o Prompt e Preparar para Inferência

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

Neste passo, tokenizamos o prompt de entrada e o preparamos para inferência, convertendo-o em uma sequência de IDs de tokens. Também inicializamos os valores de `LogitsProcessor` to handle the sampling process (probability distribution over the vocabulary) based on the given `temperature` and `top_p`. Cada token é convertido em um tensor e passado pelo modelo para obter os logits.

O loop processa cada token no prompt, atualizando o processador de logits e se preparando para a geração do próximo token.

## Passo 6: Inferência

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

No loop de inferência, geramos tokens um por um até alcançarmos o comprimento desejado ou encontrarmos o token de fim de sequência. O próximo token é convertido em um tensor e passado pelo modelo, enquanto os logits são processados para aplicar penalidades e amostragem. Em seguida, o próximo token é amostrado, decodificado e adicionado à sequência.
Para evitar texto repetitivo, uma penalidade é aplicada aos tokens repetidos com base nos parâmetros `repeat_last_n` and `repeat_penalty`.

Por fim, o texto gerado é exibido à medida que é decodificado, garantindo uma saída em tempo real.

## Passo 7: Executar o Aplicativo

Para executar o aplicativo, execute o seguinte comando no terminal:

```bash
cargo run --release
```

Isso deve imprimir um haiku sobre hóquei no gelo gerado pelo modelo Phi-3. Algo como:

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

## Conclusão

Seguindo esses passos, podemos realizar geração de texto usando o modelo Phi-3 com Rust e Candle em menos de 100 linhas de código. O código lida com carregamento do modelo, tokenização e inferência, aproveitando tensores e processamento de logits para gerar texto coerente com base no prompt de entrada.

Este aplicativo de console pode ser executado no Windows, Linux e macOS. Por causa da portabilidade do Rust, o código também pode ser adaptado para uma biblioteca que rodaria dentro de aplicativos móveis (afinal, não podemos executar aplicativos de console lá).

## Apêndice: código completo

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

Nota: para executar este código em Linux aarch64 ou Windows aarch64, adicione um arquivo chamado `.cargo/config` com o seguinte conteúdo:

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

> Você pode visitar o repositório oficial de [exemplos do Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) para mais exemplos de como usar o modelo Phi-3 com Rust e Candle, incluindo abordagens alternativas para inferência.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.