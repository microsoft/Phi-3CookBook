# **Квантизация на Phi Family с помощта на разширенията за Generative AI за onnxruntime**

## **Какво представляват разширенията за Generative AI за onnxruntime**

Тези разширения ви помагат да стартирате генеративен AI с ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Те предоставят генеративен AI цикъл за ONNX модели, включително извършване на изводи с ONNX Runtime, обработка на логити, търсене и семплиране, както и управление на KV кеш. Разработчиците могат да извикат високоневрона метода generate() или да стартират всяка итерация на модела в цикъл, генерирайки по един токен наведнъж, с възможност за промяна на параметрите на генериране вътре в цикъла. Поддържат се greedy/beam търсене и TopP, TopK семплиране за генериране на последователности от токени, както и вградена обработка на логити, като например наказания за повторения. Можете също така лесно да добавите персонализирано оценяване.

На ниво приложение можете да използвате разширенията за Generative AI за onnxruntime, за да изграждате приложения с помощта на C++/C#/Python. На ниво модел можете да ги използвате за обединяване на донастроени модели и извършване на свързана работа по количествено разгръщане.

## **Квантизация на Phi-3.5 с помощта на разширенията за Generative AI за onnxruntime**

### **Поддържани модели**

Разширенията за Generative AI за onnxruntime поддържат преобразуване с квантизация на Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Създател на модели в разширенията за Generative AI за onnxruntime**

Създателят на модели значително ускорява създаването на оптимизирани и квантизирани ONNX модели, които работят с API-то generate() на ONNX Runtime.

Чрез Създателя на модели можете да квантизирате модела до INT4, INT8, FP16, FP32 и да комбинирате различни методи за хардуерно ускорение, като CPU, CUDA, DirectML, Mobile и други.

За да използвате Създателя на модели, трябва да инсталирате:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

След инсталацията можете да стартирате скрипта на Създателя на модели от терминала, за да извършите преобразуване на формата и квантизацията на модела.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Разбиране на съответните параметри:

1. **model_name** Това е моделът в Hugging Face, като например microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct и други. Може също така да е пътят, където съхранявате модела.

2. **path_to_output_folder** Път за съхранение на преобразуваните с квантизация файлове.

3. **execution_provider** Поддръжка на различни методи за хардуерно ускорение, като cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Изтегляме модела от Hugging Face и го кешираме локално.

***Забележка:***

## **Как да използваме Създателя на модели за квантизация на Phi-3.5**

Създателят на модели вече поддържа квантизация на ONNX моделите Phi-3.5 Instruct и Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Конвертиране на квантизиран INT4 с ускорение от CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Конвертиране на квантизиран INT4 с ускорение от CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Настройте средата в терминала:

```bash

mkdir models

cd models 

```

2. Изтеглете microsoft/Phi-3.5-vision-instruct в папката models:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Моля, изтеглете следните файлове в папката Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Изтеглете този файл в папката models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Отидете в терминала:

    Конвертиране на ONNX с поддръжка на FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Забележка:**

1. Създателят на модели в момента поддържа преобразуване на Phi-3.5-Instruct и Phi-3.5-Vision, но не и на Phi-3.5-MoE.

2. За да използвате квантизирания модел на ONNX, можете да го използвате чрез SDK на разширенията за Generative AI за onnxruntime.

3. Трябва да разгледаме въпроса за по-отговорен AI, затова след преобразуването с квантизация се препоръчва провеждането на по-ефективно тестване на резултатите.

4. Чрез квантизация на CPU INT4 модела можем да го внедрим на Edge устройства, което предоставя по-добри приложения, затова завършихме Phi-3.5-Instruct около INT4.

## **Ресурси**

1. Научете повече за разширенията за Generative AI за onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub хранилище за разширенията за Generative AI за onnxruntime:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.