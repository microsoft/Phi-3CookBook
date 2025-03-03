# Doladenie Phi3 pomocou Olive

V tomto príklade použijete Olive na:

1. Doladenie LoRA adaptéra na klasifikáciu fráz do kategórií Smútok, Radosť, Strach, Prekvapenie.
2. Zlúčenie váh adaptéra do základného modelu.
3. Optimalizáciu a kvantizáciu modelu do `int4`.

Taktiež vám ukážeme, ako vykonať inferenciu doladeného modelu pomocou ONNX Runtime (ORT) Generate API.

> **⚠️ Na doladenie budete potrebovať vhodné GPU - napríklad A10, V100, A100.**

## 💾 Inštalácia

Vytvorte nové virtuálne prostredie Pythonu (napríklad pomocou `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Následne nainštalujte Olive a závislosti pre doladiaci workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Doladenie Phi3 pomocou Olive
[Konfiguračný súbor Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) obsahuje *workflow* s nasledujúcimi *passmi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na vysokej úrovni tento workflow vykoná:

1. Doladenie Phi3 (počas 150 krokov, čo môžete upraviť) pomocou dát [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Zlúčenie váh LoRA adaptéra do základného modelu. Výsledkom bude jeden modelový artefakt vo formáte ONNX.
3. Model Builder optimalizuje model pre ONNX runtime *a* kvantizuje model do `int4`.

Na spustenie workflowu vykonajte:

```bash
olive run --config phrase-classification.json
```

Po dokončení Olive bude váš optimalizovaný `int4` doladený Phi3 model dostupný v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrácia doladeného Phi3 do vašej aplikácie 

Na spustenie aplikácie:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Táto odpoveď by mala byť jednoslovná klasifikácia frázy (Smútok/Radosť/Strach/Prekvapenie).

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladateľských služieb založených na umelej inteligencii. Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.