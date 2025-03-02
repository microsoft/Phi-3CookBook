# Ajustar Phi3 usando Olive

En este ejemplo, usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Tristeza, Alegría, Miedo y Sorpresa.
1. Fusionar los pesos del adaptador en el modelo base.
1. Optimizar y cuantizar el modelo en `int4`.

También te mostraremos cómo realizar inferencias con el modelo ajustado utilizando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste, necesitarás tener una GPU adecuada disponible, como una A10, V100 o A100.**

## 💾 Instalación

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Luego, instala Olive y las dependencias necesarias para el flujo de trabajo de ajuste:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 usando Olive
El [archivo de configuración de Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *flujo de trabajo* con los siguientes *procesos*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A un nivel general, este flujo de trabajo realizará lo siguiente:

1. Ajustar Phi3 (durante 150 pasos, lo cual puedes modificar) usando los datos de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionar los pesos del adaptador LoRA en el modelo base. Esto generará un único artefacto del modelo en formato ONNX.
1. Model Builder optimizará el modelo para el tiempo de ejecución de ONNX *y* cuantizará el modelo en `int4`.

Para ejecutar el flujo de trabajo, ejecuta:

```bash
olive run --config phrase-classification.json
```

Cuando Olive haya terminado, tu modelo ajustado y optimizado `int4` de Phi3 estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integra el modelo ajustado de Phi3 en tu aplicación 

Para ejecutar la aplicación:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Esta respuesta debería ser una clasificación de una sola palabra de la frase (Tristeza/Alegría/Miedo/Sorpresa).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.