# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo za prikaz WebGPU-a i RAG uzorka

RAG uzorak s Phi-3.5 Onnx Hosted modelom koristi pristup generaciji obogaćen povratnim informacijama (Retrieval-Augmented Generation), kombinirajući snagu Phi-3.5 modela s ONNX hostingom za učinkovite AI implementacije. Ovaj uzorak ključan je za fino podešavanje modela za specifične zadatke unutar određenih domena, nudeći spoj kvalitete, isplativosti i razumijevanja konteksta na duge staze. Dio je Azure AI paketa koji pruža širok izbor modela, jednostavnih za pronalazak, isprobavanje i korištenje, prilagođenih potrebama raznih industrija.

## Što je WebGPU
WebGPU je moderna web grafička API tehnologija osmišljena za omogućavanje učinkovitog pristupa grafičkom procesoru uređaja (GPU) izravno iz web preglednika. Namijenjen je kao nasljednik WebGL-a, nudeći nekoliko ključnih poboljšanja:

1. **Kompatibilnost s modernim GPU-ovima**: WebGPU je razvijen kako bi besprijekorno radio s suvremenim GPU arhitekturama, koristeći sustavne API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opće GPU izračune i brže operacije, čineći ga pogodnim i za renderiranje grafike i za zadatke strojnog učenja.
3. **Napredne značajke**: WebGPU omogućuje pristup naprednijim GPU mogućnostima, omogućujući složenije i dinamičnije grafičke i računalne zadatke.
4. **Smanjeno opterećenje JavaScripta**: Prebacivanjem više zadataka na GPU, WebGPU značajno smanjuje opterećenje JavaScripta, što dovodi do boljih performansi i glatkijeg korisničkog iskustva.

WebGPU je trenutno podržan u preglednicima poput Google Chromea, a radi se na proširenju podrške na druge platforme.

### 03.WebGPU
Potrebno okruženje:

**Podržani preglednici:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogućavanje WebGPU-a:

- U Chrome/Microsoft Edge 

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite svoj preglednik:
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici s postavkama zastavica:
U adresnu traku upišite `chrome://flags` i pritisnite Enter.

#### Pretražite zastavicu:
U okvir za pretraživanje na vrhu stranice upišite 'enable-unsafe-webgpu'.

#### Omogućite zastavicu:
Pronađite zastavicu #enable-unsafe-webgpu na popisu rezultata.

Kliknite na padajući izbornik pokraj nje i odaberite Enabled.

#### Ponovno pokrenite preglednik:

Nakon omogućavanja zastavice, morat ćete ponovno pokrenuti preglednik kako bi promjene stupile na snagu. Kliknite na gumb Relaunch koji će se pojaviti na dnu stranice.

- Za Linux, pokrenite preglednik s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU omogućen prema zadanim postavkama.
- U Firefox Nightly, upišite about:config u adresnu traku i `set dom.webgpu.enabled to true`.

### Postavljanje GPU-a za Microsoft Edge 

Evo koraka za postavljanje GPU-a visokih performansi za Microsoft Edge na Windowsima:

- **Otvorite Postavke:** Kliknite na izbornik Start i odaberite Postavke.
- **Postavke sustava:** Idite na Sustav, a zatim na Zaslon.
- **Grafičke postavke:** Pomaknite se prema dolje i kliknite na Grafičke postavke.
- **Odaberite aplikaciju:** Pod "Odaberite aplikaciju za postavljanje preferencija," odaberite Desktop app i zatim Pregledaj.
- **Odaberite Edge:** Pronađite mapu s instalacijom Edgea (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i odaberite `msedge.exe`.
- **Postavite preferencije:** Kliknite na Opcije, odaberite Visoke performanse, a zatim kliknite Spremi.
To će osigurati da Microsoft Edge koristi vaš GPU visokih performansi za bolje performanse.
- **Ponovno pokrenite** svoje računalo kako bi ove postavke stupile na snagu.

### Primjeri: Molimo [kliknite na ovu poveznicu](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Odricanje odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojno baziranog AI prijevoda. Iako nastojimo postići točnost, molimo vas da budete svjesni da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne snosimo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.