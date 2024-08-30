# **AI PCでPhi-3を推論する**

生成AIの進展とエッジデバイスのハードウェア能力の向上に伴い、ますます多くの生成AIモデルがユーザーの持ち込みデバイス（BYOD）に統合できるようになりました。AI PCはこれらのモデルの一つです。2024年から、Intel、AMD、QualcommはPCメーカーと協力して、ハードウェアの変更を通じてローカル生成AIモデルの展開を促進するAI PCを導入しました。このディスカッションでは、Intel AI PCに焦点を当て、Intel AI PCでPhi-3を展開する方法を探ります。

### **NPUとは何か**

NPU（Neural Processing Unit）は、神経ネットワークの操作やAIタスクを加速するために特別に設計された専用プロセッサまたは大規模SoC上の処理ユニットです。一般的なCPUやGPUとは異なり、NPUはデータ駆動型の並列計算に最適化されており、ビデオや画像などの大量のマルチメディアデータを処理し、神経ネットワークのデータを処理するのに非常に効率的です。特に、音声認識、ビデオ通話中の背景ぼかし、写真やビデオ編集プロセス（オブジェクト検出など）などのAI関連タスクに優れています。

## **NPUとGPUの違い** 
多くのAIおよび機械学習のワークロードはGPU上で実行されますが、GPUとNPUの間には重要な違いがあります。
GPUは並列計算能力で知られていますが、すべてのGPUがグラフィックス処理以外のタスクに同じように効率的であるわけではありません。一方、NPUは神経ネットワーク操作に関わる複雑な計算のために特別に設計されており、AIタスクに非常に効果的です。

要約すると、NPUはAI計算を加速する数学の天才であり、新しいAI PC時代において重要な役割を果たしています！

***この例は、Intelの最新のIntel Core Ultra Processorに基づいています***

## **1. NPUを使用してPhi-3モデルを実行する**

Intel® NPUデバイスは、Intel® Core™ Ultra世代のCPU（以前はMeteor Lakeとして知られていた）から始まるIntelクライアントCPUに統合されたAI推論アクセラレータです。これにより、人工神経ネットワークタスクのエネルギー効率の高い実行が可能になります。

![Latency](../../../../imgs/03/AIPC/aipcphitokenlatency.png)

![Latency770](../../../../imgs/03/AIPC/aipcphitokenlatency770.png)

**Intel NPUアクセラレーションライブラリ**

Intel NPUアクセラレーションライブラリ [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) は、Intel Neural Processing Unit (NPU) のパワーを活用して、対応するハードウェア上で高速計算を実行することで、アプリケーションの効率を向上させるために設計されたPythonライブラリです。

Intel® Core™ Ultraプロセッサを搭載したAI PCで動作するPhi-3-miniの例。

![DemoPhiIntelAIPC](../../../../imgs/03/AIPC/aipcphi3-mini.gif)

pipを使用してPythonライブラリをインストールする

```bash

   pip install intel-npu-acceleration-library

```

***注意*** プロジェクトはまだ開発中ですが、参照モデルはすでに非常に完成しています。

### **Intel NPUアクセラレーションライブラリを使用してPhi-3を実行する**

Intel NPUアクセラレーションを使用する場合、このライブラリは従来のエンコードプロセスに影響を与えません。このライブラリを使用して元のPhi-3モデルを量子化するだけで済みます。例えば、FP16、INT8、INT4などです。

```python

from transformers import AutoTokenizer, pipeline,TextStreamer
import intel_npu_acceleration_library as npu_lib
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

model = npu_lib.NPUModelForCausalLM.from_pretrained(
                                    model_id,
                                    torch_dtype="auto",
                                    dtype=npu_lib.int4,
                                    trust_remote_code=True
                                )

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)

```
量子化が成功した後、続行してNPUを呼び出してPhi-3モデルを実行します。

```python

generation_args = {
            "max_new_tokens": 1024,
            "return_full_text": False,
            "temperature": 0.3,
            "do_sample": False,
            "streamer": text_streamer,
        }

pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)


```

コードを実行する際、タスクマネージャーを通じてNPUの実行状況を確認できます。

![NPU](../../../../imgs/03/AIPC/aipc_NPU.png)

***サンプル*** : [AIPC_NPU_DEMO.ipynb](../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. DirectML + ONNX Runtimeを使用してPhi-3モデルを実行する**

### **DirectMLとは何か**

[DirectML](https://github.com/microsoft/DirectML) は、機械学習のための高性能でハードウェアアクセラレートされたDirectX 12ライブラリです。DirectMLは、AMD、Intel、NVIDIA、QualcommなどのベンダーからのすべてのDirectX 12対応GPUを含む、広範な対応ハードウェアとドライバにわたる一般的な機械学習タスクのGPUアクセラレーションを提供します。

単独で使用する場合、DirectML APIは低レベルのDirectX 12ライブラリであり、フレームワーク、ゲーム、その他のリアルタイムアプリケーションなどの高性能で低遅延のアプリケーションに適しています。DirectMLのDirect3D 12とのシームレスな相互運用性、およびその低オーバーヘッドとハードウェア全体の適合性により、高性能が求められ、ハードウェア全体での結果の信頼性と予測可能性が重要な場合に、機械学習を加速するための理想的な選択肢となります。

***注意*** : 最新のDirectMLはNPUをサポートしています (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectMLとCUDAの機能と性能の比較:

**DirectML** は、Microsoftによって開発された機械学習ライブラリです。これは、デスクトップ、ラップトップ、エッジデバイスなどのWindowsデバイス上の機械学習ワークロードを加速するように設計されています。
- DX12ベース: DirectMLはDirectX 12（DX12）上に構築されており、NVIDIAおよびAMDを含む幅広いハードウェアサポートを提供します。
- 広範なサポート: DX12を利用しているため、DirectMLはDX12をサポートする任意のGPUと連携できます。統合GPUも含まれます。
- 画像処理: DirectMLは、神経ネットワークを使用して画像やその他のデータを処理し、画像認識、物体検出などのタスクに適しています。
- 設定の簡単さ: DirectMLの設定は簡単で、GPUメーカーの特定のSDKやライブラリを必要としません。
- パフォーマンス: 一部のケースでは、DirectMLは優れたパフォーマンスを発揮し、特定のワークロードではCUDAよりも高速です。
- 制限: ただし、DirectMLは一部のケースでは遅くなることがあります。特にfloat16の大規模バッチサイズの場合です。

**CUDA** は、NVIDIAの並列計算プラットフォームおよびプログラミングモデルです。これにより、開発者はNVIDIA GPUのパワーを利用して、機械学習や科学シミュレーションなどの汎用計算を行うことができます。
- NVIDIA専用: CUDAはNVIDIA GPUと緊密に統合されており、特にそれらのために設計されています。
- 高度に最適化: CUDAは、特にNVIDIA GPUを使用する場合、GPUアクセラレーションタスクに対して優れたパフォーマンスを提供します。
- 広く使用されている: 多くの機械学習フレームワークやライブラリ（TensorFlowやPyTorchなど）がCUDAをサポートしています。
- カスタマイズ: 開発者は特定のタスクに対してCUDA設定を微調整でき、最適なパフォーマンスを実現できます。
- 制限: ただし、CUDAはNVIDIAハードウェアに依存しているため、異なるGPU間での広範な互換性を求める場合に制限が生じる可能性があります。

### DirectMLとCUDAの選択:
DirectMLとCUDAの選択は、特定の使用ケース、ハードウェアの可用性、および好みに依存します。
より広範な互換性と設定の簡単さを求める場合、DirectMLが良い選択肢かもしれません。ただし、NVIDIA GPUを持ち、高度に最適化されたパフォーマンスが必要な場合、CUDAは依然として強力な競争相手です。要約すると、DirectMLとCUDAの両方にはそれぞれの強みと弱みがあるため、決定を下す際には要件と利用可能なハードウェアを考慮してください。

### **ONNX Runtimeを使用した生成AI**

AIの時代において、AIモデルの移植性は非常に重要です。ONNX Runtimeを使用すると、トレーニングされたモデルを簡単に異なるデバイスにデプロイできます。開発者は推論フレームワークに注意を払う必要はなく、統一されたAPIを使用してモデル推論を完了できます。生成AIの時代において、ONNX Runtimeはコードの最適化も行っています（https://onnxruntime.ai/docs/genai/）。最適化されたONNX Runtimeを使用すると、量子化された生成AIモデルを異なる端末で推論できます。ONNX Runtimeを使用した生成AIでは、Python、C#、C / C++を通じてAIモデルAPIを推論できます。もちろん、iPhoneにデプロイする場合は、C++の生成AIとONNX Runtime APIを利用できます。

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***生成AIとONNX Runtimeライブラリをコンパイルする***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**ライブラリをインストールする**


```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

これは実行結果です

![DML](../../../../imgs/03/AIPC/aipc_DML.png)

***サンプル*** : [AIPC_DirectML_DEMO.ipynb](../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Intel OpenVinoを使用してPhi-3モデルを実行する**

### **OpenVINOとは何か**

[OpenVINO](https://github.com/openvinotoolkit/openvino) は、深層学習モデルの最適化とデプロイのためのオープンソースツールキットです。これは、TensorFlow、PyTorchなどの人気のあるフレームワークからの視覚、音声、および言語モデルの深層学習パフォーマンスを向上させます。OpenVINOを使用して始めましょう。OpenVINOは、CPUおよびGPUと組み合わせてPhi-3モデルを実行することもできます。

***注意***: 現在、OpenVINOはNPUをサポートしていません。

### **OpenVINOライブラリをインストールする**


```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **OpenVINOを使用してPhi-3を実行する**

NPUと同様に、OpenVINOは量子化モデルを実行することで生成AIモデルの呼び出しを完了します。まずPhi-3モデルを量子化し、optimum-cliを使用してコマンドラインでモデルの量子化を完了します。

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

変換された形式は次のようになります

![openvino_convert](../../../../imgs/03/AIPC/aipc_OpenVINO_convert.png)


OVModelForCausalLMを通じて、モデルパス（model_dir）、関連設定（ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}）、およびハードウェアアクセラレートデバイス（GPU.0）をロードします。

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

コードを実行する際、タスクマネージャーを通じてGPUの実行状況を確認できます。

![openvino_gpu](../../../../imgs/03/AIPC/aipc_OpenVINO_GPU.png)

***サンプル*** : [AIPC_OpenVino_Demo.ipynb](../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***注意*** : 上記の3つの方法にはそれぞれの利点がありますが、AI PC推論にはNPUアクセラレーションを使用することをお勧めします。
