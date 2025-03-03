### Voorbeeldscenario

Stel je hebt een afbeelding (`demo.png`) en je wilt Python-code genereren die deze afbeelding verwerkt en een nieuwe versie ervan opslaat (`phi-3-vision.jpg`).

De bovenstaande code automatiseert dit proces door:

1. Het instellen van de omgeving en benodigde configuraties.
2. Het maken van een prompt die het model instrueert om de vereiste Python-code te genereren.
3. Het verzenden van de prompt naar het model en het verzamelen van de gegenereerde code.
4. Het extraheren en uitvoeren van de gegenereerde code.
5. Het weergeven van de originele en verwerkte afbeeldingen.

Deze aanpak maakt gebruik van de kracht van AI om taken voor beeldverwerking te automatiseren, waardoor je doelen eenvoudiger en sneller bereikt kunnen worden.

[Voorbeeldoplossing Code](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Laten we stap voor stap bekijken wat de volledige code doet:

1. **Vereiste Pakket Installeren**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Deze opdracht installeert het pakket `langchain_nvidia_ai_endpoints` en zorgt ervoor dat het de nieuwste versie is.

2. **Benodigde Modules Importeren**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Deze imports halen de benodigde modules binnen voor interactie met de NVIDIA AI-eindpunten, het veilig omgaan met wachtwoorden, interactie met het besturingssysteem en het coderen/decoderen van gegevens in base64-formaat.

3. **API-sleutel Instellen**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Deze code controleert of de omgevingsvariabele `NVIDIA_API_KEY` is ingesteld. Zo niet, dan vraagt het de gebruiker om hun API-sleutel veilig in te voeren.

4. **Model en Afbeeldingspad Definiëren**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Dit stelt het te gebruiken model in, maakt een instantie van `ChatNVIDIA` met het gespecificeerde model en definieert het pad naar het afbeeldingsbestand.

5. **Tekstprompt Maken**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Dit definieert een tekstprompt die het model instrueert om Python-code te genereren voor het verwerken van een afbeelding.

6. **Afbeelding Coderen in Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Deze code leest het afbeeldingsbestand, codeert het in base64 en maakt een HTML-afbeeldingstag met de gecodeerde gegevens.

7. **Tekst en Afbeelding Combineren in Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Dit combineert de tekstprompt en de HTML-afbeeldingstag tot één string.

8. **Code Genereren met ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Deze code stuurt de prompt naar `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Python-code Uit de Gegeneerde Inhoud Halen**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Dit haalt de daadwerkelijke Python-code uit de gegenereerde inhoud door de markdown-opmaak te verwijderen.

10. **De Gegeneerde Code Uitvoeren**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Dit voert de geëxtraheerde Python-code uit als een subprocess en legt de uitvoer vast.

11. **Afbeeldingen Weergeven**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Deze regels tonen de afbeeldingen met behulp van de module `IPython.display`.

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gebaseerde vertaaldiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.