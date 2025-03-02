# Fino podešavanje Phi3 pomoću Olive

U ovom primjeru koristit ćete Olive za:

1. Fino podešavanje LoRA adaptera za klasifikaciju fraza u kategorije Tuga, Radost, Strah, Iznenađenje.
1. Spajanje težina adaptera u osnovni model.
1. Optimizaciju i kvantizaciju modela u `int4`.

Također ćemo vam pokazati kako izvršiti inferenciju fino podešenog modela koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino podešavanje, trebat će vam odgovarajući GPU - na primjer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novu Python virtualnu okolinu (na primjer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i ovisnosti za workflow fino podešavanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino podešavanje Phi3 pomoću Olive
[Olive konfiguracijska datoteka](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) sadrži *workflow* s sljedećim *koracima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokoj razini, ovaj workflow će:

1. Fino podesiti Phi3 (za 150 koraka, što možete izmijeniti) koristeći podatke iz [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Spojiti težine LoRA adaptera u osnovni model. Ovo će vam dati jedan modelni artefakt u ONNX formatu.
1. Model Builder će optimizirati model za ONNX runtime *i* kvantizirati model u `int4`.

Za pokretanje workflowa, izvršite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizirani `int4` fino podešeni Phi3 model bit će dostupan u: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino podešenog Phi3 u vašu aplikaciju 

Za pokretanje aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ovaj odgovor trebao bi biti jednostavna klasifikacija fraze u jednu riječ (Tuga/Radost/Strah/Iznenađenje).

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno podržanog AI prevođenja. Iako težimo točnosti, molimo vas da budete svjesni da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.