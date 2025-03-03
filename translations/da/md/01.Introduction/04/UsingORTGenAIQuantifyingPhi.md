# **Kvantisering af Phi-familien ved hjælp af Generative AI-udvidelser til onnxruntime**

## **Hvad er Generative AI-udvidelser til onnxruntime**

Disse udvidelser hjælper dig med at køre generativ AI med ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). De tilbyder den generative AI-løkke til ONNX-modeller, herunder inferens med ONNX Runtime, logits-behandling, søgning og sampling samt KV-cachehåndtering. Udviklere kan kalde en høj-niveau generate()-metode eller køre hver iteration af modellen i en løkke, hvor de genererer én token ad gangen og eventuelt opdaterer genereringsparametrene inde i løkken. Udvidelserne understøtter greedy/beam-søgning og TopP, TopK-sampling til at generere token-sekvenser samt indbygget logits-behandling som gentagelsesstraffe. Du kan også nemt tilføje brugerdefineret scoring.

På applikationsniveau kan du bruge Generative AI-udvidelser til onnxruntime til at bygge applikationer ved hjælp af C++/C#/Python. På modelliveau kan du bruge dem til at flette finjusterede modeller og udføre relateret kvantitativ implementeringsarbejde.

## **Kvantisering af Phi-3.5 med Generative AI-udvidelser til onnxruntime**

### **Understøttede modeller**

Generative AI-udvidelser til onnxruntime understøtter kvantiseringskonvertering af Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder i Generative AI-udvidelser til onnxruntime**

Model Builder fremskynder markant oprettelsen af optimerede og kvantiserede ONNX-modeller, der kører med ONNX Runtime generate()-API'en.

Med Model Builder kan du kvantisere modellen til INT4, INT8, FP16, FP32 og kombinere forskellige hardwareaccelerationsmetoder som CPU, CUDA, DirectML, Mobile osv.

For at bruge Model Builder skal du installere

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Efter installation kan du køre Model Builder-scriptet fra terminalen for at udføre modelkonvertering og kvantisering.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Forstå de relevante parametre:

1. **model_name** Dette er modellen på Hugging Face, som f.eks. microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct osv. Det kan også være stien, hvor du gemmer modellen.

2. **path_to_output_folder** Sti til lagring af kvantiseringskonverteringen.

3. **execution_provider** Understøttelse af forskellig hardwareacceleration, som f.eks. cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Vi downloader modellen fra Hugging Face og cacher den lokalt.

***Bemærk:***

## **Sådan bruges Model Builder til at kvantisere Phi-3.5**

Model Builder understøtter nu ONNX-modelkvantisering for Phi-3.5 Instruct og Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-accelereret konvertering til kvantiseret INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-accelereret konvertering til kvantiseret INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Opsæt miljø i terminalen

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct til models-mappen  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download venligst disse filer til din Phi-3.5-vision-instruct-mappe:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Download denne fil til models-mappen:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå til terminalen

   Konverter ONNX-understøttelse med FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Bemærk:**

1. Model Builder understøtter i øjeblikket konvertering af Phi-3.5-Instruct og Phi-3.5-Vision, men ikke Phi-3.5-MoE.

2. For at bruge ONNX's kvantiserede model kan du bruge den gennem Generative AI-udvidelser til onnxruntime SDK.

3. Vi skal tage højde for mere ansvarlig AI, så efter modelkvantiseringskonvertering anbefales det at gennemføre mere effektiv test af resultaterne.

4. Ved at kvantisere CPU INT4-modellen kan vi implementere den på Edge-enheder, hvilket giver bedre anvendelsesscenarier. Derfor har vi færdiggjort Phi-3.5-Instruct omkring INT4.

## **Ressourcer**

1. Læs mere om Generative AI-udvidelser til onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-udvidelser til onnxruntime GitHub-repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.