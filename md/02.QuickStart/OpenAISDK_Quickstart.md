# Use OpenAI SDK with Phi-3 in Azure AI and Azure ML

Use `openai` SDK to consume Phi-3 deployments in Azure AI and Azure ML. The Phi-3 family of models in Azure AI and Azure ML offers an API compatible with the OpenAI Chat Completion API. It allows customers and users to transition seamlessly from OpenAI models to Phi-3 LLMs. 

The API can be directly used with OpenAI's client libraries or third-party tools, like LangChain or LlamaIndex.

The example below shows how to make this transition using the OpenAI Python Library. Notice that Phi-3 supports only chat completions API.

To use the Phi-3 model with the OpenAI SDK, you'll need to follow a few steps to set up your environment and make API calls. Here's a guide to help you get started:

1. **Install the OpenAI SDK**: First, you'll need to install the OpenAI Python package if you haven't already.
   ```bash
   pip install openai
   ```

2. **Set Up Your API Key**: Make sure you have your OpenAI API key. You can set it up in your environment variables or directly in your code.
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **Make API Calls**: Use the OpenAI SDK to interact with the Phi-3 model. Here's an example of how to make a completion request:
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **Handle Responses**: Process the responses from the model as needed for your application.

Here's a more detailed example:
```python
import openai

# Set your API key
openai.api_key = "your-api-key"

# Define the prompt
prompt = "Write a short story about a brave knight."

# Make the API call
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Print the response
print(response.choices[0].text.strip())
```

This will generate a short story based on the prompt provided. You can adjust the `max_tokens` parameter to control the length of the output.

[See A complete Notebook Sample for Phi-3 Models](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

Review the [documentation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-phi3) for the Phi-3 family of models at for AI Studio and for ML Studio for details on how to provision inference endpoints, regional availability, pricing and inference schema reference.