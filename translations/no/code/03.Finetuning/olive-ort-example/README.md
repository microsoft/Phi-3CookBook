# Finjuster Phi3 med Olive

I dette eksempelet skal du bruke Olive til å:

1. Finjustere en LoRA-adapter for å klassifisere fraser som Sad, Joy, Fear, Surprise.
1. Slå sammen adaptervektene med basismodellen.
1. Optimalisere og kvantisere modellen til `int4`.

Vi vil også vise deg hvordan du kan gjøre inferens med den finjusterte modellen ved å bruke ONNX Runtime (ORT) Generate API.

> **⚠️ For finjustering trenger du tilgang til en passende GPU - for eksempel en A10, V100, A100.**

## 💾 Installere

Opprett et nytt virtuelt Python-miljø (for eksempel ved å bruke `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Deretter installerer du Olive og avhengighetene for en finjusteringsarbeidsflyt:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Finjustere Phi3 med Olive
[Olive-konfigurasjonsfilen](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) inneholder en *arbeidsflyt* med følgende *passeringer*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På et overordnet nivå vil denne arbeidsflyten:

1. Finjustere Phi3 (i 150 steg, som du kan endre) ved å bruke data fra [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Slå sammen LoRA-adaptervektene med basismodellen. Dette vil gi deg én enkelt modellartefakt i ONNX-format.
1. Model Builder vil optimalisere modellen for ONNX Runtime *og* kvantisere modellen til `int4`.

For å kjøre arbeidsflyten, kjør:

```bash
olive run --config phrase-classification.json
```

Når Olive er ferdig, vil din optimaliserte `int4` finjusterte Phi3-modell være tilgjengelig i: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrere finjustert Phi3 i applikasjonen din

For å kjøre appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Denne responsen skal være en enkeltordsklassifisering av frasen (Sad/Joy/Fear/Surprise).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.