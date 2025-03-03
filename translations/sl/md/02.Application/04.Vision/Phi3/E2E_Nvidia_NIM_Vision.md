### Primer scenarij

Predstavljajte si, da imate sliko (`demo.png`) in želite ustvariti Python kodo, ki obdeluje to sliko in shrani njeno novo različico (`phi-3-vision.jpg`).

Zgornja koda avtomatizira ta proces z naslednjimi koraki:

1. Nastavi okolje in potrebne konfiguracije.
2. Ustvari poziv, ki modelu naroči, naj generira zahtevano Python kodo.
3. Pošlje poziv modelu in zbere generirano kodo.
4. Izlušči in zažene generirano kodo.
5. Prikaže izvirno in obdelano sliko.

Ta pristop izkorišča moč umetne inteligence za avtomatizacijo nalog obdelave slik, kar omogoča hitrejše in enostavnejše doseganje ciljev.

[Rešitev s primerom kode](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Poglejmo podrobneje, kaj celotna koda počne, korak za korakom:

1. **Namestitev potrebnega paketa**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ta ukaz namesti paket `langchain_nvidia_ai_endpoints` in zagotovi, da je najnovejša različica.

2. **Uvoz potrebnih modulov**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ti uvozi omogočajo interakcijo z NVIDIA AI endpoints, varno ravnanje z gesli, delo z operacijskim sistemom ter kodiranje/dekodiranje podatkov v formatu base64.

3. **Nastavitev API ključa**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ta koda preveri, ali je okoljska spremenljivka `NVIDIA_API_KEY` nastavljena. Če ni, uporabnika pozove, da varno vnese svoj API ključ.

4. **Določitev modela in poti slike**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Določi model, ki se bo uporabljal, ustvari instanco `ChatNVIDIA` z izbranim modelom in določi pot do slikovne datoteke.

5. **Ustvarjanje besedilnega poziva**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ta del kode definira besedilni poziv, ki modelu naroči, naj generira Python kodo za obdelavo slike.

6. **Kodiranje slike v base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ta koda prebere slikovno datoteko, jo kodira v base64 in ustvari HTML oznako slike z zakodiranimi podatki.

7. **Združitev besedila in slike v poziv**:
    ```python
    prompt = f"{text} {image}"
    ```
    Združi besedilni poziv in HTML oznako slike v eno samo besedilo.

8. **Generiranje kode z uporabo ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ta koda pošlje poziv funkciji `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` niz.

9. **Izluščitev Python kode iz generirane vsebine**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Iz generirane vsebine izloči dejansko Python kodo tako, da odstrani markdown oblikovanje.

10. **Zagon generirane kode**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ta del kode zažene izluščeno Python kodo kot podproces in zajame njen izhod.

11. **Prikaz slik**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ti ukazi prikažejo slike z uporabo modula `IPython.display`.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.