# **Apple MLX फ्रेमवर्कसँग Phi-3 लाई फाइन-ट्यून गर्ने**

Apple MLX फ्रेमवर्क कमाण्ड लाइनको माध्यमबाट Lora सहित फाइन-ट्यूनिंग पूरा गर्न सकिन्छ। (यदि तपाईं MLX फ्रेमवर्कको अपरेशनबारे थप जान्न चाहनुहुन्छ भने, कृपया [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) पढ्नुहोस्।)

## **१. डाटा तयारी**

डिफल्ट अनुसार, MLX फ्रेमवर्कले train, test, र eval का लागि jsonl फर्म्याटलाई आवश्यक पर्छ, र Lora को साथमा मिलाएर फाइन-ट्यूनिंग कार्यहरू पूरा गर्छ।

### ***नोट:***

1. jsonl डाटा फर्म्याटः

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. हाम्रो उदाहरणमा [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) प्रयोग गरिएको छ, तर डाटाको मात्रा तुलनात्मक रूपमा अपर्याप्त छ, त्यसैले फाइन-ट्यूनिंगको परिणाम अनिवार्य रूपमा उत्कृष्ट नहुन सक्छ। सिफारिस गरिन्छ कि सिक्न चाहनेहरूले आफ्नै परिदृश्यहरूमा आधारित राम्रो डाटा प्रयोग गरेर यसलाई पूरा गरून्।

3. डाटा फर्म्याट Phi-3 टेम्प्लेटसँग मिलाइएको छ।

कृपया यो [लिंक](../../../../code/04.Finetuning/mlx) बाट डाटा डाउनलोड गर्नुहोस्, कृपया ***data*** फोल्डरमा सबै .jsonl समावेश गर्नुहोस्।

## **२. तपाईंको टर्मिनलमा फाइन-ट्यूनिंग गर्नुहोस्**

कृपया यो कमाण्ड टर्मिनलमा चलाउनुहोस्:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***नोट:***

1. यो LoRA फाइन-ट्यूनिंग हो, MLX फ्रेमवर्कले QLoRA हालसम्म प्रकाशित गरेको छैन।

2. तपाईं config.yaml सेट गरेर केही arguments परिवर्तन गर्न सक्नुहुन्छ, जस्तैः

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

कृपया यो कमाण्ड टर्मिनलमा चलाउनुहोस्:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **३. फाइन-ट्यूनिंग एडाप्टर चलाएर परीक्षण गर्नुहोस्**

तपाईं टर्मिनलमा फाइन-ट्यूनिंग एडाप्टर यसरी चलाउन सक्नुहुन्छः

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

र ओरिजिनल मोडेल चलाएर नतिजा तुलना गर्न सक्नुहुन्छः

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

तपाईं फाइन-ट्यूनिंगको नतिजा र ओरिजिनल मोडेलको नतिजा तुलना गर्न प्रयास गर्न सक्नुहुन्छ।

## **४. एडाप्टरहरू मर्ज गरेर नयाँ मोडेल बनाउनुहोस्**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **५. क्वान्टिफाइड फाइन-ट्यूनिंग मोडेलहरू ollama प्रयोग गरेर चलाउनुहोस्**

प्रयोग गर्नुअघि, कृपया तपाईंको llama.cpp वातावरण कन्फिगर गर्नुहोस्।

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***नोट:*** 

1. अहिले fp32, fp16 र INT8 को क्वान्टाइजेसन कन्भर्सनलाई समर्थन गर्छ।

2. मर्ज गरिएको मोडेलमा tokenizer.model हराएको हुन्छ, कृपया यो https://huggingface.co/microsoft/Phi-3-mini-4k-instruct बाट डाउनलोड गर्नुहोस्।

Ollama मोडेल फाइल सेट गर्नुहोस् (यदि ollama इन्स्टल गरिएको छैन भने, कृपया [Ollama QuickStart](https://ollama.com/) पढ्नुहोस्)।

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

टर्मिनलमा कमाण्ड चलाउनुहोस्:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

बधाई छ! MLX फ्रेमवर्कको साथ फाइन-ट्यूनिंग सिक्नुभयो।

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। यद्यपि हामी शुद्धताका लागि प्रयास गर्छौं, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषामा रहेको मूल दस्तावेजलाई प्रामाणिक स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।