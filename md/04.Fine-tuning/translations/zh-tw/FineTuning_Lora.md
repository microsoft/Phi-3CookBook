# **微調 Phi-3 與 Lora**

微調 Microsoft 的 Phi-3 Mini 語言模型，使用 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自訂聊天指令資料集上。

LORA 將有助於改善對話理解和回應生成。

## Phi-3 Mini 微調的逐步指南:

**匯入和設定**

安裝 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA
```

開始匯入必要的函式庫，如 datasets、transformers、peft、trl 和 torch。
設定 logging 以追蹤訓練過程。

您可以選擇通過用 loralib 中實現的對應層替換來調整一些層。我們目前僅支持 nn.Linear、nn.Embedding 和 nn.Conv2d。我們還支持 MergedLinear，用於單個 nn.Linear 代表多個層的情況，例如在一些注意力 qkv 投影的實現中（有關更多資訊，請參見附加說明）。

```
# ===== 之前 =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== 之後 ======
```

import loralib as lora

```
# 添加一對低階適應矩陣，秩為 r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在訓練 for 迴圈開始之前，僅標記 LoRA 參數為可訓練。

```
import loralib as lora
model = BigModel()
# 這將 requires_grad 設定為 False，對於所有名稱中不包含 "lora_" 的參數
lora.mark_only_lora_as_trainable(model)
# 訓練迴圈
for batch in dataloader:
```

當儲存檢查點時，生成僅包含 LoRA 參數的 state_dict。

```
# ===== 之前 =====
# torch.save(model.state_dict(), checkpoint_path)
```

```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

當使用 load_state_dict 加載檢查點時，請確保將 strict=False 設定。

```
# 先載入預訓練的檢查點
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# 然後載入 LoRA 檢查點
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

現在訓練可以照常進行。

**超參數**

定義兩個字典: training_config 和 peft_config。training_config 包含訓練的超參數，例如學習率、批次大小和日誌設定。

peft_config 指定了與 LoRA 相關的參數，如 rank、dropout 和 task type。

**模型和分詞器載入**

指定預訓練 Phi-3 模型的路徑（例如，"microsoft/Phi-3-mini-4k-instruct"）。配置模型設定，包括快取使用、資料類型（bfloat16 用於混合精度）和注意力實現。

**訓練**

微調 Phi-3 模型，使用自訂聊天指令資料集。利用 peft_config 中的 LoRA 設定進行高效適應。使用指定的日誌策略監控訓練進度。
評估和保存: 評估微調後的模型。
在訓練期間保存檢查點以供日後使用。

**範例**

- [了解更多，請參考此範例筆記本](../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../code/04.Finetuning/FineTrainingScript.py)
- [使用 LORA 進行 Hugging Face Hub 微調範例](../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡範例 - LORA 微調範例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用 QLORA 進行 Hugging Face Hub 微調範例](../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

