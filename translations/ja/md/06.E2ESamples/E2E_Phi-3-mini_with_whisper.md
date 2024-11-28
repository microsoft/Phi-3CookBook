# インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概要

インタラクティブ Phi 3 Mini 4K Instruct Chatbotは、Microsoft Phi 3 Mini 4K instructデモとテキストや音声入力で対話できるツールです。このチャットボットは、翻訳、天気情報の更新、一般的な情報収集など、さまざまなタスクに使用できます。

### 始めに

このチャットボットを使用するには、以下の手順に従ってください:

1. 新しい [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開きます。
2. ノートブックのメインウィンドウには、テキスト入力ボックスと「送信」ボタンがあるチャットボックスインターフェースが表示されます。
3. テキストベースのチャットボットを使用するには、テキスト入力ボックスにメッセージを入力して「送信」ボタンをクリックします。チャットボットは、ノートブック内で直接再生できる音声ファイルで応答します。

**Note**: このツールを使用するには、GPUとMicrosoft Phi-3およびOpenAI Whisperモデルへのアクセスが必要です。これらは音声認識と翻訳に使用されます。

### GPUの要件

このデモを実行するには、12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct**デモをGPUで実行するためのメモリ要件は、入力データのサイズ（音声またはテキスト）、翻訳に使用する言語、モデルの速度、およびGPUの利用可能なメモリなど、いくつかの要因に依存します。

一般に、WhisperモデルはGPUでの実行を前提としています。Whisperモデルを実行するための推奨最小GPUメモリは8GBですが、必要に応じてより大きなメモリを処理できます。

大量のデータや高頻度のリクエストをモデルに対して実行する場合、より多くのGPUメモリが必要になる可能性があり、またはパフォーマンスの問題が発生する可能性があることに注意してください。異なる構成で使用ケースをテストし、メモリ使用量を監視して、特定のニーズに最適な設定を決定することをお勧めします。

## インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper のE2Eサンプル

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)というタイトルのjupyterノートブックは、Microsoft Phi 3 Mini 4K instructデモを使用して、音声またはテキスト入力からテキストを生成する方法を示しています。このノートブックには、いくつかの関数が定義されています:

1. `tts_file_name(text)`: 入力テキストに基づいて生成された音声ファイルを保存するためのファイル名を生成する関数です。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 入力テキストのチャンクリストから音声ファイルを生成するためにEdge TTS APIを使用する関数です。入力パラメータは、チャンクリスト、スピーチレート、音声名、および生成された音声ファイルを保存するための出力パスです。
1. `talk(input_text)`: Edge TTS APIを使用して音声ファイルを生成し、/content/audioディレクトリにランダムなファイル名で保存する関数です。入力パラメータは、音声に変換するための入力テキストです。
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instructデモを使用してメッセージ入力から音声ファイルを生成し、チャット履歴に追加する関数です。
1. `run_audio_prompt(audio, chat_history)`: WhisperモデルAPIを使用して音声ファイルをテキストに変換し、`run_text_prompt()`関数に渡す関数です。
1. このコードは、ユーザーがメッセージを入力するか音声ファイルをアップロードしてPhi 3 Mini 4K instructデモと対話できるGradioアプリを起動します。出力はアプリ内のテキストメッセージとして表示されます。

## トラブルシューティング

Cuda GPUドライバーのインストール

1. Linuxアプリケーションが最新であることを確認します

    ```bash
    sudo apt update
    ```

1. Cudaドライバーをインストールします

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cudaドライバーの場所を登録します

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPUメモリサイズを確認します（12GBのGPUメモリが必要）

    ```bash
    nvidia-smi
    ```

1. キャッシュを空にする: PyTorchを使用している場合は、torch.cuda.empty_cache()を呼び出して、他のGPUアプリケーションが使用できるように未使用のキャッシュメモリをすべて解放できます

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cudaを確認します

    ```bash
    nvcc --version
    ```

1. 以下のタスクを実行してHugging Faceトークンを作成します。

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens)に移動します。
    - **New token**を選択します。
    - 使用したいプロジェクトの**Name**を入力します。
    - **Type**を**Write**に設定します。

> **Note**
>
> 次のエラーが発生した場合:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> これを解決するには、ターミナル内で次のコマンドを入力します。
>
> ```bash
> sudo ldconfig
> ```

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期していますが、自動翻訳にはエラーや不正確さが含まれる場合がありますのでご注意ください。元の言語での原文が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。