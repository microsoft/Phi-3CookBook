## Karibu kwenye maabara ya Phi ukitumia C#

Kuna uteuzi wa maabara unaoonyesha jinsi ya kuunganisha matoleo tofauti yenye nguvu ya mifano ya Phi katika mazingira ya .NET.

## Mahitaji ya Awali

Kabla ya kuendesha sampuli, hakikisha una vitu vifuatavyo vimewekwa:

**.NET 9:** Hakikisha una [toleo jipya zaidi la .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) lililowekwa kwenye kompyuta yako.

**(Hiari) Visual Studio au Visual Studio Code:** Utahitaji IDE au mhariri wa msimbo unaoweza kuendesha miradi ya .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) au [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) vinapendekezwa.

**Kutumia git** kloni kwa ndani moja ya matoleo yanayopatikana ya Phi-3, Phi3.5 au Phi-4 kutoka [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Pakua mifano ya Phi-4 ONNX** kwenye kompyuta yako:

### nenda kwenye folda ya kuhifadhi mifano

```bash
cd c:\phi\models
```

### ongeza msaada kwa lfs

```bash
git lfs install 
```

### kloni na pakua mfano wa Phi-4 mini instruct na mfano wa Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Pakua mifano ya Phi-3 ONNX** kwenye kompyuta yako:

### kloni na pakua mfano wa Phi-3 mini 4K instruct na mfano wa Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Muhimu:** Maonyesho ya sasa yameundwa kutumia matoleo ya ONNX ya mfano. Hatua za awali zinakloni mifano ifuatayo.

## Kuhusu Maabara

Suluhisho kuu lina maabara kadhaa ya sampuli zinazoonyesha uwezo wa mifano ya Phi ukitumia C#.

| Mradi | Mfano | Maelezo |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 au Phi-3.5 | Sampuli ya mazungumzo ya console inayoruhusu mtumiaji kuuliza maswali. Mradi unapakua mfano wa Phi-3 wa ndani wa ONNX ukitumia `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Endesha mradi kwa amri

    ```bash
    dotnet run
    ```

1. Mradi wa sampuli utaomba maoni ya mtumiaji na kujibu ukitumia hali ya ndani. 

   Maonyesho yanayoendeshwa yanafanana na haya:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za kiakili za mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.