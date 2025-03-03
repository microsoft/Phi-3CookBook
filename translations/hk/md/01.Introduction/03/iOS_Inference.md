# **在 iOS 上使用 Phi-3 進行推理**

Phi-3-mini 是 Microsoft 推出的一系列新模型，可以在邊緣設備和物聯網設備上運行大型語言模型 (LLMs)。Phi-3-mini 支援 iOS、Android 和邊緣設備部署，讓生成式 AI 可以在 BYOD 環境中運行。以下示例展示如何在 iOS 上部署 Phi-3-mini。

## **1. 準備工作**

- **a.** macOS 14 或以上
- **b.** Xcode 15 或以上
- **c.** iOS SDK 17.x (iPhone 14 A16 或更高版本)
- **d.** 安裝 Python 3.10 或以上版本 (推薦使用 Conda)
- **e.** 安裝 Python 庫：`python-flatbuffers`
- **f.** 安裝 CMake

### Semantic Kernel 與推理

Semantic Kernel 是一個應用框架，允許你建立與 Azure OpenAI Service、OpenAI 模型，甚至是本地模型相容的應用。透過 Semantic Kernel 訪問本地服務，能輕鬆整合你的自託管 Phi-3-mini 模型伺服器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶更喜歡使用量化模型在本地運行模型。[Ollama](https://ollama.com) 和 [LlamaEdge](https://llamaedge.com) 提供了調用不同量化模型的方式：

#### **Ollama**

你可以直接運行 `ollama run phi3` 或離線配置它。建立一個 Modelfile，並指定你的 `gguf` 文件路徑。以下是運行 Phi-3-mini 量化模型的示例代碼：

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

如果你希望在雲端和邊緣設備上同時使用 `gguf`，LlamaEdge 是一個不錯的選擇。

## **2. 為 iOS 編譯 ONNX Runtime**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **注意事項**

- **a.** 在編譯之前，確保 Xcode 已正確配置，並在終端中將其設置為活躍的開發者目錄：

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime 需要為不同平台編譯。對於 iOS，你可以為 `arm64` or `x86_64` 編譯。

- **c.** 建議使用最新的 iOS SDK 進行編譯。但如果需要與舊版 SDK 相容，也可以使用舊版本。

## **3. 為 iOS 編譯 ONNX Runtime 的生成式 AI**

> **注意：** 因為 ONNX Runtime 的生成式 AI 功能目前處於預覽階段，請注意可能會有變更。

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

## **4. 在 Xcode 中建立 App 應用**

我選擇使用 Objective-C 作為 App 的開發方式，因為在使用 ONNX Runtime 的 C++ API 時，Objective-C 的相容性更好。當然，你也可以通過 Swift bridging 完成相關調用。

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.hk.png)

## **5. 將 ONNX 量化的 INT4 模型複製到 App 項目中**

我們需要匯入 ONNX 格式的 INT4 量化模型，這需要先下載。

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.hk.png)

下載後，需要將其添加到 Xcode 項目的 Resources 目錄中。

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.hk.png)

## **6. 在 ViewControllers 中添加 C++ API**

> **注意：**

- **a.** 將相應的 C++ 標頭文件添加到項目中。

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.hk.png)

- **b.** 包含 `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.hk.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` 以啟用 Objective-C++ 支援。

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

## **7. 運行應用程式**

完成設置後，你可以運行應用程式，查看 Phi-3-mini 模型推理的結果。

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.hk.jpg)

更多範例代碼和詳細指導，請參考 [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios)。

**免責聲明**:  
此文件是使用機器翻譯服務進行翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業的人工作翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。