# Phi3 finomhangolása Olive segítségével

Ebben a példában az Olive segítségével:

1. Finomhangolsz egy LoRA adaptert, hogy kifejezéseket osztályozz Sad, Joy, Fear, Surprise kategóriákba.
2. Egyesíted az adapter súlyait az alapmodellbe.
3. Optimalizálod és kvantálod a modellt `int4` formátumba.

Megmutatjuk azt is, hogyan végezhetsz következtetést (inference) a finomhangolt modellen az ONNX Runtime (ORT) Generate API használatával.

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
Az [Olive konfigurációs fájl](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) egy *munkafolyamatot* tartalmaz a következő *lépésekkel*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Magas szinten ez a munkafolyamat a következőket hajtja végre:

1. Finomhangolja a Phi3 modellt (150 lépésben, amelyet módosíthatsz) a [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) adatainak felhasználásával.
2. Egyesíti a LoRA adapter súlyait az alapmodellbe. Ezáltal egyetlen ONNX formátumú modellarifaktot kapsz.
3. A Model Builder optimalizálja a modellt az ONNX runtime számára *és* kvantálja a modellt `int4` formátumba.

A munkafolyamat futtatásához használd a következő parancsot:

```bash
olive run --config phrase-classification.json
```

Amikor az Olive befejezte, az optimalizált `int4` finomhangolt Phi3 modell elérhető lesz itt: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 A finomhangolt Phi3 integrálása az alkalmazásodba 

Az alkalmazás futtatásához:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A válasz egyetlen szavas osztályozás lesz a kifejezésre (Sad/Joy/Fear/Surprise).

**Felelősség kizárása**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal készült fordítás. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.