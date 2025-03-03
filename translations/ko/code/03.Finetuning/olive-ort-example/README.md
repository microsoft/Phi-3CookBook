# Olive를 사용하여 Phi3 미세 조정하기

이 예제에서는 Olive를 사용하여 다음을 수행합니다:

1. 문구를 Sad, Joy, Fear, Surprise로 분류하는 LoRA 어댑터를 미세 조정합니다.
1. 어댑터 가중치를 기본 모델에 병합합니다.
1. 모델을 `int4`로 최적화하고 양자화합니다.

또한 ONNX Runtime (ORT) Generate API를 사용하여 미세 조정된 모델을 추론하는 방법도 보여드립니다.

> **⚠️ 미세 조정을 위해 적합한 GPU가 필요합니다 - 예를 들어, A10, V100, A100.**

## 💾 설치

새로운 Python 가상 환경을 생성하세요 (예: `conda` 사용):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

다음으로, Olive와 미세 조정 워크플로우에 필요한 종속성을 설치하세요:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive를 사용하여 Phi3 미세 조정하기
[Olive 구성 파일](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json)에는 다음 *패스*를 포함하는 *워크플로우*가 있습니다:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

이 워크플로우는 다음과 같은 고수준 작업을 수행합니다:

1. [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 데이터를 사용하여 Phi3를 (150단계 동안, 원하는 경우 수정 가능) 미세 조정합니다.
1. LoRA 어댑터 가중치를 기본 모델에 병합합니다. 이를 통해 ONNX 형식의 단일 모델 아티팩트를 생성합니다.
1. Model Builder는 모델을 ONNX 런타임에 최적화하고 모델을 `int4`로 양자화합니다.

워크플로우를 실행하려면 다음을 실행하세요:

```bash
olive run --config phrase-classification.json
```

Olive가 완료되면, 최적화된 `int4` 미세 조정 Phi3 모델은 `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`에 저장됩니다.

## 🧑‍💻 미세 조정된 Phi3를 애플리케이션에 통합하기 

앱을 실행하려면:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

이 응답은 문구에 대한 단일 단어 분류 (Sad/Joy/Fear/Surprise)여야 합니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.