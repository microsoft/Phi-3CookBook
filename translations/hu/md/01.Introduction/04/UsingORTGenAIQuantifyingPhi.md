# **Phi Család Kvantálása Generatív AI kiterjesztésekkel az onnxruntime-hoz**

## **Mi az onnxruntime generatív AI kiterjesztése?**

Ez a kiterjesztés segít generatív AI-t futtatni az ONNX Runtime segítségével ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Az ONNX modellekhez generatív AI ciklust biztosít, beleértve az ONNX Runtime általi következtetést, a logitok feldolgozását, a keresést és mintavételezést, valamint a KV cache kezelését. A fejlesztők hívhatják a magas szintű generate() metódust, vagy iteratívan futtathatják a modellt egy ciklusban, egyszerre egy token generálásával, és opcionálisan frissíthetik a generálási paramétereket a ciklus közben. Támogatja a mohó/sugárkeresést és a TopP, TopK mintavételezést token szekvenciák generálásához, valamint beépített logit feldolgozást, például ismétlési büntetéseket. Egyedi pontozási módszereket is könnyen hozzáadhatsz.

Alkalmazási szinten az onnxruntime generatív AI kiterjesztéseit használhatod alkalmazások építésére C++/C#/Python nyelveken. Modell szinten pedig használhatod finomhangolt modellek egyesítésére és kapcsolódó kvantitatív telepítési munkák elvégzésére.

## **Phi-3.5 kvantálása generatív AI kiterjesztésekkel az onnxruntime-hoz**

### **Támogatott modellek**

Az onnxruntime generatív AI kiterjesztései támogatják a Microsoft Phi, Google Gemma, Mistral és Meta LLaMA modellek kvantálási konverzióját.

### **Model Builder az onnxruntime generatív AI kiterjesztéseiben**

A Model Builder jelentősen felgyorsítja az optimalizált és kvantált ONNX modellek létrehozását, amelyek az ONNX Runtime generate() API-val futnak.

A Model Builder segítségével a modellt kvantálhatod INT4, INT8, FP16, FP32 formátumokra, és kombinálhatod különböző hardvergyorsítási módszerekkel, például CPU, CUDA, DirectML, Mobile stb.

A Model Builder használatához telepítened kell:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

A telepítés után a terminálból futtathatod a Model Builder szkriptet a modellformátum és kvantálási konverzió végrehajtásához.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Értsd meg a releváns paramétereket:

1. **model_name** Ez a Hugging Face-en található modell neve, például microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct stb. Lehet az a hely is, ahol a modellt tárolod.

2. **path_to_output_folder** A kvantált konverzió mentési útvonala.

3. **execution_provider** Különböző hardvergyorsítási támogatás, például cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** A modellt a Hugging Face-ről töltjük le, és helyileg gyorsítótárazzuk.

***Megjegyzés:*** 

## **Hogyan használd a Model Builder-t a Phi-3.5 kvantálásához**

A Model Builder mostantól támogatja az ONNX modellek kvantálását a Phi-3.5 Instruct és Phi-3.5-Vision modellekhez.

### **Phi-3.5-Instruct**

**Kvantált INT4 CPU-gyorsított konverzió**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Kvantált INT4 CUDA-gyorsított konverzió**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Állítsd be a környezetet a terminálban:

```bash

mkdir models

cd models 

```

2. Töltsd le a microsoft/Phi-3.5-vision-instruct modellt a models mappába:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Töltsd le az alábbi fájlokat a Phi-3.5-vision-instruct mappádba:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Töltsd le ezt a fájlt a models mappába:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Nyisd meg a terminált:

   ONNX támogatás konvertálása FP32 formátumra:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Megjegyzés:**

1. A Model Builder jelenleg a Phi-3.5-Instruct és Phi-3.5-Vision konverzióját támogatja, de nem támogatja a Phi-3.5-MoE-t.

2. Az ONNX kvantált modell használatához az onnxruntime generatív AI kiterjesztéseinek SDK-ján keresztül használhatod.

3. Törekednünk kell a felelősségteljesebb AI használatra, ezért a modell kvantálási konverziója után javasolt hatékonyabb eredménytesztelést végezni.

4. Az INT4 CPU modell kvantálásával éleszközökre is telepíthetjük, ami jobb alkalmazási forgatókönyveket biztosít. Ezért az INT4 köré építettük a Phi-3.5-Instruct modellt.

## **Források**

1. További információ az onnxruntime generatív AI kiterjesztéseiről:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime generatív AI kiterjesztések GitHub repó:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Felelősségkizárás**:  
Ezt a dokumentumot gépi AI fordítási szolgáltatások segítségével fordították le. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítás ajánlott. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.