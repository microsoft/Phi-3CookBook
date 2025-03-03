# Prilagoditev Phi3 z uporabo Olive

V tem primeru boste uporabili Olive za:

1. Prilagoditev LoRA adapterja za razvrščanje fraz v kategorije: Žalost, Veselje, Strah, Presenečenje.
1. Združitev uteži adapterja z osnovnim modelom.
1. Optimizacijo in kvantizacijo modela v `int4`.

Prav tako vam bomo pokazali, kako izvajati sklepanje (inference) na prilagojenem modelu z uporabo ONNX Runtime (ORT) Generate API.

> **⚠️ Za prilagajanje boste potrebovali ustrezen GPU - na primer A10, V100, A100.**

## 💾 Namestitev

Ustvarite novo virtualno okolje Python (na primer z uporabo `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Nato namestite Olive in odvisnosti za potek dela prilagajanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Prilagoditev Phi3 z uporabo Olive

[Konfiguracijska datoteka Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) vsebuje *potek dela* s sledečimi *koraki*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visoki ravni bo ta potek dela izvedel:

1. Prilagoditev Phi3 (za 150 korakov, kar lahko spremenite) z uporabo podatkov iz datoteke [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Združitev uteži LoRA adapterja z osnovnim modelom. To bo ustvarilo enoten artefakt modela v ONNX formatu.
1. Model Builder bo optimiziral model za ONNX runtime *in* kvantiziral model v `int4`.

Za zagon poteka dela izvedite:

```bash
olive run --config phrase-classification.json
```

Ko Olive zaključi, bo vaš optimiziran `int4` prilagojen model Phi3 na voljo v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija prilagojenega modela Phi3 v vašo aplikacijo

Za zagon aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odgovor bi moral biti enobesedna klasifikacija fraze (Žalost/Veselje/Strah/Presenečenje).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokovni prevod s strani človeškega prevajalca. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.