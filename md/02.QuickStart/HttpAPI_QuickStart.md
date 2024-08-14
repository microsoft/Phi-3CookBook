# Use Azure API with Phi-3

This notebook shows examples of how to use Phi-3 APIs offered by Microsoft Azure AI and Azure ML. We will cover:  
* HTTP requests API usage for Phi-3 pretrained and chat models in CLI
* HTTP requests API usage for Phi-3 pretrained and chat models in Python

Sure, here's an overview of **HTTP Requests API Usage in CLI**:

## HTTP Requests API Usage in CLI

### Basics

For using the REST API, you will need to have an Endpoint URL and an Authentication Key associated with that endpoint. These can be acquired from previous steps.

In this chat completion example, we use a simple `curl` call for illustration. There are three major components:

1. **The `host-url`**: This is your endpoint URL with the chat completion schema `/v1/chat/completions`.
2. **The `headers`**: This defines the content type as well as your API key.
3. **The `payload` or `data`**: This includes your prompt details and model hyperparameters.

### Example

Here’s an example of how to make a chat completion request using `curl`:

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "max_tokens": 50
}'
```

### Breakdown

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY` with your actual API key.
- **Payload**: Customize the payload as per your requirements, including different prompts, models, and parameters.

See Sample [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

Review the [documentation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-Phi-3) for the Phi-3 family of models at for AI Studio and for ML Studio for details on how to provision inference endpoints, regional availability, pricing and inference schema reference.