# Windows GPU gebruiken om een Prompt Flow-oplossing te creëren met Phi-3.5-Instruct ONNX

Dit document is een voorbeeld van hoe je PromptFlow kunt gebruiken met ONNX (Open Neural Network Exchange) voor het ontwikkelen van AI-toepassingen gebaseerd op Phi-3-modellen.

PromptFlow is een reeks ontwikkeltools die ontworpen zijn om de volledige ontwikkelcyclus van LLM-gebaseerde (Large Language Model) AI-toepassingen te stroomlijnen, van idee en prototyping tot testen en evaluatie.

Door PromptFlow te integreren met ONNX kunnen ontwikkelaars:

- **Modelprestaties optimaliseren**: Gebruik ONNX voor efficiënte modelinference en implementatie.  
- **Ontwikkeling vereenvoudigen**: Gebruik PromptFlow om workflows te beheren en repetitieve taken te automatiseren.  
- **Samenwerking verbeteren**: Bied een uniforme ontwikkelomgeving om de samenwerking tussen teamleden te vergemakkelijken.

**Prompt flow** is een reeks ontwikkeltools die ontworpen zijn om de volledige ontwikkelcyclus van LLM-gebaseerde AI-toepassingen te stroomlijnen, van idee, prototyping, testen, evaluatie tot implementatie en monitoring in productie. Het maakt prompt engineering veel eenvoudiger en stelt je in staat om LLM-apps van productiekwaliteit te bouwen.

Prompt flow kan verbinding maken met OpenAI, Azure OpenAI Service en aanpasbare modellen (Huggingface, lokale LLM/SLM). We hopen Phi-3.5's gequantiseerde ONNX-model te implementeren in lokale toepassingen. Prompt flow kan ons helpen onze bedrijfsvoering beter te plannen en lokale oplossingen te voltooien op basis van Phi-3.5. In dit voorbeeld combineren we de ONNX Runtime GenAI Library om de Prompt Flow-oplossing te realiseren op basis van Windows GPU.

## **Installatie**

### **ONNX Runtime GenAI voor Windows GPU**

Lees deze handleiding om ONNX Runtime GenAI voor Windows GPU in te stellen [klik hier](./ORTWindowGPUGuideline.md)

### **Prompt flow instellen in VSCode**

1. Installeer de Prompt flow VS Code-extensie

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.nl.png)

2. Nadat je de Prompt flow VS Code-extensie hebt geïnstalleerd, klik je op de extensie en kies je **Installation dependencies**. Volg deze handleiding om de Prompt flow SDK in je omgeving te installeren.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.nl.png)

3. Download [Voorbeeldcode](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) en open dit voorbeeld met VS Code.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.nl.png)

4. Open **flow.dag.yaml** om je Python-omgeving te selecteren.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.nl.png)

   Open **chat_phi3_ort.py** om de locatie van je Phi-3.5-Instruct ONNX-model te wijzigen.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.nl.png)

5. Voer je Prompt Flow uit om te testen.

Open **flow.dag.yaml** en klik op de visuele editor.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.nl.png)

Klik hierop en voer het uit om te testen.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.nl.png)

1. Je kunt een batch uitvoeren in de terminal om meer resultaten te bekijken.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Je kunt de resultaten bekijken in je standaardbrowser.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.nl.png)

**Disclaimer (Vrijwaring)**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.