# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo para ipakita ang WebGPU at RAG Pattern

Ang RAG Pattern gamit ang Phi-3.5 Onnx Hosted model ay gumagamit ng Retrieval-Augmented Generation na pamamaraan, pinagsasama ang kakayahan ng mga Phi-3.5 models sa ONNX hosting para sa mas episyenteng AI deployments. Ang pattern na ito ay mahalaga sa pagpapahusay ng mga modelo para sa mga espesipikong gawain sa isang larangan, nag-aalok ng kombinasyon ng kalidad, pagiging cost-effective, at mas malawak na pag-unawa sa konteksto. Bahagi ito ng Azure AI suite, na nag-aalok ng malawak na seleksyon ng mga modelong madaling hanapin, subukan, at gamitin, na tumutugon sa mga pangangailangan ng iba’t ibang industriya.

## Ano ang WebGPU 
Ang WebGPU ay isang makabagong web graphics API na dinisenyo upang magbigay ng episyenteng akses sa graphics processing unit (GPU) ng isang device nang direkta mula sa mga web browser. Layunin nitong maging kahalili ng WebGL, na may mga sumusunod na pangunahing pagpapabuti:

1. **Pagkakatugma sa Makabagong GPUs**: Ang WebGPU ay ginawa upang gumana nang maayos sa mga kontemporaryong GPU architectures, gamit ang mga system API tulad ng Vulkan, Metal, at Direct3D 12.
2. **Pinahusay na Performance**: Sinusuportahan nito ang general-purpose GPU computations at mas mabilis na operasyon, na angkop para sa parehong graphics rendering at mga gawain sa machine learning.
3. **Mga Advanced na Katangian**: Nagbibigay ang WebGPU ng akses sa mas advanced na kakayahan ng GPU, na nagpapahintulot ng mas komplikado at dinamikong graphics at computational workloads.
4. **Bawas na JavaScript Workload**: Sa pamamagitan ng pag-offload ng mas maraming gawain sa GPU, malaki ang nababawasan ang workload sa JavaScript, na nagdudulot ng mas magandang performance at mas maayos na karanasan.

Sa kasalukuyan, sinusuportahan ang WebGPU sa mga browser tulad ng Google Chrome, at patuloy ang mga pagsisikap na palawakin ang suporta nito sa iba pang mga platform.

### 03.WebGPU
Kailangan na Kapaligiran:

**Mga Sinusuportahang Browser:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Paganahin ang WebGPU:

- Sa Chrome/Microsoft Edge 

Paganahin ang `chrome://flags/#enable-unsafe-webgpu` flag.

#### Buksan ang Iyong Browser:
Ilunsad ang Google Chrome o Microsoft Edge.

#### Pumunta sa Flags Page:
Sa address bar, i-type ang `chrome://flags` at pindutin ang Enter.

#### Hanapin ang Flag:
Sa search box sa itaas ng pahina, i-type ang 'enable-unsafe-webgpu'

#### Paganahin ang Flag:
Hanapin ang #enable-unsafe-webgpu flag sa listahan ng mga resulta.

I-click ang dropdown menu sa tabi nito at piliin ang Enabled.

#### I-restart ang Iyong Browser:

Pagkatapos paganahin ang flag, kakailanganin mong i-restart ang iyong browser upang magkabisa ang mga pagbabago. I-click ang Relauch button na lilitaw sa ibaba ng pahina.

- Para sa Linux, ilunsad ang browser gamit ang `--enable-features=Vulkan`.
- Ang Safari 18 (macOS 15) ay may naka-enable na WebGPU bilang default.
- Sa Firefox Nightly, i-type ang about:config sa address bar at `set dom.webgpu.enabled to true`.

### Pagsasaayos ng GPU para sa Microsoft Edge 

Narito ang mga hakbang upang i-set up ang high-performance GPU para sa Microsoft Edge sa Windows:

- **Buksan ang Settings:** I-click ang Start menu at piliin ang Settings.
- **System Settings:** Pumunta sa System at pagkatapos ay Display.
- **Graphics Settings:** Mag-scroll pababa at i-click ang Graphics settings.
- **Piliin ang App:** Sa ilalim ng “Choose an app to set preference,” piliin ang Desktop app at pagkatapos ay Browse.
- **Piliin ang Edge:** Hanapin ang Edge installation folder (karaniwang `C:\Program Files (x86)\Microsoft\Edge\Application`) at piliin ang `msedge.exe`.
- **I-set ang Preference:** I-click ang Options, piliin ang High performance, at pagkatapos ay i-click ang Save.
Titiyakin nito na ginagamit ng Microsoft Edge ang iyong high-performance GPU para sa mas magandang performance.
- **I-restart** ang iyong computer upang magkabisa ang mga setting na ito.

### Mga Halimbawa: Pakibisita ang [link na ito](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Bagamat aming sinisikap na maging wasto, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.