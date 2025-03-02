Phi-3-mini WebGPU RAG Chatbot

## Demo för att visa upp WebGPU och RAG-mönster
RAG-mönstret med Phi-3 Onnx Hosted-modellen använder sig av Retrieval-Augmented Generation-metoden, som kombinerar kraften i Phi-3-modeller med ONNX-hosting för effektiva AI-distributioner. Detta mönster är avgörande för att finjustera modeller för uppgiftsspecifika behov, och erbjuder en kombination av kvalitet, kostnadseffektivitet och lång kontextförståelse. Det är en del av Azure AI:s utbud och erbjuder ett brett urval av modeller som är enkla att hitta, testa och använda, anpassade för olika branscher. Phi-3-modellerna, inklusive Phi-3-mini, Phi-3-small och Phi-3-medium, finns tillgängliga i Azure AI Model Catalog och kan finjusteras och distribueras antingen självständigt eller via plattformar som HuggingFace och ONNX, vilket visar Microsofts engagemang för tillgängliga och effektiva AI-lösningar.

## Vad är WebGPU 
WebGPU är ett modernt webb-grafik-API designat för att ge effektiv åtkomst till en enhets grafikprocessor (GPU) direkt från webbläsare. Det är tänkt att vara efterföljaren till WebGL och erbjuder flera viktiga förbättringar:

1. **Kompatibilitet med moderna GPU:er**: WebGPU är byggt för att fungera sömlöst med samtida GPU-arkitekturer och använder system-API:er som Vulkan, Metal och Direct3D 12.
2. **Förbättrad prestanda**: Det stödjer allmänna GPU-beräkningar och snabbare operationer, vilket gör det lämpligt för både grafikrendering och maskininlärningsuppgifter.
3. **Avancerade funktioner**: WebGPU ger tillgång till mer avancerade GPU-funktioner och möjliggör mer komplexa och dynamiska grafik- och beräkningsarbetsflöden.
4. **Minskad JavaScript-belastning**: Genom att överföra fler uppgifter till GPU:n minskar WebGPU avsevärt belastningen på JavaScript, vilket leder till bättre prestanda och smidigare upplevelser.

WebGPU stöds för närvarande i webbläsare som Google Chrome, med pågående arbete för att utöka stödet till andra plattformar.

### 03.WebGPU
Nödvändig miljö:

**Stödda webbläsare:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Aktivera WebGPU:

- I Chrome/Microsoft Edge 

Aktivera `chrome://flags/#enable-unsafe-webgpu`-flaggan.

#### Öppna din webbläsare:
Starta Google Chrome eller Microsoft Edge.

#### Gå till flaggsidan:
Skriv `chrome://flags` i adressfältet och tryck på Enter.

#### Sök efter flaggan:
Skriv 'enable-unsafe-webgpu' i sökrutan högst upp på sidan.

#### Aktivera flaggan:
Hitta flaggan #enable-unsafe-webgpu i resultatlistan.

Klicka på rullgardinsmenyn bredvid och välj Enabled.

#### Starta om din webbläsare:

Efter att ha aktiverat flaggan måste du starta om din webbläsare för att ändringarna ska börja gälla. Klicka på knappen "Relaunch" som visas längst ner på sidan.

- För Linux, starta webbläsaren med `--enable-features=Vulkan`.
- Safari 18 (macOS 15) har WebGPU aktiverat som standard.
- I Firefox Nightly, skriv about:config i adressfältet och `set dom.webgpu.enabled to true`.

### Ställa in GPU för Microsoft Edge 

Här är stegen för att ställa in en högpresterande GPU för Microsoft Edge på Windows:

- **Öppna Inställningar:** Klicka på Start-menyn och välj Inställningar.
- **Systeminställningar:** Gå till System och sedan Bildskärm.
- **Grafikinställningar:** Bläddra ner och klicka på Grafikinställningar.
- **Välj App:** Under “Välj en app för att ange preferens,” välj Desktop-app och sedan Bläddra.
- **Välj Edge:** Navigera till Edge-installationsmappen (vanligtvis `C:\Program Files (x86)\Microsoft\Edge\Application`) och välj `msedge.exe`.
- **Ange preferens:** Klicka på Alternativ, välj Hög prestanda och klicka sedan på Spara.
Detta säkerställer att Microsoft Edge använder din högpresterande GPU för bättre prestanda. 
- **Starta om** din dator för att dessa inställningar ska börja gälla.

### Öppna din Codespace:
Navigera till ditt repository på GitHub.
Klicka på knappen Code och välj Open with Codespaces.

Om du inte har en Codespace ännu kan du skapa en genom att klicka på New codespace.

**Notera** Installera Node-miljö i din Codespace
Att köra en npm-demo från en GitHub Codespace är ett utmärkt sätt att testa och utveckla ditt projekt. Här är en steg-för-steg-guide för att hjälpa dig komma igång:

### Ställ in din miljö:
När din Codespace är öppen, se till att du har Node.js och npm installerade. Du kan kontrollera detta genom att köra:
```
node -v
```
```
npm -v
```

Om de inte är installerade kan du installera dem med:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigera till din projektkatalog:
Använd terminalen för att navigera till katalogen där ditt npm-projekt finns:
```
cd path/to/your/project
```

### Installera beroenden:
Kör följande kommando för att installera alla nödvändiga beroenden som anges i din package.json-fil:

```
npm install
```

### Kör demon:
När beroendena är installerade kan du köra ditt demoskript. Detta anges vanligtvis i scripts-sektionen av din package.json. Om ditt demoskript till exempel heter start kan du köra:

```
npm run build
```
```
npm run dev
```

### Kom åt demon:
Om din demo involverar en webbserver kommer Codespaces att ge en URL för att komma åt den. Leta efter en notifikation eller kontrollera fliken Ports för att hitta URL:en.

**Notera:** Modellen måste cachelagras i webbläsaren, så det kan ta lite tid att ladda.

### RAG Demo
Ladda upp markdown-filen `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Välj din fil:
Klicka på knappen som säger “Choose File” för att välja det dokument du vill ladda upp.

### Ladda upp dokumentet:
Efter att ha valt din fil, klicka på knappen “Upload” för att ladda upp ditt dokument för RAG (Retrieval-Augmented Generation).

### Starta din chatt:
När dokumentet är uppladdat kan du starta en chattsession med RAG baserat på innehållet i ditt dokument.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.