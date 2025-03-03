Phi-3-mini의 맥락에서 추론이란, 모델을 사용하여 입력 데이터 기반으로 예측하거나 출력을 생성하는 과정을 의미합니다. Phi-3-mini와 그 추론 기능에 대해 더 자세히 설명드리겠습니다.

Phi-3-mini는 Microsoft에서 출시한 Phi-3 시리즈 모델의 일부입니다. 이 모델들은 소형 언어 모델(SLM)로 가능한 것의 한계를 재정의하도록 설계되었습니다.

다음은 Phi-3-mini와 그 추론 기능에 대한 주요 사항입니다:

## **Phi-3-mini 개요:**
- Phi-3-mini는 38억 개의 파라미터를 보유하고 있습니다.
- 전통적인 컴퓨팅 장치뿐만 아니라 모바일 기기나 IoT 기기와 같은 엣지 디바이스에서도 실행이 가능합니다.
- Phi-3-mini의 출시로 개인 및 기업이 자원 제한 환경에서도 다양한 하드웨어 장치에서 SLM을 배포할 수 있게 되었습니다.
- 이 모델은 전통적인 PyTorch 형식, gguf 형식의 양자화된 버전, 그리고 ONNX 기반의 양자화된 버전과 같은 다양한 모델 형식을 지원합니다.

## **Phi-3-mini에 접근하기:**
Phi-3-mini에 접근하려면 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 Copilot 애플리케이션에서 사용할 수 있습니다. Semantic Kernel은 Azure OpenAI Service, Hugging Face의 오픈소스 모델, 로컬 모델과 일반적으로 호환됩니다.  
또한 [Ollama](https://ollama.com)나 [LlamaEdge](https://llamaedge.com)를 사용하여 양자화된 모델을 호출할 수 있습니다. Ollama는 개인 사용자가 다양한 양자화된 모델을 호출할 수 있게 해주며, LlamaEdge는 GGUF 모델의 크로스 플랫폼 가용성을 제공합니다.

## **양자화된 모델:**
많은 사용자가 로컬 추론을 위해 양자화된 모델을 선호합니다. 예를 들어, Ollama를 사용하여 Phi-3을 직접 실행하거나 Modelfile을 사용하여 오프라인으로 구성할 수 있습니다. Modelfile은 GGUF 파일 경로와 프롬프트 형식을 지정합니다.

## **생성형 AI 가능성:**
Phi-3-mini와 같은 SLM을 결합하면 생성형 AI의 새로운 가능성이 열립니다. 추론은 첫 번째 단계일 뿐이며, 이러한 모델들은 자원 제한, 지연 시간 제약, 비용 제약과 같은 다양한 시나리오에서 여러 작업에 사용할 수 있습니다.

## **Phi-3-mini를 활용한 생성형 AI 잠재력: 추론 및 배포 가이드**
Semantic Kernel, Ollama/LlamaEdge, ONNX Runtime을 사용하여 Phi-3-mini 모델에 접근하고 추론하는 방법을 배우며, 다양한 애플리케이션 시나리오에서 생성형 AI의 가능성을 탐구해 보세요.

**기능**
Phi-3-mini 모델 추론 가능 플랫폼:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

요약하자면, Phi-3-mini는 개발자들이 다양한 모델 형식을 탐구하고 여러 애플리케이션 시나리오에서 생성형 AI를 활용할 수 있도록 해줍니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.