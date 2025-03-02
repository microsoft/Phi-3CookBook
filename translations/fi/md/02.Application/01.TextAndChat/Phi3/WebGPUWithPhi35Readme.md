# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo WebGPU:n ja RAG-mallin esittelemiseksi

RAG-malli Phi-3.5 Onnx Hosted -mallilla hyödyntää Retrieval-Augmented Generation -lähestymistapaa, yhdistäen Phi-3.5-mallien voiman ONNX-hostaukseen tehokkaiden tekoälysovellusten käyttöönotossa. Tämä malli on erityisen hyödyllinen mallien hienosäätöön tiettyjä toimialakohtaisia tehtäviä varten, tarjoten laadun, kustannustehokkuuden ja pitkien kontekstien ymmärryksen yhdistelmän. Se on osa Azure AI:n valikoimaa, joka tarjoaa laajan valikoiman malleja, jotka ovat helposti löydettävissä, kokeiltavissa ja käytettävissä eri toimialojen räätälöintitarpeisiin.

## Mikä on WebGPU
WebGPU on moderni verkkografiikka-rajapinta, joka on suunniteltu tarjoamaan tehokkaan pääsyn laitteen grafiikkaprosessoriin (GPU) suoraan verkkoselaimista. Se on tarkoitettu WebGL:n seuraajaksi ja tarjoaa useita keskeisiä parannuksia:

1. **Yhteensopivuus nykyaikaisten GPU:iden kanssa**: WebGPU on rakennettu toimimaan saumattomasti nykyaikaisten GPU-arkkitehtuurien kanssa, hyödyntäen järjestelmä-API:ita, kuten Vulkan, Metal ja Direct3D 12.
2. **Parannettu suorituskyky**: Se tukee yleiskäyttöistä GPU-laskentaa ja nopeampia operaatioita, tehden siitä sopivan sekä grafiikan renderöintiin että koneoppimistehtäviin.
3. **Edistyneet ominaisuudet**: WebGPU tarjoaa pääsyn kehittyneempiin GPU-ominaisuuksiin, mahdollistaen monimutkaisemmat ja dynaamisemmat grafiikka- ja laskentatyöt.
4. **Vähentynyt JavaScript-kuormitus**: Siirtämällä enemmän tehtäviä GPU:lle WebGPU vähentää merkittävästi JavaScriptin kuormitusta, mikä parantaa suorituskykyä ja tarjoaa sulavampia käyttökokemuksia.

WebGPU on tällä hetkellä tuettu selaimissa, kuten Google Chrome, ja työtä tehdään tuen laajentamiseksi muihin alustoihin.

### 03.WebGPU
Vaadittu ympäristö:

**Tuetut selaimet:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU:n käyttöönotto:

- Chrome/Microsoft Edge -selaimessa 

Ota `chrome://flags/#enable-unsafe-webgpu`-lippu käyttöön.

#### Avaa selaimesi:
Käynnistä Google Chrome tai Microsoft Edge.

#### Siirry liput-sivulle:
Kirjoita osoiteriville `chrome://flags` ja paina Enter.

#### Etsi lippu:
Kirjoita sivun yläosan hakukenttään 'enable-unsafe-webgpu'.

#### Ota lippu käyttöön:
Löydä hakutuloksista #enable-unsafe-webgpu-lippu.

Klikkaa sen vieressä olevaa pudotusvalikkoa ja valitse Enabled.

#### Käynnistä selaimesi uudelleen:

Kun olet ottanut lipun käyttöön, sinun täytyy käynnistää selaimesi uudelleen, jotta muutokset tulevat voimaan. Klikkaa sivun alareunaan ilmestyvää Relaunch-painiketta.

- Linuxissa käynnistä selain käyttäen `--enable-features=Vulkan`.
- Safari 18 (macOS 15) -selaimessa WebGPU on oletuksena käytössä.
- Firefox Nightly -selaimessa kirjoita osoiteriville about:config ja `set dom.webgpu.enabled to true`.

### GPU:n asettaminen Microsoft Edgeä varten

Tässä ohjeet korkean suorituskyvyn GPU:n asettamiseen Microsoft Edgeä varten Windowsissa:

- **Avaa asetukset:** Klikkaa Käynnistä-valikkoa ja valitse Asetukset.
- **Järjestelmäasetukset:** Siirry kohtaan Järjestelmä ja sitten Näyttö.
- **Grafiikka-asetukset:** Vieritä alas ja klikkaa Grafiikka-asetukset.
- **Valitse sovellus:** Kohdassa "Valitse sovellus, jolle haluat asettaa asetukset," valitse Työpöytäsovellus ja sitten Selaa.
- **Valitse Edge:** Siirry Edgen asennuskansioon (yleensä `C:\Program Files (x86)\Microsoft\Edge\Application`) ja valitse `msedge.exe`.
- **Aseta mieltymys:** Klikkaa Asetukset, valitse Korkea suorituskyky ja sitten Tallenna.
Tämä varmistaa, että Microsoft Edge käyttää korkean suorituskyvyn GPU:ta paremman suorituskyvyn takaamiseksi.
- **Käynnistä tietokoneesi uudelleen**, jotta nämä asetukset tulevat voimaan.

### Esimerkit: Katso [tämä linkki](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista, ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.