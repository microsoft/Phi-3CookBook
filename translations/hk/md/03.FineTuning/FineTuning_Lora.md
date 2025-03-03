# **用 LoRA 微調 Phi-3**

使用 [LoRA (低秩適應)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 喺自訂對話指令數據集上微調 Microsoft 嘅 Phi-3 Mini 語言模型。

LoRA 可以幫助改進對話理解同生成回應嘅能力。

## 微調 Phi-3 Mini 嘅逐步指南：

**導入同設置**

安裝 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先導入必要嘅庫，例如 datasets、transformers、peft、trl 同 torch。  
設置日誌記錄，用嚟追蹤訓練過程。

你可以選擇用 loralib 實現嘅對應層嚟取代某啲層。我哋而家只支持 nn.Linear、nn.Embedding 同 nn.Conv2d。仲支持 MergedLinear，適用於單個 nn.Linear 代表多層嘅情況，例如某啲注意力 qkv 投影嘅實現（詳細請參閱附加說明）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

喺訓練循環開始之前，只標記 LoRA 嘅參數為可訓練。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

保存檢查點時，生成只包含 LoRA 參數嘅 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

使用 load_state_dict 加載檢查點時，記得設置 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

而家可以如常進行訓練。

**超參數**

定義兩個字典：training_config 同 peft_config。  
training_config 包括訓練嘅超參數，例如學習率、批量大小同日誌設置。

peft_config 指定同 LoRA 有關嘅參數，例如秩、dropout 同任務類型。

**模型同分詞器加載**

指定預訓練 Phi-3 模型嘅路徑（例如 "microsoft/Phi-3-mini-4k-instruct"）。  
配置模型設置，包括緩存使用、數據類型（混合精度嘅 bfloat16）同注意力實現。

**訓練**

使用自訂對話指令數據集微調 Phi-3 模型。  
利用 peft_config 中嘅 LoRA 設置嚟進行高效適應。  
通過指定嘅日誌策略監控訓練進度。  
評估同保存：評估微調後嘅模型。  
喺訓練期間保存檢查點以供日後使用。

**範例**
- [用呢個範例筆記學多啲](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [用 LoRA 喺 Hugging Face Hub 微調嘅範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face 模型卡範例 - LoRA 微調範例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [用 QLORA 喺 Hugging Face Hub 微調嘅範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)  

**免責聲明**：  
本文件已使用機器翻譯服務進行翻譯。我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文文件應被視為權威來源。對於關鍵信息，建議使用專業的人工作翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。