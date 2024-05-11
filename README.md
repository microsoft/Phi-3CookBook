# Welcome to Microsoft Phi-3 Cookbook

This is a manual on how to use the Microsoft Phi-3 family. 

Phi-3, a family of open AI models developed by Microsoft. Phi-3 models are the most capable and cost-effective small language models (SLMs) available, outperforming models of the same size and next size up across a variety of language, reasoning, coding, and math benchmarks. 

Phi-3-mini, a 3.8B language model is available on [Microsoft Azure AI Studio](https://aka.ms/phi3-azure-ai), [Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3), and [Ollama](https://ollama.com/library/phi3). Phi-3 models significantly outperform language models of the same and larger sizes on key benchmarks (see benchmark numbers below, higher is better). Phi-3-mini does better than models twice its size, and Phi-3-small and Phi-3-medium outperform much larger models, including GPT-3.5T.  

All reported numbers are produced with the same pipeline to ensure that the numbers are comparable. As a result, these numbers may differ from other published numbers due to slight differences in the evaluation methodology. More details on benchmarks are provided in our technical paper. 

![phimodel](https://github.com/microsoft/Phi-3CookBook/assets/2511341/8bb25dfc-616d-44c2-940a-d0e2f0b8c41d)

Note: Phi-3 models do not perform as well on factual knowledge benchmarks (such as TriviaQA) as the smaller model size results in less capacity to retain facts. 

You can learn how to use Microsoft Phi-3 and how to build E2E solutions in your different hardware devices. To experience Phi-3 for yourself, start with playing with the model on [Azure AI Playground](https://aka.ms/try-phi3). You can also find the model on the [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct). Start building with and customizing Phi-3 for your scenarios using the [Azure AI Studio](https://aka.ms/phi3-azure-ai). 

This content includes:

## **Microsoft Phi-3 Cookbook**

* [Introduction]()
    * [Welcome to the Phi-3 Family](./md/01.Introduce/Phi3Family.md)(✅)
* [Quick Start]()
    * [Using Phi-3 in Hugging face](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
    * [Using Phi-3 in Azure AI Studio](./md/02.QuickStart/AzureAIStudio_QuickStart.md)
    * [Using Phi-3 in Ollama](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
    * [Using Phi-3 in LM Studio](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
* [Inference Phi-3](./md/03.Inference/overview.md)  
    * [Inference Phi-3 in iOS](./md/03.Inference/iOS_Inference.md)
    * [Inference Phi-3 in Android](./md/03.Inference/Android_Inference.md)
    * [Inference Phi-3 in Jetson](./md/03.Inference/Jetson_Inference.md)
    * [Inference Phi-3 in AIPC](./md/03.Inference/AIPC_Inference.md)
    * [Inference Phi-3 in Local Server](./md/03.Inference/Local_Server_Inference.md)
* [Fine-tuning Phi-3]()
    * [Import Data for Phi-3](./md/04.Fine-tuning/Import_Data.md)
    * [Introduce Azure Machine Learning Service](./md/04.Fine-tuning/Introduce_AzureML.md)
    * [Introduce Microsoft Olive](./md/04.Fine-tuning/Introduce_Mirosoft_Olive.md)
    * [Fine-tuning Phi-3 Guideline](./md/04.Fine-tuning/FineTuning_Guideline.md)
* [Evaluation Phi-3]()
    * [Introduce Responsible AI](./md/05.Evaluation/ResponsibleAI.md)
    * [Introduce Promptflow](./md/05.Evaluation/Promptflow.md)
    * [Using Azure AI Studio to evluation](./md/05.Evaluation/AzureAIStudio.md)
* [E2E Solution]()
    * [.NET MAUI Samples](./md/06.Samples/dotNETMAUI_samples.md)
    * [Azure AI Studio Samples](./md/06.Samples/AzureAIStudio_samples.md)
    * [Semantic Kernel RAG Samples](./md/06.Samples/SemanticKernel_RAG_samples.md)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
