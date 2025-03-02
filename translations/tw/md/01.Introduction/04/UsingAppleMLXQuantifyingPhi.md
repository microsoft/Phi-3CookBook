# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是一個專為 Apple Silicon 上的機器學習研究設計的陣列框架，由 Apple 機器學習研究團隊開發。

MLX 是專為機器學習研究人員設計的框架，目的是提供使用者友好的操作體驗，同時保證模型的訓練與部署效率。這個框架的設計概念簡單明瞭，目的是讓研究人員能夠輕鬆擴展和改進 MLX，從而快速探索新想法。

透過 MLX，可以在 Apple Silicon 設備上加速運行大型語言模型（LLMs），並且可以非常方便地在本地運行模型。

目前 Apple MLX 框架支援 Phi-3.5-Instruct（**Apple MLX Framework 支援**）、Phi-3.5-Vision（**MLX-VLM Framework 支援**）、以及 Phi-3.5-MoE（**Apple MLX Framework 支援**）的量化轉換功能。我們接下來試試看：

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

### **🤖 使用 Apple MLX 的 Phi-3.5 範例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-介紹 Phi-3.5 Instruct  | 學習如何使用 Apple MLX 框架操作 Phi-3.5 Instruct   |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-介紹 Phi-3.5 Vision（圖像） | 學習如何使用 Apple MLX 框架分析圖像，運行 Phi-3.5 Vision     |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-介紹 Phi-3.5 MoE   | 學習如何使用 Apple MLX 框架操作 Phi-3.5 MoE  |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 儲存庫 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 儲存庫 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**：  
本文件是使用機器翻譯AI服務進行翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文的母語版本作為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對於因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。