# 언급된 주요 기술

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - DirectX 12 위에 구축된 하드웨어 가속 머신 러닝을 위한 저수준 API.
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - Nvidia가 개발한 병렬 컴퓨팅 플랫폼 및 API 모델로, 그래픽 처리 장치(GPU)에서 범용 처리를 가능하게 함.
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - 머신 러닝 모델을 표현하기 위해 설계된 개방형 포맷으로, 다양한 ML 프레임워크 간의 상호 운용성을 제공함.
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - 머신 러닝 모델을 표현하고 업데이트하는 데 사용되는 포맷으로, 4-8비트 양자화로 CPU에서 효과적으로 실행할 수 있는 소형 언어 모델에 특히 유용함.

## DirectML

DirectML은 하드웨어 가속 머신 러닝을 가능하게 하는 저수준 API입니다. DirectX 12 위에 구축되어 GPU 가속을 활용하며, 벤더에 구애받지 않기 때문에 다양한 GPU 벤더에서 코드 변경 없이 작동합니다. 주로 GPU에서 모델 훈련과 추론 작업에 사용됩니다.

하드웨어 지원 측면에서 DirectML은 AMD 통합 및 독립형 GPU, Intel 통합 GPU, NVIDIA 독립형 GPU를 포함한 다양한 GPU와 작동하도록 설계되었습니다. 이는 Windows AI 플랫폼의 일부이며, Windows 10 및 11에서 지원되어 모든 Windows 장치에서 모델 훈련과 추론을 가능하게 합니다.

DirectML과 관련된 업데이트와 기회로는 최대 150개의 ONNX 연산자를 지원하고, ONNX 런타임과 WinML에서 사용된다는 점이 있습니다. 주요 통합 하드웨어 벤더(IHV)들이 다양한 메타명령을 구현하여 이를 지원하고 있습니다.

## CUDA

CUDA는 Compute Unified Device Architecture의 약자로, Nvidia가 만든 병렬 컴퓨팅 플랫폼 및 API 모델입니다. 소프트웨어 개발자가 CUDA 지원 GPU를 사용하여 범용 처리를 수행할 수 있게 하며, 이를 GPGPU(General-Purpose computing on Graphics Processing Units)라고 합니다. CUDA는 Nvidia의 GPU 가속을 가능하게 하는 주요 기술로, 머신 러닝, 과학 컴퓨팅, 비디오 처리 등 다양한 분야에서 널리 사용됩니다.

CUDA의 하드웨어 지원은 Nvidia의 GPU에 한정되며, 이는 Nvidia가 개발한 독점 기술입니다. 각 아키텍처는 특정 버전의 CUDA 툴킷을 지원하며, 개발자가 CUDA 애플리케이션을 구축하고 실행하는 데 필요한 라이브러리와 도구를 제공합니다.

## ONNX

ONNX(Open Neural Network Exchange)는 머신 러닝 모델을 표현하기 위해 설계된 개방형 포맷입니다. 확장 가능한 계산 그래프 모델의 정의와 내장 연산자 및 표준 데이터 유형의 정의를 제공합니다. ONNX는 개발자가 다양한 ML 프레임워크 간에 모델을 이동할 수 있게 하여 상호 운용성을 가능하게 하고 AI 애플리케이션을 더 쉽게 만들고 배포할 수 있게 합니다.

Phi3 mini는 서버 플랫폼, Windows, Linux 및 Mac 데스크톱, 모바일 CPU를 포함한 다양한 장치에서 CPU 및 GPU로 ONNX Runtime과 함께 실행할 수 있습니다. 우리가 추가한 최적화된 구성은 다음과 같습니다:

- int4 DML을 위한 ONNX 모델: AWQ를 통해 int4로 양자화
- fp16 CUDA를 위한 ONNX 모델
- int4 CUDA를 위한 ONNX 모델: RTN을 통해 int4로 양자화
- int4 CPU 및 모바일을 위한 ONNX 모델: RTN을 통해 int4로 양자화

## Llama.cpp

Llama.cpp는 C++로 작성된 오픈 소스 소프트웨어 라이브러리로, Llama를 포함한 다양한 대형 언어 모델(LLM)에서 추론을 수행합니다. ggml 라이브러리(범용 텐서 라이브러리)와 함께 개발된 llama.cpp는 원래의 Python 구현보다 더 빠른 추론과 낮은 메모리 사용량을 제공하는 것을 목표로 합니다. 하드웨어 최적화, 양자화, 간단한 API 및 예제를 제공합니다. 효율적인 LLM 추론에 관심이 있다면 Phi3가 Llama.cpp를 실행할 수 있기 때문에 탐구할 가치가 있습니다.

## GGUF

GGUF(Generic Graph Update Format)는 머신 러닝 모델을 표현하고 업데이트하는 데 사용되는 포맷입니다. 특히 4-8비트 양자화로 CPU에서 효과적으로 실행할 수 있는 소형 언어 모델(SLM)에 유용합니다. GGUF는 신속한 프로토타이핑과 엣지 장치 또는 CI/CD 파이프라인과 같은 배치 작업에서 모델을 실행하는 데 유리합니다.

면책 조항: 이 번역은 AI 모델에 의해 원문에서 번역되었으며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주십시오.