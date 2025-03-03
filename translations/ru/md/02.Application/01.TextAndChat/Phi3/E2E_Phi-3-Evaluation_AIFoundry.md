# Оценка дообученной модели Phi-3 / Phi-3.5 в Azure AI Foundry с акцентом на принципы ответственного использования ИИ от Microsoft

Этот пример от начала до конца (E2E) основан на руководстве "[Оценка дообученных моделей Phi-3 / 3.5 в Azure AI Foundry с акцентом на принципы ответственного использования ИИ от Microsoft](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" из сообщества Microsoft Tech Community.

## Обзор

### Как оценить безопасность и производительность дообученной модели Phi-3 / Phi-3.5 в Azure AI Foundry?

Дообучение модели иногда может приводить к нежелательным или непредвиденным ответам. Чтобы убедиться, что модель остается безопасной и эффективной, важно оценить её потенциал для генерации вредоносного контента, а также её способность выдавать точные, релевантные и связные ответы. В этом руководстве вы узнаете, как оценить безопасность и производительность дообученной модели Phi-3 / Phi-3.5, интегрированной с Prompt flow в Azure AI Foundry.

Вот процесс оценки в Azure AI Foundry.

![Архитектура руководства.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ru.png)

*Источник изображения: [Оценка приложений генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Для получения более детальной информации и изучения дополнительных ресурсов о Phi-3 / Phi-3.5 посетите [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Предварительные требования

- [Python](https://www.python.org/downloads)
- [Подписка Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Дообученная модель Phi-3 / Phi-3.5

### Содержание

1. [**Сценарий 1: Введение в оценку Prompt flow в Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Введение в оценку безопасности](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Введение в оценку производительности](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Перед началом](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Оценка дообученной модели Phi-3 / Phi-3.5 с использованием Prompt flow в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Поздравляем!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Сценарий 1: Введение в оценку Prompt flow в Azure AI Foundry**

### Введение в оценку безопасности

Чтобы ваш ИИ-модель соответствовала этическим стандартам и была безопасной, важно оценивать её в соответствии с принципами ответственного использования ИИ от Microsoft. В Azure AI Foundry оценки безопасности позволяют проверить уязвимость модели к атакам на обход ограничений (jailbreak attacks) и её способность генерировать вредоносный контент, что напрямую соответствует этим принципам.

![Оценка безопасности.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.ru.png)

*Источник изображения: [Оценка приложений генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципы ответственного использования ИИ от Microsoft

Прежде чем переходить к техническим шагам, важно понимать Принципы ответственного использования ИИ от Microsoft — этическую основу, разработанную для руководства по ответственному развитию, внедрению и эксплуатации систем ИИ. Эти принципы направлены на то, чтобы ИИ технологии разрабатывались с учетом справедливости, прозрачности и инклюзивности. Они служат основой для оценки безопасности моделей ИИ.

Принципы ответственного использования ИИ от Microsoft включают:

- **Справедливость и инклюзивность**: Системы ИИ должны относиться ко всем справедливо и избегать различного воздействия на схожие группы людей. Например, если ИИ дает рекомендации по медицинскому лечению, заявкам на кредиты или трудоустройству, они должны быть одинаковыми для всех с аналогичными симптомами, финансовым положением или профессиональными квалификациями.

- **Надежность и безопасность**: Чтобы завоевать доверие, важно, чтобы системы ИИ работали надежно, безопасно и стабильно. Они должны функционировать так, как изначально задумывались, безопасно реагировать на непредвиденные условия и быть устойчивыми к вредоносным манипуляциям.

- **Прозрачность**: Когда системы ИИ помогают принимать решения, которые существенно влияют на жизнь людей, важно, чтобы люди понимали, как принимаются эти решения. Например, банк может использовать ИИ для оценки кредитоспособности человека.

- **Конфиденциальность и безопасность**: По мере распространения ИИ защита конфиденциальности и обеспечение безопасности данных становятся всё более важными. Конфиденциальность и безопасность данных требуют особого внимания, так как доступ к данным необходим для точных прогнозов и решений.

- **Ответственность**: Люди, которые разрабатывают и внедряют системы ИИ, должны быть ответственны за их работу. Организации должны следовать отраслевым стандартам, чтобы выработать нормы ответственности.

![Центр принципов.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.ru.png)

*Источник изображения: [Что такое ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Чтобы узнать больше о принципах ответственного использования ИИ от Microsoft, посетите [Что такое ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики безопасности

В этом руководстве вы оцените безопасность дообученной модели Phi-3 с использованием метрик безопасности Azure AI Foundry. Эти метрики помогают оценить склонность модели к генерации вредоносного контента и её уязвимость к атакам на обход ограничений. Метрики безопасности включают:

- **Контент, связанный с самоповреждением**: Оценивает, имеет ли модель тенденцию генерировать контент, связанный с самоповреждением.
- **Ненавистный и несправедливый контент**: Оценивает склонность модели к генерации ненавистного или несправедливого контента.
- **Насильственный контент**: Оценивает склонность модели к генерации насильственного контента.
- **Сексуальный контент**: Оценивает склонность модели к генерации неподобающего сексуального контента.

Оценка этих аспектов гарантирует, что модель ИИ не генерирует вредоносный или оскорбительный контент, соответствуя общественным ценностям и нормативным стандартам.

![Оценка на основе безопасности.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.ru.png)

### Введение в оценку производительности

Чтобы убедиться, что модель ИИ работает так, как ожидается, важно оценить её производительность на основе метрик производительности. В Azure AI Foundry такие оценки позволяют проверить эффективность модели в генерации точных, релевантных и связных ответов.

![Оценка производительности.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.ru.png)

*Источник изображения: [Оценка приложений генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики производительности

В этом руководстве вы оцените производительность дообученной модели Phi-3 / Phi-3.5 с использованием метрик производительности Azure AI Foundry. Эти метрики помогают оценить эффективность модели в генерации точных, релевантных и связных ответов. Метрики производительности включают:

- **Основанность**: Оценивает, насколько ответы модели соответствуют информации из входного источника.
- **Релевантность**: Оценивает уместность сгенерированных ответов для заданных вопросов.
- **Связность**: Оценивает, насколько плавно и естественно читается текст, насколько он похож на человеческую речь.
- **Беглость**: Оценивает уровень языковой грамотности сгенерированного текста.
- **Сходство с GPT**: Сравнивает сгенерированный ответ с эталонным по степени сходства.
- **F1 Score**: Рассчитывает долю общих слов между сгенерированным ответом и исходными данными.

Эти метрики помогают оценить эффективность модели в генерации точных, релевантных и связных ответов.

![Оценка на основе производительности.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.ru.png)

## **Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Azure AI Foundry**

### Перед началом

Это руководство является продолжением предыдущих публикаций "[Дообучение и интеграция пользовательских моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Дообучение и интеграция пользовательских моделей Phi-3 с Prompt Flow в Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." В этих публикациях описан процесс дообучения модели Phi-3 / Phi-3.5 в Azure AI Foundry и её интеграции с Prompt flow.

В этом руководстве вы развернёте модель Azure OpenAI в качестве оценщика в Azure AI Foundry и используете её для оценки вашей дообученной модели Phi-3 / Phi-3.5.

Перед началом убедитесь, что у вас есть следующие предварительные условия, описанные в предыдущих руководствах:

1. Подготовленный набор данных для оценки дообученной модели Phi-3 / Phi-3.5.
1. Модель Phi-3 / Phi-3.5, дообученная и развернутая в Azure Machine Learning.
1. Prompt flow, интегрированный с вашей дообученной моделью Phi-3 / Phi-3.5 в Azure AI Foundry.

> [!NOTE]
> Вы будете использовать файл *test_data.jsonl*, расположенный в папке данных набора **ULTRACHAT_200k**, загруженного в предыдущих публикациях, в качестве набора данных для оценки дообученной модели Phi-3 / Phi-3.5.

#### Интеграция пользовательской модели Phi-3 / Phi-3.5 с Prompt flow в Azure AI Foundry (подход на основе кода)

> [!NOTE]
> Если вы следовали подходу с минимальным кодированием, описанному в "[Дообучение и интеграция пользовательских моделей Phi-3 с Prompt Flow в Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", вы можете пропустить это упражнение и перейти к следующему.
> Однако если вы использовали подход "сначала код" из публикации "[Дообучение и интеграция пользовательских моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", процесс подключения вашей модели к Prompt flow немного отличается. Вы изучите этот процесс в данном упражнении.

Для продолжения необходимо интегрировать вашу дообученную модель Phi-3 / Phi-3.5 в Prompt flow в Azure AI Foundry.

#### Создание хаба Azure AI Foundry

Перед созданием проекта необходимо создать хаб. Хаб действует как группа ресурсов, позволяя организовывать и управлять несколькими проектами в Azure AI Foundry.

1. Войдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Выберите **Все хабы** в левой панели.

1. Нажмите **+ Новый хаб** в меню навигации.

    ![Создание хаба.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.ru.png)

1. Выполните следующие действия:

    - Введите **Имя хаба**. Оно должно быть уникальным.
    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **Группу ресурсов** (создайте новую, если необходимо).
    - Укажите **Локацию**, которую хотите использовать.
    - Выберите **Подключить службы Azure AI** (создайте новые, если необходимо).
    - Выберите **Пропустить подключение** для Azure AI Search.
![Заполнить хаб.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.ru.png)

1. Выберите **Next**.

#### Создание проекта Azure AI Foundry

1. В созданном вами хабе выберите **All projects** в левой панели.

1. Выберите **+ New project** в навигационном меню.

    ![Выберите новый проект.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.ru.png)

1. Введите **Project name**. Оно должно быть уникальным.

    ![Создать проект.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.ru.png)

1. Выберите **Create a project**.

#### Добавление пользовательского подключения для дообученной модели Phi-3 / Phi-3.5

Чтобы интегрировать вашу пользовательскую модель Phi-3 / Phi-3.5 с Prompt flow, необходимо сохранить endpoint и ключ модели в пользовательском подключении. Это обеспечит доступ к вашей модели в Prompt flow.

#### Установка api key и endpoint uri для дообученной модели Phi-3 / Phi-3.5

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Перейдите в созданное вами рабочее пространство Azure Machine Learning.

1. Выберите **Endpoints** в левой панели.

    ![Выберите endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.ru.png)

1. Выберите созданный вами endpoint.

    ![Выберите созданный endpoint.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.ru.png)

1. Выберите **Consume** в навигационном меню.

1. Скопируйте ваш **REST endpoint** и **Primary key**.

    ![Скопируйте api key и endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.ru.png)

#### Добавление пользовательского подключения

1. Перейдите на [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдите в созданный вами проект Azure AI Foundry.

1. В созданном проекте выберите **Settings** в левой панели.

1. Выберите **+ New connection**.

    ![Выберите новое подключение.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.ru.png)

1. Выберите **Custom keys** в навигационном меню.

    ![Выберите пользовательские ключи.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.ru.png)

1. Выполните следующие действия:

    - Выберите **+ Add key value pairs**.
    - Введите **endpoint** в качестве имени ключа и вставьте endpoint, скопированный из Azure ML Studio, в поле значения.
    - Снова выберите **+ Add key value pairs**.
    - Введите **key** в качестве имени ключа и вставьте ключ, скопированный из Azure ML Studio, в поле значения.
    - После добавления ключей выберите **is secret**, чтобы ключ не был видимым.

    ![Добавьте подключение.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.ru.png)

1. Выберите **Add connection**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Azure AI Foundry. Теперь давайте создадим Prompt flow, используя следующие шаги. Затем вы подключите этот Prompt flow к пользовательскому подключению, чтобы использовать дообученную модель в рамках Prompt flow.

1. Перейдите в созданный вами проект Azure AI Foundry.

1. Выберите **Prompt flow** в левой панели.

1. Выберите **+ Create** в навигационном меню.

    ![Выберите Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.ru.png)

1. Выберите **Chat flow** в навигационном меню.

    ![Выберите chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.ru.png)

1. Введите **Folder name**, который хотите использовать.

    ![Введите имя папки.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.ru.png)

1. Выберите **Create**.

#### Настройка Prompt flow для работы с вашей моделью Phi-3 / Phi-3.5

Необходимо интегрировать дообученную модель Phi-3 / Phi-3.5 в Prompt flow. Однако текущий Prompt flow не подходит для этой цели. Поэтому потребуется изменить его для интеграции пользовательской модели.

1. В Prompt flow выполните следующие действия для изменения существующего потока:

    - Выберите **Raw file mode**.
    - Удалите весь существующий код в файле *flow.dag.yml*.
    - Добавьте следующий код в *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Выберите **Save**.

    ![Выберите режим редактирования файлов.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.ru.png)

1. Добавьте следующий код в *integrate_with_promptflow.py*, чтобы использовать пользовательскую модель Phi-3 / Phi-3.5 в Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Вставьте код Prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.ru.png)

> [!NOTE]
> Для получения дополнительной информации о работе с Prompt flow в Azure AI Foundry, обратитесь к [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Выберите **Chat input**, **Chat output**, чтобы включить чат с вашей моделью.

    ![Выберите Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.ru.png)

1. Теперь вы готовы к работе с вашей моделью Phi-3 / Phi-3.5. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с дообученной моделью Phi-3 / Phi-3.5.

> [!NOTE]
>
> Измененный поток должен выглядеть следующим образом:
>
> ![Пример потока](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.ru.png)
>

#### Запуск Prompt flow

1. Выберите **Start compute sessions**, чтобы запустить Prompt flow.

    ![Запустите вычислительную сессию.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.ru.png)

1. Выберите **Validate and parse input**, чтобы обновить параметры.

    ![Проверьте ввод.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.ru.png)

1. Выберите **Value** для **connection**, чтобы подключиться к созданному вами пользовательскому подключению. Например, *connection*.

    ![Подключение.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.ru.png)

#### Общение с вашей моделью Phi-3 / Phi-3.5

1. Выберите **Chat**.

    ![Выберите чат.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.ru.png)

1. Пример результатов: Теперь вы можете общаться с вашей моделью Phi-3 / Phi-3.5. Рекомендуется задавать вопросы, основанные на данных, использованных для дообучения.

    ![Общение через Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.ru.png)

### Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5

Чтобы оценить модель Phi-3 / Phi-3.5 в Azure AI Foundry, необходимо развернуть модель Azure OpenAI. Она будет использоваться для оценки производительности Phi-3 / Phi-3.5.

#### Развертывание Azure OpenAI

1. Войдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдите в созданный вами проект Azure AI Foundry.

    ![Выберите проект.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ru.png)

1. В созданном проекте выберите **Deployments** в левой панели.

1. Выберите **+ Deploy model** в навигационном меню.

1. Выберите **Deploy base model**.

    ![Выберите развертывания.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.ru.png)

1. Выберите модель Azure OpenAI, которую хотите использовать. Например, **gpt-4o**.

    ![Выберите модель Azure OpenAI.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.ru.png)

1. Выберите **Confirm**.

### Оценка дообученной модели Phi-3 / Phi-3.5 с использованием Prompt flow в Azure AI Foundry

### Начало новой оценки

1. Перейдите на [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдите в созданный вами проект Azure AI Foundry.

    ![Выберите проект.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.ru.png)

1. В созданном проекте выберите **Evaluation** в левой панели.

1. Выберите **+ New evaluation** в навигационном меню.
![Выбор оценки.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.ru.png)

1. Выберите **Prompt flow** оценку.

    ![Выбор оценки Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.ru.png)

1. Выполните следующие действия:

    - Введите имя оценки. Оно должно быть уникальным.
    - Выберите **Вопрос и ответ без контекста** в качестве типа задачи. Это связано с тем, что набор данных **ULTRACHAT_200k**, используемый в этом руководстве, не содержит контекста.
    - Выберите поток подсказок, который вы хотите оценить.

    ![Оценка Prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.ru.png)

1. Нажмите **Далее**.

1. Выполните следующие действия:

    - Выберите **Добавить ваш набор данных**, чтобы загрузить набор данных. Например, вы можете загрузить файл тестового набора данных, такой как *test_data.json1*, который включен при загрузке набора данных **ULTRACHAT_200k**.
    - Выберите соответствующий **Столбец набора данных**, который соответствует вашему набору данных. Например, если вы используете набор данных **ULTRACHAT_200k**, выберите **${data.prompt}** в качестве столбца набора данных.

    ![Оценка Prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.ru.png)

1. Нажмите **Далее**.

1. Выполните следующие действия для настройки метрик производительности и качества:

    - Выберите метрики производительности и качества, которые вы хотите использовать.
    - Выберите модель Azure OpenAI, созданную вами для оценки. Например, выберите **gpt-4o**.

    ![Оценка Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.ru.png)

1. Выполните следующие действия для настройки метрик риска и безопасности:

    - Выберите метрики риска и безопасности, которые вы хотите использовать.
    - Установите порог для расчета уровня дефектов, который вы хотите использовать. Например, выберите **Средний**.
    - Для **вопроса** выберите **Источник данных** как **{$data.prompt}**.
    - Для **ответа** выберите **Источник данных** как **{$run.outputs.answer}**.
    - Для **ground_truth** выберите **Источник данных** как **{$data.message}**.

    ![Оценка Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.ru.png)

1. Нажмите **Далее**.

1. Нажмите **Отправить**, чтобы начать оценку.

1. Оценка займет некоторое время. Вы можете отслеживать прогресс на вкладке **Оценка**.

### Просмотр результатов оценки

> [!NOTE]
> Результаты, представленные ниже, предназначены для иллюстрации процесса оценки. В этом руководстве использовалась модель, дообученная на относительно небольшом наборе данных, что может привести к неоптимальным результатам. Фактические результаты могут значительно отличаться в зависимости от размера, качества и разнообразия используемого набора данных, а также от конкретной конфигурации модели.

После завершения оценки вы можете просмотреть результаты по метрикам производительности и безопасности.

1. Метрики производительности и качества:

    - Оцените эффективность модели в создании связных, плавных и релевантных ответов.

    ![Результат оценки.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.ru.png)

1. Метрики риска и безопасности:

    - Убедитесь, что ответы модели безопасны и соответствуют принципам ответственного ИИ, избегая вредного или оскорбительного контента.

    ![Результат оценки.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.ru.png)

1. Вы можете прокрутить вниз, чтобы увидеть **Детализированные результаты метрик**.

    ![Результат оценки.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.ru.png)

1. Оценивая вашу индивидуальную модель Phi-3 / Phi-3.5 по метрикам производительности и безопасности, вы можете подтвердить, что модель не только эффективна, но и соответствует принципам ответственного ИИ, что делает её готовой к реальному использованию.

## Поздравляем!

### Вы завершили это руководство

Вы успешно провели оценку дообученной модели Phi-3, интегрированной с Prompt flow в Azure AI Foundry. Это важный шаг для обеспечения того, чтобы ваши модели ИИ не только демонстрировали высокую производительность, но и соответствовали принципам ответственного ИИ Microsoft, помогая вам создавать надежные и заслуживающие доверия приложения на основе ИИ.

![Архитектура.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.ru.png)

## Очистка ресурсов Azure

Очистите свои ресурсы Azure, чтобы избежать дополнительных затрат на вашем аккаунте. Перейдите в портал Azure и удалите следующие ресурсы:

- Ресурс Azure Machine Learning.
- Конечную точку модели Azure Machine Learning.
- Ресурс проекта Azure AI Foundry.
- Ресурс Prompt flow в Azure AI Foundry.

### Следующие шаги

#### Документация

- [Оценка систем ИИ с использованием панели ответственного ИИ](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрики оценки и мониторинга для генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документация Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документация Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Учебные материалы

- [Введение в подход Microsoft к ответственному ИИ](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Введение в Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Справочные материалы

- [Что такое ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Анонс новых инструментов в Azure AI для создания более безопасных и надежных генеративных приложений ИИ](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Оценка генеративных приложений ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматизированных сервисов перевода на основе искусственного интеллекта. Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные интерпретации, возникшие в результате использования этого перевода.