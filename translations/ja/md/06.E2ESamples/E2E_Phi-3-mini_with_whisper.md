# インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概要

インタラクティブ Phi 3 Mini 4K Instruct Chatbotは、Microsoft Phi 3 Mini 4K instruct デモをテキストまたは音声入力で操作できるツールです。このチャットボットは翻訳、天気情報の更新、一般的な情報収集など、さまざまなタスクに使用できます。

### はじめに

このチャットボットを使用するには、以下の手順に従ってください:

1. 新しい [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) を開きます。
2. ノートブックのメインウィンドウには、テキスト入力ボックスと「送信」ボタンがあるチャットボックスインターフェースが表示されます。
3. テキストベースのチャットボットを使用するには、テキスト入力ボックスにメッセージを入力し、「送信」ボタンをクリックします。チャットボットはノートブック内で直接再生できる音声ファイルで応答します。

**Note**: このツールを使用するには、GPUとMicrosoft Phi-3およびOpenAI Whisperモデルへのアクセスが必要です。これらは音声認識と翻訳に使用されます。

### GPU要件

このデモを実行するには、12GBのGPUメモリが必要です。

**Microsoft-Phi-3-Mini-4K instruct** デモをGPUで実行するためのメモリ要件は、入力データのサイズ（音声またはテキスト）、使用する言語、モデルの速度、GPUの利用可能メモリなど、いくつかの要因に依存します。

一般的に、WhisperモデルはGPU上で実行するように設計されています。Whisperモデルを実行するための推奨最小GPUメモリ量は8GBですが、必要に応じてより多くのメモリを処理できます。

大量のデータや高ボリュームのリクエストをモデルで実行する場合、より多くのGPUメモリが必要になる可能性があり、パフォーマンスの問題が発生する可能性があります。異なる構成で使用ケースをテストし、メモリ使用量を監視して、特定のニーズに最適な設定を確認することをお勧めします。

## インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper のE2Eサンプル

[インタラクティブ Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) というタイトルのjupyterノートブックは、Microsoft Phi 3 Mini 4K instruct デモを使用して音声またはテキスト入力からテキストを生成する方法を示しています。このノートブックには、いくつかの関数が定義されています:

1. `tts_file_name(text)`: この関数は、生成された音声ファイルを保存するためのファイル名を入力テキストに基づいて生成します。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: この関数は、Edge TTS APIを使用して、入力テキストのチャンクリストから音声ファイルを生成します。入力パラメータは、チャンクのリスト、音声速度、声の名前、および生成された音声ファイルを保存する出力パスです。
1. `talk(input_text)`: この関数は、Edge TTS APIを使用して音声ファイルを生成し、それを/content/audioディレクトリ内のランダムなファイル名に保存します。入力パラメータは、音声に変換する入力テキストです。
1. `run_text_prompt(message, chat_history)`: この関数は、Microsoft Phi 3 Mini 4K instruct デモを使用してメッセージ入力から音声ファイルを生成し、それをチャット履歴に追加します。
1. `run_audio_prompt(audio, chat_history)`: この関数は、WhisperモデルAPIを使用して音声ファイルをテキストに変換し、それを`run_text_prompt()`関数に渡します。
1. コードは、ユーザーがメッセージを入力したり、音声ファイルをアップロードしたりしてPhi 3 Mini 4K instruct デモと対話できるGradioアプリを起動します。出力はアプリ内のテキストメッセージとして表示されます。

## トラブルシューティング

Cuda GPUドライバのインストール

1. Linuxアプリケーションを最新の状態に保つ

    ```bash
    sudo apt update
    ```

1. Cudaドライバをインストール

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. cudaドライバの場所を登録

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPUメモリサイズを確認 (12GBのGPUメモリが必要)

    ```bash
    nvidia-smi
    ```

1. キャッシュを空にする: PyTorchを使用している場合、torch.cuda.empty_cache()を呼び出して、未使用のキャッシュメモリをすべて解放し、他のGPUアプリケーションで使用できるようにします。

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cudaを確認

    ```bash
    nvcc --version
    ```

1. Hugging Faceトークンを作成するには、以下のタスクを実行します。

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens) に移動します。
    - **New token** を選択します。
    - 使用したいプロジェクトの **Name** を入力します。
    - **Type** を **Write** に選択します。

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

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を行ってください。