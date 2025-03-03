# 使用 Olive 微调 Phi3

在此示例中，您将使用 Olive 来完成以下任务：

1. 微调一个 LoRA 适配器，将短语分类为 Sad（悲伤）、Joy（喜悦）、Fear（恐惧）、Surprise（惊讶）。
2. 将适配器权重合并到基础模型中。
3. 优化并量化模型为 `int4`。

我们还会向您展示如何使用 ONNX Runtime (ORT) 的 Generate API 推理微调后的模型。

> **⚠️ 微调需要有合适的 GPU，例如 A10、V100、A100。**

## 💾 安装

创建一个新的 Python 虚拟环境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下来，安装 Olive 和微调工作流所需的依赖项：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微调 Phi3

[Olive 配置文件](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含一个包含以下 *步骤* 的 *工作流*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

从总体上看，该工作流将执行以下操作：

1. 使用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 数据微调 Phi3（150 步，您可以自行修改）。
2. 将 LoRA 适配器权重合并到基础模型中。这将生成一个 ONNX 格式的单一模型文件。
3. Model Builder 将优化模型以适配 ONNX Runtime，并将模型量化为 `int4`。

要执行工作流，请运行：

```bash
olive run --config phrase-classification.json
```

当 Olive 完成后，您优化后的 `int4` 微调 Phi3 模型将位于以下路径：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 将微调后的 Phi3 集成到您的应用程序中

运行应用程序：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

该响应应为短语的单词分类结果（Sad/Joy/Fear/Surprise）。

**免责声明**：  
本文档是使用基于机器的AI翻译服务翻译的。虽然我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的母语版本作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读概不负责。