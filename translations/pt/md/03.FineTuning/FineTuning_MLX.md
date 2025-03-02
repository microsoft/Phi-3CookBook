# **Ajuste fino do Phi-3 com o Framework Apple MLX**

Podemos realizar o ajuste fino combinado com Lora através da linha de comando do framework Apple MLX. (Se você quiser saber mais sobre o funcionamento do Framework MLX, leia [Inferência do Phi-3 com o Framework Apple MLX](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Preparação dos dados**

Por padrão, o Framework MLX exige que os dados de treino, teste e avaliação estejam no formato jsonl, e o ajuste fino é realizado em conjunto com Lora.


### ***Nota:***

1. Formato de dados jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nosso exemplo utiliza os [dados do TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), mas a quantidade de dados é relativamente limitada, então os resultados do ajuste fino podem não ser os melhores. Recomenda-se que os usuários utilizem dados mais adequados para seus próprios cenários.

3. O formato dos dados é combinado com o modelo Phi-3.

Baixe os dados neste [link](../../../../code/04.Finetuning/mlx), incluindo todos os arquivos .jsonl na pasta ***data***.


## **2. Ajuste fino no terminal**

Execute este comando no terminal:


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Este é um ajuste fino com LoRA, o framework MLX ainda não publicou suporte para QLoRA.

2. Você pode editar o arquivo config.yaml para alterar alguns parâmetros, como:


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

Execute este comando no terminal:


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Executar o adaptador de ajuste fino para teste**

Você pode executar o adaptador de ajuste fino no terminal, como no exemplo abaixo:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

E executar o modelo original para comparar os resultados:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Tente comparar os resultados do ajuste fino com os do modelo original.


## **4. Mesclar adaptadores para gerar novos modelos**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Executar modelos ajustados quantificados usando o Ollama**

Antes de usar, configure o ambiente llama.cpp:


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:*** 

1. Agora é suportada a conversão quantizada para fp32, fp16 e INT8.

2. O modelo mesclado não contém o arquivo tokenizer.model. Faça o download em https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Configure o arquivo de modelo do Ollama (Se o Ollama não estiver instalado, leia [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)):


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Execute o comando no terminal:


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Parabéns! Você aprendeu a realizar ajuste fino com o Framework MLX.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automatizada por IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.