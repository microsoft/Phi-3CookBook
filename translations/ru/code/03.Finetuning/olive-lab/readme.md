# Лабораторная работа. Оптимизация AI-моделей для выполнения на устройствах

## Введение

> [!IMPORTANT]  
> Для выполнения этой лабораторной работы требуется **GPU Nvidia A10 или A100** с установленными драйверами и CUDA toolkit (версии 12+).

> [!NOTE]  
> Эта лабораторная работа рассчитана на **35 минут** и даст вам практическое введение в основные концепции оптимизации моделей для выполнения на устройствах с использованием OLIVE.

## Учебные цели

К концу этой лабораторной работы вы сможете использовать OLIVE для:

- Квантования AI-модели с использованием метода квантования AWQ.
- Тонкой настройки AI-модели для конкретной задачи.
- Генерации адаптеров LoRA (тонко настроенной модели) для эффективного выполнения на устройствах с использованием ONNX Runtime.

### Что такое Olive

Olive (*O*NNX *live*) — это инструмент для оптимизации моделей с интерфейсом CLI, который позволяет разрабатывать модели для ONNX runtime +++https://onnxruntime.ai+++ с учетом качества и производительности.

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.ru.png)

Входными данными для Olive обычно является модель PyTorch или Hugging Face, а выходными — оптимизированная ONNX-модель, которая выполняется на устройстве (целевой платформе), работающем на ONNX runtime. Olive оптимизирует модель для AI-ускорителя целевой платформы (NPU, GPU, CPU), предоставляемого производителем оборудования, таким как Qualcomm, AMD, Nvidia или Intel.

Olive выполняет *workflow* (рабочий процесс), который представляет собой упорядоченную последовательность отдельных задач по оптимизации модели, называемых *passes* (проходы). Примеры проходов включают: сжатие модели, захват графа, квантование, оптимизацию графа. Каждый проход имеет набор параметров, которые можно настроить для достижения наилучших метрик, например, точности и задержки, которые оцениваются соответствующим оценщиком. Olive использует стратегию поиска, которая применяет алгоритм поиска для автоматической настройки каждого прохода по отдельности или набора проходов вместе.

#### Преимущества Olive

- **Уменьшение времени и разочарований**, связанных с ручным экспериментированием с различными методами оптимизации графов, сжатия и квантования. Определите свои требования к качеству и производительности, и Olive автоматически найдет для вас лучшую модель.
- **40+ встроенных компонентов для оптимизации моделей**, охватывающих передовые методы квантования, сжатия, оптимизации графов и тонкой настройки.
- **Простой CLI** для выполнения распространенных задач оптимизации моделей. Например, olive quantize, olive auto-opt, olive finetune.
- Встроенная упаковка и развертывание моделей.
- Поддержка генерации моделей для **мульти-LORA-сервиса**.
- Создание рабочих процессов с использованием YAML/JSON для организации задач оптимизации и развертывания моделей.
- Интеграция с **Hugging Face** и **Azure AI**.
- Встроенный механизм **кэширования** для **снижения затрат**.

## Инструкции к лабораторной работе

> [!NOTE]  
> Убедитесь, что вы настроили ваш Azure AI Hub и проект, а также настроили вычислительный ресурс A100 в соответствии с Лабораторной работой 1.

### Шаг 0: Подключение к вашему Azure AI Compute

Вы подключитесь к вычислительному ресурсу Azure AI, используя удаленную функцию в **VS Code.**

1. Откройте приложение **VS Code** на вашем компьютере.  
1. Откройте **палитру команд**, нажав **Shift+Ctrl+P**.  
1. В палитре команд найдите **AzureML - remote: Connect to compute instance in New Window**.  
1. Следуйте инструкциям на экране для подключения к вычислительному ресурсу. Это включает выбор вашей подписки Azure, группы ресурсов, проекта и имени вычислительного ресурса, которые вы настроили в Лабораторной работе 1.  
1. После подключения к узлу Azure ML Compute информация об этом отобразится в **нижнем левом углу Visual Code** `><Azure ML: Compute Name`.

### Шаг 1: Клонируйте этот репозиторий

В VS Code вы можете открыть новый терминал, нажав **Ctrl+J**, и клонировать этот репозиторий.

В терминале вы увидите запрос:

```
azureuser@computername:~/cloudfiles/code$ 
```  
Клонируйте решение:  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```  

### Шаг 2: Откройте папку в VS Code

Чтобы открыть VS Code в соответствующей папке, выполните следующую команду в терминале. Это откроет новое окно:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```  

Или вы можете открыть папку, выбрав **File** > **Open Folder**.

### Шаг 3: Зависимости

Откройте окно терминала в VS Code на вашем узле Azure AI Compute (подсказка: **Ctrl+J**) и выполните следующие команды для установки зависимостей:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```  

> [!NOTE]  
> Установка всех зависимостей займет около **5 минут**.

В этой лабораторной работе вы будете загружать и выгружать модели в каталог моделей Azure AI. Чтобы получить доступ к каталогу моделей, вам нужно будет войти в Azure, используя:

```bash
az login
```  

> [!NOTE]  
> Во время входа вам будет предложено выбрать подписку. Убедитесь, что вы выбрали подписку, предоставленную для этой лабораторной работы.

### Шаг 4: Выполнение команд Olive

Откройте окно терминала в VS Code на вашем узле Azure AI Compute (подсказка: **Ctrl+J**) и убедитесь, что активирована среда `olive-ai` conda:

```bash
conda activate olive-ai
```  

Затем выполните следующие команды Olive в командной строке.

1. **Проверьте данные:** В этом примере вы будете тонко настраивать модель Phi-3.5-Mini для специализации на ответах на вопросы, связанные с путешествиями. Код ниже отображает первые несколько записей из набора данных в формате JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```  

1. **Квантование модели:** Перед обучением модели сначала выполните ее квантование с помощью следующей команды, которая использует метод Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ выполняет квантование весов модели, учитывая активации, создаваемые во время выполнения. Это означает, что процесс квантования принимает во внимание фактическое распределение данных в активациях, что позволяет лучше сохранить точность модели по сравнению с традиционными методами квантования весов.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```  

    Процесс квантования AWQ займет **~8 минут** и **уменьшит размер модели с ~7,5 ГБ до ~2,5 ГБ**.

    В этой лабораторной работе мы покажем, как использовать модели из Hugging Face (например: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` для тонкой настройки квантованной модели. Квантование модели *до* тонкой настройки, а не после, обеспечивает лучшую точность, так как процесс тонкой настройки восстанавливает часть потерь от квантования.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```  

    Процесс тонкой настройки (с 100 шагами) займет **~6 минут**.

1. **Оптимизация:** После обучения модели вы оптимизируете ее с помощью команды Olive `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` - но для целей этой лабораторной работы мы будем использовать CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```  

    Оптимизация займет **~5 минут**.

### Шаг 5: Быстрое тестирование модели

Чтобы протестировать выполнение модели, создайте файл Python в своей папке с именем **app.py** и скопируйте следующий код:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```  

Выполните код с помощью:

```bash
python app.py
```  

### Шаг 6: Загрузка модели в Azure AI

Загрузка модели в репозиторий моделей Azure AI делает модель доступной для других участников вашей команды разработки, а также обеспечивает контроль версий модели. Для загрузки модели выполните следующую команду:

> [!NOTE]  
> Обновите `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` и имя проекта Azure AI, затем выполните следующую команду:

```
az ml workspace show
```  

Или перейдите на +++ai.azure.com+++ и выберите **management center** **project** **overview**.

Обновите `{}` заполнители именем вашей группы ресурсов и именем проекта Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Затем вы сможете увидеть загруженную модель и развернуть ее на https://ml.azure.com/model/list

**Отказ от ответственности**:  
Данный документ был переведен с использованием автоматизированных сервисов перевода на основе искусственного интеллекта. Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неверные интерпретации, возникшие в результате использования данного перевода.