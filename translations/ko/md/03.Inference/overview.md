Phi-3-mini의 맥락에서 추론이란 모델을 사용하여 입력 데이터 기반으로 예측하거나 출력을 생성하는 과정을 의미합니다. Phi-3-mini와 그 추론 기능에 대해 더 자세히 설명드리겠습니다.

Phi-3-mini는 Microsoft가 출시한 Phi-3 시리즈 모델의 일부입니다. 이 모델들은 소형 언어 모델(SLM)로 가능한 것을 재정의하도록 설계되었습니다.

다음은 Phi-3-mini와 그 추론 기능에 대한 주요 사항입니다:

## **Phi-3-mini 개요:**
- Phi-3-mini는 38억 개의 파라미터를 가지고 있습니다.
- 전통적인 컴퓨팅 장치뿐만 아니라 모바일 장치나 IoT 장치 같은 엣지 장치에서도 실행할 수 있습니다.
- Phi-3-mini의 출시로 개인과 기업은 자원이 제한된 환경에서도 다양한 하드웨어 장치에 SLM을 배포할 수 있게 되었습니다.
- 전통적인 PyTorch 포맷, gguf 포맷의 양자화 버전, ONNX 기반 양자화 버전을 포함한 다양한 모델 포맷을 지원합니다.

## **Phi-3-mini 접근 방법:**
Phi-3-mini에 접근하려면 Copilot 애플리케이션에서 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 사용할 수 있습니다. Semantic Kernel은 일반적으로 Azure OpenAI Service, Hugging Face의 오픈 소스 모델, 로컬 모델과 호환됩니다.
또한 [Ollama](https://ollama.com)나 [LlamaEdge](https://llamaedge.com)를 사용하여 양자화 모델을 호출할 수 있습니다. Ollama는 개별 사용자가 다양한 양자화 모델을 호출할 수 있게 하고, LlamaEdge는 GGUF 모델의 크로스 플랫폼 가용성을 제공합니다.

## **양자화 모델:**
많은 사용자들이 로컬 추론을 위해 양자화 모델을 사용하는 것을 선호합니다. 예를 들어, Ollama run Phi-3를 직접 실행하거나 Modelfile을 사용하여 오프라인으로 구성할 수 있습니다. Modelfile은 GGUF 파일 경로와 프롬프트 포맷을 지정합니다.

## **생성 AI 가능성:**
Phi-3-mini와 같은 SLM을 결합하면 생성 AI의 새로운 가능성이 열립니다. 추론은 첫 단계일 뿐이며, 이 모델들은 자원이 제한되고, 지연 시간이 중요하며, 비용이 제한된 시나리오에서 다양한 작업에 사용될 수 있습니다.

## **Phi-3-mini로 생성 AI 잠금 해제: 추론 및 배포 가이드**
Semantic Kernel, Ollama/LlamaEdge, ONNX Runtime을 사용하여 Phi-3-mini 모델에 접근하고 추론하는 방법을 배우고, 다양한 애플리케이션 시나리오에서 생성 AI의 가능성을 탐색해보세요.

**특징**
phi3-mini 모델 추론 가능:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

요약하자면, Phi-3-mini는 개발자들이 다양한 모델 포맷을 탐색하고 다양한 애플리케이션 시나리오에서 생성 AI를 활용할 수 있도록 합니다.

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정을 해주시기 바랍니다.