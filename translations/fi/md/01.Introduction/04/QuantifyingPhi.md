# **Phi-perheen kvantisointi**

Mallin kvantisointi tarkoittaa prosessia, jossa neuroverkkomallin parametrit (kuten painot ja aktivaatioarvot) muunnetaan suuresta arvojoukosta (yleensä jatkuvasta arvojoukosta) pienempään, rajalliseen arvojoukkoon. Tämä tekniikka voi pienentää mallin kokoa ja laskennallista monimutkaisuutta sekä parantaa mallin suorituskykyä resurssirajoitteisissa ympäristöissä, kuten mobiililaitteissa tai sulautetuissa järjestelmissä. Kvantisointi saavuttaa tiivistyksen vähentämällä parametrien tarkkuutta, mutta se tuo mukanaan myös jonkin verran tarkkuuden menetystä. Siksi kvantisointiprosessissa on tärkeää tasapainottaa mallin koko, laskennallinen monimutkaisuus ja tarkkuus. Yleisiä kvantisointimenetelmiä ovat esimerkiksi kiintopiste- ja liukulukukvantisointi. Sopiva kvantisointistrategia tulisi valita käyttötapauksen ja tarpeiden mukaan.

Tavoitteenamme on ottaa GenAI-malli käyttöön reunalaitteissa ja mahdollistaa useampien laitteiden pääsy GenAI-skenaarioihin, kuten mobiililaitteisiin, AI-tietokoneisiin/Copilot-tietokoneisiin ja perinteisiin IoT-laitteisiin. Kvantisointimallin avulla voimme ottaa sen käyttöön eri reunalaitteissa laitekohtaisesti. Yhdistämällä laitevalmistajien tarjoamat mallikiihdytysratkaisut ja kvantisointimallit voimme rakentaa parempia SLM-sovellusskenaarioita.

Kvantisointiskenaariossa käytössämme on eri tarkkuuksia (INT4, INT8, FP16, FP32). Alla on selitetty yleisesti käytetyt kvantisointitarkkuudet.

### **INT4**

INT4-kvantisointi on radikaali menetelmä, jossa mallin painot ja aktivaatioarvot kvantisoidaan 4-bittisiksi kokonaisluvuiksi. INT4-kvantisointi johtaa yleensä suurempaan tarkkuuden menetykseen pienemmän edustusalueen ja alhaisemman tarkkuuden vuoksi. Verrattuna INT8-kvantisointiin, INT4 voi kuitenkin edelleen vähentää mallin tallennusvaatimuksia ja laskennallista monimutkaisuutta. On kuitenkin huomattava, että INT4-kvantisointi on käytännön sovelluksissa melko harvinaista, koska liian alhainen tarkkuus voi heikentää mallin suorituskykyä merkittävästi. Lisäksi kaikki laitteistot eivät tue INT4-toimintoja, joten laitteiston yhteensopivuus on huomioitava kvantisointimenetelmää valittaessa.

### **INT8**

INT8-kvantisointi muuntaa mallin painot ja aktivoinnit liukuluvuista 8-bittisiksi kokonaisluvuiksi. Vaikka INT8:n edustama lukuarvojen alue on pienempi ja vähemmän tarkka, se voi merkittävästi vähentää tallennus- ja laskentavaatimuksia. INT8-kvantisoinnissa mallin painot ja aktivaatioarvot käyvät läpi kvantisointiprosessin, johon kuuluu skaalaus ja siirtymä, jotta alkuperäinen liukulukuinformaatio säilyy mahdollisimman hyvin. Inferenssin aikana nämä kvantisoidut arvot muunnetaan takaisin liukuluvuiksi laskentaa varten ja kvantisoidaan sitten uudelleen INT8-muotoon seuraavaa vaihetta varten. Tämä menetelmä tarjoaa riittävän tarkkuuden useimmissa sovelluksissa ja säilyttää samalla korkean laskentatehokkuuden.

### **FP16**

FP16-formaatti, eli 16-bittiset liukuluvut (float16), vähentää muistin käyttöä puoleen verrattuna 32-bittisiin liukulukuihin (float32), mikä on merkittävä etu suurten syväoppimissovellusten yhteydessä. FP16 mahdollistaa suurempien mallien lataamisen tai suuremman tietomäärän käsittelyn samojen GPU-muistirajoitusten puitteissa. Kun moderni GPU-laitteisto tukee yhä enemmän FP16-toimintoja, FP16:n käyttö voi myös parantaa laskentanopeutta. FP16:lla on kuitenkin omat haittansa, kuten alhaisempi tarkkuus, mikä voi joissain tapauksissa johtaa numeeriseen epävakauteen tai tarkkuuden menetykseen.

### **FP32**

FP32-formaatti tarjoaa korkeamman tarkkuuden ja pystyy esittämään laajan arvojoukon tarkasti. Kun suoritetaan monimutkaisia matemaattisia operaatioita tai tarvitaan erittäin tarkkoja tuloksia, FP32 on ensisijainen valinta. Korkea tarkkuus tarkoittaa kuitenkin myös suurempaa muistin käyttöä ja pidempiä laskenta-aikoja. Suurten syväoppimismallien kohdalla, erityisesti kun mallin parametreja ja tietomäärää on paljon, FP32 voi johtaa GPU-muistin riittämättömyyteen tai inferenssinopeuden hidastumiseen.

Mobiililaitteissa tai IoT-laitteissa voimme muuntaa Phi-3.x-mallit INT4-muotoon, kun taas AI-tietokoneet / Copilot-tietokoneet voivat käyttää tarkempia muotoja, kuten INT8, FP16 tai FP32.

Tällä hetkellä eri laitevalmistajilla on erilaisia kehyksiä generatiivisten mallien tukemiseen, kuten Intelin OpenVINO, Qualcommin QNN, Applen MLX ja Nvidian CUDA. Näitä voidaan yhdistää kvantisointiin paikallista käyttöönottoa varten.

Teknisestä näkökulmasta kvantisoinnin jälkeen on saatavilla eri formaattien tuki, kuten PyTorch / TensorFlow -formaatit, GGUF ja ONNX. Olen tehnyt vertailun GGUF:n ja ONNX:n välillä sekä niiden käyttöskenaarioista. Suosittelen ONNX-kvantisointiformaattia, joka tarjoaa hyvän tuen mallikehyksestä laitteistoon. Tässä luvussa keskitymme ONNX Runtimeen GenAI:lle, OpenVINOon ja Applen MLX:ään mallien kvantisointia varten (jos sinulla on parempi tapa, voit lähettää sen meille PR:nä).

**Tämä luku sisältää**

1. [Phi-3.5 / 4 kvantisointi käyttämällä llama.cpp:ää](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantisointi käyttämällä Generative AI -laajennuksia onnxruntimeen](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantisointi käyttämällä Intel OpenVINOa](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantisointi käyttämällä Apple MLX Frameworkia](./UsingAppleMLXQuantifyingPhi.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälykäännöspalveluita käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.