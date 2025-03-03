## **Phi Family Quantization Using Generative AI Extensions for onnxruntime**

## **What Are Generative AI Extensions for onnxruntime?**

These extensions enable the use of generative AI with ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). They provide a generative AI loop for ONNX models, encompassing inference with ONNX Runtime, logits processing, search and sampling, and KV cache management. Developers can leverage a high-level `generate()` method or execute each model iteration in a loop to generate tokens step by step, with the flexibility to update generation parameters within the loop. The extensions support greedy/beam search, TopP, TopK sampling for token sequence generation, and built-in logits processing such as repetition penalties. Additionally, custom scoring can be easily integrated.

At the application level, Generative AI extensions for onnxruntime allow developers to build applications in C++/C#/Python. At the model level, they facilitate merging fine-tuned models and performing related quantitative deployment tasks.

## **Quantizing Phi-3.5 with Generative AI Extensions for onnxruntime**

### **Supported Models**

Generative AI extensions for onnxruntime support quantization for Microsoft Phi, Google Gemma, Mistral, and Meta LLaMA.

### **Model Builder in Generative AI Extensions for onnxruntime**

The Model Builder simplifies and accelerates the creation of optimized and quantized ONNX models compatible with the ONNX Runtime `generate()` API.

With Model Builder, you can quantize models to INT4, INT8, FP16, FP32, and combine various hardware acceleration methods such as CPU, CUDA, DirectML, Mobile, etc.

To use Model Builder, you need to install:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

After installation, you can execute the Model Builder script in the terminal to convert model formats and apply quantization.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

### **Understanding Key Parameters**

1. **model_name**: The model's identifier on Hugging Face, such as `microsoft/Phi-3.5-mini-instruct` or `microsoft/Phi-3.5-vision-instruct`. Alternatively, this can be the local path where the model is stored.

2. **path_to_output_folder**: The directory where the quantized model will be saved.

3. **execution_provider**: Specifies the hardware acceleration to be used, such as CPU, CUDA, or DirectML.

4. **cache_dir_to_save_hf_files**: The directory where models downloaded from Hugging Face will be cached locally.

***Note:***

## **How to Use Model Builder to Quantize Phi-3.5**

The Model Builder now supports ONNX model quantization for Phi-3.5 Instruct and Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-Accelerated Quantization to INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-Accelerated Quantization to INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Set up the environment in the terminal:

```bash

mkdir models

cd models 

```

2. Download the `microsoft/Phi-3.5-vision-instruct` model to the `models` folder:  
   [https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download the following files to your `Phi-3.5-vision-instruct` folder:

   - [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

   - [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

   - [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Download this file to the `models` folder:  
   [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Open the terminal and convert ONNX support to FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Note:**

1. The Model Builder currently supports Phi-3.5-Instruct and Phi-3.5-Vision but does not support Phi-3.5-MoE.

2. You can utilize ONNX's quantized models through the Generative AI extensions for onnxruntime SDK.

3. Responsible AI considerations are crucial. After quantizing a model, it is recommended to conduct comprehensive testing to validate results.

4. By quantizing the CPU INT4 model, deployment on edge devices becomes feasible, offering better application scenarios. Therefore, Phi-3.5-Instruct has been prioritized for INT4 quantization.

## **Resources**

1. Learn more about Generative AI extensions for onnxruntime:  
   [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Explore the Generative AI extensions for onnxruntime GitHub repository:  
   [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

It seems you are asking for a translation into "mo." Could you clarify what "mo" refers to? For instance, is it a specific language or abbreviation? Common possibilities might include Mongolian, Maori, or something else. Let me know so I can assist you accurately!