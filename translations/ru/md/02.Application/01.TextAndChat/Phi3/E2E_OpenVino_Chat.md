[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Этот код экспортирует модель в формат OpenVINO, загружает её и использует для генерации ответа на заданный запрос.

1. **Экспорт модели**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Эта команда использует `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Импорт необходимых библиотек**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Эти строки импортируют классы из модуля `transformers` library and the `optimum.intel.openvino`, которые нужны для загрузки и использования модели.

3. **Настройка директории модели и конфигурации**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` — это словарь, который настраивает модель OpenVINO на приоритет низкой задержки, использование одного потока для вывода и отсутствие использования директории кэша.

4. **Загрузка модели**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Эта строка загружает модель из указанной директории, используя ранее заданные настройки конфигурации. Она также допускает выполнение удалённого кода, если это необходимо.

5. **Загрузка токенизатора**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Эта строка загружает токенизатор, который отвечает за преобразование текста в токены, понятные модели.

6. **Настройка аргументов токенизатора**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Этот словарь указывает, что специальные токены не должны добавляться к токенизированному выводу.

7. **Определение запроса**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Эта строка задаёт текстовый запрос, в котором пользователь просит AI-ассистента представиться.

8. **Токенизация запроса**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Эта строка преобразует запрос в токены, которые может обработать модель, возвращая результат в виде тензоров PyTorch.

9. **Генерация ответа**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Эта строка использует модель для генерации ответа на основе входных токенов, с максимальным количеством новых токенов, равным 1024.

10. **Декодирование ответа**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Эта строка преобразует сгенерированные токены обратно в читаемую строку, пропуская любые специальные токены, и возвращает первый результат.

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматизированных сервисов перевода на основе ИИ. Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.