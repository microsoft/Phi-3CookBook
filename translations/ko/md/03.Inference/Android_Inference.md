# **안드로이드에서 Phi-3 추론**

안드로이드 기기에서 Phi-3-mini를 사용하여 추론을 수행하는 방법을 살펴보겠습니다. Phi-3-mini는 Microsoft의 새로운 모델 시리즈로, 엣지 기기와 IoT 기기에 대형 언어 모델(LLM)을 배포할 수 있게 해줍니다.

## Semantic Kernel과 추론

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)은 Azure OpenAI Service, OpenAI 모델, 심지어 로컬 모델과 호환되는 애플리케이션을 만들 수 있게 해주는 애플리케이션 프레임워크입니다. Semantic Kernel이 처음이라면 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 참고하는 것을 권장합니다.

### Semantic Kernel을 사용하여 Phi-3-mini에 접근하기

Semantic Kernel에서 Hugging Face Connector와 결합할 수 있습니다. 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

기본적으로 Hugging Face의 모델 ID에 해당하지만, 로컬에서 구축한 Phi-3-mini 모델 서버에 연결할 수도 있습니다.

### Ollama 또는 LlamaEdge로 양자화된 모델 호출

많은 사용자가 로컬에서 모델을 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com/)와 [LlamaEdge](https://llamaedge.com)는 개별 사용자가 다양한 양자화된 모델을 호출할 수 있게 해줍니다:

#### Ollama

`ollama run Phi-3`를 직접 실행하거나 `.gguf` 파일 경로를 포함한 `Modelfile`을 만들어 오프라인으로 구성할 수 있습니다.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

클라우드와 엣지 기기에서 동시에 `.gguf` 파일을 사용하고 싶다면, LlamaEdge가 좋은 선택입니다. 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)를 참고하여 시작할 수 있습니다.

### 안드로이드 폰에 설치 및 실행

1. **MLC Chat 앱** (무료)을 안드로이드 폰에 다운로드합니다.
2. APK 파일(148MB)을 다운로드하여 기기에 설치합니다.
3. MLC Chat 앱을 실행합니다. Phi-3-mini를 포함한 AI 모델 목록이 표시됩니다.

요약하자면, Phi-3-mini는 엣지 기기에서 생성 AI의 새로운 가능성을 열어줍니다. 안드로이드에서 그 기능을 탐색해 보세요.

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.