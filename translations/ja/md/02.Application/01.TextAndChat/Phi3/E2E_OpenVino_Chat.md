[OpenVino Chat サンプル](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

このコードはモデルをOpenVINO形式にエクスポートし、それを読み込んで、指定されたプロンプトに対する応答を生成します。

1. **モデルのエクスポート**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - このコマンドは、`optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` を使用します。

2. **必要なライブラリのインポート**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - これらの行は、`transformers` library and the `optimum.intel.openvino` モジュールからクラスをインポートし、モデルを読み込み、使用するために必要です。

3. **モデルディレクトリと設定の準備**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` は、OpenVINOモデルが低遅延を優先し、1つの推論ストリームを使用し、キャッシュディレクトリを使用しないように設定する辞書です。

4. **モデルの読み込み**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - この行は、指定されたディレクトリからモデルを設定済みの構成を使用して読み込みます。また、必要に応じてリモートコード実行も許可します。

5. **トークナイザーの読み込み**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - この行は、テキストをモデルが理解できるトークンに変換する役割を持つトークナイザーを読み込みます。

6. **トークナイザー引数の設定**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - この辞書は、トークン化された出力に特別なトークンを追加しないよう指定しています。

7. **プロンプトの定義**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - この文字列は、ユーザーがAIアシスタントに自己紹介を求める会話プロンプトを設定します。

8. **プロンプトのトークン化**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - この行は、プロンプトをモデルが処理できるトークンに変換し、その結果をPyTorchテンソルとして返します。

9. **応答の生成**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - この行は、入力トークンに基づいてモデルが応答を生成するために使用され、最大1024個の新しいトークンを生成します。

10. **応答のデコード**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - この行は、生成されたトークンを人間が読める文字列に変換し、特別なトークンをスキップして最初の結果を取得します。

**免責事項**:  
本書類は、AIによる機械翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（元の言語で記載された文書）が信頼できる唯一の情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いかねます。