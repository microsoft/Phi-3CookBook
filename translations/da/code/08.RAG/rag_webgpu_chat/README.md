Phi-3-mini WebGPU RAG Chatbot

## Demo til at demonstrere WebGPU og RAG-mønster
RAG-mønstret med Phi-3 Onnx Hosted-modellen udnytter Retrieval-Augmented Generation-tilgangen, som kombinerer styrken ved Phi-3-modeller med ONNX-hosting for effektiv AI-udrulning. Dette mønster er afgørende for finjustering af modeller til specifikke domæneopgaver og tilbyder en kombination af kvalitet, omkostningseffektivitet og forståelse af lange kontekster. Det er en del af Azure AI’s portefølje, der giver adgang til et bredt udvalg af modeller, som er nemme at finde, prøve og anvende, og som imødekommer tilpasningsbehovene i forskellige industrier. Phi-3-modellerne, herunder Phi-3-mini, Phi-3-small og Phi-3-medium, er tilgængelige i Azure AI Model Catalog og kan finjusteres og udrulles selvstændigt eller via platforme som HuggingFace og ONNX, hvilket viser Microsofts engagement i tilgængelige og effektive AI-løsninger.

## Hvad er WebGPU
WebGPU er en moderne webgrafik-API designet til at give effektiv adgang til en enheds grafiske behandlingsenhed (GPU) direkte fra webbrowseren. Den er beregnet som efterfølgeren til WebGL og tilbyder flere vigtige forbedringer:

1. **Kompatibilitet med moderne GPU'er**: WebGPU er bygget til at fungere problemfrit med nutidige GPU-arkitekturer og udnytter system-API'er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ydeevne**: Den understøtter generelle GPU-beregninger og hurtigere operationer, hvilket gør den velegnet til både grafikgengivelse og maskinlæringsopgaver.
3. **Avancerede funktioner**: WebGPU giver adgang til mere avancerede GPU-muligheder, hvilket muliggør mere komplekse og dynamiske grafiske og beregningsmæssige arbejdsbyrder.
4. **Reduceret JavaScript-belastning**: Ved at overføre flere opgaver til GPU’en reducerer WebGPU markant belastningen på JavaScript, hvilket fører til bedre ydeevne og glattere oplevelser.

WebGPU understøttes i øjeblikket af browsere som Google Chrome, og der arbejdes på at udvide understøttelsen til andre platforme.

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
Skriv `chrome://flags` i adressefeltet, og tryk på Enter.

#### Søg efter flaget:
Skriv 'enable-unsafe-webgpu' i søgefeltet øverst på siden.

#### Aktiver flaget:
Find flaget #enable-unsafe-webgpu i resultatlisten.

Klik på rullemenuen ved siden af det og vælg Enabled.

#### Genstart din browser:
Efter aktivering af flaget skal du genstarte din browser for at ændringerne træder i kraft. Klik på knappen Relaunch, der vises nederst på siden.

- For Linux skal du starte browseren med `--enable-features=Vulkan`.
- Safari 18 (macOS 15) har WebGPU aktiveret som standard.
- I Firefox Nightly skal du skrive about:config i adressefeltet og `set dom.webgpu.enabled to true`.

### Opsætning af GPU til Microsoft Edge 

Følg disse trin for at opsætte en højtydende GPU til Microsoft Edge på Windows:

- **Åbn Indstillinger:** Klik på Start-menuen og vælg Indstillinger.
- **Systemindstillinger:** Gå til System og derefter Skærm.
- **Grafikindstillinger:** Rul ned og klik på Grafikindstillinger.
- **Vælg app:** Under "Vælg en app for at angive præference" skal du vælge Desktop-app og derefter Gennemse.
- **Vælg Edge:** Naviger til Edge-installationsmappen (normalt `C:\Program Files (x86)\Microsoft\Edge\Application`) og vælg `msedge.exe`.
- **Angiv præference:** Klik på Indstillinger, vælg Høj ydeevne, og klik derefter på Gem.
Dette sikrer, at Microsoft Edge bruger din højtydende GPU for bedre ydeevne. 
- **Genstart** din maskine for at disse indstillinger træder i kraft.

### Åbn din Codespace:
Naviger til dit repository på GitHub.
Klik på knappen Code og vælg Åbn med Codespaces.

Hvis du endnu ikke har en Codespace, kan du oprette en ved at klikke på Ny codespace.

**Bemærk** Installation af Node-miljø i din codespace
At køre en npm-demo fra en GitHub Codespace er en fantastisk måde at teste og udvikle dit projekt på. Her er en trin-for-trin guide til at komme i gang:

### Opsæt dit miljø:
Når din Codespace er åben, skal du sikre dig, at du har Node.js og npm installeret. Du kan tjekke dette ved at køre:
```
node -v
```
```
npm -v
```

Hvis de ikke er installeret, kan du installere dem ved hjælp af:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Naviger til din projektmappe:
Brug terminalen til at navigere til den mappe, hvor dit npm-projekt er placeret:
```
cd path/to/your/project
```

### Installer afhængigheder:
Kør følgende kommando for at installere alle nødvendige afhængigheder, der er angivet i din package.json-fil:

```
npm install
```

### Kør demoen:
Når afhængighederne er installeret, kan du køre dit demoscript. Dette er normalt specificeret i scripts-sektionen af din package.json. For eksempel, hvis dit demoscript hedder start, kan du køre:

```
npm run build
```
```
npm run dev
```

### Adgang til demoen:
Hvis din demo involverer en webserver, vil Codespaces give en URL til at få adgang til den. Kig efter en notifikation eller tjek fanen Ports for at finde URL'en.

**Bemærk:** Modellen skal caches i browseren, så det kan tage lidt tid at indlæse.

### RAG Demo
Upload markdown-filen `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Vælg din fil:
Klik på knappen, der siger “Vælg fil” for at vælge det dokument, du vil uploade.

### Upload dokumentet:
Efter at have valgt din fil skal du klikke på knappen “Upload” for at indlæse dit dokument til RAG (Retrieval-Augmented Generation).

### Start din chat:
Når dokumentet er uploadet, kan du starte en chat-session ved hjælp af RAG baseret på indholdet af dit dokument.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.