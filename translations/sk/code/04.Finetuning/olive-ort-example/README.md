# Vyladenie Phi3 pomocou Olive

V tomto príklade použijete Olive na:

1. Vyladenie LoRA adaptéra na klasifikáciu fráz do kategórií Smútok, Radosť, Strach, Prekvapenie.
2. Zlúčenie váh adaptéra do základného modelu.
3. Optimalizáciu a kvantizáciu modelu do `int4`.

Tiež vám ukážeme, ako vykonať inferenciu s vyladeným modelom pomocou Generate API v ONNX Runtime (ORT).

> **⚠️ Na vyladenie budete potrebovať vhodné GPU - napríklad A10, V100, A100.**

## 💾 Inštalácia

Vytvorte nové virtuálne prostredie pre Python (napríklad pomocou `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Následne nainštalujte Olive a závislosti potrebné na workflow vyladenia:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Vyladenie Phi3 pomocou Olive
[Konfiguračný súbor Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) obsahuje *workflow* s nasledujúcimi *prechodmi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na vysokej úrovni tento workflow vykoná:

1. Vyladenie Phi3 (150 krokov, čo môžete upraviť) pomocou dát zo súboru [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Zlúčenie váh LoRA adaptéra do základného modelu. Výsledkom bude jeden modelový artefakt vo formáte ONNX.
3. Model Builder optimalizuje model pre ONNX runtime *a* kvantizuje model do `int4`.

Na spustenie workflow použite:

```bash
olive run --config phrase-classification.json
```

Po dokončení Olive bude váš optimalizovaný `int4` vyladený Phi3 model dostupný v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrácia vyladeného Phi3 do vašej aplikácie 

Na spustenie aplikácie použite:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpoveď by mala byť jednoslovná klasifikácia frázy (Smútok/Radosť/Strach/Prekvapenie).

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Aj keď sa snažíme o presnosť, prosím, vezmite na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.