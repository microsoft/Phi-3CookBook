# Fine-tune Phi3 met Olive

In dit voorbeeld gebruik je Olive om:

1. Een LoRA-adapter te fine-tunen om zinnen te classificeren als Sad, Joy, Fear, Surprise.
1. De adapter-gewichten samen te voegen met het basismodel.
1. Het model te optimaliseren en te kwantificeren in `int4`.

We laten je ook zien hoe je het fine-getunede model kunt gebruiken voor inferentie met de ONNX Runtime (ORT) Generate API.

> **⚠️ Voor fine-tuning heb je een geschikte GPU nodig, zoals een A10, V100, A100.**

## 💾 Installeren

Maak een nieuwe Python-virtuele omgeving (bijvoorbeeld met `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installeer vervolgens Olive en de afhankelijkheden voor een fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 met Olive
Het [Olive-configuratiebestand](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) bevat een *workflow* met de volgende *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Op hoofdlijnen zal deze workflow:

1. Phi3 fine-tunen (voor 150 stappen, wat je kunt aanpassen) met behulp van de gegevens in [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. De LoRA-adapter-gewichten samenvoegen met het basismodel. Dit resulteert in een enkel modelbestand in ONNX-formaat.
1. Model Builder zal het model optimaliseren voor de ONNX-runtime *en* het model kwantificeren in `int4`.

Om de workflow uit te voeren, voer je het volgende uit:

```bash
olive run --config phrase-classification.json
```

Wanneer Olive klaar is, is je geoptimaliseerde `int4` fine-getunede Phi3-model beschikbaar in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integreer fine-getunede Phi3 in je applicatie

Om de applicatie uit te voeren:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

De respons moet een enkel woord zijn dat de classificatie van de zin aangeeft (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.