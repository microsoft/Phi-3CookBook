# **Kvantisering av Phi-familien ved bruk av Generative AI-utvidelser for onnxruntime**

## **Hva er Generative AI-utvidelser for onnxruntime**

Disse utvidelsene hjelper deg med å kjøre generativ AI med ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). De gir en generativ AI-loop for ONNX-modeller, inkludert inferens med ONNX Runtime, behandling av logits, søk og sampling, samt håndtering av KV-cache. Utviklere kan bruke en høynivåmetode generate(), eller kjøre hver iterasjon av modellen i en loop som genererer én token om gangen, og eventuelt oppdatere generasjonsparametere inne i loopen. Den støtter greedy/beam search og TopP, TopK-sampling for å generere sekvenser av tokens, samt innebygd logits-behandling som repetisjonsstraff. Du kan også enkelt legge til egendefinert scoring.

På applikasjonsnivå kan du bruke Generative AI-utvidelser for onnxruntime til å bygge applikasjoner ved bruk av C++/C#/Python. På modellnivå kan du bruke dem til å slå sammen finjusterte modeller og utføre relatert kvantitativ distribusjonsarbeid.

## **Kvantisering av Phi-3.5 med Generative AI-utvidelser for onnxruntime**

### **Støttede modeller**

Generative AI-utvidelser for onnxruntime støtter kvantiseringskonvertering av Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Modellbygger i Generative AI-utvidelser for onnxruntime**

Modellbyggeren akselererer sterkt prosessen med å lage optimaliserte og kvantiserte ONNX-modeller som kjører med ONNX Runtime generate()-API-et.

Med Modellbyggeren kan du kvantisere modellen til INT4, INT8, FP16, FP32, og kombinere ulike maskinvareakselerasjonsmetoder som CPU, CUDA, DirectML, Mobile osv.

For å bruke Modellbyggeren må du installere

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Etter installasjon kan du kjøre Modellbygger-skriptet fra terminalen for å utføre modellformat- og kvantiseringskonvertering.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Forstå de relevante parameterne:

1. **model_name** Dette er modellen på Hugging Face, som for eksempel microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, osv. Det kan også være banen der du lagrer modellen.

2. **path_to_output_folder** Lagresti for kvantisert konvertering.

3. **execution_provider** Ulike maskinvareakselerasjonsstøtter, som CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Vi laster ned modellen fra Hugging Face og cacher den lokalt.

***Merk:***

## **Hvordan bruke Modellbyggeren til å kvantisere Phi-3.5**

Modellbyggeren støtter nå ONNX-modellkvantisering for Phi-3.5 Instruct og Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-akselerert konvertering til kvantisert INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-akselerert konvertering til kvantisert INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Sett opp miljø i terminalen:

```bash

mkdir models

cd models 

```

2. Last ned microsoft/Phi-3.5-vision-instruct til models-mappen.  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Last ned følgende filer til din Phi-3.5-vision-instruct-mappe:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Last ned denne filen til models-mappen:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå til terminalen:

    Konverter ONNX-støtte med FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Merk:**

1. Modellbyggeren støtter foreløpig konvertering av Phi-3.5-Instruct og Phi-3.5-Vision, men ikke Phi-3.5-MoE.

2. For å bruke ONNXs kvantiserte modell kan du bruke Generative AI-utvidelser for onnxruntime SDK.

3. Vi må ta hensyn til mer ansvarlig AI, så etter modellkvantiseringskonvertering anbefales det å gjennomføre mer effektiv testing av resultatene.

4. Ved å kvantisere CPU INT4-modellen kan vi distribuere den til Edge-enheter, noe som gir bedre bruksscenarier. Derfor har vi fullført Phi-3.5-Instruct rundt INT 4.

## **Ressurser**

1. Lær mer om Generative AI-utvidelser for onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-utvidelser for onnxruntime GitHub-repo:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.