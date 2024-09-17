# Inferencia multiplataforma con Rust

Este tutorial nos guiará a través del proceso de realizar inferencias usando Rust y el [framework Candle ML](https://github.com/huggingface/candle) de HuggingFace. Usar Rust para inferencia ofrece varias ventajas, especialmente en comparación con otros lenguajes de programación. Rust es conocido por su alto rendimiento, comparable al de C y C++. Esto lo convierte en una excelente opción para tareas de inferencia, que pueden ser computacionalmente intensivas. En particular, esto se debe a las abstracciones de costo cero y a la gestión eficiente de memoria, sin la sobrecarga de recolección de basura. Las capacidades multiplataforma de Rust permiten desarrollar código que se ejecute en varios sistemas operativos, incluyendo Windows, macOS y Linux, así como en sistemas operativos móviles, sin cambios significativos en la base de código.

El requisito previo para seguir este tutorial es [instalar Rust](https://www.rust-lang.org/tools/install), que incluye el compilador de Rust y Cargo, el gestor de paquetes de Rust.

## Paso 1: Crear un Nuevo Proyecto en Rust

Para crear un nuevo proyecto en Rust, ejecuta el siguiente comando en la terminal:

```bash
cargo new phi-console-app
```

Esto genera una estructura inicial del proyecto con un archivo `Cargo.toml` y un directorio `src` que contiene un archivo `main.rs`.

A continuación, agregaremos nuestras dependencias - concretamente los crates `candle`, `hf-hub` y `tokenizers` - al archivo `Cargo.toml`:

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

## Paso 2: Configurar Parámetros Básicos

Dentro del archivo main.rs, configuraremos los parámetros iniciales para nuestra inferencia. Todos estarán codificados de forma fija para simplificar, pero podemos modificarlos según sea necesario.

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

- **temperature**: Controla la aleatoriedad del proceso de muestreo.
- **sample_len**: Especifica la longitud máxima del texto generado.
- **top_p**: Se utiliza para el muestreo de núcleo para limitar el número de tokens considerados en cada paso.
- **repeat_last_n**: Controla el número de tokens considerados para aplicar una penalización y prevenir secuencias repetitivas.
- **repeat_penalty**: El valor de la penalización para desalentar tokens repetidos.
- **seed**: Una semilla aleatoria (podríamos usar un valor constante para una mejor reproducibilidad).
- **prompt**: El texto inicial para comenzar la generación. Observa que pedimos al modelo que genere un haiku sobre el hockey sobre hielo, y que lo envolvemos con tokens especiales para indicar las partes del usuario y el asistente de la conversación. El modelo completará el prompt con un haiku.
- **device**: Usamos la CPU para el cálculo en este ejemplo. Candle soporta la ejecución en GPU con CUDA y Metal también.

## Paso 3: Descargar/Preparar el Modelo y el Tokenizador

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

Usamos la API `hf_hub` para descargar los archivos del modelo y del tokenizador desde el hub de modelos de Hugging Face. El archivo `gguf` contiene los pesos del modelo cuantizado, mientras que el archivo `tokenizer.json` se utiliza para tokenizar nuestro texto de entrada. Una vez descargado, el modelo se almacena en caché, por lo que la primera ejecución será lenta (ya que descarga los 2.4GB del modelo) pero las ejecuciones posteriores serán más rápidas.

## Paso 4: Cargar el Modelo

```rust
let mut file = std::fs::File::open(&model_path)?;
let model_content = gguf_file::Content::read(&mut file)?;
let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;
```

Cargamos los pesos del modelo cuantizado en memoria e inicializamos el modelo Phi-3. Este paso implica leer los pesos del modelo desde el archivo `gguf` y configurar el modelo para la inferencia en el dispositivo especificado (CPU en este caso).

## Paso 5: Procesar el Prompt y Preparar para la Inferencia

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

En este paso, tokenizamos el prompt de entrada y lo preparamos para la inferencia convirtiéndolo en una secuencia de IDs de tokens. También inicializamos el `LogitsProcessor` para manejar el proceso de muestreo (distribución de probabilidad sobre el vocabulario) basado en los valores dados de `temperature` y `top_p`. Cada token se convierte en un tensor y se pasa por el modelo para obtener los logits.

El bucle procesa cada token en el prompt, actualizando el procesador de logits y preparando la generación del próximo token.

## Paso 6: Inferencia

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

En el bucle de inferencia, generamos tokens uno por uno hasta alcanzar la longitud de muestra deseada o encontrar el token de fin de secuencia. El próximo token se convierte en un tensor y se pasa por el modelo, mientras que los logits se procesan para aplicar penalizaciones y muestreo. Luego se muestrea el próximo token, se decodifica y se añade a la secuencia.
Para evitar texto repetitivo, se aplica una penalización a los tokens repetidos basada en los parámetros `repeat_last_n` y `repeat_penalty`.

Finalmente, el texto generado se imprime a medida que se decodifica, asegurando una salida en tiempo real.

## Paso 7: Ejecutar la Aplicación

Para ejecutar la aplicación, ejecuta el siguiente comando en la terminal:

```bash
cargo run --release
```

Esto debería imprimir un haiku sobre hockey sobre hielo generado por el modelo Phi-3. Algo como:

```
El puck se desliza,
Patines en hielo bailan—paz hallada 
en la fría batalla.
```

o

```
Puck brillante desliza,
En el escenario silencioso del hielo prospera—
Susurro de palos ahora vivo.
```

## Conclusión

Siguiendo estos pasos, podemos realizar generación de texto usando el modelo Phi-3 con Rust y Candle en menos de 100 líneas de código. El código maneja la carga del modelo, la tokenización y la inferencia, aprovechando tensores y el procesamiento de logits para generar texto coherente basado en el prompt de entrada.

Esta aplicación de consola puede ejecutarse en Windows, Linux y Mac OS. Debido a la portabilidad de Rust, el código también puede adaptarse a una biblioteca que se ejecute dentro de aplicaciones móviles (después de todo, no podemos ejecutar aplicaciones de consola allí).

## Apéndice: código completo

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
    // 1. configurar parámetros básicos
    let temperature: f64 = 1.0;
    let sample_len: usize = 100;
    let top_p: Option<f64> = None;
    let repeat_last_n: usize = 64;
    let repeat_penalty: f32 = 1.2;
    let mut rng = rand::thread_rng();
    let seed: u64 = rng.gen();
    let prompt = "<|user|>\nWrite a haiku about ice hockey<|end|>\n<|assistant|>";

    // vamos a usar solo la CPU
    let device = Device::Cpu;

    // 2. descargar/preparar modelo y tokenizador
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

    // 3. cargar modelo
    let mut file = std::fs::File::open(&model_path)?;
    let model_content = gguf_file::Content::read(&mut file)?;
    let mut model = Phi3::from_gguf(false, model_content, &mut file, &device)?;

    // 4. procesar prompt y preparar para la inferencia
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

        // Muestrear el siguiente token solo para el último token en el prompt
        if pos == tokens.len() - 1 {
            next_token = logits_processor.sample(&logits)?;
            all_tokens.push(next_token);
        }
    }

    // 5. inferencia
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

        // decodificar la secuencia actual de tokens
        let decoded_text = tokenizer.decode(&all_tokens, true).map_err(|e| e.to_string())?;

        // solo imprimir la nueva parte del texto decodificado
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

Nota: para ejecutar este código en Linux aarch64 o Windows aarch64, añade un archivo llamado `.cargo/config` con el siguiente contenido:

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

> Puedes visitar el repositorio oficial de [ejemplos de Candle](https://github.com/huggingface/candle/blob/main/candle-examples/examples/quantized-phi/main.rs) para más ejemplos sobre cómo usar el modelo Phi-3 con Rust y Candle, incluyendo enfoques alternativos para la inferencia.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.