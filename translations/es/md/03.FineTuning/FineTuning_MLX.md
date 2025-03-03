# **Ajuste fino de Phi-3 con el marco Apple MLX**

Podemos realizar el ajuste fino combinado con Lora a través de la línea de comandos del marco Apple MLX. (Si deseas saber más sobre el funcionamiento del marco MLX, por favor lee [Inferencia de Phi-3 con el marco Apple MLX](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Preparación de datos**

Por defecto, el marco MLX requiere el formato jsonl para train, test y eval, y se combina con Lora para completar los trabajos de ajuste fino.


### ***Nota:***

1. Formato de datos jsonl：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nuestro ejemplo utiliza los [datos de TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), pero la cantidad de datos es relativamente insuficiente, por lo que los resultados del ajuste fino no son necesariamente los mejores. Se recomienda que los usuarios utilicen datos de mejor calidad basados en sus propios escenarios.

3. El formato de los datos se combina con la plantilla de Phi-3.

Por favor, descarga los datos desde este [enlace](../../../../code/04.Finetuning/mlx), incluye todos los archivos .jsonl en la carpeta ***data***.


## **2. Ajuste fino en tu terminal**

Por favor, ejecuta este comando en el terminal:


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Este es un ajuste fino con LoRA, el marco MLX no ha publicado QLoRA.

2. Puedes configurar config.yaml para cambiar algunos parámetros, como:


```yaml


# The path to the local model directory or Hugging Face repo.
model: "microsoft/Phi-3-mini-4k-instruct"
# Whether or not to train (boolean)
train: true

# Directory with {train, valid, test}.jsonl files
data: "data"

# The PRNG seed
seed: 0

# Number of layers to fine-tune
lora_layers: 32

# Minibatch size.
batch_size: 1

# Iterations to train for.
iters: 1000

# Number of validation batches, -1 uses the entire validation set.
val_batches: 25

# Adam learning rate.
learning_rate: 1e-6

# Number of training steps between loss reporting.
steps_per_report: 10

# Number of training steps between validations.
steps_per_eval: 200

# Load path to resume training with the given adapter weights.
resume_adapter_file: null

# Save/load path for the trained adapter weights.
adapter_path: "adapters"

# Save the model every N iterations.
save_every: 1000

# Evaluate on the test set after training
test: false

# Number of test set batches, -1 uses the entire test set.
test_batches: 100

# Maximum sequence length.
max_seq_length: 2048

# Use gradient checkpointing to reduce memory use.
grad_checkpoint: true

# LoRA parameters can only be specified in a config file
lora_parameters:
  # The layer keys to apply LoRA to.
  # These will be applied for the last lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  scale: 1
  dropout: 0.1


```

Por favor, ejecuta este comando en el terminal:


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Ejecutar el adaptador de ajuste fino para probar**

Puedes ejecutar el adaptador de ajuste fino en el terminal, de esta forma:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

y ejecutar el modelo original para comparar los resultados:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Intenta comparar los resultados del ajuste fino con los del modelo original.


## **4. Combinar adaptadores para generar nuevos modelos**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ejecutar modelos ajustados y cuantificados usando Ollama**

Antes de usar, por favor configura tu entorno llama.cpp.


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:***

1. Ahora se admite la conversión de cuantización de fp32, fp16 e INT 8.

2. El modelo combinado no incluye tokenizer.model, por favor descárgalo desde https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Configura el archivo del modelo de Ollama (si no has instalado Ollama, por favor lee [Inicio rápido de Ollama](https://ollama.com/)):


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Ejecuta el comando en el terminal:


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

¡Felicidades! Has dominado el ajuste fino con el marco MLX.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.