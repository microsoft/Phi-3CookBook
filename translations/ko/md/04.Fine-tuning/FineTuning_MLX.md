# **Apple MLX 프레임워크를 사용한 Phi-3 미세 조정**

Apple MLX 프레임워크 명령어를 통해 Lora와 결합한 미세 조정을 완료할 수 있습니다. (MLX 프레임워크의 작동에 대해 더 알고 싶다면 [Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md)를 읽어보세요)


## **1. 데이터 준비**

기본적으로 MLX 프레임워크는 train, test, eval의 jsonl 형식을 필요로 하며, 이는 Lora와 결합하여 미세 조정 작업을 완료합니다.


### ***참고:***

1. jsonl 데이터 형식:


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 예제에서는 [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)를 사용했지만, 데이터 양이 충분하지 않아 미세 조정 결과가 최선이 아닐 수 있습니다. 학습자는 자신의 시나리오에 맞는 더 나은 데이터를 사용하는 것이 좋습니다.

3. 데이터 형식은 Phi-3 템플릿과 결합됩니다.

이 [링크](../../../../code/04.Finetuning/mlx)에서 데이터를 다운로드하고, ***data*** 폴더에 모든 .jsonl 파일을 포함해주세요.


## **2. 터미널에서 미세 조정**

터미널에서 이 명령어를 실행하세요


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***참고:***

1. 이것은 LoRA 미세 조정이며, MLX 프레임워크는 QLoRA를 아직 공개하지 않았습니다.

2. config.yaml을 설정하여 몇 가지 인수를 변경할 수 있습니다. 예를 들어:


```yaml


# 로컬 모델 디렉토리 또는 Hugging Face repo 경로
model: "microsoft/Phi-3-mini-4k-instruct"
# 학습 여부 (boolean)
train: true

# {train, valid, test}.jsonl 파일이 있는 디렉토리
data: "data"

# PRNG 시드
seed: 0

# 미세 조정할 레이어 수
lora_layers: 32

# 미니배치 크기
batch_size: 1

# 학습 반복 횟수
iters: 1000

# 검증 배치 수, -1은 전체 검증 세트를 사용
val_batches: 25

# Adam 학습률
learning_rate: 1e-6

# 손실 보고 간격
steps_per_report: 10

# 검증 간격
steps_per_eval: 200

# 어댑터 가중치를 사용하여 학습을 재개할 경로
resume_adapter_file: null

# 학습된 어댑터 가중치를 저장/로드할 경로
adapter_path: "adapters"

# N 반복마다 모델 저장
save_every: 1000

# 학습 후 테스트 세트 평가
test: false

# 테스트 세트 배치 수, -1은 전체 테스트 세트를 사용
test_batches: 100

# 최대 시퀀스 길이
max_seq_length: 2048

# 메모리 사용을 줄이기 위해 그래디언트 체크포인팅 사용
grad_checkpoint: true

# LoRA 매개변수는 config 파일에서만 지정할 수 있음
lora_parameters:
  # LoRA를 적용할 레이어 키
  # 마지막 lora_layers에 적용됨
  keys: ["o_proj","qkv_proj"]
  rank: 64
  alpha: 64
  dropout: 0.1


```

터미널에서 이 명령어를 실행하세요


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. 미세 조정 어댑터 실행하여 테스트**

터미널에서 미세 조정 어댑터를 실행할 수 있습니다. 예를 들어


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

그리고 원본 모델을 실행하여 결과를 비교하세요


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

미세 조정 결과와 원본 모델의 결과를 비교해보세요


## **4. 어댑터 병합하여 새로운 모델 생성**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama를 사용하여 양자화된 미세 조정 모델 실행**

사용하기 전에 llama.cpp 환경을 설정하세요


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***참고:*** 

1. 현재 fp32, fp16 및 INT 8의 양자화 변환을 지원합니다.

2. 병합된 모델에는 tokenizer.model이 없으므로 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct에서 다운로드하세요.

Ollama 모델 파일 설정 (ollama가 설치되지 않았다면 [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)를 참조하세요)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

터미널에서 명령어를 실행하세요


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

축하합니다! MLX 프레임워크를 사용한 미세 조정을 마스터했습니다.

면책 조항: 이 번역은 AI 모델에 의해 원문에서 번역되었으며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주세요.