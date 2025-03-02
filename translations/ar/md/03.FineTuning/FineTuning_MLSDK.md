## كيفية استخدام مكونات إكمال المحادثة من سجل نظام Azure ML لتخصيص نموذج

في هذا المثال، سنقوم بتخصيص نموذج Phi-3-mini-4k-instruct لإكمال محادثة بين شخصين باستخدام مجموعة بيانات ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.ar.png)

سيعرض هذا المثال كيفية إجراء التخصيص باستخدام Azure ML SDK وPython ثم نشر النموذج المخصص إلى نقطة نهاية عبر الإنترنت للحصول على استنتاج في الوقت الفعلي.

### بيانات التدريب

سنستخدم مجموعة بيانات ultrachat_200k. هذه نسخة مفلترة بشكل كبير من مجموعة بيانات UltraChat وتم استخدامها لتدريب Zephyr-7B-β، وهو نموذج محادثة متقدم يحتوي على 7 مليارات معلمة.

### النموذج

سنستخدم نموذج Phi-3-mini-4k-instruct لشرح كيفية تخصيص نموذج لمهمة إكمال المحادثة. إذا فتحت هذا الدفتر من بطاقة نموذج معينة، تذكر استبدال اسم النموذج المحدد.

### المهام

- اختيار نموذج لتخصيصه.
- اختيار واستكشاف بيانات التدريب.
- إعداد وظيفة التخصيص.
- تشغيل وظيفة التخصيص.
- مراجعة مقاييس التدريب والتقييم.
- تسجيل النموذج المخصص.
- نشر النموذج المخصص للحصول على استنتاج في الوقت الفعلي.
- تنظيف الموارد.

## 1. إعداد المتطلبات الأساسية

- تثبيت التبعيات.
- الاتصال بـ AzureML Workspace. لمعرفة المزيد، اقرأ إعداد مصادقة SDK. استبدل <WORKSPACE_NAME> و<RESOURCE_GROUP> و<SUBSCRIPTION_ID> أدناه.
- الاتصال بسجل نظام AzureML.
- تعيين اسم تجربة اختياري.
- التحقق أو إنشاء الحوسبة.

> [!NOTE]
> تتطلب الوظيفة عقدة GPU واحدة يمكن أن تحتوي على عدة بطاقات GPU. على سبيل المثال، تحتوي عقدة واحدة من Standard_NC24rs_v3 على 4 بطاقات NVIDIA V100، بينما تحتوي Standard_NC12s_v3 على بطاقتين NVIDIA V100. راجع المستندات للحصول على هذه المعلومات. يتم تحديد عدد بطاقات GPU لكل عقدة في المعامل gpus_per_node أدناه. تعيين هذه القيمة بشكل صحيح سيضمن استخدام جميع بطاقات GPU في العقدة. يمكن العثور على توصيات الحوسبة GPU هنا وهنا.

### مكتبات Python

قم بتثبيت التبعيات عن طريق تشغيل الخلية أدناه. هذه خطوة غير اختيارية إذا كنت تعمل في بيئة جديدة.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### التفاعل مع Azure ML

1. هذا النص البرمجي Python يُستخدم للتفاعل مع خدمة Azure Machine Learning (Azure ML). إليك ما يقوم به:

    - يستورد الوحدات اللازمة من azure.ai.ml، azure.identity، وazure.ai.ml.entities، بالإضافة إلى وحدة time.

    - يحاول المصادقة باستخدام DefaultAzureCredential()، الذي يوفر تجربة مصادقة مبسطة لبدء تطوير التطبيقات بسرعة في السحابة Azure. إذا فشل ذلك، فإنه ينتقل إلى InteractiveBrowserCredential()، الذي يوفر مطالبة تسجيل دخول تفاعلية.

    - يحاول بعد ذلك إنشاء مثيل MLClient باستخدام طريقة from_config التي تقرأ التكوين من ملف التكوين الافتراضي (config.json). إذا فشل ذلك، فإنه ينشئ مثيل MLClient يدويًا عن طريق تقديم subscription_id وresource_group_name وworkspace_name.

    - ينشئ مثيلًا آخر لـ MLClient، هذه المرة لسجل Azure ML باسم "azureml". هذا السجل هو المكان الذي يتم فيه تخزين النماذج وخطوط أنابيب التخصيص والبيئات.

    - يحدد experiment_name بـ "chat_completion_Phi-3-mini-4k-instruct".

    - يُنشئ طابعًا زمنيًا فريدًا عن طريق تحويل الوقت الحالي (بالثواني منذ العصر، كرقم عشري) إلى عدد صحيح ثم إلى سلسلة نصية. يمكن استخدام هذا الطابع الزمني لإنشاء أسماء وإصدارات فريدة.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. اختيار نموذج أساسي للتخصيص

1. Phi-3-mini-4k-instruct هو نموذج يحتوي على 3.8 مليار معلمة، خفيف الوزن، وحديث، يعتمد على مجموعات البيانات المستخدمة لنموذج Phi-2. ينتمي النموذج إلى عائلة Phi-3، ويأتي الإصدار Mini في نسختين 4K و128K وهي طول السياق (بالرموز) الذي يمكنه دعمه. نحتاج إلى تخصيص النموذج لغرضنا المحدد لاستخدامه. يمكنك تصفح هذه النماذج في كتالوج النماذج في AzureML Studio، مع التصفية حسب مهمة إكمال المحادثة. في هذا المثال، نستخدم نموذج Phi-3-mini-4k-instruct. إذا فتحت هذا الدفتر لنموذج مختلف، استبدل اسم النموذج والإصدار وفقًا لذلك.

    > [!NOTE]
    > الخاصية model id للنموذج. سيتم تمريرها كمدخل لوظيفة التخصيص. هذه الخاصية متوفرة أيضًا كحقل Asset ID في صفحة تفاصيل النموذج في كتالوج نماذج AzureML Studio.

2. هذا النص البرمجي Python يتفاعل مع خدمة Azure Machine Learning (Azure ML). إليك ما يقوم به:

    - يحدد model_name بـ "Phi-3-mini-4k-instruct".

    - يستخدم طريقة get الخاصة بـ models property لكائن registry_ml_client لاسترداد أحدث إصدار من النموذج بالاسم المحدد من سجل Azure ML. يتم استدعاء طريقة get بوسيطين: اسم النموذج وعلامة تشير إلى أنه يجب استرداد أحدث إصدار من النموذج.

    - يطبع رسالة إلى وحدة التحكم تشير إلى اسم وإصدار ومعرف النموذج الذي سيتم استخدامه للتخصيص. يتم استخدام طريقة format للسلسلة النصية لإدراج اسم وإصدار ومعرف النموذج في الرسالة. يتم الوصول إلى اسم وإصدار ومعرف النموذج كخصائص لكائن foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. إنشاء حوسبة لاستخدامها مع الوظيفة

تعمل وظيفة التخصيص فقط مع حوسبة GPU. يعتمد حجم الحوسبة على حجم النموذج، وفي معظم الحالات يصبح من الصعب تحديد الحوسبة المناسبة للوظيفة. في هذه الخلية، نرشد المستخدم لاختيار الحوسبة المناسبة للوظيفة.

> [!NOTE]
> الحوسبات المدرجة أدناه تعمل مع التكوين الأكثر تحسينًا. أي تغييرات في التكوين قد تؤدي إلى خطأ Cuda Out Of Memory. في مثل هذه الحالات، حاول ترقية الحوسبة إلى حجم أكبر.

> [!NOTE]
> عند تحديد compute_cluster_size أدناه، تأكد من أن الحوسبة متاحة في مجموعة الموارد الخاصة بك. إذا لم تكن حوسبة معينة متاحة، يمكنك تقديم طلب للوصول إلى موارد الحوسبة.

### التحقق من دعم النموذج للتخصيص

1. هذا النص البرمجي Python يتفاعل مع نموذج Azure Machine Learning (Azure ML). إليك ما يقوم به:

    - يستورد وحدة ast التي توفر وظائف لمعالجة أشجار قواعد النحو المجردة في Python.

    - يتحقق مما إذا كان كائن foundation_model (الذي يمثل نموذجًا في Azure ML) يحتوي على علامة باسم finetune_compute_allow_list. العلامات في Azure ML هي أزواج مفتاح-قيمة يمكنك إنشاؤها واستخدامها لتصفية النماذج وترتيبها.

    - إذا كانت العلامة finetune_compute_allow_list موجودة، فإنه يستخدم وظيفة ast.literal_eval لتحليل قيمة العلامة (سلسلة نصية) بأمان إلى قائمة Python. يتم تعيين هذه القائمة إلى المتغير computes_allow_list. ثم يطبع رسالة تشير إلى أنه يجب إنشاء حوسبة من القائمة.

    - إذا لم تكن العلامة finetune_compute_allow_list موجودة، فإنه يعين computes_allow_list إلى None ويطبع رسالة تشير إلى أن العلامة ليست جزءًا من علامات النموذج.

    - باختصار، يتحقق هذا النص البرمجي من وجود علامة معينة في بيانات النموذج الوصفية، ويحول قيمة العلامة إلى قائمة إذا كانت موجودة، ويوفر ملاحظات للمستخدم وفقًا لذلك.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### التحقق من مثيل الحوسبة

1. هذا النص البرمجي Python يتفاعل مع خدمة Azure Machine Learning (Azure ML) ويقوم بعدة فحوصات على مثيل الحوسبة. إليك ما يقوم به:

    - يحاول استرداد مثيل الحوسبة بالاسم المخزن في compute_cluster من مساحة عمل Azure ML. إذا كانت حالة توفير مثيل الحوسبة "فشلت"، فإنه يثير خطأ ValueError.

    - يتحقق مما إذا كانت computes_allow_list ليست None. إذا لم تكن كذلك، فإنه يحول جميع أحجام الحوسبة في القائمة إلى أحرف صغيرة ويتحقق مما إذا كان حجم مثيل الحوسبة الحالي موجودًا في القائمة. إذا لم يكن كذلك، فإنه يثير خطأ ValueError.

    - إذا كانت computes_allow_list تساوي None، فإنه يتحقق مما إذا كان حجم مثيل الحوسبة موجودًا في قائمة أحجام GPU VM غير المدعومة. إذا كان كذلك، فإنه يثير خطأ ValueError.

    - يسترد قائمة بجميع أحجام الحوسبة المتاحة في مساحة العمل. ثم يتنقل عبر هذه القائمة، ولكل حجم حوسبة يتحقق مما إذا كان اسمه يطابق حجم مثيل الحوسبة الحالي. إذا كان كذلك، فإنه يسترد عدد وحدات GPU لهذا الحجم ويعين gpu_count_found إلى True.

    - إذا كانت gpu_count_found تساوي True، فإنه يطبع عدد وحدات GPU في مثيل الحوسبة. إذا كانت gpu_count_found تساوي False، فإنه يثير خطأ ValueError.

    - باختصار، يقوم هذا النص البرمجي بإجراء عدة فحوصات على مثيل الحوسبة في مساحة عمل Azure ML، بما في ذلك التحقق من حالة توفيره، حجمه مقابل قائمة السماح أو قائمة الحظر، وعدد وحدات GPU التي يحتوي عليها.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. اختيار مجموعة البيانات لتخصيص النموذج

1. نستخدم مجموعة بيانات ultrachat_200k. تحتوي مجموعة البيانات على أربعة تقسيمات، مناسبة للتخصيص الخاضع للإشراف (sft). التصنيف التوليدي (gen). يظهر عدد الأمثلة لكل تقسيم كما يلي:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. تعرض الخلايا التالية إعداد البيانات الأساسية للتخصيص:

### تصور بعض الصفوف من البيانات

نريد تشغيل هذا المثال بسرعة، لذا نحفظ ملفات train_sft وtest_sft التي تحتوي على 5% فقط من الصفوف المقلصة بالفعل. يعني هذا أن النموذج المخصص سيكون دقته أقل، لذا لا ينبغي استخدامه في العالم الحقيقي. يتم استخدام download-dataset.py لتنزيل مجموعة بيانات ultrachat_200k وتحويلها إلى تنسيق قابل للاستهلاك بواسطة مكونات خط أنابيب التخصيص. أيضًا، نظرًا لأن مجموعة البيانات كبيرة، فإننا هنا نستخدم جزءًا فقط منها.

1. يؤدي تشغيل النص البرمجي أدناه إلى تنزيل 5% فقط من البيانات. يمكن زيادة ذلك عن طريق تغيير المعامل dataset_split_pc إلى النسبة المطلوبة.

    > [!NOTE]
    > تحتوي بعض نماذج اللغة على رموز لغة مختلفة، وبالتالي يجب أن تعكس أسماء الأعمدة في مجموعة البيانات نفس الشيء.

1. هنا مثال على كيفية تنظيم البيانات:
تُخزن مجموعة بيانات إكمال المحادثة بتنسيق parquet، مع استخدام كل إدخال للمخطط التالي:

    - هذا مستند JSON (JavaScript Object Notation)، وهو تنسيق شائع لتبادل البيانات. إليك تحليل بنيته:

    - "prompt": يحتوي هذا المفتاح على قيمة نصية تمثل مهمة أو سؤالًا موجهًا إلى مساعد AI.

    - "messages": يحتوي هذا المفتاح على مصفوفة من الكائنات. يمثل كل كائن رسالة في محادثة بين المستخدم ومساعد AI. يحتوي كل كائن رسالة على مفتاحين:

    - "content": يحتوي هذا المفتاح على قيمة نصية تمثل محتوى الرسالة.
    - "role": يحتوي هذا المفتاح على قيمة نصية تمثل دور الكيان الذي أرسل الرسالة. يمكن أن يكون إما "user" أو "assistant".
    - "prompt_id": يحتوي هذا المفتاح على قيمة نصية تمثل معرفًا فريدًا للموجه.

1. في هذا المستند JSON المحدد، تمثل المحادثة حيث يطلب المستخدم من مساعد AI إنشاء بطل لقصة ديستوبية. يرد المساعد، ثم يطلب المستخدم مزيدًا من التفاصيل. يوافق المساعد على تقديم المزيد من التفاصيل. ترتبط المحادثة بأكملها بمعرف موجه محدد.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### تنزيل البيانات

1. هذا النص البرمجي Python يُستخدم لتنزيل مجموعة بيانات باستخدام نص مساعد باسم download-dataset.py. إليك ما يقوم به:

    - يستورد وحدة os، التي توفر طريقة محمولة لاستخدام الوظائف المعتمدة على نظام التشغيل.

    - يستخدم وظيفة os.system لتشغيل نص download-dataset.py في القشرة مع وسائط سطر أوامر محددة. تشير الوسائط إلى مجموعة البيانات التي سيتم تنزيلها (HuggingFaceH4/ultrachat_200k)، الدليل الذي سيتم تنزيلها فيه (ultrachat_200k_dataset)، والنسبة المئوية لتقسيم مجموعة البيانات (5). تُخزن حالة الخروج من الأمر الذي تم تنفيذه في المتغير exit_status.

    - يتحقق مما إذا كانت exit_status لا تساوي 0. في أنظمة التشغيل الشبيهة بـ Unix، تشير حالة الخروج 0 عادةً إلى أن الأمر قد نجح، بينما يشير أي رقم آخر إلى خطأ. إذا كانت exit_status لا تساوي 0، فإنه يثير استثناءً مع رسالة تشير إلى وجود خطأ في تنزيل مجموعة البيانات.

    - باختصار، يقوم هذا النص البرمجي بتشغيل أمر لتنزيل مجموعة بيانات باستخدام نص مساعد، ويثير استثناءً إذا فشل الأمر.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### تحميل البيانات إلى DataFrame

1. هذا النص البرمجي Python يقوم بتحميل ملف JSON Lines إلى DataFrame باستخدام مكتبة pandas ويعرض أول 5 صفوف. إليك ما يقوم به:

    - يستورد مكتبة pandas، وهي مكتبة قوية لمعالجة البيانات وتحليلها.

    - يضبط عرض العمود الأقصى لخيارات عرض pandas إلى 0. يعني ذلك أن النص الكامل لكل عمود سيتم عرضه دون اقتطاع عند طباعة DataFrame.

    - يستخدم وظيفة pd.read_json لتحميل ملف train_sft.jsonl من دليل ultrachat_200k_dataset إلى DataFrame. يشير الوسيط lines=True إلى أن الملف بتنسيق JSON Lines، حيث يمثل كل سطر كائن JSON منفصل.

    - يستخدم طريقة head لعرض أول 5 صفوف من DataFrame. إذا كان DataFrame يحتوي على أقل من 5 صفوف، فسيعرضها جميعًا.

    - باختصار، يقوم هذا النص البرمجي بتحميل ملف JSON Lines إلى DataFrame وعرض أول 5 صفوف مع النص الكامل للأعمدة.

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. إرسال وظيفة التخصيص باستخدام النموذج والبيانات كمدخلات

قم بإنشاء الوظيفة التي تستخدم مكون خط أنابيب إكمال المحادثة. تعرف على المزيد حول جميع المعاملات المدعومة للتخصيص.

### تعريف معاملات التخصيص

1. يمكن تصنيف معاملات التخصيص إلى فئتين - معاملات التدريب، معاملات التحسين.

1. معاملات التدريب تحدد جوانب التدريب مثل:

    - المُحسن، المجدول الذي سيتم استخدامه.
    - المقياس الذي سيتم تحسين التخصيص بناءً عليه.
    - عدد خطوات التدريب وحجم الدفعة وهكذا.

1. معاملات التحسين تساعد في تحسين ذاكرة GPU واستخدام موارد الحوسبة بشكل فعال.

    - تمكين DeepSpeed وLoRA.
    - تمكين التدريب بدقة مختلطة.
    - تمكين التدريب متعدد العقد.

> [!NOTE]
> قد يؤدي التخصيص الخاضع للإشراف إلى فقدان المحاذاة أو النسيان الكارثي. نوصي بالتحقق من هذه المشكلة وتشغيل مرحلة محاذاة بعد التخصيص.

### معاملات التخصيص

1. هذا النص البرمجي Python يُعد معاملات لتخصيص نموذج تعلم الآلة. إليك ما يقوم به:

    - يُعد معاملات تدريب افتراضية مثل عدد عصور التدريب، أحجام الدُفعات للتدريب والتقييم، معدل التعلم، ونوع جدولة معدل التعلم.

    - يُعد معاملات تحسين افتراضية مثل ما إذا كان سيتم تطبيق Layer-wise Relevance Propagation (LoRa) وDeepSpeed، ومرحلة DeepSpeed.

    - يجمع معاملات التدريب والتحسين في قاموس واحد يسمى finetune_parameters.

    - يتحقق مما إذا كان foundation_model يحتوي على أي معاملات افتراضية خاصة بالنموذج. إذا كان كذلك، فإنه يطبع رسالة تحذير ويُحدث قاموس finetune_parameters بهذه الافتراضات الخاصة بالنموذج. تُستخدم وظيفة ast.literal_eval لتحويل الافتراضات الخاصة بالنموذج من سلسلة نصية إلى قاموس Python.

    - يطبع المجموعة النهائية من معاملات التخصيص التي سيتم استخدامها للتشغيل.

    - باختصار، يُعد هذا النص البرمجي معاملات لتخصيص نموذج تعلم الآلة ويعرضها، مع القدرة على تجاوز الافتراضات الافتراضية باستخدام معاملات خاصة بالنموذج.

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### خط أنابيب التدريب

1. هذا النص البرمجي Python يُعرف دالة لتوليد اسم عرض لخط أنابيب تدريب تعلم الآلة، ثم يستدعي هذه الدالة لتوليد وطباعة اسم العرض. إليك ما يقوم به:

    1. تُعرف الدالة get_pipeline_display_name. تُولد هذه الدالة اسم عرض بناءً على معاملات مختلفة متعلقة بخط أنابيب التدريب.

    1. داخل الدالة، تُحسب حجم الدُفعة الإجمالي بضرب حجم الدُفعة لكل جهاز، عدد خطوات تراكم التدرجات، عدد وحدات GPU لكل عقدة، وعدد العقد المستخدمة للتخصيص.

    1. تسترد معاملات أخرى مثل نوع جدولة معدل التعلم، ما إذا كان DeepSpeed مطبقًا، مرحلة DeepSpeed، ما إذا كان Layer-wise Relevance Propagation (LoRa) مطبقًا، الحد الأقصى لعدد نقاط التحقق للنموذج، وأقصى طول تسلسل.

    1. تُنشئ سلسلة نصية تتضمن كل هذه المعاملات، مفصولة بشرطات. إذا كان DeepSpeed أو LoRa مطبقًا، تتضمن السلسلة النصية "ds" متبوعة بمرحلة DeepSpeed، أو "lora"، على التوالي. إذا لم يكن كذلك، تتضمن "nods" أو "nolora"، على التوالي.

    1. تُعيد الدالة هذه السلسلة النصية، التي تُستخدم كاسم عرض لخط أنابيب التدريب.

    1. بعد تعريف الدالة، تُستدعى لتوليد اسم العرض، الذي يُطبع بعد ذلك.

    1. باختصار، يُولد هذا النص البرمجي اسم عرض لخط أنابيب تدريب تعلم الآلة.
### إعداد خط أنابيب التدريب
بناء خط أنابيب تدريب يعتمد على معايير مختلفة، ثم طباعة اسم العرض الخاص به.  
```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```  

### تكوين خط الأنابيب
هذا السكربت المكتوب بلغة Python يقوم بتعريف وتكوين خط أنابيب تعلم آلي باستخدام Azure Machine Learning SDK. فيما يلي تفصيل لما يقوم به:

1. يقوم باستيراد الوحدات الضرورية من Azure AI ML SDK.
2. يجلب مكون خط أنابيب يسمى "chat_completion_pipeline" من السجل.
3. يُعرّف مهمة خط أنابيب باستخدام:
   `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`، مما يعني أن خط الأنابيب سيتوقف إذا فشل أي خطوة.
4. باختصار، هذا السكربت يُعرّف ويُكوّن خط أنابيب تعلم آلي لمهمة إكمال المحادثات باستخدام Azure Machine Learning SDK.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```  

### إرسال المهمة
1. هذا السكربت المكتوب بلغة Python يقوم بإرسال مهمة خط أنابيب تعلم آلي إلى مساحة عمل Azure Machine Learning ثم ينتظر حتى تكتمل المهمة. فيما يلي تفصيل لما يقوم به:

   - يستدعي الطريقة create_or_update من كائن jobs في workspace_ml_client لإرسال مهمة خط الأنابيب. يتم تحديد خط الأنابيب الذي سيتم تشغيله من خلال pipeline_object، ويتم تحديد التجربة التي سيتم تشغيل المهمة تحتها من خلال experiment_name.
   - يستدعي الطريقة stream من كائن jobs في workspace_ml_client للانتظار حتى تكتمل مهمة خط الأنابيب. يتم تحديد المهمة المراد انتظارها من خلال السمة name الخاصة بكائن pipeline_job.
   - باختصار، هذا السكربت يقوم بإرسال مهمة خط أنابيب تعلم آلي إلى مساحة عمل Azure Machine Learning ثم ينتظر حتى تكتمل المهمة.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```  

## 6. تسجيل النموذج المحسن مع مساحة العمل
سنقوم بتسجيل النموذج الناتج من مهمة تحسين الأداء. هذا سيتتبع العلاقة بين النموذج المحسن ومهمة تحسين الأداء. مهمة تحسين الأداء تتبع بدورها العلاقة مع النموذج الأساسي والبيانات وكود التدريب.

### تسجيل نموذج التعلم الآلي
1. هذا السكربت المكتوب بلغة Python يقوم بتسجيل نموذج تعلم آلي تم تدريبه في خط أنابيب Azure Machine Learning. فيما يلي تفصيل لما يقوم به:

   - يستورد الوحدات الضرورية من Azure AI ML SDK.
   - يتحقق مما إذا كان مخرج trained_model متاحًا من مهمة خط الأنابيب عن طريق استدعاء الطريقة get من كائن jobs في workspace_ml_client والوصول إلى السمة outputs.
   - يبني مسارًا إلى النموذج المدرب عن طريق تنسيق سلسلة نصوص باسم مهمة خط الأنابيب واسم المخرج ("trained_model").
   - يُعرّف اسمًا للنموذج المحسن بإضافة "-ultrachat-200k" إلى اسم النموذج الأصلي واستبدال أي شرطات مائلة بشرطات.
   - يجهز لتسجيل النموذج عن طريق إنشاء كائن Model مع معلمات مختلفة، بما في ذلك المسار إلى النموذج، نوع النموذج (نموذج MLflow)، اسم النموذج وإصداره، ووصف النموذج.
   - يُسجل النموذج عن طريق استدعاء الطريقة create_or_update من كائن models في workspace_ml_client مع كائن Model كمعامل.
   - يطبع النموذج المسجل.
   - باختصار، هذا السكربت يقوم بتسجيل نموذج تعلم آلي تم تدريبه في خط أنابيب Azure Machine Learning.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```  

## 7. نشر النموذج المحسن إلى نقطة نهاية عبر الإنترنت
تقدم نقاط النهاية عبر الإنترنت واجهة برمجية REST API دائمة يمكن استخدامها للتكامل مع التطبيقات التي تحتاج إلى استخدام النموذج.

### إدارة نقطة النهاية
1. هذا السكربت المكتوب بلغة Python يقوم بإنشاء نقطة نهاية مُدارة عبر الإنترنت في Azure Machine Learning لنموذج مسجل. فيما يلي تفصيل لما يقوم به:

   - يستورد الوحدات الضرورية من Azure AI ML SDK.
   - يُعرّف اسمًا فريدًا لنقطة النهاية عبر الإنترنت بإضافة طابع زمني إلى السلسلة النصية "ultrachat-completion-".
   - يجهز لإنشاء نقطة النهاية عبر الإنترنت عن طريق إنشاء كائن ManagedOnlineEndpoint مع معلمات مختلفة، بما في ذلك اسم نقطة النهاية، وصف نقطة النهاية، ووضع المصادقة ("key").
   - يُنشئ نقطة النهاية عبر الإنترنت عن طريق استدعاء الطريقة begin_create_or_update من workspace_ml_client مع كائن ManagedOnlineEndpoint كمعامل. ثم ينتظر حتى تكتمل عملية الإنشاء عن طريق استدعاء الطريقة wait.
   - باختصار، هذا السكربت يقوم بإنشاء نقطة نهاية مُدارة عبر الإنترنت في Azure Machine Learning لنموذج مسجل.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```  

> [!NOTE]  
> يمكنك العثور هنا على قائمة SKU المدعومة للنشر - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)  

### نشر نموذج التعلم الآلي
1. هذا السكربت المكتوب بلغة Python يقوم بنشر نموذج تعلم آلي مسجل إلى نقطة نهاية مُدارة عبر الإنترنت في Azure Machine Learning. فيما يلي تفصيل لما يقوم به:

   - يستورد وحدة ast، التي توفر وظائف لمعالجة أشجار قواعد بناء الجمل في Python.
   - يُحدد نوع المثيل للنشر بـ "Standard_NC6s_v3".
   - يتحقق مما إذا كانت العلامة inference_compute_allow_list موجودة في النموذج الأساسي. إذا كانت موجودة، فإنه يحول قيمة العلامة من سلسلة نصوص إلى قائمة Python ويُعيّنها إلى inference_computes_allow_list. إذا لم تكن موجودة، فإنه يعيّن inference_computes_allow_list إلى None.
   - يتحقق مما إذا كان نوع المثيل المحدد موجودًا في قائمة السماح. إذا لم يكن كذلك، فإنه يطبع رسالة تطلب من المستخدم اختيار نوع مثيل من قائمة السماح.
   - يجهز لإنشاء النشر عن طريق إنشاء كائن ManagedOnlineDeployment مع معلمات مختلفة، بما في ذلك اسم النشر، اسم نقطة النهاية، معرف النموذج، نوع وعدد المثيلات، إعدادات فحص الجاهزية، وإعدادات الطلب.
   - يُنشئ النشر عن طريق استدعاء الطريقة begin_create_or_update من workspace_ml_client مع كائن ManagedOnlineDeployment كمعامل. ثم ينتظر حتى تكتمل عملية الإنشاء عن طريق استدعاء الطريقة wait.
   - يُحدد حركة المرور لنقطة النهاية لتوجيه 100% من الحركة إلى نشر "demo".
   - يُحدث نقطة النهاية عن طريق استدعاء الطريقة begin_create_or_update من workspace_ml_client مع كائن endpoint كمعامل. ثم ينتظر حتى تكتمل عملية التحديث عن طريق استدعاء الطريقة result.
   - باختصار، هذا السكربت يقوم بنشر نموذج تعلم آلي مسجل إلى نقطة نهاية مُدارة عبر الإنترنت في Azure Machine Learning.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```  

## 8. اختبار نقطة النهاية باستخدام بيانات تجريبية
سنقوم بجلب بعض البيانات التجريبية من مجموعة بيانات الاختبار وإرسالها إلى نقطة النهاية عبر الإنترنت للاستدلال. ثم سنعرض النتائج المسجلة إلى جانب القيم الحقيقية.

### قراءة النتائج
1. هذا السكربت المكتوب بلغة Python يقوم بقراءة ملف JSON Lines إلى DataFrame من pandas، وأخذ عينة عشوائية، وإعادة تعيين الفهرس. فيما يلي تفصيل لما يقوم به:

   - يقرأ الملف ./ultrachat_200k_dataset/test_gen.jsonl إلى DataFrame من pandas. يتم استخدام وظيفة read_json مع الوسيطة lines=True لأن الملف بتنسيق JSON Lines، حيث كل سطر هو كائن JSON منفصل.
   - يأخذ عينة عشوائية من صف واحد من DataFrame. يتم استخدام وظيفة sample مع الوسيطة n=1 لتحديد عدد الصفوف العشوائية المراد اختيارها.
   - يُعيد تعيين الفهرس الخاص بـ DataFrame. يتم استخدام وظيفة reset_index مع الوسيطة drop=True لإزالة الفهرس الأصلي واستبداله بفهرس جديد من القيم الصحيحة الافتراضية.
   - يعرض أول صفين من DataFrame باستخدام وظيفة head مع الوسيطة 2. ومع ذلك، نظرًا لأن DataFrame يحتوي فقط على صف واحد بعد أخذ العينة، سيتم عرض هذا الصف فقط.
   - باختصار، هذا السكربت يقوم بقراءة ملف JSON Lines إلى DataFrame من pandas، وأخذ عينة عشوائية من صف واحد، وإعادة تعيين الفهرس، وعرض الصف الأول.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```  

### إنشاء كائن JSON
1. هذا السكربت المكتوب بلغة Python يقوم بإنشاء كائن JSON بمعلمات محددة وحفظه في ملف. فيما يلي تفصيل لما يقوم به:

   - يستورد وحدة json، التي توفر وظائف للعمل مع بيانات JSON.
   - يُنشئ قاموسًا parameters بمفاتيح وقيم تمثل معلمات لنموذج تعلم الآلي. المفاتيح هي "temperature"، "top_p"، "do_sample"، و"max_new_tokens"، والقيم المقابلة لها هي 0.6، 0.9، True، و200 على التوالي.
   - يُنشئ قاموسًا آخر test_json بمفتاحين: "input_data" و"params". قيمة "input_data" هي قاموس آخر بمفاتيح "input_string" و"parameters". قيمة "input_string" هي قائمة تحتوي على الرسالة الأولى من DataFrame test_df. قيمة "parameters" هي القاموس parameters الذي تم إنشاؤه سابقًا. قيمة "params" هي قاموس فارغ.
   - يفتح ملفًا باسم sample_score.json.

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```  

### استدعاء نقطة النهاية
1. هذا السكربت المكتوب بلغة Python يقوم باستدعاء نقطة نهاية عبر الإنترنت في Azure Machine Learning لتسجيل ملف JSON. فيما يلي تفصيل لما يقوم به:

   - يستدعي الطريقة invoke من الخاصية online_endpoints لكائن workspace_ml_client. يتم استخدام هذه الطريقة لإرسال طلب إلى نقطة نهاية عبر الإنترنت والحصول على استجابة.
   - يُحدد اسم نقطة النهاية والنشر باستخدام الوسيطتين endpoint_name وdeployment_name. في هذه الحالة، يتم تخزين اسم نقطة النهاية في المتغير online_endpoint_name واسم النشر هو "demo".
   - يُحدد المسار إلى ملف JSON الذي سيتم تسجيله باستخدام الوسيطة request_file. في هذه الحالة، الملف هو ./ultrachat_200k_dataset/sample_score.json.
   - يُخزن الاستجابة من نقطة النهاية في المتغير response.
   - يطبع الاستجابة الأولية.
   - باختصار، هذا السكربت يقوم باستدعاء نقطة نهاية عبر الإنترنت في Azure Machine Learning لتسجيل ملف JSON وطباعة الاستجابة.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```  

## 9. حذف نقطة النهاية عبر الإنترنت
1. لا تنس حذف نقطة النهاية عبر الإنترنت، وإلا ستترك عداد الفوترة يعمل للحوسبة المستخدمة من قبل نقطة النهاية. هذه السطر من كود Python يقوم بحذف نقطة نهاية عبر الإنترنت في Azure Machine Learning. فيما يلي تفصيل لما يقوم به:

   - يستدعي الطريقة begin_delete من الخاصية online_endpoints لكائن workspace_ml_client. يتم استخدام هذه الطريقة لبدء حذف نقطة نهاية عبر الإنترنت.
   - يُحدد اسم نقطة النهاية التي سيتم حذفها باستخدام الوسيطة name. في هذه الحالة، يتم تخزين اسم نقطة النهاية في المتغير online_endpoint_name.
   - يستدعي الطريقة wait للانتظار حتى تكتمل عملية الحذف. هذه عملية حظر، مما يعني أنها ستمنع السكربت من الاستمرار حتى ينتهي الحذف.
   - باختصار، هذا السطر من الكود يقوم ببدء حذف نقطة نهاية عبر الإنترنت في Azure Machine Learning والانتظار حتى تكتمل العملية.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```  

**إخلاء مسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. على الرغم من أننا نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأم المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.