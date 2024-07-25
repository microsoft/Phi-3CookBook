# **Using Phi-3 in Azure AI Studio**

With the development of Generative AI, we hope to use a unified platform to manage different LLM and SLM, enterprise data integration, fine-tuning/RAG operations, and the evaluation of different enterprise businesses after integrating LLM and SLM, etc., so that generative AI can Smart applications are better implemented. [Azure AI Studio](https://ai.azure.com) is an enterprise-level generative AI application platform.

![aistudo](../../imgs/02/AIStudio/ai-studio-home.png)

With Azure AI Studio, you can evaluate large language model (LLM) responses and orchestrate prompt application components with prompt flow for better performance. The platform facilitates scalability for transforming proof of concepts into full-fledged production with ease. Continuous monitoring and refinement support long-term success.

We can quickly deploy the Phi-3 model on Azure AI Studio through simple steps, and then use Azure AI Studio to complete Phi-3 related Playground/Chat, Fine-tuning, evaluation and other related work.

## **1. Preparation**

## [AZD AI Studio Starter Template](https://azure.github.io/awesome-azd/?name=AI+Studio)

### Azure AI Studio Starter

This is Bicep template that deploys everything you need to get started with Azure AI Studio. Includes AI Hub with dependent resources, AI project, AI Services and an online endpoint

### Quick Use

If you already have the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) installed on your machine, using this template is as simple as running this command in a new directory.

### Terminal Command

```bash
azd init -t azd-aistudio-starter
```

Or
If using the azd VS Code extension you can paste this URL in the VS Code command terminal.

### Terminal URL

```bash
azd-aistudio-starter
```

## Manual Creation

Create Azure AI Studio on [Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo)

![portal](../../imgs/02/AIStudio/ai-studio-portal.png)

After completing the naming of the studio and setting the region, you can create it

![settings](../../imgs/02/AIStudio/ai-studio-settings.png)

After successful creation, you can access the studio you created through [ai.azure.com](https://ai.azure.com/)

![page](../../imgs/02/AIStudio/ai-studio-page.png)

There can be multiple projects on one AI Studio. Create a project in AI Studio to prepare.

![proj](../../imgs/02/AIStudio/ai-studio-proj.png)

## **2. Deploy the Phi-3 model in Azure AI Studio**

Click the Explore option of the project to enter the Model Catalog and select Phi-3

![model](../../imgs/02/AIStudio/ai-studio-model.png)

Select Phi-3-mini-4k-instruct

![phi3](../../imgs/02/AIStudio/ai-studio-phi3.png)

Click 'Deploy' to deploy the Phi-3-mini-4k-instruct model

> [!NOTE]
>
> You can select computing power when deploying

## **3. Playground Chat Phi-3 in Azure AI Studio**

Go to the deployment page, select Playground, and chat with Phi-3 of Azure AI Studio

![chat](../../imgs/02/AIStudio/ai-studio-chat.png)

## **4. Deploying the Model from Azure AI Studio**

To deploy a model from the Azure Model Catalog, you can follow these steps:

- Sign in to Azure AI Studio.
- Choose the model you want to deploy from the Azure AI Studio model catalog.
- On the model's Details page, select Deploy and then select Serverless API with Azure AI Content Safety.
- Select the project in which you want to deploy your models. To use the Serverless API offering, your workspace must belong to the East US 2 or Sweden Central region. You can customize the Deployment name.
- On the deployment wizard, select the Pricing and terms to learn about the pricing and terms of use.
- Select Deploy. Wait until the deployment is ready and you're redirected to the Deployments page.
- Select Open in playground to start interacting with the model.
- You can return to the Deployments page, select the deployment, and note the endpoint's Target URL and the Secret Key, which you can use to call the deployment and generate completions.
- You can always find the endpoint's details, URL, and access keys by navigating to the Build tab and selecting Deployments from the Components section.

> [!NOTE]
> Please note that your account must have the Azure AI Developer role permissions on the Resource Group to perform these steps.

## **5. Using Phi-3 API in Azure AI Studio**

You can access https://{Your project name}.region.inference.ml.azure.com/swagger.json through Postman GET and combine it with Key to learn about the provided interfaces

![swagger](../../imgs/02/AIStudio/ai-studio-swagger.png)

such as access score api 

![score](../../imgs/02/AIStudio/ai-studio-score.png)

You can get the request parameters very conveniently, as well as the response parameters. This is Postman result

![result](../../imgs/02/AIStudio/ai-studio-result.png)
