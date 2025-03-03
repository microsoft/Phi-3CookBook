Phi-3-mini WebGPU RAG Chatbot

## Demo for å demonstrere WebGPU og RAG-mønster
RAG-mønsteret med Phi-3 Onnx Hosted-modell bruker Retrieval-Augmented Generation-tilnærmingen, som kombinerer kraften til Phi-3-modeller med ONNX-hosting for effektive AI-distribusjoner. Dette mønsteret er avgjørende for å finjustere modeller for oppgaver innen spesifikke domener, og tilbyr en kombinasjon av kvalitet, kostnadseffektivitet og forståelse av lange kontekster. Det er en del av Azure AIs portefølje, som gir et bredt utvalg av modeller som er enkle å finne, prøve og bruke, og som imøtekommer tilpasningsbehovene til ulike bransjer. Phi-3-modellene, inkludert Phi-3-mini, Phi-3-small og Phi-3-medium, er tilgjengelige i Azure AI Model Catalog og kan finjusteres og distribueres enten selvstyrt eller gjennom plattformer som HuggingFace og ONNX, noe som viser Microsofts engasjement for tilgjengelige og effektive AI-løsninger.

## Hva er WebGPU 
WebGPU er et moderne grafikk-API for nettlesere, designet for å gi effektiv tilgang til en enhets grafikkprosessor (GPU) direkte fra nettlesere. Det er ment å være etterfølgeren til WebGL, med flere viktige forbedringer:

1. **Kompatibilitet med moderne GPU-er**: WebGPU er bygget for å fungere sømløst med moderne GPU-arkitekturer og bruker system-API-er som Vulkan, Metal og Direct3D 12.
2. **Forbedret ytelse**: Det støtter generelle GPU-beregninger og raskere operasjoner, noe som gjør det egnet for både grafikkgjengivelse og maskinlæringsoppgaver.
3. **Avanserte funksjoner**: WebGPU gir tilgang til mer avanserte GPU-funksjoner, som muliggjør mer komplekse og dynamiske grafikk- og beregningsoppgaver.
4. **Redusert arbeidsbelastning for JavaScript**: Ved å overføre flere oppgaver til GPU-en reduserer WebGPU betydelig arbeidsbelastningen på JavaScript, noe som fører til bedre ytelse og jevnere opplevelser.

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
Skriv 'enable-unsafe-webgpu' i søkefeltet øverst på siden.

#### Aktiver flagget:
Finn flagget #enable-unsafe-webgpu i resultatlisten.

Klikk på rullegardinmenyen ved siden av det og velg Enabled.

#### Start nettleseren på nytt:

Etter å ha aktivert flagget, må du starte nettleseren på nytt for at endringene skal tre i kraft. Klikk på Relanser-knappen som vises nederst på siden.

- For Linux, start nettleseren med `--enable-features=Vulkan`.
- Safari 18 (macOS 15) har WebGPU aktivert som standard.
- I Firefox Nightly, skriv about:config i adressefeltet og `set dom.webgpu.enabled to true`.

### Sette opp GPU for Microsoft Edge 

Her er trinnene for å sette opp en høyytelses-GPU for Microsoft Edge på Windows:

- **Åpne Innstillinger:** Klikk på Start-menyen og velg Innstillinger.
- **Systeminnstillinger:** Gå til System og deretter Skjerm.
- **Grafikkinnstillinger:** Rull nedover og klikk på Grafikkinnstillinger.
- **Velg app:** Under “Velg en app for å angi preferanse,” velg Desktop app og deretter Bla gjennom.
- **Velg Edge:** Gå til Edge-installasjonsmappen (vanligvis `C:\Program Files (x86)\Microsoft\Edge\Application`) og velg `msedge.exe`.
- **Angi preferanse:** Klikk på Alternativer, velg Høy ytelse, og klikk deretter Lagre.
Dette vil sikre at Microsoft Edge bruker GPU-en med høy ytelse for bedre ytelse. 
- **Start** maskinen din på nytt for at disse innstillingene skal tre i kraft.

### Åpne Codespace:
Gå til ditt repository på GitHub.
Klikk på Code-knappen og velg Open with Codespaces.

Hvis du ikke har en Codespace ennå, kan du opprette en ved å klikke på New codespace.

**Merk** Installere Node-miljø i din Codespace
Å kjøre en npm-demo fra en GitHub Codespace er en flott måte å teste og utvikle prosjektet ditt på. Her er en trinnvis veiledning for å komme i gang:

### Sett opp miljøet ditt:
Når Codespace er åpen, sørg for at du har Node.js og npm installert. Du kan sjekke dette ved å kjøre:
```
node -v
```
```
npm -v
```

Hvis de ikke er installert, kan du installere dem ved å bruke:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Naviger til prosjektkatalogen din:
Bruk terminalen for å navigere til katalogen der npm-prosjektet ditt er plassert:
```
cd path/to/your/project
```

### Installer avhengigheter:
Kjør følgende kommando for å installere alle nødvendige avhengigheter som er oppført i din package.json-fil:

```
npm install
```

### Kjør demoen:
Når avhengighetene er installert, kan du kjøre demoskriptet ditt. Dette er vanligvis spesifisert i script-delen av package.json-filen. For eksempel, hvis demoskriptet ditt heter start, kan du kjøre:

```
npm run build
```
```
npm run dev
```

### Få tilgang til demoen:
Hvis demoen din involverer en webserver, vil Codespaces gi en URL for å få tilgang til den. Se etter en varsling eller sjekk Ports-fanen for å finne URL-en.

**Merk:** Modellen må hurtigbufres i nettleseren, så det kan ta litt tid å laste.

### RAG Demo
Last opp markdown-filen `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Velg filen din:
Klikk på knappen som sier “Choose File” for å velge dokumentet du vil laste opp.

### Last opp dokumentet:
Etter å ha valgt filen din, klikk på “Upload”-knappen for å laste opp dokumentet for RAG (Retrieval-Augmented Generation).

### Start chatten din:
Når dokumentet er lastet opp, kan du starte en chatøkt ved å bruke RAG basert på innholdet i dokumentet ditt.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell, menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.