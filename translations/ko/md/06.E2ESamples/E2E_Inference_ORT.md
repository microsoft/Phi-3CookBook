# **Fine-tuning 모델 추론하기**

Fine-tuning을 마친 후, ONNX Runtime GenAI를 사용하여 새로운 모델에 접근할 수 있습니다.

## **ORT GenAI SDK 설치하기**

**참고** - 먼저 CUDA 12.1을 설치해야 합니다. 설치 방법을 모른다면 이 가이드를 참조하세요: [https://developer.nvidia.com/cuda-12-1-0-download-archive](https://developer.nvidia.com/cuda-12-1-0-download-archive)

CUDA 설치가 완료된 후, onnxruntime genai sdk를 cuda와 함께 설치하세요.

```bash

pip install numpy

pip install onnxruntime-genai-cuda --pre --index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-genai/pypi/simple/

```

## **모델 추론하기**

```python

import onnxruntime_genai as og

model = og.Model('Your onnx model folder location')
tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

search_options = {"max_length": 1024,"temperature":0.3}

params = og.GeneratorParams(model)
params.try_use_cuda_graph_with_max_batch_size(1)
params.set_search_options(**search_options)

prompt = "prompt = "<|user|>Who are you not allowed to marry in the UK?<|end|><|assistant|>""
input_tokens = tokenizer.encode(prompt)
params.input_ids = input_tokens

generator = og.Generator(model, params)

while not generator.is_done():
                generator.compute_logits()
                generator.generate_next_token()

                new_token = generator.get_next_tokens()[0]
                print(tokenizer_stream.decode(new_token), end='', flush=True)

```

### **결과 테스트하기**

![result](../../../../translated_images/result.b9b025fc2577ad5e3fd97341dd6c1e858a83c3291a4ed5ad4dc4fbd80a575b67.ko.png)

면책 조항: 이 번역은 AI 모델에 의해 원문에서 번역되었으며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주세요.