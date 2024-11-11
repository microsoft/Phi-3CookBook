## Run the Phi Family model in Python For other samples see https://github.com/marketplace/models

Below are example code snippets for a few use cases. For additional information about Azure AI Inference SDK, see [full documentation](https://aka.ms/azsdk/azure-ai-inference/python/reference) and [samples](https://aka.ms/azsdk/azure-ai-inference/python/samples).

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings if your using GitHub Marketplace models (https://github.com/marketplace/models). 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# Create a .env file with GitHub_token for your GitHub Personal Token or Azure Key

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="Can you explain the basics of machine learning?"),
    ],
    # Simply change the model name for the appropiate model "Phi-3.5-mini-instruct" or "Phi-3.5-vision-instruct"
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
