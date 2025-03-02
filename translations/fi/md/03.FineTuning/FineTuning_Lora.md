# **Phi-3:n hienosäätö Lora-menetelmällä**

Microsoftin Phi-3 Mini -kielimallin hienosäätö käyttäen [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) -menetelmää mukautetulla keskusteluohjeistodatasetillä.

LORA parantaa keskustelun ymmärtämistä ja vastausten tuottamista.

## Vaiheittainen opas Phi-3 Mini -mallin hienosäätöön:

**Tuonnit ja asetukset** 

Loralibin asentaminen

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Aloita tuomalla tarvittavat kirjastot, kuten datasets, transformers, peft, trl ja torch. 
Määritä lokitus koulutusprosessin seuraamiseksi.

Voit valita mukautettavia kerroksia korvaamalla ne loralibin toteutuksilla. Tällä hetkellä tuemme vain nn.Linear-, nn.Embedding- ja nn.Conv2d-kerroksia. Lisäksi tuemme MergedLinear-rakennetta tapauksissa, joissa yksi nn.Linear edustaa useampaa kerrosta, kuten joissakin attention qkv -projektion toteutuksissa (katso lisätietoja kohdasta Additional Notes).

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

Ennen koulutussilmukan aloittamista merkitse vain LoRA-parametrit koulutettaviksi.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Kun tallennat tarkistuspisteen, luo state_dict, joka sisältää vain LoRA-parametrit.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kun lataat tarkistuspisteen load_state_dict-funktiolla, varmista, että strict=False on asetettu.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nyt koulutus voi jatkua normaalisti.

**Hyperparametrit** 

Määritä kaksi sanakirjaa: training_config ja peft_config. training_config sisältää koulutuksen hyperparametrit, kuten oppimisnopeuden, eräkoolla ja lokitusasetukset.

peft_config määrittää LoRA:an liittyvät parametrit, kuten rank, dropout ja tehtävätyypin.

**Mallin ja tokenisoijan lataaminen** 

Määritä polku esikoulutettuun Phi-3-malliin (esim. "microsoft/Phi-3-mini-4k-instruct"). Konfiguroi malliasetukset, mukaan lukien välimuistin käyttö, datatyyppi (bfloat16 sekoitetulle tarkkuudelle) ja attention-toteutus.

**Koulutus** 

Hienosäädä Phi-3-malli mukautetun keskusteluohjeistodatasetin avulla. Hyödynnä LoRA-asetuksia peft_configista tehokasta mukautusta varten. Seuraa koulutuksen etenemistä määritetyn lokitusstrategian avulla.
Arviointi ja tallennus: Arvioi hienosäädetty malli.
Tallenna tarkistuspisteet koulutuksen aikana myöhempää käyttöä varten.

**Esimerkit**
- [Lisätietoja tästä esimerkkitiedostosta](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python-hienosäätöesimerkki](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub -hienosäätö LORA:lla](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face -mallikortti - LORA-hienosäätöesimerkki](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub -hienosäätö QLORA:lla](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälykäännöspalveluita käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virheellisistä tulkinnoista.