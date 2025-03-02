# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo för att visa WebGPU och RAG-mönster

RAG-mönstret med Phi-3.5 Onnx Hosted-modellen använder sig av Retrieval-Augmented Generation-metoden, som kombinerar kraften hos Phi-3.5-modeller med ONNX-hosting för effektiva AI-distributioner. Detta mönster är avgörande för att finjustera modeller för uppgiftsspecifika behov och erbjuder en kombination av kvalitet, kostnadseffektivitet och förståelse för längre kontexter. Det är en del av Azure AI:s verktygssvit, som erbjuder ett brett urval av modeller som är enkla att hitta, testa och använda, och som kan anpassas för olika branschers behov.

## Vad är WebGPU
WebGPU är ett modernt webbgrafik-API som är utformat för att ge effektiv åtkomst till en enhets grafikprocessor (GPU) direkt från webbläsare. Det är tänkt att ersätta WebGL och erbjuder flera viktiga förbättringar:

1. **Kompatibilitet med moderna GPU:er**: WebGPU är utformat för att fungera sömlöst med moderna GPU-arkitekturer och använder system-API:er som Vulkan, Metal och Direct3D 12.
2. **Förbättrad prestanda**: Det stödjer allmänna GPU-beräkningar och snabbare operationer, vilket gör det lämpligt för både grafikrendering och maskininlärningsuppgifter.
3. **Avancerade funktioner**: WebGPU ger åtkomst till mer avancerade GPU-funktioner, vilket möjliggör mer komplexa och dynamiska grafik- och beräkningsarbetsbelastningar.
4. **Minskad JavaScript-belastning**: Genom att flytta fler uppgifter till GPU:n minskar WebGPU avsevärt belastningen på JavaScript, vilket leder till bättre prestanda och smidigare upplevelser.

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

#### Gå till flags-sidan:
Skriv `chrome://flags` i adressfältet och tryck på Enter.

#### Sök efter flaggan:
Skriv 'enable-unsafe-webgpu' i sökrutan högst upp på sidan.

#### Aktivera flaggan:
Hitta flaggan #enable-unsafe-webgpu i resultatlistan.

Klicka på rullgardinsmenyn bredvid den och välj Enabled.

#### Starta om din webbläsare:

Efter att ha aktiverat flaggan måste du starta om din webbläsare för att ändringarna ska träda i kraft. Klicka på knappen Relaunch som visas längst ner på sidan.

- För Linux, starta webbläsaren med `--enable-features=Vulkan`.
- Safari 18 (macOS 15) har WebGPU aktiverat som standard.
- I Firefox Nightly, skriv about:config i adressfältet och `set dom.webgpu.enabled to true`.

### Ställa in GPU för Microsoft Edge 

Här är stegen för att ställa in en högpresterande GPU för Microsoft Edge på Windows:

- **Öppna inställningar:** Klicka på Start-menyn och välj Inställningar.
- **Systeminställningar:** Gå till System och sedan Bildskärm.
- **Grafikinställningar:** Scrolla ner och klicka på Grafikinställningar.
- **Välj app:** Under "Välj en app för att ställa in preferens," välj Desktop app och klicka sedan på Bläddra.
- **Välj Edge:** Navigera till Edge-installationsmappen (vanligtvis `C:\Program Files (x86)\Microsoft\Edge\Application`) och välj `msedge.exe`.
- **Ställ in preferens:** Klicka på Alternativ, välj Hög prestanda och klicka sedan på Spara.
Detta säkerställer att Microsoft Edge använder din högpresterande GPU för bättre prestanda. 
- **Starta om** datorn för att dessa inställningar ska träda i kraft.

### Exempel: Vänligen [klicka på denna länk](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på sitt ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.