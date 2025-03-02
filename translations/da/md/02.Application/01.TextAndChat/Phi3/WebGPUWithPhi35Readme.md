# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo til fremvisning af WebGPU og RAG-mønster

RAG-mønsteret med Phi-3.5 Onnx Hosted-modellen udnytter Retrieval-Augmented Generation-metoden, som kombinerer styrken fra Phi-3.5-modeller med ONNX-hosting for effektive AI-implementeringer. Dette mønster er afgørende for finjustering af modeller til branchespecifikke opgaver og tilbyder en kombination af kvalitet, omkostningseffektivitet og lang kontekstforståelse. Det er en del af Azure AI's portefølje, som giver adgang til et bredt udvalg af modeller, der er nemme at finde, afprøve og bruge, og som opfylder tilpasningsbehovene i forskellige industrier.

## Hvad er WebGPU 
WebGPU er en moderne webgrafik-API designet til at give effektiv adgang til en enheds grafikprocessor (GPU) direkte fra webbrowseren. Den er beregnet som efterfølgeren til WebGL og tilbyder flere vigtige forbedringer:

1. **Kompatibilitet med moderne GPU'er**: WebGPU er udviklet til at fungere problemfrit med nutidens GPU-arkitekturer og udnytter system-API'er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ydeevne**: Den understøtter generelle GPU-beregninger og hurtigere operationer, hvilket gør den velegnet til både grafikrendering og maskinlæringsopgaver.
3. **Avancerede funktioner**: WebGPU giver adgang til mere avancerede GPU-muligheder, hvilket muliggør mere komplekse og dynamiske grafik- og beregningsopgaver.
4. **Reduceret arbejdsbyrde for JavaScript**: Ved at flytte flere opgaver til GPU'en reducerer WebGPU markant JavaScripts arbejdsbyrde, hvilket resulterer i bedre ydeevne og mere flydende oplevelser.

WebGPU understøttes i øjeblikket af browsere som Google Chrome, og der arbejdes løbende på at udvide understøttelsen til andre platforme.

### 03.WebGPU
Påkrævet miljø:

**Understøttede browsere:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Aktiver WebGPU:

- I Chrome/Microsoft Edge 

Aktiver `chrome://flags/#enable-unsafe-webgpu`-flaget.

#### Åbn din browser:
Start Google Chrome eller Microsoft Edge.

#### Gå til flagsiden:
Skriv `chrome://flags` i adressefeltet, og tryk Enter.

#### Søg efter flaget:
Skriv 'enable-unsafe-webgpu' i søgefeltet øverst på siden.

#### Aktiver flaget:
Find #enable-unsafe-webgpu-flaget i resultatlisten.

Klik på rullemenuen ved siden af det, og vælg Enabled.

#### Genstart din browser:

Efter aktivering af flaget skal du genstarte din browser, for at ændringerne træder i kraft. Klik på knappen Relaunch, der vises nederst på siden.

- For Linux, start browseren med `--enable-features=Vulkan`.
- Safari 18 (macOS 15) har WebGPU aktiveret som standard.
- I Firefox Nightly skal du skrive about:config i adressefeltet og `set dom.webgpu.enabled to true`.

### Opsætning af GPU til Microsoft Edge 

Her er trinnene til at opsætte en højtydende GPU til Microsoft Edge på Windows:

- **Åbn Indstillinger:** Klik på Startmenuen, og vælg Indstillinger.
- **Systemindstillinger:** Gå til System og derefter Skærm.
- **Grafikindstillinger:** Rul ned, og klik på Grafikindstillinger.
- **Vælg app:** Under “Vælg en app for at indstille præference” skal du vælge Desktop-app og derefter Gennemse.
- **Vælg Edge:** Naviger til Edge-installationsmappen (normalt `C:\Program Files (x86)\Microsoft\Edge\Application`) og vælg `msedge.exe`.
- **Indstil præference:** Klik på Indstillinger, vælg Høj ydeevne, og klik derefter på Gem.
Dette vil sikre, at Microsoft Edge bruger din højtydende GPU for bedre ydeevne.
- **Genstart** din computer for at disse indstillinger træder i kraft.

### Eksempler: Klik venligst på [dette link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.