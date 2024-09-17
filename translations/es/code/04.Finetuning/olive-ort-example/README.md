# Ajustar Phi3 usando Olive

En este ejemplo usarás Olive para:

1. Ajustar un adaptador LoRA para clasificar frases en Tristeza, Alegría, Miedo, Sorpresa.
1. Fusionar los pesos del adaptador en el modelo base.
1. Optimizar y cuantificar el modelo en `int4`.

También te mostraremos cómo inferir el modelo ajustado usando la API Generate de ONNX Runtime (ORT).

> **⚠️ Para el ajuste, necesitarás tener una GPU adecuada disponible, por ejemplo, una A10, V100, A100.**

## 💾 Instalación

Crea un nuevo entorno virtual de Python (por ejemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

A continuación, instala Olive y las dependencias para un flujo de trabajo de ajuste:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar Phi3 usando Olive
El [archivo de configuración de Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con los siguientes *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A un alto nivel, este flujo de trabajo hará:

1. Ajustar Phi3 (por 150 pasos, los cuales puedes modificar) usando los datos de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionar los pesos del adaptador LoRA en el modelo base. Esto te dará un único artefacto de modelo en formato ONNX.
1. Model Builder optimizará el modelo para el runtime de ONNX *y* cuantificará el modelo en `int4`.

Para ejecutar el flujo de trabajo, ejecuta:

```bash
olive run --config phrase-classification.json
```

Cuando Olive haya completado, tu modelo Phi3 ajustado y optimizado en `int4` estará disponible en: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar Phi3 ajustado en tu aplicación 

Para ejecutar la aplicación:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Esta respuesta debería ser una clasificación de una sola palabra de la frase (Tristeza/Alegría/Miedo/Sorpresa).

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.