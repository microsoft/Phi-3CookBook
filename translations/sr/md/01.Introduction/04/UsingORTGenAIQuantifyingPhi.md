# **Kvantizacija Phi porodice pomoću proširenja za generativnu AI u onnxruntime**

## **Šta su proširenja za generativnu AI u onnxruntime**

Ova proširenja omogućavaju pokretanje generativne AI sa ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ona pružaju generativnu AI petlju za ONNX modele, uključujući inferenciju sa ONNX Runtime, obradu logita, pretragu i uzorkovanje, kao i upravljanje KV kešom. Programeri mogu koristiti visokonivojsku metodu generate(), ili pokretati svaku iteraciju modela u petlji, generišući jedan token po iteraciji, uz mogućnost podešavanja parametara generacije unutar petlje. Podržava pretragu sa pohlepnim algoritmom/beam search, kao i TopP, TopK uzorkovanje za generisanje sekvenci tokena, uz ugrađenu obradu logita poput kazni za ponavljanje. Takođe, lako možete dodati prilagođeno bodovanje.

Na nivou aplikacije, možete koristiti proširenja za generativnu AI u onnxruntime za izgradnju aplikacija koristeći C++/C#/Python. Na nivou modela, možete ih koristiti za spajanje fino podešenih modela i izvođenje povezane kvantitativne implementacije.

## **Kvantizacija Phi-3.5 pomoću proširenja za generativnu AI u onnxruntime**

### **Podržani modeli**

Proširenja za generativnu AI u onnxruntime podržavaju konverziju kvantizacije za Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Konstruktor modela u proširenjima za generativnu AI u onnxruntime**

Konstruktor modela značajno ubrzava kreiranje optimizovanih i kvantizovanih ONNX modela koji rade sa ONNX Runtime generate() API-jem.

Pomoću konstruktora modela možete kvantizovati model na INT4, INT8, FP16, FP32 i kombinovati različite metode ubrzanja hardvera kao što su CPU, CUDA, DirectML, Mobile, itd.

Da biste koristili konstruktor modela, potrebno je da instalirate:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Nakon instalacije, možete pokrenuti skriptu konstruktora modela iz terminala za obavljanje konverzije formata i kvantizacije modela.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Razumevanje relevantnih parametara:

1. **model_name** Ovo je model na Hugging Face platformi, poput microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, itd. Takođe može biti i putanja gde čuvate model.

2. **path_to_output_folder** Putanja za čuvanje kvantizovane konverzije.

3. **execution_provider** Podrška za različita hardverska ubrzanja, kao što su cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Preuzimamo model sa Hugging Face platforme i keširamo ga lokalno.

***Napomena:***

## **Kako koristiti konstruktor modela za kvantizaciju Phi-3.5**

Konstruktor modela sada podržava ONNX kvantizaciju modela za Phi-3.5 Instruct i Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU ubrzana konverzija kvantizovanog INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ubrzana konverzija kvantizovanog INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Postavite okruženje u terminalu

```bash

mkdir models

cd models 

```

2. Preuzmite microsoft/Phi-3.5-vision-instruct u folder "models"  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Preuzmite sledeće fajlove u vaš Phi-3.5-vision-instruct folder:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Preuzmite ovaj fajl u folder "models":  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Otvorite terminal.

   Konvertujte ONNX podršku sa FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Napomena:**

1. Konstruktor modela trenutno podržava konverziju za Phi-3.5-Instruct i Phi-3.5-Vision, ali ne i za Phi-3.5-MoE.

2. Da biste koristili kvantizovani model ONNX-a, možete ga koristiti putem SDK-a za proširenja generativne AI u onnxruntime.

3. Potrebno je razmotriti odgovorniju upotrebu AI, pa se nakon konverzije kvantizacije modela preporučuje sprovođenje dodatnog testiranja rezultata.

4. Kvantizacijom CPU INT4 modela možemo ga implementirati na uređajima na ivici mreže, što pruža bolje scenarije primene. Zbog toga smo završili Phi-3.5-Instruct koristeći INT 4.

## **Resursi**

1. Saznajte više o proširenjima za generativnu AI u onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub repozitorijum za proširenja generativne AI u onnxruntime:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо тачности, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква неспоразумевања или погрешна тумачења настала коришћењем овог превода.