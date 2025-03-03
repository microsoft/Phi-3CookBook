# **Phi-3 finomhangolása Lora-val**

A Microsoft Phi-3 Mini nyelvi modelljének finomhangolása egyedi chat utasításos adathalmazon a [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) segítségével.

A LORA segít javítani a beszélgetések megértését és a válaszok generálását.

## Lépésről lépésre útmutató a Phi-3 Mini finomhangolásához:

**Importálás és beállítás**

A loralib telepítése

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Kezdjük a szükséges könyvtárak importálásával, mint például datasets, transformers, peft, trl és torch. Állítsuk be a naplózást a tréning folyamat nyomon követéséhez.

Kiválaszthatod, hogy néhány réteget a loralib által implementált megfelelőikkel helyettesítesz. Jelenleg csak nn.Linear, nn.Embedding és nn.Conv2d támogatott. Továbbá támogatjuk a MergedLinear-t azokban az esetekben, amikor egyetlen nn.Linear több réteget képvisel, például az attention qkv vetítés néhány implementációjában (további információkért lásd az Egyéb Megjegyzések részt).

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

A tréning ciklus megkezdése előtt jelöljük meg csak a LoRA paramétereket taníthatóként.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Ellenőrzési pont mentésekor hozz létre egy state_dict-et, amely csak a LoRA paramétereket tartalmazza.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Amikor egy ellenőrzési pontot betöltünk a load_state_dict segítségével, ügyeljünk arra, hogy a strict=False legyen beállítva.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Most a tréning szokásos módon folytatódhat.

**Hiperparaméterek**

Határozz meg két szótárat: training_config és peft_config. A training_config tartalmazza a tréninghez szükséges hiperparamétereket, például a tanulási rátát, batch méretet és naplózási beállításokat.

A peft_config meghatározza a LoRA-hoz kapcsolódó paramétereket, mint például a rank, dropout és task type.

**Modell és Tokenizer betöltése**

Add meg az előre betanított Phi-3 modell elérési útját (például "microsoft/Phi-3-mini-4k-instruct"). Konfiguráld a modell beállításait, beleértve a gyorsítótár használatát, az adat típusát (bfloat16 a kevert pontossághoz) és az attention implementációt.

**Tréning**

Finomhangold a Phi-3 modellt az egyedi chat utasításos adathalmazon. Használd a LoRA beállításokat a peft_config-ból a hatékony adaptációhoz. Kövesd nyomon a tréning előrehaladását a megadott naplózási stratégiával.  
Értékelés és mentés: Értékeld ki a finomhangolt modellt.  
Mentett ellenőrzési pontokat használj a későbbi alkalmazásokhoz.

**Minták**
- [További információ ehhez a mintafüzethez](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Példa Python Finomhangolási Minta](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Példa Hugging Face Hub Finomhangolás LORA-val](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Példa Hugging Face Modellkártya - LORA Finomhangolási Minta](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Példa Hugging Face Hub Finomhangolás QLORA-val](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.