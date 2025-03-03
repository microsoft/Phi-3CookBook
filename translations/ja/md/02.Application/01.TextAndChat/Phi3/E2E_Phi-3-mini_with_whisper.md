# インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概要

インタラクティブ Phi 3 Mini 4K Instruct Chatbot は、Microsoft Phi 3 Mini 4K instruct デモを使用して、テキストまたは音声入力でやり取りできるツールです。このチャットボットは、翻訳、天気情報の取得、一般的な情報収集など、さまざまなタスクに利用できます。

### 始め方

このチャットボットを使用するには、以下の手順に従ってください：

1. 新しい [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開きます。
2. ノートブックのメインウィンドウに、テキスト入力ボックスと「Send」ボタンがあるチャットボックスインターフェイスが表示されます。
3. テキストベースのチャットボットを使用するには、テキスト入力ボックスにメッセージを入力し、「Send」ボタンをクリックします。チャットボットは、ノートブック内で直接再生可能な音声ファイルで応答します。

**注**: このツールを使用するには、GPUおよび音声認識と翻訳に使用される Microsoft Phi-3 と OpenAI Whisper モデルへのアクセスが必要です。

### GPU要件

このデモを実行するには、12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct** デモをGPUで実行する際のメモリ要件は、入力データのサイズ（音声またはテキスト）、使用言語、モデルの速度、およびGPUの利用可能なメモリなど、いくつかの要因によって異なります。

一般的に、WhisperモデルはGPU上で動作するように設計されています。Whisperモデルを実行するための推奨最小GPUメモリは8GBですが、必要に応じてより大きなメモリ量にも対応できます。

大量のデータや高頻度のリクエストをモデルで処理する場合、より多くのGPUメモリが必要になる可能性があり、パフォーマンスの問題が発生する可能性があります。異なる構成で使用例をテストし、メモリ使用量を監視して、特定のニーズに最適な設定を判断することをお勧めします。

## Whisperを使用したインタラクティブ Phi 3 Mini 4K Instruct Chatbot のE2Eサンプル

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) というタイトルのJupyterノートブックでは、Microsoft Phi 3 Mini 4K instruct デモを使用して、音声またはテキスト入力からテキストを生成する方法を示しています。このノートブックでは、いくつかの関数が定義されています：

1. `tts_file_name(text)`: 入力テキストに基づいて、生成された音声ファイルを保存するためのファイル名を生成します。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Edge TTS API を使用して、入力テキストのチャンクリストから音声ファイルを生成します。入力パラメータは、チャンクリスト、音声速度、音声名、および生成された音声ファイルを保存するための出力パスです。
1. `talk(input_text)`: Edge TTS API を使用して音声ファイルを生成し、それを /content/audio ディレクトリ内のランダムなファイル名で保存します。入力パラメータは、音声に変換する入力テキストです。
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instruct デモを使用して、メッセージ入力から音声ファイルを生成し、それをチャット履歴に追加します。
1. `run_audio_prompt(audio, chat_history)`: Whisper モデル API を使用して音声ファイルをテキストに変換し、それを `run_text_prompt()` 関数に渡します。
1. コードは、ユーザーが Phi 3 Mini 4K instruct デモとやり取りできる Gradio アプリを起動します。ユーザーはメッセージを入力するか音声ファイルをアップロードでき、出力はアプリ内にテキストメッセージとして表示されます。

## トラブルシューティング

Cuda GPU ドライバーのインストール

1. Linux アプリケーションを最新の状態に保つ

    ```bash
    sudo apt update
    ```

1. Cuda ドライバーをインストール

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cuda ドライバーの場所を登録

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU メモリサイズを確認（12GBのGPUメモリが必要）

    ```bash
    nvidia-smi
    ```

1. キャッシュを空にする：PyTorchを使用している場合は、torch.cuda.empty_cache() を呼び出して、未使用のキャッシュメモリを解放し、他のGPUアプリケーションで使用できるようにします。

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda の確認

    ```bash
    nvcc --version
    ```

1. 以下の手順を実行して Hugging Face トークンを作成します。

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) に移動します。
    - **New token** を選択します。
    - 使用するプロジェクトの**Name**を入力します。
    - **Type**を**Write**に設定します。

> **注**
>
> 以下のエラーが発生した場合：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決するには、ターミナル内で次のコマンドを入力してください。
>
> ```bash
> sudo ldconfig
> ```

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文（原本）が信頼できる正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じた誤解や解釈の誤りについて、当方は一切の責任を負いません。