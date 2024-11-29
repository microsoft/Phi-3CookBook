# MLflow

[MLflow](https://mlflow.org/)는 머신 러닝 라이프사이클 전반을 관리하기 위해 설계된 오픈 소스 플랫폼입니다.

![MLFlow](../../../../translated_images/MlFlowmlops.9c163870a3150e994d8e662d65cdb1158e5e87df857f4c7793eb04367e4748dd.ko.png)

MLFlow는 실험, 재현성, 배포 및 중앙 모델 레지스트리를 포함한 ML 라이프사이클을 관리하는 데 사용됩니다. 현재 MLFlow는 네 가지 구성 요소를 제공합니다.

- **MLflow Tracking:** 실험, 코드, 데이터 구성 및 결과를 기록하고 쿼리합니다.
- **MLflow Projects:** 데이터 과학 코드를 어떤 플랫폼에서도 실행할 수 있는 형식으로 패키징합니다.
- **MLflow Models:** 다양한 서빙 환경에서 머신 러닝 모델을 배포합니다.
- **Model Registry:** 모델을 중앙 저장소에 저장, 주석 및 관리합니다.

MLFlow는 실험 추적, 재현 가능한 실행을 위한 코드 패키징, 모델 공유 및 배포 기능을 포함합니다. MLFlow는 Databricks에 통합되어 있으며 다양한 ML 라이브러리를 지원하여 라이브러리 독립적입니다. REST API와 CLI를 제공하므로 어떤 머신 러닝 라이브러리나 프로그래밍 언어에서도 사용할 수 있습니다.

![MLFlow](../../../../translated_images/MLflow2.4b79a06c76e338ff4deea61f7c0ffd0d9ae2ddff2e20a4c43f2c1098c13bb54b.ko.png)

MLFlow의 주요 기능은 다음과 같습니다:

- **실험 추적:** 매개변수와 결과를 기록하고 비교합니다.
- **모델 관리:** 다양한 서빙 및 추론 플랫폼에 모델을 배포합니다.
- **모델 레지스트리:** MLFlow 모델의 라이프사이클을 협력적으로 관리하며, 버전 관리와 주석을 포함합니다.
- **프로젝트:** ML 코드를 공유하거나 프로덕션용으로 패키징합니다.
MLFlow는 데이터 준비, 모델 등록 및 관리, 모델 실행을 위한 패키징, 서비스 배포, 모델 모니터링을 포함하는 MLOps 루프도 지원합니다. 특히 클라우드 및 엣지 환경에서 프로토타입에서 프로덕션 워크플로로 이동하는 과정을 단순화하는 것을 목표로 합니다.

## E2E 시나리오 - 래퍼를 만들고 Phi-3을 MLFlow 모델로 사용하기

이 E2E 샘플에서는 Phi-3 소형 언어 모델(SLM) 주위에 래퍼를 만드는 두 가지 접근 방식을 보여주고, 이를 로컬 또는 클라우드(예: Azure Machine Learning 작업 공간)에서 MLFlow 모델로 실행하는 방법을 시연합니다.

![MLFlow](../../../../translated_images/MlFlow1.03f2450731cbbebec395ae9820571ba0ac8fd5e37462c26b7cf6bc00ca4d899a.ko.png)

| 프로젝트 | 설명 | 위치 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline은 HuggingFace 모델을 MLFlow의 실험적 transformers flavour와 함께 사용하고자 할 때 래퍼를 만드는 가장 쉬운 옵션입니다. | [**TransformerPipeline.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | 작성 당시 Transformer Pipeline은 ONNX 형식의 HuggingFace 모델에 대해 MLFlow 래퍼 생성을 지원하지 않았습니다. 이러한 경우에는 MLFlow 모드를 위한 사용자 정의 Python 래퍼를 만들 수 있습니다. | [**CustomPythonWrapper.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## 프로젝트: Transformer Pipeline

1. MLFlow와 HuggingFace의 관련 Python 패키지가 필요합니다:

    ``` Python
    import mlflow
    import transformers
    ```

2. 다음으로, HuggingFace 레지스트리에서 대상 Phi-3 모델을 참조하여 transformer pipeline을 시작해야 합니다. _Phi-3-mini-4k-instruct_ 모델 카드에서 볼 수 있듯이, 이 모델의 작업 유형은 "텍스트 생성"입니다:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. 이제 Phi-3 모델의 transformer pipeline을 MLFlow 형식으로 저장하고, 대상 아티팩트 경로, 특정 모델 구성 설정 및 추론 API 유형과 같은 추가 세부 정보를 제공할 수 있습니다:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## 프로젝트: Custom Python Wrapper

1. 여기서 Microsoft의 [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai)를 ONNX 모델의 추론 및 토큰 인코딩/디코딩에 사용할 수 있습니다. 아래 예시는 CPU를 대상으로 하는 _onnxruntime_genai_ 패키지를 선택합니다:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. 우리의 사용자 정의 클래스는 두 가지 메서드를 구현합니다: **ONNX 모델**인 Phi-3 Mini 4K Instruct, **생성기 매개변수** 및 **토크나이저**를 초기화하는 _load_context()_와 제공된 프롬프트에 대한 출력 토큰을 생성하는 _predict()_입니다:

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

1. 이제 _mlflow.pyfunc.log_model()_ 함수를 사용하여 Phi-3 모델에 대한 사용자 정의 Python 래퍼(피클 형식)를 생성하고, 원래의 ONNX 모델 및 필요한 종속성을 함께 생성할 수 있습니다:

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

## 생성된 MLFlow 모델의 시그니처

1. 위의 Transformer Pipeline 프로젝트의 3단계에서, 우리는 MLFlow 모델의 작업을 “_llm/v1/chat_”으로 설정했습니다. 이러한 지침은 아래와 같이 OpenAI의 Chat API와 호환되는 모델의 API 래퍼를 생성합니다:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. 결과적으로, 다음 형식으로 프롬프트를 제출할 수 있습니다:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. 그런 다음, OpenAI API 호환 후처리(e.g., _response[0][‘choices’][0][‘message’][‘content’]_)를 사용하여 출력 결과를 다음과 같이 아름답게 만들 수 있습니다:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. 위의 Custom Python Wrapper 프로젝트의 3단계에서, 우리는 MLFlow 패키지가 주어진 입력 예제에서 모델의 시그니처를 생성하도록 허용합니다. 우리의 MLFlow 래퍼의 시그니처는 다음과 같습니다:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. 따라서, 우리의 프롬프트는 다음과 같이 "prompt" 딕셔너리 키를 포함해야 합니다:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. 모델의 출력은 문자열 형식으로 제공됩니다:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 본래 언어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 우리는 책임을 지지 않습니다.