Tämä demo näyttää, miten esikoulutettua mallia voidaan käyttää Python-koodin luomiseen kuvan ja tekstikuvauksen perusteella.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tässä vaiheittainen selitys:

1. **Kirjastojen ja asetusten lataaminen**:
   - Tarvittavat kirjastot ja moduulit tuodaan, mukaan lukien `requests`, `PIL` kuvankäsittelyyn sekä `transformers` mallin käsittelyyn ja prosessointiin.

2. **Kuvan lataaminen ja näyttäminen**:
   - Kuvatiedosto (`demo.png`) avataan käyttämällä `PIL`-kirjastoa ja näytetään.

3. **Kuvauksen määrittäminen**:
   - Luodaan viesti, joka sisältää kuvan ja pyynnön luoda Python-koodia kuvan käsittelyyn ja sen tallentamiseen käyttäen `plt` (matplotlib).

4. **Prosessorin lataaminen**:
   - `AutoProcessor` ladataan esikoulutetusta mallista, joka sijaitsee `out_dir`-hakemistossa. Tämä prosessori käsittelee teksti- ja kuva-syötteet.

5. **Kuvauksen luominen**:
   - `apply_chat_template`-metodia käytetään muotoilemaan viesti mallille sopivaksi kuvaukseksi.

6. **Syötteiden prosessointi**:
   - Kuvaus ja kuva muunnetaan tensoreiksi, joita malli pystyy ymmärtämään.

7. **Generointiparametrien asettaminen**:
   - Määritetään mallin generointiprosessin parametrit, mukaan lukien suurin määrä uusia luotavia tokeneita ja käytetäänkö satunnaisotantaa.

8. **Koodin generointi**:
   - Malli luo Python-koodin syötteiden ja generointiparametrien perusteella. `TextStreamer`-metodia käytetään tuloksen käsittelyyn, ohittaen kuvauksen ja erikoismerkit.

9. **Tuloste**:
   - Luotu koodi tulostetaan, ja sen pitäisi sisältää Python-koodi, joka käsittelee kuvan ja tallentaa sen kuvauksessa määritetyllä tavalla.

Tämä demo havainnollistaa, miten esikoulutettua mallia voidaan hyödyntää OpenVinon avulla koodin dynaamiseen generointiin käyttäjän syötteiden ja kuvien perusteella.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisten tekoälykäännöspalveluiden avulla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.