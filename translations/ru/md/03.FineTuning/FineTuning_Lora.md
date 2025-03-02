# **Тонкая настройка Phi-3 с использованием LoRA**

Тонкая настройка языковой модели Microsoft Phi-3 Mini с помощью [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) на основе пользовательского набора данных для инструкций в чатах.

LoRA поможет улучшить понимание диалогов и генерацию ответов.

## Пошаговое руководство по тонкой настройке Phi-3 Mini:

**Импорты и настройка**

Установка loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Начните с импорта необходимых библиотек, таких как datasets, transformers, peft, trl и torch. Настройте логирование для отслеживания процесса обучения.

Вы можете адаптировать некоторые слои, заменяя их на аналоги, реализованные в loralib. На данный момент поддерживаются только nn.Linear, nn.Embedding и nn.Conv2d. Также поддерживается MergedLinear для случаев, когда один nn.Linear представляет более одного слоя, например, в некоторых реализациях проекции qkv в механизме внимания (см. Дополнительные заметки для подробностей).

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

Перед началом цикла обучения отметьте только параметры LoRA как обучаемые.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

При сохранении контрольной точки создайте state_dict, содержащий только параметры LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При загрузке контрольной точки с использованием load_state_dict обязательно установите strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Теперь можно приступать к обучению, как обычно.

**Гиперпараметры**

Определите два словаря: training_config и peft_config. training_config включает гиперпараметры для обучения, такие как скорость обучения, размер батча и настройки логирования.

peft_config задает параметры, связанные с LoRA, такие как ранг, dropout и тип задачи.

**Загрузка модели и токенизатора**

Укажите путь к предварительно обученной модели Phi-3 (например, "microsoft/Phi-3-mini-4k-instruct"). Настройте параметры модели, включая использование кеша, тип данных (bfloat16 для смешанной точности) и реализацию внимания.

**Обучение**

Выполните тонкую настройку модели Phi-3, используя пользовательский набор данных для инструкций в чатах. Используйте настройки LoRA из peft_config для эффективной адаптации. Отслеживайте процесс обучения с помощью заданной стратегии логирования.

Оценка и сохранение: Оцените модель после тонкой настройки. Сохраняйте контрольные точки во время обучения для последующего использования.

**Примеры**
- [Узнайте больше с этим примером ноутбука](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример скрипта для тонкой настройки на Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример тонкой настройки с использованием LORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример карточки модели Hugging Face - тонкая настройка с LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Пример тонкой настройки с использованием QLORA на Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматизированных сервисов перевода на основе искусственного интеллекта. Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.