Denne demo viser, hvordan man bruger en forudtrænet model til at generere Python-kode baseret på et billede og en tekstprompt.

[Eksempelkode](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Her er en trin-for-trin forklaring:

1. **Imports og Opsætning**:
   - De nødvendige biblioteker og moduler importeres, herunder `requests`, `PIL` til billedbehandling og `transformers` til håndtering af modellen og processeringen.

2. **Indlæsning og Visning af Billedet**:
   - En billedfil (`demo.png`) åbnes ved hjælp af `PIL`-biblioteket og vises.

3. **Definering af Prompten**:
   - En besked oprettes, som inkluderer billedet og en anmodning om at generere Python-kode til at behandle billedet og gemme det ved hjælp af `plt` (matplotlib).

4. **Indlæsning af Processoren**:
   - `AutoProcessor` indlæses fra en forudtrænet model specificeret af `out_dir`-mappen. Denne processor håndterer tekst- og billedinput.

5. **Oprettelse af Prompten**:
   - `apply_chat_template`-metoden bruges til at formatere beskeden til en prompt, der passer til modellen.

6. **Behandling af Input**:
   - Prompten og billedet behandles til tensorer, som modellen kan forstå.

7. **Indstilling af Genereringsparametre**:
   - Parametre for modellens genereringsproces defineres, herunder det maksimale antal nye tokens, der skal genereres, og om outputtet skal samples.

8. **Generering af Koden**:
   - Modellen genererer Python-koden baseret på input og genereringsparametrene. `TextStreamer` bruges til at håndtere outputtet, hvor prompten og specialtegn springes over.

9. **Output**:
   - Den genererede kode udskrives, og den bør indeholde Python-kode til at behandle billedet og gemme det, som angivet i prompten.

Denne demo viser, hvordan man kan udnytte en forudtrænet model med OpenVino til dynamisk at generere kode baseret på brugerinput og billeder.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.