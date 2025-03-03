# Använda Windows GPU för att skapa en Prompt flow-lösning med Phi-3.5-Instruct ONNX

Detta dokument är ett exempel på hur man använder PromptFlow med ONNX (Open Neural Network Exchange) för att utveckla AI-applikationer baserade på Phi-3-modeller.

PromptFlow är en uppsättning utvecklingsverktyg som är utformade för att effektivisera hela utvecklingscykeln för AI-applikationer baserade på stora språkmodeller (LLM), från idé och prototyp till testning och utvärdering.

Genom att integrera PromptFlow med ONNX kan utvecklare:

- **Optimera modellprestanda**: Dra nytta av ONNX för effektiv modellinferens och distribution.
- **Förenkla utveckling**: Använd PromptFlow för att hantera arbetsflödet och automatisera repetitiva uppgifter.
- **Förbättra samarbete**: Underlätta bättre samarbete mellan teammedlemmar genom att tillhandahålla en enhetlig utvecklingsmiljö.

**Prompt flow** är en uppsättning utvecklingsverktyg som är utformade för att effektivisera hela utvecklingscykeln för AI-applikationer baserade på stora språkmodeller (LLM), från idé, prototyp, testning och utvärdering till produktionsdistribution och övervakning. Det gör prompt engineering mycket enklare och gör det möjligt att bygga LLM-applikationer med produktionskvalitet.

Prompt flow kan ansluta till OpenAI, Azure OpenAI Service och anpassningsbara modeller (Huggingface, lokala LLM/SLM). Vi hoppas kunna distribuera Phi-3.5:s kvantiserade ONNX-modell till lokala applikationer. Prompt flow kan hjälpa oss att bättre planera vår verksamhet och skapa lokala lösningar baserade på Phi-3.5. I detta exempel kommer vi att kombinera ONNX Runtime GenAI Library för att skapa en Prompt flow-lösning baserad på Windows GPU.

## **Installation**

### **ONNX Runtime GenAI för Windows GPU**

Läs denna guide för att konfigurera ONNX Runtime GenAI för Windows GPU [klicka här](./ORTWindowGPUGuideline.md)

### **Konfigurera Prompt flow i VSCode**

1. Installera Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.sv.png)

2. Efter att ha installerat Prompt flow VS Code Extension, klicka på tillägget och välj **Installation dependencies**. Följ denna guide för att installera Prompt flow SDK i din miljö.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.sv.png)

3. Ladda ner [Exempelkod](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) och öppna detta exempel i VS Code.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.sv.png)

4. Öppna **flow.dag.yaml** för att välja din Python-miljö.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.sv.png)

   Öppna **chat_phi3_ort.py** för att ändra platsen för din Phi-3.5-instruct ONNX-modell.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.sv.png)

5. Kör din Prompt flow för att testa.

Öppna **flow.dag.yaml** och klicka på visuell redigerare.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.sv.png)

Efter att ha klickat på detta, kör och testa.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.sv.png)

1. Du kan köra batch i terminalen för att kontrollera fler resultat.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan kontrollera resultaten i din standardwebbläsare.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.sv.png)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.