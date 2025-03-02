### Scenariu Exemplu

Imaginează-ți că ai o imagine (`demo.png`) și vrei să generezi cod Python care să proceseze această imagine și să salveze o versiune nouă a acesteia (`phi-3-vision.jpg`). 

Codul de mai sus automatizează acest proces prin:

1. Configurarea mediului și a setărilor necesare.
2. Crearea unui prompt care instruiește modelul să genereze codul Python necesar.
3. Trimiterea promptului către model și colectarea codului generat.
4. Extracția și rularea codului generat.
5. Afișarea imaginilor originale și procesate.

Această abordare valorifică puterea AI pentru a automatiza sarcinile de procesare a imaginilor, făcând mai ușor și mai rapid să îți atingi obiectivele.

[Exemplu de Soluție Cod](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Să descompunem ce face întregul cod, pas cu pas:

1. **Instalează Pachetul Necesitar**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Această comandă instalează pachetul `langchain_nvidia_ai_endpoints`, asigurându-se că este cea mai recentă versiune.

2. **Importă Modulele Necesare**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Aceste importuri aduc modulele necesare pentru interacțiunea cu punctele finale NVIDIA AI, gestionarea securizată a parolelor, interacțiunea cu sistemul de operare și codificarea/decodificarea datelor în format base64.

3. **Configurează Cheia API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Acest cod verifică dacă variabila de mediu `NVIDIA_API_KEY` este setată. Dacă nu, solicită utilizatorului să introducă cheia API în mod securizat.

4. **Definește Modelul și Calea Imaginilor**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Se setează modelul care va fi utilizat, se creează o instanță de `ChatNVIDIA` cu modelul specificat și se definește calea către fișierul imaginii.

5. **Creează Prompt-ul Text**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Se definește un prompt text care instruiește modelul să genereze cod Python pentru procesarea unei imagini.

6. **Codifică Imaginea în Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Acest cod citește fișierul imaginii, îl codifică în base64 și creează un tag HTML pentru imagine cu datele codificate.

7. **Combină Textul și Imaginea în Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Se combină prompt-ul text și tag-ul HTML al imaginii într-un singur șir de caractere.

8. **Generează Cod Folosind ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Acest cod trimite prompt-ul către `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extrage Codul Python din Conținutul Generat**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Se extrage codul Python efectiv din conținutul generat prin eliminarea formatării markdown.

10. **Rulează Codul Generat**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Se rulează codul Python extras ca un subprocess și se capturează rezultatul acestuia.

11. **Afișează Imaginile**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Aceste linii afișează imaginile folosind modulul `IPython.display`.

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.