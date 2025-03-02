# **Apple MLX फ्रेमवर्कसह Phi-3 चे फाइन-ट्यूनिंग**

Apple MLX फ्रेमवर्कच्या कमांड लाइनद्वारे Lora सोबत एकत्रित फाइन-ट्यूनिंग पूर्ण करू शकतो. (MLX फ्रेमवर्कच्या ऑपरेशनबद्दल अधिक जाणून घ्यायचे असल्यास, कृपया [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) वाचा)

## **1. डेटा तयार करणे**

डीफॉल्टनुसार, MLX फ्रेमवर्कला train, test, आणि eval साठी jsonl फॉरमॅटची आवश्यकता असते, आणि Lora सोबत एकत्रित करून फाइन-ट्यूनिंग जॉब्स पूर्ण करतो.

### ***टीप:***

1. jsonl डेटा फॉरमॅटः

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. आमच्या उदाहरणात [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) वापरले आहे, परंतु डेटाचा प्रमाण तुलनेने अपुरे आहे, त्यामुळे फाइन-ट्यूनिंगचे परिणाम नेहमीच सर्वोत्तम असतील असे नाही. शिकणाऱ्यांनी आपल्या स्वतःच्या गरजांनुसार चांगल्या डेटाचा वापर करून फाइन-ट्यूनिंग पूर्ण करावे, अशी शिफारस केली जाते.

3. डेटा Phi-3 टेम्प्लेटसह एकत्रित आहे.

कृपया या [लिंक](../../../../code/04.Finetuning/mlx) वरून डेटा डाउनलोड करा आणि ***data*** फोल्डरमध्ये सर्व .jsonl समाविष्ट करा.

## **2. तुमच्या टर्मिनलमध्ये फाइन-ट्यूनिंग**

कृपया हा कमांड टर्मिनलमध्ये चालवा:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***टीप:***

1. हे LoRA फाइन-ट्यूनिंग आहे, MLX फ्रेमवर्कने QLoRA प्रकाशित केलेले नाही.

2. तुम्ही config.yaml सेट करून काही arguments बदलू शकता, जसे की:

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

कृपया हा कमांड टर्मिनलमध्ये चालवा:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. फाइन-ट्यूनिंग अडॅप्टर चालवून चाचणी करा**

तुम्ही टर्मिनलमध्ये फाइन-ट्यूनिंग अडॅप्टर चालवू शकता, अशा प्रकारे:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

आणि मूळ मॉडेल चालवून परिणामाची तुलना करा:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

तुम्ही फाइन-ट्यूनिंगच्या परिणामांची मूळ मॉडेलशी तुलना करून पाहू शकता.

## **4. अडॅप्टर्स एकत्रित करून नवीन मॉडेल्स तयार करा**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama वापरून क्वांटिफाइड फाइन-ट्यूनिंग मॉडेल्स चालवणे**

वापरण्यापूर्वी, कृपया तुमचे llama.cpp वातावरण कॉन्फिगर करा.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***टीप:*** 

1. आता fp32, fp16 आणि INT 8 च्या क्वांटायझेशन कन्व्हर्जनला सपोर्ट करते.

2. एकत्रित मॉडेलमध्ये tokenizer.model गायब आहे, कृपया ते https://huggingface.co/microsoft/Phi-3-mini-4k-instruct येथून डाउनलोड करा.

Ollama मॉडेल फाइल सेट करा (जर Ollama इंस्टॉल केलेले नसेल, तर कृपया [Ollama QuickStart](https://ollama.com/) वाचा).

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

टर्मिनलमध्ये कमांड चालवा:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

अभिनंदन! MLX फ्रेमवर्कसह फाइन-ट्यूनिंगमध्ये प्रवीण झालात.

**अस्वीकृती**:  
हे दस्तऐवज मशीन-आधारित एआय भाषांतर सेवांचा वापर करून भाषांतरित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने ग्रस्त असू शकतात. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.