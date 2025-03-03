# **Kvantifiera Phi-familjen med Generative AI-tillägg för onnxruntime**

## **Vad är Generative AI-tillägg för onnxruntime**

Dessa tillägg hjälper dig att köra generativ AI med ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Det tillhandahåller en generativ AI-loop för ONNX-modeller, inklusive inferens med ONNX Runtime, bearbetning av logits, sökning och sampling samt hantering av KV-cache. Utvecklare kan antingen använda en hög nivå av generate()-metoden eller köra varje iteration av modellen i en loop, generera en token i taget och eventuellt uppdatera genereringsparametrarna inuti loopen. Det har stöd för girig/beam-sökning samt TopP- och TopK-sampling för att generera sekvenser av tokens och inbyggd logitsbearbetning som exempelvis repetitionsstraff. Du kan också enkelt lägga till egen poängsättning.

På applikationsnivå kan du använda Generative AI-tillägg för onnxruntime för att bygga applikationer med C++/C#/Python. På modellnivå kan du använda det för att slå samman finjusterade modeller och utföra relaterat kvantitativt distributionsarbete.

## **Kvantifiera Phi-3.5 med Generative AI-tillägg för onnxruntime**

### **Stödda modeller**

Generative AI-tillägg för onnxruntime stödjer kvantiseringskonvertering av Microsoft Phi, Google Gemma, Mistral och Meta LLaMA.

### **Model Builder i Generative AI-tillägg för onnxruntime**

Model Builder påskyndar processen att skapa optimerade och kvantiserade ONNX-modeller som körs med ONNX Runtime generate()-API.

Med hjälp av Model Builder kan du kvantifiera modellen till INT4, INT8, FP16, FP32 och kombinera olika hårdvaruaccelerationsmetoder som CPU, CUDA, DirectML, Mobile, etc.

För att använda Model Builder behöver du installera:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Efter installationen kan du köra Model Builder-skriptet från terminalen för att utföra modellformat- och kvantiseringskonvertering.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Förstå de relevanta parametrarna:

1. **model_name** Detta är modellen på Hugging Face, exempelvis microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Det kan också vara sökvägen där du lagrar modellen.

2. **path_to_output_folder** Sökväg där den kvantiserade modellen sparas.

3. **execution_provider** Stöd för olika hårdvaruaccelerationer, exempelvis cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Vi laddar ner modellen från Hugging Face och cachelagrar den lokalt.

***Obs:***

## **Hur man använder Model Builder för att kvantifiera Phi-3.5**

Model Builder stödjer nu ONNX-modellkvantifiering för Phi-3.5 Instruct och Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-accelererad konvertering av kvantiserad INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-accelererad konvertering av kvantiserad INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Ställ in miljön i terminalen:

```bash

mkdir models

cd models 

```

2. Ladda ner microsoft/Phi-3.5-vision-instruct till mappen models.  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Ladda ner följande filer till din Phi-3.5-vision-instruct-mapp:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Ladda ner följande fil till mappen models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå till terminalen:

    Konvertera ONNX-stöd till FP32.

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Obs:**

1. Model Builder stödjer för närvarande konvertering av Phi-3.5-Instruct och Phi-3.5-Vision, men inte Phi-3.5-MoE.

2. För att använda ONNX:s kvantiserade modell kan du använda den via Generative AI-tillägg för onnxruntime SDK.

3. Vi måste ta hänsyn till mer ansvarsfull AI, så efter modellkvantiseringskonverteringen rekommenderas att genomföra mer effektiv resultattestning.

4. Genom att kvantifiera CPU INT4-modellen kan vi distribuera den till Edge-enheter, vilket har bättre tillämpningsscenarier. Därför har vi färdigställt Phi-3.5-Instruct kring INT4.

## **Resurser**

1. Läs mer om Generative AI-tillägg för onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-tillägg för onnxruntime GitHub-repo:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.