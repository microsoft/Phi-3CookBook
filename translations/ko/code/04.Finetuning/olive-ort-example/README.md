# Olive를 사용하여 Phi3 미세 조정하기

이 예제에서는 Olive를 사용하여 다음을 수행합니다:

1. LoRA 어댑터를 미세 조정하여 문구를 슬픔, 기쁨, 공포, 놀람으로 분류합니다.
2. 어댑터 가중치를 기본 모델에 병합합니다.
3. 모델을 최적화하고 `int4`로 양자화합니다.

또한 ONNX Runtime (ORT) Generate API를 사용하여 미세 조정된 모델을 추론하는 방법도 보여드리겠습니다.

> **⚠️ 미세 조정을 위해서는 적합한 GPU가 필요합니다 - 예를 들어, A10, V100, A100 등이 있습니다.**

## 💾 설치

새로운 Python 가상 환경을 만듭니다 (예를 들어, `conda`를 사용하여):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

다음으로, Olive와 미세 조정 워크플로우에 필요한 종속성을 설치합니다:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive를 사용하여 Phi3 미세 조정
[Olive 구성 파일](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)에는 다음과 같은 *패스*를 포함하는 *워크플로우*가 있습니다:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

고수준에서 이 워크플로우는 다음을 수행합니다:

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 데이터를 사용하여 Phi3을 (150단계 동안, 필요에 따라 수정 가능) 미세 조정합니다.
2. LoRA 어댑터 가중치를 기본 모델에 병합합니다. 이를 통해 ONNX 형식의 단일 모델 아티팩트를 얻을 수 있습니다.
3. Model Builder는 모델을 ONNX 런타임에 최적화하고 모델을 `int4`로 양자화합니다.

워크플로우를 실행하려면 다음을 실행합니다:

```bash
olive run --config phrase-classification.json
```

Olive가 완료되면, 최적화된 `int4` 미세 조정된 Phi3 모델이 `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`에 있습니다.

## 🧑‍💻 미세 조정된 Phi3을 애플리케이션에 통합하기

앱을 실행하려면:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

이 응답은 문구의 단일 단어 분류 (슬픔/기쁨/공포/놀람)이어야 합니다.

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정을 해주시기 바랍니다.