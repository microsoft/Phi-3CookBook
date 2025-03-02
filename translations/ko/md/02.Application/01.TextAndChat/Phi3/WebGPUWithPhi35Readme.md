# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU와 RAG 패턴 데모

Phi-3.5 Onnx Hosted 모델을 사용하는 RAG 패턴은 검색 기반 생성(Retrieval-Augmented Generation) 접근 방식을 활용하여, Phi-3.5 모델의 성능과 ONNX 호스팅의 효율성을 결합합니다. 이 패턴은 도메인별 작업에 모델을 미세 조정하는 데 유용하며, 품질, 비용 효율성, 긴 문맥 이해를 모두 제공하는 솔루션입니다. Azure AI의 모델 제품군의 일부로, 다양한 산업의 요구를 충족하기 위해 쉽게 검색, 시도, 활용할 수 있는 다양한 모델을 제공합니다.

## WebGPU란? 
WebGPU는 웹 브라우저에서 기기의 그래픽 처리 장치(GPU)에 직접적으로 효율적으로 접근할 수 있도록 설계된 현대적인 웹 그래픽 API입니다. 이는 WebGL의 후속 기술로 여러 주요 개선점을 제공합니다:

1. **최신 GPU와의 호환성**: WebGPU는 최신 GPU 아키텍처와 원활히 작동하도록 설계되었으며, Vulkan, Metal, Direct3D 12와 같은 시스템 API를 활용합니다.
2. **성능 향상**: 그래픽 렌더링뿐만 아니라 기계 학습 작업에도 적합한 일반 목적 GPU 연산과 더 빠른 작업을 지원합니다.
3. **고급 기능**: WebGPU는 더 복잡하고 동적인 그래픽 및 계산 작업을 가능하게 하는 고급 GPU 기능에 대한 접근을 제공합니다.
4. **JavaScript 작업량 감소**: 더 많은 작업을 GPU로 오프로드하여 JavaScript의 작업량을 크게 줄이고, 성능 향상과 더 부드러운 사용자 경험을 제공합니다.

현재 WebGPU는 Google Chrome과 같은 브라우저에서 지원되며, 다른 플랫폼으로 지원을 확대하기 위한 작업이 진행 중입니다.

### 03.WebGPU
필요 환경:

**지원 브라우저:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU 활성화:

- Chrome/Microsoft Edge에서 

`chrome://flags/#enable-unsafe-webgpu` 플래그를 활성화합니다.

#### 브라우저 열기:
Google Chrome 또는 Microsoft Edge를 실행합니다.

#### 플래그 페이지 접속:
주소창에 `chrome://flags`를 입력하고 Enter를 누릅니다.

#### 플래그 검색:
페이지 상단의 검색창에 'enable-unsafe-webgpu'를 입력합니다.

#### 플래그 활성화:
검색 결과 목록에서 #enable-unsafe-webgpu 플래그를 찾습니다.

드롭다운 메뉴를 클릭하고 'Enabled'를 선택합니다.

#### 브라우저 재시작:

플래그를 활성화한 후, 변경 사항을 적용하려면 브라우저를 재시작해야 합니다. 페이지 하단에 나타나는 'Relaunch' 버튼을 클릭합니다.

- Linux의 경우, `--enable-features=Vulkan` 명령어로 브라우저를 실행합니다.
- Safari 18 (macOS 15)은 기본적으로 WebGPU가 활성화되어 있습니다.
- Firefox Nightly에서는 주소창에 about:config를 입력하고 `set dom.webgpu.enabled to true`를 설정합니다.

### Microsoft Edge에서 GPU 설정

Windows에서 Microsoft Edge에 고성능 GPU를 설정하는 방법은 다음과 같습니다:

- **설정 열기:** 시작 메뉴를 클릭하고 '설정'을 선택합니다.
- **시스템 설정:** '시스템'으로 이동한 후 '디스플레이'를 선택합니다.
- **그래픽 설정:** 아래로 스크롤하여 '그래픽 설정'을 클릭합니다.
- **앱 선택:** “선호 사항을 설정할 앱 선택”에서 '데스크톱 앱'을 선택한 후 '찾아보기'를 클릭합니다.
- **Edge 선택:** Edge 설치 폴더(보통 `C:\Program Files (x86)\Microsoft\Edge\Application`)로 이동하여 `msedge.exe`를 선택합니다.
- **선호 사항 설정:** '옵션'을 클릭하고 '고성능'을 선택한 후 '저장'을 클릭합니다.
이 설정은 Microsoft Edge가 고성능 GPU를 사용하도록 보장합니다.
- 변경 사항을 적용하려면 **컴퓨터를 재시작**하세요.

### 샘플: [이 링크를 클릭하세요](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.