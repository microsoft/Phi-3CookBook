### Esimerkkitilanne

Kuvittele, että sinulla on kuva (`demo.png`) ja haluat luoda Python-koodin, joka käsittelee tämän kuvan ja tallentaa siitä uuden version (`phi-3-vision.jpg`).

Yllä oleva koodi automatisoi tämän prosessin seuraavasti:

1. Ympäristön ja tarvittavien asetusten määrittäminen.
2. Kehotteen luominen, joka ohjeistaa mallia tuottamaan tarvittavan Python-koodin.
3. Kehotteen lähettäminen mallille ja tuotetun koodin kerääminen.
4. Tuotetun koodin erottaminen ja suorittaminen.
5. Alkuperäisen ja käsitellyn kuvan näyttäminen.

Tämä lähestymistapa hyödyntää tekoälyn voimaa automatisoimaan kuvankäsittelytehtäviä, mikä tekee tavoitteiden saavuttamisesta helpompaa ja nopeampaa.

[Esimerkkikoodiratkaisu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Käydään läpi, mitä koko koodi tekee vaihe vaiheelta:

1. **Asenna vaadittu paketti**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Tämä komento asentaa `langchain_nvidia_ai_endpoints`-paketin varmistaen, että käytössä on uusin versio.

2. **Tuo tarvittavat moduulit**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Nämä tuonnit tuovat käyttöön tarvittavat moduulit NVIDIA AI -päätepisteiden kanssa työskentelyyn, salasanojen turvalliseen käsittelyyn, käyttöjärjestelmän kanssa vuorovaikuttamiseen sekä datan base64-koodaukseen ja -purkamiseen.

3. **Määritä API-avain**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Tämä koodi tarkistaa, onko ympäristömuuttuja `NVIDIA_API_KEY` asetettu. Jos ei, se pyytää käyttäjää syöttämään API-avaimensa turvallisesti.

4. **Määritä malli ja kuvan polku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Tämä asettaa käytettävän mallin, luo `ChatNVIDIA`-instanssin määritellyllä mallilla ja määrittää kuvatiedoston polun.

5. **Luo tekstikehote**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Tämä määrittelee tekstikehotteen, joka ohjeistaa mallia tuottamaan Python-koodia kuvan käsittelyä varten.

6. **Koodaa kuva base64-muotoon**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Tämä koodi lukee kuvatiedoston, koodaa sen base64-muotoon ja luo HTML-kuvatagin koodatulla datalla.

7. **Yhdistä teksti ja kuva kehotteeseen**:
    ```python
    prompt = f"{text} {image}"
    ```
    Tämä yhdistää tekstikehotteen ja HTML-kuvatagin yhdeksi merkkijonoksi.

8. **Luo koodi ChatNVIDIA:n avulla**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Tämä koodi lähettää kehotteen `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-merkkijonolle.

9. **Erota Python-koodi tuotetusta sisällöstä**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Tämä erottelee varsinaisen Python-koodin tuotetusta sisällöstä poistamalla markdown-muotoilut.

10. **Suorita tuotettu koodi**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Tämä suorittaa erotetun Python-koodin aliprosessina ja tallentaa sen tulosteen.

11. **Näytä kuvat**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Nämä rivit näyttävät kuvat käyttäen `IPython.display`-moduulia.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.