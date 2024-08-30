# **LM StudioでPhi-3を使用する**

[LM Studio](https://lmstudio.ai)は、ローカルデスクトップアプリケーションでSLMおよびLLMを呼び出すためのアプリケーションです。ユーザーは、さまざまなモデルを簡単に使用でき、NVIDIA/AMD GPU/Apple Siliconを使用した加速計算をサポートしています。LM Studioを使用すると、ユーザーはHugging Faceに基づいたさまざまなオープンソースLLMおよびSLMをダウンロード、インストール、および実行して、コードなしでローカルでモデルのパフォーマンスをテストできます。

## **1. インストール**

![LMStudio](../../../../imgs/02/LMStudio/LMStudio.png)

LM StudioのWebサイト[https://lmstudio.ai/](https://lmstudio.ai/)から、Windows、Linux、macOSにインストールすることができます。

## **2. LM StudioでPhi-3をダウンロードする**

LM Studioは、量子化されたgguf形式のオープンソースモデルを呼び出します。LM Studio Search UIが提供するプラットフォームから直接ダウンロードするか、自分でダウンロードして関連ディレクトリに指定して呼び出すことができます。

***LM Studio SearchでPhi3を検索し、Phi-3 ggufモデルをダウンロードします***

![LMStudioSearch](../../../../imgs/02/LMStudio/LMStudio_Search.png)

***LM Studioを通じてダウンロードしたモデルを管理します***

![LMStudioLocal](../../../../imgs/02/LMStudio/LMStudio_Local.png)

## **3. LM StudioでPhi-3とチャットする**

LM Studio ChatでPhi-3を選択し、チャットテンプレート（Preset - Phi3）を設定して、Phi-3とのローカルチャットを開始します。

![LMStudioChat](../../../../imgs/02/LMStudio/LMStudio_Chat.png)

***注意***:

a. LM StudioコントロールパネルのAdvance Configurationでパラメータを設定できます。

b. Phi-3には特定のチャットテンプレート要件があるため、PresetでPhi-3を選択する必要があります。

c. GPUの使用など、さまざまなパラメータを設定することもできます。

## **4. LM StudioからPhi-3 APIを呼び出す**

LM Studioはローカルサービスの迅速なデプロイをサポートしており、コードなしでモデルサービスを構築できます。

![LMStudioServer](../../../../imgs/02/LMStudio/LMStudio_Server.png)

これはPostmanの結果です。

![LMStudioPostman](../../../../imgs/02/LMStudio/LMStudio_Postman.png)
