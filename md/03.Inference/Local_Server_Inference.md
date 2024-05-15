# **Inference Phi-3 in Local Server**

We can deploy Phi-3 on a local server. Users can choose Ollama or LM Studio solutions, or they can write their own code. You can connect Phi-3's local services through Semantic Kernel or Langchain to build Copilot applications


## **Use Semantic Kernel to access phi3-mini**

In the Copilot application, we create applications through Semantic Kernel / LangChain. This type of application framework is generally compatible with Azure OpenAI Service / OpenAI models, and can also support open source models on Hugging face and local models. What should we do if we want to use Semantic Kernel to access phi3-mini? Using .NET as an example, we can combine it with the Hugging face Connector in  Semantic Kernel. By default, it can correspond to the model id on Hugging face (the first time you use it, the model will be downloaded from Hugging face, which takes a long time). You can also connect to the built local service. Compared with the two, I recommend using the latter because it has a higher degree of autonomy, especially in enterprise applications.

![sk](../../imgs/03/LocalServer/sk.png)


From the figure accessing local services through Semantic Kernel can easily connect to the self-built phi3-mini model server. Here is the running result


![skrun](../../imgs/03/LocalServer/skrun.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

