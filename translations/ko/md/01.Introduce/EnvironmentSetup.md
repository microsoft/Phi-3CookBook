# 로컬 환경에서 Phi-3 시작하기

이 가이드는 Ollama를 사용하여 로컬 환경에서 Phi-3 모델을 실행하는 방법을 안내합니다. GitHub Codespaces, VS Code Dev Containers 또는 로컬 환경을 포함한 몇 가지 방법으로 모델을 실행할 수 있습니다.

## 환경 설정

### GitHub Codespaces

GitHub Codespaces를 사용하여 이 템플릿을 가상으로 실행할 수 있습니다. 버튼을 클릭하면 브라우저에서 웹 기반 VS Code 인스턴스가 열립니다:

1. 템플릿을 엽니다 (몇 분 정도 소요될 수 있습니다):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 터미널 창을 엽니다

### VS Code Dev Containers

⚠️ 이 옵션은 Docker Desktop이 최소 16 GB의 RAM을 할당받은 경우에만 작동합니다. 16 GB 미만의 RAM을 가지고 있다면 [GitHub Codespaces 옵션](../../../../md/01.Introduce)이나 [로컬 설정](../../../../md/01.Introduce)을 시도해 보세요.

관련 옵션으로는 VS Code Dev Containers가 있습니다. 이 옵션은 [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 사용하여 로컬 VS Code에서 프로젝트를 엽니다:

1. Docker Desktop을 시작합니다 (설치되지 않은 경우 설치)
2. 프로젝트를 엽니다:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. VS Code 창이 열리면 프로젝트 파일이 나타날 때까지 (몇 분 정도 소요될 수 있습니다) 기다린 후 터미널 창을 엽니다.
4. [배포 단계](../../../../md/01.Introduce)를 계속 진행합니다.

### 로컬 환경

1. 다음 도구들이 설치되어 있는지 확인합니다:

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## 모델 테스트

1. Ollama에게 phi3:mini 모델을 다운로드하고 실행하도록 요청합니다:

    ```shell
    ollama run phi3:mini
    ```

    모델을 다운로드하는 데 몇 분 정도 소요됩니다.

2. 출력에서 "success" 메시지를 확인한 후, 프롬프트에서 모델에 메시지를 보낼 수 있습니다.

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 몇 초 후에 모델로부터 응답 스트림을 볼 수 있습니다.

4. 언어 모델에서 사용되는 다양한 기술을 배우려면 Python 노트북 [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb)를 열고 각 셀을 실행해 보세요. 'phi3:mini' 이외의 모델을 사용한 경우, 첫 번째 셀에서 `MODEL_NAME`을 변경하세요.

5. Python에서 phi3:mini 모델과 대화하려면 Python 파일 [chat.py](../../../../code/01.Introduce/chat.py)를 열고 실행하세요. 파일 상단에서 `MODEL_NAME`을 필요에 따라 변경할 수 있으며, 시스템 메시지를 수정하거나 몇 가지 예시를 추가할 수도 있습니다.

