# **Kvantizácia Phi Family pomocou Generative AI rozšírení pre onnxruntime**

## **Čo sú Generative AI rozšírenia pre onnxruntime**

Tieto rozšírenia umožňujú spustiť generatívnu AI pomocou ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Poskytujú generatívnu AI slučku pre ONNX modely, vrátane inferencie s ONNX Runtime, spracovania logitov, vyhľadávania a samplovania, a správy KV cache. Vývojári môžu volať vysokú úroveň metódy generate(), alebo spúšťať každú iteráciu modelu v slučke, generovať jeden token naraz a voliteľne upravovať parametre generovania v rámci slučky. Podporuje greedy/beam vyhľadávanie a TopP, TopK samplovanie na generovanie sekvencií tokenov a zabudované spracovanie logitov, ako sú penalizácie opakovania. Môžete tiež jednoducho pridať vlastné skórovanie.

Na aplikačnej úrovni môžete použiť Generative AI rozšírenia pre onnxruntime na vytváranie aplikácií pomocou C++/C#/Python. Na úrovni modelu ich môžete použiť na zlúčenie jemne doladených modelov a vykonanie súvisiacich kvantitatívnych nasadzovacích úloh.

## **Kvantizácia Phi-3.5 pomocou Generative AI rozšírení pre onnxruntime**

### **Podporované modely**

Generative AI rozšírenia pre onnxruntime podporujú kvantizačnú konverziu modelov Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder v Generative AI rozšíreniach pre onnxruntime**

Model Builder výrazne urýchľuje vytváranie optimalizovaných a kvantizovaných ONNX modelov, ktoré bežia s ONNX Runtime generate() API.

Pomocou Model Builder môžete kvantizovať model na INT4, INT8, FP16, FP32 a kombinovať rôzne metódy akcelerácie hardvéru, ako sú CPU, CUDA, DirectML, Mobile, atď.

Na použitie Model Builder musíte nainštalovať

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po inštalácii môžete spustiť skript Model Builder z terminálu na vykonanie konverzie formátu a kvantizácie modelu.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Pochopte relevantné parametre:

1. **model_name** Toto je model na Hugging Face, napríklad microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, atď. Môže to byť aj cesta, kde máte model uložený.

2. **path_to_output_folder** Cesta na uloženie kvantizovanej konverzie.

3. **execution_provider** Podpora rôznych hardvérových akcelerácií, ako napríklad cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Model sťahujeme z Hugging Face a ukladáme ho lokálne do cache.

***Poznámka：***

## **Ako používať Model Builder na kvantizáciu Phi-3.5**

Model Builder teraz podporuje kvantizáciu ONNX modelu pre Phi-3.5 Instruct a Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Kvantizovaná INT4 konverzia akcelerovaná CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Kvantizovaná INT4 konverzia akcelerovaná CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nastavte prostredie v termináli

```bash

mkdir models

cd models 

```

2. Stiahnite microsoft/Phi-3.5-vision-instruct do priečinka models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Stiahnite tieto súbory do priečinka Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Stiahnite tento súbor do priečinka models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Prejdite do terminálu  

   Konvertujte ONNX podporu s FP32  

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Poznámka：**

1. Model Builder momentálne podporuje konverziu Phi-3.5-Instruct a Phi-3.5-Vision, ale nie Phi-3.5-MoE.

2. Na použitie kvantizovaného modelu ONNX ho môžete použiť prostredníctvom Generative AI rozšírení pre onnxruntime SDK.

3. Musíme zohľadniť zodpovednejšiu AI, preto sa po kvantizačnej konverzii modelu odporúča vykonať efektívnejšie testovanie výsledkov.

4. Kvantizáciou CPU INT4 modelu ho môžeme nasadiť na Edge zariadenia, ktoré majú lepšie aplikačné scenáre, preto sme dokončili Phi-3.5-Instruct pre INT4.

## **Zdroje**

1. Viac o Generative AI rozšíreniach pre onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI rozšírenia pre onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu založených na umelej inteligencii. Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.