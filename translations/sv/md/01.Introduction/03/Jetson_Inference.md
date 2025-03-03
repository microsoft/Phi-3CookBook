# **Inferens Phi-3 i Nvidia Jetson**

Nvidia Jetson är en serie inbyggda datorplattformar från Nvidia. Modellerna Jetson TK1, TX1 och TX2 har alla en Tegra-processor (eller SoC) från Nvidia som integrerar en ARM-arkitektur för centralprocessor (CPU). Jetson är ett energieffektivt system och är designat för att accelerera maskininlärningsapplikationer. Nvidia Jetson används av professionella utvecklare för att skapa banbrytande AI-produkter inom alla branscher, samt av studenter och entusiaster för praktisk AI-inlärning och att skapa fantastiska projekt. SLM används i edge-enheter som Jetson, vilket möjliggör bättre implementering av industriella generativa AI-applikationsscenarier.

## Implementering på NVIDIA Jetson:
Utvecklare som arbetar med autonoma robotar och inbyggda enheter kan dra nytta av Phi-3 Mini. Phi-3:s relativt lilla storlek gör den idealisk för edge-implementering. Parametrar har noggrant justerats under träningen för att säkerställa hög noggrannhet i svaren.

### TensorRT-LLM-optimering:
NVIDIAs [TensorRT-LLM-bibliotek](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimerar inferens för stora språkmodeller. Det stödjer Phi-3 Minis långa kontextfönster och förbättrar både genomströmning och latens. Optimeringar inkluderar tekniker som LongRoPE, FP8 och inflight-batchning.

### Tillgänglighet och implementering:
Utvecklare kan utforska Phi-3 Mini med ett 128K-kontextfönster på [NVIDIAs AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Den levereras som en NVIDIA NIM, en mikrotjänst med ett standard-API som kan implementeras var som helst. Dessutom finns [TensorRT-LLM-implementeringar på GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Förberedelser**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

## **2. Köra Phi-3 i Jetson**

Vi kan välja [Ollama](https://ollama.com) eller [LlamaEdge](https://llamaedge.com).

Om du vill använda gguf både i molnet och på edge-enheter samtidigt kan LlamaEdge ses som WasmEdge (WasmEdge är en lättviktig, högpresterande och skalbar WebAssembly-runtime som är lämplig för molnbaserade, edge- och decentraliserade applikationer. Den stödjer serverlösa applikationer, inbäddade funktioner, mikrotjänster, smarta kontrakt och IoT-enheter. Du kan implementera ggufs kvantitativa modell på edge-enheter och i molnet via LlamaEdge).

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.sv.jpg)

Här är stegen för att använda:

1. Installera och ladda ner relaterade bibliotek och filer

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Obs**: llama-api-server.wasm och chatbot-ui behöver vara i samma katalog

2. Kör skript i terminalen

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Här är körningsresultatet:

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.sv.png)

***Exempelkod*** [Phi-3 Mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Sammanfattningsvis representerar Phi-3 Mini ett stort framsteg inom språkmodellering, med en kombination av effektivitet, kontextmedvetenhet och NVIDIAs optimeringsförmåga. Oavsett om du bygger robotar eller edge-applikationer är Phi-3 Mini ett kraftfullt verktyg att känna till.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi tar inget ansvar för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.