### Primjer scenarija

Zamislite da imate sliku (`demo.png`) i želite generirati Python kod koji obrađuje tu sliku i sprema novu verziju (`phi-3-vision.jpg`).

Gornji kod automatizira ovaj proces na sljedeći način:

1. Postavljanje okruženja i potrebnih konfiguracija.
2. Kreiranje upita koji modelu daje upute za generiranje potrebnog Python koda.
3. Slanje upita modelu i prikupljanje generiranog koda.
4. Ekstrakcija i pokretanje generiranog koda.
5. Prikaz originalne i obrađene slike.

Ovaj pristup koristi snagu umjetne inteligencije za automatizaciju zadataka obrade slika, čineći ih bržima i jednostavnijima za postizanje vaših ciljeva.

[Primjer rješenja koda](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Razmotrimo što cijeli kod radi korak po korak:

1. **Instalirajte potreban paket**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ova naredba instalira paket `langchain_nvidia_ai_endpoints`, osiguravajući da je najnovija verzija.

2. **Uvezite potrebne module**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ovi uvozi omogućuju rad s NVIDIA AI endpointima, sigurno upravljanje lozinkama, interakciju s operativnim sustavom te kodiranje i dekodiranje podataka u base64 formatu.

3. **Postavite API ključ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ovaj kod provjerava je li postavljena varijabla okruženja `NVIDIA_API_KEY`. Ako nije, korisnika se traži da unese svoj API ključ na siguran način.

4. **Definirajte model i putanju slike**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Ovo postavlja model koji će se koristiti, stvara instancu `ChatNVIDIA` s odabranim modelom i definira putanju do datoteke slike.

5. **Kreirajte tekstualni upit**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ovo definira tekstualni upit koji daje modelu upute za generiranje Python koda za obradu slike.

6. **Kodirajte sliku u Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ovaj kod čita datoteku slike, kodira je u base64 formatu i kreira HTML oznaku slike s kodiranim podacima.

7. **Kombinirajte tekst i sliku u upit**:
    ```python
    prompt = f"{text} {image}"
    ```
    Ovo kombinira tekstualni upit i HTML oznaku slike u jedan string.

8. **Generirajte kod pomoću ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ovaj kod šalje upit `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Ekstrahirajte Python kod iz generiranog sadržaja**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ovo ekstrahira stvarni Python kod iz generiranog sadržaja uklanjanjem markdown formatiranja.

10. **Pokrenite generirani kod**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ovaj dio pokreće ekstrahirani Python kod kao podproces i bilježi njegov izlaz.

11. **Prikažite slike**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ove linije prikazuju slike koristeći modul `IPython.display`.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prijevoda. Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne snosimo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.