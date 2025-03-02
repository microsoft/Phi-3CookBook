# Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry

Този пример от край до край (E2E) е базиран на ръководството "[Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt Flow в Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" от Microsoft Tech Community. То представя процесите за фина настройка, внедряване и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry.  
За разлика от примера "[Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", който включва изпълнение на код локално, това ръководство се фокусира изцяло върху фината настройка и интеграция на вашия модел в Azure AI / ML Studio.

## Обзор

В този пример от край до край ще научите как да направите фина настройка на Phi-3 модела и да го интегрирате с Prompt flow в Azure AI Foundry. Използвайки Azure AI / ML Studio, ще установите работен процес за внедряване и използване на персонализирани AI модели. Този пример е разделен на три сценария:

**Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка**

**Сценарий 2: Фина настройка на Phi-3 модела и внедряване в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и чат с персонализирания ви модел в Azure AI Foundry**

Ето обзор на този пример от край до край.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.bg.png)

### Съдържание

1. **[Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
   - [Създаване на работно пространство за Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Заявка за GPU квоти в Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Добавяне на ролево присвояване](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Настройка на проект](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Подготовка на датасет за фина настройка](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Сценарий 2: Фина настройка на Phi-3 модела и внедряване в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
   - [Фина настройка на Phi-3 модела](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Внедряване на фино настроения Phi-3 модел](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Сценарий 3: Интеграция с Prompt flow и чат с персонализирания ви модел в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
   - [Интеграция на персонализирания Phi-3 модел с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Чат с персонализирания ви Phi-3 модел](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка

### Създаване на работно пространство за Azure Machine Learning

1. Въведете *azure machine learning* в **търсачката** в горната част на портала и изберете **Azure Machine Learning** от предложените опции.

    ![Въведете azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.bg.png)

2. Изберете **+ Create** от менюто за навигация.

3. Изберете **New workspace** от менюто за навигация.

    ![Изберете ново работно пространство.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.bg.png)

4. Изпълнете следните стъпки:

    - Изберете вашия Azure **Subscription**.  
    - Изберете **Resource group** (създайте нова, ако е необходимо).  
    - Въведете **Име на работното пространство**. То трябва да е уникално.  
    - Изберете **Регион**, който искате да използвате.  
    - Изберете **Storage account** (създайте нов, ако е необходимо).  
    - Изберете **Key vault** (създайте нов, ако е необходимо).  
    - Изберете **Application insights** (създайте нов, ако е необходимо).  
    - Изберете **Container registry** (създайте нов, ако е необходимо).  

    ![Попълнете полетата за Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.bg.png)

5. Изберете **Review + Create**.

6. Изберете **Create**.

### Заявка за GPU квоти в Azure Subscription

В това ръководство ще научите как да направите фина настройка и внедряване на Phi-3 модел, използвайки GPU. За фината настройка ще използвате GPU *Standard_NC24ads_A100_v4*, което изисква заявка за квота. За внедряване ще използвате GPU *Standard_NC6s_v3*, което също изисква заявка за квота.

> [!NOTE]  
> Само абонаменти Pay-As-You-Go (стандартният тип абонамент) са допустими за GPU разпределение; абонаментите с предимства в момента не се поддържат.

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изпълнете следните стъпки, за да заявите квота за *Standard NCADSA100v4 Family*:

    - Изберете **Quota** от лявото меню.  
    - Изберете **Virtual machine family**, която искате да използвате. Например, изберете **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, което включва GPU *Standard_NC24ads_A100_v4*.  
    - Изберете **Request quota** от менюто за навигация.  

        ![Заявка за квота.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.bg.png)

    - В страницата за заявка за квота въведете **Нов лимит за ядра**, който искате да използвате. Например, 24.  
    - В страницата за заявка за квота изберете **Submit**, за да подадете заявката за GPU квота.  

1. Изпълнете следните стъпки, за да заявите квота за *Standard NCSv3 Family*:

    - Изберете **Quota** от лявото меню.  
    - Изберете **Virtual machine family**, която искате да използвате. Например, изберете **Standard NCSv3 Family Cluster Dedicated vCPUs**, което включва GPU *Standard_NC6s_v3*.  
    - Изберете **Request quota** от менюто за навигация.  
    - В страницата за заявка за квота въведете **Нов лимит за ядра**, който искате да използвате. Например, 24.  
    - В страницата за заявка за квота изберете **Submit**, за да подадете заявката за GPU квота.  

### Добавяне на ролево присвояване

За да направите фина настройка и внедряване на вашите модели, първо трябва да създадете потребителска управлявана идентичност (UAI) и да ѝ присвоите подходящите разрешения. Тази UAI ще се използва за удостоверяване по време на внедряването.

#### Създаване на потребителска управлявана идентичност (UAI)

1. Въведете *managed identities* в **търсачката** в горната част на портала и изберете **Managed Identities** от предложените опции.

    ![Въведете managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.bg.png)

1. Изберете **+ Create**.

    ![Изберете създаване.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.bg.png)

1. Изпълнете следните стъпки:

    - Изберете вашия Azure **Subscription**.  
    - Изберете **Resource group** (създайте нова, ако е необходимо).  
    - Изберете **Регион**, който искате да използвате.  
    - Въведете **Име**. То трябва да е уникално.  

    ![Попълнете информация за управляваната идентичност.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.bg.png)

1. Изберете **Review + create**.

1. Изберете **+ Create**.

#### Добавяне на роля "Contributor" към управляваната идентичност

1. Навигирайте до ресурса за управляваната идентичност, който създадохте.

1. Изберете **Azure role assignments** от лявото меню.

1. Изберете **+ Add role assignment** от менюто за навигация.

1. В страницата за добавяне на роля изпълнете следните стъпки:
    - Изберете **Обхват** на **Resource group**.  
    - Изберете вашия Azure **Subscription**.  
    - Изберете **Resource group**, който ще използвате.  
    - Изберете **Роля** на **Contributor**.  

    ![Попълнете информация за роля Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.bg.png)

2. Изберете **Save**.  

...
1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете **Compute** от лявото меню.

1. Изберете **Compute clusters** от навигационното меню.

1. Изберете **+ New**.

    ![Изберете изчислителен ресурс.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Region**, който искате да използвате.
    - Изберете **Virtual machine tier** на **Dedicated**.
    - Изберете **Virtual machine type** на **GPU**.
    - Изберете **Virtual machine size** филтър на **Select from all options**.
    - Изберете **Virtual machine size** на **Standard_NC24ads_A100_v4**.

    ![Създайте клъстер.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.bg.png)

1. Изберете **Next**.

1. Изпълнете следните задачи:

    - Въведете **Compute name**. Трябва да бъде уникално.
    - Изберете **Minimum number of nodes** на **0**.
    - Изберете **Maximum number of nodes** на **1**.
    - Изберете **Idle seconds before scale down** на **120**.

    ![Създайте клъстер.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.bg.png)

1. Изберете **Create**.

#### Фина настройка на модела Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете работното пространство Azure Machine Learning, което сте създали.

    ![Изберете работното пространство, което сте създали.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Model catalog** от лявото меню.
    - Въведете *phi-3-mini-4k* в **търсачката** и изберете **Phi-3-mini-4k-instruct** от предложените опции.

    ![Въведете phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.bg.png)

1. Изберете **Fine-tune** от навигационното меню.

    ![Изберете фина настройка.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Select task type** на **Chat completion**.
    - Изберете **+ Select data**, за да качите **Training data**.
    - Изберете тип качване на Validation data на **Provide different validation data**.
    - Изберете **+ Select data**, за да качите **Validation data**.

    ![Попълнете страницата за фина настройка.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.bg.png)

    > [!TIP]
    >
    > Можете да изберете **Advanced settings**, за да персонализирате конфигурации като **learning_rate** и **lr_scheduler_type**, за да оптимизирате процеса на фина настройка според вашите специфични нужди.

1. Изберете **Finish**.

1. В това упражнение успешно направихте фина настройка на модела Phi-3, използвайки Azure Machine Learning. Имайте предвид, че процесът на фина настройка може да отнеме значително време. След стартирането на задачата за фина настройка трябва да изчакате тя да завърши. Можете да следите статуса на задачата за фина настройка, като отидете на раздела Jobs в лявото меню на вашето Azure Machine Learning Workspace. В следващата серия ще разгърнете финално настроения модел и ще го интегрирате с Prompt Flow.

    ![Вижте задачата за фина настройка.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.bg.png)

### Разгръщане на финално настроения модел Phi-3

За да интегрирате финално настроения модел Phi-3 с Prompt Flow, трябва да разположите модела, за да го направите достъпен за реалновремеви прогнози. Този процес включва регистриране на модела, създаване на онлайн крайна точка и разгръщане на модела.

В това упражнение ще:

- Регистрирате финално настроения модел в работното пространство на Azure Machine Learning.
- Създадете онлайн крайна точка.
- Разположите регистрирания финално настроен модел Phi-3.

#### Регистриране на финално настроения модел

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете работното пространство Azure Machine Learning, което сте създали.

    ![Изберете работното пространство, което сте създали.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.bg.png)

1. Изберете **Models** от лявото меню.
1. Изберете **+ Register**.
1. Изберете **From a job output**.

    ![Регистрирайте модела.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.bg.png)

1. Изберете задачата, която сте създали.

    ![Изберете задача.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.bg.png)

1. Изберете **Next**.

1. Изберете **Model type** на **MLflow**.

1. Уверете се, че **Job output** е избрано; трябва да е автоматично избрано.

    ![Изберете изход.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.bg.png)

2. Изберете **Next**.

3. Изберете **Register**.

    ![Изберете регистриране.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.bg.png)

4. Можете да видите регистрирания си модел, като отидете в менюто **Models** от лявото меню.

    ![Регистриран модел.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.bg.png)

#### Разгръщане на финално настроения модел

1. Отидете в работното пространство Azure Machine Learning, което сте създали.

1. Изберете **Endpoints** от лявото меню.

1. Изберете **Real-time endpoints** от навигационното меню.

    ![Създайте крайна точка.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.bg.png)

1. Изберете **Create**.

1. Изберете регистрирания модел, който сте създали.

    ![Изберете регистрирания модел.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.bg.png)

1. Изберете **Select**.

1. Изпълнете следните задачи:

    - Изберете **Virtual machine** на *Standard_NC6s_v3*.
    - Изберете **Instance count**, който искате да използвате. Например, *1*.
    - Изберете **Endpoint** на **New**, за да създадете крайна точка.
    - Въведете **Endpoint name**. Трябва да бъде уникално.
    - Въведете **Deployment name**. Трябва да бъде уникално.

    ![Попълнете настройките за разгръщане.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.bg.png)

1. Изберете **Deploy**.

> [!WARNING]
> За да избегнете допълнителни такси по вашия акаунт, уверете се, че сте изтрили създадената крайна точка в работното пространство Azure Machine Learning.
>

#### Проверка на статуса на разгръщане в Azure Machine Learning Workspace

1. Отидете в работното пространство Azure Machine Learning, което сте създали.

1. Изберете **Endpoints** от лявото меню.

1. Изберете крайна точка, която сте създали.

    ![Изберете крайни точки.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.bg.png)

1. На тази страница можете да управлявате крайните точки по време на процеса на разгръщане.

> [!NOTE]
> След като разгръщането приключи, уверете се, че **Live traffic** е настроен на **100%**. Ако не е, изберете **Update traffic**, за да коригирате настройките за трафика. Имайте предвид, че не можете да тествате модела, ако трафикът е настроен на 0%.
>
> ![Настройте трафика.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.bg.png)
> 

## Сценарий 3: Интеграция с Prompt Flow и чат с вашия персонализиран модел в Azure AI Foundry

### Интегриране на персонализирания модел Phi-3 с Prompt Flow

След успешното разгръщане на финално настроения модел, вече можете да го интегрирате с Prompt Flow, за да го използвате в реалновремеви приложения, позволявайки различни интерактивни задачи с вашия персонализиран модел Phi-3.

В това упражнение ще:

- Създадете Azure AI Foundry Hub.
- Създадете Azure AI Foundry Project.
- Създадете Prompt Flow.
- Добавите персонализирана връзка за финално настроения модел Phi-3.
- Настроите Prompt Flow за чат с вашия персонализиран модел Phi-3.

> [!NOTE]
> Можете също така да интегрирате с Prompt Flow, използвайки Azure ML Studio. Същият процес на интеграция може да се приложи към Azure ML Studio.

#### Създаване на Azure AI Foundry Hub

Трябва да създадете Hub преди да създадете Project. Hub действа като Resource Group, позволявайки ви да организирате и управлявате множество проекти в Azure AI Foundry.

1. Посетете [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Изберете **All hubs** от лявото меню.

1. Изберете **+ New hub** от навигационното меню.

    ![Създайте Hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.bg.png)

1. Изпълнете следните задачи:

    - Въведете **Hub name**. Трябва да бъде уникално.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Location**, който искате да използвате.
    - Изберете **Connect Azure AI Services**, които да използвате (създайте нов, ако е необходимо).
    - Изберете **Connect Azure AI Search** на **Skip connecting**.

    ![Попълнете Hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.bg.png)

1. Изберете **Next**.

#### Създаване на Azure AI Foundry Project

1. В Hub, който сте създали, изберете **All projects** от лявото меню.

1. Изберете **+ New project** от навигационното меню.

    ![Изберете нов проект.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.bg.png)

1. Въведете **Project name**. Трябва да бъде уникално.

    ![Създайте проект.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.bg.png)

1. Изберете **Create a project**.

#### Добавяне на персонализирана връзка за финално настроения модел Phi-3

За да интегрирате вашия персонализиран модел Phi-3 с Prompt Flow, трябва да запазите крайната точка и ключа на модела в персонализирана връзка. Тази настройка осигурява достъп до вашия персонализиран модел Phi-3 в Prompt Flow.

#### Задаване на API ключ и URI на крайната точка на финално настроения модел Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Отидете в работното пространство Azure Machine Learning, което сте създали.

1. Изберете **Endpoints** от лявото меню.

    ![Изберете крайни точки.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.bg.png)

1. Изберете крайната точка, която сте създали.

    ![Изберете крайните точки.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.bg.png)

1. Изберете **Consume** от навигационното меню.

1. Копирайте вашия **REST endpoint** и **Primary key**.
![Копирайте API ключа и URI на крайна точка.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.bg.png)

#### Добавяне на персонализирана връзка

1. Посетете [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Навигирайте до проекта в Azure AI Foundry, който сте създали.

1. В проекта, който сте създали, изберете **Settings** от страничното меню вляво.

1. Изберете **+ New connection**.

    ![Изберете нова връзка.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.bg.png)

1. Изберете **Custom keys** от навигационното меню.

    ![Изберете персонализирани ключове.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.bg.png)

1. Изпълнете следните стъпки:

    - Изберете **+ Add key value pairs**.
    - За името на ключа въведете **endpoint** и поставете крайна точка, която сте копирали от Azure ML Studio, в полето за стойност.
    - Отново изберете **+ Add key value pairs**.
    - За името на ключа въведете **key** и поставете ключа, който сте копирали от Azure ML Studio, в полето за стойност.
    - След добавянето на ключовете, изберете **is secret**, за да предотвратите излагането на ключа.

    ![Добавяне на връзка.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.bg.png)

1. Изберете **Add connection**.

#### Създаване на Prompt flow

Добавихте персонализирана връзка в Azure AI Foundry. Сега нека създадем Prompt flow, като използваме следните стъпки. След това ще свържете този Prompt flow с персонализираната връзка, за да можете да използвате финно настроения модел в рамките на Prompt flow.

1. Навигирайте до проекта в Azure AI Foundry, който сте създали.

1. Изберете **Prompt flow** от страничното меню вляво.

1. Изберете **+ Create** от навигационното меню.

    ![Изберете Prompt flow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.bg.png)

1. Изберете **Chat flow** от навигационното меню.

    ![Изберете тип поток.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.bg.png)

1. Въведете **Име на папка**, която да използвате.

    ![Въведете име.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.bg.png)

2. Изберете **Create**.

#### Настройване на Prompt flow за чат с персонализирания Phi-3 модел

Трябва да интегрирате финно настроения Phi-3 модел в Prompt flow. Съществуващият Prompt flow обаче не е проектиран за тази цел. Затова трябва да преработите Prompt flow, за да позволите интеграцията на персонализирания модел.

1. В Prompt flow изпълнете следните стъпки, за да преработите съществуващия поток:

    - Изберете **Raw file mode**.
    - Изтрийте целия съществуващ код във файла *flow.dag.yml*.
    - Добавете следния код във файла *flow.dag.yml*.

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

    - Изберете **Save**.

    ![Изберете режим на суров файл.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.bg.png)

1. Добавете следния код във файла *integrate_with_promptflow.py*, за да използвате персонализирания Phi-3 модел в Prompt flow.

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

    ![Поставете код за Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.bg.png)

> [!NOTE]
> За по-подробна информация относно използването на Prompt flow в Azure AI Foundry, можете да се обърнете към [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изберете **Chat input**, **Chat output**, за да активирате чат с вашия модел.

    ![Вход и изход.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.bg.png)

1. Сега сте готови да чатите с вашия персонализиран Phi-3 модел. В следващото упражнение ще научите как да стартирате Prompt flow и да го използвате за чат с вашия финно настроен Phi-3 модел.

> [!NOTE]
>
> Преработеният поток трябва да изглежда като на изображението по-долу:
>
> ![Пример за поток.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.bg.png)
>

### Чат с вашия персонализиран Phi-3 модел

Сега, след като сте финно настроили и интегрирали вашия персонализиран Phi-3 модел с Prompt flow, сте готови да започнете да взаимодействате с него. Това упражнение ще ви преведе през процеса на настройка и стартиране на чат с вашия модел, използвайки Prompt flow. Следвайки тези стъпки, ще можете напълно да използвате възможностите на вашия финно настроен Phi-3 модел за различни задачи и разговори.

- Чат с вашия персонализиран Phi-3 модел, използвайки Prompt flow.

#### Стартиране на Prompt flow

1. Изберете **Start compute sessions**, за да стартирате Prompt flow.

    ![Стартирайте изчислителна сесия.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.bg.png)

1. Изберете **Validate and parse input**, за да обновите параметрите.

    ![Потвърдете входа.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.bg.png)

1. Изберете **Value** на **connection** към персонализираната връзка, която сте създали. Например, *connection*.

    ![Връзка.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.bg.png)

#### Чат с вашия персонализиран модел

1. Изберете **Chat**.

    ![Изберете чат.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.bg.png)

1. Ето пример за резултатите: Сега можете да чатите с вашия персонализиран Phi-3 модел. Препоръчително е да задавате въпроси, базирани на данните, използвани за финно настройване.

    ![Чат с Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.bg.png)

**Отказ от отговорност**:  
Този документ е преведен с помощта на машинни AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.