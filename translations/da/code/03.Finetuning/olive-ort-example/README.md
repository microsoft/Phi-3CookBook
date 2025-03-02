# Finjuster Phi3 med Olive

I dette eksempel vil du bruge Olive til at:

1. Finjustere en LoRA-adapter til at klassificere sætninger som Sad, Joy, Fear, Surprise.
1. Flette adapterens vægte ind i basismodellen.
1. Optimere og kvantisere modellen til `int4`.

Vi viser dig også, hvordan du foretager inferens med den finjusterede model ved hjælp af ONNX Runtime (ORT) Generate API.

> **⚠️ Til finjustering skal du have adgang til en passende GPU - for eksempel en A10, V100, A100.**

## 💾 Installation

Opret et nyt Python-virtuelt miljø (for eksempel ved hjælp af `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installer derefter Olive og de nødvendige afhængigheder til en finjusteringsarbejdsgang:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Finjuster Phi3 med Olive
[Olive-konfigurationsfilen](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) indeholder en *arbejdsgang* med følgende *passer*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

På et overordnet niveau vil denne arbejdsgang:

1. Finjustere Phi3 (i 150 trin, som du kan ændre) ved hjælp af dataene fra [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Flette LoRA-adapterens vægte ind i basismodellen. Dette giver dig en enkelt modelartefakt i ONNX-format.
1. Model Builder vil optimere modellen til ONNX runtime *og* kvantisere modellen til `int4`.

For at køre arbejdsgangen skal du udføre:

```bash
olive run --config phrase-classification.json
```

Når Olive er færdig, vil din optimerede `int4` finjusterede Phi3-model være tilgængelig her: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrer den finjusterede Phi3 i din applikation 

For at køre appen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Dette svar skal være en enkelt ordklassifikation af sætningen (Sad/Joy/Fear/Surprise).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvaret for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.