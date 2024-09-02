# **iOSでPhi-3を推論する**

Phi-3-miniは、Microsoftが提供する新しいモデルシリーズで、エッジデバイスやIoTデバイスに大型言語モデル（LLM）を展開することができます。Phi-3-miniは、iOS、Android、およびエッジデバイスの展開に対応しており、BYOD環境で生成AIを展開することができます。以下の例では、iOSをベースにしたPhi-3-miniの展開方法を説明します。

## **1. 準備**

a. macOS 14+

b. Xcode 15+

c. iOS SDK 17.x (iPhone 14 A16またはそれ以上)

d. Python 3.10+のインストール（Condaを推奨）

e. Pythonライブラリのインストール - python-flatbuffers

f. CMakeのインストール

### セマンティックカーネルと推論:
セマンティックカーネルは、Azure OpenAIサービス、OpenAIモデル、さらにはローカルモデルと互換性のあるアプリケーションを作成できるアプリケーションフレームワークです。セマンティックカーネルを通じてローカルサービスにアクセスすることで、自分で構築したPhi-3-miniモデルサーバーに簡単に接続できます。

### OllamaまたはLlamaEdgeを使用して量子化モデルを呼び出す:
多くのユーザーは、量子化モデルを使用してローカルでモデルを実行することを好みます。[Ollama](https://ollama.com)および[LlamaEdge](https://llamaedge.com)は、個々のユーザーが異なる量子化モデルを呼び出すことを可能にします:

**Ollama**
Ollamaを直接実行するか、オフラインで構成します。Modelfileを作成し、ggufファイルへのパスを指定します。Phi-3-mini量子化モデルを実行するためのサンプルコード:

```

FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096

```
**LlamaEdge**
ggufをクラウドおよびエッジデバイスで同時に使用したい場合、LlamaEdgeが選択肢となります。


## **2. iOS用にONNX Runtimeをコンパイルする**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

***注意***

  a. コンパイル前に、Xcodeが正しく構成されていることを確認し、ターミナルで設定します


```bash

sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer

```

  b. ONNX Runtimeは異なるプラットフォームに基づいてコンパイルする必要があります。iOSの場合、arm64 / x86_64に基づいてコンパイルできます

  c. 最新のiOS SDKを使用してコンパイルすることをお勧めします。もちろん、過去のSDKと互換性を持たせるためにバージョンを下げることもできます。


## **3. iOS用に生成AIをONNX Runtimeでコンパイルする**


 ***注意:*** 生成AIとONNX Runtimeはプレビュー中であるため、変更に注意してください。


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


## **4. Xcodeでアプリケーションを作成する**

アプリケーション開発方法としてObjective-Cを選択しました。これは、生成AIとONNX Runtime C++ APIを使用する場合、Objective-Cがより互換性があるためです。もちろん、Swiftブリッジングを通じて関連する呼び出しを完了することもできます。


![xcode](../../../../imgs/03/iOS/xcode.png)


## **5. ONNX量子化INT4モデルをアプリケーションプロジェクトにコピーする**

ONNX形式のINT4量子化モデルをインポートする必要があります。まずモデルをダウンロードする必要があります

![hf](../../../../imgs/03/iOS/hf.png)

ダウンロード後、XcodeのプロジェクトのResourcesディレクトリに追加する必要があります。

![model](../../../../imgs/03/iOS/model.png)


 ## **6. ViewControllersにC++ APIを追加する**

***注意***:

  a. プロジェクトに対応するC++ヘッダーファイルを追加します


  ![head](../../../../imgs/03/iOS/head.png)

  b. Xcodeにonnxruntime-gen ai dylibを追加します


  ![lib](../../../../imgs/03/iOS/lib.png)

  c. このサンプルでは、Cサンプルのコードを直接使用してテストします。もちろん、moreto run（例：ChatUI）を追加して実行することもできます

  d. C++を呼び出す必要があるため、ViewController.mをViewController.mmに変更してください

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


## **7. 実行結果**

![result](../../../../imgs/03/iOS/result.jpg)

***サンプルコード：*** https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios
