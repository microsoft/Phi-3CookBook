# **Cuantizarea familiei Phi folosind extensii Generative AI pentru onnxruntime**

## **Ce sunt extensiile Generative AI pentru onnxruntime**

Aceste extensii te ajută să rulezi AI generativ cu ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ele oferă un ciclu generativ AI pentru modelele ONNX, incluzând inferența cu ONNX Runtime, procesarea logit-urilor, căutarea și eșantionarea, precum și gestionarea cache-ului KV. Dezvoltatorii pot apela metoda de nivel înalt generate() sau pot rula fiecare iterație a modelului într-un ciclu, generând un token pe rând și, opțional, actualizând parametrii de generare în interiorul ciclului. Suportă căutarea greedy/beam și eșantionarea TopP, TopK pentru a genera secvențe de tokeni, precum și procesarea logit-urilor încorporată, cum ar fi penalizările pentru repetiție. De asemenea, poți adăuga cu ușurință scorări personalizate.

La nivel de aplicație, poți utiliza extensiile Generative AI pentru onnxruntime pentru a construi aplicații folosind C++/ C# / Python. La nivel de model, le poți folosi pentru a îmbina modele fine-tunate și pentru lucrări de implementare cantitativă aferente.

## **Cuantizarea Phi-3.5 cu extensii Generative AI pentru onnxruntime**

### **Modele suportate**

Extensiile Generative AI pentru onnxruntime suportă conversia de cuantizare a modelelor Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Constructorul de modele în extensiile Generative AI pentru onnxruntime**

Constructorul de modele accelerează semnificativ crearea de modele ONNX optimizate și cuantizate care rulează cu API-ul generate() al ONNX Runtime.

Prin intermediul Constructorului de modele, poți cuantiza modelul la INT4, INT8, FP16, FP32 și combina diferite metode de accelerare hardware, cum ar fi CPU, CUDA, DirectML, Mobile etc.

Pentru a utiliza Constructorul de modele, trebuie să instalezi

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

După instalare, poți rula scriptul Constructorului de modele din terminal pentru a efectua conversia formatului și cuantizarea modelului.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Înțelegerea parametrilor relevanți:

1. **model_name** Acesta este modelul de pe Hugging Face, cum ar fi microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct etc. Poate fi și calea unde ai stocat modelul.

2. **path_to_output_folder** Calea unde se salvează conversia cuantizată.

3. **execution_provider** Suport pentru diferite accelerări hardware, cum ar fi cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Descărcăm modelul de pe Hugging Face și îl salvăm local în cache.

***Notă:***

## **Cum se utilizează Constructorul de modele pentru cuantizarea Phi-3.5**

Constructorul de modele suportă acum cuantizarea modelelor ONNX pentru Phi-3.5 Instruct și Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversia cuantizată INT4 accelerată de CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversia cuantizată INT4 accelerată de CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configurează mediul în terminal

```bash

mkdir models

cd models 

```

2. Descarcă microsoft/Phi-3.5-vision-instruct în folderul models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Te rog să descarci aceste fișiere în folderul tău Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Descarcă acest fișier în folderul models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Accesează terminalul

   Convertește suportul ONNX cu FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Notă:**

1. Constructorul de modele suportă în prezent conversia pentru Phi-3.5-Instruct și Phi-3.5-Vision, dar nu pentru Phi-3.5-MoE.

2. Pentru a utiliza modelul cuantizat al ONNX, poți să-l accesezi prin SDK-ul extensiilor Generative AI pentru onnxruntime.

3. Trebuie să luăm în considerare un AI mai responsabil, așa că după conversia cuantizată a modelului, este recomandat să efectuezi teste mai eficiente ale rezultatelor.

4. Prin cuantizarea modelului CPU INT4, îl putem implementa pe dispozitive Edge, ceea ce oferă scenarii de aplicare mai bune, astfel încât am finalizat Phi-3.5-Instruct pentru INT4.

## **Resurse**

1. Află mai multe despre extensiile Generative AI pentru onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repozitoriu GitHub pentru extensiile Generative AI pentru onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Declinarea responsabilității**:  
Acest document a fost tradus utilizând servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa natală, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.