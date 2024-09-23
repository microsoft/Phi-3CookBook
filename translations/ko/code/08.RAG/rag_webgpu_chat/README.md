Phi-3-mini WebGPU RAG 챗봇

## WebGPU와 RAG 패턴 데모
Phi-3 Onnx Hosted 모델을 활용한 RAG 패턴은 Retrieval-Augmented Generation 접근 방식을 활용하여 Phi-3 모델의 성능과 ONNX 호스팅을 결합해 효율적인 AI 배포를 제공합니다. 이 패턴은 도메인 특화 작업을 위한 모델을 미세 조정하는 데 유용하며, 품질, 비용 효율성, 긴 문맥 이해를 모두 갖춘 솔루션을 제공합니다. Azure AI의 일환으로 다양한 모델을 쉽게 찾고, 시도하고, 사용할 수 있으며, 다양한 산업의 맞춤형 요구를 충족시킵니다. Phi-3 모델, 포함하여 Phi-3-mini, Phi-3-small, Phi-3-medium은 Azure AI Model Catalog에서 제공되며, 자체 관리 또는 HuggingFace 및 ONNX와 같은 플랫폼을 통해 미세 조정 및 배포가 가능합니다. 이는 접근 가능하고 효율적인 AI 솔루션에 대한 Microsoft의 의지를 보여줍니다.

## WebGPU란 무엇인가
WebGPU는 웹 브라우저에서 장치의 그래픽 처리 장치(GPU)에 효율적으로 접근할 수 있도록 설계된 현대적인 웹 그래픽 API입니다. 이는 WebGL의 후속으로 여러 주요 개선 사항을 제공합니다:

1. **현대 GPU와의 호환성**: WebGPU는 Vulkan, Metal, Direct3D 12와 같은 시스템 API를 활용하여 현대적인 GPU 아키텍처와 원활하게 작동하도록 설계되었습니다.
2. **향상된 성능**: WebGPU는 일반적인 GPU 계산과 더 빠른 작업을 지원하여 그래픽 렌더링과 기계 학습 작업 모두에 적합합니다.
3. **고급 기능**: WebGPU는 더 복잡하고 동적인 그래픽 및 계산 작업을 가능하게 하는 고급 GPU 기능에 접근할 수 있습니다.
4. **JavaScript 작업 부하 감소**: 더 많은 작업을 GPU에 오프로드하여 WebGPU는 JavaScript의 작업 부하를 크게 줄여 성능을 향상시키고 부드러운 경험을 제공합니다.

현재 Google Chrome과 같은 브라우저에서 지원되며, 다른 플랫폼으로의 지원 확장을 위한 작업이 진행 중입니다.

### 03.WebGPU
필수 환경:

**지원되는 브라우저:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU 활성화:

- Chrome/Microsoft Edge에서

`chrome://flags/#enable-unsafe-webgpu` 플래그를 활성화하세요.

#### 브라우저 열기:
Google Chrome 또는 Microsoft Edge를 실행하세요.

#### 플래그 페이지 접근:
주소 표시줄에 `chrome://flags`를 입력하고 Enter 키를 누르세요.

#### 플래그 검색:
페이지 상단의 검색 상자에 'enable-unsafe-webgpu'를 입력하세요.

#### 플래그 활성화:
결과 목록에서 #enable-unsafe-webgpu 플래그를 찾으세요.

옆에 있는 드롭다운 메뉴를 클릭하고 Enabled를 선택하세요.

#### 브라우저 재시작:

플래그를 활성화한 후에는 변경 사항이 적용되도록 브라우저를 재시작해야 합니다. 페이지 하단에 나타나는 Relaunch 버튼을 클릭하세요.

- Linux의 경우, `--enable-features=Vulkan`을 사용하여 브라우저를 실행하세요.
- Safari 18 (macOS 15)은 기본적으로 WebGPU가 활성화되어 있습니다.
- Firefox Nightly에서는 주소 표시줄에 about:config를 입력하고 `dom.webgpu.enabled`를 true로 설정하세요.

### Microsoft Edge용 GPU 설정 

Windows에서 Microsoft Edge에 고성능 GPU를 설정하는 단계는 다음과 같습니다:

- **설정 열기:** 시작 메뉴를 클릭하고 설정을 선택하세요.
- **시스템 설정:** 시스템으로 이동한 다음 디스플레이로 이동하세요.
- **그래픽 설정:** 아래로 스크롤하여 그래픽 설정을 클릭하세요.
- **앱 선택:** "선호 설정을 지정할 앱 선택"에서 데스크탑 앱을 선택한 다음 찾아보기를 클릭하세요.
- **Edge 선택:** Edge 설치 폴더(보통 `C:\Program Files (x86)\Microsoft\Edge\Application`)로 이동하여 `msedge.exe`를 선택하세요.
- **선호 설정 지정:** 옵션을 클릭하고 고성능을 선택한 다음 저장을 클릭하세요.
이렇게 하면 Microsoft Edge가 더 나은 성능을 위해 고성능 GPU를 사용하도록 설정됩니다.
- **재시작** 설정이 적용되도록 컴퓨터를 재시작하세요.

### Codespace 열기:
GitHub에서 저장소로 이동하세요.
Code 버튼을 클릭하고 Codespaces로 열기를 선택하세요.

아직 Codespace가 없다면, New codespace를 클릭하여 새로 만들 수 있습니다.

**참고** Codespace에 Node 환경 설치
GitHub Codespace에서 npm 데모를 실행하는 것은 프로젝트를 테스트하고 개발하는 훌륭한 방법입니다. 다음은 시작하는 데 도움이 되는 단계별 가이드입니다:

### 환경 설정:
Codespace가 열리면 Node.js와 npm이 설치되어 있는지 확인하세요. 다음 명령어를 실행하여 확인할 수 있습니다:
```
node -v
```
```
npm -v
```

설치되어 있지 않다면, 다음 명령어를 사용하여 설치할 수 있습니다:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 프로젝트 디렉토리로 이동:
터미널을 사용하여 npm 프로젝트가 위치한 디렉토리로 이동하세요:
```
cd path/to/your/project
```

### 종속성 설치:
다음 명령어를 실행하여 package.json 파일에 나열된 모든 필요한 종속성을 설치하세요:

```
npm install
```

### 데모 실행:
종속성이 설치되면 데모 스크립트를 실행할 수 있습니다. 이는 보통 package.json의 scripts 섹션에 지정되어 있습니다. 예를 들어, 데모 스크립트 이름이 start라면 다음 명령어를 실행할 수 있습니다:

```
npm run build
```
```
npm run dev
```

### 데모 접근:
데모가 웹 서버와 관련이 있다면, Codespaces는 접근할 수 있는 URL을 제공합니다. 알림을 확인하거나 Ports 탭에서 URL을 찾으세요.

**참고:** 모델은 브라우저에 캐시되어야 하므로 로드하는 데 시간이 걸릴 수 있습니다.

### RAG 데모
RAG 솔루션을 완료하려면 `intro_rag.md` 마크다운 파일을 업로드하세요. Codespaces를 사용하는 경우 `01.InferencePhi3/docs/`에 위치한 파일을 다운로드할 수 있습니다.

### 파일 선택:
“Choose File” 버튼을 클릭하여 업로드할 문서를 선택하세요.

### 문서 업로드:
파일을 선택한 후, “Upload” 버튼을 클릭하여 문서를 RAG (Retrieval-Augmented Generation)로 로드하세요.

### 채팅 시작:
문서가 업로드되면, 문서 내용을 기반으로 RAG를 사용하여 채팅 세션을 시작할 수 있습니다.

