# Fino podešavanje Phi3 koristeći Olive

U ovom primjeru koristit ćete Olive za:

1. Fino podešavanje LoRA adaptera kako biste klasificirali fraze u kategorije: Tuga, Radost, Strah, Iznenađenje.
2. Spajanje težina adaptera s osnovnim modelom.
3. Optimizaciju i kvantizaciju modela u `int4`.

Također ćemo vam pokazati kako napraviti inferenciju fino podešenog modela koristeći ONNX Runtime (ORT) Generate API.

> **⚠️ Za fino podešavanje trebat ćete imati odgovarajući GPU - na primjer, A10, V100, A100.**

## 💾 Instalacija

Kreirajte novo Python virtualno okruženje (na primjer, koristeći `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Zatim instalirajte Olive i ovisnosti potrebne za workflow fino podešavanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fino podešavanje Phi3 koristeći Olive
[Olive konfiguracijska datoteka](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) sadrži *workflow* s sljedećim *prolazima*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visokoj razini, ovaj workflow će:

1. Fino podesiti Phi3 (za 150 koraka, što možete prilagoditi) koristeći podatke iz [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Spojiti težine LoRA adaptera s osnovnim modelom. Ovo će rezultirati jednim modelom u ONNX formatu.
3. Model Builder će optimizirati model za ONNX runtime *i* kvantizirati model u `int4`.

Za pokretanje workflowa, izvršite:

```bash
olive run --config phrase-classification.json
```

Kada Olive završi, vaš optimizirani `int4` fino podešeni Phi3 model bit će dostupan na: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracija fino podešenog Phi3 u vašu aplikaciju 

Za pokretanje aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ovaj odgovor bi trebao biti jednostavna klasifikacija fraze u jednu riječ (Tuga/Radost/Strah/Iznenađenje).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluga za strojno prevođenje. Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.