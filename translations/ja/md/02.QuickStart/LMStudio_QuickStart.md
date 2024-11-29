# **LM StudioでPhi-3を使用する**

[LM Studio](https://lmstudio.ai) は、ローカルデスクトップアプリケーションでSLMとLLMを呼び出すためのアプリケーションです。ユーザーは異なるモデルを簡単に使用でき、NVIDIA/AMD GPU/Apple Siliconを使用した高速計算をサポートします。LM Studioを通じて、ユーザーはHugging Faceに基づいたさまざまなオープンソースのLLMとSLMをダウンロード、インストール、実行して、コードを書かずにローカルでモデルの性能をテストできます。

## **1. インストール**

![LMStudio](../../../../translated_images/LMStudio.87422bdb03d330dc05137ba237dd0cb43f7964245b848a466ab1730de93bc4db.ja.png)

Windows、Linux、macOSにインストールするには、LM Studioのウェブサイト [https://lmstudio.ai/](https://lmstudio.ai/) から選択できます。

## **2. LM StudioでPhi-3をダウンロードする**

LM Studioは、量子化されたgguf形式のオープンソースモデルを呼び出します。LM Studio Search UIが提供するプラットフォームから直接ダウンロードするか、自分でダウンロードして関連ディレクトリに指定して呼び出すことができます。

***LM Studio SearchでPhi3を検索し、Phi-3 ggufモデルをダウンロードします***

![LMStudioSearch](../../../../translated_images/LMStudio_Search.1e577e0f69f336fc26e56653eeec2a20b90c3895cc4aa2ff05b6ec51059f12fd.ja.png)

***ダウンロードしたモデルをLM Studioで管理します***

![LMStudioLocal](../../../../translated_images/LMStudio_Local.55f9d6f61eb27f0f37fc4833599aa43fa45a66dfc20444ba1419a922b60b5005.ja.png)

## **3. LM StudioでPhi-3とチャットする**

LM Studio ChatでPhi-3を選択し、チャットテンプレート（Preset - Phi3）を設定して、Phi-3とのローカルチャットを開始します。

![LMStudioChat](../../../../translated_images/LMStudio_Chat.1bdc3a8f804f12d9548b386448c1642b741c10816576973155a90ef55f8a9c8d.ja.png)

***Note***:

a. LM Studioのコントロールパネルで詳細設定を通じてパラメータを設定できます。

b. Phi-3には特定のチャットテンプレート要件があるため、PresetでPhi-3を選択する必要があります。

c. GPUの使用量など、異なるパラメータも設定できます。

## **4. LM StudioからPhi-3 APIを呼び出す**

LM Studioはローカルサービスの迅速な展開をサポートし、コードを書かずにモデルサービスを構築できます。

![LMStudioServer](../../../../translated_images/LMStudio_Server.917c115e12599e7698ce323085ce4f8bdb020665656bbe90edca2d45a7de932d.ja.png)

これはPostmanでの結果です。

![LMStudioPostman](../../../../translated_images/LMStudio_Postman.4481aa4873ecaae0e05032f539090897002fc9aca9da5d1336fb28776f4c45a7.ja.png)

**免責事項**:
この文書は機械翻訳AIサービスを使用して翻訳されています。正確さを期すよう努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。元の言語で書かれた文書が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。