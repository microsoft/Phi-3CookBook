# **Phi-3'ü Apple MLX Framework ile İnce Ayar**

Apple MLX framework komut satırı üzerinden Lora ile birleştirilmiş ince ayar işlemini tamamlayabiliriz. (MLX Framework'ün nasıl çalıştığı hakkında daha fazla bilgi almak isterseniz, lütfen [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) dokümanını okuyun.)

## **1. Veri Hazırlığı**

Varsayılan olarak, MLX Framework, ince ayar işlemlerini tamamlamak için train, test ve eval dosyalarının jsonl formatında olmasını ve Lora ile birleştirilmesini gerektirir.

### ***Not:***

1. jsonl veri formatı:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Örneğimizde [TruthfulQA'nın verilerini](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) kullanıyoruz, ancak veri miktarı nispeten yetersiz olduğu için ince ayar sonuçları mutlaka en iyi olmayabilir. Öğrencilere, kendi senaryolarına uygun daha iyi veriler kullanarak işlemi tamamlamaları önerilir.

3. Veri formatı Phi-3 şablonuyla birleştirilmiştir.

Lütfen verileri bu [bağlantıdan](../../../../code/04.Finetuning/mlx) indirin ve ***data*** klasöründe bulunan tüm .jsonl dosyalarını dahil edin.

## **2. Terminalde İnce Ayar İşlemi**

Lütfen aşağıdaki komutu terminalde çalıştırın:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Not:***

1. Bu, LoRA ince ayarıdır, MLX framework henüz QLoRA'yı yayınlamadı.

2. config.yaml dosyasını düzenleyerek bazı parametreleri değiştirebilirsiniz, örneğin:

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

Lütfen aşağıdaki komutu terminalde çalıştırın:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. İnce Ayar Adaptörünü Test Etme**

Terminalde ince ayar adaptörünü şu şekilde çalıştırabilirsiniz:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ve orijinal modeli çalıştırarak sonuçları karşılaştırabilirsiniz:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

İnce ayar sonuçlarını orijinal model ile karşılaştırmayı deneyebilirsiniz.

## **4. Yeni Modeller Oluşturmak İçin Adaptörleri Birleştirme**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama Kullanarak Kuantize Edilmiş İnce Ayar Modellerini Çalıştırma**

Kullanmadan önce, lütfen llama.cpp ortamınızı yapılandırın.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Not:***

1. Şu anda fp32, fp16 ve INT8 için kuantizasyon dönüşümünü desteklemektedir.

2. Birleştirilmiş modelde tokenizer.model eksik olabilir, lütfen https://huggingface.co/microsoft/Phi-3-mini-4k-instruct adresinden indirin.

Ollama Model dosyasını ayarlayın (Eğer Ollama yüklü değilse, lütfen [Ollama QuickStart](https://ollama.com/) dokümanını okuyun.)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Komutu terminalde çalıştırın:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Tebrikler! MLX Framework ile ince ayar işlemini başarıyla öğrendiniz.

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.