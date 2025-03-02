### Exempelscenario

Föreställ dig att du har en bild (`demo.png`) och att du vill generera Python-kod som bearbetar denna bild och sparar en ny version av den (`phi-3-vision.jpg`).

Koden ovan automatiserar denna process genom att:

1. Ställa in miljön och nödvändiga konfigurationer.
2. Skapa en prompt som instruerar modellen att generera den önskade Python-koden.
3. Skicka prompten till modellen och samla in den genererade koden.
4. Extrahera och köra den genererade koden.
5. Visa den ursprungliga och bearbetade bilden.

Den här metoden utnyttjar kraften hos AI för att automatisera bildbearbetningsuppgifter, vilket gör det enklare och snabbare att nå dina mål.

[Exempel på kodlösning](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Låt oss gå igenom vad hela koden gör steg för steg:

1. **Installera nödvändigt paket**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Detta kommando installerar paketet `langchain_nvidia_ai_endpoints` och ser till att det är den senaste versionen.

2. **Importera nödvändiga moduler**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Dessa importeringar inkluderar de moduler som krävs för att interagera med NVIDIA AI-endpoints, hantera lösenord säkert, interagera med operativsystemet och koda/avkoda data i base64-format.

3. **Ställ in API-nyckel**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Den här koden kontrollerar om miljövariabeln `NVIDIA_API_KEY` är inställd. Om inte, uppmanas användaren att ange sin API-nyckel säkert.

4. **Definiera modell och bildsökväg**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Detta anger vilken modell som ska användas, skapar en instans av `ChatNVIDIA` med den specificerade modellen och definierar sökvägen till bildfilen.

5. **Skapa textprompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Detta definierar en textprompt som instruerar modellen att generera Python-kod för att bearbeta en bild.

6. **Koda bilden i Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Den här koden läser bildfilen, kodar den i base64 och skapar en HTML-bildtagg med den kodade datan.

7. **Kombinera text och bild i prompten**:
    ```python
    prompt = f"{text} {image}"
    ```
    Detta kombinerar textprompten och HTML-bildtaggen till en enda sträng.

8. **Generera kod med ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Den här koden skickar prompten till `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-strängen.

9. **Extrahera Python-kod från genererat innehåll**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Detta extraherar den faktiska Python-koden från det genererade innehållet genom att ta bort markdown-formateringen.

10. **Kör den genererade koden**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Detta kör den extraherade Python-koden som en subprocess och fångar dess output.

11. **Visa bilder**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Dessa rader visar bilderna med hjälp av modulen `IPython.display`.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.