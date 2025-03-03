# फाईन-ट्यून करा आणि Azure AI Foundry मध्ये Prompt flow सह कस्टम Phi-3 मॉडेल्स एकत्रित करा

ही एंड-टू-एंड (E2E) नमुना प्रक्रिया Microsoft Tech Community मधील "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" मार्गदर्शिकेवर आधारित आहे. यामध्ये Phi-3 मॉडेल्सचे फाईन-ट्यूनिंग, तैनाती, आणि Prompt flow सह Azure AI Foundry मध्ये एकत्रिकरणाच्या प्रक्रिया समाविष्ट आहेत. 
या ट्युटोरियलमध्ये स्थानिकरित्या कोड चालवण्याऐवजी Azure AI/ML Studio मध्ये मॉडेल फाईन-ट्यून आणि एकत्रिकरणावर पूर्णतः लक्ष केंद्रित केले आहे.

## आढावा

या E2E नमुन्यामध्ये, तुम्ही Phi-3 मॉडेल फाईन-ट्यून कसे करायचे आणि Azure AI Foundry मधील Prompt flow सह ते कसे एकत्र करायचे हे शिकाल. Azure AI/ML Studio चा वापर करून, तुम्ही कस्टम AI मॉडेल्स तैनात करण्यासाठी आणि वापरण्यासाठी कार्यप्रवाह तयार कराल. हा E2E नमुना तीन परिस्थितींमध्ये विभागलेला आहे:

**परिस्थिती 1: Azure संसाधने सेट करा आणि फाईन-ट्यूनिंगसाठी तयारी करा**

**परिस्थिती 2: Phi-3 मॉडेल फाईन-ट्यून करा आणि Azure Machine Learning Studio मध्ये तैनात करा**

**परिस्थिती 3: Prompt flow सह एकत्रिकरण करा आणि Azure AI Foundry मध्ये तुमच्या कस्टम मॉडेलशी संवाद साधा**

खाली या E2E नमुन्याचा आढावा दिला आहे.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.mr.png)

### विषय सूची

1. **[परिस्थिती 1: Azure संसाधने सेट करा आणि फाईन-ट्यूनिंगसाठी तयारी करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace तयार करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure Subscription मध्ये GPU कोटा मागणी करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [भूमिका असाइनमेंट जोडा](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [प्रकल्प सेट करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाईन-ट्यूनिंगसाठी डेटासेट तयार करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)

2. **[परिस्थिती 2: Phi-3 मॉडेल फाईन-ट्यून करा आणि Azure Machine Learning Studio मध्ये तैनात करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 मॉडेल फाईन-ट्यून करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [फाईन-ट्यून केलेले Phi-3 मॉडेल तैनात करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)

3. **[परिस्थिती 3: Prompt flow सह एकत्रिकरण करा आणि Azure AI Foundry मध्ये तुमच्या कस्टम मॉडेलशी संवाद साधा](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Prompt flow सह कस्टम Phi-3 मॉडेल एकत्र करा](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [तुमच्या कस्टम Phi-3 मॉडेलशी संवाद साधा](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## परिस्थिती 1: Azure संसाधने सेट करा आणि फाईन-ट्यूनिंगसाठी तयारी करा

### Azure Machine Learning Workspace तयार करा

1. **Azure Machine Learning** शोधण्यासाठी पोर्टल पृष्ठाच्या शीर्षस्थानी **शोध पट्टीत** *azure machine learning* टाइप करा आणि दिसणाऱ्या पर्यायांमधून **Azure Machine Learning** निवडा.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.mr.png)

2. नेव्हिगेशन मेनूमधून **+ Create** निवडा.

3. नेव्हिगेशन मेनूमधून **New workspace** निवडा.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.mr.png)

4. खालील कार्ये पूर्ण करा:

    - तुमचे Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - **Workspace Name** प्रविष्ट करा. हे एक अद्वितीय मूल्य असले पाहिजे.
    - वापरण्यासाठी **Region** निवडा.
    - वापरण्यासाठी **Storage account** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Key vault** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Application insights** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Container registry** निवडा (आवश्यक असल्यास नवीन तयार करा).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.mr.png)

5. **Review + Create** निवडा.

6. **Create** निवडा.

### Azure Subscription मध्ये GPU कोटा मागणी करा

या ट्युटोरियलमध्ये, तुम्ही GPUs चा वापर करून Phi-3 मॉडेल फाईन-ट्यून आणि तैनात करायला शिकाल. फाईन-ट्यूनिंगसाठी, तुम्ही *Standard_NC24ads_A100_v4* GPU वापराल, ज्यासाठी कोटा मागणी आवश्यक आहे. तैनातीसाठी, तुम्ही *Standard_NC6s_v3* GPU वापराल, ज्यासाठीही कोटा मागणी आवश्यक आहे.

> [!NOTE]
>
> फक्त Pay-As-You-Go सदस्यता (मानक सदस्यता प्रकार) GPU वाटपासाठी पात्र आहेत; लाभ सदस्यता सध्या समर्थित नाहीत.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ला भेट द्या.

1. *Standard NCADSA100v4 Family* कोटा मागणीसाठी खालील कार्ये करा:

    - डाव्या बाजूच्या टॅबमधून **Quota** निवडा.
    - वापरण्यासाठी **Virtual machine family** निवडा. उदाहरणार्थ, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** निवडा, ज्यामध्ये *Standard_NC24ads_A100_v4* GPU समाविष्ट आहे.
    - नेव्हिगेशन मेनूमधून **Request quota** निवडा.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.mr.png)

    - **Request quota** पृष्ठावर, वापरण्यासाठी **New cores limit** प्रविष्ट करा. उदाहरणार्थ, 24.
    - **Request quota** पृष्ठावर, GPU कोटा मागणीसाठी **Submit** निवडा.

1. *Standard NCSv3 Family* कोटा मागणीसाठी खालील कार्ये करा:

    - डाव्या बाजूच्या टॅबमधून **Quota** निवडा.
    - वापरण्यासाठी **Virtual machine family** निवडा. उदाहरणार्थ, **Standard NCSv3 Family Cluster Dedicated vCPUs** निवडा, ज्यामध्ये *Standard_NC6s_v3* GPU समाविष्ट आहे.
    - नेव्हिगेशन मेनूमधून **Request quota** निवडा.
    - **Request quota** पृष्ठावर, वापरण्यासाठी **New cores limit** प्रविष्ट करा. उदाहरणार्थ, 24.
    - **Request quota** पृष्ठावर, GPU कोटा मागणीसाठी **Submit** निवडा.

### भूमिका असाइनमेंट जोडा

तुमचे मॉडेल फाईन-ट्यून आणि तैनात करण्यासाठी, तुम्हाला प्रथम User Assigned Managed Identity (UAI) तयार करणे आणि त्याला योग्य परवानग्या असाइन करणे आवश्यक आहे. तैनाती दरम्यान प्रमाणीकरणासाठी या UAI चा वापर केला जाईल.

#### User Assigned Managed Identity (UAI) तयार करा

1. पोर्टल पृष्ठाच्या शीर्षस्थानी **शोध पट्टीत** *managed identities* टाइप करा आणि दिसणाऱ्या पर्यायांमधून **Managed Identities** निवडा.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.mr.png)

1. **+ Create** निवडा.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.mr.png)

1. खालील कार्ये पूर्ण करा:

    - तुमचे Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - वापरण्यासाठी **Region** निवडा.
    - **Name** प्रविष्ट करा. हे एक अद्वितीय मूल्य असले पाहिजे.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.mr.png)

1. **Review + create** निवडा.

1. **+ Create** निवडा.

#### Managed Identity साठी Contributor भूमिका असाइनमेंट जोडा

1. तुम्ही तयार केलेल्या Managed Identity संसाधनाकडे जा.

1. डाव्या बाजूच्या टॅबमधून **Azure role assignments** निवडा.

1. नेव्हिगेशन मेनूमधून **+Add role assignment** निवडा.

1. **Add role assignment** पृष्ठावर, खालील कार्ये करा:
    - **Scope** **Resource group** वर सेट करा.
    - तुमचे Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा.
    - **Role** **Contributor** वर सेट करा.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.mr.png)

2. **Save** निवडा.

#### Managed Identity साठी Storage Blob Data Reader भूमिका असाइनमेंट जोडा

1. पोर्टल पृष्ठाच्या शीर्षस्थानी **शोध पट्टीत** *storage accounts* टाइप करा आणि दिसणाऱ्या पर्यायांमधून **Storage accounts** निवडा.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.mr.png)

1. Azure Machine Learning workspace शी संबंधित storage account निवडा. उदाहरणार्थ, *finetunephistorage*.

1. **Add role assignment** पृष्ठावर नेण्यासाठी खालील कार्ये करा:

    - तयार केलेल्या Azure Storage account वर जा.
    - डाव्या बाजूच्या टॅबमधून **Access Control (IAM)** निवडा.
    - नेव्हिगेशन मेनूमधून **+ Add** निवडा.
    - नेव्हिगेशन मेनूमधून **Add role assignment** निवडा.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.mr.png)

1. **Add role assignment** पृष्ठावर, खालील कार्ये करा:

    - **Role** पृष्ठावर, **Storage Blob Data Reader** शोधा आणि दिसणाऱ्या पर्यायांमधून **Storage Blob Data Reader** निवडा.
    - **Role** पृष्ठावर, **Next** निवडा.
    - **Members** पृष्ठावर, **Assign access to** **Managed identity** निवडा.
    - **Members** पृष्ठावर, **+ Select members** निवडा.
    - **Select managed identities** पृष्ठावर, तुमचे Azure **Subscription** निवडा.
    - **Select managed identities** पृष्ठावर, **Managed identity** **Manage Identity** वर सेट करा.
    - **Select managed identities** पृष्ठावर, तुम्ही तयार केलेले Managed Identity निवडा. उदाहरणार्थ, *finetunephi-managedidentity*.
    - **Select managed identities** पृष्ठावर, **Select** निवडा.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.mr.png)

1. **Review + assign** निवडा.

#### Managed Identity साठी AcrPull भूमिका असाइनमेंट जोडा

1. पोर्टल पृष्ठाच्या शीर्षस्थानी **शोध पट्टीत** *container registries* टाइप करा आणि दिसणाऱ्या पर्यायांमधून **Container registries** निवडा.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.mr.png)

1. Azure Machine Learning workspace शी संबंधित container registry निवडा. उदाहरणार्थ, *finetunephicontainerregistry*.

1. **Add role assignment** पृष्ठावर नेण्यासाठी खालील कार्ये करा:

    - डाव्या बाजूच्या टॅबमधून **Access Control (IAM)** निवडा.
    - नेव्हिगेशन मेनूमधून **+ Add** निवडा.
    - नेव्हिगेशन मेनूमधून **Add role assignment** निवडा.

1. **Add role assignment** पृष्ठावर, खालील कार्ये करा:

    - **Role** पृष्ठावर, **AcrPull** शोधा आणि दिसणाऱ्या पर्यायांमधून **AcrPull** निवडा.
    - **Role** पृष्ठावर, **Next** निवडा.
    - **Members** पृष्ठावर, **Assign access to** **Managed identity** निवडा.
    - **Members** पृष्ठावर, **+ Select members** निवडा.
    - **Select managed identities** पृष्ठावर, तुमचे Azure **Subscription** निवडा.
    - **Select managed identities** पृष्ठावर, **Managed identity** **Manage Identity** वर सेट करा.
    - **Select managed identities** पृष्ठावर, तुम्ही तयार केलेले Managed Identity निवडा. उदाहरणार्थ, *finetunephi-managedidentity*.
    - **Select managed identities** पृष्ठावर, **Select** निवडा.
    - **Review + assign** निवडा.

### प्रकल्प सेट करा

फाईन-ट्यूनिंगसाठी आवश्यक डेटासेट डाउनलोड करण्यासाठी स्थानिक वातावरण तयार करा.

या व्यायामात, तुम्ही

- काम करण्यासाठी फोल्डर तयार कराल.
- एक आभासी वातावरण तयार कराल.
- आवश्यक पॅकेजेस स्थापित कराल.
- डेटासेट डाउनलोड करण्यासाठी *download_dataset.py* फाईल तयार कराल.

#### कामासाठी फोल्डर तयार करा

1. टर्मिनल विंडो उघडा आणि *finetune-phi* नावाचा फोल्डर तयार करण्यासाठी खालील आदेश टाइप करा.

    ```console
    mkdir finetune-phi
    ```

2. तयार केलेल्या *finetune-phi* फोल्डरमध्ये नेव्हिगेट करण्यासाठी तुमच्या टर्मिनलमध्ये खालील आदेश टाइप करा.

    ```console
    cd finetune-phi
    ```

#### आभासी वातावरण तयार करा

1. *.venv* नावाचे आभासी वातावरण तयार करण्यासाठी तुमच्या टर्मिनलमध्ये खालील आदेश टाइप करा.

    ```console
    python -m venv .venv
    ```

2. आभासी वातावरण सक्रिय करण्यासाठी तुमच्या टर्मिनलमध्ये खालील आदेश टाइप करा.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> जर हे कार्य केले असेल, तर तुम्हाला कमांड प्रॉम्प्टच्या आधी *(.venv)* दिसेल.

#### आवश्यक पॅकेजेस स्थापित करा

1. आवश्यक पॅकेजेस स्थापित करण्यासाठी तुमच्या टर्मिनलमध्ये खालील आदेश टाइप करा.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` तयार करा

> [!NOTE]
> पूर्ण फोल्डर रचना:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** उघडा.

1. मेनू बारमधून **File** निवडा.

1. **Open Folder** निवडा.

1. तुम्ही तयार केलेला *finetune-phi* फोल्डर निवडा, जो *C:\Users\yourUserName\finetune-phi* येथे स्थित आहे.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.mr.png)

1. Visual Studio Code च्या डाव्या बाजूच्या पॅनमध्ये, उजवे क्लिक करा आणि **New File** निवडा आणि *download_dataset.py* नावाची नवीन फाईल तयार करा.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.mr.png)

### फाईन-ट्यूनिंगसाठी डेटासेट तयार करा

या व्यायामात, तुम्ही *download_dataset.py* फाईल चालवून *ultrachat_200k* डेटासेट्स तुमच्या स्थानिक वातावरणात डाउनलोड कराल. नंतर तुम्ही या डेटासेट्सचा वापर Azure Machine Learning मध्ये Phi-3 मॉडेल फाईन-ट्यून करण्यासाठी कराल.

या व्यायामात, तुम्ही:

- *download_dataset.py* फाईलमध्ये कोड जोडून डेटासेट्स डाउनलोड कराल.
- *download_dataset.py* फाईल चालवून डेटासेट्स तुमच्या स्थानिक वातावरणात डाउनलोड कराल.

#### *download_dataset.py* वापरून तुमचे डेटासेट डाउनलोड करा

1. Visual Studio Code मध्ये *download_dataset.py* फाईल उघडा.

1. *download_dataset.py* फाईलमध्ये खालील कोड जोडा.

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

1. स्क्रिप्ट चालवून डेटासेट्स स्थानिक वातावरणात डाउनलोड करण्यासाठी तुमच्या टर्मिनलमध्ये खालील आदेश ट
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ला भेट द्या.

1. डाव्या बाजूच्या टॅबमधून **Compute** निवडा.

1. नेव्हिगेशन मेनूमधून **Compute clusters** निवडा.

1. **+ New** निवडा.

    ![Compute निवडा.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.mr.png)

1. खालील गोष्टी करा:

    - तुम्हाला हवी असलेली **Region** निवडा.
    - **Virtual machine tier** **Dedicated** ला निवडा.
    - **Virtual machine type** **GPU** ला निवडा.
    - **Virtual machine size** फिल्टर **Select from all options** वर सेट करा.
    - **Virtual machine size** **Standard_NC24ads_A100_v4** ला निवडा.

    ![क्लस्टर तयार करा.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.mr.png)

1. **Next** निवडा.

1. खालील गोष्टी करा:

    - **Compute name** प्रविष्ट करा. हे अद्वितीय असले पाहिजे.
    - **Minimum number of nodes** **0** ला सेट करा.
    - **Maximum number of nodes** **1** ला सेट करा.
    - **Idle seconds before scale down** **120** ला सेट करा.

    ![क्लस्टर तयार करा.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.mr.png)

1. **Create** निवडा.

#### Phi-3 मॉडेल फाइन-ट्यून करा

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ला भेट द्या.

1. तुम्ही तयार केलेले Azure Machine Learning workspace निवडा.

    ![तुमचे workspace निवडा.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.mr.png)

1. खालील गोष्टी करा:

    - डाव्या बाजूच्या टॅबमधून **Model catalog** निवडा.
    - **search bar** मध्ये *phi-3-mini-4k* टाइप करा आणि दिसणाऱ्या पर्यायांमधून **Phi-3-mini-4k-instruct** निवडा.

    ![phi-3-mini-4k टाइप करा.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.mr.png)

1. नेव्हिगेशन मेनूमधून **Fine-tune** निवडा.

    ![Fine tune निवडा.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.mr.png)

1. खालील गोष्टी करा:

    - **Select task type** **Chat completion** ला निवडा.
    - **+ Select data** निवडून **Training data** अपलोड करा.
    - Validation data अपलोड प्रकार **Provide different validation data** ला सेट करा.
    - **+ Select data** निवडून **Validation data** अपलोड करा.

    ![Fine-tuning पृष्ठ भरा.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.mr.png)

    > [!TIP]
    >
    > **Advanced settings** निवडून **learning_rate** आणि **lr_scheduler_type** सारख्या कॉन्फिगरेशन सानुकूलित करा, जेणेकरून तुमच्या गरजेनुसार फाइन-ट्यूनिंग प्रक्रिया अनुकूल होईल.

1. **Finish** निवडा.

1. या व्यायामामध्ये, तुम्ही Azure Machine Learning वापरून Phi-3 मॉडेल यशस्वीरित्या फाइन-ट्यून केले. कृपया लक्षात ठेवा की फाइन-ट्यूनिंग प्रक्रिया वेळखाऊ असू शकते. फाइन-ट्यूनिंग जॉब चालवल्यानंतर, त्याच्या पूर्ण होण्याची प्रतीक्षा करावी लागते. Azure Machine Learning Workspace च्या डाव्या बाजूच्या **Jobs** टॅबवर जाऊन तुम्ही जॉबची स्थिती मॉनिटर करू शकता. पुढील मालिकेत, तुम्ही फाइन-ट्यून केलेले मॉडेल डिप्लॉय कराल आणि ते Prompt flow सह एकत्रित कराल.

    ![Fine-tuning जॉब पहा.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.mr.png)

### फाइन-ट्यून केलेले Phi-3 मॉडेल डिप्लॉय करा

फाइन-ट्यून केलेले Phi-3 मॉडेल Prompt flow सह एकत्रित करण्यासाठी, तुम्हाला मॉडेल डिप्लॉय करावे लागेल जेणेकरून ते रिअल-टाइम इनफरन्ससाठी उपलब्ध होईल. या प्रक्रियेमध्ये मॉडेल नोंदणी करणे, ऑनलाइन एंडपॉइंट तयार करणे आणि मॉडेल डिप्लॉय करणे समाविष्ट आहे.

या व्यायामामध्ये, तुम्ही:

- Azure Machine Learning workspace मध्ये फाइन-ट्यून केलेले मॉडेल नोंदणी करा.
- ऑनलाइन एंडपॉइंट तयार करा.
- नोंदणीकृत फाइन-ट्यून केलेले Phi-3 मॉडेल डिप्लॉय करा.

#### फाइन-ट्यून केलेले मॉडेल नोंदणी करा

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ला भेट द्या.

1. तुम्ही तयार केलेले Azure Machine Learning workspace निवडा.

    ![तुमचे workspace निवडा.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.mr.png)

1. डाव्या बाजूच्या टॅबमधून **Models** निवडा.
1. **+ Register** निवडा.
1. **From a job output** निवडा.

    ![मॉडेल नोंदणी करा.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.mr.png)

1. तुम्ही तयार केलेला जॉब निवडा.

    ![जॉब निवडा.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.mr.png)

1. **Next** निवडा.

1. **Model type** **MLflow** ला निवडा.

1. **Job output** निवडलेले असल्याची खात्री करा; हे आपोआप निवडलेले असले पाहिजे.

    ![आउटपुट निवडा.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.mr.png)

2. **Next** निवडा.

3. **Register** निवडा.

    ![नोंदणी निवडा.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.mr.png)

4. डाव्या बाजूच्या **Models** मेनूमध्ये जाऊन तुम्ही तुमचे नोंदणीकृत मॉडेल पाहू शकता.

    ![नोंदणीकृत मॉडेल.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.mr.png)

#### फाइन-ट्यून केलेले मॉडेल डिप्लॉय करा

1. तुम्ही तयार केलेल्या Azure Machine Learning workspace वर जा.

1. डाव्या बाजूच्या टॅबमधून **Endpoints** निवडा.

1. नेव्हिगेशन मेनूमधून **Real-time endpoints** निवडा.

    ![एंडपॉइंट तयार करा.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.mr.png)

1. **Create** निवडा.

1. तुम्ही तयार केलेले नोंदणीकृत मॉडेल निवडा.

    ![नोंदणीकृत मॉडेल निवडा.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.mr.png)

1. **Select** निवडा.

1. खालील गोष्टी करा:

    - **Virtual machine** *Standard_NC6s_v3* ला निवडा.
    - तुम्हाला हवा असलेला **Instance count** निवडा. उदाहरणार्थ, *1*.
    - **Endpoint** **New** वर सेट करा.
    - **Endpoint name** प्रविष्ट करा. हे अद्वितीय असले पाहिजे.
    - **Deployment name** प्रविष्ट करा. हे अद्वितीय असले पाहिजे.

    ![डिप्लॉयमेंट सेटिंग भरा.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.mr.png)

1. **Deploy** निवडा.

> [!WARNING]
> तुमच्या खात्यावर अतिरिक्त शुल्क टाळण्यासाठी, Azure Machine Learning workspace मध्ये तयार केलेले एंडपॉइंट हटवण्याची खात्री करा.
>

#### Azure Machine Learning Workspace मध्ये डिप्लॉयमेंट स्थिती तपासा

1. तुम्ही तयार केलेल्या Azure Machine Learning workspace वर जा.

1. डाव्या बाजूच्या टॅबमधून **Endpoints** निवडा.

1. तुम्ही तयार केलेले एंडपॉइंट निवडा.

    ![एंडपॉइंट निवडा.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.mr.png)

1. या पृष्ठावर, तुम्ही डिप्लॉयमेंट प्रक्रियेदरम्यान एंडपॉइंट्स व्यवस्थापित करू शकता.

> [!NOTE]
> डिप्लॉयमेंट पूर्ण झाल्यानंतर, **Live traffic** **100%** वर सेट असल्याची खात्री करा. जर तसे नसेल, तर ट्रॅफिक सेटिंग समायोजित करण्यासाठी **Update traffic** निवडा. जर ट्रॅफिक 0% वर सेट असेल तर तुम्ही मॉडेलची चाचणी करू शकत नाही.
>
> ![ट्रॅफिक सेट करा.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.mr.png)
>

## प्रसंग 3: Prompt flow सह एकत्रित करा आणि Azure AI Foundry मध्ये तुमच्या कस्टम मॉडेलसह चॅट करा

### कस्टम Phi-3 मॉडेल Prompt flow सह एकत्रित करा

तुमचे फाइन-ट्यून केलेले मॉडेल यशस्वीरित्या डिप्लॉय केल्यानंतर, तुम्ही ते Prompt flow सह एकत्रित करू शकता जेणेकरून तुमचे मॉडेल रिअल-टाइम ऍप्लिकेशन्समध्ये वापरता येईल. यामुळे तुमच्या कस्टम Phi-3 मॉडेलसह विविध परस्परसंवादी कार्ये सक्षम होतात.

या व्यायामामध्ये, तुम्ही:

- Azure AI Foundry Hub तयार करा.
- Azure AI Foundry Project तयार करा.
- Prompt flow तयार करा.
- फाइन-ट्यून केलेल्या Phi-3 मॉडेलसाठी कस्टम कनेक्शन जोडा.
- Prompt flow सेट करा जेणेकरून तुमच्या कस्टम Phi-3 मॉडेलसह चॅट करता येईल.

> [!NOTE]
> तुम्ही Azure ML Studio वापरून देखील Prompt flow सह एकत्रित करू शकता. एकाच प्रकारची एकत्रीकरण प्रक्रिया Azure ML Studio वर लागू केली जाऊ शकते.

#### Azure AI Foundry Hub तयार करा

प्रोजेक्ट तयार करण्यापूर्वी तुम्हाला Hub तयार करणे आवश्यक आहे. Hub हे Resource Group सारखे कार्य करते, ज्यामुळे तुम्हाला Azure AI Foundry मध्ये एकाधिक प्रोजेक्ट्सचे आयोजन आणि व्यवस्थापन करता येते.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) ला भेट द्या.

1. डाव्या बाजूच्या टॅबमधून **All hubs** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New hub** निवडा.

    ![Hub तयार करा.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.mr.png)

1. खालील गोष्टी करा:

    - **Hub name** प्रविष्ट करा. हे अद्वितीय असले पाहिजे.
    - तुमचे Azure **Subscription** निवडा.
    - वापरण्यासाठी **Resource group** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - तुम्हाला हवी असलेली **Location** निवडा.
    - वापरण्यासाठी **Connect Azure AI Services** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - **Connect Azure AI Search** **Skip connecting** ला निवडा.

    ![Hub भरा.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.mr.png)

1. **Next** निवडा.

#### Azure AI Foundry Project तयार करा

1. तुम्ही तयार केलेल्या Hub मध्ये, डाव्या बाजूच्या टॅबमधून **All projects** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New project** निवडा.

    ![नवीन प्रोजेक्ट निवडा.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.mr.png)

1. **Project name** प्रविष्ट करा. हे अद्वितीय असले पाहिजे.

    ![प्रोजेक्ट तयार करा.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.mr.png)

1. **Create a project** निवडा.

#### फाइन-ट्यून केलेल्या Phi-3 मॉडेलसाठी कस्टम कनेक्शन जोडा

तुमच्या कस्टम Phi-3 मॉडेलला Prompt flow सह एकत्रित करण्यासाठी, तुम्हाला मॉडेलचा एंडपॉइंट आणि की कस्टम कनेक्शनमध्ये जतन करावी लागेल. ही सेटअप सुनिश्चित करते की तुमच्या कस्टम Phi-3 मॉडेलला Prompt flow मध्ये प्रवेश मिळेल.

#### फाइन-ट्यून केलेल्या Phi-3 मॉडेलचा API की आणि एंडपॉइंट URI सेट करा

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) ला भेट द्या.

1. तुम्ही तयार केलेल्या Azure Machine Learning workspace वर जा.

1. डाव्या बाजूच्या टॅबमधून **Endpoints** निवडा.

    ![Endpoints निवडा.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.mr.png)

1. तुम्ही तयार केलेले एंडपॉइंट निवडा.

    ![Endpoints निवडा.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.mr.png)

1. नेव्हिगेशन मेनूमधून **Consume** निवडा.

1. तुमचा **REST endpoint** आणि **Primary key** कॉपी करा.
![एपीआय की आणि एंडपॉइंट युरी कॉपी करा.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.mr.png)

#### कस्टम कनेक्शन जोडा

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) ला भेट द्या.

1. तुम्ही तयार केलेल्या Azure AI Foundry प्रकल्पावर जा.

1. तयार केलेल्या प्रकल्पात, डाव्या बाजूच्या टॅबमधून **Settings** निवडा.

1. **+ New connection** निवडा.

    ![नवीन कनेक्शन निवडा.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.mr.png)

1. नेव्हिगेशन मेनूमधून **Custom keys** निवडा.

    ![कस्टम कीज निवडा.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.mr.png)

1. खालील टास्क पूर्ण करा:

    - **+ Add key value pairs** निवडा.
    - कीचे नाव **endpoint** असे टाका आणि Azure ML Studio मधून कॉपी केलेला एंडपॉइंट व्हॅल्यू फील्डमध्ये पेस्ट करा.
    - पुन्हा **+ Add key value pairs** निवडा.
    - कीचे नाव **key** असे टाका आणि Azure ML Studio मधून कॉपी केलेली की व्हॅल्यू फील्डमध्ये पेस्ट करा.
    - कीज जोडल्यानंतर, **is secret** निवडा, जेणेकरून की उघड होणार नाही.

    ![कनेक्शन जोडा.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.mr.png)

1. **Add connection** निवडा.

#### Prompt flow तयार करा

तुम्ही Azure AI Foundry मध्ये कस्टम कनेक्शन जोडले आहे. आता, खालील पायऱ्या वापरून एक Prompt flow तयार करूया. त्यानंतर, तुम्ही हा Prompt flow कस्टम कनेक्शनशी कनेक्ट कराल, जेणेकरून तुम्ही Prompt flow मध्ये fine-tuned मॉडेल वापरू शकाल.

1. तुम्ही तयार केलेल्या Azure AI Foundry प्रकल्पावर जा.

1. डाव्या बाजूच्या टॅबमधून **Prompt flow** निवडा.

1. नेव्हिगेशन मेनूमधून **+ Create** निवडा.

    ![Promptflow निवडा.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.mr.png)

1. नेव्हिगेशन मेनूमधून **Chat flow** निवडा.

    ![चॅट फ्लो निवडा.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.mr.png)

1. वापरण्यासाठी **Folder name** भरा.

    ![नाव प्रविष्ट करा.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.mr.png)

2. **Create** निवडा.

#### कस्टम Phi-3 मॉडेलसह चॅट करण्यासाठी Prompt flow सेट करा

तुम्हाला fine-tuned Phi-3 मॉडेल Prompt flow मध्ये समाकलित करायचे आहे. मात्र, विद्यमान Prompt flow यासाठी डिझाइन केलेले नाही. त्यामुळे, तुम्हाला कस्टम मॉडेलच्या एकत्रीकरणासाठी Prompt flow पुन्हा डिझाइन करावे लागेल.

1. Prompt flow मध्ये, विद्यमान फ्लो पुन्हा तयार करण्यासाठी खालील टास्क पूर्ण करा:

    - **Raw file mode** निवडा.
    - *flow.dag.yml* फाईलमधील सर्व विद्यमान कोड हटवा.
    - खालील कोड *flow.dag.yml* फाईलमध्ये जोडा.

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

    - **Save** निवडा.

    ![Raw file mode निवडा.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.mr.png)

1. Prompt flow मध्ये कस्टम Phi-3 मॉडेल वापरण्यासाठी खालील कोड *integrate_with_promptflow.py* फाईलमध्ये जोडा.

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

    ![Prompt flow कोड पेस्ट करा.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.mr.png)

> [!NOTE]
> Azure AI Foundry मध्ये Prompt flow कसे वापरायचे याबद्दल अधिक तपशीलवार माहिती [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) येथे मिळवू शकता.

1. तुमच्या मॉडेलसह चॅट करण्यासाठी **Chat input**, **Chat output** निवडा.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.mr.png)

1. आता तुम्ही तुमच्या कस्टम Phi-3 मॉडेलसह चॅट करण्यास तयार आहात. पुढील व्यायामात, तुम्हाला Prompt flow सुरू करण्यासाठी आणि तुमच्या fine-tuned Phi-3 मॉडेलसह चॅट कसे करायचे हे शिकवले जाईल.

> [!NOTE]
>
> पुन्हा तयार केलेला फ्लो खालील प्रतिमेसारखा दिसायला हवा:
>
> ![फ्लो उदाहरण.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.mr.png)
>

### तुमच्या कस्टम Phi-3 मॉडेलसह चॅट करा

आता तुम्ही तुमचे कस्टम Phi-3 मॉडेल fine-tune करून Prompt flow सह एकत्रित केले आहे, त्यामुळे तुम्ही त्याच्यासोबत संवाद साधण्यास तयार आहात. या व्यायामामध्ये तुम्हाला तुमच्या मॉडेलसह चॅट सुरू करण्यासाठी आणि सेट करण्याच्या प्रक्रियेचे मार्गदर्शन केले जाईल. या पायऱ्या पूर्ण करून, तुम्ही तुमच्या fine-tuned Phi-3 मॉडेलच्या क्षमतांचा विविध कार्ये आणि संभाषणांसाठी पूर्णपणे उपयोग करू शकता.

- Prompt flow वापरून तुमच्या कस्टम Phi-3 मॉडेलसह चॅट करा.

#### Prompt flow सुरू करा

1. Prompt flow सुरू करण्यासाठी **Start compute sessions** निवडा.

    ![कंप्युट सेशन सुरू करा.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.mr.png)

1. पॅरामीटर्स रिन्यू करण्यासाठी **Validate and parse input** निवडा.

    ![इनपुट सत्यापित करा.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.mr.png)

1. तुम्ही तयार केलेल्या कस्टम कनेक्शनसाठी **connection** चा **Value** निवडा. उदाहरणार्थ, *connection*.

    ![कनेक्शन.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.mr.png)

#### तुमच्या कस्टम मॉडेलसह चॅट करा

1. **Chat** निवडा.

    ![चॅट निवडा.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.mr.png)

1. खालीलप्रमाणे परिणामाचा एक उदाहरण: आता तुम्ही तुमच्या कस्टम Phi-3 मॉडेलसह चॅट करू शकता. fine-tuning साठी वापरलेल्या डेटाच्या आधारावर प्रश्न विचारण्याची शिफारस केली जाते.

    ![Prompt flow सह चॅट करा.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.mr.png)

**अस्वीकरण**:  
हा दस्तऐवज मशीन-आधारित एआय अनुवाद सेवांचा वापर करून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज अधिकृत स्रोत मानावा. महत्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.