## Phi प्रयोगशालाहरूमा स्वागत छ, C# प्रयोग गर्दै

यहाँ विभिन्न Phi मोडेलहरूलाई .NET वातावरणमा कसरी एकीकृत गर्ने भनेर देखाउने केही प्रयोगशालाहरूको चयन गरिएको छ।

## आवश्यकताहरू

नमूना चलाउनु अघि, निम्न चीजहरू स्थापना गरिएको सुनिश्चित गर्नुहोस्:

**.NET 9:** तपाईंको मेसिनमा [नवीनतम संस्करणको .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) स्थापना गरिएको छ भनेर सुनिश्चित गर्नुहोस्।

**(वैकल्पिक) Visual Studio वा Visual Studio Code:** तपाईंलाई .NET प्रोजेक्टहरू चलाउन सक्षम हुने कुनै IDE वा कोड सम्पादक आवश्यक हुनेछ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) वा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) सिफारिस गरिन्छ।

**git प्रयोग गरेर** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) बाट उपलब्ध Phi-3, Phi3.5 वा Phi-4 भर्सनहरू मध्ये कुनै एकलाई स्थानीय रूपमा क्लोन गर्नुहोस्।

**Phi-4 ONNX मोडेलहरू डाउनलोड गर्नुहोस्** तपाईंको स्थानीय मेसिनमा:

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

**Phi-3 ONNX मोडेलहरू डाउनलोड गर्नुहोस्** तपाईंको स्थानीय मेसिनमा:

### Phi-3 मिनी 4K इन्स्ट्रक्ट मोडेल र Phi-3 भिजन 128K मोडेल क्लोन र डाउनलोड गर्नुहोस्

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वपूर्ण:** हालका डेमोहरू मोडेलको ONNX संस्करणहरू प्रयोग गर्न डिजाइन गरिएका छन्। माथिका चरणहरूले निम्न मोडेलहरू क्लोन गर्छन्।

## प्रयोगशालाहरूको बारेमा

मुख्य समाधानमा Phi मोडेलहरूको क्षमताहरू C# प्रयोग गरेर प्रदर्शन गर्ने धेरै नमूना प्रयोगशालाहरू छन्।

| प्रोजेक्ट | मोडेल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 वा Phi-3.5 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। यो प्रोजेक्टले `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` प्रयोग गर्दै स्थानीय ONNX Phi-3 मोडेल लोड गर्छ।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. यो प्रोजेक्ट निम्न आदेश प्रयोग गरेर चलाउनुहोस्

    ```bash
    dotnet run
    ```

1. नमूना प्रोजेक्टले प्रयोगकर्ताको इनपुट माग्छ र स्थानीय मोड प्रयोग गरेर जवाफ दिन्छ।

   चलिरहेको डेमो यस्तो देखिन्छ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
यो दस्तावेज मेशिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव सही अनुवाद प्रदान गर्न प्रयास गर्छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा असत्यताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेजलाई प्रामाणिक स्रोत मान्नुपर्छ। महत्त्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यो अनुवाद प्रयोग गर्दा उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।