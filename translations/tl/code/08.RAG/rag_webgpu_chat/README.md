Phi-3-mini WebGPU RAG Chatbot

## Demo para sa pagpapakita ng WebGPU at RAG Pattern
Ang RAG Pattern gamit ang Phi-3 Onnx Hosted model ay gumagamit ng Retrieval-Augmented Generation na pamamaraan, pinagsasama ang kakayahan ng Phi-3 models at ONNX hosting para sa mahusay na AI deployments. Mahalaga ang pattern na ito sa pag-fine-tune ng mga modelo para sa mga partikular na gawain sa industriya, nag-aalok ng kombinasyon ng kalidad, pagiging cost-effective, at malalim na pag-unawa sa konteksto. Bahagi ito ng Azure AI suite, na nagbibigay ng malawak na seleksyon ng mga modelong madaling hanapin, subukan, at gamitin, na tumutugon sa mga pangangailangan ng iba't ibang industriya. Ang mga Phi-3 models, kabilang ang Phi-3-mini, Phi-3-small, at Phi-3-medium, ay makukuha sa Azure AI Model Catalog at maaaring i-fine-tune at i-deploy nang self-managed o sa pamamagitan ng mga platform tulad ng HuggingFace at ONNX, na nagpapakita ng dedikasyon ng Microsoft sa accessible at mahusay na AI solutions.

## Ano ang WebGPU
Ang WebGPU ay isang modernong web graphics API na idinisenyo upang magbigay ng epektibong access sa graphics processing unit (GPU) ng isang device direkta mula sa mga web browser. Ito ang itinuturing na kapalit ng WebGL, na may ilang mahahalagang pagpapabuti:

1. **Compatibility sa Makabagong GPUs**: Ang WebGPU ay binuo upang gumana nang maayos sa mga makabagong GPU architectures, gamit ang system APIs tulad ng Vulkan, Metal, at Direct3D 12.
2. **Pinahusay na Performance**: Sinusuportahan nito ang general-purpose GPU computations at mas mabilis na operasyon, na angkop para sa parehong graphics rendering at machine learning tasks.
3. **Advanced na Mga Tampok**: Nagbibigay ang WebGPU ng access sa mas advanced na GPU capabilities, na nagpapahintulot ng mas kumplikado at dinamikong graphics at computational workloads.
4. **Pinababang JavaScript Workload**: Sa pamamagitan ng pag-offload ng mas maraming gawain sa GPU, lubos na nababawasan ang workload sa JavaScript, na nagreresulta sa mas mahusay na performance at mas maayos na karanasan.

Sa kasalukuyan, sinusuportahan ang WebGPU sa mga browser tulad ng Google Chrome, at patuloy ang pag-develop para mapalawak ang suporta sa iba pang mga platform.

### 03.WebGPU
Kinakailangang Kapaligiran:

**Sinusuportahang mga browser:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Paganahin ang WebGPU:

- Sa Chrome/Microsoft Edge 

Paganahin ang `chrome://flags/#enable-unsafe-webgpu` flag.

#### Buksan ang Iyong Browser:
Ilunsad ang Google Chrome o Microsoft Edge.

#### I-access ang Flags Page:
Sa address bar, i-type ang `chrome://flags` at pindutin ang Enter.

#### Hanapin ang Flag:
Sa search box sa itaas ng pahina, i-type ang 'enable-unsafe-webgpu'

#### I-enable ang Flag:
Hanapin ang #enable-unsafe-webgpu flag sa listahan ng mga resulta.

I-click ang dropdown menu sa tabi nito at piliin ang Enabled.

#### I-restart ang Iyong Browser:

Pagkatapos paganahin ang flag, kailangang i-restart ang iyong browser para magkabisa ang mga pagbabago. I-click ang Relauch button na lilitaw sa ibaba ng pahina.

- Para sa Linux, ilunsad ang browser gamit ang `--enable-features=Vulkan`.
- Ang Safari 18 (macOS 15) ay may WebGPU na naka-enable bilang default.
- Sa Firefox Nightly, i-type ang about:config sa address bar at `set dom.webgpu.enabled to true`.

### Pag-set up ng GPU para sa Microsoft Edge 

Narito ang mga hakbang para i-set up ang high-performance GPU para sa Microsoft Edge sa Windows:

- **Buksan ang Settings:** I-click ang Start menu at piliin ang Settings.
- **System Settings:** Pumunta sa System at pagkatapos ay Display.
- **Graphics Settings:** Mag-scroll pababa at i-click ang Graphics settings.
- **Piliin ang App:** Sa ilalim ng “Choose an app to set preference,” piliin ang Desktop app at pagkatapos ay Browse.
- **Piliin ang Edge:** Pumunta sa Edge installation folder (karaniwang `C:\Program Files (x86)\Microsoft\Edge\Application`) at piliin ang `msedge.exe`.
- **I-set ang Preference:** I-click ang Options, piliin ang High performance, at pagkatapos ay i-click ang Save.
Ito ay titiyakin na ginagamit ng Microsoft Edge ang iyong high-performance GPU para sa mas mahusay na performance. 
- **I-restart** ang iyong makina para magkabisa ang mga setting na ito.

### Buksan ang Iyong Codespace:
Pumunta sa iyong repositoryo sa GitHub.
I-click ang Code button at piliin ang Open with Codespaces.

Kung wala ka pang Codespace, maaari kang gumawa ng bago sa pamamagitan ng pag-click sa New codespace.

**Tandaan** Pag-install ng Node Environment sa iyong codespace
Ang pagpapatakbo ng npm demo mula sa isang GitHub Codespace ay isang mahusay na paraan upang subukan at i-develop ang iyong proyekto. Narito ang step-by-step na gabay upang makapagsimula:

### I-set Up ang Iyong Environment:
Kapag bukas na ang iyong Codespace, tiyakin na naka-install ang Node.js at npm. Maaari mong suriin ito sa pamamagitan ng pagpapatakbo ng:
```
node -v
```
```
npm -v
```

Kung hindi pa naka-install, maaari mo itong i-install gamit ang:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Mag-navigate sa Iyong Project Directory:
Gamitin ang terminal upang pumunta sa directory kung saan matatagpuan ang iyong npm project:
```
cd path/to/your/project
```

### I-install ang Dependencies:
Patakbuhin ang sumusunod na command upang i-install ang lahat ng kinakailangang dependencies na nakalista sa iyong package.json file:

```
npm install
```

### Patakbuhin ang Demo:
Kapag naka-install na ang mga dependencies, maaari mong patakbuhin ang iyong demo script. Karaniwan itong tinutukoy sa scripts section ng iyong package.json. Halimbawa, kung ang pangalan ng iyong demo script ay start, maaari mo itong patakbuhin gamit ang:

```
npm run build
```
```
npm run dev
```

### I-access ang Demo:
Kung ang iyong demo ay may kinalaman sa isang web server, magbibigay ang Codespaces ng URL upang ma-access ito. Hanapin ang notification o tingnan ang Ports tab upang makita ang URL.

**Tandaan:** Kailangang ma-cache ang modelo sa browser, kaya maaaring magtagal bago ito mag-load. 

### RAG Demo
I-upload ang markdown file na `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Piliin ang Iyong File:
I-click ang button na “Choose File” upang piliin ang dokumentong nais mong i-upload.

### I-upload ang Dokumento:
Pagkatapos piliin ang iyong file, i-click ang “Upload” button upang i-load ang iyong dokumento para sa RAG (Retrieval-Augmented Generation).

### Simulan ang Iyong Chat:
Kapag na-upload na ang dokumento, maaari kang magsimula ng chat session gamit ang RAG batay sa nilalaman ng iyong dokumento.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Bagamat pinagsisikapan naming maging wasto, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na salin. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.