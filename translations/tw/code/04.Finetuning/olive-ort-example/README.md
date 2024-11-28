# 使用 Olive 微调 Phi3

在这个示例中，你将使用 Olive 来：

1. 微调一个 LoRA 适配器，将短语分类为 Sad、Joy、Fear、Surprise。
2. 将适配器权重合并到基础模型中。
3. 优化并量化模型到 `int4`。

我们还会向你展示如何使用 ONNX Runtime (ORT) Generate API 对微调后的模型进行推理。

> **⚠️ 对于微调，你需要有一个合适的 GPU 可用 - 例如 A10、V100、A100。**

## 💾 安装

创建一个新的 Python 虚拟环境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下来，安装 Olive 及其微调工作流所需的依赖：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微调 Phi3

[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含一个包含以下 *passes* 的 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

从高层次来看，这个工作流将：

1. 使用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 数据微调 Phi3（150 步，你可以修改）。
2. 将 LoRA 适配器权重合并到基础模型中。这将为你提供一个 ONNX 格式的单一模型工件。
3. Model Builder 将优化模型以适用于 ONNX runtime *并且* 将模型量化到 `int4`。

要执行工作流，运行：

```bash
olive run --config phrase-classification.json
```

当 Olive 完成后，你优化的 `int4` 微调 Phi3 模型将可在 `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model` 中找到。

## 🧑‍💻 将微调后的 Phi3 集成到你的应用中

运行应用程序：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

这个响应应该是短语的单词分类（Sad/Joy/Fear/Surprise）。

**免责声明**：
本文档已使用基于机器的人工智能翻译服务进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对使用此翻译所产生的任何误解或误读承担责任。