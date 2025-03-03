# **Cuantización de la familia Phi utilizando extensiones de IA generativa para onnxruntime**

## **¿Qué son las extensiones de IA generativa para onnxruntime?**

Estas extensiones te ayudan a ejecutar IA generativa con ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Proporcionan el bucle de IA generativa para modelos ONNX, incluyendo inferencia con ONNX Runtime, procesamiento de logits, búsqueda y muestreo, y gestión de caché KV. Los desarrolladores pueden llamar a un método de alto nivel generate(), o ejecutar cada iteración del modelo en un bucle, generando un token a la vez y, opcionalmente, actualizando los parámetros de generación dentro del bucle. Tiene soporte para búsqueda greedy/beam y muestreo TopP, TopK para generar secuencias de tokens, además de procesamiento integrado de logits como penalizaciones por repetición. También puedes añadir fácilmente puntuaciones personalizadas.

A nivel de aplicación, puedes usar las extensiones de IA generativa para onnxruntime para construir aplicaciones utilizando C++/ C# / Python. A nivel de modelo, puedes utilizarlas para fusionar modelos ajustados y realizar trabajos relacionados con el despliegue cuantitativo.


## **Cuantización de Phi-3.5 con extensiones de IA generativa para onnxruntime**

### **Modelos compatibles**

Las extensiones de IA generativa para onnxruntime admiten la conversión cuantitativa de Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder en extensiones de IA generativa para onnxruntime**

El Model Builder acelera enormemente la creación de modelos ONNX optimizados y cuantizados que funcionan con la API generate() de ONNX Runtime.

A través de Model Builder, puedes cuantizar el modelo a INT4, INT8, FP16, FP32, y combinar diferentes métodos de aceleración de hardware como CPU, CUDA, DirectML, Mobile, etc.

Para usar Model Builder necesitas instalar:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Después de la instalación, puedes ejecutar el script de Model Builder desde el terminal para realizar la conversión de formato y cuantización del modelo.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Entender los parámetros relevantes:

1. **model_name** Este es el modelo en Hugging Face, como microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. También puede ser la ruta donde almacenas el modelo.

2. **path_to_output_folder** Ruta de guardado de la conversión cuantizada.

3. **execution_provider** Soporte de aceleración de hardware, como cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Descargamos el modelo desde Hugging Face y lo almacenamos en caché localmente.

***Nota:***


## **Cómo usar Model Builder para cuantizar Phi-3.5**

Model Builder ahora admite la cuantización de modelos ONNX para Phi-3.5 Instruct y Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversión cuantizada INT 4 acelerada por CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversión cuantizada INT 4 acelerada por CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configura el entorno en el terminal.

```bash

mkdir models

cd models 

```

2. Descarga microsoft/Phi-3.5-vision-instruct en la carpeta de modelos.  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Descarga estos archivos en tu carpeta Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Descarga este archivo en la carpeta de modelos:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ve al terminal:

    Convierte a soporte ONNX con FP32.

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Nota:**

1. Model Builder actualmente admite la conversión de Phi-3.5-Instruct y Phi-3.5-Vision, pero no Phi-3.5-MoE.

2. Para usar el modelo cuantizado de ONNX, puedes hacerlo a través del SDK de extensiones de IA generativa para onnxruntime.

3. Necesitamos considerar un enfoque más responsable en IA, por lo que, después de la conversión cuantitativa del modelo, se recomienda realizar pruebas más efectivas de los resultados.

4. Al cuantizar el modelo INT4 para CPU, podemos desplegarlo en dispositivos Edge, lo que ofrece mejores escenarios de aplicación. Por ello, hemos completado Phi-3.5-Instruct en torno a INT 4.


## **Recursos**

1. Aprende más sobre las extensiones de IA generativa para onnxruntime: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositorio de extensiones de IA generativa para onnxruntime en GitHub: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.