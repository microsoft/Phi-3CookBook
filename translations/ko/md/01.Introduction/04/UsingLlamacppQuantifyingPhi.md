# **llama.cpp를 사용한 Phi 패밀리 양자화**

## **llama.cpp란 무엇인가**

llama.cpp는 Llama와 같은 다양한 대규모 언어 모델(LLM)에 대해 추론을 수행하는 오픈소스 소프트웨어 라이브러리로, 주로 C++로 작성되었습니다. 이 라이브러리의 주요 목표는 최소한의 설정으로 다양한 하드웨어에서 최첨단 성능의 LLM 추론을 제공하는 것입니다. 또한, 텍스트 완성과 OpenAI 호환 웹 서버를 위한 고수준 API를 제공하는 Python 바인딩도 사용할 수 있습니다.

llama.cpp의 주요 목표는 최소한의 설정으로 로컬 및 클라우드에서 다양한 하드웨어에서 최첨단 성능의 LLM 추론을 가능하게 하는 것입니다.

- 의존성 없는 순수 C/C++ 구현
- Apple 실리콘 최적화 - ARM NEON, Accelerate 및 Metal 프레임워크를 통해 최적화
- x86 아키텍처를 위한 AVX, AVX2 및 AVX512 지원
- 더 빠른 추론과 메모리 사용 감소를 위한 1.5비트, 2비트, 3비트, 4비트, 5비트, 6비트, 8비트 정수 양자화
- NVIDIA GPU에서 LLM을 실행하기 위한 맞춤형 CUDA 커널 (AMD GPU는 HIP을 통해 지원)
- Vulkan 및 SYCL 백엔드 지원
- VRAM 용량을 초과하는 대형 모델의 일부 가속을 위한 CPU+GPU 하이브리드 추론

## **llama.cpp를 사용한 Phi-3.5 양자화**

Phi-3.5-Instruct 모델은 llama.cpp를 사용하여 양자화할 수 있지만, Phi-3.5-Vision 및 Phi-3.5-MoE는 아직 지원되지 않습니다. llama.cpp로 변환된 형식은 gguf이며, 이는 가장 널리 사용되는 양자화 형식이기도 합니다.

Hugging Face에는 수많은 양자화된 GGUF 형식 모델이 있습니다. AI Foundry, Ollama, LlamaEdge는 llama.cpp에 의존하기 때문에 GGUF 모델이 자주 사용됩니다.

### **GGUF란 무엇인가**

GGUF는 모델의 빠른 로딩과 저장을 위해 최적화된 이진 형식으로, 추론 목적에 매우 효율적입니다. GGUF는 GGML 및 기타 실행 엔진과 함께 사용하도록 설계되었습니다. GGUF는 llama.cpp의 개발자인 @ggerganov에 의해 개발되었습니다. llama.cpp는 인기 있는 C/C++ LLM 추론 프레임워크입니다. PyTorch와 같은 프레임워크에서 처음 개발된 모델은 이러한 엔진과 함께 사용하기 위해 GGUF 형식으로 변환될 수 있습니다.

### **ONNX와 GGUF 비교**

ONNX는 전통적인 머신러닝/딥러닝 형식으로, 다양한 AI 프레임워크에서 잘 지원되며 엣지 디바이스에서 유용한 사용 시나리오를 가지고 있습니다. GGUF는 llama.cpp를 기반으로 하며, 생성형 AI(GenAI) 시대에 만들어졌다고 할 수 있습니다. 두 형식은 비슷한 용도를 가지고 있습니다. 임베디드 하드웨어 및 애플리케이션 계층에서 더 나은 성능을 원한다면 ONNX가 선택이 될 수 있습니다. 반면, llama.cpp의 파생 프레임워크와 기술을 사용한다면 GGUF가 더 나은 선택일 수 있습니다.

### **llama.cpp를 사용한 Phi-3.5-Instruct 양자화**

**1. 환경 설정**  

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```  

**2. 양자화**  

llama.cpp를 사용하여 Phi-3.5-Instruct를 FP16 GGUF로 변환  


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```  

Phi-3.5를 INT4로 양자화  


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```  

**3. 테스트**  

llama-cpp-python 설치  


```bash

pip install llama-cpp-python -U

```  

***참고***  

Apple Silicon을 사용하는 경우, 다음과 같이 llama-cpp-python을 설치하십시오  


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```  

테스트  


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```  

## **리소스**

1. llama.cpp에 대해 더 알아보기 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  

2. GGUF에 대해 더 알아보기 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)  

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원문이 작성된 언어의 문서를 권위 있는 원본으로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.