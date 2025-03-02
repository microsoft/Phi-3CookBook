# 使用 Olive 微調 Phi3

在這個範例中，你將使用 Olive 完成以下任務：

1. 微調 LoRA adapter，將短語分類為 Sad、Joy、Fear、Surprise。
2. 將 adapter 權重合併到基礎模型中。
3. 將模型優化並量化為 `int4`。

我們還會向你展示如何使用 ONNX Runtime (ORT) Generate API 對微調後的模型進行推理。

> **⚠️ 微調需要合適的 GPU，例如 A10、V100 或 A100。**

## 💾 安裝

建立一個新的 Python 虛擬環境（例如使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下來，安裝 Olive 和微調工作流程所需的依賴項：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3
[Olive 配置檔案](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含了一個包含以下 *passes* 的 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

從高層次來看，這個工作流程將完成以下任務：

1. 使用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 資料對 Phi3 進行微調（150 步，這個數值可以修改）。
2. 將 LoRA adapter 的權重合併到基礎模型中。這會生成一個 ONNX 格式的單一模型文件。
3. 使用 Model Builder 將模型優化為適用於 ONNX runtime 並將其量化為 `int4`。

執行工作流程的指令為：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你的經過優化的 `int4` 微調 Phi3 模型將存放於：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後的 Phi3 整合到你的應用程式中

執行應用程式：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

這個回應應該是短語的一個單字分類（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文檔使用基於機器的人工智能翻譯服務進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。