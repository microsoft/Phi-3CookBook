# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是一个专为 Apple Silicon 上的机器学习研究设计的数组框架，由 Apple 机器学习研究团队开发。

MLX 是为机器学习研究人员设计的，旨在兼顾易用性和高效性，方便模型的训练和部署。框架本身的设计也非常简洁，研究人员可以轻松扩展和改进 MLX，从而快速探索新想法。

通过 MLX，可以在 Apple Silicon 设备上加速运行大型语言模型（LLMs），并且可以非常方便地在本地运行模型。

目前，Apple MLX 框架支持对以下模型的量化转换：Phi-3.5-Instruct（**Apple MLX Framework 支持**）、Phi-3.5-Vision（**MLX-VLM Framework 支持**）、以及 Phi-3.5-MoE（**Apple MLX Framework 支持**）。接下来让我们试试：

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

### **🤖 Phi-3.5 与 Apple MLX 的示例**

| 实验室    | 简介 | 链接 |
| -------- | ------- |  ------- |
| 🚀 实验室 - 介绍 Phi-3.5 Instruct  | 学习如何使用 Apple MLX 框架运行 Phi-3.5 Instruct   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 实验室 - 介绍 Phi-3.5 Vision（图像） | 学习如何使用 Apple MLX 框架通过 Phi-3.5 Vision 分析图像     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 实验室 - 介绍 Phi-3.5 MoE   | 学习如何使用 Apple MLX 框架运行 Phi-3.5 MoE  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **资源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 仓库 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 仓库 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件作为权威来源。对于关键性信息，建议使用专业的人类翻译服务。我们对因使用本翻译而引起的任何误解或误读概不负责。