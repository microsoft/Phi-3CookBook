# **로컬 서버에서 Phi-3 추론**

로컬 서버에 Phi-3를 배포할 수 있습니다. 사용자는 [Ollama](https://ollama.com) 또는 [LM Studio](https://llamaedge.com) 솔루션을 선택하거나 직접 코드를 작성할 수 있습니다. [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) 또는 [Langchain](https://www.langchain.com/)을 통해 Phi-3의 로컬 서비스를 연결하여 Copilot 애플리케이션을 만들 수 있습니다.

## **Semantic Kernel을 사용하여 Phi-3-mini에 접근하기**

Copilot 애플리케이션에서는 Semantic Kernel / LangChain을 통해 애플리케이션을 만듭니다. 이 유형의 애플리케이션 프레임워크는 일반적으로 Azure OpenAI Service / OpenAI 모델과 호환되며, Hugging Face의 오픈 소스 모델 및 로컬 모델도 지원할 수 있습니다. 만약 Semantic Kernel을 사용하여 Phi-3-mini에 접근하려면 어떻게 해야 할까요? .NET을 예로 들어, 이를 Semantic Kernel의 Hugging Face Connector와 결합할 수 있습니다. 기본적으로 Hugging Face의 모델 ID에 대응할 수 있으며(처음 사용할 때 모델이 Hugging Face에서 다운로드되므로 시간이 오래 걸립니다), 자체 구축한 로컬 서비스에도 연결할 수 있습니다. 두 가지를 비교했을 때, 특히 기업 애플리케이션에서는 후자가 더 높은 자율성을 제공하므로 후자를 사용하는 것을 권장합니다.

![sk](../../../../translated_images/sk.fc8f38bb6ac491315099aa29a2704de109fc0b052448c9bc3d7c02586c196ca4.ko.png)

그림에서 볼 수 있듯이, Semantic Kernel을 통해 로컬 서비스에 접근하면 자체 구축한 Phi-3-mini 모델 서버에 쉽게 연결할 수 있습니다. 다음은 실행 결과입니다.

![skrun](../../../../translated_images/skrun.f579fcb28592ba4644af8b578e66fb01923bf032b670cef44874c6550e85876d.ko.png)

***샘플 코드*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.