The [Azure AI Model Inference is an API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo) that exposes a common set of capabilities for foundational models and that can be used by developers to consume predictions from a diverse set of models in a uniform and consistent way. Developers can talk with different models deployed in Azure AI Studio without changing the underlying code they are using.

Microsoft now has its own SDK for AI Model inference, for different models hosted on [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo). 

Python and JS versions are out. C# will be released next. 

For [Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo).  [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

For [JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

The SDK uses the [REST API documented here](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo).

## Availability
The Azure AI Model Inference API is available in the following Phi-3 models:

- Models deployed to serverless API endpoints:
- Models deployed to managed inference:


The API is compatible with Azure OpenAI model deployments.
**Note**  The Azure AI model inference API is available in managed inference (Managed Online Endpoints) for models deployed after June 24th, 2024. To take advance of the API, redeploy your endpoint if the model has been deployed before such date.

## Capabilities
The following section describes some of the capabilities the API exposes. For a full specification of the API, view the reference section.

### Modalities
The API indicates how developers can consume predictions for the following modalities:

- Get info: Returns the information about the model deployed under the endpoint.
- Text embeddings: Creates an embedding vector representing the input text.
- Text completions: Creates a completion for the provided prompt and parameters.
- Chat completions: Creates a model response for the given chat conversation.
- Image embeddings: Creates an embedding vector representing the input text and image.
