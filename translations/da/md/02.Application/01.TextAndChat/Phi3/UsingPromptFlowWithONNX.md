# Brug af Windows GPU til at skabe Prompt Flow-løsning med Phi-3.5-Instruct ONNX

Dette dokument er et eksempel på, hvordan man bruger PromptFlow med ONNX (Open Neural Network Exchange) til at udvikle AI-applikationer baseret på Phi-3-modeller.

PromptFlow er en samling udviklingsværktøjer designet til at forenkle hele udviklingscyklussen for AI-applikationer baseret på store sprogmodeller (LLM), fra idéudvikling og prototyper til test og evaluering.

Ved at integrere PromptFlow med ONNX kan udviklere:

- **Optimere modelydelse**: Udnyt ONNX til effektiv modelinference og implementering.
- **Forenkle udvikling**: Brug PromptFlow til at styre arbejdsgangen og automatisere gentagne opgaver.
- **Forbedre samarbejde**: Skab bedre samarbejde mellem teammedlemmer ved at tilbyde et samlet udviklingsmiljø.

**Prompt flow** er en samling udviklingsværktøjer designet til at forenkle hele udviklingscyklussen for AI-applikationer baseret på LLM, fra idéudvikling, prototyper, test og evaluering til produktion og overvågning. Det gør prompt engineering meget nemmere og giver dig mulighed for at bygge LLM-applikationer med produktionskvalitet.

Prompt flow kan forbindes til OpenAI, Azure OpenAI Service og tilpassede modeller (Huggingface, lokale LLM/SLM). Vi håber at kunne implementere Phi-3.5's kvantiserede ONNX-model i lokale applikationer. Prompt flow kan hjælpe os med bedre at planlægge vores forretning og fuldføre lokale løsninger baseret på Phi-3.5. I dette eksempel vil vi kombinere ONNX Runtime GenAI Library for at fuldføre Prompt flow-løsningen baseret på Windows GPU.

## **Installation**

### **ONNX Runtime GenAI til Windows GPU**

Læs denne vejledning for at opsætte ONNX Runtime GenAI til Windows GPU [klik her](./ORTWindowGPUGuideline.md)

### **Opsæt Prompt flow i VSCode**

1. Installer Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.da.png)

2. Efter installation af Prompt flow VS Code Extension, klik på udvidelsen, og vælg **Installation dependencies**. Følg denne vejledning for at installere Prompt flow SDK i dit miljø.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.da.png)

3. Download [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) og åbn dette eksempel i VS Code.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.da.png)

4. Åbn **flow.dag.yaml** for at vælge dit Python-miljø.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.da.png)

   Åbn **chat_phi3_ort.py** for at ændre placeringen af din Phi-3.5-instruct ONNX-model.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.da.png)

5. Kør dit Prompt flow for at teste.

Åbn **flow.dag.yaml**, og klik på visual editor.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.da.png)

Klik herefter på denne, og kør for at teste.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.da.png)

1. Du kan køre batch i terminalen for at tjekke flere resultater.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Du kan tjekke resultaterne i din standardbrowser.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.da.png)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.