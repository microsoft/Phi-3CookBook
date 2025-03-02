# **Kurekebisha Phi-3 kwa kutumia LoRA**

Kurekebisha mfano wa lugha wa Microsoft Phi-3 Mini kwa kutumia [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) kwenye seti ya data maalum ya maelekezo ya mazungumzo. 

LoRA itasaidia kuboresha uelewa wa mazungumzo na kizazi cha majibu.

## Mwongozo wa hatua kwa hatua wa kurekebisha Phi-3 Mini:

**Uingizaji na Maandalizi**

Kufunga loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Anza kwa kuingiza maktaba muhimu kama datasets, transformers, peft, trl, na torch. 
Sanidi ufuatiliaji wa mafunzo kwa kutumia logging.

Unaweza kuchagua kurekebisha baadhi ya tabaka kwa kuzibadilisha na tabaka zinazotekelezwa na loralib. Kwa sasa tunasaidia nn.Linear, nn.Embedding, na nn.Conv2d pekee. Pia tunasaidia MergedLinear kwa hali ambapo nn.Linear moja inawakilisha zaidi ya tabaka moja, kama katika utekelezaji fulani wa makadirio ya umakini wa qkv (angalia Maelezo ya Ziada kwa zaidi).

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

Kabla ya mzunguko wa mafunzo kuanza, weka tu vigezo vya LoRA kama vinavyoweza kufundishwa.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Unapohifadhi checkpoint, tengeneza state_dict inayojumuisha tu vigezo vya LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Unapopakua checkpoint kwa kutumia load_state_dict, hakikisha umeweka strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sasa mafunzo yanaweza kuendelea kama kawaida.

**Hyperparameters**

Taja kamusi mbili: training_config na peft_config. training_config inajumuisha hyperparameters za mafunzo, kama kiwango cha kujifunza, ukubwa wa kundi, na mipangilio ya logging.

peft_config inabainisha vigezo vinavyohusiana na LoRA kama rank, dropout, na aina ya kazi.

**Upakiaji wa Mfano na Tokenizer**

Bainisha njia ya mfano wa Phi-3 uliokwisha funzwa (kwa mfano, "microsoft/Phi-3-mini-4k-instruct"). Sanidi mipangilio ya mfano, ikijumuisha matumizi ya cache, aina ya data (bfloat16 kwa mchanganyiko wa usahihi), na utekelezaji wa umakini.

**Mafunzo**

Rekebisha mfano wa Phi-3 kwa kutumia seti ya data maalum ya maelekezo ya mazungumzo. Tumia mipangilio ya LoRA kutoka peft_config kwa urekebishaji wa ufanisi. Fuatilia maendeleo ya mafunzo kwa kutumia mkakati wa logging uliobainishwa.

Tathmini na Kuhifadhi: Tathmini mfano uliorekebishwa. Hifadhi checkpoints wakati wa mafunzo kwa matumizi ya baadaye.

**Mifano**
- [Jifunze Zaidi na daftari hili la mfano](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Mfano wa Skripti ya Python ya Kufundisha](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Mfano wa Kufundisha kwa Hugging Face Hub kwa kutumia LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Mfano wa Kadi ya Mfano ya Hugging Face - Kufundisha kwa LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Mfano wa Kufundisha kwa Hugging Face Hub kwa kutumia QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.