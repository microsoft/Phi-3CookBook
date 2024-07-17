The [Azure AI Model Inference is an API](https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo) that exposes a common set of capabilities for foundational models and that can be used by developers to consume predictions from a diverse set of models in a uniform and consistent way. Developers can talk with different models deployed in Azure AI Studio without changing the underlying code they are using.

Microsoft now has its own SDK for AI Model inference, for different models hosted on MaaS/MaaP. Python and JS versions are out. C# will be released next. 
For [Python](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo). 
The SDK uses the [REST API documented here]:(https://learn.microsoft.com/en-us/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo).

## Benefits
Foundational models, such as language models, have indeed made remarkable strides in recent years. These advancements have revolutionized various fields, including natural language processing and computer vision, and they have enabled applications like chatbots, virtual assistants, and language translation services.

While foundational models excel in specific domains, they lack a uniform set of capabilities. Some models are better at specific task and even across the same task, some models may approach the problem in one way while others in another. Developers can benefit from this diversity by using the right model for the right job allowing them to:

- Improve the performance in a specific downstream task.
- Use more efficient models for simpler tasks.
- Use smaller models that can run faster on specific tasks.
- Compose multiple models to develop intelligent experiences.
- Having a uniform way to consume foundational models allow developers to realize all those benefits without sacrificing portability or changing the underlying code.

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
