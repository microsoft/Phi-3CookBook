# **Pag-Fine-tune ng Phi-3 gamit ang LoRA**

Pag-Fine-tune ng Phi-3 Mini language model ng Microsoft gamit ang [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) sa isang custom na dataset para sa chat instructions.

Makakatulong ang LoRA na mapabuti ang pag-unawa sa mga pag-uusap at ang paggawa ng mga tugon.

## Gabay sa bawat hakbang kung paano mag-Fine-tune ng Phi-3 Mini:

**Pag-import at Setup**

Pag-install ng loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Simulan sa pag-import ng mga kinakailangang library tulad ng datasets, transformers, peft, trl, at torch. Mag-set up ng logging para masubaybayan ang proseso ng training.

Maaari mong piliing i-adapt ang ilang mga layer sa pamamagitan ng pagpapalit ng mga ito sa mga katumbas na ipinatupad gamit ang loralib. Sa ngayon, sinusuportahan lamang namin ang nn.Linear, nn.Embedding, at nn.Conv2d. Sinusuportahan din namin ang MergedLinear para sa mga kaso kung saan ang isang nn.Linear ay kumakatawan sa higit sa isang layer, tulad ng sa ilang implementasyon ng attention qkv projection (tingnan ang Karagdagang Tala para sa higit pang impormasyon).

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

Bago magsimula ang training loop, markahan lamang ang LoRA parameters bilang trainable.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Kapag nagse-save ng checkpoint, gumawa ng state_dict na naglalaman lamang ng LoRA parameters.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kapag naglo-load ng checkpoint gamit ang load_state_dict, tiyaking naka-set ang strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ngayon, maaari nang magpatuloy ang training gaya ng dati.

**Hyperparameters**

Mag-define ng dalawang dictionary: training_config at peft_config. Ang training_config ay naglalaman ng mga hyperparameters para sa training, tulad ng learning rate, batch size, at logging settings.

Ang peft_config ay tumutukoy sa mga LoRA-related parameters tulad ng rank, dropout, at uri ng task.

**Pag-load ng Model at Tokenizer**

Itakda ang path papunta sa pre-trained Phi-3 model (halimbawa, "microsoft/Phi-3-mini-4k-instruct"). I-configure ang mga setting ng model, kabilang ang paggamit ng cache, uri ng data (bfloat16 para sa mixed precision), at implementasyon ng attention.

**Training**

I-fine-tune ang Phi-3 model gamit ang custom na dataset para sa chat instructions. Gamitin ang LoRA settings mula sa peft_config para sa mas episyenteng pag-aangkop. Subaybayan ang progreso ng training gamit ang tinukoy na logging strategy.  
**Pagsusuri at Pag-save:** Suriin ang na-fine-tune na model.  
Mag-save ng checkpoints habang nagte-training para magamit sa hinaharap.

**Mga Halimbawa**
- [Alamin Pa gamit ang sample notebook na ito](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Halimbawa ng Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang LoRA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Halimbawa ng Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Habang sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng salin na ito.