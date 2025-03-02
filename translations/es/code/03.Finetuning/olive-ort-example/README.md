# Ajustar Phi3 usando Olive

En este ejemplo, usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Tristeza, Alegría, Miedo, Sorpresa.
1. Fusionar los pesos del adaptador con el modelo base.
1. Optimizar y cuantizar el modelo en `int4`.

También te mostraremos cómo inferir el modelo ajustado usando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste fino, necesitarás tener una GPU adecuada disponible, por ejemplo, una A10, V100, A100.**

## 💾 Instalación

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

A continuación, instala Olive y las dependencias para un flujo de trabajo de ajuste fino:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 usando Olive
El [archivo de configuración de Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contiene un *flujo de trabajo* con los siguientes *pases*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A un nivel general, este flujo de trabajo hará lo siguiente:

1. Ajustar Phi3 (durante 150 pasos, que puedes modificar) usando los datos de [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionar los pesos del adaptador LoRA con el modelo base. Esto te proporcionará un único artefacto del modelo en formato ONNX.
1. Model Builder optimizará el modelo para el tiempo de ejecución ONNX *y* cuantizará el modelo en `int4`.

Para ejecutar el flujo de trabajo, ejecuta:

```bash
olive run --config phrase-classification.json
```

Cuando Olive haya terminado, tu modelo Phi3 ajustado y optimizado en `int4` estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integra Phi3 ajustado en tu aplicación 

Para ejecutar la aplicación:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Esta respuesta debería ser una clasificación de una sola palabra de la frase (Tristeza/Alegría/Miedo/Sorpresa).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.