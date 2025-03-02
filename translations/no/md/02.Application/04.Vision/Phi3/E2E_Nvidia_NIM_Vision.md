### Eksempelscenario

Tenk deg at du har et bilde (`demo.png`) og ønsker å generere Python-kode som prosesserer dette bildet og lagrer en ny versjon av det (`phi-3-vision.jpg`).

Koden ovenfor automatiserer denne prosessen ved å:

1. Sette opp miljøet og nødvendige konfigurasjoner.
2. Lage en prompt som instruerer modellen til å generere den nødvendige Python-koden.
3. Sende prompten til modellen og hente ut den genererte koden.
4. Ekstrahere og kjøre den genererte koden.
5. Vise det originale og det prosesserte bildet.

Denne tilnærmingen utnytter AI for å automatisere bildebehandlingsoppgaver, noe som gjør det enklere og raskere å oppnå målene dine.

[Eksempelløsning i kode](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

La oss gå gjennom hva hele koden gjør, steg for steg:

1. **Installer nødvendig pakke**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Denne kommandoen installerer `langchain_nvidia_ai_endpoints`-pakken og sørger for at det er den nyeste versjonen.

2. **Importer nødvendige moduler**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Disse importene henter inn nødvendige moduler for å samhandle med NVIDIA AI-endepunkter, håndtere passord sikkert, samhandle med operativsystemet og kode/dekode data i base64-format.

3. **Sett opp API-nøkkel**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Denne koden sjekker om miljøvariabelen `NVIDIA_API_KEY` er satt. Hvis ikke, ber den brukeren om å skrive inn API-nøkkelen sin på en sikker måte.

4. **Definer modell og bildebane**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Dette setter modellen som skal brukes, oppretter en instans av `ChatNVIDIA` med den spesifiserte modellen, og definerer banen til bildefilen.

5. **Lag tekstprompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Denne definerer en tekstprompt som instruerer modellen til å generere Python-kode for bildebehandling.

6. **Koder bildet i Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Denne koden leser bildefilen, koder den i base64 og lager en HTML-bildetagg med de kodede dataene.

7. **Kombiner tekst og bilde i prompten**:
    ```python
    prompt = f"{text} {image}"
    ```
    Dette kombinerer tekstprompten og HTML-bildetaggen til én enkelt streng.

8. **Generer kode med ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Denne koden sender prompten til `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-strengen.

9. **Ekstraher Python-kode fra generert innhold**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Dette ekstraherer den faktiske Python-koden fra det genererte innholdet ved å fjerne markdown-formateringen.

10. **Kjør den genererte koden**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Dette kjører den ekstraherte Python-koden som en subprocess og fanger opp utdataene.

11. **Vis bilder**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Disse linjene viser bildene ved hjelp av `IPython.display`-modulen.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi bestreber oss på nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.