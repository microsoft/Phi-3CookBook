# Bijdragen

Dit project verwelkomt bijdragen en suggesties. Voor de meeste bijdragen moet je akkoord gaan met een Contributor License Agreement (CLA) waarin wordt verklaard dat je het recht hebt om, en daadwerkelijk doet, ons de rechten te geven om jouw bijdrage te gebruiken. Voor meer informatie, bezoek [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet indienen en de PR dienovereenkomstig markeren (bijv. statuscontrole, opmerking). Volg gewoon de instructies van de bot. Je hoeft dit slechts één keer te doen voor alle repositories die onze CLA gebruiken.

## Gedragscode

Dit project heeft de [Microsoft Open Source Gedragscode](https://opensource.microsoft.com/codeofconduct/) aangenomen. Voor meer informatie, lees de [Gedragscode FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of neem contact op met [opencode@microsoft.com](mailto:opencode@microsoft.com) voor eventuele aanvullende vragen of opmerkingen.

## Waarschuwingen voor het aanmaken van issues

Open geen GitHub-issues voor algemene ondersteuningsvragen, aangezien de GitHub-lijst bedoeld is voor functieverzoeken en bugmeldingen. Op deze manier kunnen we daadwerkelijke problemen of bugs in de code gemakkelijker volgen en algemene discussies gescheiden houden van de daadwerkelijke code.

## Hoe Bijdragen

### Richtlijnen voor Pull Requests

Bij het indienen van een pull request (PR) naar de Phi-3 CookBook-repository, gebruik de volgende richtlijnen:

- **Fork de repository**: Fork de repository altijd naar je eigen account voordat je wijzigingen aanbrengt.

- **Gescheiden pull requests (PR)**:
  - Dien elk type wijziging in een aparte pull request in. Bijvoorbeeld, bugfixes en documentatie-updates moeten in afzonderlijke PR's worden ingediend.
  - Typografische fouten en kleine documentatie-updates kunnen waar nodig worden gecombineerd in één PR.

- **Omgaan met mergeconflicten**: Als je pull request mergeconflicten toont, werk dan je lokale `main`-branch bij zodat deze overeenkomt met de hoofdrepository voordat je wijzigingen aanbrengt.

- **Indienen van vertalingen**: Zorg er bij het indienen van een vertaal-PR voor dat de vertaalmap vertalingen bevat voor alle bestanden in de originele map.

### Richtlijnen voor Vertalingen

> [!IMPORTANT]
>
> Gebruik geen machinevertaling bij het vertalen van tekst in deze repository. Meld je alleen aan voor vertalingen in talen waarin je vaardig bent.

Als je vaardig bent in een niet-Engelse taal, kun je helpen met het vertalen van de inhoud. Volg deze stappen om ervoor te zorgen dat je vertaalbijdragen correct worden geïntegreerd. Gebruik de volgende richtlijnen:

- **Maak een vertaalmap aan**: Navigeer naar de juiste sectiemap en maak een vertaalmap aan voor de taal waaraan je bijdraagt. Bijvoorbeeld:
  - Voor de introductiesectie: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Voor de quick start-sectie: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Ga door met dit patroon voor andere secties (03.Inference, 04.Finetuning, enz.).

- **Pas relatieve paden aan**: Pas bij het vertalen de mapstructuur aan door `../../` toe te voegen aan het begin van relatieve paden binnen de markdown-bestanden, zodat links correct werken. Bijvoorbeeld, wijzig als volgt:
  - Wijzig `(../../imgs/01/phi3aisafety.png)` in `(../../../../imgs/01/phi3aisafety.png)`

- **Organiseer je vertalingen**: Elk vertaald bestand moet worden geplaatst in de corresponderende sectiemap voor vertalingen. Bijvoorbeeld, als je de introductiesectie in het Spaans vertaalt, maak je de volgende structuur:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Dien een volledige PR in**: Zorg ervoor dat alle vertaalde bestanden voor een sectie in één PR worden opgenomen. We accepteren geen gedeeltelijke vertalingen voor een sectie. Zorg er bij het indienen van een vertaal-PR voor dat de vertaalmap vertalingen bevat voor alle bestanden in de originele map.

### Schrijfrichtlijnen

Om consistentie in alle documenten te waarborgen, gebruik de volgende richtlijnen:

- **URL-opmaak**: Plaats alle URLs tussen vierkante haken gevolgd door haakjes, zonder extra spaties eromheen of erin. Bijvoorbeeld: `[example](https://www.microsoft.com)`.

- **Relatieve links**: Gebruik `./` voor relatieve links die verwijzen naar bestanden of mappen in de huidige directory, en `../` voor die in een bovenliggende directory. Bijvoorbeeld: `[example](../../path/to/file)` of `[example](../../../path/to/file)`.

- **Geen land-specifieke lokale instellingen**: Zorg ervoor dat je links geen land-specifieke lokale instellingen bevatten. Vermijd bijvoorbeeld `/en-us/` of `/en/`.

- **Afbeeldingenopslag**: Sla alle afbeeldingen op in de `./imgs`-map.

- **Beschrijvende afbeeldingsnamen**: Geef afbeeldingen beschrijvende namen met Engelse karakters, cijfers en streepjes. Bijvoorbeeld: `example-image.jpg`.

## GitHub Workflows

Wanneer je een pull request indient, worden de volgende workflows geactiveerd om de wijzigingen te valideren. Volg de onderstaande instructies om ervoor te zorgen dat je pull request de workflowcontroles doorstaat:

- [Controleer Gebroken Relatieve Paden](../..)
- [Controleer of URLs Geen Locale Hebben](../..)

### Controleer Gebroken Relatieve Paden

Deze workflow zorgt ervoor dat alle relatieve paden in je bestanden correct zijn.

1. Om ervoor te zorgen dat je links correct werken, voer de volgende taken uit met behulp van VS Code:
    - Beweeg je muis over een link in je bestanden.
    - Druk op **Ctrl + Klik** om naar de link te navigeren.
    - Als je op een link klikt en deze werkt niet lokaal, zal dit de workflow activeren en niet werken op GitHub.

1. Om dit probleem op te lossen, voer de volgende taken uit met behulp van de padvoorstellen die door VS Code worden gegeven:
    - Typ `./` of `../`.
    - VS Code zal je opties tonen op basis van wat je hebt getypt.
    - Volg het pad door op het gewenste bestand of de gewenste map te klikken om ervoor te zorgen dat je pad correct is.

Zodra je het juiste relatieve pad hebt toegevoegd, sla je de wijzigingen op en push je ze.

### Controleer of URLs Geen Locale Hebben

Deze workflow zorgt ervoor dat elke web-URL geen land-specifieke locale bevat. Omdat deze repository wereldwijd toegankelijk is, is het belangrijk om ervoor te zorgen dat URLs geen locale van jouw land bevatten.

1. Om te controleren of je URLs geen land-locale bevatten, voer de volgende taken uit:

    - Controleer op tekst zoals `/en-us/`, `/en/`, of andere taal-locale in de URLs.
    - Als deze niet aanwezig zijn in je URLs, slaag je voor deze controle.

1. Om dit probleem op te lossen, voer de volgende taken uit:
    - Open het bestandspad dat door de workflow wordt gemarkeerd.
    - Verwijder de land-locale uit de URLs.

Zodra je de land-locale hebt verwijderd, sla je de wijzigingen op en push je ze.

### Controleer Gebroken URLs

Deze workflow zorgt ervoor dat elke web-URL in je bestanden werkt en een 200-statuscode retourneert.

1. Om te controleren of je URLs correct werken, voer de volgende taken uit:
    - Controleer de status van de URLs in je bestanden.

2. Om gebroken URLs te repareren, voer de volgende taken uit:
    - Open het bestand dat de gebroken URL bevat.
    - Werk de URL bij naar de juiste.

Zodra je de URLs hebt gerepareerd, sla je de wijzigingen op en push je ze.

> [!NOTE]
>
> Er kunnen gevallen zijn waarin de URL-controle mislukt, zelfs als de link toegankelijk is. Dit kan om verschillende redenen gebeuren, waaronder:
>
> - **Netwerkbeperkingen:** GitHub-actieservers kunnen netwerkbeperkingen hebben die toegang tot bepaalde URLs verhinderen.
> - **Timeoutproblemen:** URLs die te lang nodig hebben om te reageren, kunnen een timeoutfout veroorzaken in de workflow.
> - **Tijdelijke serverproblemen:** Occasionele serverdowntime of onderhoud kan ervoor zorgen dat een URL tijdelijk niet beschikbaar is tijdens de validatie.

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, moet u zich ervan bewust zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.