# Bidrag

Dette projekt byder bidrag og forslag velkommen. De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), som erklærer, at du har retten til, og faktisk gør, give os rettighederne til at bruge dit bidrag. For detaljer, besøg [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal indsende en CLA og markere PR'en korrekt (f.eks. statuscheck, kommentar). Følg blot instruktionerne, som botten giver. Du skal kun gøre dette én gang på tværs af alle repos, der bruger vores CLA.

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For mere information, læs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med yderligere spørgsmål eller kommentarer.

## Forbehold ved oprettelse af issues

Åbn venligst ikke GitHub issues for generelle supportspørgsmål, da GitHub-listen bør bruges til funktionsanmodninger og fejlrapporter. På denne måde kan vi lettere spore faktiske problemer eller fejl i koden og holde den generelle diskussion adskilt fra selve koden.

## Sådan bidrager du

### Retningslinjer for pull requests

Når du indsender en pull request (PR) til Phi-3 CookBook-repositoriet, skal du følge disse retningslinjer:

- **Fork repositoryet**: Fork altid repositoryet til din egen konto, før du foretager dine ændringer.

- **Adskilte pull requests (PR)**:
  - Indsend hver type ændring i sin egen pull request. For eksempel bør fejlrettelser og dokumentationsopdateringer indsendes i separate PR'er.
  - Typografifejl og mindre dokumentationsopdateringer kan kombineres i én PR, hvor det er passende.

- **Håndter merge-konflikter**: Hvis din pull request viser merge-konflikter, opdater din lokale `main`-gren til at spejle hovedrepositoryet, før du foretager dine ændringer.

- **Indsendelse af oversættelser**: Når du indsender en oversættelses-PR, skal du sikre, at oversættelsesmappen indeholder oversættelser for alle filer i den originale mappe.

### Retningslinjer for oversættelser

> [!IMPORTANT]
>
> Når du oversætter tekst i dette repository, må du ikke bruge maskinoversættelse. Bidrag kun med oversættelser på sprog, hvor du er flydende.

Hvis du er flydende i et ikke-engelsk sprog, kan du hjælpe med at oversætte indholdet. Følg disse trin for at sikre, at dine oversættelsesbidrag bliver korrekt integreret. Brug følgende retningslinjer:

- **Opret oversættelsesmappe**: Naviger til den relevante sektionsmappe og opret en oversættelsesmappe for det sprog, du bidrager til. For eksempel:
  - For introduktionssektionen: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - For quick start-sektionen: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Fortsæt dette mønster for andre sektioner (03.Inference, 04.Finetuning osv.)

- **Opdater relative stier**: Når du oversætter, skal du justere mappe-strukturen ved at tilføje `../../` til begyndelsen af relative stier i markdown-filerne for at sikre, at links fungerer korrekt. For eksempel, ændr som følger:
  - Ændr `(../../imgs/01/phi3aisafety.png)` til `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser dine oversættelser**: Hver oversat fil skal placeres i den tilsvarende sektions oversættelsesmappe. For eksempel, hvis du oversætter introduktionssektionen til spansk, skal du oprette følgende:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Indsend en komplet PR**: Sørg for, at alle oversatte filer for en sektion er inkluderet i én PR. Vi accepterer ikke delvise oversættelser for en sektion. Når du indsender en oversættelses-PR, skal du sikre, at oversættelsesmappen indeholder oversættelser for alle filer i den originale mappe.

### Retningslinjer for skrivning

For at sikre konsistens på tværs af alle dokumenter, skal du bruge følgende retningslinjer:

- **URL-formattering**: Indram alle URL'er i firkantede parenteser efterfulgt af parenteser, uden ekstra mellemrum omkring eller inden i dem. For eksempel: `[example](https://www.microsoft.com)`.

- **Relative links**: Brug `./` til relative links, der peger på filer eller mapper i den aktuelle mappe, og `../` til dem i en overordnet mappe. For eksempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ikke landespecifikke lokaliteter**: Sørg for, at dine links ikke inkluderer landespecifikke lokaliteter. For eksempel, undgå `/en-us/` eller `/en/`.

- **Billedlagring**: Gem alle billeder i `./imgs`-mappen.

- **Beskrivende billednavne**: Navngiv billeder beskrivende ved brug af engelske tegn, tal og bindestreger. For eksempel: `example-image.jpg`.

## GitHub Workflows

Når du indsender en pull request, vil følgende workflows blive udløst for at validere ændringerne. Følg nedenstående instruktioner for at sikre, at din pull request består workflow-tjek:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Denne workflow sikrer, at alle relative stier i dine filer er korrekte.

1. For at sikre, at dine links fungerer korrekt, udfør følgende opgaver ved hjælp af VS Code:
    - Hold musen over ethvert link i dine filer.
    - Tryk på **Ctrl + Klik** for at navigere til linket.
    - Hvis du klikker på et link, og det ikke fungerer lokalt, vil det udløse workflowen og heller ikke fungere på GitHub.

1. For at løse dette problem skal du udføre følgende opgaver ved hjælp af sti-forslagene fra VS Code:
    - Skriv `./` eller `../`.
    - VS Code vil bede dig om at vælge blandt de tilgængelige muligheder baseret på, hvad du har skrevet.
    - Følg stien ved at klikke på den ønskede fil eller mappe for at sikre, at din sti er korrekt.

Når du har tilføjet den korrekte relative sti, gem og push dine ændringer.

### Check URLs Don't Have Locale

Denne workflow sikrer, at enhver web-URL ikke inkluderer en landespecifik lokalitet. Da dette repository er tilgængeligt globalt, er det vigtigt at sikre, at URL'er ikke indeholder din lands lokalitet.

1. For at verificere, at dine URL'er ikke har landelokaliteter, udfør følgende opgaver:

    - Kontroller for tekst som `/en-us/`, `/en/` eller enhver anden sprog-lokalitet i URL'erne.
    - Hvis disse ikke er til stede i dine URL'er, vil du bestå dette tjek.

1. For at løse dette problem skal du udføre følgende opgaver:
    - Åbn filstien, der er fremhævet af workflowen.
    - Fjern landelokaliteten fra URL'erne.

Når du har fjernet landelokaliteten, gem og push dine ændringer.

### Check Broken Urls

Denne workflow sikrer, at enhver web-URL i dine filer fungerer og returnerer statuskoden 200.

1. For at verificere, at dine URL'er fungerer korrekt, udfør følgende opgaver:
    - Tjek status for URL'erne i dine filer.

2. For at løse eventuelle ødelagte URL'er skal du udføre følgende opgaver:
    - Åbn filen, der indeholder den ødelagte URL.
    - Opdater URL'en til den korrekte.

Når du har rettet URL'erne, gem og push dine ændringer.

> [!NOTE]
>
> Der kan være tilfælde, hvor URL-tjekket fejler, selvom linket er tilgængeligt. Dette kan ske af flere årsager, herunder:
>
> - **Netværksrestriktioner**: GitHub actions-servere kan have netværksrestriktioner, der forhindrer adgang til visse URL'er.
> - **Timeout-problemer**: URL'er, der tager for lang tid at svare, kan udløse en timeout-fejl i workflowen.
> - **Midlertidige serverproblemer**: Lejlighedsvis servernedetid eller vedligeholdelse kan gøre en URL midlertidigt utilgængelig under validering.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.