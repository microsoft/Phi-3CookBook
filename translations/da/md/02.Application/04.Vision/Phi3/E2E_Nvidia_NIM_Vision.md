### Eksempel Scenarie

Forestil dig, at du har et billede (`demo.png`), og du ønsker at generere Python-kode, der behandler dette billede og gemmer en ny version af det (`phi-3-vision.jpg`).

Koden ovenfor automatiserer denne proces ved at:

1. Opsætte miljøet og de nødvendige konfigurationer.
2. Oprette en prompt, der instruerer modellen til at generere den ønskede Python-kode.
3. Sende prompten til modellen og indsamle den genererede kode.
4. Udpakke og køre den genererede kode.
5. Vise de originale og behandlede billeder.

Denne tilgang udnytter AI's kraft til at automatisere billedbehandlingsopgaver, hvilket gør det nemmere og hurtigere at nå dine mål.

[Eksempel på Kodeløsning](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Lad os gennemgå, hvad hele koden gør, trin for trin:

1. **Installer Nødvendig Pakke**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Denne kommando installerer pakken `langchain_nvidia_ai_endpoints` og sikrer, at det er den nyeste version.

2. **Importer Nødvendige Moduler**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Disse imports bringer de nødvendige moduler ind til at interagere med NVIDIA AI-endpoints, håndtere adgangskoder sikkert, interagere med operativsystemet og kode/dekode data i base64-format.

3. **Opsæt API-nøgle**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Denne kode tjekker, om miljøvariablen `NVIDIA_API_KEY` er sat. Hvis ikke, beder den brugeren om at indtaste deres API-nøgle sikkert.

4. **Definer Model og Billedsti**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Dette angiver den model, der skal bruges, opretter en instans af `ChatNVIDIA` med den specificerede model og definerer stien til billedfilen.

5. **Opret Tekstprompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Dette definerer en tekstprompt, der instruerer modellen til at generere Python-kode til billedbehandling.

6. **Kod Billedet i Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Denne kode læser billedfilen, koder den i base64 og opretter et HTML-billedtag med de kodede data.

7. **Kombiner Tekst og Billede i Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Dette kombinerer tekstprompten og HTML-billedtagget til en enkelt streng.

8. **Generer Kode med ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Denne kode sender prompten til `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-strengen.

9. **Udpak Python-kode fra Genereret Indhold**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Dette udtrækker den faktiske Python-kode fra det genererede indhold ved at fjerne markdown-formatet.

10. **Kør den Genererede Kode**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Denne kører den udpakkede Python-kode som en subprocess og fanger dens output.

11. **Vis Billeder**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Disse linjer viser billederne ved hjælp af modulet `IPython.display`.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.