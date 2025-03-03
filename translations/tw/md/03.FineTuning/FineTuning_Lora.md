# **使用 LoRA 微調 Phi-3**

使用 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自定義聊天指令數據集上微調微軟的 Phi-3 Mini 語言模型。

LoRA 將幫助提升對話理解能力及回應生成效果。

## 微調 Phi-3 Mini 的逐步指南：

**導入和設置**

安裝 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先導入必要的庫，例如 datasets、transformers、peft、trl 和 torch。
設置日誌記錄以追蹤訓練過程。

你可以選擇替換一些層，使用 loralib 中實現的對應層。目前我們僅支持 nn.Linear、nn.Embedding 和 nn.Conv2d。我們還支持 MergedLinear，用於處理單個 nn.Linear 表示多層的情況，例如某些注意力 qkv 投影的實現（詳見附加說明）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

導入 loralib 模組

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在訓練循環開始前，僅標記 LoRA 參數為可訓練。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

保存檢查點時，生成僅包含 LoRA 參數的 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

使用 load_state_dict 加載檢查點時，請務必設置 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

現在可以像平常一樣進行訓練。

**超參數**

定義兩個字典：training_config 和 peft_config。training_config 包含訓練相關的超參數，例如學習率、批次大小和日誌設置。

peft_config 指定與 LoRA 相關的參數，如 rank、dropout 和任務類型。

**模型和分詞器加載**

指定預訓練 Phi-3 模型的路徑（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型設置，包括緩存使用、數據類型（bfloat16 用於混合精度）和注意力實現。

**訓練**

使用自定義聊天指令數據集微調 Phi-3 模型。利用 peft_config 中的 LoRA 設置實現高效適應。通過指定的日誌策略監控訓練進度。

**評估和保存**

評估微調後的模型。
在訓練過程中保存檢查點以供後續使用。

**範例**
- [透過這個範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 Hugging Face Hub 與 LORA 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡範例 - LORA 微調範例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用 Hugging Face Hub 與 QLORA 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：  
本文件使用基於機器的AI翻譯服務進行翻譯。我們雖然努力確保準確性，但請注意，自動翻譯可能會包含錯誤或不精確之處。應以原文語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀不承擔責任。