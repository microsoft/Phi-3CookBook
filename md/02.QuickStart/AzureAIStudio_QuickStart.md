# **Using Phi-3 in Azure AI Studio**

With the development of Generative AI, we hope to use a unified platform to manage different LLM and SLM, enterprise data integration, fine-tuning/RAG operations, and the evaluation of different enterprise businesses after integrating LLM and SLM, etc., so that generative AI can Smart applications are better implemented. Azure AI Studio is an enterprise-level generative AI application platform.

![aistudo](../../imgs/02/AIStudio/ai-studio-home.png)

With Azure AI Studio, you can evaluate large language model (LLM) responses and orchestrate prompt application components with prompt flow for better performance. The platform facilitates scalability for transforming proof of concepts into full-fledged production with ease. Continuous monitoring and refinement support long-term success.

We can quickly deploy the Phi-3 model on Azure AI Studio through simple steps, and then use Azure AI Studio to complete Phi-3 related Playground/Chat, Fine-tuning, evaluation and other related work.

## **1. Preparation**

Create Azure AI Studio on Azure Portal

![portal](../../imgs/02/AIStudio/ai-studio-portal.png)

After completing the naming of the studio and setting the region, you can create it


![settings](../../imgs/02/AIStudio/ai-studio-settings.png)

After successful creation, you can access the studio you created through [ai.azure.com](https://ai.azure.com/)

![page](../../imgs/02/AIStudio/ai-studio-page.png)

There can be multiple projects on one AI Studio. Create a project in AI Studio to prepare.

![proj](../../imgs/02/AIStudio/ai-studio-proj.png)


## **2. Deploy Phi-3 in Azure AI Studio**

Click the Explore option of the project to enter the Model Catalog and select Phi-3

![model](../../imgs/02/AIStudio/ai-studio-model.png)

Select Phi-3-mini-4k-instruct

![phi3](../../imgs/02/AIStudio/ai-studio-phi3.png)

Click 'Deploy' to deploy the Phi-3-mini-4k-instruct model

***Note***:  You can select computing power when deploying


## **3. Chat Phi-3 in Azure AI Studio**

Go to the deployment page, select Playground, and chat with Phi-3 of Azure AI Studio


![chat](../../imgs/02/AIStudio/ai-studio-chat.png)

hen deploying


## **3. Using Phi-3 API in Azure AI Studio**

You can access https://{Your project name}.swedencentral.inference.ml.azure.com/swagger.json through Postman GET and combine it with Key to learn about the provided interfaces


![swagger](../../imgs/02/AIStudio/ai-studio-swagger.png)


such as access score api 


![score](../../imgs/02/AIStudio/ai-studio-score.png)

You can get the request parameters very conveniently, as well as the response parameters. This is Postman result

![result](../../imgs/02/AIStudio/ai-studio-result.png)























