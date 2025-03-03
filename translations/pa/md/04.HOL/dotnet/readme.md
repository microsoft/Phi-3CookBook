## ਫਾਈ ਲੈਬਜ਼ ਵਿੱਚ C# ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਸੁਆਗਤ ਹੈ

ਇਹ ਲੈਬਜ਼ ਦੀ ਇੱਕ ਚੋਣ ਹੈ ਜੋ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ .NET ਮਾਹੌਲ ਵਿੱਚ ਤਾਕਤਵਰ ਅਤੇ ਵੱਖ-ਵੱਖ ਵਰਜਨਾਂ ਵਾਲੇ ਫਾਈ ਮਾਡਲਜ਼ ਨੂੰ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਪਹਿਲਾਂ ਦੀਆਂ ਲੋੜਾਂ

ਸੈਂਪਲ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠ ਲਿਖੇ ਤੌਰ 'ਤੇ ਇੰਸਟਾਲ ਹਨ:

**.NET 9:** ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੰਪਿਊਟਰ 'ਤੇ [.NET ਦਾ ਨਵਾਂ ਵਰਜਨ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ਇੰਸਟਾਲ ਹੈ।

**(ਵਿਕਲਪਿਕ) Visual Studio ਜਾਂ Visual Studio Code:** ਤੁਹਾਨੂੰ ਇੱਕ IDE ਜਾਂ ਕੋਡ ਐਡੀਟਰ ਦੀ ਲੋੜ ਹੋਵੇਗੀ ਜੋ .NET ਪ੍ਰੋਜੈਕਟਾਂ ਨੂੰ ਚਲਾ ਸਕੇ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ਜਾਂ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

**Git ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) ਤੋਂ ਫਾਈ-3, ਫਾਈ-3.5 ਜਾਂ ਫਾਈ-4 ਦੇ ਕਿਸੇ ਵੀ ਉਪਲਬਧ ਵਰਜਨ ਨੂੰ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ ਕਲੋਨ ਕਰੋ।

**Phi-4 ONNX ਮਾਡਲਜ਼ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ** ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ:

### ਮਾਡਲ ਸਟੋਰ ਕਰਨ ਲਈ ਫੋਲਡਰ 'ਤੇ ਜਾਓ

```bash
cd c:\phi\models
```

### lfs ਲਈ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕਰੋ

```bash
git lfs install 
```

### Phi-4 ਮਿਨੀ ਇੰਸਟਰੱਕਟ ਮਾਡਲ ਅਤੇ Phi-4 ਮਲਟੀ ਮੋਡਲ ਮਾਡਲ ਕਲੋਨ ਅਤੇ ਡਾਊਨਲੋਡ ਕਰੋ

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX ਮਾਡਲਜ਼ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ** ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ:

### Phi-3 ਮਿਨੀ 4K ਇੰਸਟਰੱਕਟ ਮਾਡਲ ਅਤੇ Phi-3 ਵਿਜ਼ਨ 128K ਮਾਡਲ ਕਲੋਨ ਅਤੇ ਡਾਊਨਲੋਡ ਕਰੋ

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**ਮਹੱਤਵਪੂਰਨ:** ਮੌਜੂਦਾ ਡੈਮੋ ONNX ਵਰਜਨਾਂ ਵਾਲੇ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤੇ ਗਏ ਹਨ। ਉਪਰੋਕਤ ਕਦਮ ਹੇਠ ਲਿਖੇ ਮਾਡਲ ਕਲੋਨ ਕਰਦੇ ਹਨ।

## ਲੈਬਜ਼ ਬਾਰੇ

ਮੁੱਖ ਸਾਲਿਊਸ਼ਨ ਵਿੱਚ ਕਈ ਸੈਂਪਲ ਲੈਬਜ਼ ਹਨ ਜੋ C# ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਫਾਈ ਮਾਡਲਜ਼ ਦੀ ਸਮਰੱਥਾਵਾਂ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰਦੇ ਹਨ।

| ਪ੍ਰੋਜੈਕਟ | ਮਾਡਲ | ਵੇਰਵਾ |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ਜਾਂ Phi-3.5 | ਇੱਕ ਸਧਾਰਣ ਕੰਸੋਲ ਚੈਟ ਸੈਂਪਲ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ ਇੱਕ ਲੋਕਲ ONNX Phi-3 ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ ਜਿਸਦੀ ਵਰਤੋਂ `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡ ਨਾਲ ਚਲਾਓ

    ```bash
    dotnet run
    ```

1. ਸੈਂਪਲ ਪ੍ਰੋਜੈਕਟ ਯੂਜ਼ਰ ਇੰਪੁੱਟ ਮੰਗਦਾ ਹੈ ਅਤੇ ਲੋਕਲ ਮੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

   ਚੱਲ ਰਹੇ ਡੈਮੋ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖਦੇ ਹਨ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਆਟੋਮੇਟਡ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।