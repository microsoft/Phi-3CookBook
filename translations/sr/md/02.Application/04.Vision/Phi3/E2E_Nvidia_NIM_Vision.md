### Primer Scenario

Zamislite da imate sliku (`demo.png`) i želite da generišete Python kod koji obrađuje ovu sliku i čuva novu verziju iste (`phi-3-vision.jpg`). 

Kod iznad automatizuje ovaj proces tako što:

1. Postavlja okruženje i neophodne konfiguracije.
2. Kreira prompt koji daje instrukcije modelu da generiše potreban Python kod.
3. Šalje prompt modelu i prikuplja generisani kod.
4. Ekstrahuje i izvršava generisani kod.
5. Prikazuje originalnu i obrađenu sliku.

Ovaj pristup koristi snagu veštačke inteligencije kako bi automatizovao zadatke obrade slika, čineći ih jednostavnijim i bržim za postizanje vaših ciljeva.

[Primer rešenja koda](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Hajde da detaljno analiziramo šta ceo kod radi, korak po korak:

1. **Instalacija Potrebnog Paketa**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ova komanda instalira paket `langchain_nvidia_ai_endpoints`, osiguravajući da je u pitanju najnovija verzija.

2. **Uvoz Potrebnih Modula**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ovi uvozi omogućavaju korišćenje potrebnih modula za interakciju sa NVIDIA AI endpointima, sigurno rukovanje lozinkama, interakciju sa operativnim sistemom i kodiranje/dekodiranje podataka u base64 formatu.

3. **Podešavanje API Ključa**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ovaj kod proverava da li je postavljena promenljiva okruženja `NVIDIA_API_KEY`. Ako nije, korisnik se poziva da unese svoj API ključ na siguran način.

4. **Definisanje Modela i Putanje do Slike**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Ovo postavlja model koji će se koristiti, kreira instancu `ChatNVIDIA` sa specificiranim modelom i definiše putanju do fajla sa slikom.

5. **Kreiranje Tekstualnog Prompt-a**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ovo definiše tekstualni prompt koji daje instrukcije modelu da generiše Python kod za obradu slike.

6. **Kodiranje Slike u Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ovaj kod čita fajl sa slikom, kodira ga u base64 formatu i kreira HTML tag za sliku sa kodiranim podacima.

7. **Kombinovanje Teksta i Slike u Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Ovo kombinuje tekstualni prompt i HTML tag slike u jedan string.

8. **Generisanje Koda Korišćenjem ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ovaj kod šalje prompt `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Ekstrakcija Python Koda iz Generisanog Sadržaja**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ovo izdvaja stvarni Python kod iz generisanog sadržaja uklanjanjem markdown formatiranja.

10. **Izvršavanje Generisanog Koda**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ovo izvršava izdvojeni Python kod kao podproces i hvata njegov izlaz.

11. **Prikazivanje Slika**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ove linije prikazuju slike koristeći modul `IPython.display`.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала употребом овог превода.