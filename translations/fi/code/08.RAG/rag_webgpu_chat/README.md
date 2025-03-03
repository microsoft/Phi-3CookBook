Phi-3-mini WebGPU RAG Chatbot

## Demo WebGPU:n ja RAG-mallin esittelyyn
RAG-malli Phi-3 Onnx Hosted -mallilla hyödyntää Retrieval-Augmented Generation -lähestymistapaa, yhdistäen Phi-3-mallien ja ONNX-hostauksen voiman tehokkaisiin tekoälysovelluksiin. Tämä malli on keskeinen mallien hienosäätämisessä toimialakohtaisia tehtäviä varten, tarjoten yhdistelmän laatua, kustannustehokkuutta ja pitkän kontekstin ymmärrystä. Se on osa Azure AI:n tarjontaa, joka tarjoaa laajan valikoiman helposti löydettäviä, kokeiltavia ja käytettäviä malleja, vastaten eri toimialojen räätälöintitarpeisiin. Phi-3-mallit, kuten Phi-3-mini, Phi-3-small ja Phi-3-medium, ovat saatavilla Azure AI Model Catalogissa, ja niitä voi hienosäätää ja ottaa käyttöön itsehallinnollisesti tai alustoilla kuten HuggingFace ja ONNX, mikä osoittaa Microsoftin sitoutumista saavutettaviin ja tehokkaisiin tekoälyratkaisuihin.

## Mikä on WebGPU
WebGPU on moderni web-grafiikka-API, joka on suunniteltu tarjoamaan tehokas pääsy laitteen grafiikkaprosessoriyksikköön (GPU) suoraan verkkoselaimista. Se on tarkoitettu WebGL:n seuraajaksi ja tarjoaa useita merkittäviä parannuksia:

1. **Yhteensopivuus nykyaikaisten GPU:iden kanssa**: WebGPU on suunniteltu toimimaan saumattomasti nykyisten GPU-arkkitehtuurien kanssa, hyödyntäen järjestelmä-API:ta, kuten Vulkan, Metal ja Direct3D 12.
2. **Parannettu suorituskyky**: Se tukee yleiskäyttöisiä GPU-laskelmia ja nopeampia toimintoja, tehden siitä sopivan sekä grafiikan renderöintiin että koneoppimistehtäviin.
3. **Kehittyneet ominaisuudet**: WebGPU tarjoaa pääsyn kehittyneempiin GPU-ominaisuuksiin, mahdollistaen monimutkaisemmat ja dynaamisemmat grafiikka- ja laskentatyöt.
4. **Vähentynyt JavaScript-kuorma**: Siirtämällä enemmän tehtäviä GPU:lle WebGPU vähentää merkittävästi JavaScriptin kuormitusta, mikä johtaa parempaan suorituskykyyn ja sujuvampiin käyttökokemuksiin.

WebGPU on tällä hetkellä tuettu selaimissa kuten Google Chrome, ja tukea laajennetaan jatkuvasti muihin alustoihin.

### 03.WebGPU
Vaadittu ympäristö:

**Tuetut selaimet:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Ota WebGPU käyttöön:

- Chrome/Microsoft Edge 

Ota käyttöön `chrome://flags/#enable-unsafe-webgpu`-asetus.

#### Avaa selaimesi:
Käynnistä Google Chrome tai Microsoft Edge.

#### Siirry asetussivulle:
Kirjoita osoiteriville `chrome://flags` ja paina Enter.

#### Etsi asetus:
Kirjoita hakukenttään yläreunaan 'enable-unsafe-webgpu'.

#### Ota asetus käyttöön:
Etsi tuloslistasta #enable-unsafe-webgpu.

Klikkaa vieressä olevaa valikkoa ja valitse Enabled.

#### Käynnistä selaimesi uudelleen:

Kun asetus on otettu käyttöön, sinun täytyy käynnistää selaimesi uudelleen, jotta muutokset tulevat voimaan. Klikkaa Relaunch-painiketta, joka näkyy sivun alareunassa.

- Linuxilla käynnistä selain komennolla `--enable-features=Vulkan`.
- Safari 18 (macOS 15):ssa WebGPU on oletuksena käytössä.
- Firefox Nightlyssa kirjoita osoiteriville about:config ja `set dom.webgpu.enabled to true`.

### GPU:n määrittäminen Microsoft Edgeä varten

Näin voit määrittää suorituskykyisen GPU:n Microsoft Edgeä varten Windowsissa:

- **Avaa asetukset:** Klikkaa Käynnistä-valikkoa ja valitse Asetukset.
- **Järjestelmäasetukset:** Siirry kohtaan Järjestelmä ja sitten Näyttö.
- **Grafiikka-asetukset:** Vieritä alas ja klikkaa Grafiikka-asetukset.
- **Valitse sovellus:** Valitse “Valitse sovellus, jolle määritetään asetukset” -kohdasta Työpöytäsovellus ja selaa.
- **Valitse Edge:** Siirry Edgen asennuskansioon (yleensä `C:\Program Files (x86)\Microsoft\Edge\Application`) ja valitse `msedge.exe`.
- **Määritä asetukset:** Klikkaa Asetukset, valitse Suorituskykyinen ja tallenna.
Tämä varmistaa, että Microsoft Edge käyttää suorituskykyistä GPU:ta paremman suorituskyvyn saavuttamiseksi.
- **Käynnistä tietokoneesi uudelleen**, jotta asetukset tulevat voimaan.

### Avaa Codespace:
Siirry GitHub-repositorioosi.
Klikkaa Koodi-painiketta ja valitse Avaa Codespacessa.

Jos sinulla ei ole Codespacea, voit luoda uuden klikkaamalla Uusi Codespace.

**Huomio** Node-ympäristön asentaminen Codespaceesi
npm-demon suorittaminen GitHub Codespacesta on loistava tapa testata ja kehittää projektiasi. Tässä vaiheittainen opas:

### Määritä ympäristösi:
Kun Codespace on avattu, varmista, että sinulla on Node.js ja npm asennettuna. Voit tarkistaa tämän suorittamalla:
```
node -v
```
```
npm -v
```

Jos niitä ei ole asennettu, voit asentaa ne seuraavilla komennoilla:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Siirry projektihakemistoosi:
Käytä terminaalia navigoidaksesi hakemistoon, jossa npm-projektisi sijaitsee:
```
cd path/to/your/project
```

### Asenna riippuvuudet:
Suorita seuraava komento asentaaksesi kaikki package.json-tiedostossa luetellut tarvittavat riippuvuudet:

```
npm install
```

### Suorita demo:
Kun riippuvuudet on asennettu, voit suorittaa demon skriptin. Tämä määritellään yleensä package.json-tiedoston scripts-osiossa. Esimerkiksi, jos demon skripti on nimeltään start, voit suorittaa sen:

```
npm run build
```
```
npm run dev
```

### Pääsy demoon:
Jos demo sisältää web-palvelimen, Codespaces tarjoaa URL-osoitteen sen käyttöön. Etsi ilmoitus tai tarkista Portit-välilehti löytääksesi URL-osoitteen.

**Huomio:** Malli täytyy tallentaa selaimeen välimuistiin, joten lataaminen voi kestää hetken.

### RAG Demo
Lataa markdown-tiedosto `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Valitse tiedostosi:
Klikkaa painiketta, jossa lukee “Valitse tiedosto” valitaksesi ladattavan dokumentin.

### Lataa dokumentti:
Kun tiedosto on valittu, klikkaa “Lataa” -painiketta ladataksesi dokumenttisi RAG:n (Retrieval-Augmented Generation) käyttöön.

### Aloita keskustelu:
Kun dokumentti on ladattu, voit aloittaa keskustelusession RAG:n avulla dokumenttisi sisällön pohjalta.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Vaikka pyrimme tarkkuuteen, on hyvä olla tietoinen siitä, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.