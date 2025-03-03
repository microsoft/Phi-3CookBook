# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo za prikaz WebGPU in RAG vzorca

RAG vzorec z gostovanim modelom Phi-3.5 Onnx uporablja pristop generacije z okrepljenim iskanjem (Retrieval-Augmented Generation), ki združuje zmogljivosti modelov Phi-3.5 z gostovanjem ONNX za učinkovito uvajanje AI. Ta vzorec je ključnega pomena za prilagoditev modelov na naloge specifične za določen domen, saj ponuja kombinacijo kakovosti, stroškovne učinkovitosti in razumevanja dolgega konteksta. Je del nabora Azure AI, ki ponuja širok izbor modelov, ki so enostavni za iskanje, preizkušanje in uporabo, ter ustrezajo potrebam prilagoditve v različnih panogah.

## Kaj je WebGPU 
WebGPU je sodoben spletni grafični API, zasnovan za učinkovito dostopanje do grafičnega procesorja (GPU) naprave neposredno iz spletnih brskalnikov. Namenjen je kot naslednik WebGL, z več ključnimi izboljšavami:

1. **Združljivost z modernimi GPU-ji**: WebGPU je zasnovan za brezhibno delovanje z najnovejšimi GPU arhitekturami, saj uporablja sistemske API-je, kot so Vulkan, Metal in Direct3D 12.
2. **Izboljšana zmogljivost**: Podpira splošne izračune na GPU-ju in hitrejše operacije, kar ga naredi primernega tako za grafično upodabljanje kot za naloge strojnega učenja.
3. **Napredne funkcije**: WebGPU omogoča dostop do naprednejših zmogljivosti GPU, kar omogoča bolj kompleksne in dinamične grafične ter računske delovne obremenitve.
4. **Zmanjšana obremenitev JavaScripta**: Z večjim prenosom nalog na GPU WebGPU znatno zmanjša obremenitev JavaScripta, kar vodi do boljše zmogljivosti in bolj tekoče uporabniške izkušnje.

WebGPU je trenutno podprt v brskalnikih, kot je Google Chrome, medtem ko potekajo prizadevanja za širitev podpore na druge platforme.

### 03.WebGPU
Zahtevano okolje:

**Podprti brskalniki:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogočanje WebGPU:

- V Chrome/Microsoft Edge 

Omogočite zastavico `chrome://flags/#enable-unsafe-webgpu`.

#### Odprite brskalnik:
Zaženite Google Chrome ali Microsoft Edge.

#### Dostop do strani z zastavicami:
V naslovno vrstico vnesite `chrome://flags` in pritisnite Enter.

#### Poiščite zastavico:
V iskalno polje na vrhu strani vnesite 'enable-unsafe-webgpu'.

#### Omogočite zastavico:
Na seznamu rezultatov poiščite zastavico #enable-unsafe-webgpu.

Kliknite spustni meni poleg nje in izberite Enabled.

#### Znova zaženite brskalnik:

Po omogočitvi zastavice boste morali znova zagnati brskalnik, da bodo spremembe začele veljati. Kliknite gumb Relaunch, ki se prikaže na dnu strani.

- Za Linux zaženite brskalnik z `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU privzeto omogočen.
- V Firefox Nightly vnesite about:config v naslovno vrstico in `set dom.webgpu.enabled to true`.

### Nastavitev GPU za Microsoft Edge 

Tukaj so koraki za nastavitev zmogljivega GPU za Microsoft Edge v sistemu Windows:

- **Odprite nastavitve:** Kliknite na meni Start in izberite Nastavitve.
- **Sistemske nastavitve:** Pojdite na Sistem in nato Zaslon.
- **Grafične nastavitve:** Pomaknite se navzdol in kliknite na Grafične nastavitve.
- **Izberite aplikacijo:** Pod »Izberite aplikacijo za nastavitev prednosti« izberite Namizna aplikacija in nato Prebrskaj.
- **Izberite Edge:** Poiščite mapo z namestitvijo Edge (običajno `C:\Program Files (x86)\Microsoft\Edge\Application`) in izberite `msedge.exe`.
- **Nastavite prednost:** Kliknite Možnosti, izberite Visoka zmogljivost in nato Shrani.
To bo zagotovilo, da Microsoft Edge uporablja vaš zmogljiv GPU za boljšo zmogljivost.
- **Znova zaženite** računalnik, da bodo te nastavitve začele veljati.

### Vzorci : Prosimo [kliknite na to povezavo](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.