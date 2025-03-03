# 使用 Olive 微調 Phi3

喺呢個例子入面，你會用 Olive 去：

1. 微調 LoRA adapter，將短語分類為 Sad、Joy、Fear、Surprise。
2. 將 adapter 權重合併到基礎模型。
3. 將模型優化並量化為 `int4`。

我哋仲會示範點樣用 ONNX Runtime (ORT) Generate API 去推理經微調嘅模型。

> **⚠️ 微調需要合適嘅 GPU，例如 A10、V100、A100。**

## 💾 安裝

創建一個新的 Python 虛擬環境（例如，用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接住，安裝 Olive 同埋微調工作流程所需嘅依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 用 Olive 微調 Phi3

[Olive 配置文件](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含一個帶有以下 *passes* 嘅 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

喺高層次嚟睇，呢個工作流程會：

1. 用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據微調 Phi3（150 步，你可以修改呢個數字）。
2. 將 LoRA adapter 權重合併到基礎模型。咁樣你就會有一個 ONNX 格式嘅單一模型工件。
3. Model Builder 會優化模型以適配 ONNX runtime *並且* 將模型量化為 `int4`。

執行工作流程：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你優化好嘅 `int4` 微調 Phi3 模型會喺呢度：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調嘅 Phi3 集成到你嘅應用程序

運行應用程序：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

呢個回應應該係短語嘅單一分類結果（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
此文件已使用機器翻譯服務進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。