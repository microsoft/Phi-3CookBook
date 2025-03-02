[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Този код експортира модел във формат OpenVINO, зарежда го и го използва, за да генерира отговор на дадена заявка.

1. **Експортиране на модела**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Тази команда използва `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Импортиране на необходимите библиотеки**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Тези редове импортират класове от модула `transformers` library and the `optimum.intel.openvino`, които са необходими за зареждане и използване на модела.

3. **Настройване на директорията и конфигурацията на модела**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` е речник, който конфигурира OpenVINO модела да дава приоритет на ниска латентност, да използва един поток за инференция и да не използва кеш директория.

4. **Зареждане на модела**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Този ред зарежда модела от указаната директория, използвайки предварително дефинираните конфигурационни настройки. Също така позволява изпълнение на отдалечен код, ако е необходимо.

5. **Зареждане на токенизатора**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Този ред зарежда токенизатора, който е отговорен за преобразуването на текст в токени, разбираеми за модела.

6. **Настройване на параметрите на токенизатора**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Този речник указва, че специални токени не трябва да бъдат добавяни към резултата от токенизацията.

7. **Дефиниране на заявката**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Този низ задава примерен разговор, в който потребителят моли AI асистента да се представи.

8. **Токенизиране на заявката**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Този ред преобразува заявката в токени, които моделът може да обработи, като връща резултата като PyTorch тензори.

9. **Генериране на отговор**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Този ред използва модела, за да генерира отговор на базата на входните токени, с максимум 1024 нови токена.

10. **Декодиране на отговора**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Този ред преобразува генерираните токени обратно в четим текст, пропускайки специални токени, и извлича първия резултат.

**Отказ от отговорност**:  
Този документ е преведен с помощта на услуги за машинен превод с изкуствен интелект. Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.