In de context van Phi-3-mini verwijst inferentie naar het proces waarbij het model wordt gebruikt om voorspellingen te doen of output te genereren op basis van invoergegevens. Hier zijn meer details over Phi-3-mini en zijn inferentiecapaciteiten.

Phi-3-mini maakt deel uit van de Phi-3-serie modellen die door Microsoft zijn uitgebracht. Deze modellen zijn ontworpen om de mogelijkheden van Small Language Models (SLMs) opnieuw te definiëren.

Hier zijn enkele belangrijke punten over Phi-3-mini en zijn inferentiecapaciteiten:

## **Overzicht van Phi-3-mini:**
- Phi-3-mini heeft een parameterset van 3,8 miljard.
- Het kan niet alleen draaien op traditionele computers, maar ook op edge-apparaten zoals mobiele apparaten en IoT-apparaten.
- Met de release van Phi-3-mini kunnen zowel individuen als bedrijven SLMs implementeren op verschillende hardware-apparaten, vooral in omgevingen met beperkte middelen.
- Het ondersteunt verschillende modelformaten, waaronder het traditionele PyTorch-formaat, de gequantiseerde versie van het gguf-formaat en de op ONNX gebaseerde gequantiseerde versie.

## **Toegang tot Phi-3-mini:**
Om toegang te krijgen tot Phi-3-mini kun je [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) gebruiken in een Copilot-applicatie. Semantic Kernel is over het algemeen compatibel met Azure OpenAI Service, open-source modellen op Hugging Face en lokale modellen.  
Je kunt ook [Ollama](https://ollama.com) of [LlamaEdge](https://llamaedge.com) gebruiken om gequantiseerde modellen aan te roepen. Ollama stelt individuele gebruikers in staat verschillende gequantiseerde modellen aan te roepen, terwijl LlamaEdge cross-platform beschikbaarheid biedt voor GGUF-modellen.

## **Gequantiseerde Modellen:**
Veel gebruikers geven de voorkeur aan het gebruik van gequantiseerde modellen voor lokale inferentie. Bijvoorbeeld, je kunt direct Ollama run Phi-3 uitvoeren of het offline configureren met behulp van een Modelfile. Het Modelfile specificeert het GGUF-bestandspad en het promptformaat.

## **Mogelijkheden van Generatieve AI:**
De combinatie van SLMs zoals Phi-3-mini opent nieuwe mogelijkheden voor generatieve AI. Inferentie is slechts de eerste stap; deze modellen kunnen worden gebruikt voor diverse taken in omgevingen met beperkte middelen, lage latentie en kostenbeperkingen.

## **Generatieve AI Ontgrendelen met Phi-3-mini: Een Gids voor Inferentie en Implementatie**  
Leer hoe je Semantic Kernel, Ollama/LlamaEdge en ONNX Runtime kunt gebruiken om toegang te krijgen tot en inferentie uit te voeren met Phi-3-mini-modellen, en ontdek de mogelijkheden van generatieve AI in verschillende toepassingsscenario's.

**Functies**  
Inferentie van het phi3-mini-model in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Samenvattend stelt Phi-3-mini ontwikkelaars in staat om verschillende modelformaten te verkennen en generatieve AI te benutten in diverse toepassingsscenario's.

**Disclaimer**:  
Dit document is vertaald met behulp van AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, moet u zich ervan bewust zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.