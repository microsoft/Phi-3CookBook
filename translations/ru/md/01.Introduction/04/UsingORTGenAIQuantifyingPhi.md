# **Квантование семейства Phi с использованием расширений Generative AI для onnxruntime**

## **Что такое расширения Generative AI для onnxruntime**

Эти расширения помогают запускать генеративный ИИ с ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Они предоставляют цикл генеративного ИИ для моделей ONNX, включая выполнение с помощью ONNX Runtime, обработку логитов, поиск и выборку, а также управление кэшированием KV. Разработчики могут вызывать высокоуровневый метод generate() или запускать каждую итерацию модели в цикле, генерируя по одному токену за раз, при необходимости обновляя параметры генерации внутри цикла. Поддерживаются жадный/лучевой поиск и выборка TopP, TopK для генерации последовательностей токенов, а также встроенная обработка логитов, например, штрафы за повторение. Вы также можете легко добавлять собственные методы оценки.

На уровне приложений вы можете использовать расширения Generative AI для onnxruntime для создания приложений с использованием C++/C#/Python. На уровне моделей вы можете использовать их для объединения дообученных моделей и выполнения связанных задач по развертыванию с учетом количественных характеристик.

## **Квантование Phi-3.5 с использованием расширений Generative AI для onnxruntime**

### **Поддерживаемые модели**

Расширения Generative AI для onnxruntime поддерживают преобразование с квантованием моделей Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Конструктор моделей в расширениях Generative AI для onnxruntime**

Конструктор моделей значительно ускоряет создание оптимизированных и квантованных моделей ONNX, которые работают с API generate() в ONNX Runtime.

С помощью конструктора моделей вы можете квантовать модель в INT4, INT8, FP16, FP32 и комбинировать различные методы аппаратного ускорения, такие как CPU, CUDA, DirectML, Mobile и другие.

Для использования конструктора моделей необходимо установить:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

После установки вы можете запустить скрипт конструктора моделей из терминала для выполнения преобразования формата модели и квантования.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Описание соответствующих параметров:

1. **model_name** Это модель на Hugging Face, например microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct и др. Это также может быть путь, где вы храните модель.

2. **path_to_output_folder** Путь для сохранения результата квантованного преобразования.

3. **execution_provider** Поддержка различных методов аппаратного ускорения, таких как cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Мы загружаем модель с Hugging Face и кэшируем её локально.

***Примечание:***

## **Как использовать конструктор моделей для квантования Phi-3.5**

Конструктор моделей теперь поддерживает квантование моделей ONNX для Phi-3.5 Instruct и Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Квантование INT4 с ускорением на CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Квантование INT4 с ускорением на CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Настройте окружение в терминале:

```bash

mkdir models

cd models 

```

2. Загрузите microsoft/Phi-3.5-vision-instruct в папку models:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Пожалуйста, загрузите следующие файлы в папку Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Загрузите этот файл в папку models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. В терминале выполните:  

    Преобразование ONNX с поддержкой FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Примечание:**

1. Конструктор моделей в настоящее время поддерживает преобразование Phi-3.5-Instruct и Phi-3.5-Vision, но не Phi-3.5-MoE.

2. Для использования квантованной модели ONNX вы можете воспользоваться SDK расширений Generative AI для onnxruntime.

3. Мы должны учитывать более ответственное использование ИИ, поэтому после преобразования модели с квантованием рекомендуется проводить более эффективное тестирование результатов.

4. Квантуя модель CPU INT4, мы можем развернуть её на Edge-устройствах, что открывает более широкие сценарии применения. Именно поэтому мы завершили квантование Phi-3.5-Instruct в INT4.

## **Ресурсы**

1. Узнайте больше о расширениях Generative AI для onnxruntime: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Репозиторий Generative AI extensions for onnxruntime на GitHub: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматизированных AI-сервисов перевода. Несмотря на наши усилия обеспечить точность, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.