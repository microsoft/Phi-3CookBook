# **iOS에서 Phi-3 추론하기**

Phi-3-mini는 Microsoft의 새로운 모델 시리즈로, 엣지 디바이스와 IoT 디바이스에서 대형 언어 모델(LLM)을 배포할 수 있게 합니다. Phi-3-mini는 iOS, Android, 그리고 엣지 디바이스 배포를 지원하여 BYOD 환경에서도 생성형 AI를 사용할 수 있습니다. 아래 예시는 iOS에서 Phi-3-mini를 배포하는 방법을 보여줍니다.

## **1. 준비 사항**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 이상)
- **d.** Python 3.10+ 설치 (Conda 권장)
- **e.** Python 라이브러리 `python-flatbuffers` 설치
- **f.** CMake 설치

### Semantic Kernel과 추론

Semantic Kernel은 Azure OpenAI 서비스, OpenAI 모델, 그리고 로컬 모델과 호환되는 애플리케이션을 만들 수 있는 프레임워크입니다. Semantic Kernel을 통해 로컬 서비스를 사용하면 자체 호스팅된 Phi-3-mini 모델 서버와 쉽게 통합할 수 있습니다.

### Ollama 또는 LlamaEdge로 양자화된 모델 호출하기

많은 사용자는 로컬에서 모델을 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com)와 [LlamaEdge](https://llamaedge.com)를 사용하면 다양한 양자화된 모델을 호출할 수 있습니다:

#### **Ollama**

`ollama run phi3` 명령어를 직접 실행하거나 오프라인으로 설정할 수 있습니다. `gguf` 파일 경로를 포함한 Modelfile을 생성하세요. Phi-3-mini 양자화 모델을 실행하는 샘플 코드:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

클라우드와 엣지 디바이스에서 동시에 `gguf`를 사용하려면, LlamaEdge가 좋은 선택입니다.

## **2. iOS용 ONNX Runtime 컴파일하기**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **유의사항**

- **a.** 컴파일하기 전에 Xcode가 제대로 구성되어 있고, 터미널에서 활성 개발자 디렉터리로 설정되어 있는지 확인하세요:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime은 다양한 플랫폼에 맞게 컴파일해야 합니다. iOS의 경우 `arm64` 또는 `x86_64`로 컴파일할 수 있습니다.

- **c.** 최신 iOS SDK를 사용하여 컴파일하는 것이 권장되지만, 이전 SDK와의 호환성을 위해 더 오래된 버전을 사용할 수도 있습니다.

## **3. iOS용 ONNX Runtime을 사용한 생성형 AI 컴파일하기**

> **Note:** ONNX Runtime을 사용한 생성형 AI는 프리뷰 상태이므로, 변경 사항이 있을 수 있습니다.

```bash

git clone https://github.com/microsoft/onnxruntime-genai
 
cd onnxruntime-genai
 
mkdir ort
 
cd ort
 
mkdir include
 
mkdir lib
 
cd ../
 
cp ../onnxruntime/include/onnxruntime/core/session/onnxruntime_c_api.h ort/include
 
cp ../onnxruntime/build_ios/Release/Release-iphoneos/libonnxruntime*.dylib* ort/lib
 
export OPENCV_SKIP_XCODEBUILD_FORCE_TRYCOMPILE_DEBUG=1
 
python3 build.py --parallel --build_dir ./build_ios --ios --ios_sysroot iphoneos --ios_arch arm64 --ios_deployment_target 17.5 --cmake_generator Xcode --cmake_extra_defines CMAKE_XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED=NO

```

## **4. Xcode에서 앱 애플리케이션 생성하기**

ONNX Runtime C++ API를 사용한 생성형 AI와의 호환성 때문에, Objective-C를 앱 개발 방법으로 선택했습니다. 물론 Swift 브리징을 통해 관련 호출을 완료할 수도 있습니다.

![xcode](../../../../translated_images/xcode.2817f1d089dc7d09ba6a41361db7052567d63f714062e2e4325b0e0895ccb4c4.ko.png)

## **5. ONNX 양자화 INT4 모델을 앱 애플리케이션 프로젝트에 복사하기**

ONNX 형식의 INT4 양자화 모델을 가져와야 하며, 먼저 다운로드해야 합니다.

![hf](../../../../translated_images/hf.dd843c3e95f3b462a3d5f06dbbb17c1f1a33b87688c1cda4d990084ef71a4eed.ko.png)

다운로드한 후, 프로젝트의 Resources 디렉토리에 추가해야 합니다.

![model](../../../../translated_images/model.2b8e95a590e70374b2294b16f8ae18c9110239a550e64dc034d6bc16d37e0106.ko.png)

## **6. ViewControllers에 C++ API 추가하기**

> **유의사항:**

- **a.** 프로젝트에 해당하는 C++ 헤더 파일을 추가하세요.

  ![Header File](../../../../translated_images/head.7eeb79e1de8f375590e7a5c54fcc8278d265fee3135ebce9c8e241e08d823f7c.ko.png)

- **b.** Xcode에 `onnxruntime-genai` 동적 라이브러리를 포함시키세요.

  ![Library](../../../../translated_images/lib.9388329df08543518d094d14c8ca0c8e6f0ce264ee68630a8c5c3d783355b6d1.ko.png)

- **c.** C 샘플 코드를 사용하여 테스트하세요. 추가 기능을 원하면 ChatUI 같은 기능을 추가할 수도 있습니다.

- **d.** 프로젝트에서 C++을 사용해야 하므로, `ViewController.m`을 `ViewController.mm`으로 이름을 변경하여 Objective-C++ 지원을 활성화하세요.

```objc

    NSString *llmPath = [[NSBundle mainBundle] resourcePath];
    char const *modelPath = llmPath.cString;

    auto model =  OgaModel::Create(modelPath);

    auto tokenizer = OgaTokenizer::Create(*model);

    const char* prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>";

    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt, *sequences);

    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 100);
    params->SetInputSequences(*sequences);

    auto output_sequences = model->Generate(*params);
    const auto output_sequence_length = output_sequences->SequenceCount(0);
    const auto* output_sequence_data = output_sequences->SequenceData(0);
    auto out_string = tokenizer->Decode(output_sequence_data, output_sequence_length);
    
    auto tmp = out_string;

```

## **7. 애플리케이션 실행하기**

설정이 완료되면, 애플리케이션을 실행하여 Phi-3-mini 모델 추론 결과를 확인할 수 있습니다.

![Running Result](../../../../translated_images/result.a2debbd16a6697a8cbd23dadff703358ea87eee7d68f0643b83707a578ca73e8.ko.jpg)

더 많은 샘플 코드와 자세한 지침은 [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios)를 방문하세요.

면책 조항: 이 번역은 AI 모델에 의해 원문에서 번역된 것으로 완벽하지 않을 수 있습니다.
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.