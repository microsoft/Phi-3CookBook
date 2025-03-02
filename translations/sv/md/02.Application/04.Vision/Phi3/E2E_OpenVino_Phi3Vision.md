Den här demon visar hur man använder en förtränad modell för att generera Python-kod baserat på en bild och en textprompt.

[Exempelkod](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Här är en steg-för-steg-förklaring:

1. **Import och Inställning**:
   - De nödvändiga biblioteken och modulerna importeras, inklusive `requests`, `PIL` för bildbearbetning, och `transformers` för att hantera modellen och bearbetningen.

2. **Laddning och Visning av Bilden**:
   - En bildfil (`demo.png`) öppnas med hjälp av `PIL`-biblioteket och visas.

3. **Definiera Prompten**:
   - Ett meddelande skapas som inkluderar bilden och en begäran om att generera Python-kod för att bearbeta bilden och spara den med `plt` (matplotlib).

4. **Ladda Processorn**:
   - `AutoProcessor` laddas från en förtränad modell som anges av `out_dir`-katalogen. Den här processorn hanterar text- och bildinmatningar.

5. **Skapa Prompten**:
   - `apply_chat_template`-metoden används för att formatera meddelandet till en prompt som modellen kan använda.

6. **Bearbeta Inmatningarna**:
   - Prompten och bilden bearbetas till tensorer som modellen kan förstå.

7. **Ställa in Genereringsargument**:
   - Argument för modellens genereringsprocess definieras, inklusive det maximala antalet nya tokens som ska genereras och om utdata ska sampelas.

8. **Generera Koden**:
   - Modellen genererar Python-koden baserat på inmatningarna och genereringsargumenten. `TextStreamer` används för att hantera utdata, hoppa över prompten och specialtecken.

9. **Utdata**:
   - Den genererade koden skrivs ut och ska innehålla Python-kod för att bearbeta bilden och spara den enligt specifikationerna i prompten.

Den här demon visar hur man kan använda en förtränad modell med OpenVino för att dynamiskt generera kod baserat på användarinmatningar och bilder.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.