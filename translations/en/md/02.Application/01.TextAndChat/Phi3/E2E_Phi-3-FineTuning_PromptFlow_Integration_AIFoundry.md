# Fine-tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry

This end-to-end (E2E) sample is based on the guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community. It covers the processes of fine-tuning, deploying, and integrating custom Phi-3 models with Prompt Flow in Azure AI Foundry.  
Unlike the E2E sample, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", which required running code locally, this tutorial focuses entirely on fine-tuning and integrating your model within the Azure AI / ML Studio.

## Overview

In this E2E sample, you'll learn how to fine-tune the Phi-3 model and integrate it with Prompt Flow in Azure AI Foundry. By leveraging Azure AI / ML Studio, you'll establish a workflow for deploying and utilizing custom AI models. This E2E sample is divided into three scenarios:

**Scenario 1: Set up Azure resources and Prepare for fine-tuning**  
**Scenario 2: Fine-tune the Phi-3 model and Deploy in Azure Machine Learning Studio**  
**Scenario 3: Integrate with Prompt Flow and Chat with your custom model in Azure AI Foundry**

Here’s an overview of this E2E sample.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.en.png)

### Table of Contents

1. **[Scenario 1: Set up Azure resources and Prepare for fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Create an Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Request GPU quotas in Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Add role assignment](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Set up project](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Prepare dataset for fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Fine-tune the Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Deploy the fine-tuned Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrate with Prompt Flow and Chat with your custom model in Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Integrate the custom Phi-3 model with Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Chat with your custom Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Set up Azure resources and Prepare for fine-tuning

### Create an Azure Machine Learning Workspace

1. Type *azure machine learning* in the **search bar** at the top of the portal page and select **Azure Machine Learning** from the options that appear.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.en.png)

2. Select **+ Create** from the navigation menu.

3. Select **New workspace** from the navigation menu.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.en.png)

4. Perform the following tasks:  

    - Select your Azure **Subscription**.  
    - Select the **Resource group** to use (create a new one if needed).  
    - Enter **Workspace Name**. It must be a unique value.  
    - Select the **Region** you'd like to use.  
    - Select the **Storage account** to use (create a new one if needed).  
    - Select the **Key vault** to use (create a new one if needed).  
    - Select the **Application insights** to use (create a new one if needed).  
    - Select the **Container registry** to use (create a new one if needed).  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.en.png)

5. Select **Review + Create**.

6. Select **Create**.

### Request GPU quotas in Azure Subscription

In this tutorial, you'll fine-tune and deploy a Phi-3 model using GPUs. For fine-tuning, you'll use the *Standard_NC24ads_A100_v4* GPU, which requires a quota request. For deployment, you'll use the *Standard_NC6s_v3* GPU, which also requires a quota request.

> [!NOTE]  
> Only Pay-As-You-Go subscriptions (the standard subscription type) are eligible for GPU allocation; benefit subscriptions are not currently supported.

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Perform the following tasks to request *Standard NCADSA100v4 Family* quota:

    - Select **Quota** from the left-side tab.  
    - Select the **Virtual machine family** to use. For example, select **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC24ads_A100_v4* GPU.  
    - Select **Request quota** from the navigation menu.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.en.png)

    - Inside the Request quota page, enter the **New cores limit** you'd like to use. For example, 24.  
    - Inside the Request quota page, select **Submit** to request the GPU quota.

1. Perform the following tasks to request *Standard NCSv3 Family* quota:

    - Select **Quota** from the left-side tab.  
    - Select the **Virtual machine family** to use. For example, select **Standard NCSv3 Family Cluster Dedicated vCPUs**, which includes the *Standard_NC6s_v3* GPU.  
    - Select **Request quota** from the navigation menu.  
    - Inside the Request quota page, enter the **New cores limit** you'd like to use. For example, 24.  
    - Inside the Request quota page, select **Submit** to request the GPU quota.

### Add role assignment

To fine-tune and deploy your models, you must first create a User Assigned Managed Identity (UAI) and assign it the appropriate permissions. This UAI will be used for authentication during deployment.

#### Create User Assigned Managed Identity (UAI)

1. Type *managed identities* in the **search bar** at the top of the portal page and select **Managed Identities** from the options that appear.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.en.png)

1. Select **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.en.png)

1. Perform the following tasks:  

    - Select your Azure **Subscription**.  
    - Select the **Resource group** to use (create a new one if needed).  
    - Select the **Region** you'd like to use.  
    - Enter the **Name**. It must be a unique value.  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.en.png)

1. Select **Review + create**.

1. Select **+ Create**.

#### Add Contributor role assignment to Managed Identity

1. Navigate to the Managed Identity resource that you created.

1. Select **Azure role assignments** from the left-side tab.

1. Select **+ Add role assignment** from the navigation menu.

1. Inside Add role assignment page, perform the following tasks:  
    - Select the **Scope** to **Resource group**.  
    - Select your Azure **Subscription**.  
    - Select the **Resource group** to use.  
    - Select the **Role** to **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.en.png)

2. Select **Save**.

#### Add Storage Blob Data Reader role assignment to Managed Identity

1. Type *storage accounts* in the **search bar** at the top of the portal page and select **Storage accounts** from the options that appear.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.en.png)

1. Select the storage account associated with the Azure Machine Learning workspace that you created. For example, *finetunephistorage*.

1. Perform the following tasks to navigate to the Add role assignment page:

    - Navigate to the Azure Storage account that you created.  
    - Select **Access Control (IAM)** from the left-side tab.  
    - Select **+ Add** from the navigation menu.  
    - Select **Add role assignment** from the navigation menu.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.en.png)

1. Inside Add role assignment page, perform the following tasks:  

    - Inside the Role page, type *Storage Blob Data Reader* in the **search bar** and select **Storage Blob Data Reader** from the options that appear.  
    - Inside the Role page, select **Next**.  
    - Inside the Members page, select **Assign access to** **Managed identity**.  
    - Inside the Members page, select **+ Select members**.  
    - Inside Select managed identities page, select your Azure **Subscription**.  
    - Inside Select managed identities page, select the **Managed identity** to **Manage Identity**.  
    - Inside Select managed identities page, select the Managed Identity that you created. For example, *finetunephi-managedidentity*.  
    - Inside Select managed identities page, select **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.en.png)

1. Select **Review + assign**.

#### Add AcrPull role assignment to Managed Identity

1. Type *container registries* in the **search bar** at the top of the portal page and select **Container registries** from the options that appear.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.en.png)

1. Select the container registry associated with the Azure Machine Learning workspace. For example, *finetunephicontainerregistry*.

1. Perform the following tasks to navigate to the Add role assignment page:

    - Select **Access Control (IAM)** from the left-side tab.  
    - Select **+ Add** from the navigation menu.  
    - Select **Add role assignment** from the navigation menu.

1. Inside Add role assignment page, perform the following tasks:

    - Inside the Role page, type *AcrPull* in the **search bar** and select **AcrPull** from the options that appear.  
    - Inside the Role page, select **Next**.  
    - Inside the Members page, select **Assign access to** **Managed identity**.  
    - Inside the Members page, select **+ Select members**.  
    - Inside Select managed identities page, select your Azure **Subscription**.  
    - Inside Select managed identities page, select the **Managed identity** to **Manage Identity**.  
    - Inside Select managed identities page, select the Managed Identity that you created. For example, *finetunephi-managedidentity*.  
    - Inside Select managed identities page, select **Select**.  
    - Select **Review + assign**.

### Set up project

To download the datasets needed for fine-tuning, you'll set up a local environment.

In this exercise, you will:

- Create a folder to work inside it.  
- Create a virtual environment.  
- Install the required packages.  
- Create a *download_dataset.py* file to download the dataset.

#### Create a folder to work inside it

1. Open a terminal window and type the following command to create a folder named *finetune-phi* in the default path.

    ```console
    mkdir finetune-phi
    ```

2. Type the following command inside your terminal to navigate to the *finetune-phi* folder you created.

    ```console
    cd finetune-phi
    ```

#### Create a virtual environment

1. Type the following command inside your terminal to create a virtual environment named *.venv*.

    ```console
    python -m venv .venv
    ```

2. Type the following command inside your terminal to activate the virtual environment.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> If it worked, you should see *(.venv)* before the command prompt.

#### Install the required packages

1. Type the following commands inside your terminal to install the required packages.

    ```console
    pip install datasets==2.19.1
    ```

#### Create `download_dataset.py`

> [!NOTE]  
> Complete folder structure:  
>  
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Open **Visual Studio Code**.

1. Select **File** from the menu bar.

1. Select **Open Folder**.

1. Select the *finetune-phi* folder that you created, located at *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.en.png)

1. In the left pane of Visual Studio Code, right-click and select **New File** to create a new file named *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.en.png)

### Prepare dataset for fine-tuning

In this exercise, you'll run the *download_dataset.py* file to download the *ultrachat_200k* datasets to your local environment. You'll then use these datasets to fine-tune the Phi-3 model in Azure Machine Learning.

In this exercise, you will:

- Add code to the *download_dataset.py* file to download the datasets.  
- Run the *download_dataset.py* file to download datasets to your local environment.

#### Download your dataset using *download_dataset.py*

1. Open the *download_dataset.py* file in Visual Studio Code.

1. Add the following code into the *download_dataset.py* file.

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

1. Type the following command inside your terminal to run the script and download the dataset to your local environment.

    ```console
    python download_dataset.py
    ```

1. Verify that the datasets were saved successfully to your local *finetune-phi/data* directory.

> [!NOTE]  
> #### Note on dataset size and fine-tuning time  
> In this tutorial, you use only 1% of the dataset (`split='train[:1%]'`). This significantly reduces the amount of data, speeding up both the upload and fine-tuning processes. You can adjust the percentage to find the right balance between training time and model performance. Using a smaller subset of the dataset reduces the time required for fine-tuning, making the process more manageable for a tutorial.

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Fine-tune the Phi-3 model

In this exercise, you'll fine-tune the Phi-3 model in Azure Machine Learning Studio.

In this exercise, you will:

- Create a compute cluster for fine-tuning.  
- Fine-tune the Phi-3 model in Azure Machine Learning Studio.  

#### Create a compute cluster for fine-tuning
1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select **Compute** from the left-hand menu.

1. Click on **Compute clusters** in the navigation menu.

1. Click **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.en.png)

1. Complete the following steps:

    - Choose the **Region** you want to use.
    - Set the **Virtual machine tier** to **Dedicated**.
    - Set the **Virtual machine type** to **GPU**.
    - Apply the **Virtual machine size** filter to **Select from all options**.
    - Choose **Standard_NC24ads_A100_v4** for the **Virtual machine size**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.en.png)

1. Click **Next**.

1. Complete the following steps:

    - Enter a unique **Compute name**.
    - Set the **Minimum number of nodes** to **0**.
    - Set the **Maximum number of nodes** to **1**.
    - Set the **Idle seconds before scale down** to **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.en.png)

1. Click **Create**.

#### Fine-tune the Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select the Azure Machine Learning workspace you created.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.en.png)

1. Complete the following steps:

    - Click on **Model catalog** in the left-hand menu.
    - Enter *phi-3-mini-4k* in the **search bar** and select **Phi-3-mini-4k-instruct** from the search results.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.en.png)

1. Click **Fine-tune** in the navigation menu.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.en.png)

1. Complete the following steps:

    - Set **Select task type** to **Chat completion**.
    - Click **+ Select data** to upload your **Training data**.
    - Set the Validation data upload type to **Provide different validation data**.
    - Click **+ Select data** to upload your **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.en.png)

    > [!TIP]
    >
    > You can access **Advanced settings** to adjust configurations like **learning_rate** and **lr_scheduler_type** for optimizing the fine-tuning process to suit your requirements.

1. Click **Finish**.

1. Congratulations! You have successfully fine-tuned the Phi-3 model using Azure Machine Learning. Please note that the fine-tuning process may take some time. Once the job starts, you will need to wait for it to complete. You can monitor its progress in the Jobs tab within your Azure Machine Learning Workspace. In the next steps, you will deploy the fine-tuned model and integrate it with Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.en.png)

### Deploy the fine-tuned Phi-3 model

To integrate the fine-tuned Phi-3 model with Prompt flow, the model must be deployed for real-time inference. This process includes registering the model, creating an online endpoint, and deploying it.

In this exercise, you will:

- Register the fine-tuned model in your Azure Machine Learning workspace.
- Create an online endpoint.
- Deploy the fine-tuned Phi-3 model.

#### Register the fine-tuned model

1. Visit [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Select the Azure Machine Learning workspace you created.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.en.png)

1. Click **Models** in the left-hand menu.
1. Click **+ Register**.
1. Choose **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.en.png)

1. Select the job you created.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.en.png)

1. Click **Next**.

1. Set **Model type** to **MLflow**.

1. Ensure **Job output** is selected (this should be automatically selected).

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.en.png)

2. Click **Next**.

3. Click **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.en.png)

4. You can view your registered model by navigating to the **Models** section in the left-hand menu.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.en.png)

#### Deploy the fine-tuned model

1. Navigate to the Azure Machine Learning workspace you created.

1. Click **Endpoints** in the left-hand menu.

1. Choose **Real-time endpoints** from the navigation menu.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.en.png)

1. Click **Create**.

1. Select the registered model you created.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.en.png)

1. Click **Select**.

1. Complete the following steps:

    - Set **Virtual machine** to *Standard_NC6s_v3*.
    - Choose the **Instance count** (e.g., *1*).
    - Set the **Endpoint** to **New** to create a new endpoint.
    - Enter a unique **Endpoint name**.
    - Enter a unique **Deployment name**.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.en.png)

1. Click **Deploy**.

> [!WARNING]
> To prevent unnecessary charges, ensure you delete the created endpoint in your Azure Machine Learning workspace after completing your tasks.

#### Check deployment status in Azure Machine Learning Workspace

1. Navigate to the Azure Machine Learning workspace you created.

1. Click **Endpoints** in the left-hand menu.

1. Select the endpoint you created.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.en.png)

1. On this page, you can manage the endpoint during the deployment process.

> [!NOTE]
> After deployment is complete, ensure **Live traffic** is set to **100%**. If not, click **Update traffic** to adjust the traffic settings. Note that the model cannot be tested if the traffic is set to 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.en.png)
>

## Scenario 3: Integrate with Prompt flow and Chat with your custom model in Azure AI Foundry

### Integrate the custom Phi-3 model with Prompt flow

Once your fine-tuned model is deployed, you can integrate it with Prompt Flow to use it in real-time applications, enabling interactive tasks with your custom Phi-3 model.

In this exercise, you will:

- Create an Azure AI Foundry Hub.
- Create an Azure AI Foundry Project.
- Create a Prompt flow.
- Add a custom connection for the fine-tuned Phi-3 model.
- Set up Prompt flow to interact with your custom Phi-3 model.

> [!NOTE]
> You can also integrate Prompt Flow directly using Azure ML Studio. The process is the same.

#### Create Azure AI Foundry Hub

Before creating a Project, you need to create a Hub. A Hub functions like a Resource Group, helping you organize and manage multiple Projects within Azure AI Foundry.

1. Visit [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Click **All hubs** in the left-hand menu.

1. Click **+ New hub** in the navigation menu.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.en.png)

1. Complete the following steps:

    - Enter a unique **Hub name**.
    - Select your Azure **Subscription**.
    - Choose a **Resource group** (or create a new one if necessary).
    - Select the **Location** you want to use.
    - Choose the **Connect Azure AI Services** option (or create a new one if necessary).
    - Set **Connect Azure AI Search** to **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.en.png)

1. Click **Next**.

#### Create Azure AI Foundry Project

1. In the Hub you created, click **All projects** in the left-hand menu.

1. Click **+ New project** in the navigation menu.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.en.png)

1. Enter a unique **Project name**.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.en.png)

1. Click **Create a project**.

#### Add a custom connection for the fine-tuned Phi-3 model

To integrate your custom Phi-3 model with Prompt flow, you need to save the model's endpoint and key as a custom connection. This will allow access to your model in Prompt flow.

#### Set API key and endpoint URI of the fine-tuned Phi-3 model

1. Visit [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigate to the Azure Machine Learning workspace you created.

1. Click **Endpoints** in the left-hand menu.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.en.png)

1. Select the endpoint you created.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.en.png)

1. Click **Consume** in the navigation menu.

1. Copy your **REST endpoint** and **Primary key**.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.en.png)

#### Add the Custom Connection

1. Go to [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Open the Azure AI Foundry project you created.

1. In the project, select **Settings** from the left-hand menu.

1. Click on **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.en.png)

1. From the navigation menu, choose **Custom keys**.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.en.png)

1. Complete the following steps:

    - Click **+ Add key value pairs**.
    - For the key name, type **endpoint** and paste the endpoint copied from Azure ML Studio into the value field.
    - Click **+ Add key value pairs** again.
    - For the key name, type **key** and paste the key copied from Azure ML Studio into the value field.
    - After adding the keys, enable **is secret** to keep the key hidden.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.en.png)

1. Click **Add connection**.

#### Create Prompt flow

You’ve successfully added a custom connection in Azure AI Foundry. Now, let’s create a Prompt flow. Afterward, you’ll link this Prompt flow to the custom connection, allowing you to use the fine-tuned model within the Prompt flow.

1. Open the Azure AI Foundry project you created.

1. From the left-hand menu, select **Prompt flow**.

1. Click **+ Create** from the navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.en.png)

1. Choose **Chat flow** from the navigation menu.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.en.png)

1. Enter a **Folder name**.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.en.png)

2. Click **Create**.

#### Set up Prompt flow to chat with your custom Phi-3 model

To integrate the fine-tuned Phi-3 model into a Prompt flow, you’ll need to modify the existing Prompt flow. The current setup isn’t designed for this purpose, so you’ll have to rebuild it.

1. In the Prompt flow, follow these steps to rebuild the flow:

    - Switch to **Raw file mode**.
    - Delete all existing code in the *flow.dag.yml* file.
    - Insert the following code into the *flow.dag.yml* file:

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

    - Click **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.en.png)

1. Add the following code to the *integrate_with_promptflow.py* file to enable the use of the custom Phi-3 model in Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.en.png)

> [!NOTE]
> For detailed guidance on using Prompt flow in Azure AI Foundry, refer to [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Enable **Chat input** and **Chat output** to interact with your model.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.en.png)

1. You’re now ready to chat with your custom Phi-3 model. In the next exercise, you’ll learn how to start Prompt flow and use it to interact with your fine-tuned Phi-3 model.

> [!NOTE]
>
> The redesigned flow should look like the image below:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.en.png)
>

### Chat with your custom Phi-3 model

Now that your custom Phi-3 model is fine-tuned and integrated with Prompt flow, you’re ready to start interacting with it. This exercise will walk you through setting up and initiating a chat with your model using Prompt flow. Follow these steps to fully leverage your fine-tuned Phi-3 model for various tasks and conversations.

- Use Prompt flow to chat with your custom Phi-3 model.

#### Start Prompt flow

1. Click **Start compute sessions** to launch Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.en.png)

1. Select **Validate and parse input** to refresh parameters.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.en.png)

1. Choose the **Value** of the **connection** corresponding to the custom connection you created, such as *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.en.png)

#### Chat with your custom model

1. Click **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.en.png)

1. Example result: You can now chat with your custom Phi-3 model. It’s recommended to ask questions relevant to the data used for fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.en.png)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.