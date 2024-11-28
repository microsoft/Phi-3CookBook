# Phi-3 로컬에서 시작하기

이 가이드는 Ollama를 사용하여 Phi-3 모델을 실행하기 위해 로컬 환경을 설정하는 방법을 안내합니다. GitHub Codespaces, VS Code Dev Containers 또는 로컬 환경을 사용하여 모델을 실행할 수 있습니다.

## 환경 설정

### GitHub Codespaces

GitHub Codespaces를 사용하여 이 템플릿을 가상으로 실행할 수 있습니다. 버튼을 클릭하면 브라우저에서 웹 기반의 VS Code 인스턴스가 열립니다:

1. 템플릿을 엽니다 (몇 분이 소요될 수 있습니다):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 터미널 창을 엽니다

### VS Code Dev Containers

⚠️ 이 옵션은 Docker Desktop에 최소 16 GB의 RAM이 할당된 경우에만 작동합니다. 16 GB 미만의 RAM을 사용하는 경우, [GitHub Codespaces 옵션](../../../../md/01.Introduce)이나 [로컬 환경 설정](../../../../md/01.Introduce)을 시도해 보세요.

관련 옵션으로는 VS Code Dev Containers가 있으며, 이는 [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 사용하여 로컬 VS Code에서 프로젝트를 엽니다:

1. Docker Desktop을 시작합니다 (설치되지 않은 경우 설치)
2. 프로젝트를 엽니다:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 프로젝트 파일이 표시되면 (몇 분이 소요될 수 있습니다) 터미널 창을 엽니다.
4. [배포 단계](../../../../md/01.Introduce)를 계속 진행합니다.

### 로컬 환경

1. 다음 도구가 설치되어 있는지 확인합니다:

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## 모델 테스트

1. Ollama에게 phi3:mini 모델을 다운로드하고 실행하도록 요청합니다:

    ```shell
    ollama run phi3:mini
    ```

    모델을 다운로드하는 데 몇 분이 소요됩니다.

2. 출력에서 "success"를 확인한 후, 프롬프트에서 해당 모델에 메시지를 보낼 수 있습니다.

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 몇 초 후, 모델로부터 응답 스트림을 볼 수 있습니다.

4. 언어 모델과 함께 사용되는 다양한 기술에 대해 배우려면 Python 노트북 [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb)를 열고 각 셀을 실행합니다. 'phi3:mini' 외의 모델을 사용한 경우, 파일 상단의 `MODEL_NAME` in the first cell.

5. To have a conversation with the phi3:mini model from Python, open the Python file [chat.py](../../../../code/01.Introduce/chat.py) and run it. You can change the `MODEL_NAME`을 필요에 따라 변경할 수 있으며, 시스템 메시지를 수정하거나 몇 가지 샘플 예제를 추가할 수도 있습니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.