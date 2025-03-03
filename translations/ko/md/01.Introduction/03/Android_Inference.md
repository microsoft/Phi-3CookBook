# **Android에서 Phi-3 추론하기**

Android 기기에서 Phi-3-mini를 사용해 추론을 수행하는 방법을 알아보겠습니다. Phi-3-mini는 Microsoft에서 새롭게 선보인 모델 시리즈로, 대규모 언어 모델(LLMs)을 엣지 기기와 IoT 기기에서 실행할 수 있도록 설계되었습니다.

## Semantic Kernel과 추론

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)은 Azure OpenAI Service, OpenAI 모델, 심지어 로컬 모델과 호환되는 애플리케이션을 만들 수 있게 해주는 애플리케이션 프레임워크입니다. Semantic Kernel을 처음 접하신다면 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)을 참고하시길 권장합니다.

### Semantic Kernel을 사용해 Phi-3-mini에 접근하기

Semantic Kernel에서 Hugging Face Connector를 결합해 사용할 수 있습니다. 자세한 내용은 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

기본적으로 Hugging Face의 모델 ID에 해당하지만, 로컬에서 빌드된 Phi-3-mini 모델 서버와도 연결할 수 있습니다.

### Ollama 또는 LlamaEdge로 양자화된 모델 호출하기

많은 사용자가 로컬에서 모델을 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com/)와 [LlamaEdge](https://llamaedge.com)는 개별 사용자가 다양한 양자화된 모델을 호출할 수 있도록 지원합니다:

#### Ollama

`ollama run Phi-3`을 직접 실행하거나, `Modelfile`을 생성해 `.gguf` 파일 경로를 설정하여 오프라인에서 구성할 수 있습니다.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

클라우드와 엣지 기기에서 동시에 `.gguf` 파일을 사용하고 싶다면, LlamaEdge가 훌륭한 선택입니다. 시작하려면 이 [샘플 코드](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)를 참고하세요.

### Android 폰에 설치하고 실행하기

1. **MLC Chat 앱 다운로드** (무료) - Android 폰용.
2. APK 파일(148MB)을 다운로드하고 기기에 설치하세요.
3. MLC Chat 앱을 실행합니다. Phi-3-mini를 포함한 AI 모델 목록이 표시됩니다.

요약하자면, Phi-3-mini는 엣지 기기에서 생성형 AI를 활용할 수 있는 흥미로운 가능성을 열어줍니다. Android에서 그 기능을 탐색해 보세요.

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태로 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.