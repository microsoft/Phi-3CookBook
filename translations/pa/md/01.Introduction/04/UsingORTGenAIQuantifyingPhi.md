# **Generative AI ਦੀ ਵਰਤੋਂ ਨਾਲ Phi ਪਰਿਵਾਰ ਨੂੰ Quantize ਕਰਨਾ**

## **Generative AI ਲਈ onnxruntime ਐਕਸਟੈਂਸ਼ਨ ਕੀ ਹਨ**

ਇਹ ਐਕਸਟੈਂਸ਼ਨ ਤੁਹਾਨੂੰ ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) ਨਾਲ ਜਨਰੇਟਿਵ AI ਚਲਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ। ਇਹ ONNX ਮਾਡਲਾਂ ਲਈ ਜਨਰੇਟਿਵ AI ਲੂਪ ਮੁਹੱਈਆ ਕਰਦੀਆਂ ਹਨ, ਜਿਸ ਵਿੱਚ ONNX Runtime ਨਾਲ ਇਨਫਰੈਂਸ, logits ਪ੍ਰੋਸੈਸਿੰਗ, ਖੋਜ ਅਤੇ ਸੈਂਪਲਿੰਗ, ਅਤੇ KV ਕੈਸ਼ ਪ੍ਰਬੰਧਨ ਸ਼ਾਮਲ ਹਨ। ਡਿਵੈਲਪਰ ਇੱਕ ਉੱਚ ਪੱਧਰੀ generate() ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਨ ਜਾਂ ਮਾਡਲ ਦੇ ਹਰ ਇਟਰੇਸ਼ਨ ਨੂੰ ਇੱਕ ਲੂਪ ਵਿੱਚ ਚਲਾ ਸਕਦੇ ਹਨ, ਇੱਕ ਸਮੇਂ ਵਿੱਚ ਇੱਕ ਟੋਕਨ ਤਿਆਰ ਕਰਦੇ ਹੋਏ, ਅਤੇ ਲੂਪ ਦੇ ਅੰਦਰ ਜਨਰੇਸ਼ਨ ਪੈਰਾਮੀਟਰ ਨੂੰ ਇੱਛਾ ਅਨੁਸਾਰ ਅੱਪਡੇਟ ਕਰ ਸਕਦੇ ਹਨ। ਇਹ ਗ੍ਰੀਡੀ/ਬੀਮ ਸਾਰਚ ਅਤੇ TopP, TopK ਸੈਂਪਲਿੰਗ ਲਈ ਸਪੋਰਟ ਕਰਦਾ ਹੈ, ਜੋ ਕਿ ਟੋਕਨ ਸੀਕਵੰਸ ਤਿਆਰ ਕਰਨ ਲਈ ਹੈ, ਅਤੇ ਦੁਹਰਾਈ ਗਈ ਦੰਡਾਂ ਵਰਗੇ ਲੌਜਿਟਸ ਪ੍ਰੋਸੈਸਿੰਗ ਬਿਲਟ-ਇਨ ਹਨ। ਤੁਸੀਂ ਆਸਾਨੀ ਨਾਲ ਕਸਟਮ ਸਕੋਰਿੰਗ ਵੀ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ।

ਐਪਲੀਕੇਸ਼ਨ ਪੱਧਰ 'ਤੇ, ਤੁਸੀਂ Generative AI ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ C++/C#/Python ਦੇ ਨਾਲ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾ ਸਕਦੇ ਹੋ। ਮਾਡਲ ਪੱਧਰ 'ਤੇ, ਤੁਸੀਂ ਇਸ ਦੀ ਵਰਤੋਂ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲਾਂ ਨੂੰ ਮਰਜ ਕਰਨ ਅਤੇ ਸੰਬੰਧਤ ਮਾਤਰਾਤਮਕ ਤੈਨਾਤੀ ਕੰਮ ਕਰਨ ਲਈ ਕਰ ਸਕਦੇ ਹੋ।

## **Generative AI ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 ਨੂੰ Quantize ਕਰਨਾ**

### **ਸਪੋਰਟ ਕੀਤੇ ਮਾਡਲ**

Generative AI ਐਕਸਟੈਂਸ਼ਨ Microsoft Phi, Google Gemma, Mistral, Meta LLaMA ਦੇ ਮਾਡਲਾਂ ਦੇ quantization ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਪੋਰਟ ਕਰਦੇ ਹਨ।

### **Generative AI ਐਕਸਟੈਂਸ਼ਨ ਵਿੱਚ ਮਾਡਲ ਬਿਲਡਰ**

ਮਾਡਲ ਬਿਲਡਰ ONNX Runtime ਦੇ generate() API ਨਾਲ ਚਲਣ ਵਾਲੇ optimized ਅਤੇ quantized ONNX ਮਾਡਲ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਬਹੁਤ ਤੇਜ਼ ਕਰਦਾ ਹੈ।

ਮਾਡਲ ਬਿਲਡਰ ਰਾਹੀਂ, ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ INT4, INT8, FP16, FP32 ਵਿੱਚ quantize ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ CPU, CUDA, DirectML, Mobile ਆਦਿ ਵਰਗੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਸ਼ਨ ਤਰੀਕਿਆਂ ਨੂੰ ਮਿਲਾ ਸਕਦੇ ਹੋ।

ਮਾਡਲ ਬਿਲਡਰ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਤੁਹਾਨੂੰ ਇਹ ਇੰਸਟਾਲ ਕਰਨਾ ਪਵੇਗਾ:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ਇੰਸਟਾਲੇਸ਼ਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਟਰਮਿਨਲ ਤੋਂ ਮਾਡਲ ਬਿਲਡਰ ਸਕ੍ਰਿਪਟ ਚਲਾ ਕੇ ਮਾਡਲ ਫਾਰਮੈਟ ਅਤੇ quantization ਕਨਵਰਜ਼ਨ ਕਰ ਸਕਦੇ ਹੋ।

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

ਸੰਬੰਧਤ ਪੈਰਾਮੀਟਰ ਸਮਝੋ:

1. **model_name** ਇਹ Hugging Face 'ਤੇ ਮਾਡਲ ਹੈ, ਜਿਵੇਂ microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct ਆਦਿ। ਇਹ ਉਹ ਪਾਥ ਵੀ ਹੋ ਸਕਦਾ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ ਮਾਡਲ ਸਟੋਰ ਕੀਤਾ ਹੈ।

2. **path_to_output_folder** Quantized ਕਨਵਰਜ਼ਨ ਸੇਵ ਕਰਨ ਦਾ ਪਾਥ।

3. **execution_provider** ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਸ਼ਨ ਸਪੋਰਟ, ਜਿਵੇਂ ਕਿ cpu, cuda, DirectML।

4. **cache_dir_to_save_hf_files** ਅਸੀਂ Hugging Face ਤੋਂ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਲੋਕਲ ਸਟੋਰ ਕਰਦੇ ਹਾਂ।

***ਨੋਟ:*** 

## **ਮਾਡਲ ਬਿਲਡਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 ਨੂੰ Quantize ਕਰਨ ਦਾ ਤਰੀਕਾ**

ਮਾਡਲ ਬਿਲਡਰ ਹੁਣ Phi-3.5 Instruct ਅਤੇ Phi-3.5-Vision ਲਈ ONNX ਮਾਡਲ quantization ਸਪੋਰਟ ਕਰਦਾ ਹੈ।

### **Phi-3.5-Instruct**

**Quantized INT 4 ਲਈ CPU ਐਕਸਲੇਰੇਸ਼ਨ ਕਨਵਰਜ਼ਨ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Quantized INT 4 ਲਈ CUDA ਐਕਸਲੇਰੇਸ਼ਨ ਕਨਵਰਜ਼ਨ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ਟਰਮਿਨਲ ਵਿੱਚ ਐਨਵਾਇਰਨਮੈਂਟ ਸੈਟ ਕਰੋ।

```bash

mkdir models

cd models 

```

2. ਮਾਡਲ ਫੋਲਡਰ ਵਿੱਚ microsoft/Phi-3.5-vision-instruct ਡਾਊਨਲੋਡ ਕਰੋ।  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਫਾਈਲਾਂ ਆਪਣੇ Phi-3.5-vision-instruct ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ਇਹ ਫਾਈਲ ਮਾਡਲ ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ਟਰਮਿਨਲ 'ਚ ਜਾਓ।  

    FP32 ਸਪੋਰਟ ਲਈ ONNX ਵਿੱਚ ਕਨਵਰਟ ਕਰੋ।

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ਨੋਟ:**

1. ਮਾਡਲ ਬਿਲਡਰ ਇਸ ਸਮੇਂ Phi-3.5-Instruct ਅਤੇ Phi-3.5-Vision ਦੇ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਪੋਰਟ ਕਰਦਾ ਹੈ, ਪਰ Phi-3.5-MoE ਨੂੰ ਨਹੀਂ।

2. ONNX ਦੇ quantized ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ, ਤੁਸੀਂ Generative AI ਐਕਸਟੈਂਸ਼ਨ SDK ਰਾਹੀਂ ਇਸਨੂੰ ਵਰਤ ਸਕਦੇ ਹੋ।

3. ਜ਼ਿੰਮੇਵਾਰ AI ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਮਾਡਲ quantization ਕਨਵਰਜ਼ਨ ਤੋਂ ਬਾਅਦ, ਵਧੇਰੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਨਤੀਜਿਆਂ ਦੀ ਜਾਂਚ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

4. CPU INT4 ਮਾਡਲ ਨੂੰ quantize ਕਰਕੇ, ਅਸੀਂ ਇਸਨੂੰ Edge Device 'ਤੇ ਤੈਨਾਤ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਸ ਨਾਲ ਬਿਹਤਰ ਐਪਲੀਕੇਸ਼ਨ ਸਥਿਤੀਆਂ ਪ੍ਰਾਪਤ ਹੁੰਦੀਆਂ ਹਨ। ਇਸ ਲਈ, ਅਸੀਂ Phi-3.5-Instruct ਲਈ INT 4 ਦੇ ਆਸਪਾਸ ਕੰਮ ਪੂਰਾ ਕੀਤਾ ਹੈ।

## **ਸਰੋਤ**

1. Generative AI ਐਕਸਟੈਂਸ਼ਨ ਬਾਰੇ ਹੋਰ ਸਿੱਖੋ: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI ਐਕਸਟੈਂਸ਼ਨ ਲਈ GitHub ਰਿਪੋ: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤਰ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਈਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।