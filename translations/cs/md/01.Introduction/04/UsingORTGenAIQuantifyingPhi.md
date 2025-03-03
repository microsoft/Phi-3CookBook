# **Kvantizace rodiny Phi pomocí rozšíření Generative AI pro onnxruntime**

## **Co jsou rozšíření Generative AI pro onnxruntime**

Tato rozšíření vám umožní spouštět generativní AI s ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Poskytují generativní AI smyčku pro ONNX modely, včetně inferencí s ONNX Runtime, zpracování logitů, hledání a vzorkování a správu KV cache. Vývojáři mohou volat vysoce úrovňovou metodu generate(), nebo spouštět každou iteraci modelu v cyklu, generovat jeden token po druhém a volitelně upravovat parametry generování uvnitř cyklu. Podporuje metody jako greedy/beam search, TopP a TopK vzorkování pro generování sekvencí tokenů, a zabudované zpracování logitů, jako jsou penalizace opakování. Také snadno můžete přidat vlastní skórování.

Na aplikační úrovni můžete využít rozšíření Generative AI pro onnxruntime k vytváření aplikací pomocí C++/C#/Python. Na úrovni modelu je můžete použít k slučování jemně doladěných modelů a provádění souvisejících kvantitativních implementačních úloh.

## **Kvantizace Phi-3.5 pomocí rozšíření Generative AI pro onnxruntime**

### **Podporované modely**

Rozšíření Generative AI pro onnxruntime podporují kvantizační převody modelů Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder v rozšířeních Generative AI pro onnxruntime**

Model Builder výrazně urychluje vytváření optimalizovaných a kvantizovaných ONNX modelů, které fungují s API generate() ONNX Runtime.

Prostřednictvím Model Builderu můžete kvantizovat model na INT4, INT8, FP16, FP32 a kombinovat různé metody hardwarové akcelerace, jako jsou CPU, CUDA, DirectML, Mobile atd.

K použití Model Builderu je třeba nainstalovat:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po instalaci můžete spustit skript Model Builder z terminálu a provést převod formátu modelu a kvantizaci.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Vysvětlení příslušných parametrů:

1. **model_name** Toto je model na Hugging Face, například microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct atd. Může to být také cesta, kde máte model uložený.

2. **path_to_output_folder** Cesta, kam se uloží kvantizovaný převod.

3. **execution_provider** Podpora různých hardwarových akcelerací, například cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Stahujeme model z Hugging Face a ukládáme ho lokálně do mezipaměti.

***Poznámka:***

## **Jak používat Model Builder ke kvantizaci Phi-3.5**

Model Builder nyní podporuje kvantizaci ONNX modelů Phi-3.5 Instruct a Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Kvantizace INT4 akcelerovaná CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Kvantizace INT4 akcelerovaná CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nastavte prostředí v terminálu:

```bash

mkdir models

cd models 

```

2. Stáhněte microsoft/Phi-3.5-vision-instruct do složky models:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Stáhněte následující soubory do složky Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Stáhněte tento soubor do složky models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Přejděte do terminálu:

   Převod na ONNX s podporou FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Poznámka:**

1. Model Builder aktuálně podporuje převod Phi-3.5-Instruct a Phi-3.5-Vision, ale ne Phi-3.5-MoE.

2. Pro použití kvantizovaného modelu ONNX jej můžete využít prostřednictvím SDK rozšíření Generative AI pro onnxruntime.

3. Je třeba zohlednit odpovědnější AI, proto se po kvantizačním převodu modelu doporučuje provést důkladnější testování výsledků.

4. Kvantizací modelu CPU INT4 jej můžeme nasadit na Edge zařízení, což přináší lepší aplikační scénáře, proto jsme dokončili kvantizaci Phi-3.5-Instruct na INT4.

## **Zdroje**

1. Více o rozšířeních Generative AI pro onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub repozitář rozšíření Generative AI pro onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Prohlášení:**  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nezodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.