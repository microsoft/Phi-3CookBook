# Настройка и интеграция пользовательских моделей Phi-3 с Prompt flow в Azure AI Foundry

Этот пошаговый пример основан на руководстве "[Настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow в Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community. Он охватывает процессы настройки, развертывания и интеграции пользовательских моделей Phi-3 с Prompt flow в Azure AI Foundry.  
В отличие от другого примера, "[Настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", который предполагает выполнение кода локально, это руководство полностью сосредоточено на настройке и интеграции модели в Azure AI / ML Studio.

## Обзор

В этом пошаговом примере вы узнаете, как настроить модель Phi-3 и интегрировать её с Prompt flow в Azure AI Foundry. Используя Azure AI / ML Studio, вы создадите рабочий процесс для развертывания и использования пользовательских AI моделей. Этот пример состоит из трёх сценариев:

**Сценарий 1: Настройка ресурсов Azure и подготовка к настройке**

**Сценарий 2: Настройка модели Phi-3 и развертывание в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и взаимодействие с вашей моделью в Azure AI Foundry**

Ниже представлен обзор этого примера.

![Обзор Phi-3-FineTuning_PromptFlow_Integration.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ru.png)

### Содержание

1. **[Сценарий 1: Настройка ресурсов Azure и подготовка к настройке](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Создание рабочего пространства Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Запрос квот GPU в подписке Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Добавление назначения ролей](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Настройка проекта](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Подготовка набора данных для настройки](../../../../../../md/02.Application/01.TextAndChat/Phi3)

2. **[Сценарий 2: Настройка модели Phi-3 и развертывание в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Настройка модели Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Развертывание настроенной модели Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

3. **[Сценарий 3: Интеграция с Prompt flow и взаимодействие с вашей моделью в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Интеграция пользовательской модели Phi-3 с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Взаимодействие с вашей моделью Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарий 1: Настройка ресурсов Azure и подготовка к настройке

### Создание рабочего пространства Azure Machine Learning

1. Введите *azure machine learning* в **поисковой строке** в верхней части портала и выберите **Azure Machine Learning** из появившихся опций.

    ![Введите azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ru.png)

2. Выберите **+ Создать** в меню навигации.

3. Выберите **Новое рабочее пространство** в меню навигации.

    ![Выберите новое рабочее пространство.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ru.png)

4. Выполните следующие действия:

    - Выберите вашу **Подписку** Azure.  
    - Выберите **Группу ресурсов** (создайте новую, если необходимо).  
    - Укажите **Имя рабочего пространства**. Оно должно быть уникальным.  
    - Выберите **Регион**, который вы хотите использовать.  
    - Выберите **Учётную запись хранения** (создайте новую, если необходимо).  
    - Выберите **Key Vault** (создайте новый, если необходимо).  
    - Выберите **Application Insights** (создайте новый, если необходимо).  
    - Выберите **Реестр контейнеров** (создайте новый, если необходимо).  

    ![Заполните параметры Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ru.png)

5. Выберите **Обзор + Создать**.

6. Выберите **Создать**.

### Запрос квот GPU в подписке Azure

В этом руководстве вы научитесь настраивать и развертывать модель Phi-3, используя GPU. Для настройки потребуется GPU *Standard_NC24ads_A100_v4*, для которого необходимо запросить квоту. Для развертывания потребуется GPU *Standard_NC6s_v3*, который также требует запроса квоты.

> [!NOTE]  
> Только подписки Pay-As-You-Go (стандартный тип подписки) имеют право на выделение GPU; подписки с льготами в настоящее время не поддерживаются.

1. Перейдите в [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выполните следующие действия для запроса квоты на *Standard NCADSA100v4 Family*:

    - Выберите **Квота** в левой панели.  
    - Выберите **Семейство виртуальных машин**. Например, выберите **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, включающее GPU *Standard_NC24ads_A100_v4*.  
    - Выберите **Запросить квоту** в меню навигации.  

        ![Запросить квоту.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ru.png)

    - В странице запроса квоты укажите **Новый лимит ядер**. Например, 24.  
    - Нажмите **Отправить** для запроса квоты GPU.

1. Выполните аналогичные действия для запроса квоты на *Standard NCSv3 Family*:

    - Выберите **Квота** в левой панели.  
    - Выберите **Семейство виртуальных машин**. Например, выберите **Standard NCSv3 Family Cluster Dedicated vCPUs**, включающее GPU *Standard_NC6s_v3*.  
    - Выберите **Запросить квоту** в меню навигации.  
    - Укажите **Новый лимит ядер**. Например, 24.  
    - Нажмите **Отправить** для запроса квоты GPU.

### Добавление назначения ролей

Для настройки и развертывания моделей сначала необходимо создать Управляемую Идентичность Пользователя (UAI) и назначить ей соответствующие разрешения. Эта идентичность будет использоваться для аутентификации во время развертывания.

#### Создание Управляемой Идентичности Пользователя (UAI)

1. Введите *managed identities* в **поисковой строке** в верхней части портала и выберите **Managed Identities** из появившихся опций.

    ![Введите managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ru.png)

1. Выберите **+ Создать**.

    ![Выберите создать.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ru.png)

1. Выполните следующие действия:

    - Выберите вашу **Подписку** Azure.  
    - Выберите **Группу ресурсов** (создайте новую, если необходимо).  
    - Выберите **Регион**, который вы хотите использовать.  
    - Укажите **Имя**. Оно должно быть уникальным.  

    ![Заполните параметры для создания управляемой идентичности.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ru.png)

1. Выберите **Обзор + создать**.

1. Нажмите **Создать**.

#### Назначение роли Contributor управляемой идентичности

1. Перейдите к созданному ресурсу Управляемой Идентичности.

1. Выберите **Назначения ролей Azure** в левой панели.

1. Нажмите **+ Добавить назначение роли** в меню навигации.

1. На странице добавления роли выполните следующие действия:
    - Укажите **Область** как **Группа ресурсов**.  
    - Выберите вашу **Подписку** Azure.  
    - Выберите **Группу ресурсов**.  
    - Укажите **Роль** как **Contributor**.  

    ![Заполните параметры для роли Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ru.png)

2. Нажмите **Сохранить**.

#### Назначение роли Storage Blob Data Reader управляемой идентичности

1. Введите *storage accounts* в **поисковой строке** в верхней части портала и выберите **Storage accounts** из появившихся опций.

    ![Введите storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ru.png)

1. Выберите учётную запись хранения, связанную с созданным рабочим пространством Azure Machine Learning. Например, *finetunephistorage*.

1. Выполните следующие действия, чтобы перейти на страницу добавления роли:

    - Перейдите к учётной записи хранения.  
    - Выберите **Контроль доступа (IAM)** в левой панели.  
    - Нажмите **+ Добавить** в меню навигации.  
    - Выберите **Добавить назначение роли**.  

    ![Добавление роли.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ru.png)

1. На странице добавления роли выполните следующие действия:

    - Введите *Storage Blob Data Reader* в **поисковой строке** и выберите **Storage Blob Data Reader** из появившихся опций.  
    - Нажмите **Далее**.  
    - В разделе **Члены** выберите **Назначить доступ к** **Управляемой идентичности**.  
    - Нажмите **+ Выбрать участников**.  
    - Выберите вашу **Подписку** Azure.  
    - Выберите созданную Управляемую Идентичность. Например, *finetunephi-managedidentity*.  
    - Нажмите **Выбрать**.  

    ![Выберите управляемую идентичность.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ru.png)

1. Нажмите **Обзор + назначить**.

#### Назначение роли AcrPull управляемой идентичности

1. Введите *container registries* в **поисковой строке** в верхней части портала и выберите **Container registries** из появившихся опций.

    ![Введите container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ru.png)

1. Выберите реестр контейнеров, связанный с рабочим пространством Azure Machine Learning. Например, *finetunephicontainerregistry*.

1. Выполните следующие действия, чтобы перейти на страницу добавления роли:

    - Выберите **Контроль доступа (IAM)** в левой панели.  
    - Нажмите **+ Добавить** в меню навигации.  
    - Выберите **Добавить назначение роли**.  

1. На странице добавления роли выполните следующие действия:

    - Введите *AcrPull* в **поисковой строке** и выберите **AcrPull** из появившихся опций.  
    - Нажмите **Далее**.  
    - В разделе **Члены** выберите **Назначить доступ к** **Управляемой идентичности**.  
    - Нажмите **+ Выбрать участников**.  
    - Выберите вашу **Подписку** Azure.  
    - Выберите созданную Управляемую Идентичность. Например, *finetunephi-managedidentity*.  
    - Нажмите **Выбрать**.  
    - Нажмите **Обзор + назначить**.

### Настройка проекта

Для загрузки наборов данных, необходимых для настройки, вы создадите локальную среду.

В этом упражнении вы:

- Создадите папку для работы.  
- Создадите виртуальную среду.  
- Установите необходимые пакеты.  
- Создадите файл *download_dataset.py* для загрузки набора данных.

#### Создание папки для работы

1. Откройте терминал и выполните следующую команду для создания папки с именем *finetune-phi* в стандартном пути.

    ```console
    mkdir finetune-phi
    ```

2. Перейдите в созданную папку, выполнив команду:

    ```console
    cd finetune-phi
    ```

#### Создание виртуальной среды

1. Выполните следующую команду для создания виртуальной среды с именем *.venv*.

    ```console
    python -m venv .venv
    ```

2. Активируйте виртуальную среду, выполнив команду:

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> Если всё прошло успешно, перед приглашением командной строки должно появиться *(.venv)*.

#### Установка необходимых пакетов

1. Установите необходимые пакеты, выполнив команду:

    ```console
    pip install datasets==2.19.1
    ```

#### Создание файла `download_dataset.py`

> [!NOTE]  
> Структура папок:  
>  
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Откройте **Visual Studio Code**.

1. Выберите **Файл** в строке меню.

1. Выберите **Открыть папку**.

1. Выберите папку *finetune-phi*, расположенную по адресу *C:\Users\yourUserName\finetune-phi*.

    ![Выберите созданную папку.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.ru.png)

1. В левой панели Visual Studio Code щёлкните правой кнопкой мыши и выберите **Новый файл**, чтобы создать файл с именем *download_dataset.py*.

    ![Создайте новый файл.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.ru.png)

### Подготовка набора данных для настройки

В этом упражнении вы выполните файл *download_dataset.py*, чтобы загрузить набор данных *ultrachat_200k* в локальную среду. Затем вы будете использовать этот набор данных для настройки модели Phi-3 в Azure Machine Learning.

В этом упражнении вы:

- Добавите код в файл *download_dataset.py* для загрузки набора данных.  
- Выполните файл *download_dataset.py*, чтобы загрузить набор данных в локальную среду.

#### Загрузка набора данных с использованием *download_dataset.py*

1. Откройте файл *download_dataset.py* в Visual Studio Code.

1. Добавьте следующий код в файл *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Выполните следующую команду в терминале для запуска скрипта и загрузки набора данных в локальную среду.

    ```console
    python download_dataset.py
    ```

1. Убедитесь, что набор данных успешно сохранён в локальной директории *finetune-phi/data*.

> [!NOTE]  
>
> #### Примечание о размере набора данных и времени настройки  
>
> В этом руководстве используется только 1% набора данных (`split='train[:1%]'`). Это значительно уменьшает объём данных, ускоряя процессы загрузки и настройки. Вы можете изменить процент, чтобы найти баланс между временем обучения и производительностью модели. Использование меньшего поднабора данных делает процесс настройки более управляемым для учебного примера.

## Сценарий 2: Настройка модели Phi-3 и развертывание в Azure Machine Learning Studio

### Настройка модели Phi-3

В этом упражнении вы настроите модель Phi-3 в Azure Machine Learning Studio.

В этом упражнении вы:

- Создадите вычислительный кластер для настройки.  
- Настроите модель Phi-3 в Azure Machine Learning Studio.

#### Создание вычислительного кластера для настройки
1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите **Compute** в меню слева.

1. Выберите **Compute clusters** в навигации.

1. Нажмите **+ New**.

    ![Выберите compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ru.png)

1. Выполните следующие действия:

    - Выберите **Region**, который хотите использовать.
    - Установите **Virtual machine tier** на **Dedicated**.
    - Установите **Virtual machine type** на **GPU**.
    - В фильтре **Virtual machine size** выберите **Select from all options**.
    - Установите **Virtual machine size** на **Standard_NC24ads_A100_v4**.

    ![Создайте кластер.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ru.png)

1. Нажмите **Next**.

1. Выполните следующие действия:

    - Укажите **Compute name**. Имя должно быть уникальным.
    - Установите **Minimum number of nodes** на **0**.
    - Установите **Maximum number of nodes** на **1**.
    - Установите **Idle seconds before scale down** на **120**.

    ![Создайте кластер.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ru.png)

1. Нажмите **Create**.

#### Тонкая настройка модели Phi-3

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите рабочую область Azure Machine Learning, которую вы создали.

    ![Выберите созданную рабочую область.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ru.png)

1. Выполните следующие действия:

    - Выберите **Model catalog** в меню слева.
    - Введите *phi-3-mini-4k* в строке поиска и выберите **Phi-3-mini-4k-instruct** из предложенных вариантов.

    ![Введите phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ru.png)

1. Выберите **Fine-tune** в навигации.

    ![Выберите fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ru.png)

1. Выполните следующие действия:

    - Установите **Select task type** на **Chat completion**.
    - Нажмите **+ Select data**, чтобы загрузить **Training data**.
    - Установите тип загрузки Validation data на **Provide different validation data**.
    - Нажмите **+ Select data**, чтобы загрузить **Validation data**.

    ![Заполните страницу настройки.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ru.png)

    > [!TIP]
    >
    > Вы можете выбрать **Advanced settings**, чтобы настроить такие параметры, как **learning_rate** и **lr_scheduler_type**, для оптимизации процесса тонкой настройки в соответствии с вашими потребностями.

1. Нажмите **Finish**.

1. В этом упражнении вы успешно провели тонкую настройку модели Phi-3 с помощью Azure Machine Learning. Обратите внимание, что процесс тонкой настройки может занять значительное время. После запуска задания на тонкую настройку вам нужно дождаться его завершения. Вы можете отслеживать статус задания, перейдя на вкладку Jobs в левой части вашей рабочей области Azure Machine Learning. В следующей серии вы развернете настроенную модель и интегрируете ее с Prompt flow.

    ![Просмотр задания на тонкую настройку.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ru.png)

### Развертывание настроенной модели Phi-3

Чтобы интегрировать настроенную модель Phi-3 с Prompt flow, необходимо развернуть модель для обеспечения доступа в режиме реального времени. Этот процесс включает регистрацию модели, создание онлайн-эндпоинта и развертывание модели.

В этом упражнении вы:

- Зарегистрируете настроенную модель в рабочей области Azure Machine Learning.
- Создадите онлайн-эндпоинт.
- Развернете зарегистрированную настроенную модель Phi-3.

#### Регистрация настроенной модели

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите рабочую область Azure Machine Learning, которую вы создали.

    ![Выберите созданную рабочую область.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ru.png)

1. Выберите **Models** в меню слева.
1. Нажмите **+ Register**.
1. Выберите **From a job output**.

    ![Регистрация модели.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ru.png)

1. Выберите созданное вами задание.

    ![Выберите задание.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ru.png)

1. Нажмите **Next**.

1. Установите **Model type** на **MLflow**.

1. Убедитесь, что **Job output** выбран автоматически.

    ![Выберите выходные данные.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ru.png)

2. Нажмите **Next**.

3. Нажмите **Register**.

    ![Нажмите Register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ru.png)

4. Вы можете просмотреть зарегистрированную модель, перейдя в меню **Models** в левой части экрана.

    ![Зарегистрированная модель.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ru.png)

#### Развертывание настроенной модели

1. Перейдите в созданную рабочую область Azure Machine Learning.

1. Выберите **Endpoints** в меню слева.

1. Выберите **Real-time endpoints** в навигации.

    ![Создание эндпоинта.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ru.png)

1. Нажмите **Create**.

1. Выберите зарегистрированную модель, которую вы создали.

    ![Выберите зарегистрированную модель.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ru.png)

1. Нажмите **Select**.

1. Выполните следующие действия:

    - Установите **Virtual machine** на *Standard_NC6s_v3*.
    - Укажите **Instance count**, например, *1*.
    - Установите **Endpoint** на **New**, чтобы создать эндпоинт.
    - Введите **Endpoint name**. Имя должно быть уникальным.
    - Введите **Deployment name**. Имя должно быть уникальным.

    ![Заполните настройки развертывания.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ru.png)

1. Нажмите **Deploy**.

> [!WARNING]
> Чтобы избежать дополнительных затрат на вашем аккаунте, убедитесь, что вы удалили созданный эндпоинт в рабочей области Azure Machine Learning.
>

#### Проверка статуса развертывания в рабочей области Azure Machine Learning

1. Перейдите в созданную рабочую область Azure Machine Learning.

1. Выберите **Endpoints** в меню слева.

1. Выберите созданный вами эндпоинт.

    ![Выберите эндпоинты.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ru.png)

1. На этой странице вы можете управлять эндпоинтами во время процесса развертывания.

> [!NOTE]
> После завершения развертывания убедитесь, что **Live traffic** установлен на **100%**. Если это не так, выберите **Update traffic**, чтобы настроить параметры трафика. Обратите внимание, что вы не сможете протестировать модель, если трафик установлен на 0%.
>
> ![Настройка трафика.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ru.png)
>

## Сценарий 3: Интеграция с Prompt flow и общение с вашей пользовательской моделью в Azure AI Foundry

### Интеграция пользовательской модели Phi-3 с Prompt flow

После успешного развертывания вашей настроенной модели вы можете интегрировать ее с Prompt Flow, чтобы использовать модель в приложениях реального времени, выполняя различные интерактивные задачи с вашей пользовательской моделью Phi-3.

В этом упражнении вы:

- Создадите Azure AI Foundry Hub.
- Создадите Azure AI Foundry Project.
- Создадите Prompt flow.
- Добавите пользовательское подключение для настроенной модели Phi-3.
- Настроите Prompt flow для общения с вашей пользовательской моделью Phi-3.

> [!NOTE]
> Вы также можете интегрировать Promptflow с помощью Azure ML Studio. Процесс интеграции аналогичен.

#### Создание Azure AI Foundry Hub

Прежде чем создавать проект, необходимо создать Hub. Hub действует как группа ресурсов, позволяя организовывать и управлять несколькими проектами в Azure AI Foundry.

1. Посетите [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Выберите **All hubs** в меню слева.

1. Нажмите **+ New hub** в навигации.

    ![Создание хаба.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ru.png)

1. Выполните следующие действия:

    - Введите **Hub name**. Имя должно быть уникальным.
    - Выберите свою подписку Azure **Subscription**.
    - Укажите **Resource group** (создайте новую, если необходимо).
    - Укажите **Location**, который хотите использовать.
    - Выберите **Connect Azure AI Services** (создайте новый, если необходимо).
    - Установите **Connect Azure AI Search** на **Skip connecting**.

    ![Заполните хаб.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ru.png)

1. Нажмите **Next**.

#### Создание Azure AI Foundry Project

1. В созданном вами хабе выберите **All projects** в меню слева.

1. Нажмите **+ New project** в навигации.

    ![Выберите новый проект.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ru.png)

1. Укажите **Project name**. Имя должно быть уникальным.

    ![Создание проекта.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ru.png)

1. Нажмите **Create a project**.

#### Добавление пользовательского подключения для настроенной модели Phi-3

Для интеграции вашей пользовательской модели Phi-3 с Prompt flow необходимо сохранить эндпоинт и ключ модели в пользовательском подключении. Это обеспечит доступ к вашей модели Phi-3 в Prompt flow.

#### Установка API-ключа и URI эндпоинта настроенной модели Phi-3

1. Посетите [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдите в созданную рабочую область Azure Machine Learning.

1. Выберите **Endpoints** в меню слева.

    ![Выберите эндпоинты.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ru.png)

1. Выберите созданный вами эндпоинт.

    ![Выберите эндпоинты.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ru.png)

1. Выберите **Consume** в навигации.

1. Скопируйте ваш **REST endpoint** и **Primary key**.
![Скопируйте ключ API и URI конечной точки.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ru.png)

#### Добавление пользовательского подключения

1. Перейдите на [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Откройте проект Azure AI Foundry, который вы создали.

1. В созданном проекте выберите **Settings** в левой панели.

1. Нажмите **+ New connection**.

    ![Выберите новое подключение.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ru.png)

1. В меню навигации выберите **Custom keys**.

    ![Выберите пользовательские ключи.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ru.png)

1. Выполните следующие действия:

    - Нажмите **+ Add key value pairs**.
    - В поле имени ключа введите **endpoint** и вставьте конечную точку, которую вы скопировали из Azure ML Studio, в поле значения.
    - Снова нажмите **+ Add key value pairs**.
    - В поле имени ключа введите **key** и вставьте ключ, который вы скопировали из Azure ML Studio, в поле значения.
    - После добавления ключей выберите **is secret**, чтобы ключ не был видимым.

    ![Добавьте подключение.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ru.png)

1. Нажмите **Add connection**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Azure AI Foundry. Теперь давайте создадим Prompt flow, используя следующие шаги. Затем вы подключите этот Prompt flow к пользовательскому подключению, чтобы использовать настроенную модель в рамках Prompt flow.

1. Откройте проект Azure AI Foundry, который вы создали.

1. Выберите **Prompt flow** в левой панели.

1. Нажмите **+ Create** в меню навигации.

    ![Выберите Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ru.png)

1. В меню навигации выберите **Chat flow**.

    ![Выберите тип потока.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ru.png)

1. Введите **Folder name**, который вы хотите использовать.

    ![Введите имя.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ru.png)

2. Нажмите **Create**.

#### Настройка Prompt flow для общения с вашей пользовательской моделью Phi-3

Вам нужно интегрировать настроенную модель Phi-3 в Prompt flow. Однако текущий Prompt flow не предназначен для этой цели. Поэтому вам необходимо переработать существующий поток, чтобы обеспечить интеграцию пользовательской модели.

1. В Prompt flow выполните следующие действия для перестройки существующего потока:

    - Выберите **Raw file mode**.
    - Удалите весь существующий код в файле *flow.dag.yml*.
    - Добавьте следующий код в файл *flow.dag.yml*.

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

    - Нажмите **Save**.

    ![Выберите режим Raw file.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ru.png)

1. Добавьте следующий код в файл *integrate_with_promptflow.py*, чтобы использовать пользовательскую модель Phi-3 в Prompt flow.

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
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
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
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Вставьте код Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ru.png)

> [!NOTE]
> Для получения более подробной информации о работе с Prompt flow в Azure AI Foundry вы можете обратиться к [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Выберите **Chat input**, **Chat output**, чтобы включить возможность общения с вашей моделью.

    ![Ввод и вывод.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ru.png)

1. Теперь вы готовы общаться с вашей пользовательской моделью Phi-3. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с вашей настроенной моделью Phi-3.

> [!NOTE]
>
> Перестроенный поток должен выглядеть, как на изображении ниже:
>
> ![Пример потока.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ru.png)
>

### Общение с вашей пользовательской моделью Phi-3

Теперь, когда вы настроили и интегрировали вашу пользовательскую модель Phi-3 с Prompt flow, вы можете начать взаимодействие с ней. Это упражнение поможет вам настроить и запустить чат с вашей моделью с использованием Prompt flow. Следуя этим шагам, вы сможете в полной мере использовать возможности вашей настроенной модели Phi-3 для различных задач и диалогов.

- Общайтесь с вашей пользовательской моделью Phi-3, используя Prompt flow.

#### Запуск Prompt flow

1. Выберите **Start compute sessions**, чтобы запустить Prompt flow.

    ![Запустите вычислительную сессию.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ru.png)

1. Выберите **Validate and parse input**, чтобы обновить параметры.

    ![Проверьте ввод.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ru.png)

1. Выберите **Value** для **connection** в вашем пользовательском подключении. Например, *connection*.

    ![Подключение.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ru.png)

#### Общение с вашей пользовательской моделью

1. Выберите **Chat**.

    ![Выберите чат.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ru.png)

1. Вот пример результатов: Теперь вы можете общаться с вашей пользовательской моделью Phi-3. Рекомендуется задавать вопросы на основе данных, использованных для настройки.

    ![Чат с Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ru.png)

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматических сервисов перевода на основе искусственного интеллекта. Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.