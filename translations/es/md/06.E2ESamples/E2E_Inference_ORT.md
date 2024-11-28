# **Inferencia de tus modelos ajustados**

Después del ajuste fino, puedes acceder al nuevo modelo a través de la referencia, que se implementa aquí usando ONNX Runtime GenAI.

## **Instalar ORT GenAI SDK**

**Notas** - Por favor, instala CUDA 12.1 primero, si no sabes cómo hacerlo, por favor lee esta guía [https://developer.nvidia.com/cuda-12-1-0-download-archive](https://developer.nvidia.com/cuda-12-1-0-download-archive)

después de terminar con cuda, por favor instala onnxruntime genai sdk con cuda

```bash

pip install numpy

pip install onnxruntime-genai-cuda --pre --index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-genai/pypi/simple/


```

## **Modelo de Inferencia**

```python

import onnxruntime_genai as og

model = og.Model('Your onnx model folder location')
tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

search_options = {"max_length": 1024,"temperature":0.3}

params = og.GeneratorParams(model)
params.try_use_cuda_graph_with_max_batch_size(1)
params.set_search_options(**search_options)

prompt = "prompt = "<|user|>Who are you not allowed to marry in the UK?<|end|><|assistant|>""
input_tokens = tokenizer.encode(prompt)
params.input_ids = input_tokens

generator = og.Generator(model, params)

while not generator.is_done():
                generator.compute_logits()
                generator.generate_next_token()

                new_token = generator.get_next_tokens()[0]
                print(tokenizer_stream.decode(new_token), end='', flush=True)


```

### **Probando tu resultado**

![result](../../../../translated_images/result.b9b025fc2577ad5e3fd97341dd6c1e858a83c3291a4ed5ad4dc4fbd80a575b67.es.png)

        **Descargo de responsabilidad**: 
        Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.