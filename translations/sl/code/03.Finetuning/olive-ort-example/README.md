# Prilagoditev Phi3 z uporabo Olive

V tem primeru boste uporabili Olive za:

1. Prilagoditev LoRA adapterja za razvrščanje fraz v kategorije: Žalost, Veselje, Strah, Presenečenje.
1. Združitev uteži adapterja z osnovnim modelom.
1. Optimizacijo in kvantizacijo modela v `int4`.

Prikazali vam bomo tudi, kako izvajati sklepanja z uporabo prilagojenega modela prek ONNX Runtime (ORT) Generate API.

> **⚠️ Za prilagajanje boste potrebovali ustrezen GPU, na primer A10, V100, A100.**

## 💾 Namestitev

Ustvarite novo Pythonovo virtualno okolje (na primer z uporabo `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Nato namestite Olive in odvisnosti za prilagoditveni delovni tok:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Prilagoditev Phi3 z uporabo Olive
[Olive konfiguracijska datoteka](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) vsebuje *delovni tok* z naslednjimi *koraki*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visoki ravni ta delovni tok izvede:

1. Prilagoditev Phi3 (za 150 korakov, kar lahko prilagodite) z uporabo podatkov [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Združitev uteži LoRA adapterja z osnovnim modelom. Tako dobite en sam model v ONNX formatu.
1. Model Builder optimizira model za ONNX Runtime *in* kvantizira model v `int4`.

Za zagon delovnega toka zaženite:

```bash
olive run --config phrase-classification.json
```

Ko Olive zaključi, bo vaš optimizirani `int4` prilagojeni Phi3 model na voljo v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija prilagojenega Phi3 v vašo aplikacijo 

Za zagon aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odgovor bo enobesedna razvrstitev fraze (Žalost/Veselje/Strah/Presenečenje).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za kakršne koli nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.