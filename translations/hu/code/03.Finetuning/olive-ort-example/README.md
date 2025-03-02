# Phi3 finomhangolása Olive segítségével

Ebben a példában Olive segítségével a következőket fogod végrehajtani:

1. Egy LoRA adapter finomhangolása, amely mondatokat osztályoz Szomorúság, Öröm, Félelem, Meglepetés kategóriákba.
1. Az adapter súlyainak egyesítése az alapmodellel.
1. A modell optimalizálása és kvantálása `int4` formátumba.

Megmutatjuk azt is, hogyan végezhetsz következtetést a finomhangolt modellen az ONNX Runtime (ORT) Generate API segítségével.

> **⚠️ A finomhangoláshoz megfelelő GPU-ra lesz szükséged - például A10, V100, A100.**

## 💾 Telepítés

Hozz létre egy új Python virtuális környezetet (például `conda` használatával):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ezután telepítsd az Olive-ot és a finomhangolási munkafolyamathoz szükséges függőségeket:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Phi3 finomhangolása Olive segítségével

Az [Olive konfigurációs fájl](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) egy *munkafolyamatot* tartalmaz a következő *lépésekkel*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Magas szinten ez a munkafolyamat a következőket végzi el:

1. Phi3 finomhangolása (150 lépésben, amit módosíthatsz) a [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) adatok segítségével.
1. A LoRA adapter súlyainak egyesítése az alapmodellel. Ez egyetlen modellartifaktot eredményez ONNX formátumban.
1. A Model Builder optimalizálja a modellt az ONNX runtime számára, *és* kvantálja a modellt `int4` formátumba.

A munkafolyamat végrehajtásához futtasd:

```bash
olive run --config phrase-classification.json
```

Amikor Olive befejezi, az optimalizált `int4` finomhangolt Phi3 modell elérhető itt: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 A finomhangolt Phi3 integrálása az alkalmazásodba

Az alkalmazás futtatásához:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A válasz egyetlen szó lesz, amely a mondat osztályozását jelöli (Szomorúság/Öröm/Félelem/Meglepetés).

**Jogi nyilatkozat**:  
Ez a dokumentum gépi alapú mesterséges intelligencia fordítási szolgáltatásokkal készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.