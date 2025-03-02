Denne demoen viser hvordan man bruker en forhåndstrent modell til å generere Python-kode basert på et bilde og en tekstprompt.

[Eksempelkode](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Her er en steg-for-steg forklaring:

1. **Imports og oppsett**:
   - De nødvendige bibliotekene og modulene importeres, inkludert `requests`, `PIL` for bildebehandling, og `transformers` for håndtering av modellen og prosessering.

2. **Laste inn og vise bildet**:
   - En bildefil (`demo.png`) åpnes ved hjelp av biblioteket `PIL` og vises.

3. **Definere prompten**:
   - En melding opprettes som inkluderer bildet og en forespørsel om å generere Python-kode for å behandle bildet og lagre det ved hjelp av `plt` (matplotlib).

4. **Laste inn prosessoren**:
   - `AutoProcessor` lastes inn fra en forhåndstrent modell spesifisert av katalogen `out_dir`. Denne prosessoren håndterer tekst- og bildeinput.

5. **Opprette prompten**:
   - Metoden `apply_chat_template` brukes til å formatere meldingen til en prompt som modellen kan bruke.

6. **Prosessere inputene**:
   - Prompten og bildet prosesseres til tensorer som modellen kan forstå.

7. **Definere genereringsargumenter**:
   - Argumenter for modellens genereringsprosess defineres, inkludert maksimalt antall nye tokens som skal genereres, og om output skal samples.

8. **Generere koden**:
   - Modellen genererer Python-koden basert på inputene og genereringsargumentene. `TextStreamer` brukes til å håndtere output, der prompten og spesialtegnene blir hoppet over.

9. **Output**:
   - Den genererte koden skrives ut, og den bør inkludere Python-kode for å behandle bildet og lagre det som spesifisert i prompten.

Denne demoen viser hvordan man kan bruke en forhåndstrent modell med OpenVino for dynamisk å generere kode basert på brukerinput og bilder.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.