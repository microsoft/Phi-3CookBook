# **Ajuste fino de Phi-3 con Lora**

Ajuste fino del modelo de lenguaje Phi-3 Mini de Microsoft utilizando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) en un conjunto de datos personalizado de instrucciones de chat.

LORA ayudará a mejorar la comprensión conversacional y la generación de respuestas.

## Guía paso a paso sobre cómo ajustar finamente Phi-3 Mini:

**Importaciones y Configuración**

Instalando loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comienza importando las bibliotecas necesarias como datasets, transformers, peft, trl y torch.
Configura el registro para rastrear el proceso de entrenamiento.

Puedes optar por adaptar algunas capas reemplazándolas con sus contrapartes implementadas en loralib. Actualmente, solo soportamos nn.Linear, nn.Embedding y nn.Conv2d. También soportamos MergedLinear para casos donde una sola nn.Linear representa más de una capa, como en algunas implementaciones de la proyección de atención qkv (ver Notas Adicionales para más detalles).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Antes de que comience el bucle de entrenamiento, marca solo los parámetros de LoRA como entrenables.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Al guardar un punto de control, genera un state_dict que solo contenga los parámetros de LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Al cargar un punto de control usando load_state_dict, asegúrate de establecer strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ahora el entrenamiento puede proceder como de costumbre.

**Hiperparámetros**

Define dos diccionarios: training_config y peft_config. training_config incluye hiperparámetros para el entrenamiento, como la tasa de aprendizaje, el tamaño del lote y la configuración de registro.

peft_config especifica parámetros relacionados con LoRA como el rango, el dropout y el tipo de tarea.

**Carga del Modelo y Tokenizador**

Especifica la ruta al modelo Phi-3 preentrenado (por ejemplo, "microsoft/Phi-3-mini-4k-instruct"). Configura los ajustes del modelo, incluyendo el uso de caché, el tipo de datos (bfloat16 para precisión mixta) y la implementación de atención.

**Entrenamiento**

Ajusta finamente el modelo Phi-3 usando el conjunto de datos personalizado de instrucciones de chat. Utiliza los ajustes de LoRA de peft_config para una adaptación eficiente. Monitorea el progreso del entrenamiento usando la estrategia de registro especificada.
Evaluación y Guardado: Evalúa el modelo ajustado finamente.
Guarda puntos de control durante el entrenamiento para uso posterior.

**Ejemplos**
- [Aprende más con este cuaderno de muestra](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ejemplo de ajuste fino en Python](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Ejemplo de ajuste fino en Hugging Face Hub con LORA](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ejemplo de tarjeta de modelo en Hugging Face - Muestra de ajuste fino con LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Ejemplo de ajuste fino en Hugging Face Hub con QLORA](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.