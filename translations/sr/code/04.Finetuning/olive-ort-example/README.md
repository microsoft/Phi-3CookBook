# Fino-tjuniranje Phi3 koristeći Olive

U ovom primeru ćete koristiti Olive da:

1. Fino-tjunirate LoRA adapter za klasifikaciju fraza u kategorije: Tuga, Radost, Strah, Iznenađenje.
2. Spojite težine adaptera sa osnovnim modelom.
3. Optimizujete i kvantizujete model u `int4`.

Takođe ćemo vam pokazati kako da koristite fino-tjunirani model za inferenciju koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino-tjuniranje, potrebno je da imate odgovarajući GPU - na primer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novo Python virtuelno okruženje (na primer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i zavisnosti potrebne za radni tok fino-tjuniranja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino-tjuniranje Phi3 koristeći Olive
[Olive konfiguraciona datoteka](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) sadrži *radni tok* sa sledećim *prolazima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokom nivou, ovaj radni tok će:

1. Fino-tjunirati Phi3 (za 150 koraka, što možete prilagoditi) koristeći podatke iz [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Spojiti LoRA težine adaptera sa osnovnim modelom. Ovo će vam dati jedan model u ONNX formatu.
3. Model Builder će optimizovati model za ONNX runtime *i* kvantizovati model u `int4`.

Da biste pokrenuli radni tok, izvršite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizovani `int4` fino-tjunirani Phi3 model će biti dostupan na lokaciji: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino-tjuniranog Phi3 modela u vašu aplikaciju 

Za pokretanje aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odgovor bi trebalo da bude klasifikacija fraze u jednu reč (Tuga/Radost/Strah/Iznenađenje).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која произилазе из коришћења овог превода.