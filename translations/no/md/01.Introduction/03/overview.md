I konteksten av Phi-3-mini refererer inferens til prosessen med å bruke modellen for å lage prediksjoner eller generere resultater basert på inngangsdata. La meg gi deg mer informasjon om Phi-3-mini og dens evner innen inferens.

Phi-3-mini er en del av Phi-3-serien med modeller utgitt av Microsoft. Disse modellene er designet for å omdefinere hva som er mulig med små språkmodeller (SLMs).

Her er noen viktige punkter om Phi-3-mini og dens inferenskapabiliteter:

## **Oversikt over Phi-3-mini:**
- Phi-3-mini har en parameterstørrelse på 3,8 milliarder.
- Den kan kjøre ikke bare på tradisjonelle datamaskiner, men også på edge-enheter som mobiltelefoner og IoT-enheter.
- Utgivelsen av Phi-3-mini gjør det mulig for både enkeltpersoner og bedrifter å distribuere SLM-er på forskjellige maskinvareenheter, spesielt i miljøer med begrensede ressurser.
- Den støtter ulike modelformater, inkludert det tradisjonelle PyTorch-formatet, den kvantiserte versjonen av gguf-formatet og den ONNX-baserte kvantiserte versjonen.

## **Tilgang til Phi-3-mini:**
For å få tilgang til Phi-3-mini kan du bruke [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) i en Copilot-applikasjon. Semantic Kernel er generelt kompatibel med Azure OpenAI Service, open-source-modeller på Hugging Face og lokale modeller.
Du kan også bruke [Ollama](https://ollama.com) eller [LlamaEdge](https://llamaedge.com) for å kjøre kvantiserte modeller. Ollama lar enkeltbrukere kjøre forskjellige kvantiserte modeller, mens LlamaEdge gir plattformuavhengig tilgang til GGUF-modeller.

## **Kvantiserte modeller:**
Mange brukere foretrekker å bruke kvantiserte modeller for lokal inferens. For eksempel kan du kjøre Ollama run Phi-3 direkte eller konfigurere den offline ved hjelp av en Modelfile. Modelfilen spesifiserer GGUF-filbanen og formatet på promptet.

## **Muligheter med generativ AI:**
Kombinasjonen av SLM-er som Phi-3-mini åpner nye muligheter for generativ AI. Inferens er bare det første steget; disse modellene kan brukes til en rekke oppgaver i miljøer med begrensede ressurser, lav latens og stramme kostnadsrammer.

## **Lås opp generativ AI med Phi-3-mini: En guide til inferens og distribusjon**  
Lær hvordan du bruker Semantic Kernel, Ollama/LlamaEdge og ONNX Runtime for å få tilgang til og kjøre Phi-3-mini-modeller, og utforsk mulighetene med generativ AI i ulike applikasjonsscenarier.

**Funksjoner**
Inferens av Phi-3-mini-modellen i:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Oppsummert gir Phi-3-mini utviklere muligheten til å utforske ulike modelformater og dra nytte av generativ AI i en rekke applikasjonsscenarier.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettingstjenester. Selv om vi bestreber oss på nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.