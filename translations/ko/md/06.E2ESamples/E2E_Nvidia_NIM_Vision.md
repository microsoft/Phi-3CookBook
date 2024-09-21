### 예제 시나리오

이미지(`demo.png`)가 있고, 이 이미지를 처리하여 새로운 버전(`phi-3-vision.jpg`)으로 저장하는 Python 코드를 생성하고 싶다고 상상해보세요.

위 코드는 다음과 같은 방식으로 이 과정을 자동화합니다:

1. 환경 및 필요한 설정을 구성합니다.
2. 모델에게 필요한 Python 코드를 생성하도록 지시하는 프롬프트를 만듭니다.
3. 프롬프트를 모델에 보내고 생성된 코드를 수집합니다.
4. 생성된 코드를 추출하고 실행합니다.
5. 원본 이미지와 처리된 이미지를 표시합니다.

이 접근 방식은 AI의 힘을 활용하여 이미지 처리 작업을 자동화함으로써 목표를 더 쉽게 그리고 빠르게 달성할 수 있게 합니다.

[샘플 코드 솔루션](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

이제 전체 코드를 단계별로 설명해 보겠습니다:

1. **필요한 패키지 설치**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    이 명령어는 `langchain_nvidia_ai_endpoints` 패키지를 최신 버전으로 설치합니다.

2. **필요한 모듈 임포트**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    이 임포트는 NVIDIA AI 엔드포인트와 상호 작용하고, 비밀번호를 안전하게 처리하며, 운영 체제와 상호 작용하고, 데이터를 base64 형식으로 인코딩/디코딩하는 데 필요한 모듈을 가져옵니다.

3. **API 키 설정**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    이 코드는 `NVIDIA_API_KEY` 환경 변수가 설정되어 있는지 확인합니다. 설정되지 않은 경우 사용자에게 API 키를 안전하게 입력하도록 요청합니다.

4. **모델 및 이미지 경로 정의**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    이는 사용할 모델을 설정하고, 지정된 모델로 `ChatNVIDIA` 인스턴스를 생성하며, 이미지 파일의 경로를 정의합니다.

5. **텍스트 프롬프트 생성**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    이는 모델에게 이미지를 처리하는 Python 코드를 생성하도록 지시하는 텍스트 프롬프트를 정의합니다.

6. **이미지를 Base64로 인코딩**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'''
    ```
    이 코드는 이미지 파일을 읽고, 이를 base64로 인코딩하며, 인코딩된 데이터로 HTML 이미지 태그를 생성합니다.

7. **텍스트와 이미지를 프롬프트에 결합**:
    ```python
    prompt = f"{text} {image}"
    ```
    이는 텍스트 프롬프트와 HTML 이미지 태그를 하나의 문자열로 결합합니다.

8. **ChatNVIDIA를 사용하여 코드 생성**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    이 코드는 프롬프트를 `ChatNVIDIA` 모델에 보내고 생성된 코드를 청크 단위로 수집하여, 각 청크를 출력하고 `code` 문자열에 추가합니다.

9. **생성된 콘텐츠에서 Python 코드 추출**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    이는 마크다운 형식을 제거하여 생성된 콘텐츠에서 실제 Python 코드를 추출합니다.

10. **생성된 코드 실행**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    이는 추출된 Python 코드를 서브프로세스로 실행하고 그 출력을 캡처합니다.

11. **이미지 표시**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    이 코드는 `IPython.display` 모듈을 사용하여 이미지를 표시합니다.

면책 조항: 이 번역은 AI 모델에 의해 원문에서 번역된 것으로 완벽하지 않을 수 있습니다.
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.