## Welcome to the Phi labs using C#

There is a selection of labs that showcases how to integrate the powerful different versions of Phi models in a .NET environment.

## Prerequisites

Before running the sample, ensure you have the following installed:

**.NET 9:** Make sure you have the [latest version of .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installed on your machine.

**(Optional) Visual Studio or Visual Studio Code:** You will need an IDE or code editor capable of running .NET projects. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) or [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) are recommended.

**Using git** clone locally one of the available Phi-3, Phi3.5 or Phi-4 versions from [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Download Phi-4 ONNX models** to your local machine:

### navigate to the folder to store the models

```bash
cd c:\phi\models
```

### add support for lfs

```bash
git lfs install 
```

### clone and download Phi-4 mini instruct model and the Phi-4 multi modal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download the Phi-3 ONNX models** to your local machine:

### clone and download Phi-3 mini 4K instruct model and Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Important:** The current demos are designed to use the ONNX versions of the model. The previous steps clone the following models.

## About the Labs

The main solution have several sample Labs that demonstrates the capabilities of the Phi models using C#.

| Project | Model | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](./src/LabsPhi301/) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](./src/LabsPhi302/) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](./src/LabsPhi303/) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](./src/LabsPhi304/) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](./src/LabsPhi4-Chat-01OnnxRuntime/) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](./src/LabsPhi4-Chat-02SK/) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [Phi-4multimodal-vision](./src/LabsPhi4-MultiModal-01Images/) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](./src/LabsPhi4-MultiModal-02Audio/) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Run the project with the command

    ```bash
    dotnet run
    ```

1. The sample project ask for a user input and replies using the local mode. 

   The running demo is similar to this one:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```
