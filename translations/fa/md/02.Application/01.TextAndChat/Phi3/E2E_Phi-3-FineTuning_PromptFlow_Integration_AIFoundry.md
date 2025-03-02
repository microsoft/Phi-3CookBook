# تنظیم و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow در Azure AI Foundry

این نمونه کامل (E2E) بر اساس راهنمای "[تنظیم و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow در Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" از Microsoft Tech Community است. این راهنما فرآیندهای تنظیم، استقرار و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow در Azure AI Foundry را معرفی می‌کند.  
برخلاف نمونه E2E "[تنظیم و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" که شامل اجرای کد به صورت محلی بود، این آموزش کاملاً بر تنظیم و یکپارچه‌سازی مدل شما در Azure AI / ML Studio متمرکز است.

## مرور کلی

در این نمونه E2E، یاد خواهید گرفت که چگونه مدل Phi-3 را تنظیم کنید و آن را با Prompt Flow در Azure AI Foundry یکپارچه نمایید. با استفاده از Azure AI / ML Studio، یک جریان کاری برای استقرار و استفاده از مدل‌های هوش مصنوعی سفارشی ایجاد خواهید کرد. این نمونه E2E به سه سناریو تقسیم شده است:

**سناریو 1: تنظیم منابع Azure و آماده‌سازی برای تنظیم**

**سناریو 2: تنظیم مدل Phi-3 و استقرار آن در Azure Machine Learning Studio**

**سناریو 3: یکپارچه‌سازی با Prompt Flow و گفتگو با مدل سفارشی خود در Azure AI Foundry**

در اینجا مروری بر این نمونه E2E ارائه شده است.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.fa.png)

### فهرست مطالب

1. **[سناریو 1: تنظیم منابع Azure و آماده‌سازی برای تنظیم](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [ایجاد یک Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [درخواست سهمیه GPU در اشتراک Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [اضافه کردن نقش](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [تنظیم پروژه](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [آماده‌سازی مجموعه داده برای تنظیم](../../../../../../md/02.Application/01.TextAndChat/Phi3)

2. **[سناریو 2: تنظیم مدل Phi-3 و استقرار آن در Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [تنظیم مدل Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [استقرار مدل تنظیم‌شده Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

3. **[سناریو 3: یکپارچه‌سازی با Prompt Flow و گفتگو با مدل سفارشی خود در Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [یکپارچه‌سازی مدل سفارشی Phi-3 با Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [گفتگو با مدل سفارشی Phi-3 خود](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## سناریو 1: تنظیم منابع Azure و آماده‌سازی برای تنظیم

### ایجاد یک Azure Machine Learning Workspace

1. عبارت *azure machine learning* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Azure Machine Learning** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.fa.png)

2. از منوی ناوبری، گزینه **+ Create** را انتخاب کنید.

3. از منوی ناوبری، گزینه **New workspace** را انتخاب کنید.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.fa.png)

4. کارهای زیر را انجام دهید:

    - اشتراک Azure خود را **Subscription** انتخاب کنید.  
    - **Resource group** مورد نظر را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).  
    - **Workspace Name** را وارد کنید. این مقدار باید یکتا باشد.  
    - **Region** مورد نظر را انتخاب کنید.  
    - **Storage account** مورد نظر را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).  
    - **Key vault** مورد نظر را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).  
    - **Application insights** مورد نظر را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).  
    - **Container registry** مورد نظر را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.fa.png)

5. گزینه **Review + Create** را انتخاب کنید.

6. گزینه **Create** را انتخاب کنید.

### درخواست سهمیه GPU در اشتراک Azure

در این آموزش، یاد خواهید گرفت که چگونه یک مدل Phi-3 را تنظیم و مستقر کنید، با استفاده از GPUها. برای تنظیم، از GPU *Standard_NC24ads_A100_v4* استفاده خواهید کرد که نیاز به درخواست سهمیه دارد. برای استقرار، از GPU *Standard_NC6s_v3* استفاده خواهید کرد که آن نیز نیاز به درخواست سهمیه دارد.

> [!NOTE]
>
> فقط اشتراک‌های Pay-As-You-Go (نوع استاندارد اشتراک) واجد شرایط تخصیص GPU هستند؛ اشتراک‌های مزایای دیگر در حال حاضر پشتیبانی نمی‌شوند.

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

1. کارهای زیر را برای درخواست سهمیه *Standard NCADSA100v4 Family* انجام دهید:

    - از تب سمت چپ، **Quota** را انتخاب کنید.  
    - خانواده ماشین مجازی مورد نظر را انتخاب کنید. برای مثال، **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** که شامل GPU *Standard_NC24ads_A100_v4* است.  
    - از منوی ناوبری، گزینه **Request quota** را انتخاب کنید.  

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.fa.png)

    - در صفحه Request quota، مقدار **New cores limit** مورد نظر را وارد کنید. برای مثال، 24.  
    - در صفحه Request quota، گزینه **Submit** را انتخاب کنید تا سهمیه GPU درخواست شود.

1. کارهای زیر را برای درخواست سهمیه *Standard NCSv3 Family* انجام دهید:

    - از تب سمت چپ، **Quota** را انتخاب کنید.  
    - خانواده ماشین مجازی مورد نظر را انتخاب کنید. برای مثال، **Standard NCSv3 Family Cluster Dedicated vCPUs** که شامل GPU *Standard_NC6s_v3* است.  
    - از منوی ناوبری، گزینه **Request quota** را انتخاب کنید.  
    - در صفحه Request quota، مقدار **New cores limit** مورد نظر را وارد کنید. برای مثال، 24.  
    - در صفحه Request quota، گزینه **Submit** را انتخاب کنید تا سهمیه GPU درخواست شود.

### اضافه کردن نقش

برای تنظیم و استقرار مدل‌های خود، ابتدا باید یک User Assigned Managed Identity (UAI) ایجاد کرده و مجوزهای مناسب را به آن اختصاص دهید. این UAI برای احراز هویت در طول فرآیند استقرار استفاده خواهد شد.

#### ایجاد User Assigned Managed Identity (UAI)

1. عبارت *managed identities* را در **نوار جستجو** بالای صفحه پورتال تایپ کنید و **Managed Identities** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.fa.png)

1. گزینه **+ Create** را انتخاب کنید.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.fa.png)

1. کارهای زیر را انجام دهید:

    - اشتراک Azure خود را **Subscription** انتخاب کنید.  
    - **Resource group** مورد نظر را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).  
    - **Region** مورد نظر را انتخاب کنید.  
    - **Name** را وارد کنید. این مقدار باید یکتا باشد.  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.fa.png)

1. گزینه **Review + create** را انتخاب کنید.

1. گزینه **+ Create** را انتخاب کنید.

#### اضافه کردن نقش Contributor به Managed Identity

1. به منبع Managed Identity که ایجاد کرده‌اید بروید.

1. از تب سمت چپ، **Azure role assignments** را انتخاب کنید.

1. از منوی ناوبری، گزینه **+Add role assignment** را انتخاب کنید.

1. در صفحه Add role assignment، کارهای زیر را انجام دهید:
    - **Scope** را به **Resource group** تغییر دهید.  
    - اشتراک Azure خود را **Subscription** انتخاب کنید.  
    - **Resource group** مورد نظر را انتخاب کنید.  
    - **Role** را به **Contributor** تغییر دهید.  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.fa.png)

2. گزینه **Save** را انتخاب کنید.

#### اضافه کردن نقش Storage Blob Data Reader به Managed Identity

1. عبارت *storage accounts* را در **نوار جستجو** تایپ کنید و **Storage accounts** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.fa.png)

1. حساب ذخیره‌سازی مرتبط با Azure Machine Learning Workspace که ایجاد کرده‌اید را انتخاب کنید. برای مثال، *finetunephistorage*.

1. کارهای زیر را برای دسترسی به صفحه Add role assignment انجام دهید:

    - به حساب ذخیره‌سازی Azure که ایجاد کرده‌اید بروید.  
    - از تب سمت چپ، **Access Control (IAM)** را انتخاب کنید.  
    - از منوی ناوبری، گزینه **+ Add** را انتخاب کنید.  
    - از منوی ناوبری، گزینه **Add role assignment** را انتخاب کنید.  

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.fa.png)

1. در صفحه Add role assignment، کارهای زیر را انجام دهید:

    - در صفحه Role، عبارت *Storage Blob Data Reader* را در **نوار جستجو** تایپ کنید و **Storage Blob Data Reader** را از گزینه‌های ظاهر شده انتخاب کنید.  
    - در صفحه Role، گزینه **Next** را انتخاب کنید.  
    - در صفحه Members، گزینه **Assign access to** را به **Managed identity** تغییر دهید.  
    - در صفحه Members، گزینه **+ Select members** را انتخاب کنید.  
    - در صفحه Select managed identities، اشتراک Azure خود را **Subscription** انتخاب کنید.  
    - در صفحه Select managed identities، **Managed identity** را به **Manage Identity** تغییر دهید.  
    - در صفحه Select managed identities، Managed Identity که ایجاد کرده‌اید را انتخاب کنید. برای مثال، *finetunephi-managedidentity*.  
    - در صفحه Select managed identities، گزینه **Select** را انتخاب کنید.  

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.fa.png)

1. گزینه **Review + assign** را انتخاب کنید.

#### اضافه کردن نقش AcrPull به Managed Identity

1. عبارت *container registries* را در **نوار جستجو** تایپ کنید و **Container registries** را از گزینه‌های ظاهر شده انتخاب کنید.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.fa.png)

1. رجیستری کانتینر مرتبط با Azure Machine Learning Workspace را انتخاب کنید. برای مثال، *finetunephicontainerregistry*.

1. کارهای زیر را برای دسترسی به صفحه Add role assignment انجام دهید:

    - از تب سمت چپ، **Access Control (IAM)** را انتخاب کنید.  
    - از منوی ناوبری، گزینه **+ Add** را انتخاب کنید.  
    - از منوی ناوبری، گزینه **Add role assignment** را انتخاب کنید.  

1. در صفحه Add role assignment، کارهای زیر را انجام دهید:

    - در صفحه Role، عبارت *AcrPull* را در **نوار جستجو** تایپ کنید و **AcrPull** را از گزینه‌های ظاهر شده انتخاب کنید.  
    - در صفحه Role، گزینه **Next** را انتخاب کنید.  
    - در صفحه Members، گزینه **Assign access to** را به **Managed identity** تغییر دهید.  
    - در صفحه Members، گزینه **+ Select members** را انتخاب کنید.  
    - در صفحه Select managed identities، اشتراک Azure خود را **Subscription** انتخاب کنید.  
    - در صفحه Select managed identities، **Managed identity** را به **Manage Identity** تغییر دهید.  
    - در صفحه Select managed identities، Managed Identity که ایجاد کرده‌اید را انتخاب کنید. برای مثال، *finetunephi-managedidentity*.  
    - در صفحه Select managed identities، گزینه **Select** را انتخاب کنید.  
    - گزینه **Review + assign** را انتخاب کنید.

### تنظیم پروژه

برای دانلود مجموعه داده‌های مورد نیاز برای تنظیم، باید یک محیط محلی تنظیم کنید.

در این تمرین، شما:

- یک پوشه ایجاد می‌کنید تا داخل آن کار کنید.  
- یک محیط مجازی ایجاد می‌کنید.  
- بسته‌های مورد نیاز را نصب می‌کنید.  
- یک فایل *download_dataset.py* برای دانلود مجموعه داده ایجاد می‌کنید.

#### ایجاد یک پوشه برای کار داخل آن

1. یک پنجره ترمینال باز کنید و دستور زیر را برای ایجاد یک پوشه به نام *finetune-phi* در مسیر پیش‌فرض وارد کنید.

    ```console
    mkdir finetune-phi
    ```

2. دستور زیر را در ترمینال وارد کنید تا به پوشه *finetune-phi* که ایجاد کرده‌اید بروید.

    ```console
    cd finetune-phi
    ```

#### ایجاد یک محیط مجازی

1. دستور زیر را در ترمینال وارد کنید تا یک محیط مجازی به نام *.venv* ایجاد کنید.

    ```console
    python -m venv .venv
    ```

2. دستور زیر را در ترمینال وارد کنید تا محیط مجازی را فعال کنید.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> اگر موفقیت‌آمیز باشد، باید *(.venv)* را قبل از خط فرمان ببینید.

#### نصب بسته‌های مورد نیاز

1. دستورات زیر را در ترمینال وارد کنید تا بسته‌های مورد نیاز نصب شوند.

    ```console
    pip install datasets==2.19.1
    ```

#### ایجاد `download_dataset.py`

> [!NOTE]
> ساختار کامل پوشه:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** را باز کنید.

1. از نوار منو، گزینه **File** را انتخاب کنید.

1. گزینه **Open Folder** را انتخاب کنید.

1. پوشه *finetune-phi* که ایجاد کرده‌اید را انتخاب کنید، که در مسیر *C:\Users\yourUserName\finetune-phi* قرار دارد.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.fa.png)

1. در پنل سمت چپ Visual Studio Code، راست‌کلیک کنید و گزینه **New File** را انتخاب کنید تا یک فایل جدید به نام *download_dataset.py* ایجاد کنید.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.fa.png)

### آماده‌سازی مجموعه داده برای تنظیم

در این تمرین، فایل *download_dataset.py* را اجرا می‌کنید تا مجموعه داده‌های *ultrachat_200k* را به محیط محلی خود دانلود کنید. سپس از این مجموعه داده برای تنظیم مدل Phi-3 در Azure Machine Learning استفاده خواهید کرد.

در این تمرین، شما:

- کد را به فایل *download_dataset.py* اضافه می‌کنید تا مجموعه داده‌ها دانلود شوند.  
- فایل *download_dataset.py* را اجرا می‌کنید تا مجموعه داده‌ها به محیط محلی شما دانلود شوند.

#### دانلود مجموعه داده با استفاده از *download_dataset.py*

1. فایل *download_dataset.py* را در Visual Studio Code باز کنید.

1. کد زیر را به فایل *download_dataset.py* اضافه کنید.

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

1. دستور زیر را در ترمینال وارد کنید تا اسکریپت اجرا شود و مجموعه داده به محیط محلی شما دانلود شود.

    ```console
    python download_dataset.py
    ```

1. اطمینان حاصل کنید که مجموعه داده‌ها به درستی در دایرکتوری محلی *finetune-phi/data* ذخیره شده‌اند.

> [!NOTE]
>
> #### یادداشت در مورد اندازه مجموعه داده و زمان تنظیم
>
> در این آموزش، فقط از 1٪ مجموعه داده (`split='train[:1%]'`) استفاده می‌کنید. این کار مقدار داده‌ها را به طور قابل توجهی کاهش می‌دهد و فرآیند آپلود و تنظیم را تسریع می‌کند. می‌توانید درصد را تنظیم کنید تا تعادلی بین زمان آموزش و عملکرد مدل پیدا کنید. استفاده از یک زیرمجموعه کوچکتر از مجموعه داده، زمان لازم برای تنظیم را کاهش می‌دهد و فرآیند را برای یک آموزش ساده‌تر مدیریت‌پذیر می‌کند.

## سناریو 2: تنظیم مدل Phi-3 و استقرار آن در Azure Machine Learning Studio

### تنظیم مدل Phi-3

در این تمرین، مدل Phi-3 را در Azure Machine Learning Studio تنظیم خواهید کرد.

در این تمرین، شما:

- یک خوشه کامپیوتری برای تنظیم ایجاد می‌کنید.  
- مدل Phi-3 را در Azure Machine Learning Studio تنظیم می‌کنید.

#### ایجاد خوشه کامپیوتری برای تنظیم
1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) بروید.

1. از نوار کناری سمت چپ، **Compute** را انتخاب کنید.

1. از منوی ناوبری، **Compute clusters** را انتخاب کنید.

1. گزینه **+ New** را انتخاب کنید.

    ![انتخاب محاسبات.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.fa.png)

1. کارهای زیر را انجام دهید:

    - **Region** مورد نظر خود را انتخاب کنید.
    - **Virtual machine tier** را به **Dedicated** تنظیم کنید.
    - **Virtual machine type** را به **GPU** تنظیم کنید.
    - فیلتر **Virtual machine size** را روی **Select from all options** قرار دهید.
    - **Virtual machine size** را به **Standard_NC24ads_A100_v4** انتخاب کنید.

    ![ایجاد کلاستر.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.fa.png)

1. گزینه **Next** را انتخاب کنید.

1. کارهای زیر را انجام دهید:

    - نامی یکتا برای **Compute name** وارد کنید.
    - **Minimum number of nodes** را روی **0** تنظیم کنید.
    - **Maximum number of nodes** را روی **1** تنظیم کنید.
    - **Idle seconds before scale down** را روی **120** تنظیم کنید.

    ![ایجاد کلاستر.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.fa.png)

1. گزینه **Create** را انتخاب کنید.

#### تنظیم مدل Phi-3

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) بروید.

1. فضای کاری Azure Machine Learning که ایجاد کرده‌اید را انتخاب کنید.

    ![انتخاب فضای کاری.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fa.png)

1. کارهای زیر را انجام دهید:

    - از نوار کناری سمت چپ، **Model catalog** را انتخاب کنید.
    - عبارت *phi-3-mini-4k* را در **نوار جستجو** تایپ کنید و گزینه **Phi-3-mini-4k-instruct** را از میان گزینه‌های نمایش داده شده انتخاب کنید.

    ![تایپ phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.fa.png)

1. از منوی ناوبری، **Fine-tune** را انتخاب کنید.

    ![انتخاب تنظیم دقیق.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.fa.png)

1. کارهای زیر را انجام دهید:

    - **Select task type** را به **Chat completion** تنظیم کنید.
    - گزینه **+ Select data** را برای آپلود **Training data** انتخاب کنید.
    - نوع آپلود داده‌های اعتبارسنجی را به **Provide different validation data** تنظیم کنید.
    - گزینه **+ Select data** را برای آپلود **Validation data** انتخاب کنید.

    ![تکمیل صفحه تنظیم دقیق.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.fa.png)

    > [!TIP]
    >
    > می‌توانید از **Advanced settings** برای شخصی‌سازی تنظیماتی مانند **learning_rate** و **lr_scheduler_type** استفاده کنید تا فرآیند تنظیم دقیق را بهینه کنید.

1. گزینه **Finish** را انتخاب کنید.

1. در این تمرین، شما مدل Phi-3 را با موفقیت تنظیم دقیق کردید. لطفاً توجه داشته باشید که فرآیند تنظیم دقیق ممکن است زمان زیادی ببرد. پس از اجرای کار تنظیم دقیق، باید منتظر بمانید تا تکمیل شود. می‌توانید وضعیت کار تنظیم دقیق را با رفتن به برگه Jobs در سمت چپ فضای کاری Azure Machine Learning خود نظارت کنید. در سری بعدی، مدل تنظیم‌شده را مستقر کرده و آن را با Prompt flow ادغام خواهید کرد.

    ![مشاهده کار تنظیم دقیق.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.fa.png)

### استقرار مدل Phi-3 تنظیم‌شده

برای ادغام مدل Phi-3 تنظیم‌شده با Prompt flow، باید مدل را مستقر کنید تا برای پیش‌بینی در زمان واقعی قابل دسترسی باشد. این فرآیند شامل ثبت مدل، ایجاد یک نقطه پایانی آنلاین و استقرار مدل است.

در این تمرین، شما:

- مدل تنظیم‌شده را در فضای کاری Azure Machine Learning ثبت خواهید کرد.
- یک نقطه پایانی آنلاین ایجاد خواهید کرد.
- مدل Phi-3 تنظیم‌شده ثبت‌شده را مستقر خواهید کرد.

#### ثبت مدل تنظیم‌شده

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) بروید.

1. فضای کاری Azure Machine Learning که ایجاد کرده‌اید را انتخاب کنید.

    ![انتخاب فضای کاری.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fa.png)

1. از نوار کناری سمت چپ، **Models** را انتخاب کنید.
1. گزینه **+ Register** را انتخاب کنید.
1. گزینه **From a job output** را انتخاب کنید.

    ![ثبت مدل.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.fa.png)

1. کاری که ایجاد کرده‌اید را انتخاب کنید.

    ![انتخاب کار.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.fa.png)

1. گزینه **Next** را انتخاب کنید.

1. **Model type** را به **MLflow** تنظیم کنید.

1. اطمینان حاصل کنید که **Job output** انتخاب شده باشد؛ این گزینه باید به صورت خودکار انتخاب شده باشد.

    ![انتخاب خروجی.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.fa.png)

2. گزینه **Next** را انتخاب کنید.

3. گزینه **Register** را انتخاب کنید.

    ![انتخاب ثبت.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.fa.png)

4. می‌توانید مدل ثبت‌شده خود را با رفتن به منوی **Models** از نوار کناری مشاهده کنید.

    ![مدل ثبت‌شده.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.fa.png)

#### استقرار مدل تنظیم‌شده

1. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.

1. از نوار کناری سمت چپ، **Endpoints** را انتخاب کنید.

1. از منوی ناوبری، **Real-time endpoints** را انتخاب کنید.

    ![ایجاد نقطه پایانی.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.fa.png)

1. گزینه **Create** را انتخاب کنید.

1. مدل ثبت‌شده‌ای که ایجاد کرده‌اید را انتخاب کنید.

    ![انتخاب مدل ثبت‌شده.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.fa.png)

1. گزینه **Select** را انتخاب کنید.

1. کارهای زیر را انجام دهید:

    - **Virtual machine** را به *Standard_NC6s_v3* تنظیم کنید.
    - **Instance count** مورد نظر خود را انتخاب کنید. به عنوان مثال، *1*.
    - **Endpoint** را به **New** تنظیم کنید تا یک نقطه پایانی جدید ایجاد کنید.
    - نامی یکتا برای **Endpoint name** وارد کنید.
    - نامی یکتا برای **Deployment name** وارد کنید.

    ![تکمیل تنظیمات استقرار.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.fa.png)

1. گزینه **Deploy** را انتخاب کنید.

> [!WARNING]
> برای جلوگیری از هزینه‌های اضافی، حتماً نقطه پایانی ایجاد شده را در فضای کاری Azure Machine Learning حذف کنید.
>

#### بررسی وضعیت استقرار در فضای کاری Azure Machine Learning

1. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.

1. از نوار کناری سمت چپ، **Endpoints** را انتخاب کنید.

1. نقطه پایانی که ایجاد کرده‌اید را انتخاب کنید.

    ![انتخاب نقاط پایانی](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.fa.png)

1. در این صفحه می‌توانید نقاط پایانی را در طول فرآیند استقرار مدیریت کنید.

> [!NOTE]
> پس از تکمیل استقرار، اطمینان حاصل کنید که **Live traffic** روی **100%** تنظیم شده باشد. اگر اینطور نیست، گزینه **Update traffic** را انتخاب کنید تا تنظیمات ترافیک را به‌روزرسانی کنید. توجه داشته باشید که اگر ترافیک روی 0% تنظیم شده باشد، نمی‌توانید مدل را تست کنید.
>
> ![تنظیم ترافیک.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.fa.png)
>

## سناریو ۳: ادغام با Prompt flow و چت با مدل سفارشی خود در Azure AI Foundry

### ادغام مدل سفارشی Phi-3 با Prompt flow

پس از موفقیت در استقرار مدل تنظیم‌شده خود، اکنون می‌توانید آن را با Prompt Flow ادغام کنید تا مدل خود را در برنامه‌های زمان واقعی استفاده کنید و وظایف تعاملی متنوعی را با مدل سفارشی Phi-3 خود انجام دهید.

در این تمرین، شما:

- یک Hub در Azure AI Foundry ایجاد می‌کنید.
- یک پروژه در Azure AI Foundry ایجاد می‌کنید.
- Prompt flow ایجاد می‌کنید.
- یک اتصال سفارشی برای مدل تنظیم‌شده Phi-3 اضافه می‌کنید.
- Prompt flow را برای چت با مدل سفارشی Phi-3 تنظیم می‌کنید.

> [!NOTE]
> شما همچنین می‌توانید از طریق Azure ML Studio با Promptflow ادغام کنید. فرآیند ادغام مشابه در Azure ML Studio نیز قابل اعمال است.

#### ایجاد Hub در Azure AI Foundry

قبل از ایجاد پروژه، باید یک Hub ایجاد کنید. Hub مانند یک گروه منابع عمل می‌کند و به شما امکان می‌دهد چندین پروژه را در Azure AI Foundry سازماندهی و مدیریت کنید.

1. به [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) بروید.

1. از نوار کناری سمت چپ، **All hubs** را انتخاب کنید.

1. از منوی ناوبری، **+ New hub** را انتخاب کنید.

    ![ایجاد hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.fa.png)

1. کارهای زیر را انجام دهید:

    - نامی یکتا برای **Hub name** وارد کنید.
    - **Subscription** Azure خود را انتخاب کنید.
    - **Resource group** مورد نظر خود را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).
    - **Location** مورد نظر خود را انتخاب کنید.
    - **Connect Azure AI Services** مورد نظر خود را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).
    - **Connect Azure AI Search** را به **Skip connecting** تنظیم کنید.

    ![تکمیل hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.fa.png)

1. گزینه **Next** را انتخاب کنید.

#### ایجاد پروژه در Azure AI Foundry

1. در Hub که ایجاد کرده‌اید، از نوار کناری سمت چپ **All projects** را انتخاب کنید.

1. از منوی ناوبری، **+ New project** را انتخاب کنید.

    ![انتخاب پروژه جدید.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.fa.png)

1. نامی یکتا برای **Project name** وارد کنید.

    ![ایجاد پروژه.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.fa.png)

1. گزینه **Create a project** را انتخاب کنید.

#### اضافه کردن اتصال سفارشی برای مدل تنظیم‌شده Phi-3

برای ادغام مدل سفارشی Phi-3 خود با Prompt flow، باید نقطه پایانی و کلید مدل را در یک اتصال سفارشی ذخیره کنید. این تنظیم دسترسی به مدل سفارشی Phi-3 شما را در Prompt flow تضمین می‌کند.

#### تنظیم کلید API و آدرس URI نقطه پایانی مدل تنظیم‌شده Phi-3

1. به [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) بروید.

1. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.

1. از نوار کناری سمت چپ، **Endpoints** را انتخاب کنید.

    ![انتخاب نقاط پایانی.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.fa.png)

1. نقطه پایانی که ایجاد کرده‌اید را انتخاب کنید.

    ![انتخاب نقاط پایانی.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.fa.png)

1. از منوی ناوبری، **Consume** را انتخاب کنید.

1. **REST endpoint** و **Primary key** خود را کپی کنید.
![کپی کردن کلید API و آدرس Endpoint.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.fa.png)

#### اضافه کردن اتصال سفارشی

1. به [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) مراجعه کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

1. در پروژه‌ای که ایجاد کرده‌اید، از نوار سمت چپ **Settings** را انتخاب کنید.

1. گزینه **+ New connection** را انتخاب کنید.

   ![انتخاب اتصال جدید.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.fa.png)

1. از منوی ناوبری گزینه **Custom keys** را انتخاب کنید.

   ![انتخاب کلیدهای سفارشی.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.fa.png)

1. مراحل زیر را انجام دهید:

   - گزینه **+ Add key value pairs** را انتخاب کنید.
   - برای نام کلید، **endpoint** وارد کنید و آدرس Endpoint که از Azure ML Studio کپی کرده‌اید را در قسمت مقدار قرار دهید.
   - دوباره گزینه **+ Add key value pairs** را انتخاب کنید.
   - برای نام کلید، **key** وارد کنید و کلیدی که از Azure ML Studio کپی کرده‌اید را در قسمت مقدار قرار دهید.
   - پس از اضافه کردن کلیدها، گزینه **is secret** را انتخاب کنید تا از نمایش کلید جلوگیری شود.

   ![اضافه کردن اتصال.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.fa.png)

1. گزینه **Add connection** را انتخاب کنید.

#### ایجاد Prompt flow

شما یک اتصال سفارشی در Azure AI Foundry اضافه کرده‌اید. حالا، بیایید با مراحل زیر یک Prompt flow ایجاد کنیم. سپس، این Prompt flow را به اتصال سفارشی متصل می‌کنید تا بتوانید مدل تنظیم‌شده را در Prompt flow استفاده کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

1. از نوار سمت چپ **Prompt flow** را انتخاب کنید.

1. از منوی ناوبری گزینه **+ Create** را انتخاب کنید.

   ![انتخاب Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.fa.png)

1. از منوی ناوبری گزینه **Chat flow** را انتخاب کنید.

   ![انتخاب chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.fa.png)

1. **Folder name** مورد نظر را وارد کنید.

   ![وارد کردن نام.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.fa.png)

2. گزینه **Create** را انتخاب کنید.

#### تنظیم Prompt flow برای چت با مدل سفارشی Phi-3

شما باید مدل تنظیم‌شده Phi-3 را به یک Prompt flow ادغام کنید. با این حال، Prompt flow موجود برای این هدف طراحی نشده است. بنابراین، باید Prompt flow را بازطراحی کنید تا ادغام مدل سفارشی امکان‌پذیر شود.

1. در Prompt flow، مراحل زیر را برای بازسازی جریان موجود انجام دهید:

   - گزینه **Raw file mode** را انتخاب کنید.
   - تمام کدهای موجود در فایل *flow.dag.yml* را حذف کنید.
   - کد زیر را به فایل *flow.dag.yml* اضافه کنید.

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

   - گزینه **Save** را انتخاب کنید.

   ![انتخاب حالت raw file.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.fa.png)

1. کد زیر را به فایل *integrate_with_promptflow.py* اضافه کنید تا از مدل سفارشی Phi-3 در Prompt flow استفاده شود.

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

   ![چسباندن کد Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.fa.png)

> [!NOTE]
> برای اطلاعات بیشتر درباره استفاده از Prompt flow در Azure AI Foundry می‌توانید به [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) مراجعه کنید.

1. گزینه‌های **Chat input** و **Chat output** را برای فعال‌سازی چت با مدل خود انتخاب کنید.

   ![ورودی و خروجی.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.fa.png)

1. اکنون آماده هستید تا با مدل سفارشی Phi-3 خود چت کنید. در تمرین بعدی، یاد می‌گیرید که چگونه Prompt flow را شروع کرده و از آن برای چت با مدل تنظیم‌شده Phi-3 استفاده کنید.

> [!NOTE]
>
> جریان بازسازی‌شده باید شبیه تصویر زیر باشد:
>
> ![نمونه جریان.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.fa.png)
>

### چت با مدل سفارشی Phi-3

اکنون که مدل سفارشی Phi-3 خود را تنظیم و در Prompt flow ادغام کرده‌اید، آماده شروع تعامل با آن هستید. این تمرین شما را در فرآیند تنظیم و شروع چت با مدل خود با استفاده از Prompt flow راهنمایی می‌کند. با دنبال کردن این مراحل، می‌توانید به طور کامل از قابلیت‌های مدل تنظیم‌شده Phi-3 خود برای وظایف و مکالمات مختلف بهره‌مند شوید.

- با استفاده از Prompt flow با مدل سفارشی Phi-3 خود چت کنید.

#### شروع Prompt flow

1. گزینه **Start compute sessions** را برای شروع Prompt flow انتخاب کنید.

   ![شروع جلسه محاسباتی.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.fa.png)

1. گزینه **Validate and parse input** را برای تجدید پارامترها انتخاب کنید.

   ![اعتبارسنجی ورودی.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.fa.png)

1. مقدار **connection** را به اتصال سفارشی که ایجاد کرده‌اید تنظیم کنید. برای مثال، *connection*.

   ![اتصال.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.fa.png)

#### چت با مدل سفارشی خود

1. گزینه **Chat** را انتخاب کنید.

   ![انتخاب چت.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.fa.png)

1. اینجا یک نمونه از نتایج آورده شده است: حالا می‌توانید با مدل سفارشی Phi-3 خود چت کنید. توصیه می‌شود سوالاتی را بپرسید که بر اساس داده‌های استفاده‌شده برای تنظیم مدل باشند.

   ![چت با Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.fa.png)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.