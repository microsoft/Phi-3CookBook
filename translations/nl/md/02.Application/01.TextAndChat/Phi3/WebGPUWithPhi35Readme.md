# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo ter demonstratie van WebGPU en het RAG-patroon

Het RAG-patroon met het Phi-3.5 Onnx Hosted-model maakt gebruik van de Retrieval-Augmented Generation-methode, waarbij de kracht van Phi-3.5-modellen wordt gecombineerd met ONNX-hosting voor efficiënte AI-implementaties. Dit patroon is essentieel voor het verfijnen van modellen voor domeinspecifieke taken en biedt een combinatie van kwaliteit, kosteneffectiviteit en begrip van lange contexten. Het maakt deel uit van de Azure AI-suite, die een brede selectie van modellen biedt die eenvoudig te vinden, uit te proberen en te gebruiken zijn, afgestemd op de aanpassingsbehoeften van verschillende industrieën.

## Wat is WebGPU 
WebGPU is een moderne webgrafische API die is ontworpen om efficiënte toegang te bieden tot de grafische verwerkingsunit (GPU) van een apparaat, rechtstreeks vanuit webbrowsers. Het is bedoeld als opvolger van WebGL en biedt verschillende belangrijke verbeteringen:

1. **Compatibiliteit met moderne GPU's**: WebGPU is ontwikkeld om naadloos samen te werken met hedendaagse GPU-architecturen en maakt gebruik van systeem-API's zoals Vulkan, Metal en Direct3D 12.
2. **Verbeterde prestaties**: Het ondersteunt algemene GPU-berekeningen en snellere operaties, waardoor het geschikt is voor zowel grafische rendering als machine learning-taken.
3. **Geavanceerde functies**: WebGPU biedt toegang tot meer geavanceerde GPU-mogelijkheden, wat complexere en dynamische grafische en computationele workloads mogelijk maakt.
4. **Verminderde belasting van JavaScript**: Door meer taken naar de GPU te verplaatsen, vermindert WebGPU aanzienlijk de belasting op JavaScript, wat leidt tot betere prestaties en soepelere ervaringen.

WebGPU wordt momenteel ondersteund in browsers zoals Google Chrome, met lopend werk om ondersteuning uit te breiden naar andere platforms.

### 03.WebGPU
Vereiste omgeving:

**Ondersteunde browsers:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU inschakelen:

- In Chrome/Microsoft Edge 

Schakel de `chrome://flags/#enable-unsafe-webgpu`-vlag in.

#### Open uw browser:
Start Google Chrome of Microsoft Edge.

#### Ga naar de Flags-pagina:
Typ `chrome://flags` in de adresbalk en druk op Enter.

#### Zoek de vlag:
Typ in het zoekvak bovenaan de pagina 'enable-unsafe-webgpu'.

#### Schakel de vlag in:
Zoek de #enable-unsafe-webgpu-vlag in de lijst met resultaten.

Klik op het dropdownmenu ernaast en selecteer Enabled.

#### Herstart uw browser:

Na het inschakelen van de vlag moet u uw browser opnieuw starten om de wijzigingen door te voeren. Klik op de knop Relaunch die onderaan de pagina verschijnt.

- Voor Linux, start de browser met `--enable-features=Vulkan`.
- Safari 18 (macOS 15) heeft WebGPU standaard ingeschakeld.
- In Firefox Nightly, voer about:config in de adresbalk in en `set dom.webgpu.enabled to true`.

### GPU instellen voor Microsoft Edge 

Hier zijn de stappen om een high-performance GPU in te stellen voor Microsoft Edge op Windows:

- **Open Instellingen:** Klik op het Startmenu en selecteer Instellingen.
- **Systeeminstellingen:** Ga naar Systeem en vervolgens naar Beeldscherm.
- **Grafische instellingen:** Scroll naar beneden en klik op Grafische instellingen.
- **App kiezen:** Onder “Kies een app om voorkeur in te stellen,” selecteer Desktop-app en klik vervolgens op Bladeren.
- **Selecteer Edge:** Navigeer naar de installatie-map van Edge (meestal `C:\Program Files (x86)\Microsoft\Edge\Application`) en selecteer `msedge.exe`.
- **Stel voorkeur in:** Klik op Opties, kies Hoge prestaties en klik vervolgens op Opslaan.
Dit zorgt ervoor dat Microsoft Edge uw high-performance GPU gebruikt voor betere prestaties. 
- **Herstart** uw apparaat om deze instellingen door te voeren.

### Voorbeelden: Klik [op deze link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer**:  
Dit document is vertaald met behulp van AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of onjuiste interpretaties die voortvloeien uit het gebruik van deze vertaling.