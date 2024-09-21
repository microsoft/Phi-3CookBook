# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 개요

인터랙티브 Phi 3 Mini 4K Instruct Chatbot은 사용자가 Microsoft Phi 3 Mini 4K instruct 데모와 텍스트 또는 오디오 입력을 통해 상호작용할 수 있게 해주는 도구입니다. 이 챗봇은 번역, 날씨 업데이트, 일반 정보 수집 등 다양한 작업에 사용할 수 있습니다.

### 시작하기

이 챗봇을 사용하려면 다음 지침을 따르세요:

1. 새 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)를 엽니다.
2. 노트북의 메인 창에서 텍스트 입력 상자와 "Send" 버튼이 있는 채팅 인터페이스를 볼 수 있습니다.
3. 텍스트 기반 챗봇을 사용하려면 텍스트 입력 상자에 메시지를 입력하고 "Send" 버튼을 클릭하세요. 챗봇은 노트북 내에서 직접 재생할 수 있는 오디오 파일로 응답할 것입니다.

**참고**: 이 도구는 GPU와 음성 인식 및 번역을 위해 Microsoft Phi-3 및 OpenAI Whisper 모델에 대한 접근이 필요합니다.

### GPU 요구사항

이 데모를 실행하려면 12GB의 GPU 메모리가 필요합니다.

**Microsoft-Phi-3-Mini-4K instruct** 데모를 GPU에서 실행하는 데 필요한 메모리 요구사항은 입력 데이터의 크기(오디오 또는 텍스트), 번역에 사용되는 언어, 모델의 속도, GPU의 사용 가능한 메모리 등 여러 요인에 따라 달라집니다.

일반적으로 Whisper 모델은 GPU에서 실행되도록 설계되었습니다. Whisper 모델을 실행하는 데 권장되는 최소 GPU 메모리는 8GB이지만, 필요에 따라 더 큰 메모리도 처리할 수 있습니다.

많은 양의 데이터 또는 높은 볼륨의 요청을 모델에서 실행하는 경우 더 많은 GPU 메모리가 필요할 수 있으며 성능 문제가 발생할 수 있습니다. 다양한 구성으로 사용 사례를 테스트하고 메모리 사용량을 모니터링하여 특정 요구에 맞는 최적의 설정을 결정하는 것이 좋습니다.

## Whisper를 사용한 인터랙티브 Phi 3 Mini 4K Instruct Chatbot의 E2E 샘플

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)이라는 제목의 주피터 노트북은 Microsoft Phi 3 Mini 4K instruct Demo를 사용하여 오디오 또는 텍스트 입력으로부터 텍스트를 생성하는 방법을 보여줍니다. 이 노트북은 여러 함수를 정의합니다:

1. `tts_file_name(text)`: 입력 텍스트를 기반으로 생성된 오디오 파일을 저장할 파일 이름을 생성합니다.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 입력 텍스트의 청크 목록에서 오디오 파일을 생성하기 위해 Edge TTS API를 사용합니다. 입력 매개변수는 청크 목록, 음성 속도, 음성 이름 및 생성된 오디오 파일을 저장할 출력 경로입니다.
1. `talk(input_text)`: Edge TTS API를 사용하여 오디오 파일을 생성하고 /content/audio 디렉토리에 무작위 파일 이름으로 저장합니다. 입력 매개변수는 음성으로 변환할 입력 텍스트입니다.
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instruct 데모를 사용하여 메시지 입력에서 오디오 파일을 생성하고 이를 채팅 기록에 추가합니다.
1. `run_audio_prompt(audio, chat_history)`: Whisper 모델 API를 사용하여 오디오 파일을 텍스트로 변환하고 이를 `run_text_prompt()` 함수에 전달합니다.
1. 코드는 사용자가 메시지를 입력하거나 오디오 파일을 업로드하여 Phi 3 Mini 4K instruct 데모와 상호작용할 수 있는 Gradio 앱을 실행합니다. 출력은 앱 내에서 텍스트 메시지로 표시됩니다.

## 문제 해결

Cuda GPU 드라이버 설치

1. Linux 애플리케이션이 최신 상태인지 확인합니다.

    ```bash
    sudo apt update
    ```

1. Cuda 드라이버 설치

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cuda 드라이버 위치 등록

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU 메모리 크기 확인 (필요한 GPU 메모리 12GB)

    ```bash
    nvidia-smi
    ```

1. 캐시 비우기: PyTorch를 사용하는 경우, torch.cuda.empty_cache()를 호출하여 다른 GPU 애플리케이션이 사용할 수 있도록 모든 사용되지 않는 캐시된 메모리를 해제할 수 있습니다.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda 확인

    ```bash
    nvcc --version
    ```

1. Hugging Face 토큰을 생성하려면 다음 작업을 수행합니다.

    - [Hugging Face Token Settings 페이지](https://huggingface.co/settings/tokens)로 이동합니다.
    - **New token**을 선택합니다.
    - 사용하려는 프로젝트 **Name**을 입력합니다.
    - **Type**을 **Write**로 선택합니다.

> **Note**
>
> 다음과 같은 오류가 발생할 경우:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 이를 해결하려면 터미널에 다음 명령을 입력하세요.
>
> ```bash
> sudo ldconfig
> ```

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정을 해주시기 바랍니다.