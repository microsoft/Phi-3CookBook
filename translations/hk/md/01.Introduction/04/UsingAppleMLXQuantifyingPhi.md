# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是一個專為 Apple Silicon 上的機器學習研究打造的陣列框架，由 Apple 機器學習研究團隊開發。

MLX 是為機器學習研究人員設計的，目的是提供一個既方便使用又高效的模型訓練和部署工具。框架的設計理念也非常簡單明瞭，讓研究人員能輕鬆擴展和改進 MLX，快速探索新想法。

透過 MLX，可以在 Apple Silicon 設備上加速 LLMs，並且可以非常方便地在本地運行模型。

現在，Apple MLX 框架支持 Phi-3.5-Instruct（**Apple MLX Framework 支持**）、Phi-3.5-Vision（**MLX-VLM Framework 支持**）和 Phi-3.5-MoE（**Apple MLX Framework 支持**）的量化轉換。接下來讓我們試試看：

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

### **🤖 使用 Apple MLX 的 Phi-3.5 示例**

| 實驗室    | 介紹 | 連結 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習如何使用 Apple MLX 框架操作 Phi-3.5 Instruct   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 學習如何使用 Apple MLX 框架分析 Phi-3.5 Vision 的影像   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 學習如何使用 Apple MLX 框架操作 Phi-3.5 MoE  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 儲存庫 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 儲存庫 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**:  
本文件使用機器翻譯服務進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本為權威來源。對於關鍵信息，建議尋求專業的人手翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。