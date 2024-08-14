Using [LiteLLM](https://docs.litellm.ai/) for the Phi-3 model can be a great choice, especially if you're looking to integrate it into various applications. LiteLLM acts as a middleware that translates API calls into requests compatible with different models, including Phi-3.

Phi-3 is a small language model (SLM) developed by Microsoft, designed to be efficient and capable of running on resource-constrained machines. It can operate on CPUs with AVX support and as little as 4 GB of RAM, making it a good option for local inference without needing GPUs.

Here are some steps to get started with LiteLLM for Phi-3:

1. **Install LiteLLM**: You can install LiteLLM using pip:
   ```bash
   pip install litellm
   ```

2. **Set Up Environment Variables**: Configure your API keys and other necessary environment variables.
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. **Make API Calls**: Use LiteLLM to make API calls to the Phi-3 model.
   ```python
   from litellm import completion

   response = completion(
       model="phi-3",
       messages=[{"role": "user", "content": "Hello, how are you?"}]
   )
   print(response)
   ```

4. **Integration**: You can integrate LiteLLM with various platforms like Nextcloud Assistant, allowing you to use Phi-3 for text generation and other task.

**Full Code Sample for LLMLite**
[Sample Code Notebook for LLMLite](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/litellm.ipynb)