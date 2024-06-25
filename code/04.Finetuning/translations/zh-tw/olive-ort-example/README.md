# 微調 Phi-3 使用 Olive

在這個範例中，你將使用 Olive 來：

1. 微調一個 LoRA 適配器以將短語分類為 Sad, Joy, Fear, Surprise。
1. 將適配器權重合併到基礎模型中。
1. 優化並量化模型為 `int4`。

我們還會向你展示如何使用 ONNX Runtime (ORT) 產生 API 來推論微調模型。

> **⚠️ 若要進行微調，你需要有一個合適的 GPU 可用 - 例如，A10、V100、A100。**

## 💾 安裝

建立一個新的 Python 虛擬環境 (例如，使用 `conda`):

```bash
conda 建立 -n olive-ai python=3.11
conda activate olive-ai
```

接下來，安裝 Olive 和相依套件以進行微調工作流程:

```bash
cd Phi-3CookBook/程式碼/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3

[Olive configuration file](./phrase-classification.json) 包含一個*工作流程*，其中有以下*步驟*:

Phi-3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

在高層次上，這個工作流程將：

1. 使用 [dataset/data-classification.json](./dataset/dataset-classification.json) 資料對 Phi3 進行微調（150 步驟，可自行修改）。
1. 將 LoRA 適配器權重合併到基礎模型中。這將為你提供一個 ONNX 格式的單一模型工件。
1. 模型建構器將優化模型以適應 ONNX 執行時 *並且* 將模型量化為 `int4`。

要執行工作流程，請執行:

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你已優化的 `int4` 微調 Phi3 模型可在以下位置找到：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調的 Phi3 整合到您的應用程式中

要執行該應用程式:

```bash
python app/app.py --phrase "板球是一項美妙的運動！" --model-path models/lora-merge-mb/gpu-cuda_model
```

此回應應該是短語的單字分類（悲傷/喜悅/恐懼/驚訝）。

