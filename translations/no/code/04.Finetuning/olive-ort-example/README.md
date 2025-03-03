# Finjustere Phi3 med Olive

I dette eksemplet vil du bruke Olive til å:

1. Finjustere en LoRA-adapter for å klassifisere fraser som Sad, Joy, Fear, Surprise.
1. Slå sammen adaptervektene med basismodellen.
1. Optimalisere og kvantisere modellen til `int4`.

Vi viser deg også hvordan du kan kjøre inferens på den finjusterte modellen ved hjelp av ONNX Runtime (ORT) Generate API.

> **⚠️ For finjustering trenger du et egnet GPU tilgjengelig - for eksempel en A10, V100, A100.**

## 💾 Installere

Opprett et nytt virtuelt Python-miljø (for eksempel ved hjelp av `conda`):

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
[Olive-konfigurasjonsfilen](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) inneholder en *arbeidsflyt* med følgende *passeringer*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På et overordnet nivå vil denne arbeidsflyten:

1. Finjustere Phi3 (i 150 steg, som du kan endre) ved hjelp av dataene i [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Slå sammen LoRA-adaptervektene med basismodellen. Dette gir deg en enkelt modellartefakt i ONNX-format.
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

Dette svaret skal være en enkeltordsklassifisering av frasen (Sad/Joy/Fear/Surprise).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.