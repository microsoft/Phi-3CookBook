# **Kvantizacija Phi obitelji pomoću proširenja Generative AI za onnxruntime**

## **Što su proširenja Generative AI za onnxruntime**

Ova proširenja pomažu vam u pokretanju generativne umjetne inteligencije s ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ona pružaju petlju generativne AI za ONNX modele, uključujući izvođenje zaključaka s ONNX Runtimeom, obradu logita, pretraživanje i uzorkovanje te upravljanje KV cacheom. Programeri mogu koristiti visoko razinu metodu generate() ili pokretati svaku iteraciju modela u petlji, generirajući jedan token odjednom, s mogućnošću ažuriranja parametara generiranja unutar petlje. Podržani su greedy/beam search i TopP, TopK uzorkovanje za generiranje sekvenci tokena te ugrađena obrada logita poput kazni za ponavljanje. Također je jednostavno dodati prilagođeno bodovanje.

Na razini aplikacije, možete koristiti proširenja Generative AI za onnxruntime kako biste izgradili aplikacije koristeći C++/C#/Python. Na razini modela, možete ih koristiti za spajanje fino podešenih modela i provođenje kvantitativnog rada na implementaciji.

## **Kvantizacija Phi-3.5 pomoću proširenja Generative AI za onnxruntime**

### **Podržani modeli**

Proširenja Generative AI za onnxruntime podržavaju konverziju kvantizacije za Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder u proširenjima Generative AI za onnxruntime**

Model Builder značajno ubrzava stvaranje optimiziranih i kvantiziranih ONNX modela koji rade s ONNX Runtime generate() API-jem.

Pomoću Model Buildera možete kvantizirati model na INT4, INT8, FP16, FP32 i kombinirati različite metode ubrzanja hardvera poput CPU, CUDA, DirectML, Mobile itd.

Za korištenje Model Buildera trebate instalirati:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Nakon instalacije, možete pokrenuti skriptu Model Buildera iz terminala za izvođenje konverzije formata modela i kvantizacije.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Razumijevanje relevantnih parametara:

1. **model_name** Ovo je model na Hugging Faceu, poput microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct itd. Također može biti i putanja gdje pohranjujete model.

2. **path_to_output_folder** Put za spremanje kvantizirane konverzije.

3. **execution_provider** Podrška za različita hardverska ubrzanja, poput cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Preuzimamo model s Hugging Facea i lokalno ga predmemoriramo.

***Napomena：***

## **Kako koristiti Model Builder za kvantizaciju Phi-3.5**

Model Builder sada podržava kvantizaciju ONNX modela za Phi-3.5 Instruct i Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-akcelerirana konverzija kvantiziranog INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-akcelerirana konverzija kvantiziranog INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Postavite okruženje u terminalu:

```bash

mkdir models

cd models 

```

2. Preuzmite microsoft/Phi-3.5-vision-instruct u mapu models:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Preuzmite ove datoteke u svoju mapu Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Preuzmite ovu datoteku u mapu models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Idite u terminal:

    Konvertirajte ONNX podršku s FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Napomena：**

1. Model Builder trenutno podržava konverziju Phi-3.5-Instruct i Phi-3.5-Vision, ali ne i Phi-3.5-MoE.

2. Za korištenje kvantiziranog modela ONNX-a, možete ga koristiti kroz SDK proširenja Generative AI za onnxruntime.

3. Trebamo uzeti u obzir odgovorniju umjetnu inteligenciju, pa se nakon kvantizacije modela preporučuje provesti učinkovitije testiranje rezultata.

4. Kvantizacijom CPU INT4 modela možemo ga implementirati na Edge uređaje, što ima bolje scenarije primjene, pa smo završili Phi-3.5-Instruct s fokusom na INT4.

## **Resursi**

1. Saznajte više o proširenjima Generative AI za onnxruntime: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub repozitorij proširenja Generative AI za onnxruntime: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prevođenja. Iako nastojimo osigurati točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.