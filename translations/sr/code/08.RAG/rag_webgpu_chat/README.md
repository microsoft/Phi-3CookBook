Phi-3-mini WebGPU RAG Četbot

## Demo za prikazivanje WebGPU i RAG šablona
RAG šablon sa Phi-3 Onnx hostovanim modelom koristi pristup generaciji uz obogaćivanje podacima iz pretrage, kombinujući snagu Phi-3 modela sa ONNX hostingom za efikasno implementiranje veštačke inteligencije. Ovaj šablon je ključan za fino podešavanje modela za zadatke specifične za određene oblasti, nudeći spoj kvaliteta, isplativosti i razumevanja dužeg konteksta. Deo je Azure AI ponude, koja pruža širok izbor modela koje je lako pronaći, isprobati i koristiti, zadovoljavajući potrebe za prilagođavanjem u različitim industrijama. Phi-3 modeli, uključujući Phi-3-mini, Phi-3-small i Phi-3-medium, dostupni su u Azure AI Model Catalog i mogu se fino podešavati i implementirati samostalno ili putem platformi kao što su HuggingFace i ONNX, što demonstrira Microsoftovu posvećenost dostupnim i efikasnim AI rešenjima.

## Šta je WebGPU 
WebGPU je moderan API za web grafiku dizajniran da obezbedi efikasan pristup grafičkoj procesorskoj jedinici (GPU) uređaja direktno iz web pregledača. Namenjen je da nasledi WebGL, nudeći nekoliko ključnih poboljšanja:

1. **Kompatibilnost sa modernim GPU-ovima**: WebGPU je kreiran da besprekorno radi sa savremenim GPU arhitekturama, koristeći sistemske API-je poput Vulkan, Metal i Direct3D 12.
2. **Poboljšane performanse**: Podržava opšte GPU računanje i brže operacije, čineći ga pogodnim za renderovanje grafike i zadatke mašinskog učenja.
3. **Napredne funkcije**: WebGPU omogućava pristup naprednijim mogućnostima GPU-a, omogućavajući složenije i dinamičnije grafičke i računarske zadatke.
4. **Smanjeno opterećenje JavaScript-a**: Prebacivanjem više zadataka na GPU, WebGPU značajno smanjuje opterećenje JavaScript-a, što dovodi do boljih performansi i glatkijeg iskustva.

WebGPU trenutno podržavaju pregledači poput Google Chrome-a, dok se radi na proširenju podrške na druge platforme.

### 03.WebGPU
Potrebno okruženje:

**Podržani pregledači:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Omogućavanje WebGPU-a:

- U Chrome/Microsoft Edge 

Omogućite `chrome://flags/#enable-unsafe-webgpu` zastavicu.

#### Otvorite pregledač:
Pokrenite Google Chrome ili Microsoft Edge.

#### Pristupite stranici sa zastavicama:
U adresnu traku unesite `chrome://flags` i pritisnite Enter.

#### Pronađite zastavicu:
U polju za pretragu na vrhu stranice unesite 'enable-unsafe-webgpu'.

#### Omogućite zastavicu:
Pronađite #enable-unsafe-webgpu zastavicu na listi rezultata.

Kliknite na padajući meni pored nje i odaberite Enabled.

#### Ponovo pokrenite pregledač:

Nakon omogućavanja zastavice, potrebno je da ponovo pokrenete pregledač kako bi promene stupile na snagu. Kliknite na dugme Relaunch koje se pojavljuje na dnu stranice.

- Za Linux, pokrenite pregledač sa `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ima WebGPU podrazumevano omogućeno.
- U Firefox Nightly, unesite about:config u adresnu traku i `set dom.webgpu.enabled to true`.

### Podešavanje GPU-a za Microsoft Edge 

Evo koraka za podešavanje visokih performansi GPU-a za Microsoft Edge na Windows-u:

- **Otvorite Podešavanja:** Kliknite na Start meni i odaberite Podešavanja.
- **Sistemska podešavanja:** Idite na Sistem, a zatim na Prikaz.
- **Grafička podešavanja:** Skrolujte nadole i kliknite na Grafička podešavanja.
- **Izaberite aplikaciju:** U okviru “Izaberite aplikaciju za podešavanje prioriteta,” odaberite Desktop aplikacija i zatim Pretraži.
- **Izaberite Edge:** Idite do instalacionog foldera Edge-a (obično `C:\Program Files (x86)\Microsoft\Edge\Application`) i odaberite `msedge.exe`.
- **Postavite prioritete:** Kliknite na Opcije, odaberite Visoke performanse i zatim kliknite na Sačuvaj.
Ovo će osigurati da Microsoft Edge koristi GPU visokih performansi za bolje performanse. 
- **Ponovo pokrenite** računar kako bi ova podešavanja stupila na snagu.

### Otvorite svoj Codespace:
Idite na svoj repozitorijum na GitHub-u.
Kliknite na dugme Code i odaberite Open with Codespaces.

Ako još nemate Codespace, možete ga kreirati klikom na New codespace.

**Napomena** Instaliranje Node okruženja u vašem Codespace-u
Pokretanje npm demo-a iz GitHub Codespace-a je odličan način za testiranje i razvoj vašeg projekta. Evo vodiča korak po korak:

### Postavite svoje okruženje:
Kada se vaš Codespace otvori, proverite da li su Node.js i npm instalirani. To možete proveriti pokretanjem:
```
node -v
```
```
npm -v
```

Ako nisu instalirani, možete ih instalirati koristeći:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigirajte do direktorijuma vašeg projekta:
Koristite terminal da se krećete do direktorijuma gde se nalazi vaš npm projekat:
```
cd path/to/your/project
```

### Instalirajte zavisnosti:
Pokrenite sledeću komandu kako biste instalirali sve potrebne zavisnosti navedene u vašem package.json fajlu:

```
npm install
```

### Pokrenite demo:
Kada se zavisnosti instaliraju, možete pokrenuti vaš demo skript. Ovo je obično navedeno u odeljku scripts vašeg package.json fajla. Na primer, ako se vaš demo skript zove start, možete ga pokrenuti:

```
npm run build
```
```
npm run dev
```

### Pristupite demo-u:
Ako vaš demo uključuje web server, Codespaces će obezbediti URL za pristup. Potražite obaveštenje ili proverite karticu Ports kako biste pronašli URL.

**Napomena:** Model mora biti keširan u pregledaču, tako da može potrajati neko vreme da se učita. 

### RAG Demo
Otpremite markdown fajl `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Izaberite svoj fajl:
Kliknite na dugme “Izaberite fajl” kako biste odabrali dokument koji želite da otpremite.

### Otpremite dokument:
Nakon odabira fajla, kliknite na dugme “Otpremi” kako biste učitali vaš dokument za RAG (generaciju uz obogaćivanje podacima iz pretrage).

### Započnite čet:
Kada je dokument učitan, možete započeti sesiju četa koristeći RAG na osnovu sadržaja vašeg dokumenta.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала употребом овог превода.