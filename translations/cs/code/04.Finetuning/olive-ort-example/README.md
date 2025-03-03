# Doladění Phi3 pomocí Olive

V tomto příkladu použijete Olive k:

1. Doladění LoRA adaptéru pro klasifikaci frází do kategorií Smutek, Radost, Strach, Překvapení.
1. Sloučení vah adaptéru do základního modelu.
1. Optimalizaci a kvantizaci modelu do `int4`.

Také vám ukážeme, jak provést inferenci doladěného modelu pomocí ONNX Runtime (ORT) Generate API.

> **⚠️ Pro doladění budete potřebovat vhodnou GPU - například A10, V100, A100.**

## 💾 Instalace

Vytvořte nové virtuální prostředí Pythonu (například pomocí `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Poté nainstalujte Olive a závislosti pro workflow doladění:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Doladění Phi3 pomocí Olive
[Konfigurační soubor Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) obsahuje *workflow* s následujícími *průchody*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na vysoké úrovni tento workflow provede:

1. Doladění Phi3 (po dobu 150 kroků, což můžete upravit) pomocí dat [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Sloučení vah LoRA adaptéru do základního modelu. Výsledkem bude jeden modelový artefakt ve formátu ONNX.
1. Model Builder optimalizuje model pro runtime ONNX *a* kvantizuje model do `int4`.

Pro spuštění workflow zadejte:

```bash
olive run --config phrase-classification.json
```

Po dokončení Olive bude váš optimalizovaný `int4` doladěný model Phi3 dostupný zde: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrace doladěného Phi3 do vaší aplikace 

Pro spuštění aplikace:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Tato odpověď by měla být jednoslovnou klasifikací fráze (Smutek/Radost/Strach/Překvapení).

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladových služeb využívajících umělou inteligenci. I když usilujeme o co nejvyšší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.