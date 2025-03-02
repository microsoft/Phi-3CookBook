# Bidra

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rett til, og faktisk gir oss, rettighetene til å bruke bidraget ditt. For detaljer, besøk [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du trenger å signere en CLA og merke PR-en deretter (f.eks. statuskontroll, kommentar). Følg ganske enkelt instruksjonene gitt av boten. Du trenger bare å gjøre dette én gang på tvers av alle repos som bruker vår CLA.

## Retningslinjer for oppførsel

Dette prosjektet har adoptert [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For mer informasjon, les [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) hvis du har ytterligere spørsmål eller kommentarer.

## Viktig ved opprettelse av issues

Vennligst ikke opprett GitHub issues for generelle supportspørsmål, da GitHub-listen skal brukes til forespørsler om nye funksjoner og feilrapporter. På denne måten kan vi enklere spore faktiske problemer eller feil i koden og holde den generelle diskusjonen adskilt fra selve koden.

## Hvordan bidra

### Retningslinjer for pull requests

Når du sender inn en pull request (PR) til Phi-3 CookBook-repositoriet, vennligst følg disse retningslinjene:

- **Fork repositoriet**: Fork alltid repositoriet til din egen konto før du gjør endringer.

- **Separate pull requests (PR)**:
  - Send inn hver type endring i sin egen pull request. For eksempel bør feilrettinger og dokumentasjonsoppdateringer sendes inn som separate PR-er.
  - Typografiske feil og mindre dokumentasjonsoppdateringer kan kombineres i én PR der det er passende.

- **Håndter merge-konflikter**: Hvis pull request-en din viser merge-konflikter, oppdater din lokale `main`-gren for å speile hovedrepositoriet før du gjør endringene dine.

- **Oversettelsesbidrag**: Når du sender inn en oversettelses-PR, sørg for at oversettelsesmappen inkluderer oversettelser for alle filer i den originale mappen.

### Retningslinjer for oversettelse

> [!IMPORTANT]
>
> Når du oversetter tekst i dette repositoriet, bruk ikke maskinoversettelse. Bidra kun med oversettelser til språk du behersker godt.

Hvis du behersker et annet språk enn engelsk, kan du bidra med oversettelser. Følg disse trinnene for å sikre at oversettelsesbidragene dine blir korrekt integrert, og bruk følgende retningslinjer:

- **Opprett oversettelsesmappe**: Naviger til riktig seksjonsmappe og opprett en oversettelsesmappe for språket du bidrar til. For eksempel:
  - For introduksjonsseksjonen: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - For hurtigstartseksjonen: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Fortsett dette mønsteret for andre seksjoner (03.Inference, 04.Finetuning, osv.)

- **Oppdater relative stier**: Når du oversetter, juster mappestrukturen ved å legge til `../../` i begynnelsen av relative stier i markdown-filene for å sikre at lenkene fungerer korrekt. For eksempel, endre som følger:
  - Endre `(../../imgs/01/phi3aisafety.png)` til `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser oversettelsene dine**: Hver oversatte fil skal plasseres i den tilsvarende seksjonens oversettelsesmappe. For eksempel, hvis du oversetter introduksjonsseksjonen til spansk, bør du opprette som følger:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Send inn en komplett PR**: Sørg for at alle oversatte filer for en seksjon er inkludert i én PR. Vi aksepterer ikke delvise oversettelser for en seksjon. Når du sender inn en oversettelses-PR, sørg for at oversettelsesmappen inkluderer oversettelser for alle filer i den originale mappen.

### Retningslinjer for skriving

For å sikre konsistens på tvers av alle dokumenter, vennligst bruk følgende retningslinjer:

- **URL-formattering**: Pakk alle URL-er inn i hakeparenteser etterfulgt av parenteser, uten ekstra mellomrom rundt eller inni dem. For eksempel: `[example](https://example.com)`.

- **Relative lenker**: Bruk `./` for relative lenker som peker til filer eller mapper i den nåværende katalogen, og `../` for de i en foreldremappe. For eksempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Unngå lands-spesifikke lokaliteter**: Sørg for at lenkene dine ikke inkluderer lands-spesifikke lokaliteter. For eksempel, unngå `/en-us/` eller `/en/`.

- **Bildelagring**: Lagre alle bilder i `./imgs`-mappen.

- **Beskrivende bilde-navn**: Navngi bilder beskrivende ved bruk av engelske tegn, tall og bindestreker. For eksempel: `example-image.jpg`.

## GitHub-arbeidsflyter

Når du sender inn en pull request, vil følgende arbeidsflyter bli trigget for å validere endringene. Følg instruksjonene nedenfor for å sikre at pull request-en din består arbeidsflytkontrollene:

- [Sjekk ødelagte relative stier](../..)
- [Sjekk at URL-er ikke har lokalitet](../..)

### Sjekk ødelagte relative stier

Denne arbeidsflyten sikrer at alle relative stier i filene dine er korrekte.

1. For å sikre at lenkene dine fungerer som de skal, utfør følgende oppgaver i VS Code:
    - Hold musepekeren over en lenke i filene dine.
    - Trykk **Ctrl + Klikk** for å navigere til lenken.
    - Hvis du klikker på en lenke og den ikke fungerer lokalt, vil det trigge arbeidsflyten og ikke fungere på GitHub.

1. For å fikse dette problemet, utfør følgende oppgaver ved hjelp av sti-forslagene som gis av VS Code:
    - Skriv `./` eller `../`.
    - VS Code vil be deg velge fra tilgjengelige alternativer basert på det du skrev.
    - Følg stien ved å klikke på ønsket fil eller mappe for å sikre at stien er korrekt.

Når du har lagt til riktig relativ sti, lagre og push endringene dine.

### Sjekk at URL-er ikke har lokalitet

Denne arbeidsflyten sikrer at ingen nett-URL-er inkluderer en lands-spesifikk lokalitet. Siden dette repositoriet er tilgjengelig globalt, er det viktig å sikre at URL-er ikke inneholder lokaliteten til landet ditt.

1. For å verifisere at URL-ene dine ikke har lands-lokaliteter, utfør følgende oppgaver:

    - Sjekk etter tekst som `/en-us/`, `/en/`, eller noen annen språk-lokalitet i URL-ene.
    - Hvis disse ikke er tilstede i URL-ene dine, vil du bestå denne sjekken.

1. For å fikse dette problemet, utfør følgende oppgaver:
    - Åpne filstien som er fremhevet av arbeidsflyten.
    - Fjern lands-lokaliteten fra URL-ene.

Når du har fjernet lands-lokaliteten, lagre og push endringene dine.

### Sjekk ødelagte URL-er

Denne arbeidsflyten sikrer at alle nett-URL-er i filene dine fungerer og returnerer statuskode 200.

1. For å verifisere at URL-ene dine fungerer korrekt, utfør følgende oppgaver:
    - Sjekk statusen til URL-ene i filene dine.

2. For å fikse eventuelle ødelagte URL-er, utfør følgende oppgaver:
    - Åpne filen som inneholder den ødelagte URL-en.
    - Oppdater URL-en til den korrekte.

Når du har fikset URL-ene, lagre og push endringene dine.

> [!NOTE]
>
> Det kan være tilfeller der URL-sjekken feiler selv om lenken er tilgjengelig. Dette kan skje av flere grunner, inkludert:
>
> - **Nettverksbegrensninger:** GitHub actions-servere kan ha nettverksbegrensninger som hindrer tilgang til visse URL-er.
> - **Tidsavbrudd:** URL-er som tar for lang tid å svare kan utløse en tidsavbruddsfeil i arbeidsflyten.
> - **Midlertidige serverproblemer:** Av og til kan servernedetid eller vedlikehold gjøre en URL midlertidig utilgjengelig under validering.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettingstjenester. Selv om vi bestreber oss på nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.