# **在 iOS 中推論 Phi-3**

Phi-3-mini 是 Microsoft 推出的新系列模型，能夠在邊緣設備和 IoT 設備上部署大型語言模型（LLMs）。Phi-3-mini 可用於 iOS、Android 和邊緣設備的部署，允許在 BYOD 中部署生成式 AI。以下範例基於 iOS 部署 Phi-3-mini

## **1. 準備**

a. macOS 14+

b. Xcode 15+

c. iOS SDK 17.x (iPhone 14 A16 或更高)

d. 安裝 Python 3.10+ (推薦使用 Conda)

e. 安裝 Python 函式庫 - python-flatbuffers

f. 安裝 CMake

### 語義核心和推論:

Semantic Kernel 是一個應用程式框架，允許你建立與 Azure OpenAI Service、OpenAI 模型，甚至本地模型相容的應用程式。通過 Semantic Kernel 訪問本地服務，可以輕鬆連接到你自建的 Phi-3-mini 模型伺服器。

### 呼叫量化模型與 Ollama 或 LlamaEdge:

許多使用者偏好使用量化模型來在本地執行模型。[Ollama](https://ollama.com) 和 [LlamaEdge](https://llamaedge.com) 允許個別使用者呼叫不同的量化模型：

**Ollama**
你可以直接執行 ollama run phi3 或離線配置。使用 gguf 檔案的路徑建立一個 Modelfile。執行 Phi-3-mini 量化模型的範例程式碼：

```
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

**LlamaEdge**
如果你想在雲端和邊緣設備上同時使用 gguf，LlamaEdge 可以是你的選擇。

## **2. 編譯 ONNX Runtime for iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

***注意***

a. 在編譯之前，您必須確保 Xcode 已正確配置並在終端機上進行設定

```bash

sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer

```

b. ONNX Runtime 需要基於不同平台進行編譯。對於 iOS，你可以基於 arm64 / x86_64 進行編譯

c. 建議直接使用最新的 iOS SDK 進行編譯。當然，你也可以降低版本以相容過去的 SDK。

## **3. 使用 ONNX Runtime 為 iOS 編譯生成式 AI**

***注意:*** 因為使用 ONNX Runtime 的生成式 AI 正在預覽中，請注意變更。

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

## **4. 建立一個 App 應用程式在 Xcode**

我選擇 Objective-C 作為 App 開發方法，因為使用 Generative AI 與 ONNX Runtime C++ API 時，Objective-C 更具相容性。當然，你也可以通過 Swift bridging 完成相關呼叫。

![xcode](../../../../imgs/03/iOS/xcode.png)

## **5. 複製 ONNX 量化 INT4 模型到 App 應用程式專案**

我們需要匯入 ONNX 格式的 INT4 量化模型，這需要先下載

![hf](../../../../imgs/03/iOS/hf.png)

下載後，你需要將它添加到 Xcode 專案的 Resources 目錄中。

![model](../../../../imgs/03/iOS/model.png)

## **6. 在 ViewControllers 中添加 C++ API**

***注意***:

a. 將相應的 C++ 標頭檔案新增到專案中

![head](../../../../imgs/03/iOS/head.png)

b. 在 Xcode 中添加 onnxruntime-gen ai 動態庫

![函式庫](../../../../imgs/03/iOS/lib.png)

c. 直接使用 C 範例上的程式碼來測試這些範例。你也可以直接添加更多來執行（例如 ChatUI)

d. 因為你需要呼叫 C++，請將 ViewController.m 改為 ViewController.mm

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

## **7. 執行結果**

![result](../../../../imgs/03/iOS/result.jpg)

***範例程式碼：*** https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios

