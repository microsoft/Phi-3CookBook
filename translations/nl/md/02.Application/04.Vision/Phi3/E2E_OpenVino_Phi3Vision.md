Deze demo laat zien hoe je een voorgetraind model kunt gebruiken om Python-code te genereren op basis van een afbeelding en een tekstprompt.

[Voorbeeldcode](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hier is een stapsgewijze uitleg:

1. **Imports en Setup**:
   - De benodigde bibliotheken en modules worden geïmporteerd, waaronder `requests`, `PIL` voor beeldverwerking, en `transformers` voor het omgaan met het model en de verwerking.

2. **Afbeelding Laden en Weergeven**:
   - Een afbeeldingsbestand (`demo.png`) wordt geopend met behulp van de bibliotheek `PIL` en weergegeven.

3. **De Prompt Definiëren**:
   - Een bericht wordt gemaakt dat de afbeelding bevat en een verzoek om Python-code te genereren om de afbeelding te verwerken en op te slaan met `plt` (matplotlib).

4. **De Processor Laden**:
   - De `AutoProcessor` wordt geladen vanuit een voorgetraind model dat is gespecificeerd in de `out_dir`-directory. Deze processor verwerkt de tekst- en afbeeldingsinvoer.

5. **De Prompt Maken**:
   - De `apply_chat_template`-methode wordt gebruikt om het bericht te formatteren tot een prompt die geschikt is voor het model.

6. **De Invoer Verwerken**:
   - De prompt en afbeelding worden verwerkt tot tensors die door het model kunnen worden begrepen.

7. **Generatieargumenten Instellen**:
   - Argumenten voor het generatieproces van het model worden gedefinieerd, waaronder het maximale aantal nieuwe tokens dat moet worden gegenereerd en of de uitvoer moet worden gesampled.

8. **De Code Genereren**:
   - Het model genereert de Python-code op basis van de invoer en generatieargumenten. De `TextStreamer` wordt gebruikt om de uitvoer te verwerken, waarbij de prompt en speciale tokens worden overgeslagen.

9. **Uitvoer**:
   - De gegenereerde code wordt afgedrukt, die Python-code zou moeten bevatten om de afbeelding te verwerken en op te slaan zoals gespecificeerd in de prompt.

Deze demo laat zien hoe je een voorgetraind model kunt gebruiken met OpenVino om dynamisch code te genereren op basis van gebruikersinvoer en afbeeldingen.

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gestuurde vertaaldiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.