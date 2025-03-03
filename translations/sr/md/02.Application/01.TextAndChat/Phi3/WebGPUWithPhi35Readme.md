# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo za prikaz WebGPU i RAG šablona

RAG šablon sa Phi-3.5 Onnx Hosted modelom koristi pristup generaciji uz podršku pretraživanja (Retrieval-Augmented Generation), kombinujući moć Phi-3.5 modela sa ONNX hostingom za efikasno implementiranje AI rešenja. Ovaj šablon je ključan za fino podešavanje modela za specifične zadatke u određenim domenima, pružajući spoj kvaliteta, ekonomičnosti i razumevanja dužeg konteksta. Deo je Azure AI ponude, koja omogućava širok izbor modela koji su laki za pronalaženje, isprobavanje i korišćenje, prilagođavajući se potrebama različitih industrija.

## Šta je WebGPU 
WebGPU je moderna web grafička API tehnologija dizajnirana da omogući efikasan pristup grafičkom procesoru (GPU) uređaja direktno iz web pregledača. Namenjen je kao naslednik WebGL-a, sa nekoliko ključnih unapređenja:

1. **Kompatibilnost sa savremenim GPU-ovima**: WebGPU je razvijen da radi besprekorno sa modernim GPU arhitekturama, koristeći sistemske API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opšte GPU proračune i brže operacije, što ga čini pogodnim i za grafičko renderovanje i za zadatke mašinskog učenja.
3. **Napredne funkcije**: WebGPU omogućava pristup naprednijim mogućnostima GPU-a, što omogućava složenije i dinamičnije grafičke i računarske zadatke.
4. **Smanjeno opterećenje JavaScript-a**: Prebacivanjem većeg broja zadataka na GPU, WebGPU značajno smanjuje opterećenje JavaScript-a, što dovodi do boljih performansi i glatkijeg iskustva.

WebGPU trenutno podržavaju pregledači poput Google Chrome-a, a rad na proširenju podrške na druge platforme je u toku.

### 03.WebGPU
Potrebno okruženje:

**Podržani pregledači:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogućavanje WebGPU:

- U Chrome/Microsoft Edge 

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite svoj pregledač:
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici sa zastavicama:
U adresnoj traci unesite `chrome://flags` i pritisnite Enter.

#### Pronađite zastavicu:
U polju za pretragu na vrhu stranice unesite 'enable-unsafe-webgpu'.

#### Omogućite zastavicu:
Pronađite #enable-unsafe-webgpu zastavicu u listi rezultata.

Kliknite na padajući meni pored nje i odaberite Enabled.

#### Ponovo pokrenite pregledač:

Nakon omogućavanja zastavice, potrebno je da ponovo pokrenete pregledač kako bi promene stupile na snagu. Kliknite na dugme Relaunch koje se pojavljuje na dnu stranice.

- Za Linux, pokrenite pregledač sa `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU podrazumevano omogućeno.
- U Firefox Nightly, unesite about:config u adresnu traku i `set dom.webgpu.enabled to true`.

### Podešavanje GPU-a za Microsoft Edge 

Evo koraka za podešavanje visokoperformantnog GPU-a za Microsoft Edge na Windows-u:

- **Otvorite Podešavanja:** Kliknite na Start meni i izaberite Podešavanja.
- **Sistemska podešavanja:** Idite na Sistem, a zatim na Ekran.
- **Grafička podešavanja:** Skrolujte nadole i kliknite na Grafička podešavanja.
- **Izaberite aplikaciju:** Pod "Izaberite aplikaciju za podešavanje prioriteta," izaberite Desktop aplikacija, a zatim Pregledaj.
- **Izaberite Edge:** Navigirajte do instalacione mape za Edge (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i izaberite `msedge.exe`.
- **Postavite prioritet:** Kliknite na Opcije, odaberite Visoke performanse, a zatim kliknite na Sačuvaj.
Ovo će osigurati da Microsoft Edge koristi vaš visokoperformantni GPU za bolje performanse. 
- **Ponovo pokrenite** računar da bi ova podešavanja stupila na snagu.

### Primeri: Molimo [kliknite na ovaj link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из коришћења овог превода.