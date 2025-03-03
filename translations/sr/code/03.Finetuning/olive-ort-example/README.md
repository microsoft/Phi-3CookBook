# Fino-tjuniranje Phi3 koristeći Olive

U ovom primeru koristićete Olive da:

1. Fino-tjunirate LoRA adapter za klasifikaciju fraza na kategorije Tuga, Radost, Strah, Iznenađenje.
1. Spojite težine adaptera sa osnovnim modelom.
1. Optimizujete i kvantizujete model u `int4`.

Takođe ćemo vam pokazati kako da izvršite inferenciju fino-tjuniranog modela koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino-tjuniranje, potrebno je da imate odgovarajući GPU - na primer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novo virtuelno okruženje za Python (na primer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i zavisnosti potrebne za fino-tjuniranje:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino-tjuniranje Phi3 koristeći Olive
[Olive konfiguraciona datoteka](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) sadrži *workflow* sa sledećim *koracima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokom nivou, ovaj workflow će:

1. Fino-tjunirati Phi3 (za 150 koraka, što možete izmeniti) koristeći podatke iz [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Spojiti težine LoRA adaptera sa osnovnim modelom. Ovo će vam dati jedan model u ONNX formatu.
1. Model Builder će optimizovati model za ONNX runtime *i* kvantizovati model u `int4`.

Da biste pokrenuli workflow, izvršite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizovani `int4` fino-tjunirani Phi3 model biće dostupan na: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino-tjuniranog Phi3 u vašu aplikaciju 

Da biste pokrenuli aplikaciju:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ovaj odgovor bi trebalo da bude jednostavna klasifikacija fraze (Tuga/Radost/Strah/Iznenađenje).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да преводи буду тачни, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неразумевања настала употребом овог превода.