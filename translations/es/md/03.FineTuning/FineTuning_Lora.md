# **Ajuste fino de Phi-3 con Lora**

Ajuste fino del modelo de lenguaje Phi-3 Mini de Microsoft utilizando [LoRA (Adaptación de Bajo Rango)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) en un conjunto de datos personalizado de instrucciones para chat.

LoRA ayudará a mejorar la comprensión conversacional y la generación de respuestas.

## Guía paso a paso para ajustar finamente Phi-3 Mini:

**Importaciones y Configuración**

Instalación de loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comienza importando las bibliotecas necesarias, como datasets, transformers, peft, trl y torch. Configura el registro para hacer seguimiento del proceso de entrenamiento.

Puedes optar por adaptar algunas capas reemplazándolas con contrapartes implementadas en loralib. Actualmente, solo admitimos nn.Linear, nn.Embedding y nn.Conv2d. También soportamos MergedLinear para casos donde un solo nn.Linear representa más de una capa, como en algunas implementaciones de la proyección de atención qkv (consulta Notas Adicionales para más información).

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

Al guardar un checkpoint, genera un state_dict que solo contenga los parámetros de LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Al cargar un checkpoint usando load_state_dict, asegúrate de establecer strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ahora el entrenamiento puede proceder como de costumbre.

**Hiperparámetros**

Define dos diccionarios: training_config y peft_config. training_config incluye hiperparámetros para el entrenamiento, como la tasa de aprendizaje, el tamaño del lote y la configuración de registro.

peft_config especifica parámetros relacionados con LoRA, como rango, dropout y tipo de tarea.

**Carga del Modelo y el Tokenizador**

Especifica la ruta al modelo Phi-3 preentrenado (por ejemplo, "microsoft/Phi-3-mini-4k-instruct"). Configura los ajustes del modelo, incluyendo el uso de caché, el tipo de datos (bfloat16 para precisión mixta) y la implementación de atención.

**Entrenamiento**

Ajusta finamente el modelo Phi-3 utilizando el conjunto de datos personalizado de instrucciones para chat. Utiliza la configuración de LoRA de peft_config para una adaptación eficiente. Supervisa el progreso del entrenamiento utilizando la estrategia de registro especificada.

**Evaluación y Guardado**

Evalúa el modelo ajustado finamente. Guarda checkpoints durante el entrenamiento para su uso posterior.

**Ejemplos**
- [Aprende más con este cuaderno de ejemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ejemplo de script de ajuste fino en Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Ejemplo de ajuste fino con LORA en Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ejemplo de tarjeta de modelo de Hugging Face - Ajuste fino con LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Ejemplo de ajuste fino con QLORA en Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.