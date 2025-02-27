# Using Windows GPU to create Prompt flow solution with Phi-3.5-Instruct ONNX 

The following document is an example of how to use PromptFlow with ONNX (Open Neural Network Exchange) for developing AI applications based on Phi-3 models.

PromptFlow is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based (Large Language Model) AI applications, from ideation and prototyping to testing and evaluation.

By integrating PromptFlow with ONNX, developers can:

- Optimize Model Performance: Leverage ONNX for efficient model inference and deployment.
- Simplify Development: Use PromptFlow to manage the workflow and automate repetitive tasks.
- Enhance Collaboration: Facilitate better collaboration among team members by providing a unified development environment.

**Prompt flow** is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications, from ideation, prototyping, testing, evaluation to production deployment and monitoring. It makes prompt engineering much easier and enables you to build LLM apps with production quality.

Prompt flow can connect to OpenAI, Azure OpenAI Service, and customizable models (Huggingface, local LLM/SLM). We hope to deploy Phi-3.5's quantized ONNX model to local applications. Prompt flow can help us better plan our business and complete local solutions based on Phi-3.5. In this example, we will combine ONNX Runtime GenAI Library to complete the Prompt flow solution based on Windows GPU.

## **Installation**

### **ONNX Runtime GenAI for Windows GPU**

Read this guideline to set ONNX Runtime GenAI for Windows GPU  [click here](./ORTWindowGPUGuideline.md)

### **Set up Prompt flow in VSCode**

1. Install Prompt flow VS Code Extension

![pfvscode](../../../../imgs/02/pfonnx/pfvscode.png)

2. After install Prompt flow VS Code Extension， click the extension，and choose **Installation dependencies** follow this guideline to install Prompt flow SDK in your env

![pfsetup](../../../../imgs/02/pfonnx/pfsetup.png)

3. Download [Sample Code](../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf/) and use VS Code to open this sample

![pfsample](../../../../imgs/02/pfonnx/pfsample.png)

4. Open **flow.dag.yaml** to choose your Python env

![pfdag](../../../../imgs/02/pfonnx/pfdag.png)

   Open **chat_phi3_ort.py** to change your Phi-3.5-instruct ONNX Model location

![pfphi](../../../../imgs/02/pfonnx/pfphi.png)

5. Run your prompt flow to testing

Open **flow.dag.yaml** click visual editor

![pfv](../../../../imgs/02/pfonnx/pfv.png)

after click this,and run it to test

![pfflow](../../../../imgs/02/pfonnx/pfflow.png)

1. You can run batch in terminal to check more result


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

You can check results in your default browser


![pfresult](../../../../imgs/02/pfonnx/pfresult.png)





















