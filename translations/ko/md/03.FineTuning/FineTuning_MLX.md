# **Apple MLX 프레임워크로 Phi-3 파인튜닝**

Apple MLX 프레임워크 명령어를 통해 Lora와 결합하여 파인튜닝을 완료할 수 있습니다. (MLX 프레임워크의 작동 방식에 대해 더 알고 싶다면 [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)를 참고하세요.)

## **1. 데이터 준비**

기본적으로, MLX 프레임워크는 train, test, eval의 jsonl 형식을 요구하며, Lora와 결합하여 파인튜닝 작업을 완료합니다.

### ***참고:***

1. jsonl 데이터 형식:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 예제에서는 [TruthfulQA의 데이터](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)를 사용하지만, 데이터 양이 상대적으로 부족하기 때문에 파인튜닝 결과가 반드시 최적이라고 할 수는 없습니다. 학습자는 자신의 시나리오에 맞는 더 나은 데이터를 사용하여 작업을 완료하는 것을 권장합니다.

3. 데이터 형식은 Phi-3 템플릿과 결합되어야 합니다.

이 [링크](../../../../code/04.Finetuning/mlx)에서 데이터를 다운로드하세요. ***data*** 폴더에 있는 모든 .jsonl 파일을 포함해야 합니다.

## **2. 터미널에서 파인튜닝 실행**

터미널에서 다음 명령어를 실행하세요.

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***참고:***

1. 이는 LoRA 파인튜닝이며, MLX 프레임워크는 QLoRA를 아직 지원하지 않습니다.

2. config.yaml을 설정하여 다음과 같은 인수를 변경할 수 있습니다.

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

터미널에서 다음 명령어를 실행하세요.

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 파인튜닝 어댑터 테스트 실행**

터미널에서 파인튜닝 어댑터를 실행하려면 다음 명령어를 사용하세요.

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

그리고 원본 모델을 실행하여 결과를 비교하세요.

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

파인튜닝 결과와 원본 모델의 결과를 비교해볼 수 있습니다.

## **4. 어댑터 병합하여 새 모델 생성**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollama를 사용하여 양자화된 파인튜닝 모델 실행**

사용 전에 llama.cpp 환경을 설정하세요.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***참고:***

1. 현재 fp32, fp16, INT 8의 양자화 변환을 지원합니다.

2. 병합된 모델에는 tokenizer.model이 누락되어 있습니다. 이를 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 에서 다운로드하세요.

Ollama 모델 파일 설정 (Ollama를 설치하지 않았다면, [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)를 참고하세요.)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

터미널에서 다음 명령어를 실행하세요.

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

축하합니다! MLX 프레임워크로 파인튜닝을 마스터했습니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 모국어 버전이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.