## Üdvözlünk a Phi laborokban C# használatával

Ez a laborok válogatása bemutatja, hogyan integrálhatók a Phi modellek különböző verziói egy .NET környezetben.

## Előfeltételek

A példa futtatása előtt győződj meg róla, hogy a következő elemek telepítve vannak:

**.NET 9:** Győződj meg róla, hogy a [legújabb .NET verzió](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) telepítve van a gépeden.

**(Opcionális) Visual Studio vagy Visual Studio Code:** Szükséged lesz egy IDE-re vagy kódszerkesztőre, amely képes .NET projekteket futtatni. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) vagy [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ajánlott.

**Git használata:** Klónozd helyileg a Phi-3, Phi-3.5 vagy Phi-4 elérhető verzióinak egyikét a [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) oldaláról.

**Phi-4 ONNX modellek letöltése** a helyi gépedre:

### navigálj a modellek tárolására szánt mappába

```bash
cd c:\phi\models
```

### lfs támogatás hozzáadása

```bash
git lfs install 
```

### klónozd és töltsd le a Phi-4 mini instruct modellt és a Phi-4 multimodális modellt

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX modellek letöltése** a helyi gépedre:

### klónozd és töltsd le a Phi-3 mini 4K instruct modellt és a Phi-3 vision 128K modellt

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Fontos:** Az aktuális demók az ONNX verziójú modellek használatára vannak tervezve. Az előző lépések során a következő modellek kerülnek klónozásra.

## A laborokról

A fő megoldás több mintalabort tartalmaz, amelyek bemutatják a Phi modellek képességeit C# használatával.

| Projekt | Modell | Leírás |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 vagy Phi-3.5 | Egy mintakonzolos csevegés, amely lehetővé teszi a felhasználó számára, hogy kérdéseket tegyen fel. A projekt egy helyi ONNX Phi-3 modellt tölt be a `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Futtasd a projektet a következő paranccsal:

    ```bash
    dotnet run
    ```

1. A mintaprojekt felhasználói bemenetet kér, majd válaszol a helyi mód használatával.

   A futó demo hasonló ehhez:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Felelősségkizárás**:  
Ezt a dokumentumot gépi AI fordítási szolgáltatásokkal fordították le. Bár igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.