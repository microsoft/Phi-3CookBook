# **Byg din egen Visual Studio Code GitHub Copilot Chat med Microsoft Phi-3 Family**

Har du brugt arbejdsområdeagenten i GitHub Copilot Chat? Vil du bygge din egen kodeagent til dit team? Denne hands-on workshop har til formål at kombinere open source-modellen for at skabe en virksomhedsniveau kodeagent.

## **Grundlag**

### **Hvorfor vælge Microsoft Phi-3**

Phi-3 er en serie, der inkluderer phi-3-mini, phi-3-small og phi-3-medium baseret på forskellige træningsparametre til tekstgenerering, dialogkomplettering og kodegenerering. Der er også phi-3-vision baseret på Vision. Det er velegnet til virksomheder eller forskellige teams, der ønsker at skabe offline generative AI-løsninger.

Anbefalet læsning: [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat-udvidelsen giver dig en chatgrænseflade, der lader dig interagere med GitHub Copilot og modtage svar på kode-relaterede spørgsmål direkte i VS Code, uden at du behøver at navigere i dokumentation eller søge på online fora.

Copilot Chat kan bruge syntaksfremhævning, indrykning og andre formateringsfunktioner til at tilføje klarhed til det genererede svar. Afhængigt af typen af spørgsmål fra brugeren kan resultatet indeholde links til konteksten, som Copilot brugte til at generere et svar, såsom kildekodefiler eller dokumentation, eller knapper til adgang til VS Code-funktioner.

- Copilot Chat integreres i din udviklerarbejdsproces og giver dig hjælp, hvor du har brug for det:

- Start en inline-chat direkte fra editoren eller terminalen for at få hjælp, mens du koder

- Brug Chat-visningen til at have en AI-assistent ved din side, der kan hjælpe dig når som helst

- Start Quick Chat for at stille et hurtigt spørgsmål og vende tilbage til det, du er i gang med

Du kan bruge GitHub Copilot Chat i forskellige scenarier, såsom:

- Besvarelse af kode-relaterede spørgsmål om, hvordan man bedst løser et problem

- Forklaring af andres kode og forslag til forbedringer

- Foreslå kodefejlrettelser

- Generering af enhedstestcases

- Generering af kodedokumentation

Anbefalet læsning: [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Ved at referere til **@workspace** i Copilot Chat kan du stille spørgsmål om hele din kodebase. Baseret på spørgsmålet henter Copilot intelligent relevante filer og symboler, som det derefter refererer til i sit svar som links og kodeeksempler.

For at besvare dit spørgsmål søger **@workspace** gennem de samme kilder, som en udvikler ville bruge, når de navigerer i en kodebase i VS Code:

- Alle filer i arbejdsområdet, undtagen filer, der ignoreres af en .gitignore-fil

- Mappestruktur med indlejrede mapper og filnavne

- GitHubs kode-søgeindeks, hvis arbejdsområdet er et GitHub-repository og indekseret af kode-søgning

- Symboler og definitioner i arbejdsområdet

- Aktuelt valgt tekst eller synlig tekst i den aktive editor

Bemærk: .gitignore ignoreres, hvis du har en fil åben eller har valgt tekst i en ignoreret fil.

Anbefalet læsning: [https://code.visualstudio.com/docs/copilot/workspace-context](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)

## **Lær mere om denne workshop**

GitHub Copilot har i høj grad forbedret programmeringseffektiviteten i virksomheder, og hver virksomhed ønsker at tilpasse de relevante funktioner i GitHub Copilot. Mange virksomheder har tilpasset udvidelser, der ligner GitHub Copilot, baseret på deres egne forretningsscenarier og open source-modeller. For virksomheder er tilpassede udvidelser nemmere at kontrollere, men det påvirker også brugeroplevelsen. Når alt kommer til alt har GitHub Copilot stærkere funktioner til at håndtere generelle scenarier og høj faglighed. Hvis oplevelsen kan holdes konsistent, ville det være bedre at tilpasse virksomhedens egen udvidelse. GitHub Copilot Chat giver relevante API'er til virksomheder, der ønsker at udvide chatoplevelsen. At opretholde en konsistent oplevelse og have tilpassede funktioner giver en bedre brugeroplevelse.

Denne workshop bruger primært Phi-3-modellen kombineret med den lokale NPU og Azure hybrid til at bygge en tilpasset agent i GitHub Copilot Chat ***@PHI3*** til at hjælpe virksomhedens udviklere med at udføre kodegenerering ***(@PHI3 /gen)*** og generere kode baseret på billeder ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.da.png)

### ***Bemærk:*** 

Denne workshop er i øjeblikket implementeret i AIPC for Intel CPU og Apple Silicon. Vi vil fortsætte med at opdatere Qualcomm-versionen af NPU.

## **Workshop**

| Navn | Beskrivelse | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installationer (✅) | Konfigurer og installer relaterede miljøer og værktøjer | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Kør Prompt flow med Phi-3-mini (✅) | Kombineret med AIPC / Apple Silicon, brug lokal NPU til at skabe kodegenerering gennem Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Udrul Phi-3-vision på Azure Machine Learning Service (✅) | Generer kode ved at udrulle Azure Machine Learning Service's Model Catalog - Phi-3-vision billede | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Opret en @phi-3 agent i GitHub Copilot Chat (✅)  | Opret en tilpasset Phi-3 agent i GitHub Copilot Chat for at fuldføre kodegenerering, grafgenerering, RAG osv. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Eksempelkode (✅)  | Download eksempelkode | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Ressourcer**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Lær mere om GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Lær mere om GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Lær mere om GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Lær mere om Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Lær mere om Azure AI Foundry's Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvaret for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.