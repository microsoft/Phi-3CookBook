# Osallistuminen

Tämä projekti toivottaa tervetulleiksi osallistumiset ja ehdotukset. Useimmat osallistumiset edellyttävät, että hyväksyt Contributor License Agreement (CLA) -sopimuksen, joka vahvistaa, että sinulla on oikeus antaa meille oikeudet käyttää panostasi. Lisätietoja löytyy osoitteesta [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kun lähetät pull requestin, CLA-botti tarkistaa automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n sen mukaisesti (esim. tilan tarkistus, kommentti). Seuraa vain botin antamia ohjeita. Tämä täytyy tehdä vain kerran kaikille repositorioille, jotka käyttävät CLA:ta.

## Käytösäännöt

Tämä projekti on omaksunut [Microsoftin avoimen lähdekoodin käytössäännöt](https://opensource.microsoft.com/codeofconduct/). 
Lisätietoja löytyy [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) -sivulta tai ottamalla yhteyttä [opencode@microsoft.com](mailto:opencode@microsoft.com), jos sinulla on lisäkysymyksiä tai kommentteja.

## Huomioitavaa ongelmia luodessa

Älä avaa GitHub-ongelmia yleisiä tukikysymyksiä varten, sillä GitHub-listaa tulisi käyttää ominaisuuspyyntöihin ja virheraportteihin. Näin voimme helpommin seurata varsinaisia ongelmia tai virheitä koodissa ja pitää yleiset keskustelut erillään itse koodista.

## Kuinka osallistua

### Pull Request -ohjeet

Kun lähetät pull requestin (PR) Phi-3 CookBook -repositorioon, noudata seuraavia ohjeita:

- **Haarauta repositorio**: Haarauta aina repositorio omaan tiliisi ennen kuin teet muutoksia.

- **Erota pull requestit (PR)**:
  - Lähetä jokainen muutos omassa pull requestissaan. Esimerkiksi virheenkorjaukset ja dokumentaation päivitykset tulisi lähettää erillisissä PR:issä.
  - Pienet kirjoitusvirheiden korjaukset ja dokumentaation päivitykset voidaan yhdistää yhteen PR:ään, jos se on tarkoituksenmukaista.

- **Ratkaise yhdistämiskonfliktit**: Jos pull requestissasi on yhdistämiskonflikteja, päivitä paikallinen `main` haarasi vastaamaan päärepositorion tilaa ennen muutosten tekemistä.

- **Käännösten lähettäminen**: Kun lähetät käännös-PR:n, varmista, että käännöskansio sisältää käännökset kaikille alkuperäisen kansion tiedostoille.

### Käännösohjeet

> [!IMPORTANT]
>
> Kun käännät tämän repositorion tekstiä, älä käytä konekäännöstä. Osallistu käännöksiin vain kielillä, joissa olet taitava.

Jos olet taitava jossain muussa kuin englannin kielessä, voit auttaa kääntämään sisältöä. Seuraa näitä ohjeita varmistaaksesi, että käännöksesi integroidaan oikein:

- **Luo käännöskansio**: Siirry oikeaan osion kansioon ja luo käännöskansio kielelle, johon osallistut. Esimerkiksi:
  - Johdanto-osio: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Nopea aloitus -osio: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Jatka tätä kaavaa muille osioille (03.Inference, 04.Finetuning jne.)

- **Päivitä suhteelliset polut**: Kääntäessäsi säädä kansiorakenne lisäämällä `../../` suhteellisten polkujen alkuun markdown-tiedostoissa varmistaaksesi, että linkit toimivat oikein. Esimerkiksi:
  - Muuta `(../../imgs/01/phi3aisafety.png)` muotoon `(../../../../imgs/01/phi3aisafety.png)`

- **Järjestä käännöksesi**: Jokainen käännetty tiedosto tulisi sijoittaa vastaavan osion käännöskansioon. Esimerkiksi, jos käännät johdanto-osion espanjaksi, loisit seuraavasti:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Lähetä täydellinen PR**: Varmista, että kaikki osion käännetyt tiedostot sisältyvät yhteen PR:ään. Emme hyväksy osittaisia käännöksiä yhdelle osiolle. Kun lähetät käännös-PR:n, varmista, että käännöskansio sisältää käännökset kaikille alkuperäisen kansion tiedostoille.

### Kirjoitusohjeet

Yhdenmukaisuuden varmistamiseksi kaikissa dokumenteissa, käytä seuraavia ohjeita:

- **URL-muotoilu**: Ympäröi kaikki URL-osoitteet hakasulkeilla, joita seuraavat sulut, ilman ylimääräisiä välilyöntejä niiden ympärillä tai sisällä. Esimerkiksi: `[example](https://www.microsoft.com)`.

- **Suhteelliset linkit**: Käytä `./` suhteellisille linkeille, jotka osoittavat tiedostoihin tai kansioihin nykyisessä hakemistossa, ja `../` niille, jotka ovat ylemmässä hakemistossa. Esimerkiksi: `[example](../../path/to/file)` tai `[example](../../../path/to/file)`.

- **Ei maa-kohtaisia paikallisia linkkejä**: Varmista, että linkkisi eivät sisällä maa-kohtaisia paikallisia viittauksia. Esimerkiksi, vältä `/en-us/` tai `/en/`.

- **Kuvien tallennus**: Tallenna kaikki kuvat `./imgs` kansioon.

- **Kuvailevat kuvien nimet**: Nimeä kuvat kuvailevasti käyttäen englanninkielisiä merkkejä, numeroita ja väliviivoja. Esimerkiksi: `example-image.jpg`.

## GitHub-työnkulut

Kun lähetät pull requestin, seuraavat työnkulut käynnistyvät muutosten tarkistamiseksi. Noudata alla olevia ohjeita varmistaaksesi, että pull requestisi läpäisee työnkulun tarkistukset:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Tarkista rikkinäiset suhteelliset polut

Tämä työnkulku varmistaa, että kaikki tiedostojesi suhteelliset polut ovat oikein.

1. Varmistaaksesi, että linkkisi toimivat oikein, suorita seuraavat tehtävät käyttäen VS Codea:
    - Vie hiiri minkä tahansa linkin päälle tiedostoissasi.
    - Paina **Ctrl + Klikkaa** siirtyäksesi linkkiin.
    - Jos napsautat linkkiä ja se ei toimi paikallisesti, se käynnistää työnkulun eikä toimi GitHubissa.

1. Korjataksesi tämän ongelman, suorita seuraavat tehtävät käyttäen VS Coden ehdotuksia:
    - Kirjoita `./` tai `../`.
    - VS Code ehdottaa valittavia vaihtoehtoja kirjoittamasi perusteella.
    - Seuraa polkua napsauttamalla haluttua tiedostoa tai kansiota varmistaaksesi, että polkusi on oikea.

Kun olet lisännyt oikean suhteellisen polun, tallenna ja lähetä muutokset.

### Tarkista, ettei URL-osoitteissa ole paikallisia viittauksia

Tämä työnkulku varmistaa, että verkkosivustojen URL-osoitteet eivät sisällä maa-kohtaisia paikallisia viittauksia. Koska tämä repositorio on käytettävissä maailmanlaajuisesti, on tärkeää varmistaa, ettei URL-osoitteissa ole paikallisia viittauksia.

1. Tarkistaaksesi, ettei URL-osoitteissasi ole paikallisia viittauksia, suorita seuraavat tehtävät:

    - Tarkista teksti, kuten `/en-us/`, `/en/`, tai mikä tahansa muu kielikohtainen paikallinen viittaus URL-osoitteissa.
    - Jos näitä ei ole URL-osoitteissasi, läpäiset tämän tarkistuksen.

1. Korjataksesi tämän ongelman, suorita seuraavat tehtävät:
    - Avaa työnkulun korostama tiedostopolku.
    - Poista maa-kohtainen paikallinen viittaus URL-osoitteista.

Kun olet poistanut maa-kohtaisen paikallisen viittauksen, tallenna ja lähetä muutokset.

### Tarkista rikkinäiset URL-osoitteet

Tämä työnkulku varmistaa, että kaikki tiedostojesi verkkosivustojen URL-osoitteet toimivat ja palauttavat 200-tilakoodin.

1. Tarkistaaksesi, että URL-osoitteesi toimivat oikein, suorita seuraavat tehtävät:
    - Tarkista URL-osoitteiden tila tiedostoissasi.

2. Korjataksesi rikkinäiset URL-osoitteet, suorita seuraavat tehtävät:
    - Avaa tiedosto, joka sisältää rikkinäisen URL-osoitteen.
    - Päivitä URL-osoite oikeaksi.

Kun olet korjannut URL-osoitteet, tallenna ja lähetä muutokset.

> [!NOTE]
>
> Saattaa olla tapauksia, joissa URL-tarkistus epäonnistuu, vaikka linkki on käytettävissä. Tämä voi johtua useista syistä, kuten:
>
> - **Verkkorajoitukset:** GitHub Actions -palvelimilla voi olla verkkorajoituksia, jotka estävät pääsyn tiettyihin URL-osoitteisiin.
> - **Aikakatkaisukysymykset:** URL-osoitteet, joiden vastaaminen kestää liian kauan, voivat aiheuttaa aikakatkaisun työnkulussa.
> - **Väliaikaiset palvelinongelmat:** Satunnainen palvelimen käyttökatko tai huolto voi tehdä URL-osoitteen tilapäisesti saavuttamattomaksi tarkistuksen aikana.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virheellisistä tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.