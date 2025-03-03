# **Фина настройка на Phi-3 с LoRA**

Фина настройка на езиковия модел Phi-3 Mini на Microsoft с помощта на [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) върху персонализиран набор от инструкции за чат.

LoRA ще помогне за подобряване на разбирането на разговорите и генерирането на отговори.

## Стъпка по стъпка ръководство за фина настройка на Phi-3 Mini:

**Импортиране и настройка**

Инсталиране на loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Започнете с импортиране на необходимите библиотеки като datasets, transformers, peft, trl и torch. Настройте логване, за да следите процеса на обучение.

Можете да изберете да адаптирате някои слоеве, като ги замените с еквиваленти, имплементирани в loralib. Засега поддържаме само nn.Linear, nn.Embedding и nn.Conv2d. Поддържаме също MergedLinear за случаи, в които един nn.Linear представлява повече от един слой, като в някои имплементации на проекцията на внимание qkv (вижте Допълнителни бележки за повече информация).

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

Преди началото на тренировъчния цикъл маркирайте само параметрите на LoRA като обучаеми.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

При запазване на контролна точка, генерирайте state_dict, който съдържа само параметрите на LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

При зареждане на контролна точка с помощта на load_state_dict, уверете се, че сте задали strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

След това обучението може да продължи нормално.

**Хиперпараметри**

Дефинирайте два речника: training_config и peft_config. training_config включва хиперпараметри за обучение, като скорост на учене, размер на партидата и настройки за логване.

peft_config уточнява параметри, свързани с LoRA, като rank, dropout и тип задача.

**Зареждане на модела и токенизатора**

Посочете пътя до предварително обучен модел Phi-3 (например "microsoft/Phi-3-mini-4k-instruct"). Конфигурирайте настройките на модела, включително използване на кеш, тип данни (bfloat16 за смесена прецизност) и имплементация на внимание.

**Обучение**

Фина настройка на модела Phi-3 с помощта на персонализирания набор от инструкции за чат. Използвайте настройките на LoRA от peft_config за ефективна адаптация. Следете напредъка на обучението чрез избраната стратегия за логване.  
Оценка и запазване: Оценете фино настроения модел.  
Запазвайте контролни точки по време на обучението за бъдеща употреба.

**Примери**
- [Научете повече с този примерен тетраден файл](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Пример за Python скрипт за фина настройка](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Пример за фина настройка с LoRA в Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Пример за Hugging Face Model Card - фина настройка с LoRA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Пример за фина настройка с QLORA в Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Не носим отговорност за каквито и да е недоразумения или погрешни интерпретации, произтичащи от използването на този превод.