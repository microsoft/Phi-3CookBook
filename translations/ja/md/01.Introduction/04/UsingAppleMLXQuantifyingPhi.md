# **Apple MLXフレームワークを使用したPhi-3.5の量子化**

MLXはAppleシリコン上での機械学習研究のための配列フレームワークであり、Appleの機械学習研究チームによって開発されました。

MLXは機械学習研究者のために設計されており、使いやすさと効率性を兼ね備えています。このフレームワークは、モデルのトレーニングやデプロイを効率的に行えるように設計されています。また、フレームワーク自体の設計も概念的にシンプルで、研究者がMLXを簡単に拡張し、新しいアイデアを迅速に試せるようにすることを目指しています。

LLMはAppleシリコンデバイス上でMLXを使用して高速化することができ、ローカルで簡単に実行することが可能です。

現在、Apple MLXフレームワークは以下のPhi-3.5モデルの量子化変換をサポートしています：
- Phi-3.5-Instruct（**Apple MLXフレームワーク対応**）
- Phi-3.5-Vision（**MLX-VLMフレームワーク対応**）
- Phi-3.5-MoE（**Apple MLXフレームワーク対応**）

次に試してみましょう：

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLXを使用したPhi-3.5のサンプル**

| ラボ    | 内容 | リンク |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instructの紹介  | Apple MLXフレームワークを使用したPhi-3.5 Instructの使い方を学ぶ   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision（画像） | Apple MLXフレームワークを使用してPhi-3.5 Visionで画像を解析する方法を学ぶ     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Phi-3.5 MoEの紹介   | Apple MLXフレームワークを使用したPhi-3.5 MoEの使い方を学ぶ  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHubリポジトリ [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責事項**:  
本書類は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（元の言語で記載された文書）が公式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤った解釈について、当社は一切の責任を負いません。