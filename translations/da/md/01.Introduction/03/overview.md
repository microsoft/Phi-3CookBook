I forbindelse med Phi-3-mini refererer inferens til processen med at bruge modellen til at lave forudsigelser eller generere output baseret på inputdata. Lad mig give dig flere detaljer om Phi-3-mini og dens inferensmuligheder.

Phi-3-mini er en del af Phi-3-serien af modeller udgivet af Microsoft. Disse modeller er designet til at omdefinere, hvad der er muligt med små sprogmodeller (SLM'er).

Her er nogle nøglepunkter om Phi-3-mini og dens inferensmuligheder:

## **Oversigt over Phi-3-mini:**
- Phi-3-mini har en parameterstørrelse på 3,8 milliarder.
- Den kan køre ikke kun på traditionelle computerenheder, men også på edge-enheder som mobiltelefoner og IoT-enheder.
- Udgivelsen af Phi-3-mini gør det muligt for både enkeltpersoner og virksomheder at implementere SLM'er på forskellige hardwareenheder, især i miljøer med begrænsede ressourcer.
- Den understøtter forskellige modelformater, herunder det traditionelle PyTorch-format, den kvantiserede version af gguf-formatet og den ONNX-baserede kvantiserede version.

## **Adgang til Phi-3-mini:**
For at få adgang til Phi-3-mini kan du bruge [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) i en Copilot-applikation. Semantic Kernel er generelt kompatibel med Azure OpenAI Service, open source-modeller på Hugging Face og lokale modeller.  
Du kan også bruge [Ollama](https://ollama.com) eller [LlamaEdge](https://llamaedge.com) til at kalde kvantiserede modeller. Ollama giver individuelle brugere mulighed for at kalde forskellige kvantiserede modeller, mens LlamaEdge tilbyder platform-uafhængig tilgængelighed for GGUF-modeller.

## **Kvantiserede modeller:**
Mange brugere foretrækker at bruge kvantiserede modeller til lokal inferens. For eksempel kan du direkte køre Ollama run Phi-3 eller konfigurere den offline ved hjælp af en Modelfile. Modelfilen specificerer GGUF-filens sti og promptformatet.

## **Muligheder inden for generativ AI:**
Kombinationen af SLM'er som Phi-3-mini åbner op for nye muligheder inden for generativ AI. Inferens er blot det første skridt; disse modeller kan bruges til forskellige opgaver i miljøer med begrænsede ressourcer, lav latenstid og stramme budgetter.

## **Sådan udnytter du generativ AI med Phi-3-mini: En guide til inferens og implementering**  
Lær, hvordan du bruger Semantic Kernel, Ollama/LlamaEdge og ONNX Runtime til at få adgang til og udføre inferens med Phi-3-mini-modeller, og udforsk mulighederne inden for generativ AI i forskellige applikationsscenarier.

**Funktioner**  
Inferens af phi3-mini-modellen i:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Sammenfattende giver Phi-3-mini udviklere mulighed for at udforske forskellige modelformater og udnytte generativ AI i forskellige applikationsscenarier.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.