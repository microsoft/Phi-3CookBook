# **Ajuste fino de Phi-3 con Lora**

Ajuste fino del modelo de lenguaje Phi-3 Mini de Microsoft utilizando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) en un conjunto de datos de instrucciones de chat personalizado.

LoRA ayudará a mejorar la comprensión conversacional y la generación de respuestas.

## Guía paso a paso sobre cómo ajustar finamente Phi-3 Mini:

**Importaciones y Configuración**

Instalando loralib

```
pip install loralib
# Alternativamente
# pip install git+https://github.com/microsoft/LoRA
```

Comienza importando las bibliotecas necesarias como datasets, transformers, peft, trl, y torch. Configura el registro para seguir el proceso de entrenamiento.

Puedes optar por adaptar algunas capas reemplazándolas con contrapartes implementadas en loralib. Solo soportamos nn.Linear, nn.Embedding y nn.Conv2d por ahora. También soportamos un MergedLinear para casos donde un solo nn.Linear representa más de una capa, como en algunas implementaciones de la proyección de atención qkv (ver Notas Adicionales para más detalles).

```
# ===== Antes =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== Después =====
```

import loralib as lora

```
# Agrega un par de matrices de adaptación de bajo rango con rango r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Antes de que comience el bucle de entrenamiento, marca solo los parámetros de LoRA como entrenables.

```
import loralib as lora
model = BigModel()
# Esto establece requires_grad en False para todos los parámetros que no tienen la cadena "lora_" en sus nombres
lora.mark_only_lora_as_trainable(model)
# Bucle de entrenamiento
for batch in dataloader:
```

Al guardar un checkpoint, genera un state_dict que solo contenga los parámetros de LoRA.

```
# ===== Antes =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== Después =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Al cargar un checkpoint usando load_state_dict, asegúrate de establecer strict=False.

```
# Primero carga el checkpoint preentrenado
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Luego carga el checkpoint de LoRA
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ahora el entrenamiento puede proceder como de costumbre.

**Hiperparámetros**

Define dos diccionarios: training_config y peft_config. training_config incluye hiperparámetros para el entrenamiento, como la tasa de aprendizaje, el tamaño del lote y la configuración de registro.

peft_config especifica parámetros relacionados con LoRA como el rango, el dropout y el tipo de tarea.

**Carga del Modelo y Tokenizador**

Especifica la ruta al modelo Phi-3 preentrenado (por ejemplo, "microsoft/Phi-3-mini-4k-instruct"). Configura los ajustes del modelo, incluyendo el uso de caché, el tipo de datos (bfloat16 para precisión mixta) y la implementación de atención.

**Entrenamiento**

Ajusta finamente el modelo Phi-3 utilizando el conjunto de datos de instrucciones de chat personalizado. Utiliza la configuración de LoRA de peft_config para una adaptación eficiente. Monitorea el progreso del entrenamiento utilizando la estrategia de registro especificada.
Evaluación y Guardado: Evalúa el modelo ajustado finamente.
Guarda checkpoints durante el entrenamiento para su uso posterior.

**Ejemplos**
- [Aprende más con este cuaderno de ejemplo](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ejemplo de ajuste fino en Python](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Ejemplo de ajuste fino en Hugging Face Hub con LORA](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ejemplo de tarjeta de modelo en Hugging Face - Ajuste fino con LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Ejemplo de ajuste fino en Hugging Face Hub con QLORA](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.