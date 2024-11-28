# Ajustar Phi3 usando Olive

En este ejemplo, usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Triste, Alegría, Miedo, Sorpresa.
1. Fusionar los pesos del adaptador en el modelo base.
1. Optimizar y Cuantizar el modelo en `int4`.

También te mostraremos cómo inferir el modelo ajustado usando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste fino, necesitarás tener una GPU adecuada disponible - por ejemplo, una A10, V100, A100.**

## 💾 Instalar

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Luego, instala Olive y las dependencias para un flujo de trabajo de ajuste fino:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 usando Olive
El [archivo de configuración de Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *flujo de trabajo* con los siguientes *pasos*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A un alto nivel, este flujo de trabajo hará:

1. Ajustar Phi3 (por 150 pasos, que puedes modificar) usando los datos de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionar los pesos del adaptador LoRA en el modelo base. Esto te dará un único artefacto de modelo en formato ONNX.
1. Model Builder optimizará el modelo para el tiempo de ejecución de ONNX *y* cuantizará el modelo en `int4`.

Para ejecutar el flujo de trabajo, ejecuta:

```bash
olive run --config phrase-classification.json
```

Cuando Olive haya completado, tu modelo Phi3 ajustado y optimizado `int4` estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar Phi3 ajustado en tu aplicación 

Para ejecutar la aplicación:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Esta respuesta debería ser una clasificación de una sola palabra de la frase (Triste/Alegría/Miedo/Sorpresa).

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automatizada por IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.