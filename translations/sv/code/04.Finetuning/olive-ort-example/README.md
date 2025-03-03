# Fintuna Phi3 med Olive

I det här exemplet kommer du att använda Olive för att:

1. Fintuna en LoRA-adapter för att klassificera fraser som Sad, Joy, Fear, Surprise.
1. Slå samman adaptervikterna med basmodellen.
1. Optimera och kvantisera modellen till `int4`.

Vi visar också hur du kan köra inferens på den fintunade modellen med ONNX Runtime (ORT) Generate API.

> **⚠️ För fintuning behöver du ha ett lämpligt GPU tillgängligt - till exempel en A10, V100, A100.**

## 💾 Installera

Skapa en ny virtuell Python-miljö (till exempel med `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installera sedan Olive och de beroenden som krävs för en fintuning-arbetsflöde:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fintuna Phi3 med Olive
[Olive-konfigurationsfilen](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) innehåller ett *arbetsflöde* med följande *passager*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På en hög nivå kommer detta arbetsflöde att:

1. Fintuna Phi3 (i 150 steg, vilket du kan ändra) med hjälp av [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)-data.
1. Slå samman LoRA-adaptervikterna med basmodellen. Detta ger dig en enda modellartefakt i ONNX-format.
1. Model Builder optimerar modellen för ONNX runtime *och* kvantiserar modellen till `int4`.

För att köra arbetsflödet, kör:

```bash
olive run --config phrase-classification.json
```

När Olive är klar, finns din optimerade `int4` fintunade Phi3-modell tillgänglig i: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrera fintunade Phi3 i din applikation 

För att köra appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Detta svar bör vara en enskild ordklassificering av frasen (Sad/Joy/Fear/Surprise).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.