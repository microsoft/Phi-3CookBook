# Fine-tune Phi3 met Olive

In dit voorbeeld gebruik je Olive om:

1. Een LoRA-adapter te fine-tunen om zinnen te classificeren als Sad, Joy, Fear, Surprise.
2. De adaptergewichten samen te voegen met het basismodel.
3. Het model te optimaliseren en te kwantificeren naar `int4`.

We laten je ook zien hoe je het gefinetunede model kunt gebruiken voor inferentie met de ONNX Runtime (ORT) Generate API.

> **⚠️ Voor fine-tuning heb je een geschikte GPU nodig - bijvoorbeeld een A10, V100, A100.**

## 💾 Installeren

Maak een nieuwe Python-virtuele omgeving aan (bijvoorbeeld met `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installeer vervolgens Olive en de benodigde afhankelijkheden voor een fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 met Olive

Het [Olive-configuratiebestand](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) bevat een *workflow* met de volgende *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Op hoofdlijnen zal deze workflow:

1. Phi3 fine-tunen (voor 150 stappen, dit kun je aanpassen) met behulp van de [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) data.
2. De LoRA-adaptergewichten samenvoegen met het basismodel. Dit resulteert in een enkel modelartefact in het ONNX-formaat.
3. Het model optimaliseren voor de ONNX-runtime *en* het model kwantificeren naar `int4` met Model Builder.

Om de workflow uit te voeren, gebruik:

```bash
olive run --config phrase-classification.json
```

Wanneer Olive klaar is, is je geoptimaliseerde `int4` gefinetunede Phi3-model beschikbaar in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integreer gefinetunede Phi3 in je applicatie

Om de app uit te voeren:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

De output moet een enkele woordclassificatie van de zin zijn (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gebaseerde automatische vertaaldiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of onjuiste interpretaties die voortvloeien uit het gebruik van deze vertaling.