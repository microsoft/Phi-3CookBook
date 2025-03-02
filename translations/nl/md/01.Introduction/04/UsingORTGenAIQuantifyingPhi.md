# **Het kwantiseren van de Phi-familie met behulp van Generative AI-extensies voor onnxruntime**

## **Wat zijn Generative AI-extensies voor onnxruntime**

Deze extensies helpen je om generatieve AI te draaien met ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Het biedt de generatieve AI-loop voor ONNX-modellen, inclusief inferentie met ONNX Runtime, logitsverwerking, zoek- en samplingmethoden en KV-cachebeheer. Ontwikkelaars kunnen een hoog niveau generate()-methode aanroepen of elke iteratie van het model in een loop uitvoeren, waarbij één token per keer wordt gegenereerd, en optioneel generatieparameters binnen de loop worden bijgewerkt. Het ondersteunt greedy/beam search en TopP-, TopK-sampling om tokenreeksen te genereren, evenals ingebouwde logitsverwerking zoals herhalingsstraffen. Je kunt ook eenvoudig aangepaste scoring toevoegen.

Op applicatieniveau kun je Generative AI-extensies voor onnxruntime gebruiken om applicaties te bouwen met C++/C#/Python. Op modelniveau kun je het gebruiken om fijn afgestemde modellen samen te voegen en gerelateerd kwantitatief implementatiewerk uit te voeren.

## **Phi-3.5 kwantiseren met Generative AI-extensies voor onnxruntime**

### **Ondersteunde modellen**

Generative AI-extensies voor onnxruntime ondersteunen kwantisatieconversie van Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder in Generative AI-extensies voor onnxruntime**

De Model Builder versnelt aanzienlijk het creëren van geoptimaliseerde en gekwantiseerde ONNX-modellen die werken met de ONNX Runtime generate()-API.

Met Model Builder kun je het model kwantiseren naar INT4, INT8, FP16, FP32 en verschillende hardwareversnellingsmethoden combineren, zoals CPU, CUDA, DirectML, Mobile, enz.

Om Model Builder te gebruiken, moet je het volgende installeren:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Na installatie kun je het Model Builder-script uitvoeren vanuit de terminal om modelconversie en kwantisatie uit te voeren.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Begrijp de relevante parameters:

1. **model_name** Dit is het model op Hugging Face, zoals microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, enz. Het kan ook het pad zijn waar je het model opslaat.

2. **path_to_output_folder** Opslagpad voor de gekwantiseerde conversie.

3. **execution_provider** Ondersteuning voor verschillende hardwareversnelling, zoals cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** We downloaden het model van Hugging Face en cachen het lokaal.

***Opmerking:***

## **Hoe Model Builder te gebruiken om Phi-3.5 te kwantiseren**

Model Builder ondersteunt nu ONNX-modelkwantisatie voor Phi-3.5 Instruct en Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-versnelde conversie naar gekwantiseerde INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-versnelde conversie naar gekwantiseerde INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Stel de omgeving in via de terminal.

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct in de models-map.  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download deze bestanden naar je Phi-3.5-vision-instruct-map:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Download dit bestand naar de models-map:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ga naar de terminal.

    Converteer ONNX-ondersteuning met FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Opmerking:**

1. Model Builder ondersteunt momenteel de conversie van Phi-3.5-Instruct en Phi-3.5-Vision, maar niet Phi-3.5-MoE.

2. Om het gekwantiseerde model van ONNX te gebruiken, kun je het gebruiken via de Generative AI-extensies voor onnxruntime SDK.

3. We moeten meer rekening houden met verantwoorde AI, dus na de modelkwantisatieconversie wordt aanbevolen om meer effectieve resultaattesten uit te voeren.

4. Door het CPU INT4-model te kwantiseren, kunnen we het inzetten op Edge Devices, wat betere toepassingsscenario's biedt. Daarom hebben we Phi-3.5-Instruct rondom INT 4 voltooid.

## **Bronnen**

1. Meer informatie over Generative AI-extensies voor onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-extensies voor onnxruntime GitHub-repository:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.