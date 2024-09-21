# 使用 Olive 微調 Phi3

在這個範例中，你將使用 Olive 來：

1. 微調一個 LoRA 適配器，將短語分類為 Sad, Joy, Fear, Surprise。
2. 將適配器的權重合併到基礎模型中。
3. 將模型優化並量化為 `int4`。

我們還會展示如何使用 ONNX Runtime (ORT) Generate API 來推理微調後的模型。

> **⚠️ 微調需要有適當的 GPU，例如 A10, V100, A100。**

## 💾 安裝

創建一個新的 Python 虛擬環境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下來，安裝 Olive 以及微調工作流程所需的依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3

[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含一個具有以下 *passes* 的 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

在高層次上，這個工作流程將：

1. 使用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據微調 Phi3（150 步，你可以修改）。
2. 將 LoRA 適配器權重合併到基礎模型中。這將為你提供一個 ONNX 格式的單一模型工件。
3. Model Builder 將為 ONNX runtime 優化模型，並將模型量化為 `int4`。

要執行這個工作流程，運行：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你的優化 `int4` 微調 Phi3 模型將在：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後的 Phi3 集成到你的應用程序中

運行應用程序：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

這個回應應該是一個單詞的短語分類 (Sad/Joy/Fear/Surprise)。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不夠完美。請檢查輸出並進行任何必要的修正。