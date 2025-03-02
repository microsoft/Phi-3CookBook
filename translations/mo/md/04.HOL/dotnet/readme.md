## Phi लैब्समा स्वागत छ, C# को प्रयोग गर्दै

यहाँ केही लैब्स छन् जसले .NET वातावरणमा विभिन्न शक्तिशाली Phi मोडेलहरूको एकीकरण कसरी गर्न सकिन्छ भन्ने देखाउँछ।

## आवश्यकताहरू

नमूना चलाउनु अघि, सुनिश्चित गर्नुहोस् कि तपाईंसँग निम्न चीजहरू स्थापना गरिएको छ:

**.NET 9:** आफ्नो मेसिनमा [नवीनतम संस्करणको .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) स्थापना गर्नुहोस्।

**(वैकल्पिक) Visual Studio वा Visual Studio Code:** तपाईंसँग .NET प्रोजेक्ट चलाउन सक्षम एक IDE वा कोड सम्पादक हुन आवश्यक छ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) वा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) सिफारिस गरिन्छ।

**git प्रयोग गर्दै** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) बाट उपलब्ध Phi-3, Phi3.5 वा Phi-4 संस्करणहरू मध्ये कुनै एकलाई स्थानीय रूपमा क्लोन गर्नुहोस्।

**Phi-4 ONNX मोडेलहरू डाउनलोड गर्नुहोस्** आफ्नो स्थानीय मेसिनमा:

### मोडेलहरू भण्डारण गर्न फोल्डरमा जानुहोस्

```bash
cd c:\phi\models
```

### lfs को लागि समर्थन थप्नुहोस्

```bash
git lfs install 
```

### Phi-4 मिनी इन्स्ट्रक्ट मोडेल र Phi-4 मल्टिमोडल मोडेल क्लोन र डाउनलोड गर्नुहोस्

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मोडेलहरू डाउनलोड गर्नुहोस्** आफ्नो स्थानीय मेसिनमा:

### Phi-3 मिनी 4K इन्स्ट्रक्ट मोडेल र Phi-3 भिजन 128K मोडेल क्लोन र डाउनलोड गर्नुहोस्

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वपूर्ण:** हालका डेमोहरू मोडेलको ONNX संस्करणहरू प्रयोग गर्न डिजाइन गरिएका छन्। माथिका चरणहरूले निम्न मोडेलहरू क्लोन गर्छन्।

## लैब्सको बारेमा

मुख्य समाधानमा विभिन्न नमूना लैब्स छन् जसले C# प्रयोग गरेर Phi मोडेलहरूको क्षमताहरू प्रदर्शन गर्छ।

| प्रोजेक्ट | मोडेल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 वा Phi-3.5 | एउटा नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। यो प्रोजेक्टले स्थानीय ONNX Phi-3 मोडेल लोड गर्दछ `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` प्रयोग गरेर।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. प्रोजेक्टलाई निम्न कमाण्डको साथ चलाउनुहोस्

    ```bash
    dotnet run
    ```

1. नमूना प्रोजेक्टले प्रयोगकर्ताको इनपुट सोध्छ र स्थानीय मोडेल प्रयोग गरेर प्रतिक्रिया दिन्छ।

   चलिरहेको डेमो यस प्रकारको हुन्छ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

It seems like you are requesting a translation into "mo." Could you please clarify what "mo" refers to? Are you referring to a specific language, such as Maori, Mongolian, or something else? Providing more context will help me assist you better!