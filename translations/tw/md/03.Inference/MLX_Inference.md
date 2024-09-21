# **使用 Apple MLX 框架推理 Phi-3**

## **什麼是 MLX 框架**

MLX 是一個針對 Apple 硅晶片上機器學習研究的陣列框架，由 Apple 機器學習研究團隊推出。

MLX 是由機器學習研究人員為機器學習研究人員設計的。這個框架旨在對使用者友好，但同時仍然高效地訓練和部署模型。框架的設計概念也相對簡單。我們希望讓研究人員能夠輕鬆擴展和改進 MLX，以便快速探索新想法。

LLMs 可以通過 MLX 在 Apple 硅晶片設備上加速運行，並且模型可以非常方便地在本地運行。

## **使用 MLX 推理 Phi-3-mini**

### **1. 設置你的 MLX 環境**

1. Python 3.11.x
2. 安裝 MLX 庫

```bash

pip install mlx-lm

```

### **2. 在終端中使用 MLX 運行 Phi-3-mini**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（我的環境是 Apple M1 Max, 64GB）如下

![Terminal](../../../../translated_images/01.5cb5f10f82619d0a98bc3584bf81264105a33d9d8559f125418a93b8d7527728.tw.png)

### **3. 在終端中使用 MLX 量化 Phi-3-mini**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** 模型可以通過 mlx_lm.convert 進行量化，默認量化為 INT4。本例將 Phi-3-mini 量化為 INT4。

模型可以通過 mlx_lm.convert 進行量化，默認量化為 INT4。本例將 Phi-3-mini 量化為 INT4。量化後，模型將存儲在默認目錄 ./mlx_model 中。

我們可以從終端測試使用 MLX 量化的模型

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果如下

![INT4](../../../../translated_images/02.6ca278966b75435a31021b0a6f1f3b377102d7e59e7b90daf8f017c1a9876cb2.tw.png)

### **4. 在 Jupyter Notebook 中使用 MLX 運行 Phi-3-mini**

![Notebook](../../../../translated_images/03.5b701d4bfe17c5d20c075f7d4c8d1201b8073c8e8196b364a9a19cbe684dd26a.tw.png)

***注意：*** 請閱讀這個範例 [點擊這個鏈接](../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 資源庫 [https://github.com/ml-explore](https://github.com/ml-explore)

免責聲明：此翻譯由人工智慧模型從原文翻譯而來，可能不夠完美。請檢查輸出並做出任何必要的修改。