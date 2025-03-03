# Receta para el ajuste fino de Phi-3.5-vision

Este es el soporte oficial para el ajuste fino de Phi-3.5-vision utilizando las bibliotecas de huggingface.  
Por favor, `cd` al directorio de código [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) antes de ejecutar los siguientes comandos.

## Instalación

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Inicio rápido

Proporcionamos dos scripts de ejemplo para ajuste fino, uno para DocVQA y otro para la clasificación de memes de odio.

Hardware mínimo probado en 4x RTX8000 (48GB de RAM por GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ahora soporta oficialmente entradas de múltiples imágenes. Aquí tienes un ejemplo para el ajuste fino de NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Guía de uso

Dependiendo del hardware, los usuarios pueden elegir diferentes estrategias de ajuste fino. Soportamos ajuste fino completo (con Deepspeed Zero-2) con parámetros de visión opcionalmente congelados, y LoRA (incluyendo QLoRA de 4 bits).  
En general, recomendamos usar ajuste fino completo con atención flash y bf16 siempre que sea posible.

### Guía para convertir tu conjunto de datos personalizado al formato requerido

Usamos un conjunto de datos mínimo de clasificación de video (un subconjunto de UCF-101) como un ejemplo de extremo a extremo para demostrar cómo convertir tu conjunto de datos personalizado al formato requerido y ajustar Phi-3.5-vision en él.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Los datos convertidos tendrán este aspecto:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

Para la anotación `jsonl`, cada línea debe ser un diccionario como este:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Nota que `conversations` es una lista, por lo que se pueden soportar conversaciones de múltiples turnos si dichos datos están disponibles.

## Solicitar una cuota de GPU en Azure 

### Requisitos previos

Una cuenta de Azure con el rol de Colaborador (o cualquier otro rol que incluya acceso de Colaborador).  

Si no tienes una cuenta de Azure, crea una [cuenta gratuita antes de comenzar](https://azure.microsoft.com).

### Solicitar un aumento de cuota

Puedes enviar una solicitud para aumentar la cuota directamente desde "Mis cuotas". Sigue los pasos a continuación para solicitar un aumento de cuota. En este ejemplo, puedes seleccionar cualquier cuota ajustable en tu suscripción.

Inicia sesión en el [portal de Azure](https://portal.azure.com).

Escribe "quotas" en el cuadro de búsqueda y selecciona Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

En la página de Descripción general, selecciona un proveedor, como Compute o AML.  

**Nota:** Para todos los proveedores excepto Compute, verás una columna llamada Solicitar aumento en lugar de la columna Ajustable descrita a continuación. Allí, puedes solicitar un aumento para una cuota específica o crear una solicitud de soporte para el aumento.

En la página Mis cuotas, bajo el nombre de la cuota, selecciona la cuota que deseas aumentar. Asegúrate de que la columna Ajustable muestre "Sí" para esta cuota.

En la parte superior de la página, selecciona Nueva solicitud de cuota y luego selecciona Introducir un nuevo límite.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

En el panel de Nueva solicitud de cuota, introduce un valor numérico para tu nuevo límite de cuota y selecciona Enviar.

Tu solicitud será revisada y se te notificará si puede cumplirse. Esto generalmente ocurre en pocos minutos.

Si tu solicitud no se cumple, verás un enlace para crear una solicitud de soporte. Cuando utilices este enlace, un ingeniero de soporte te asistirá con tu solicitud de aumento.

## Sugerencias de SKU de máquinas GPU en Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Aquí hay algunos ejemplos:

### Si tienes GPUs A100 o H100

El ajuste fino completo generalmente ofrece el mejor rendimiento. Puedes usar el siguiente comando para ajustar Phi-3-V en la clasificación de memes de odio.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Si tienes GPUs Standard_ND40rs_v2 8x V100-32GB

Todavía es posible realizar un ajuste fino completo de Phi-3-V en la clasificación de memes de odio. Sin embargo, espera un rendimiento mucho menor en comparación con las GPUs A100 o H100 debido a la falta de soporte para atención flash.  
La precisión también podría verse afectada debido a la falta de soporte para bf16 (se usa entrenamiento de precisión mixta fp16 en su lugar).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Si no tienes acceso a GPUs de centro de datos

LoRA podría ser tu única opción. Puedes usar el siguiente comando para ajustar Phi-3-V en la clasificación de memes de odio.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Para GPUs Turing+, se soporta QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hiperparámetros sugeridos y precisión esperada

### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Método de entrenamiento | Modelo de visión congelado | Tipo de datos | Rango LoRA | Alpha LoRA | Tamaño de lote | Tasa de aprendizaje | Épocas | Precisión
--- | --- | --- | --- | --- | --- | --- | --- | --- |
ajuste fino completo |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
ajuste fino completo | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Resultados de LoRA próximamente |  |  |  |  |  |  |  |  |

### NOTA
Los resultados a continuación de DocVQA y memes de odio están basados en la versión anterior (Phi-3-vision).  
Los nuevos resultados con Phi-3.5-vision se actualizarán pronto.

### DocVQA (NOTA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Método de entrenamiento | Tipo de datos | Rango LoRA | Alpha LoRA | Tamaño de lote | Tasa de aprendizaje | Épocas | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
ajuste fino completo | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
ajuste fino completo | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
modelo de imagen congelado | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
modelo de imagen congelado | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Memes de odio (NOTA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Método de entrenamiento | Tipo de datos | Rango LoRA | Alpha LoRA | Tamaño de lote | Tasa de aprendizaje | Épocas | Precisión
--- | --- | --- | --- | --- | --- | --- | --- |
ajuste fino completo | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
ajuste fino completo | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
modelo de imagen congelado | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
modelo de imagen congelado | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmarking de velocidad (NOTA: Phi-3-vision)

Los nuevos resultados de benchmarking con Phi-3.5-vision se actualizarán pronto.

El benchmarking de velocidad se realiza en el conjunto de datos DocVQA. La longitud promedio de secuencia de este conjunto de datos es de 2443.23 tokens (usando `num_crops=16` para el modelo de imagen).

### 8x A100-80GB (Ampere)

Método de entrenamiento | \# nodos | GPUs | Atención flash | Tamaño de lote efectivo | Rendimiento (img/s) | Aceleración | Memoria GPU máxima (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
ajuste fino completo | 1 | 8 |  | 64 | 5.041 | 1x | ~42
ajuste fino completo | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
ajuste fino completo | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
ajuste fino completo | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
modelo de imagen congelado | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
modelo de imagen congelado | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Método de entrenamiento | \# nodos | GPUs | Atención flash | Tamaño de lote efectivo | Rendimiento (img/s) | Aceleración | Memoria GPU máxima (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
ajuste fino completo | 1 | 8 | | 64 | 2.462 | 1x | ~32
ajuste fino completo | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
ajuste fino completo | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
modelo de imagen congelado | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Problemas conocidos

- No se puede ejecutar atención flash con fp16 (siempre se recomienda bf16 cuando está disponible, y todas las GPUs que soportan atención flash también soportan bf16).
- Aún no se soporta guardar puntos de control intermedios ni reanudar el entrenamiento.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.