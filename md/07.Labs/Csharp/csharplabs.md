## Welcome to the Phi-3 labs using C#. 

There is a selection of labs that showcases how to integrate the powerful different versions of Phi-3 models in a .NET environment.

## Prerequisites
Before running the sample, ensure you have the following installed:

**.NET 8:** Make sure you have the [latest version of .NET](https://dotnet.microsoft.com/download/dotnet/8.0?WT.mc_id=aiml-137032-kinfeylo) installed on your machine.

**(Optional) Visual Studio or Visual Studio Code:** You will need an IDE or code editor capable of running .NET projects. [Visual Studio](https://visualstudio.microsoft.com/) or [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) are recommended.

**Using git** clone locally one of the available Phi-3 versions from [Hugging Face](https://huggingface.co).

**Download the phi3-mini-4k-instruct-onnx model** to your local machine:

### navigate to the folder to store the models

```bash
cd c:\phi3\models
```

### add support for lfs

```bash
git lfs install 
```

### clone and download mini 4K instruct model

Choose between Phi-3 or Phi-3.5, or download both.

```bash
# Phi-3
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

# Phi-3.5
# git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx
```

### clone and download vision 128K model

Choose between Phi-3 or Phi-3.5, or download both.

```bash
# Phi-3
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu

# Phi-3.5
# git clone https://huggingface.co/microsoft/Phi-3.5-vision-instruct-onnx
```

**Important:** The current demos are designed to use the ONNX versions of the model. The previous steps clone the following models.

![OnnxDownload](../../../imgs/07/00/DownloadOnnx.png)

## About the Labs

The main solution have several sample Labs that demonstrates the capabilities of the Phi-3 models using C#.

| Project | Description | Location |
| ------------ | ----------- | -------- |
| LabsPhi301    | This is a sample project that uses a local phi3 model to ask a question. The project load a local ONNX Phi-3 model using the `Microsoft.ML.OnnxRuntime` libraries. | .\src\LabsPhi301\ |
| LabsPhi302    | This is a sample project that implement a Console chat using Semantic Kernel. | .\src\LabsPhi302\ |
| LabsPhi303 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. | .\src\LabsPhi303\ |
| LabsPhi304 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | .\src\LabsPhi304\ |
| LabsPhi305 | This is a sample project that uses a the Phi-3 hosted in ollama model to answer a question.  |**coming soon**|
| LabsPhi306 | This is a sample project that implement a Console chat using Semantic Kernel. |**coming soon**|
| LabsPhi307  | This is a sample project that implement a RAG using local embeddings and Semantic Kernel. |**coming soon**|


## How to Run the Projects

To run the projects, follow these steps:
1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi301`.
    ```bash
    cd .\src\LabsPhi301\
    ```

1. Run the project with the command
    ```bash
    dotnet run
    ```

1.  The sample project ask for a user input and replies using the local mode. 

    The running demo is similar to this one:

    ![Chat running demo](../../../imgs/07/00/SampleConsole.gif)

    ***Note:** there is a typo in the 1st question, Phi-3 is cool enough to share the correct answer!*

1.  The project `LabsPhi304` ask for the user to select different options, and then process the request. In example, analyzing a local image.

    The running demo is similar to this one:

    ![Image Analysis running demo](../../../imgs/07/00/SampleVisionConsole.gif)
    
