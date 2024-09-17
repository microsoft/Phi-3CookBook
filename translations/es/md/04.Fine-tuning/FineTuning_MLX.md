# **Ajuste fino de Phi-3 con el marco Apple MLX**

Podemos completar el ajuste fino combinado con Lora a través de la línea de comandos del marco Apple MLX. (Si deseas saber más sobre el funcionamiento del marco MLX, por favor lee [Inferencia Phi-3 con el marco Apple MLX](../03.Inference/MLX_Inference.md))

## **1. Preparación de datos**

Por defecto, el marco MLX requiere el formato jsonl para entrenamiento, prueba y evaluación, y se combina con Lora para completar las tareas de ajuste fino.

### ***Nota:***

1. Formato de datos jsonl:

```json
{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....
```

2. Nuestro ejemplo usa [los datos de TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), pero la cantidad de datos es relativamente insuficiente, por lo que los resultados del ajuste fino no son necesariamente los mejores. Se recomienda que los aprendices usen mejores datos basados en sus propios escenarios para completar.

3. El formato de datos se combina con la plantilla Phi-3.

Por favor, descarga los datos desde este [enlace](../../../../code/04.Finetuning/mlx), incluye todos los archivos .jsonl en la carpeta ***data***.

## **2. Ajuste fino en tu terminal**

Por favor, ejecuta este comando en el terminal:

```bash
python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 
```

## ***Nota:***

1. Este es un ajuste fino de LoRA, el marco MLX no ha publicado QLoRA.

2. Puedes configurar config.yaml para cambiar algunos parámetros, como:

```yaml
# La ruta al directorio del modelo local o repositorio de Hugging Face.
model: "microsoft/Phi-3-mini-4k-instruct"
# Si se debe entrenar o no (booleano)
train: true

# Directorio con archivos {train, valid, test}.jsonl
data: "data"

# La semilla PRNG
seed: 0

# Número de capas para ajuste fino
lora_layers: 32

# Tamaño de mini-batch.
batch_size: 1

# Iteraciones para entrenar.
iters: 1000

# Número de lotes de validación, -1 usa todo el conjunto de validación.
val_batches: 25

# Tasa de aprendizaje de Adam.
learning_rate: 1e-6

# Número de pasos de entrenamiento entre informes de pérdida.
steps_per_report: 10

# Número de pasos de entrenamiento entre validaciones.
steps_per_eval: 200

# Ruta de carga para reanudar el entrenamiento con los pesos del adaptador dados.
resume_adapter_file: null

# Ruta de guardado/carga para los pesos del adaptador entrenados.
adapter_path: "adapters"

# Guardar el modelo cada N iteraciones.
save_every: 1000

# Evaluar en el conjunto de prueba después del entrenamiento.
test: false

# Número de lotes del conjunto de prueba, -1 usa todo el conjunto de prueba.
test_batches: 100

# Longitud máxima de la secuencia.
max_seq_length: 2048

# Usar checkpoint de gradiente para reducir el uso de memoria.
grad_checkpoint: true

# Los parámetros de LoRA solo pueden especificarse en un archivo de configuración.
lora_parameters:
  # Las claves de las capas a las que se aplicará LoRA.
  # Estas se aplicarán a las últimas lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  alpha: 64
  dropout: 0.1
```

Por favor, ejecuta este comando en el terminal:

```bash
python -m  mlx_lm.lora --config lora_config.yaml
```

## **3. Ejecutar el adaptador de ajuste fino para probar**

Puedes ejecutar el adaptador de ajuste fino en el terminal, así:

```bash
python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors?" --eos-token "<|end|>"
```

y ejecutar el modelo original para comparar el resultado:

```bash
python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors?" --eos-token "<|end|>"
```

Puedes intentar comparar los resultados del ajuste fino con el modelo original.

## **4. Fusionar adaptadores para generar nuevos modelos**

```bash
python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct
```

## **5. Ejecutar modelos de ajuste fino cuantificados usando ollama**

Antes de usar, por favor configura tu entorno llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Tu ruta del modelo fusionado' --outfile phi-3-mini-ft.gguf --outtype f16
```

***Nota:***

1. Ahora se admite la conversión de cuantización de fp32, fp16 e INT 8.

2. El modelo fusionado carece de tokenizer.model, por favor descárgalo desde https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Configura el archivo del modelo de Ollama (si no tienes instalado ollama, por favor lee [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)):

```txt
FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"
```

ejecuta el comando en el terminal:

```bash
ollama create phi3ft -f Modelfile 

ollama run phi3ft "Why do chameleons change colors?"
```

¡Felicidades! Has dominado el ajuste fino con el marco MLX.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.