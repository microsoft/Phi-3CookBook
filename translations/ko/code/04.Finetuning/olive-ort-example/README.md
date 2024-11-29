# Olive을 사용하여 Phi3 미세 조정하기

이 예제에서는 Olive을 사용하여 다음을 수행합니다:

1. LoRA 어댑터를 미세 조정하여 문장을 슬픔, 기쁨, 두려움, 놀람으로 분류합니다.
1. 어댑터 가중치를 기본 모델에 병합합니다.
1. 모델을 최적화하고 `int4`로 양자화합니다.

또한 ONNX Runtime (ORT) Generate API를 사용하여 미세 조정된 모델을 추론하는 방법도 보여드리겠습니다.

> **⚠️ 미세 조정을 위해서는 적합한 GPU가 필요합니다 - 예를 들어, A10, V100, A100.**

## 💾 설치

새로운 Python 가상 환경을 만듭니다 (예를 들어, `conda`를 사용하여):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

다음으로, Olive 및 미세 조정 워크플로우에 필요한 종속성을 설치합니다:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive을 사용하여 Phi3 미세 조정하기
[Olive 설정 파일](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)에는 다음과 같은 *패스*가 포함된 *워크플로우*가 포함되어 있습니다:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

이 워크플로우는 다음과 같은 작업을 수행합니다:

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 데이터를 사용하여 Phi3을 미세 조정합니다 (150단계로, 필요에 따라 수정할 수 있습니다).
1. LoRA 어댑터 가중치를 기본 모델에 병합합니다. 이렇게 하면 ONNX 형식의 단일 모델 아티팩트를 얻을 수 있습니다.
1. Model Builder가 ONNX 런타임에 맞게 모델을 최적화하고 모델을 `int4`로 양자화합니다.

워크플로우를 실행하려면 다음을 실행하세요:

```bash
olive run --config phrase-classification.json
```

Olive이 완료되면 최적화된 `int4` 미세 조정된 Phi3 모델이 다음 위치에 제공됩니다: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 미세 조정된 Phi3을 애플리케이션에 통합하기 

앱을 실행하려면:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

이 응답은 문장의 단어 분류 (슬픔/기쁨/두려움/놀람) 중 하나여야 합니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.