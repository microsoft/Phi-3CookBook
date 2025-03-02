# **Kuantisha Familia ya Phi kwa kutumia viendelezi vya Generative AI vya onnxruntime**

## **Viendelezi vya Generative AI vya onnxruntime ni nini?**

Viendelezi hivi vinakusaidia kuendesha Generative AI kwa kutumia ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Vinatoa mchakato wa generative AI kwa mifano ya ONNX, ikijumuisha utabiri kwa kutumia ONNX Runtime, usindikaji wa logits, utafutaji na sampuli, na usimamizi wa KV cache. Watengenezaji wanaweza kutumia mbinu ya kiwango cha juu generate(), au kuendesha kila mzunguko wa mfano kwa njia ya kitanzi, wakizalisha tokeni moja kwa wakati, na kwa hiari kusasisha vigezo vya kizazi ndani ya kitanzi. Inasaidia utafutaji wa greedy/beam na sampuli za TopP, TopK ili kuzalisha mlolongo wa tokeni na ina usindikaji wa logits uliojengwa ndani kama vile adhabu za kurudia. Pia unaweza kuongeza alama maalum kwa urahisi.

Kwa ngazi ya maombi, unaweza kutumia viendelezi vya Generative AI vya onnxruntime kujenga maombi kwa kutumia C++/C#/Python. Kwa ngazi ya mfano, unaweza kutumia ili kuunganisha mifano iliyoboreshwa na kufanya kazi zinazohusiana na utekelezaji wa kiasi.

## **Kuantisha Phi-3.5 kwa kutumia viendelezi vya Generative AI vya onnxruntime**

### **Mifano Inayoungwa Mkono**

Viendelezi vya Generative AI vya onnxruntime vinaunga mkono ubadilishaji wa kuquantisha wa Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder katika Generative AI extensions for onnxruntime**

Model Builder inaharakisha sana uundaji wa mifano ya ONNX iliyoboreshwa na kuquantishwa ambayo inaendesha kwa kutumia API ya ONNX Runtime generate().

Kupitia Model Builder, unaweza kuquantisha mfano hadi INT4, INT8, FP16, FP32, na kuchanganya mbinu mbalimbali za kuongeza kasi ya vifaa kama vile CPU, CUDA, DirectML, Mobile, n.k.

Ili kutumia Model Builder unahitaji kusakinisha

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Baada ya usakinishaji, unaweza kuendesha script ya Model Builder kutoka terminal ili kufanya ubadilishaji wa muundo wa mfano na kuquantisha.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Elewa vigezo husika:

1. **model_name** Huu ni mfano kwenye Hugging Face, kama vile microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, n.k. Inaweza pia kuwa njia ambapo umehifadhi mfano.

2. **path_to_output_folder** Njia ya kuhifadhi ubadilishaji wa kuquantisha.

3. **execution_provider** Usaidizi wa kuongeza kasi ya vifaa tofauti, kama vile cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Tunapakua mfano kutoka Hugging Face na kuuhifadhi kwa muda kwenye kifaa cha ndani.

***Kumbuka:***

## **Jinsi ya kutumia Model Builder kuquantisha Phi-3.5**

Model Builder sasa inasaidia kuquantisha mifano ya ONNX ya Phi-3.5 Instruct na Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Ubadilishaji wa INT 4 ulioharakishwa na CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Ubadilishaji wa INT 4 ulioharakishwa na CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Weka mazingira kwenye terminal

```bash

mkdir models

cd models 

```

2. Pakua microsoft/Phi-3.5-vision-instruct kwenye folda ya mifano  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Tafadhali pakua faili hizi kwenye folda yako ya Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Pakua faili hii kwenye folda ya mifano  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Nenda kwenye terminal

    Badilisha ONNX ili kuunga mkono FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Kumbuka:**

1. Model Builder kwa sasa inasaidia ubadilishaji wa Phi-3.5-Instruct na Phi-3.5-Vision, lakini si Phi-3.5-MoE.

2. Ili kutumia mfano wa ONNX uliokuquantisha, unaweza kuutumia kupitia SDK ya Generative AI extensions for onnxruntime.

3. Tunapaswa kuzingatia AI inayowajibika zaidi, kwa hivyo baada ya ubadilishaji wa kuquantisha mfano, inashauriwa kufanya majaribio ya matokeo kwa ufanisi zaidi.

4. Kwa kuquantisha mfano wa CPU INT4, tunaweza kuutumia kwenye Vifaa vya Edge, ambavyo vina hali bora za matumizi, kwa hivyo tumekamilisha Phi-3.5-Instruct kwa INT 4.

## **Rasilimali**

1. Jifunze zaidi kuhusu viendelezi vya Generative AI vya onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Hifadhi ya GitHub ya Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za kimitambo zinazotumia AI. Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kimitambo zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za wataalamu wa tafsiri ya kibinadamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.