# **Kvantisering af Phi-familien**

Modelkvantisering refererer til processen med at mappe parametrene (såsom vægte og aktiveringsværdier) i en neuralt netværksmodel fra et stort værdiområde (normalt et kontinuerligt værdiområde) til et mindre, endeligt værdiområde. Denne teknologi kan reducere modellens størrelse og beregningskompleksitet samt forbedre modellens driftseffektivitet i ressourcebegrænsede miljøer som mobile enheder eller indlejrede systemer. Modelkvantisering opnår kompression ved at reducere præcisionen af parametrene, men det introducerer også et vist præcisionstab. Derfor er det nødvendigt at balancere modelstørrelse, beregningskompleksitet og præcision i kvantiseringsprocessen. Almindelige kvantiseringsmetoder inkluderer fixed-point kvantisering, floating-point kvantisering osv. Du kan vælge den passende kvantiseringsstrategi afhængigt af den specifikke situation og behov.

Vi ønsker at implementere GenAI-modeller på edge-enheder og gøre det muligt for flere enheder at indgå i GenAI-scenarier, såsom mobile enheder, AI PC/Copilot+PC og traditionelle IoT-enheder. Gennem kvantiseringsmodellen kan vi implementere den på forskellige edge-enheder baseret på deres specifikationer. Kombineret med modelaccelerationsrammer og kvantiseringsmodeller leveret af hardwareproducenter kan vi skabe bedre SLM-applikationsscenarier.

I kvantiseringsscenariet har vi forskellige præcisioner (INT4, INT8, FP16, FP32). Nedenfor følger en forklaring af de mest anvendte kvantiseringspræcisioner.

### **INT4**

INT4-kvantisering er en radikal kvantiseringsmetode, der kvantiserer modellens vægte og aktiveringsværdier til 4-bit heltal. INT4-kvantisering resulterer ofte i et større præcisionstab på grund af det mindre repræsentationsområde og den lavere præcision. Dog kan INT4-kvantisering, sammenlignet med INT8-kvantisering, yderligere reducere modellens lagerkrav og beregningskompleksitet. Det skal bemærkes, at INT4-kvantisering er relativt sjælden i praksis, fordi den lave præcision kan føre til betydelig forringelse af modellens ydeevne. Desuden understøtter ikke alle hardwareenheder INT4-operationer, så hardwarekompatibilitet skal overvejes ved valg af kvantiseringsmetode.

### **INT8**

INT8-kvantisering er processen med at konvertere en models vægte og aktiveringer fra floating point-værdier til 8-bit heltal. Selvom det numeriske område repræsenteret af INT8-heltal er mindre og mindre præcist, kan det markant reducere lager- og beregningskrav. I INT8-kvantisering gennemgår modellens vægte og aktiveringsværdier en kvantiseringsproces, der inkluderer skalering og offset, for at bevare den oprindelige floating point-information så meget som muligt. Under inferens bliver disse kvantiserede værdier dekvantiseret tilbage til floating point-værdier til beregning og derefter kvantiseret tilbage til INT8 til næste trin. Denne metode kan levere tilstrækkelig præcision i de fleste applikationer og samtidig opretholde høj beregningseffektivitet.

### **FP16**

FP16-formatet, altså 16-bit floating point-værdier (float16), reducerer hukommelsesforbruget til det halve sammenlignet med 32-bit floating point-værdier (float32), hvilket giver betydelige fordele i storskala deep learning-applikationer. FP16-formatet gør det muligt at indlæse større modeller eller behandle mere data inden for de samme GPU-hukommelsesbegrænsninger. Efterhånden som moderne GPU-hardware fortsætter med at understøtte FP16-operationer, kan brugen af FP16-formatet også føre til forbedringer i beregningshastighed. Dog har FP16-formatet også sine iboende ulemper, nemlig lavere præcision, hvilket i nogle tilfælde kan føre til numerisk ustabilitet eller præcisionstab.

### **FP32**

FP32-formatet giver højere præcision og kan nøjagtigt repræsentere et bredt spektrum af værdier. I scenarier, hvor komplekse matematiske operationer udføres, eller hvor højpræcisionsresultater er nødvendige, foretrækkes FP32-formatet. Dog betyder høj præcision også større hukommelsesforbrug og længere beregningstid. For storskala deep learning-modeller, især når der er mange modelparametre og store datamængder, kan FP32-formatet føre til utilstrækkelig GPU-hukommelse eller nedsat inferenshastighed.

På mobile enheder eller IoT-enheder kan vi konvertere Phi-3.x-modeller til INT4, mens AI PC / Copilot PC kan bruge højere præcision som INT8, FP16, FP32.

På nuværende tidspunkt har forskellige hardwareproducenter forskellige rammer til at understøtte generative modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX og Nvidias CUDA osv., kombineret med modelkvantisering til at fuldføre lokal implementering.

Teknisk set har vi forskellige formatunderstøttelser efter kvantisering, såsom PyTorch / Tensorflow-format, GGUF og ONNX. Jeg har lavet en sammenligning mellem GGUF og ONNX i forhold til format og applikationsscenarier. Her anbefaler jeg ONNX-kvantisering, som har god understøttelse fra modelrammen til hardwaren. I dette kapitel vil vi fokusere på ONNX Runtime for GenAI, OpenVINO og Apple MLX til at udføre modelkvantisering (hvis du har en bedre metode, kan du også give den til os ved at indsende en PR).

**Dette kapitel indeholder**

1. [Kvantisering af Phi-3.5 / 4 ved brug af llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantisering af Phi-3.5 / 4 ved brug af Generative AI-udvidelser til onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantisering af Phi-3.5 / 4 ved brug af Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantisering af Phi-3.5 / 4 ved brug af Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.