# **onnxruntimeのGenerative AI拡張機能を使ったPhiファミリーの量子化**

## **onnxruntimeのGenerative AI拡張機能とは**

この拡張機能は、ONNX Runtime（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）を使用して生成AIを実行するためのものです。ONNXモデルで生成AIループを提供し、ONNX Runtimeによる推論、ロジット処理、探索とサンプリング、KVキャッシュ管理を含みます。開発者は、高レベルの`generate()`メソッドを呼び出すか、モデルの各イテレーションをループ内で1トークンずつ生成しながら実行し、必要に応じてループ内で生成パラメータを更新することができます。グリーディー/ビームサーチやTopP、TopKサンプリングによるトークン列の生成、繰り返しペナルティのような組み込みのロジット処理がサポートされています。また、カスタムスコアリングを簡単に追加することも可能です。

アプリケーションレベルでは、onnxruntimeのGenerative AI拡張機能を使用して、C++/C#/Pythonでアプリケーションを構築できます。モデルレベルでは、微調整されたモデルを統合したり、関連する量子的なデプロイ作業を行うことができます。

## **onnxruntimeのGenerative AI拡張機能を使用したPhi-3.5の量子化**

### **サポートされているモデル**

onnxruntimeのGenerative AI拡張機能は、Microsoft Phi、Google Gemma、Mistral、Meta LLaMAの量子化変換をサポートしています。

### **onnxruntimeのGenerative AI拡張機能におけるモデルビルダー**

モデルビルダーは、ONNX Runtimeの`generate()` APIで動作する最適化および量子化されたONNXモデルの作成を大幅に加速します。

モデルビルダーを通じて、モデルをINT4、INT8、FP16、FP32に量子化し、CPU、CUDA、DirectML、Mobileなどのさまざまなハードウェアアクセラレーション方法を組み合わせることができます。

モデルビルダーを使用するには、以下をインストールする必要があります。

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

インストール後、ターミナルからモデルビルダースクリプトを実行して、モデル形式と量子化変換を行うことができます。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

関連するパラメータを理解する

1. **model_name** Hugging Face上のモデル名（例：`microsoft/Phi-3.5-mini-instruct`、`microsoft/Phi-3.5-vision-instruct`など）。または、モデルを保存しているパス。

2. **path_to_output_folder** 量子化変換の保存先パス。

3. **execution_provider** CPU、CUDA、DirectMLなど、異なるハードウェアアクセラレーションのサポート。

4. **cache_dir_to_save_hf_files** Hugging Faceからモデルをダウンロードしてローカルにキャッシュするディレクトリ。

***注意：***

## **モデルビルダーを使ったPhi-3.5の量子化方法**

モデルビルダーは現在、Phi-3.5 InstructとPhi-3.5-VisionのONNXモデル量子化をサポートしています。

### **Phi-3.5-Instruct**

**INT 4量子化のCPUアクセラレーション変換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**INT 4量子化のCUDAアクセラレーション変換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ターミナルで環境を設定

```bash

mkdir models

cd models 

```

2. `microsoft/Phi-3.5-vision-instruct`をmodelsフォルダにダウンロード  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 以下のファイルをPhi-3.5-vision-instructフォルダにダウンロードしてください：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 以下のファイルをmodelsフォルダにダウンロードしてください：  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ターミナルで以下を実行：

    FP32でONNXサポートに変換

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. モデルビルダーは現在、Phi-3.5-InstructとPhi-3.5-Visionの変換をサポートしていますが、Phi-3.5-MoEはサポートしていません。

2. ONNXの量子化モデルを使用するには、onnxruntimeのGenerative AI拡張機能SDKを通じて利用できます。

3. より責任あるAIを考慮するために、モデル量子化変換後は、より効果的な結果テストを行うことを推奨します。

4. CPU INT4モデルを量子化することで、エッジデバイスへのデプロイが可能となり、より優れたアプリケーションシナリオが実現します。そのため、Phi-3.5-InstructのINT4量子化を完了しています。

## **リソース**

1. onnxruntimeのGenerative AI拡張機能についてさらに学ぶ  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntimeのGenerative AI拡張機能 GitHubリポジトリ  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語で作成された原文を公式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用によって生じる誤解や解釈の相違について、当社は一切の責任を負いません。