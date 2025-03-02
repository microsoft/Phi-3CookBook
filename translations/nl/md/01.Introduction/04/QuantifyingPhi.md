# **Kwantiseren van de Phi-familie**

Modelkwantisatie verwijst naar het proces waarbij de parameters (zoals gewichten en activatiewaarden) in een neuraal netwerkmodel worden omgezet van een groot waardebereik (meestal een continu waardebereik) naar een kleiner, eindig waardebereik. Deze technologie kan de grootte en rekencomplexiteit van het model verminderen en de efficiëntie van het model verbeteren in omgevingen met beperkte middelen, zoals mobiele apparaten of embedded systemen. Modelkwantisatie bereikt compressie door de precisie van parameters te verlagen, maar dit brengt ook een zekere mate van precisieverlies met zich mee. Daarom is het tijdens het kwantisatieproces nodig om een balans te vinden tussen modelgrootte, rekencomplexiteit en precisie. Veelgebruikte kwantisatiemethoden zijn onder andere fixed-point kwantisatie, floating-point kwantisatie, enz. Je kunt de juiste kwantisatiestrategie kiezen afhankelijk van het specifieke scenario en de behoeften.

We hopen het GenAI-model te kunnen inzetten op edge-apparaten en meer apparaten toegang te geven tot GenAI-scenario's, zoals mobiele apparaten, AI PC/Copilot+PC en traditionele IoT-apparaten. Door het kwantisatiemodel kunnen we het inzetten op verschillende edge-apparaten, afhankelijk van de verschillende apparaten. Gecombineerd met het modelversnellingsframework en het kwantisatiemodel dat door hardwarefabrikanten wordt aangeboden, kunnen we betere SLM-toepassingsscenario's bouwen.

In het kwantisatiescenario hebben we verschillende precisieniveaus (INT4, INT8, FP16, FP32). Hieronder volgt een uitleg van de veelgebruikte kwantisatieprecisies.

### **INT4**

INT4-kwantisatie is een radicale kwantisatiemethode waarbij de gewichten en activatiewaarden van het model worden gekwantiseerd naar 4-bits gehele getallen. INT4-kwantisatie resulteert meestal in een groter precisieverlies vanwege het kleinere representatiebereik en de lagere precisie. Vergeleken met INT8-kwantisatie kan INT4-kwantisatie echter de opslagvereisten en de rekencomplexiteit van het model verder verminderen. Het is belangrijk op te merken dat INT4-kwantisatie relatief zeldzaam is in praktische toepassingen, omdat een te lage precisie kan leiden tot aanzienlijke degradatie van de modelprestaties. Bovendien ondersteunt niet alle hardware INT4-bewerkingen, dus hardwarecompatibiliteit moet in overweging worden genomen bij het kiezen van een kwantisatiemethode.

### **INT8**

INT8-kwantisatie is het proces waarbij de gewichten en activaties van een model worden omgezet van zwevendekommagetallen naar 8-bits gehele getallen. Hoewel het numerieke bereik dat door INT8-getallen wordt vertegenwoordigd kleiner en minder precies is, kan het de opslag- en rekenvereisten aanzienlijk verminderen. Bij INT8-kwantisatie doorlopen de gewichten en activatiewaarden van het model een kwantisatieproces, inclusief schaalvergroting en offset, om de oorspronkelijke zwevendekommagegevens zo goed mogelijk te behouden. Tijdens inferentie worden deze gekwantiseerde waarden gedequantiseerd terug naar zwevendekommagetallen voor berekeningen en vervolgens opnieuw gekwantiseerd naar INT8 voor de volgende stap. Deze methode kan in de meeste toepassingen voldoende precisie bieden, terwijl een hoge rekenefficiëntie behouden blijft.

### **FP16**

Het FP16-formaat, oftewel 16-bits zwevendekommagetallen (float16), halveert de geheugengebruik in vergelijking met 32-bits zwevendekommagetallen (float32), wat aanzienlijke voordelen biedt bij grootschalige deep learning-toepassingen. Het FP16-formaat maakt het mogelijk om grotere modellen te laden of meer gegevens te verwerken binnen dezelfde GPU-geheugenlimieten. Naarmate moderne GPU-hardware steeds meer FP16-bewerkingen ondersteunt, kan het gebruik van het FP16-formaat ook verbeteringen in rekenprestaties opleveren. Het FP16-formaat heeft echter ook inherente nadelen, namelijk een lagere precisie, wat kan leiden tot numerieke instabiliteit of precisieverlies in sommige gevallen.

### **FP32**

Het FP32-formaat biedt een hogere precisie en kan een breed scala aan waarden nauwkeurig vertegenwoordigen. In scenario's waarin complexe wiskundige bewerkingen worden uitgevoerd of hoge precisieresultaten vereist zijn, heeft het FP32-formaat de voorkeur. Hogere precisie betekent echter ook meer geheugengebruik en langere rekentijd. Voor grootschalige deep learning-modellen, vooral wanneer er veel modelparameters en een enorme hoeveelheid gegevens zijn, kan het FP32-formaat leiden tot onvoldoende GPU-geheugen of een afname van de inferentiesnelheid.

Op mobiele apparaten of IoT-apparaten kunnen we Phi-3.x-modellen converteren naar INT4, terwijl AI PC / Copilot PC hogere precisies zoals INT8, FP16 of FP32 kan gebruiken.

Momenteel hebben verschillende hardwarefabrikanten verschillende frameworks om generatieve modellen te ondersteunen, zoals Intel's OpenVINO, Qualcomm's QNN, Apple's MLX en Nvidia's CUDA. Gecombineerd met modelkwantisatie kan dit zorgen voor lokale implementatie.

Wat technologie betreft, hebben we na kwantisatie verschillende formaten die worden ondersteund, zoals PyTorch/Tensorflow-formaten, GGUF en ONNX. Ik heb een vergelijking gemaakt tussen GGUF en ONNX en hun toepassingsscenario's. Hier raad ik het ONNX-kwantisatieformaat aan, dat goede ondersteuning biedt van het modelframework tot de hardware. In dit hoofdstuk richten we ons op ONNX Runtime voor GenAI, OpenVINO en Apple MLX om modelkwantisatie uit te voeren (als je een betere methode hebt, kun je deze ook indienen via een PR).

**Dit hoofdstuk bevat**

1. [Kwantiseren van Phi-3.5 / 4 met behulp van llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kwantiseren van Phi-3.5 / 4 met behulp van Generative AI-uitbreidingen voor onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kwantiseren van Phi-3.5 / 4 met behulp van Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kwantiseren van Phi-3.5 / 4 met behulp van Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet verantwoordelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.