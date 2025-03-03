Phi-3-mini WebGPU RAG Chatbot

## Demo za prikaz WebGPU i RAG uzorka
RAG uzorak s Phi-3 Onnx hostiranim modelom koristi pristup Generiranja uz pomoć pretraživanja (Retrieval-Augmented Generation), kombinirajući snagu Phi-3 modela s ONNX hostingom za učinkovito implementiranje AI rješenja. Ovaj uzorak ključan je za prilagodbu modela specifičnim zadacima u domeni, nudeći spoj kvalitete, isplativosti i razumijevanja dugog konteksta. Dio je Azure AI portfelja, pružajući širok izbor modela koji su jednostavni za pronalaženje, isprobavanje i korištenje, zadovoljavajući potrebe prilagodbe različitih industrija. Phi-3 modeli, uključujući Phi-3-mini, Phi-3-small i Phi-3-medium, dostupni su u Azure AI Model Catalogu i mogu se prilagoditi i implementirati samostalno ili putem platformi poput HuggingFace i ONNX, pokazujući Microsoftovu predanost dostupnim i učinkovitim AI rješenjima.

## Što je WebGPU
WebGPU je moderna web grafička API tehnologija osmišljena za pružanje učinkovitog pristupa grafičkom procesoru (GPU) uređaja izravno iz web preglednika. Namijenjena je kao nasljednik WebGL-a, donoseći nekoliko ključnih poboljšanja:

1. **Kompatibilnost s modernim GPU-ovima**: WebGPU je razvijen za besprijekoran rad s suvremenim GPU arhitekturama, koristeći sustavne API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opće GPU izračune i brže operacije, što ga čini prikladnim za renderiranje grafike i zadatke strojnog učenja.
3. **Napredne značajke**: WebGPU omogućuje pristup naprednijim mogućnostima GPU-a, podržavajući složenije i dinamičnije grafičke i računalne zadatke.
4. **Smanjeno opterećenje JavaScripta**: Prebacivanjem više zadataka na GPU, WebGPU značajno smanjuje opterećenje JavaScripta, što dovodi do boljih performansi i glatkijeg korisničkog iskustva.

WebGPU trenutno podržavaju preglednici poput Google Chromea, a rad na proširenju podrške na druge platforme je u tijeku.

### 03.WebGPU
Potrebno okruženje:

**Podržani preglednici:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogućavanje WebGPU-a:

- U Chromeu/Microsoft Edgeu 

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite preglednik:
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici sa zastavicama:
U adresnu traku unesite `chrome://flags` i pritisnite Enter.

#### Pretražite zastavicu:
U okvir za pretraživanje na vrhu stranice unesite 'enable-unsafe-webgpu'.

#### Omogućite zastavicu:
Pronađite #enable-unsafe-webgpu zastavicu u popisu rezultata.

Kliknite padajući izbornik pokraj nje i odaberite Enabled.

#### Ponovno pokrenite preglednik:

Nakon omogućavanja zastavice, trebate ponovno pokrenuti preglednik kako bi promjene stupile na snagu. Kliknite gumb Relaunch koji se pojavljuje na dnu stranice.

- Za Linux, pokrenite preglednik s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU omogućen prema zadanim postavkama.
- U Firefox Nightly, unesite about:config u adresnu traku i `set dom.webgpu.enabled to true`.

### Postavljanje GPU-a za Microsoft Edge 

Evo koraka za postavljanje GPU-a visokih performansi za Microsoft Edge na Windowsu:

- **Otvorite Postavke:** Kliknite na Start izbornik i odaberite Postavke.
- **Postavke sustava:** Idite na Sustav, a zatim Prikaz.
- **Grafičke postavke:** Pomaknite se prema dolje i kliknite na Grafičke postavke.
- **Odaberite aplikaciju:** U odjeljku "Odaberite aplikaciju za postavljanje preferencija," odaberite Desktop app i zatim Browse.
- **Odaberite Edge:** Navigirajte do instalacijske mape Edgea (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i odaberite `msedge.exe`.
- **Postavite preferencije:** Kliknite na Opcije, odaberite Visoke performanse, a zatim kliknite Spremi.
To će osigurati da Microsoft Edge koristi vaš GPU visokih performansi za bolje performanse.
- **Ponovno pokrenite** računalo kako bi ove postavke stupile na snagu.

### Otvorite svoj Codespace:
Idite na svoj repozitorij na GitHubu.
Kliknite na gumb Code i odaberite Open with Codespaces.

Ako još nemate Codespace, možete ga stvoriti klikom na New codespace.

**Napomena** Instalacija Node okruženja u vašem Codespaceu
Pokretanje npm demonstracije iz GitHub Codespacea izvrstan je način za testiranje i razvoj vašeg projekta. Evo vodiča korak po korak:

### Postavljanje okruženja:
Kada se Codespace otvori, provjerite imate li instalirane Node.js i npm. To možete provjeriti pokretanjem:
```
node -v
```
```
npm -v
```

Ako nisu instalirani, možete ih instalirati pomoću:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigacija do direktorija projekta:
Koristite terminal za navigaciju do direktorija gdje se nalazi vaš npm projekt:
```
cd path/to/your/project
```

### Instalacija ovisnosti:
Pokrenite sljedeću naredbu kako biste instalirali sve potrebne ovisnosti navedene u vašoj datoteci package.json:

```
npm install
```

### Pokretanje demonstracije:
Nakon što su ovisnosti instalirane, možete pokrenuti svoj demo skriptu. To je obično specificirano u odjeljku scripts vaše datoteke package.json. Na primjer, ako se vaša demo skripta zove start, možete pokrenuti:

```
npm run build
```
```
npm run dev
```

### Pristup demonstraciji:
Ako vaša demonstracija uključuje web poslužitelj, Codespaces će pružiti URL za pristup. Potražite obavijest ili provjerite karticu Ports kako biste pronašli URL.

**Napomena:** Model treba biti predmemoriran u pregledniku, pa može potrajati neko vrijeme dok se učita.

### RAG Demonstracija
Prenesite markdown datoteku `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Odaberite svoju datoteku:
Kliknite na gumb “Odaberi datoteku” kako biste odabrali dokument koji želite prenijeti.

### Prenesite dokument:
Nakon što odaberete svoju datoteku, kliknite na gumb “Prenesi” kako biste učitali svoj dokument za RAG (Retrieval-Augmented Generation).

### Započnite razgovor:
Nakon što je dokument učitan, možete započeti razgovor koristeći RAG na temelju sadržaja vašeg dokumenta.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluga za automatski prijevod. Iako težimo točnosti, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.