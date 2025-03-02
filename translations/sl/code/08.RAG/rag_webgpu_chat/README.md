Phi-3-mini WebGPU RAG Chatbot

## Demo za predstavitev WebGPU in vzorca RAG
Vzorec RAG z modelom Phi-3 Onnx Hosted uporablja pristop Retrieval-Augmented Generation, ki združuje moč modelov Phi-3 z gostovanjem ONNX za učinkovito uvajanje umetne inteligence. Ta vzorec je ključen za prilagoditev modelov za specifične naloge v določenih domenah, saj ponuja kombinacijo kakovosti, stroškovne učinkovitosti in razumevanja dolgih kontekstov. Je del zbirke Azure AI, ki zagotavlja širok izbor modelov, ki so enostavni za iskanje, preizkušanje in uporabo, ter ustreza potrebam po prilagoditvi v različnih industrijah. Modeli Phi-3, vključno s Phi-3-mini, Phi-3-small in Phi-3-medium, so na voljo v katalogu modelov Azure AI in jih je mogoče prilagoditi ter uvajati samostojno ali prek platform, kot sta HuggingFace in ONNX, kar dokazuje Microsoftovo zavezanost k dostopnim in učinkovitim rešitvam umetne inteligence.

## Kaj je WebGPU
WebGPU je sodoben spletni grafični API, zasnovan za zagotavljanje učinkovitega dostopa do grafične procesne enote (GPU) naprave neposredno iz spletnih brskalnikov. Namenjen je kot naslednik WebGL in prinaša več ključnih izboljšav:

1. **Združljivost z modernimi GPU-ji**: WebGPU je zasnovan za brezhibno delovanje s sodobnimi arhitekturami GPU-jev, pri čemer uporablja sistemske API-je, kot so Vulkan, Metal in Direct3D 12.
2. **Izboljšana zmogljivost**: Podpira splošno računalništvo na GPU in hitrejše operacije, kar ga naredi primernega tako za grafično upodabljanje kot tudi za naloge strojnega učenja.
3. **Napredne funkcije**: WebGPU omogoča dostop do bolj naprednih zmogljivosti GPU, kar omogoča bolj kompleksne in dinamične grafične ter računalniške delovne obremenitve.
4. **Manjša obremenitev JavaScripta**: Z razbremenitvijo več nalog na GPU WebGPU bistveno zmanjša obremenitev JavaScripta, kar vodi do boljše zmogljivosti in bolj gladkih izkušenj.

WebGPU trenutno podpirajo brskalniki, kot je Google Chrome, z nadaljnjimi prizadevanji za razširitev podpore na druge platforme.

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

#### Odprite svoj brskalnik:
Zaženite Google Chrome ali Microsoft Edge.

#### Dostop do strani z zastavicami:
V naslovno vrstico vnesite `chrome://flags` in pritisnite Enter.

#### Poiščite zastavico:
V iskalno polje na vrhu strani vnesite 'enable-unsafe-webgpu'.

#### Omogočite zastavico:
Poiščite zastavico #enable-unsafe-webgpu na seznamu rezultatov.

Kliknite spustni meni poleg nje in izberite Enabled.

#### Znova zaženite svoj brskalnik:

Po omogočitvi zastavice boste morali znova zagnati brskalnik, da spremembe začnejo veljati. Kliknite gumb Relaunch, ki se prikaže na dnu strani.

- Za Linux zaženite brskalnik z `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU privzeto omogočen.
- V Firefox Nightly vnesite about:config v naslovno vrstico in `set dom.webgpu.enabled to true`.

### Nastavitev GPU za Microsoft Edge 

Tukaj so koraki za nastavitev visokozmogljivega GPU-ja za Microsoft Edge v sistemu Windows:

- **Odprite nastavitve:** Kliknite meni Start in izberite Nastavitve.
- **Sistemske nastavitve:** Pojdite na Sistem in nato Zaslon.
- **Grafične nastavitve:** Pomaknite se navzdol in kliknite Grafične nastavitve.
- **Izberite aplikacijo:** Pod “Izberite aplikacijo za nastavitev prednosti” izberite Namizna aplikacija in nato Prebrskaj.
- **Izberite Edge:** Pojdite v mapo z namestitvijo Edge (običajno `C:\Program Files (x86)\Microsoft\Edge\Application`) in izberite `msedge.exe`.
- **Nastavite prednost:** Kliknite Možnosti, izberite Visoka zmogljivost in nato Shrani.
To bo zagotovilo, da Microsoft Edge uporablja vaš visokozmogljiv GPU za boljšo zmogljivost.
- **Znova zaženite** računalnik, da te nastavitve začnejo veljati.

### Odprite svoj Codespace:
Pojdite v svoje skladišče na GitHubu.
Kliknite gumb Koda in izberite Odpri s Codespaces.

Če še nimate Codespace-a, ga lahko ustvarite s klikom na Nov Codespace.

**Opomba** Namestitev okolja Node v vašem Codespace-u
Zagon npm demonstracije iz GitHub Codespace-a je odličen način za testiranje in razvoj vašega projekta. Tukaj je korak za korakom vodič, kako začeti:

### Nastavite svoje okolje:
Ko je vaš Codespace odprt, se prepričajte, da imate nameščena Node.js in npm. To lahko preverite z ukazom:
```
node -v
```
```
npm -v
```

Če nista nameščena, ju lahko namestite z:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Pomaknite se do svoje projektne mape:
Uporabite terminal za premik v mapo, kjer se nahaja vaš npm projekt:
```
cd path/to/your/project
```

### Namestite odvisnosti:
Zaženite naslednji ukaz za namestitev vseh potrebnih odvisnosti, navedenih v vaši datoteki package.json:

```
npm install
```

### Zaženite demonstracijo:
Ko so odvisnosti nameščene, lahko zaženete svoj demo skript. To je običajno določeno v razdelku scripts v vaši datoteki package.json. Na primer, če je vaš demo skript imenovan start, ga lahko zaženete z:

```
npm run build
```
```
npm run dev
```

### Dostop do demonstracije:
Če vaša demonstracija vključuje spletni strežnik, bo Codespaces zagotovil URL za dostop. Poiščite obvestilo ali preverite zavihek Ports, da najdete URL.

**Opomba:** Model mora biti predpomnjen v brskalniku, zato lahko traja nekaj časa, da se naloži.

### RAG Demo
Naložite markdown datoteko `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Izberite svojo datoteko:
Kliknite gumb z napisom “Izberite datoteko” za izbiro dokumenta, ki ga želite naložiti.

### Naložite dokument:
Po izbiri datoteke kliknite gumb “Naloži”, da naložite dokument za RAG (Retrieval-Augmented Generation).

### Začnite pogovor:
Ko je dokument naložen, lahko začnete sejo klepeta z uporabo RAG, ki temelji na vsebini vašega dokumenta.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.