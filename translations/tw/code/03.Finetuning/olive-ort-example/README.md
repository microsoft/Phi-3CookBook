# 使用 Olive 微調 Phi3

在這個範例中，你將使用 Olive 來：

1. 微調一個 LoRA adapter，將短語分類為 Sad、Joy、Fear、Surprise。
2. 將 adapter 的權重合併到基礎模型中。
3. 將模型優化並量化為 `int4`。

我們還會向你展示如何使用 ONNX Runtime (ORT) 的 Generate API 來推論微調後的模型。

> **⚠️ 微調需要一個合適的 GPU，例如 A10、V100、A100。**

## 💾 安裝

建立一個新的 Python 虛擬環境（例如，使用 `conda`）：

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
[Olive 配置文件](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含了一個帶有以下 *passes* 的 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

從高層次來看，這個工作流程將執行以下操作：

1. 使用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據對 Phi3 進行微調（150 步，你可以修改這個數值）。
2. 將 LoRA adapter 的權重合併到基礎模型中。這將生成一個 ONNX 格式的單一模型工件。
3. Model Builder 將優化模型以適配 ONNX runtime，並將模型量化為 `int4`。

執行工作流程，運行以下命令：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，優化的 `int4` 微調 Phi3 模型將可在以下位置找到：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後的 Phi3 集成到你的應用中

運行應用程序：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

這個回應應該是一個單詞，對短語進行分類（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文件是使用機器翻譯人工智慧服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。應以原文作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀概不負責。