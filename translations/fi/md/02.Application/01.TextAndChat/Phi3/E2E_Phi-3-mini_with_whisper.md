# Interaktiivinen Phi 3 Mini 4K Instruct Chatbot Whisperillä

## Yleiskatsaus

Interaktiivinen Phi 3 Mini 4K Instruct Chatbot on työkalu, jonka avulla käyttäjät voivat olla vuorovaikutuksessa Microsoft Phi 3 Mini 4K -ohjeiden demon kanssa käyttäen joko tekstin tai äänen syötettä. Chatbotia voi käyttää monenlaisiin tehtäviin, kuten kääntämiseen, sääpäivityksiin ja yleiseen tiedonhakuun.

### Aloittaminen

Voit käyttää tätä chatbotia seuraamalla näitä ohjeita:

1. Avaa uusi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Notebookin pääikkunassa näet keskustelukäyttöliittymän, jossa on tekstinsyöttökenttä ja "Lähetä"-painike.
3. Käyttääksesi tekstipohjaista chatbotia, kirjoita viestisi tekstinsyöttökenttään ja napsauta "Lähetä"-painiketta. Chatbot vastaa äänitiedostolla, jota voi toistaa suoraan notebookista.

**Huomio**: Tämä työkalu vaatii GPU:n sekä pääsyn Microsoft Phi-3- ja OpenAI Whisper -malleihin, joita käytetään puheentunnistukseen ja kääntämiseen.

### GPU-vaatimukset

Tämän demon suorittamiseen tarvitset 12 GB GPU-muistia.

Microsoft-Phi-3-Mini-4K -ohjeiden demon GPU-suorituskyvyn vaatimukset riippuvat useista tekijöistä, kuten syötteen koosta (ääni tai teksti), käytetystä kielestä, mallin nopeudesta ja GPU:n käytettävissä olevasta muistista.

Yleisesti ottaen Whisper-malli on suunniteltu toimimaan GPU:illa. Suositeltu vähimmäismuisti Whisper-mallille on 8 GB, mutta se voi hyödyntää suurempia muistimääriä tarpeen mukaan.

On tärkeää huomata, että suuren datamäärän tai korkean pyyntövolyymin käsittely mallilla voi vaatia enemmän GPU-muistia ja/tai aiheuttaa suorituskykyongelmia. On suositeltavaa testata käyttötapausta eri kokoonpanoilla ja seurata muistin käyttöä optimaalisten asetusten määrittämiseksi.

## E2E-esimerkki Interaktiivisesta Phi 3 Mini 4K Instruct Chatbotista Whisperillä

Jupyter-notebook nimeltä [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) havainnollistaa, kuinka käyttää Microsoft Phi 3 Mini 4K -ohjeiden demoa tekstin tuottamiseen ääni- tai tekstisyötteestä. Notebook määrittelee useita toimintoja:

1. `tts_file_name(text)`: Tämä funktio luo tiedostonimen syötetyn tekstin perusteella tallentaakseen luodun äänitiedoston.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Tämä funktio käyttää Edge TTS -rajapintaa luodakseen äänitiedoston syötetekstin osista. Parametrit ovat osalista, puhenopeus, äänen nimi ja tiedostopolku, johon äänitiedosto tallennetaan.
3. `talk(input_text)`: Tämä funktio luo äänitiedoston käyttämällä Edge TTS -rajapintaa ja tallentaa sen satunnaisella tiedostonimellä hakemistoon /content/audio. Parametri on syöteteksti, joka muunnetaan puheeksi.
4. `run_text_prompt(message, chat_history)`: Tämä funktio käyttää Microsoft Phi 3 Mini 4K -ohjeiden demoa luodakseen äänitiedoston viestisyötteestä ja lisää sen keskusteluhistoriaan.
5. `run_audio_prompt(audio, chat_history)`: Tämä funktio muuntaa äänitiedoston tekstiksi käyttämällä Whisper-mallin rajapintaa ja välittää sen `run_text_prompt()`-funktiolle.
6. Koodi käynnistää Gradio-sovelluksen, jonka avulla käyttäjät voivat olla vuorovaikutuksessa Phi 3 Mini 4K -ohjeiden demon kanssa joko kirjoittamalla viestejä tai lataamalla äänitiedostoja. Tulokset näytetään tekstiviestinä sovelluksessa.

## Vianmääritys

Cuda GPU -ajurien asentaminen

1. Varmista, että Linux-sovelluksesi ovat ajan tasalla

    ```bash
    sudo apt update
    ```

2. Asenna Cuda-ajurit

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Rekisteröi Cuda-ajurin sijainti

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Tarkista Nvidia GPU -muistin koko (vaaditaan 12 GB GPU-muistia)

    ```bash
    nvidia-smi
    ```

5. Tyhjennä välimuisti: Jos käytät PyTorchia, voit kutsua torch.cuda.empty_cache(), jotta kaikki käyttämättömät välimuistitettu muisti vapautuu muiden GPU-sovellusten käyttöön.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Tarkista Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. Suorita seuraavat tehtävät luodaksesi Hugging Face -tokenin.

    - Siirry [Hugging Face Token Settings -sivulle](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Valitse **New token**.
    - Syötä projektin **Nimi**, jota haluat käyttää.
    - Valitse **Type** arvoksi **Write**.

> **Huomio**
>
> Jos kohtaat seuraavan virheen:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ratkaistaksesi tämän, kirjoita seuraava komento terminaaliisi.
>
> ```bash
> sudo ldconfig
> ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälyyn perustuvia käännöspalveluja käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.