# **Pag-aangkop ng Phi-3 gamit ang Apple MLX Framework**

Maaaring kumpletuhin ang pag-aangkop na pinagsama sa Lora gamit ang command line ng Apple MLX Framework. (Kung nais mong malaman pa ang tungkol sa operasyon ng MLX Framework, mangyaring basahin ang [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)

## **1. Paghahanda ng Data**

Sa default, ang MLX Framework ay nangangailangan ng jsonl na format para sa train, test, at eval, at pinagsasama ito sa Lora upang makumpleto ang mga gawain ng pag-aangkop.

### ***Tandaan:***

1. jsonl na format ng data:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Ang aming halimbawa ay gumagamit ng [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ngunit kulang ang dami ng data, kaya’t hindi tiyak na ang resulta ng pag-aangkop ay ang pinakamahusay. Inirerekomenda na gumamit ang mga mag-aaral ng mas mahusay na data base sa kanilang sariling mga sitwasyon upang makumpleto ito.

3. Ang format ng data ay pinagsama sa Phi-3 na template.

Mangyaring i-download ang data mula sa [link](../../../../code/04.Finetuning/mlx), at isama ang lahat ng .jsonl sa ***data*** na folder.

## **2. Pag-aangkop gamit ang iyong terminal**

Mangyaring patakbuhin ang command na ito sa terminal:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Tandaan:***

1. Ito ay LoRA na pag-aangkop; ang MLX framework ay hindi pa naglalathala ng QLoRA.

2. Maaari mong baguhin ang config.yaml upang i-adjust ang ilang mga argumento, tulad ng:

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

Patakbuhin ang command na ito sa terminal:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Patakbuhin ang Fine-tuning Adapter upang Subukan**

Maaari mong patakbuhin ang fine-tuning adapter sa terminal, tulad nito:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

At patakbuhin ang orihinal na modelo upang ikumpara ang resulta:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Subukan mong ikumpara ang mga resulta ng Fine-tuning sa orihinal na modelo.

## **4. Pagsasama ng Adapters upang Bumuo ng Bagong Modelo**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Pagpapatakbo ng Mga Quantified Fine-tuning Model Gamit ang Ollama**

Bago gamitin, mangyaring i-configure ang iyong llama.cpp na environment:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Tandaan:***

1. Ngayon ay sinusuportahan ang quantization conversion ng fp32, fp16, at INT 8.

2. Ang pinagsamang modelo ay kulang ng tokenizer.model, mangyaring i-download ito mula sa https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

I-set ang Ollama Model file (Kung hindi naka-install ang ollama, mangyaring basahin ang [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Patakbuhin ang command sa terminal:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Binabati kita! Napagtagumpayan mo ang pag-aangkop gamit ang MLX Framework.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na awtomatikong pagsasalin. Bagama't pinagsisikapan naming maging wasto, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na pangunahing mapagkukunan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.