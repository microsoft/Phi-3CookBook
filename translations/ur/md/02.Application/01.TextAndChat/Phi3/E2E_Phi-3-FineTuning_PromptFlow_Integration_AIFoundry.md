# Azure AI Foundry میں Prompt Flow کے ساتھ اپنی مرضی کے Phi-3 ماڈلز کو بہتر بنائیں اور ضم کریں

یہ مکمل گائیڈ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" پر مبنی ہے، جو Microsoft Tech Community کی طرف سے فراہم کی گئی ہے۔ یہ گائیڈ Phi-3 ماڈلز کو بہتر بنانے، ڈیپلوئے کرنے، اور Azure AI Foundry میں Prompt Flow کے ساتھ ضم کرنے کے عمل کو متعارف کراتی ہے۔  
اس گائیڈ کے برعکس، "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)"، جو مقامی طور پر کوڈ چلانے پر مرکوز تھی، یہ ٹیوٹوریل مکمل طور پر Azure AI/ML Studio کے اندر ماڈل کو بہتر بنانے اور ضم کرنے پر مرکوز ہے۔

## جائزہ

اس مکمل گائیڈ میں، آپ سیکھیں گے کہ Phi-3 ماڈل کو کیسے بہتر بنائیں اور اسے Azure AI Foundry میں Prompt Flow کے ساتھ ضم کریں۔ Azure AI/ML Studio کا استعمال کرتے ہوئے، آپ اپنی مرضی کے AI ماڈلز کو ڈیپلوئے اور استعمال کرنے کے لیے ایک ورک فلو قائم کریں گے۔ یہ گائیڈ تین منظرناموں میں تقسیم ہے:

**منظرنامہ 1: Azure وسائل سیٹ اپ کریں اور بہتر بنانے کے لیے تیاری کریں**

**منظرنامہ 2: Phi-3 ماڈل کو بہتر بنائیں اور Azure Machine Learning Studio میں ڈیپلوئے کریں**

**منظرنامہ 3: Prompt Flow کے ساتھ ضم کریں اور Azure AI Foundry میں اپنے ماڈل کے ساتھ چیٹ کریں**

یہاں اس گائیڈ کا ایک جائزہ دیا گیا ہے۔

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ur.png)

### مشمولات کی فہرست

1. **[منظرنامہ 1: Azure وسائل سیٹ اپ کریں اور بہتر بنانے کے لیے تیاری کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace بنائیں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure سبسکرپشن میں GPU کوٹہ کی درخواست کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [رول اسائنمنٹ شامل کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [پروجیکٹ سیٹ اپ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [بہتر بنانے کے لیے ڈیٹا سیٹ تیار کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[منظرنامہ 2: Phi-3 ماڈل کو بہتر بنائیں اور Azure Machine Learning Studio میں ڈیپلوئے کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 ماڈل کو بہتر بنائیں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [بہتر بنایا ہوا Phi-3 ماڈل ڈیپلوئے کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[منظرنامہ 3: Prompt Flow کے ساتھ ضم کریں اور Azure AI Foundry میں اپنے ماڈل کے ساتھ چیٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [اپنے Phi-3 ماڈل کو Prompt Flow کے ساتھ ضم کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [اپنے Phi-3 ماڈل کے ساتھ چیٹ کریں](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## منظرنامہ 1: Azure وسائل سیٹ اپ کریں اور بہتر بنانے کے لیے تیاری کریں

### Azure Machine Learning Workspace بنائیں

1. **پورٹل پیج** کے اوپر موجود **سرچ بار** میں *azure machine learning* ٹائپ کریں اور ظاہر ہونے والے آپشنز میں سے **Azure Machine Learning** منتخب کریں۔

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ur.png)

2. نیویگیشن مینو سے **+ Create** منتخب کریں۔

3. نیویگیشن مینو سے **New workspace** منتخب کریں۔

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ur.png)

4. درج ذیل کام کریں:

    - اپنی Azure **سبسکرپشن** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں (ضرورت پڑنے پر نیا بنائیں)۔
    - **Workspace Name** درج کریں۔ یہ منفرد ہونا چاہیے۔
    - اپنی پسندیدہ **Region** منتخب کریں۔
    - استعمال کرنے کے لیے **Storage account** منتخب کریں (ضرورت پڑنے پر نیا بنائیں)۔
    - استعمال کرنے کے لیے **Key vault** منتخب کریں (ضرورت پڑنے پر نیا بنائیں)۔
    - استعمال کرنے کے لیے **Application insights** منتخب کریں (ضرورت پڑنے پر نیا بنائیں)۔
    - استعمال کرنے کے لیے **Container registry** منتخب کریں (ضرورت پڑنے پر نیا بنائیں)۔

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ur.png)

5. **Review + Create** منتخب کریں۔

6. **Create** منتخب کریں۔

### Azure سبسکرپشن میں GPU کوٹہ کی درخواست کریں

اس ٹیوٹوریل میں، آپ GPU کا استعمال کرتے ہوئے Phi-3 ماڈل کو بہتر بنائیں گے اور ڈیپلوئے کریں گے۔ بہتر بنانے کے لیے، آپ *Standard_NC24ads_A100_v4* GPU استعمال کریں گے، جو کوٹہ کی درخواست کا تقاضا کرتا ہے۔ ڈیپلوئے کرنے کے لیے، آپ *Standard_NC6s_v3* GPU استعمال کریں گے، جو کوٹہ کی درخواست کا بھی تقاضا کرتا ہے۔

> [!NOTE]
>
> صرف Pay-As-You-Go سبسکرپشنز (معیاری سبسکرپشن کی قسم) GPU الاٹمنٹ کے لیے اہل ہیں؛ فائدہ سبسکرپشنز فی الحال سپورٹ نہیں کی جاتیں۔
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. *Standard NCADSA100v4 Family* کوٹہ کی درخواست کرنے کے لیے درج ذیل کام کریں:

    - بائیں جانب والے ٹیب سے **Quota** منتخب کریں۔
    - استعمال کرنے کے لیے **Virtual machine family** منتخب کریں۔ مثال کے طور پر، **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** منتخب کریں، جس میں *Standard_NC24ads_A100_v4* GPU شامل ہے۔
    - نیویگیشن مینو سے **Request quota** منتخب کریں۔

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ur.png)

    - **Request quota** صفحہ میں، مطلوبہ **New cores limit** درج کریں۔ مثال کے طور پر، 24۔
    - **Request quota** صفحہ میں، GPU کوٹہ کی درخواست کرنے کے لیے **Submit** منتخب کریں۔

1. *Standard NCSv3 Family* کوٹہ کی درخواست کرنے کے لیے درج ذیل کام کریں:

    - بائیں جانب والے ٹیب سے **Quota** منتخب کریں۔
    - استعمال کرنے کے لیے **Virtual machine family** منتخب کریں۔ مثال کے طور پر، **Standard NCSv3 Family Cluster Dedicated vCPUs** منتخب کریں، جس میں *Standard_NC6s_v3* GPU شامل ہے۔
    - نیویگیشن مینو سے **Request quota** منتخب کریں۔
    - **Request quota** صفحہ میں، مطلوبہ **New cores limit** درج کریں۔ مثال کے طور پر، 24۔
    - **Request quota** صفحہ میں، GPU کوٹہ کی درخواست کرنے کے لیے **Submit** منتخب کریں۔

### رول اسائنمنٹ شامل کریں

اپنے ماڈلز کو بہتر بنانے اور ڈیپلوئے کرنے کے لیے، آپ کو پہلے ایک **User Assigned Managed Identity (UAI)** بنانا ہوگا اور اسے مناسب اجازتیں تفویض کرنی ہوں گی۔ یہ UAI ڈیپلوئےمنٹ کے دوران توثیق کے لیے استعمال ہوگی۔

#### User Assigned Managed Identity (UAI) بنائیں

1. **پورٹل پیج** کے اوپر موجود **سرچ بار** میں *managed identities* ٹائپ کریں اور ظاہر ہونے والے آپشنز میں سے **Managed Identities** منتخب کریں۔

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ur.png)

1. **+ Create** منتخب کریں۔

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ur.png)

1. درج ذیل کام کریں:

    - اپنی Azure **سبسکرپشن** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں (ضرورت پڑنے پر نیا بنائیں)۔
    - اپنی پسندیدہ **Region** منتخب کریں۔
    - **Name** درج کریں۔ یہ منفرد ہونا چاہیے۔

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ur.png)

1. **Review + create** منتخب کریں۔

1. **+ Create** منتخب کریں۔

#### Managed Identity کو Contributor رول اسائنمنٹ شامل کریں

1. وہ Managed Identity ریسورس کھولیں جو آپ نے بنایا ہے۔

1. بائیں جانب والے ٹیب سے **Azure role assignments** منتخب کریں۔

1. نیویگیشن مینو سے **+Add role assignment** منتخب کریں۔

1. **Add role assignment** صفحہ میں، درج ذیل کام کریں:
    - **Scope** کو **Resource group** پر سیٹ کریں۔
    - اپنی Azure **سبسکرپشن** منتخب کریں۔
    - استعمال کرنے کے لیے **Resource group** منتخب کریں۔
    - **Role** کو **Contributor** پر سیٹ کریں۔

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ur.png)

2. **Save** منتخب کریں۔

#### Managed Identity کو Storage Blob Data Reader رول اسائنمنٹ شامل کریں

1. **پورٹل پیج** کے اوپر موجود **سرچ بار** میں *storage accounts* ٹائپ کریں اور ظاہر ہونے والے آپشنز میں سے **Storage accounts** منتخب کریں۔

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ur.png)

1. اس اسٹوریج اکاؤنٹ کو منتخب کریں جو آپ کے Azure Machine Learning ورک اسپیس کے ساتھ وابستہ ہے۔ مثال کے طور پر، *finetunephistorage*۔

1. **Add role assignment** صفحہ پر جانے کے لیے درج ذیل کام کریں:

    - اپنے بنائے گئے Azure Storage اکاؤنٹ پر جائیں۔
    - بائیں جانب والے ٹیب سے **Access Control (IAM)** منتخب کریں۔
    - نیویگیشن مینو سے **+ Add** منتخب کریں۔
    - نیویگیشن مینو سے **Add role assignment** منتخب کریں۔

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ur.png)

1. **Add role assignment** صفحہ میں، درج ذیل کام کریں:

    - **Role** صفحہ میں، **Storage Blob Data Reader** کو تلاش کریں اور منتخب کریں۔
    - **Role** صفحہ میں، **Next** منتخب کریں۔
    - **Members** صفحہ میں، **Assign access to** کو **Managed identity** پر سیٹ کریں۔
    - **Members** صفحہ میں، **+ Select members** منتخب کریں۔
    - **Select managed identities** صفحہ میں، اپنی Azure **سبسکرپشن** منتخب کریں۔
    - **Select managed identities** صفحہ میں، **Managed identity** منتخب کریں۔
    - **Select managed identities** صفحہ میں، وہ Managed Identity منتخب کریں جو آپ نے بنایا تھا۔ مثال کے طور پر، *finetunephi-managedidentity*۔
    - **Select managed identities** صفحہ میں، **Select** منتخب کریں۔

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ur.png)

1. **Review + assign** منتخب کریں۔

#### Managed Identity کو AcrPull رول اسائنمنٹ شامل کریں

1. **پورٹل پیج** کے اوپر موجود **سرچ بار** میں *container registries* ٹائپ کریں اور ظاہر ہونے والے آپشنز میں سے **Container registries** منتخب کریں۔

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ur.png)

1. اس کنٹینر رجسٹری کو منتخب کریں جو آپ کے Azure Machine Learning ورک اسپیس کے ساتھ وابستہ ہے۔ مثال کے طور پر، *finetunephicontainerregistry*۔

1. **Add role assignment** صفحہ پر جانے کے لیے درج ذیل کام کریں:

    - بائیں جانب والے ٹیب سے **Access Control (IAM)** منتخب کریں۔
    - نیویگیشن مینو سے **+ Add** منتخب کریں۔
    - نیویگیشن مینو سے **Add role assignment** منتخب کریں۔

1. **Add role assignment** صفحہ میں، درج ذیل کام کریں:

    - **Role** صفحہ میں، **AcrPull** کو تلاش کریں اور منتخب کریں۔
    - **Role** صفحہ میں، **Next** منتخب کریں۔
    - **Members** صفحہ میں، **Assign access to** کو **Managed identity** پر سیٹ کریں۔
    - **Members** صفحہ میں، **+ Select members** منتخب کریں۔
    - **Select managed identities** صفحہ میں، اپنی Azure **سبسکرپشن** منتخب کریں۔
    - **Select managed identities** صفحہ میں، **Managed identity** منتخب کریں۔
    - **Select managed identities** صفحہ میں، وہ Managed Identity منتخب کریں جو آپ نے بنایا تھا۔ مثال کے طور پر، *finetunephi-managedidentity*۔
    - **Select managed identities** صفحہ میں، **Select** منتخب کریں۔
    - **Review + assign** منتخب کریں۔

### پروجیکٹ سیٹ اپ کریں

ڈیٹا سیٹ ڈاؤن لوڈ کرنے کے لیے، آپ ایک مقامی ماحول سیٹ اپ کریں گے۔

اس مشق میں، آپ:

- کام کرنے کے لیے ایک فولڈر بنائیں گے۔
- ایک ورچوئل ماحول بنائیں گے۔
- مطلوبہ پیکجز انسٹال کریں گے۔
- ڈیٹا سیٹ ڈاؤن لوڈ کرنے کے لیے *download_dataset.py* فائل بنائیں گے۔

#### کام کرنے کے لیے ایک فولڈر بنائیں

1. ایک ٹرمینل ونڈو کھولیں اور *finetune-phi* نامی فولڈر بنانے کے لیے درج ذیل کمانڈ ٹائپ کریں۔

    ```console
    mkdir finetune-phi
    ```

2. ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ آپ بنائے گئے *finetune-phi* فولڈر میں جائیں۔

    ```console
    cd finetune-phi
    ```

#### ایک ورچوئل ماحول بنائیں

1. ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں تاکہ *.venv* نامی ورچوئل ماحول بنایا جا سکے۔

    ```console
    python -m venv .venv
    ```

2. ورچوئل ماحول کو ایکٹیویٹ کرنے کے لیے ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں۔

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> اگر یہ کام کر گیا، تو آپ کو کمانڈ پرامپٹ کے سامنے *(.venv)* نظر آنا چاہیے۔

#### مطلوبہ پیکجز انسٹال کریں

1. درج ذیل کمانڈز ٹرمینل میں ٹائپ کریں تاکہ مطلوبہ پیکجز انسٹال کیے جا سکیں۔

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` بنائیں

> [!NOTE]
> مکمل فولڈر اسٹرکچر:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** کھولیں۔

1. مینو بار سے **File** منتخب کریں۔

1. **Open Folder** منتخب کریں۔

1. *finetune-phi* فولڈر منتخب کریں جو آپ نے بنایا تھا، جو *C:\Users\yourUserName\finetune-phi* پر واقع ہے۔

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.ur.png)

1. Visual Studio Code کے بائیں پین میں، دائیں کلک کریں اور **New File** منتخب کریں تاکہ *download_dataset.py* نامی نئی فائل بنائی جا سکے۔

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.ur.png)

### بہتر بنانے کے لیے ڈیٹا سیٹ تیار کریں

اس مشق میں، آپ *download_dataset.py* فائل چلا کر *ultrachat_200k* ڈیٹا سیٹ کو اپنے مقامی ماحول میں ڈاؤن لوڈ کریں گے۔ آپ پھر اس ڈیٹا سیٹ کو Azure Machine Learning میں Phi-3 ماڈل کو بہتر بنانے کے لیے استعمال کریں گے۔

اس مشق میں، آپ:

- *download_dataset.py* فائل میں کوڈ شامل کریں تاکہ ڈیٹا سیٹ ڈاؤن لوڈ کیا جا سکے۔
- *download_dataset.py* فائل چلائیں تاکہ ڈیٹا سیٹ مقامی ماحول میں ڈاؤن لوڈ ہو جائے۔

#### *download_dataset.py* کا استعمال کرتے ہوئے اپنا ڈیٹا سیٹ ڈاؤن لوڈ کریں

1. Visual Studio Code میں *download_dataset.py* فائل کھولیں۔

1. درج ذیل کوڈ *download_dataset.py* فائل میں شامل کریں۔

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

1. اسکرپٹ چلانے اور ڈیٹا سیٹ کو اپنے مقامی ماحول میں ڈاؤن لوڈ کرنے کے لیے ٹرمینل میں درج ذیل
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. بائیں طرف والے ٹیب سے **Compute** منتخب کریں۔

1. نیویگیشن مینو سے **Compute clusters** منتخب کریں۔

1. **+ New** پر کلک کریں۔

    ![Compute منتخب کریں۔](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ur.png)

1. درج ذیل کام انجام دیں:

    - وہ **Region** منتخب کریں جسے آپ استعمال کرنا چاہتے ہیں۔
    - **Virtual machine tier** کو **Dedicated** پر سیٹ کریں۔
    - **Virtual machine type** کو **GPU** پر سیٹ کریں۔
    - **Virtual machine size** فلٹر کو **Select from all options** پر سیٹ کریں۔
    - **Virtual machine size** کو **Standard_NC24ads_A100_v4** پر منتخب کریں۔

    ![کلسٹر بنائیں۔](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ur.png)

1. **Next** منتخب کریں۔

1. درج ذیل کام انجام دیں:

    - **Compute name** درج کریں۔ یہ منفرد ہونا چاہیے۔
    - **Minimum number of nodes** کو **0** پر سیٹ کریں۔
    - **Maximum number of nodes** کو **1** پر سیٹ کریں۔
    - **Idle seconds before scale down** کو **120** پر سیٹ کریں۔

    ![کلسٹر بنائیں۔](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ur.png)

1. **Create** منتخب کریں۔

#### Phi-3 ماڈل کو فائن ٹون کریں

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. وہ Azure Machine Learning ورک اسپیس منتخب کریں جو آپ نے بنائی تھی۔

    ![وہ ورک اسپیس منتخب کریں جو آپ نے بنائی۔](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ur.png)

1. درج ذیل کام انجام دیں:

    - بائیں طرف والے ٹیب سے **Model catalog** منتخب کریں۔
    - **سرچ بار** میں *phi-3-mini-4k* ٹائپ کریں اور جو آپشنز آئیں ان میں سے **Phi-3-mini-4k-instruct** منتخب کریں۔

    ![phi-3-mini-4k ٹائپ کریں۔](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ur.png)

1. نیویگیشن مینو سے **Fine-tune** منتخب کریں۔

    ![فائن ٹون منتخب کریں۔](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ur.png)

1. درج ذیل کام انجام دیں:

    - **Select task type** کو **Chat completion** پر سیٹ کریں۔
    - **+ Select data** منتخب کریں تاکہ **Training data** اپلوڈ کر سکیں۔
    - Validation data اپلوڈ کرنے کا طریقہ **Provide different validation data** پر سیٹ کریں۔
    - **+ Select data** منتخب کریں تاکہ **Validation data** اپلوڈ کر سکیں۔

    ![فائن ٹوننگ پیج بھریں۔](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ur.png)

    > [!TIP]
    >
    > آپ **Advanced settings** منتخب کر کے کنفیگریشن جیسے **learning_rate** اور **lr_scheduler_type** کو اپنی ضروریات کے مطابق بہتر بنا سکتے ہیں۔

1. **Finish** منتخب کریں۔

1. اس مشق میں، آپ نے Azure Machine Learning کا استعمال کرتے ہوئے کامیابی سے Phi-3 ماڈل کو فائن ٹون کیا۔ براہ کرم نوٹ کریں کہ فائن ٹوننگ کا عمل کافی وقت لے سکتا ہے۔ فائن ٹوننگ جاب چلانے کے بعد، آپ کو اس کے مکمل ہونے کا انتظار کرنا ہوگا۔ آپ اپنی Azure Machine Learning ورک اسپیس کے بائیں طرف والے **Jobs** ٹیب پر جاکر فائن ٹوننگ جاب کی اسٹیٹس کو مانیٹر کر سکتے ہیں۔ اگلی سیریز میں، آپ فائن ٹون کیے گئے ماڈل کو ڈیپلوئے کریں گے اور اسے Prompt flow کے ساتھ انٹیگریٹ کریں گے۔

    ![فائن ٹوننگ جاب دیکھیں۔](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ur.png)

### فائن ٹون کیے گئے Phi-3 ماڈل کو ڈیپلوئے کریں

فائن ٹون کیے گئے Phi-3 ماڈل کو Prompt flow کے ساتھ انٹیگریٹ کرنے کے لیے، آپ کو ماڈل کو ریئل ٹائم انفرنس کے لیے قابل رسائی بنانے کے لیے ڈیپلوئے کرنا ہوگا۔ اس عمل میں ماڈل کو رجسٹر کرنا، ایک آن لائن اینڈ پوائنٹ بنانا، اور ماڈل کو ڈیپلوئے کرنا شامل ہے۔

اس مشق میں، آپ:

- Azure Machine Learning ورک اسپیس میں فائن ٹون کیے گئے ماڈل کو رجسٹر کریں گے۔
- ایک آن لائن اینڈ پوائنٹ بنائیں گے۔
- رجسٹرڈ فائن ٹون کیے گئے Phi-3 ماڈل کو ڈیپلوئے کریں گے۔

#### فائن ٹون کیے گئے ماڈل کو رجسٹر کریں

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) پر جائیں۔

1. وہ Azure Machine Learning ورک اسپیس منتخب کریں جو آپ نے بنائی تھی۔

    ![وہ ورک اسپیس منتخب کریں جو آپ نے بنائی۔](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ur.png)

1. بائیں طرف والے ٹیب سے **Models** منتخب کریں۔
1. **+ Register** منتخب کریں۔
1. **From a job output** منتخب کریں۔

    ![ماڈل رجسٹر کریں۔](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ur.png)

1. وہ جاب منتخب کریں جو آپ نے بنائی تھی۔

    ![جاب منتخب کریں۔](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ur.png)

1. **Next** منتخب کریں۔

1. **Model type** کو **MLflow** پر سیٹ کریں۔

1. یقینی بنائیں کہ **Job output** منتخب ہے؛ یہ خودکار طور پر منتخب ہونا چاہیے۔

    ![آؤٹ پٹ منتخب کریں۔](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ur.png)

2. **Next** منتخب کریں۔

3. **Register** منتخب کریں۔

    ![رجسٹر منتخب کریں۔](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ur.png)

4. آپ اپنے رجسٹرڈ ماڈل کو بائیں طرف والے ٹیب سے **Models** مینو میں جاکر دیکھ سکتے ہیں۔

    ![رجسٹرڈ ماڈل۔](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ur.png)

#### فائن ٹون کیے گئے ماڈل کو ڈیپلوئے کریں

1. اس Azure Machine Learning ورک اسپیس میں جائیں جو آپ نے بنائی تھی۔

1. بائیں طرف والے ٹیب سے **Endpoints** منتخب کریں۔

1. نیویگیشن مینو سے **Real-time endpoints** منتخب کریں۔

    ![اینڈ پوائنٹ بنائیں۔](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ur.png)

1. **Create** منتخب کریں۔

1. وہ رجسٹرڈ ماڈل منتخب کریں جو آپ نے بنایا تھا۔

    ![رجسٹرڈ ماڈل منتخب کریں۔](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ur.png)

1. **Select** منتخب کریں۔

1. درج ذیل کام انجام دیں:

    - **Virtual machine** کو *Standard_NC6s_v3* پر منتخب کریں۔
    - وہ **Instance count** منتخب کریں جو آپ استعمال کرنا چاہتے ہیں۔ مثلاً، *1*۔
    - **Endpoint** کو **New** پر سیٹ کریں تاکہ ایک نیا اینڈ پوائنٹ بنایا جا سکے۔
    - **Endpoint name** درج کریں۔ یہ منفرد ہونا چاہیے۔
    - **Deployment name** درج کریں۔ یہ منفرد ہونا چاہیے۔

    ![ڈیپلوئےمنٹ سیٹنگ بھریں۔](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ur.png)

1. **Deploy** منتخب کریں۔

> [!WARNING]
> اپنے اکاؤنٹ پر اضافی چارجز سے بچنے کے لیے، Azure Machine Learning ورک اسپیس میں بنائے گئے اینڈ پوائنٹ کو حذف کرنا یقینی بنائیں۔
>

#### Azure Machine Learning ورک اسپیس میں ڈیپلوئےمنٹ اسٹیٹس چیک کریں

1. اس Azure Machine Learning ورک اسپیس میں جائیں جو آپ نے بنائی تھی۔

1. بائیں طرف والے ٹیب سے **Endpoints** منتخب کریں۔

1. وہ اینڈ پوائنٹ منتخب کریں جو آپ نے بنایا تھا۔

    ![اینڈ پوائنٹس منتخب کریں۔](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ur.png)

1. اس صفحے پر، آپ ڈیپلوئےمنٹ کے عمل کے دوران اینڈ پوائنٹس کو مینیج کر سکتے ہیں۔

> [!NOTE]
> ایک بار جب ڈیپلوئےمنٹ مکمل ہو جائے، تو یقینی بنائیں کہ **Live traffic** کو **100%** پر سیٹ کیا گیا ہے۔ اگر ایسا نہ ہو تو، **Update traffic** منتخب کریں تاکہ ٹریفک سیٹنگز کو ایڈجسٹ کیا جا سکے۔ نوٹ کریں کہ اگر ٹریفک 0% پر سیٹ ہو تو آپ ماڈل کو ٹیسٹ نہیں کر سکتے۔
>
> ![ٹریفک سیٹ کریں۔](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ur.png)
>
Translation for chunk 3 skipped due to timeout.

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ سروسز کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔