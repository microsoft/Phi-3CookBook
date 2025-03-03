Phi-3-mini WebGPU RAG Chatbot

## Demo om WebGPU en RAG-patroon te tonen
Het RAG-patroon met het Phi-3 Onnx Hosted-model maakt gebruik van de Retrieval-Augmented Generation-benadering, waarbij de kracht van Phi-3-modellen wordt gecombineerd met ONNX-hosting voor efficiënte AI-implementaties. Dit patroon is cruciaal voor het verfijnen van modellen voor domeinspecifieke taken en biedt een mix van kwaliteit, kosteneffectiviteit en begrip van lange contexten. Het maakt deel uit van de Azure AI-suite, die een breed scala aan modellen biedt die eenvoudig te vinden, te proberen en te gebruiken zijn, afgestemd op de behoeften van verschillende sectoren. De Phi-3-modellen, waaronder Phi-3-mini, Phi-3-small en Phi-3-medium, zijn beschikbaar in de Azure AI Model Catalog en kunnen worden verfijnd en zelf beheerd geïmplementeerd of via platforms zoals HuggingFace en ONNX, wat Microsofts toewijding aan toegankelijke en efficiënte AI-oplossingen benadrukt.

## Wat is WebGPU
WebGPU is een moderne webgraphics-API die is ontworpen om efficiënte toegang te bieden tot de grafische verwerkingseenheid (GPU) van een apparaat rechtstreeks vanuit webbrowsers. Het is bedoeld als opvolger van WebGL en biedt verschillende belangrijke verbeteringen:

1. **Compatibiliteit met moderne GPU's**: WebGPU is ontworpen om naadloos samen te werken met hedendaagse GPU-architecturen en maakt gebruik van systeem-API's zoals Vulkan, Metal en Direct3D 12.
2. **Verbeterde prestaties**: Het ondersteunt GPU-berekeningen voor algemene doeleinden en snellere bewerkingen, waardoor het geschikt is voor zowel graphics rendering als machine learning-taken.
3. **Geavanceerde functies**: WebGPU biedt toegang tot meer geavanceerde GPU-mogelijkheden, wat complexere en dynamischere graphics en computationele workloads mogelijk maakt.
4. **Verminderde JavaScript-belasting**: Door meer taken naar de GPU te verplaatsen, vermindert WebGPU de belasting op JavaScript aanzienlijk, wat leidt tot betere prestaties en soepelere ervaringen.

WebGPU wordt momenteel ondersteund in browsers zoals Google Chrome, met lopend werk om ondersteuning uit te breiden naar andere platforms.

### 03.WebGPU
Benodigde omgeving:

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

#### Ga naar de vlaggenpagina:
Typ `chrome://flags` in de adresbalk en druk op Enter.

#### Zoek de vlag:
Typ 'enable-unsafe-webgpu' in het zoekvak bovenaan de pagina.

#### Schakel de vlag in:
Zoek de vlag #enable-unsafe-webgpu in de lijst met resultaten.

Klik op het dropdownmenu ernaast en selecteer Enabled.

#### Herstart uw browser:

Na het inschakelen van de vlag moet u uw browser opnieuw starten om de wijzigingen door te voeren. Klik op de knop Relaunch die onderaan de pagina verschijnt.

- Voor Linux start u de browser met `--enable-features=Vulkan`.
- Safari 18 (macOS 15) heeft WebGPU standaard ingeschakeld.
- In Firefox Nightly typt u about:config in de adresbalk en `set dom.webgpu.enabled to true`.

### GPU instellen voor Microsoft Edge 

Hier zijn de stappen om een GPU met hoge prestaties in te stellen voor Microsoft Edge op Windows:

- **Open Instellingen:** Klik op het Startmenu en selecteer Instellingen.
- **Systeeminstellingen:** Ga naar Systeem en vervolgens naar Beeldscherm.
- **Grafische instellingen:** Scroll naar beneden en klik op Grafische instellingen.
- **Kies app:** Selecteer onder "Een app kiezen om voorkeur in te stellen" de optie Desktop app en klik op Bladeren.
- **Selecteer Edge:** Navigeer naar de installatiemap van Edge (meestal `C:\Program Files (x86)\Microsoft\Edge\Application`) en selecteer `msedge.exe`.
- **Stel voorkeur in:** Klik op Opties, kies Hoge prestaties en klik vervolgens op Opslaan.
Dit zorgt ervoor dat Microsoft Edge uw GPU met hoge prestaties gebruikt voor betere prestaties.
- **Herstart** uw computer om deze instellingen door te voeren.

### Open uw Codespace:
Navigeer naar uw repository op GitHub.
Klik op de knop Code en selecteer Open met Codespaces.

Als u nog geen Codespace heeft, kunt u er een maken door op Nieuwe codespace te klikken.

**Opmerking** Het installeren van een Node-omgeving in uw codespace
Een npm-demo uitvoeren vanuit een GitHub Codespace is een geweldige manier om uw project te testen en te ontwikkelen. Hier is een stapsgewijze handleiding om u op weg te helpen:

### Stel uw omgeving in:
Zodra uw Codespace is geopend, controleert u of Node.js en npm zijn geïnstalleerd. U kunt dit controleren door het volgende uit te voeren:
```
node -v
```
```
npm -v
```

Als ze niet zijn geïnstalleerd, kunt u ze installeren met:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigeer naar uw projectmap:
Gebruik de terminal om naar de map te navigeren waar uw npm-project zich bevindt:
```
cd path/to/your/project
```

### Installeer afhankelijkheden:
Voer de volgende opdracht uit om alle benodigde afhankelijkheden te installeren die in uw package.json-bestand zijn vermeld:

```
npm install
```

### Voer de demo uit:
Zodra de afhankelijkheden zijn geïnstalleerd, kunt u uw demoscript uitvoeren. Dit wordt meestal gespecificeerd in het scriptsgedeelte van uw package.json. Als uw demoscript bijvoorbeeld start heet, kunt u het uitvoeren met:

```
npm run build
```
```
npm run dev
```

### Open de demo:
Als uw demo een webserver omvat, biedt Codespaces een URL om er toegang toe te krijgen. Zoek naar een melding of controleer het tabblad Poorten om de URL te vinden.

**Opmerking:** Het model moet in de browser worden gecachet, dus het kan enige tijd duren om te laden.

### RAG-demo
Upload het markdown-bestand `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecteer uw bestand:
Klik op de knop met de tekst "Bestand kiezen" om het document te selecteren dat u wilt uploaden.

### Upload het document:
Klik na het selecteren van uw bestand op de knop "Uploaden" om uw document te laden voor RAG (Retrieval-Augmented Generation).

### Start uw chat:
Zodra het document is geüpload, kunt u een chatsessie starten met RAG op basis van de inhoud van uw document.

**Disclaimer**:  
Dit document is vertaald met behulp van machinegebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.