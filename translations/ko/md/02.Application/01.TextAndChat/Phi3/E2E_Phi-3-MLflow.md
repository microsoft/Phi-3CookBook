# MLflow

[MLflow](https://mlflow.org/)는 머신러닝 라이프사이클 전 과정을 관리하기 위해 설계된 오픈소스 플랫폼입니다.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.ko.png)

MLflow는 실험, 재현성, 배포 및 중앙 모델 레지스트리를 포함한 ML 라이프사이클을 관리하는 데 사용됩니다. 현재 MLflow는 네 가지 주요 구성 요소를 제공합니다.

- **MLflow Tracking:** 실험, 코드, 데이터 구성 및 결과를 기록하고 조회합니다.
- **MLflow Projects:** 데이터 과학 코드를 어떤 플랫폼에서도 실행 가능한 형식으로 패키징합니다.
- **MLflow Models:** 다양한 서빙 환경에서 머신러닝 모델을 배포합니다.
- **Model Registry:** 중앙 저장소에서 모델을 저장, 주석 작성 및 관리합니다.

MLflow는 실험 추적, 코드의 재현 가능한 실행 패키징, 모델 공유 및 배포 기능을 포함합니다. MLflow는 Databricks에 통합되어 있으며 다양한 ML 라이브러리를 지원하므로 라이브러리 비종속적입니다. REST API와 CLI를 제공하므로 어떤 머신러닝 라이브러리 및 프로그래밍 언어에서도 사용할 수 있습니다.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.ko.png)

MLflow의 주요 기능은 다음과 같습니다:

- **실험 추적:** 매개변수와 결과를 기록하고 비교합니다.
- **모델 관리:** 다양한 서빙 및 추론 플랫폼에 모델을 배포합니다.
- **모델 레지스트리:** 버전 관리와 주석을 포함하여 MLflow 모델의 라이프사이클을 협업적으로 관리합니다.
- **프로젝트:** ML 코드를 공유하거나 프로덕션 용도로 패키징합니다.

MLflow는 데이터 준비, 모델 등록 및 관리, 실행을 위한 모델 패키징, 서비스 배포 및 모델 모니터링을 포함하는 MLOps 루프도 지원합니다. 특히 클라우드와 엣지 환경에서 프로토타입에서 프로덕션 워크플로로 이동하는 과정을 단순화하는 것을 목표로 합니다.

## E2E 시나리오 - 래퍼 생성 및 Phi-3을 MLflow 모델로 사용하기

이 E2E 샘플에서는 Phi-3 소형 언어 모델(SLM)을 래핑하는 두 가지 다른 접근 방식을 보여주고, 이를 로컬 또는 클라우드(예: Azure Machine Learning 워크스페이스)에서 MLflow 모델로 실행하는 방법을 설명합니다.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.ko.png)

| 프로젝트 | 설명 | 위치 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline은 HuggingFace 모델을 MLflow의 실험적 변환기 기능과 함께 사용하려는 경우 래퍼를 생성하는 가장 간단한 옵션입니다. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | 작성 당시, 변환기 파이프라인은 ONNX 형식의 HuggingFace 모델에 대해 MLflow 래퍼 생성을 지원하지 않았습니다. 이러한 경우에는 MLflow 모드에 대한 사용자 정의 Python 래퍼를 생성할 수 있습니다. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## 프로젝트: Transformer Pipeline

1. MLflow 및 HuggingFace와 관련된 Python 패키지가 필요합니다:

    ``` Python
    import mlflow
    import transformers
    ```

2. 다음으로, HuggingFace 레지스트리의 대상 Phi-3 모델을 참조하여 변환기 파이프라인을 초기화해야 합니다. _Phi-3-mini-4k-instruct_의 모델 카드에서 알 수 있듯이, 이 모델의 작업 유형은 "텍스트 생성"입니다:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. 이제 Phi-3 모델의 변환기 파이프라인을 MLflow 형식으로 저장하고, 대상 아티팩트 경로, 특정 모델 구성 설정 및 추론 API 유형과 같은 추가 세부 정보를 제공할 수 있습니다:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## 프로젝트: Custom Python Wrapper

1. 여기서는 ONNX 모델의 추론과 토큰 인코딩/디코딩을 위해 Microsoft의 [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai)를 사용할 수 있습니다. 아래 예시는 CPU를 대상으로 _onnxruntime_genai_ 패키지를 선택합니다:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

2. 우리의 사용자 정의 클래스는 두 가지 메서드를 구현합니다: _load_context()_는 Phi-3 Mini 4K Instruct의 **ONNX 모델**, **생성기 매개변수**, **토크나이저**를 초기화하고, _predict()_는 제공된 프롬프트에 대해 출력 토큰을 생성합니다:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

3. 이제 _mlflow.pyfunc.log_model()_ 함수를 사용하여 Phi-3 모델에 대한 사용자 정의 Python 래퍼(피클 형식)와 원본 ONNX 모델 및 필요한 종속성을 생성할 수 있습니다:

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## 생성된 MLflow 모델의 서명

1. 위의 Transformer Pipeline 프로젝트의 3단계에서 MLflow 모델의 작업을 "_llm/v1/chat_"로 설정했습니다. 이러한 지시사항은 OpenAI의 Chat API와 호환되는 모델의 API 래퍼를 생성합니다:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

2. 결과적으로, 아래 형식으로 프롬프트를 제출할 수 있습니다:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

3. 그런 다음 OpenAI API와 호환되는 후처리(예: _response[0][‘choices’][0][‘message’][‘content’]_)를 사용하여 결과를 다음과 같이 보기 좋게 만들 수 있습니다:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

4. 위의 Custom Python Wrapper 프로젝트의 3단계에서는 제공된 입력 예제를 기반으로 MLflow 패키지가 모델 서명을 생성하도록 설정했습니다. 우리의 MLflow 래퍼 서명은 다음과 같습니다:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

5. 따라서 프롬프트는 "prompt"라는 딕셔너리 키를 포함해야 합니다. 예시는 다음과 같습니다:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

6. 모델의 출력은 문자열 형식으로 제공됩니다:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.