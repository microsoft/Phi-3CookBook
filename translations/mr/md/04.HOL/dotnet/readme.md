## Phi Labs मध्ये C# वापरून आपले स्वागत आहे

.NET वातावरणात विविध Phi मॉडेल्सच्या सामर्थ्यशाली आवृत्त्या एकत्रित कशा करायच्या याचे प्रात्यक्षिक देणाऱ्या काही प्रयोगशाळा येथे उपलब्ध आहेत.

## पूर्वतयारी

नमुना चालवण्यापूर्वी, तुमच्याकडे खालील गोष्टी असल्याची खात्री करा:

**.NET 9:** तुमच्या मशीनवर [NET ची नवीनतम आवृत्ती](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) स्थापित आहे याची खात्री करा.

**(पर्यायी) Visual Studio किंवा Visual Studio Code:** तुम्हाला .NET प्रकल्प चालवण्यासाठी सक्षम असलेले IDE किंवा कोड संपादक आवश्यक असेल. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) किंवा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) यांची शिफारस केली जाते.

**git वापरून** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) वरून उपलब्ध Phi-3, Phi3.5 किंवा Phi-4 आवृत्त्यांपैकी एक आवृत्ती स्थानिक स्तरावर क्लोन करा.

**Phi-4 ONNX मॉडेल्स डाउनलोड करा** तुमच्या स्थानिक मशीनवर:

### मॉडेल्स साठवण्यासाठी फोल्डरवर जा

```bash
cd c:\phi\models
```

### lfs साठी सपोर्ट जोडा

```bash
git lfs install 
```

### Phi-4 mini instruct मॉडेल आणि Phi-4 multi modal मॉडेल क्लोन करा आणि डाउनलोड करा

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मॉडेल्स डाउनलोड करा** तुमच्या स्थानिक मशीनवर:

### Phi-3 mini 4K instruct मॉडेल आणि Phi-3 vision 128K मॉडेल क्लोन करा आणि डाउनलोड करा

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्त्वाचे:** सध्याचे डेमो ONNX आवृत्त्यांचा वापर करण्यासाठी डिझाइन केलेले आहेत. वरील पायऱ्या खालील मॉडेल्स क्लोन करतात.

## प्रयोगशाळांबद्दल

मुख्य सोल्यूशनमध्ये Phi मॉडेल्सच्या क्षमतांचे प्रात्यक्षिक देणाऱ्या C# वापरून तयार केलेल्या अनेक नमुना प्रयोगशाळांचा समावेश आहे.

| प्रकल्प | मॉडेल | वर्णन |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 किंवा Phi-3.5 | नमुना कन्सोल चॅट जे वापरकर्त्याला प्रश्न विचारण्याची परवानगी देते. प्रकल्प स्थानिक ONNX Phi-3 मॉडेल लोड करतो `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. खालील आदेशाने प्रकल्प चालवा:

    ```bash
    dotnet run
    ```

1. नमुना प्रकल्प वापरकर्त्याच्या इनपुटची विचारणा करतो आणि स्थानिक मोड वापरून प्रतिसाद देतो.

   चालणारे डेमो यासारखे आहे:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकृती**:  
हे दस्तऐवज मशीन-आधारित AI भाषांतर सेवा वापरून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा प्राधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराचा सल्ला घेतला जावा. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.