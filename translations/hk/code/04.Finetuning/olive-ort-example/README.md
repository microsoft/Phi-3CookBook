# 使用 Olive 微調 Phi3

喺呢個例子入面，你會用 Olive 嚟：

1. 微調 LoRA adapter，將句子分類為 Sad, Joy, Fear, Surprise。
1. 將 adapter 權重合併到 base model。
1. 優化同量化模型為 `int4`。

我哋仲會教你點樣用 ONNX Runtime (ORT) Generate API 去推論經微調嘅模型。

> **⚠️ 微調需要有合適嘅 GPU，例如 A10, V100, A100。**

## 💾 安裝

創建一個新的 Python 虛擬環境（例如用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接住，安裝 Olive 同埋微調流程所需嘅依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 用 Olive 微調 Phi3
[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含咗一個 *workflow*，入面有以下 *passes*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

喺高層次嚟講，呢個 workflow 會：

1. 用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 嘅數據微調 Phi3（150 個步驟，你可以修改呢個數字）。
1. 將 LoRA adapter 權重合併到 base model。呢樣會生成一個 ONNX 格式嘅單一模型工件。
1. Model Builder 會優化模型以適配 ONNX runtime，並將模型量化為 `int4`。

要執行呢個 workflow，運行：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你嘅經優化 `int4` 微調 Phi3 模型會喺呢度：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後嘅 Phi3 整合到你嘅應用程式

要運行應用程式：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

呢個回應應該係句子嘅單字分類（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文件使用機器翻譯人工智能服務進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。