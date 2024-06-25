# **推論 Phi-3 與 Apple MLX 框架**

## **什麼是 MLX 框架**

MLX 是一個用於蘋果矽晶機器學習研究的陣列框架，由蘋果機器學習研究提供。

MLX 是由機器學習研究人員為機器學習研究人員設計的。該框架旨在對使用者友好，但仍能有效地訓練和部署模型。框架本身的設計在概念上也很簡單。我們的目標是讓研究人員能夠輕鬆擴展和改進 MLX，以便快速探索新想法。

蘋果 Silicon 設備中的 LLMs 可以通過 MLX 加速，並且模型可以非常方便地在本地執行。

## **使用 MLX 推論 Phi-3-mini**

### **1. 設定你 MLX 環境**

1. Python 3.11.x
2. 安裝 MLX 函式庫

```bash

pip install mlx-lm

```

### **2. 執行 Phi-3-mini 在 Terminal 與 MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\n你可以介紹一下你自己嗎<|end|>\n<|assistant|>"

```

結果 (我的環境是 Apple M1 Max,64GB) 是

![終端機](../../../../imgs/03/MLX/01.png)

### **3. 使用 MLX 在終端機量化 Phi-3-mini**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** 該模型可以通過 mlx_lm.convert 量化，預設量化為 INT4。此範例將 Phi-3-mini 量化為 INT4

模型可以通過 mlx_lm.convert 量化，預設量化為 INT4。此範例是將 Phi-3-mini 量化為 INT4。量化後，它將儲存在預設目錄 ./mlx_model 中。

我們可以從終端測試使用 MLX 量化的模型

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

結果是

![INT4](../../../../imgs/03/MLX/02.png)

### **4. 執行 Phi-3-mini 與 MLX 在 Jupyter Notebook**

![Notebook](../../../../imgs/03/MLX/03.png)

***注意:*** 請閱讀此範例 [點擊此連結](../../../../code/03.Inference/translations/zh-tw/MLX/MLX_DEMO.ipynb)。

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 資源庫 [https://github.com/ml-explore](https://github.com/ml-explore)

