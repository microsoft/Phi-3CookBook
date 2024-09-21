[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

このコードは、モデルをOpenVINO形式にエクスポートし、それを読み込んで指定されたプロンプトに対する応答を生成します。

1. **モデルのエクスポート**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - このコマンドは、`optimum-cli`ツールを使用してモデルを効率的な推論のために最適化されたOpenVINO形式にエクスポートします。
   - エクスポートされるモデルは `"microsoft/Phi-3-mini-4k-instruct"` で、過去のコンテキストに基づいてテキストを生成するタスクに設定されています。
   - モデルの重みは4ビット整数（`int4`）に量子化され、モデルサイズの縮小と処理速度の向上が図られます。
   - `group-size`、`ratio`、`sym` などの他のパラメータは量子化プロセスを微調整するために使用されます。
   - エクスポートされたモデルは `./model/phi3-instruct/int4` ディレクトリに保存されます。

2. **必要なライブラリのインポート**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - これらの行は、モデルを読み込み使用するために必要な `transformers` ライブラリと `optimum.intel.openvino` モジュールからクラスをインポートします。

3. **モデルディレクトリと設定の準備**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` はモデルファイルが保存されている場所を指定します。
   - `ov_config` はOpenVINOモデルを低遅延優先、1つの推論ストリーム使用、キャッシュディレクトリ不使用に設定する辞書です。

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
   - この行は、指定されたディレクトリから設定を使用してモデルを読み込みます。また、必要に応じてリモートコードの実行を許可します。

5. **トークナイザーの読み込み**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - この行は、モデルが理解できるトークンにテキストを変換するトークナイザーを読み込みます。

6. **トークナイザーの引数設定**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - この辞書は、トークン化された出力に特別なトークンを追加しないことを指定します。

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
   - この行は、入力トークンに基づいてモデルが応答を生成し、最大1024の新しいトークンを生成します。

10. **応答のデコード**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - この行は、生成されたトークンを人間が読める文字列に変換し、特別なトークンをスキップして最初の結果を取得します。

