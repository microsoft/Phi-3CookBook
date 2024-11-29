# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 개요

Interactive Phi 3 Mini 4K Instruct Chatbot은 Microsoft Phi 3 Mini 4K instruct 데모와 텍스트 또는 오디오 입력을 통해 상호작용할 수 있는 도구입니다. 이 챗봇은 번역, 날씨 업데이트, 일반 정보 수집 등 다양한 작업에 사용할 수 있습니다.

### 시작하기

이 챗봇을 사용하려면 다음 지침을 따르세요:

1. 새로운 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 파일을 엽니다.
2. 노트북의 메인 창에서 텍스트 입력 상자와 "Send" 버튼이 있는 채팅 인터페이스를 볼 수 있습니다.
3. 텍스트 기반 챗봇을 사용하려면 텍스트 입력 상자에 메시지를 입력하고 "Send" 버튼을 클릭하세요. 챗봇은 노트북 내에서 직접 재생할 수 있는 오디오 파일로 응답할 것입니다.

**참고**: 이 도구는 GPU와 Microsoft Phi-3 및 OpenAI Whisper 모델에 대한 접근이 필요하며, 이는 음성 인식 및 번역에 사용됩니다.

### GPU 요구 사항

이 데모를 실행하려면 12GB의 GPU 메모리가 필요합니다.

**Microsoft-Phi-3-Mini-4K instruct** 데모를 GPU에서 실행하기 위한 메모리 요구 사항은 입력 데이터(오디오 또는 텍스트)의 크기, 번역에 사용되는 언어, 모델의 속도 및 GPU의 가용 메모리와 같은 여러 요인에 따라 달라집니다.

일반적으로 Whisper 모델은 GPU에서 실행되도록 설계되었습니다. Whisper 모델을 실행하기 위한 최소 권장 GPU 메모리는 8GB이지만, 필요에 따라 더 큰 메모리도 처리할 수 있습니다.

모델에서 대량의 데이터나 많은 요청을 실행하면 더 많은 GPU 메모리가 필요하거나 성능 문제가 발생할 수 있습니다. 다양한 구성으로 사용 사례를 테스트하고 메모리 사용량을 모니터링하여 특정 요구 사항에 맞는 최적의 설정을 결정하는 것이 좋습니다.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)라는 제목의 주피터 노트북은 Microsoft Phi 3 Mini 4K instruct 데모를 사용하여 오디오 또는 텍스트 입력에서 텍스트를 생성하는 방법을 보여줍니다. 이 노트북은 여러 함수를 정의합니다:

1. `tts_file_name(text)`: 생성된 오디오 파일을 저장하기 위해 입력 텍스트를 기반으로 파일 이름을 생성하는 함수입니다.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS API를 사용하여 입력 텍스트 조각 목록에서 오디오 파일을 생성하는 함수입니다. 입력 매개변수는 조각 목록, 음성 속도, 음성 이름 및 생성된 오디오 파일을 저장할 출력 경로입니다.
1. `talk(input_text)`: Edge TTS API를 사용하여 오디오 파일을 생성하고 /content/audio 디렉토리에 무작위 파일 이름으로 저장하는 함수입니다. 입력 매개변수는 음성으로 변환할 입력 텍스트입니다.
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instruct 데모를 사용하여 메시지 입력에서 오디오 파일을 생성하고 채팅 기록에 추가하는 함수입니다.
1. `run_audio_prompt(audio, chat_history)`: Whisper 모델 API를 사용하여 오디오 파일을 텍스트로 변환하고 이를 `run_text_prompt()` 함수로 전달하는 함수입니다.
1. 코드는 사용자가 메시지를 입력하거나 오디오 파일을 업로드하여 Phi 3 Mini 4K instruct 데모와 상호작용할 수 있는 Gradio 앱을 실행합니다. 출력은 앱 내에서 텍스트 메시지로 표시됩니다.

## 문제 해결

Cuda GPU 드라이버 설치

1. Linux 애플리케이션이 최신 상태인지 확인하세요

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

1. Nvidia GPU 메모리 크기 확인 (12GB의 GPU 메모리 필요)

    ```bash
    nvidia-smi
    ```

1. 캐시 비우기: PyTorch를 사용하는 경우 torch.cuda.empty_cache()를 호출하여 사용되지 않는 모든 캐시된 메모리를 해제하여 다른 GPU 애플리케이션에서 사용할 수 있도록 할 수 있습니다.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda 확인

    ```bash
    nvcc --version
    ```

1. Hugging Face 토큰을 생성하려면 다음 작업을 수행하세요.

    - [Hugging Face Token Settings 페이지](https://huggingface.co/settings/tokens)로 이동합니다.
    - **New token**을 선택합니다.
    - 사용할 프로젝트 **Name**을 입력합니다.
    - **Type**을 **Write**로 선택합니다.

> **Note**
>
> 다음 오류가 발생하면:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 이를 해결하려면 터미널에서 다음 명령을 입력하세요.
>
> ```bash
> sudo ldconfig
> ```

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서는 해당 언어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.