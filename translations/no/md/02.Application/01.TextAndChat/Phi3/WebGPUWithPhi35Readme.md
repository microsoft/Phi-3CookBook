# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo for å demonstrere WebGPU og RAG-mønsteret

RAG-mønsteret med Phi-3.5 Onnx Hosted-modellen benytter seg av Retrieval-Augmented Generation-tilnærmingen, som kombinerer kraften til Phi-3.5-modellene med ONNX-hosting for effektiv AI-distribusjon. Dette mønsteret er avgjørende for finjustering av modeller for oppgavespesifikke behov, og tilbyr en kombinasjon av kvalitet, kostnadseffektivitet og evne til å håndtere lange kontekster. Det er en del av Azure AI, som gir et bredt utvalg av modeller som er enkle å finne, teste og bruke, og tilpasset ulike bransjers behov.

## Hva er WebGPU 
WebGPU er et moderne grafikk-API for nettlesere, designet for å gi effektiv tilgang til enhetens grafikkprosesseringsenhet (GPU) direkte fra nettlesere. Det er ment som en etterfølger til WebGL og tilbyr flere viktige forbedringer:

1. **Kompatibilitet med moderne GPU-er**: WebGPU er utviklet for å fungere sømløst med dagens GPU-arkitekturer, ved å bruke system-API-er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ytelse**: Det støtter generelle GPU-beregninger og raskere operasjoner, noe som gjør det egnet både for grafikkrendering og maskinlæringsoppgaver.
3. **Avanserte funksjoner**: WebGPU gir tilgang til mer avanserte GPU-funksjoner, som muliggjør mer komplekse og dynamiske grafikk- og beregningsarbeidsoppgaver.
4. **Redusert arbeidsmengde for JavaScript**: Ved å overføre flere oppgaver til GPU-en, reduserer WebGPU betydelig arbeidsmengden for JavaScript, noe som gir bedre ytelse og en jevnere opplevelse.

WebGPU støttes for øyeblikket i nettlesere som Google Chrome, med pågående arbeid for å utvide støtten til andre plattformer.

### 03.WebGPU
Krav til miljø:

**Støttede nettlesere:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Aktiver WebGPU:

- I Chrome/Microsoft Edge 

Aktiver `chrome://flags/#enable-unsafe-webgpu`-flagget.

#### Åpne nettleseren din:
Start Google Chrome eller Microsoft Edge.

#### Gå til Flags-siden:
Skriv `chrome://flags` i adressefeltet og trykk Enter.

#### Søk etter flagget:
Skriv 'enable-unsafe-webgpu' i søkeboksen øverst på siden.

#### Aktiver flagget:
Finn flagget #enable-unsafe-webgpu i resultatlisten.

Klikk på rullegardinmenyen ved siden av og velg Enabled.

#### Start nettleseren på nytt:

Etter å ha aktivert flagget, må du starte nettleseren på nytt for at endringene skal tre i kraft. Klikk på knappen Relaunch som vises nederst på siden.

- For Linux, start nettleseren med `--enable-features=Vulkan`.
- Safari 18 (macOS 15) har WebGPU aktivert som standard.
- I Firefox Nightly, skriv about:config i adressefeltet og `set dom.webgpu.enabled to true`.

### Sette opp GPU for Microsoft Edge 

Her er trinnene for å sette opp en høyytelses-GPU for Microsoft Edge på Windows:

- **Åpne Innstillinger:** Klikk på Start-menyen og velg Innstillinger.
- **Systeminnstillinger:** Gå til System og deretter Skjerm.
- **Grafikkinnstillinger:** Rull nedover og klikk på Grafikkinnstillinger.
- **Velg app:** Under "Velg en app for å angi preferanse," velg Desktop-app og deretter Bla gjennom.
- **Velg Edge:** Gå til Edge-installasjonsmappen (vanligvis `C:\Program Files (x86)\Microsoft\Edge\Application`) og velg `msedge.exe`.
- **Angi preferanse:** Klikk på Alternativer, velg Høy ytelse, og klikk deretter Lagre.
Dette vil sikre at Microsoft Edge bruker din høyytelses-GPU for bedre ytelse. 
- **Start maskinen på nytt** for at disse innstillingene skal tre i kraft.

### Eksempler: Vennligst [klikk på denne lenken](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettingstjenester. Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.