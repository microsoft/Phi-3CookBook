# **Quantizing Phi Family using Generative AI extensions for onnxruntime**

## **What's Generative AI extensions for onnxruntime**

This extensions help you to run generatice AI with ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). It provides the generative AI loop for ONNX models, including inference with ONNX Runtime, logits processing, search and sampling, and KV cache management. Developers can call a high level generate() method, or run each iteration of the model in a loop, generating one token at a time, and optionally updating generation parameters inside the loop.It has support for greedy/beam search and TopP, TopK sampling to generate token sequences and built-in logits processing like repetition penalties. You can also easily add custom scoring.

At the application level, you can use Generative AI extensions for onnxruntime to build applications using C++/ C# / Python. At the model level, you can use it to merge fine-tuned models and do related quantitative deployment work.


## **Quantizing Phi-3.5 with Generative AI extensions for onnxruntime**

### **Support Models**

Generative AI extensions for onnxruntime support quantization conversion of Microsoft Phi , Google Gemma, Mistral, Meta LLaMA。


### **Model Builder in Generative AI extensions for onnxruntime**

The model builder greatly accelerates creating optimized and quantized ONNX models that run with the ONNX Runtime generate() API.

Through Model Builder, you can quantize the model to INT4, INT8, FP16, FP32, and combine different hardware acceleration methods such as CPU, CUDA, DirectML, Mobile, etc.

To use Model Builder you need to install

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

After installation, you can run the Model Builder script from the terminal to perform model format and quantization conversion.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Understand the relevant parameters

1. **model_name** This is the  model on Hugging face, such as microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. It can also be the path where you store the model

2. **path_to_output_folder** Quantized conversion save path

3. **execution_provider** Different hardware acceleration support, such as cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** We download the model from Hugging face and cache it locally




***Note：*** <ul>Although Generative AI extensions for onnxruntime are in preview, they have been incorporated into Microsoft Olive, and you can also call Generative AI extensions for onnxruntime Model Builder functions through Microsoft Olive.</ul>

## **How to use Model Builder to quantizing Phi-3.5**

Model Builder now supports ONNX model quantization for Phi-3.5 Instruct and Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU accelerated conversion of quantized INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA accelerated conversion of quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Set environment in terminal

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct in models folder
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Please download these files to Your Phi-3.5-vision-instruct folder

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Download this file to models folder
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Go to terminal

    Convert ONNX support with FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Note：**

1. Model Builder currently supports the conversion of Phi-3.5-Instruct and Phi-3.5-Vision, but not Phi-3.5-MoE

2. To use ONNX's quantized model, you can use it through Generative AI extensions for onnxruntime SDK

3. We need to consider more responsible AI, so after the model quantization conversion, it is recommended to conduct more effective result testing

4. By quantizing the CPU INT4 model, we can deploy it to Edge Device, which has better application scenarios, so we have completed Phi-3.5-Instruct around INT 4


## **Resources**

1. Learn more about Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

