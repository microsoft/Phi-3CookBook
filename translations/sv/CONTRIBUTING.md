# Bidra

Det här projektet välkomnar bidrag och förslag. De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att, och faktiskt gör, ge oss rättigheterna att använda ditt bidrag. För mer information, besök [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

När du skickar in en pull request kommer en CLA-bot automatiskt att avgöra om du behöver tillhandahålla en CLA och märka PR:n därefter (t.ex. statuskontroll, kommentar). Följ helt enkelt instruktionerna som tillhandahålls av boten. Du behöver bara göra detta en gång för alla repos som använder vår CLA.

## Uppförandekod

Det här projektet har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). För mer information, läs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) om du har ytterligare frågor eller kommentarer.

## Försiktighet vid skapande av ärenden

Öppna inte GitHub-ärenden för allmänna supportfrågor eftersom GitHub-listan bör användas för funktionsförfrågningar och buggrapporter. På detta sätt kan vi lättare spåra faktiska problem eller buggar från koden och hålla den allmänna diskussionen separat från själva koden.

## Hur man bidrar

### Riktlinjer för pull requests

När du skickar in en pull request (PR) till Phi-3 CookBook-repot, använd följande riktlinjer:

- **Forka repot**: Forka alltid repot till ditt eget konto innan du gör dina ändringar.

- **Separata pull requests (PR)**:
  - Skicka in varje typ av ändring i en egen pull request. Till exempel bör buggfixar och dokumentationsuppdateringar skickas in i separata PR.
  - Stavfel och mindre dokumentationsuppdateringar kan kombineras i en enda PR där det är lämpligt.

- **Hantering av mergekonflikter**: Om din pull request visar mergekonflikter, uppdatera din lokala `main`-gren för att spegla huvudrepot innan du gör dina ändringar.

- **Översättningsbidrag**: När du skickar in en översättnings-PR, se till att översättningsmappen innehåller översättningar för alla filer i originalmappen.

### Riktlinjer för översättning

> [!IMPORTANT]
>
> När du översätter text i detta repo, använd inte maskinöversättning. Volontärarbeta endast för översättningar i språk där du är kunnig.

Om du är kunnig i ett icke-engelskt språk kan du hjälpa till att översätta innehållet. Följ dessa steg för att säkerställa att dina översättningsbidrag integreras korrekt, använd följande riktlinjer:

- **Skapa en översättningsmapp**: Navigera till rätt sektionsmapp och skapa en översättningsmapp för språket du bidrar till. Till exempel:
  - För introduktionssektionen: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - För snabbstartsektionen: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Fortsätt detta mönster för andra sektioner (03.Inference, 04.Finetuning, etc.)

- **Uppdatera relativa sökvägar**: När du översätter, justera mappstrukturen genom att lägga till `../../` i början av relativa sökvägar i markdown-filerna för att säkerställa att länkar fungerar korrekt. Till exempel, ändra enligt följande:
  - Ändra `(../../imgs/01/phi3aisafety.png)` till `(../../../../imgs/01/phi3aisafety.png)`

- **Organisera dina översättningar**: Varje översatt fil ska placeras i motsvarande sektions översättningsmapp. Till exempel, om du översätter introduktionssektionen till spanska, skulle du skapa enligt följande:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Skicka in en komplett PR**: Se till att alla översatta filer för en sektion ingår i en PR. Vi accepterar inte partiella översättningar för en sektion. När du skickar in en översättnings-PR, se till att översättningsmappen innehåller översättningar för alla filer i originalmappen.

### Riktlinjer för skrivande

För att säkerställa konsekvens i alla dokument, använd följande riktlinjer:

- **URL-formattering**: Omslut alla URL:er med hakparenteser följt av parenteser, utan extra mellanslag runt eller inuti dem. Till exempel: `[example](https://example.com)`.

- **Relativa länkar**: Använd `./` för relativa länkar som pekar på filer eller mappar i aktuell katalog, och `../` för de i en överordnad katalog. Till exempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Inte landsspecifika lokaler**: Se till att dina länkar inte innehåller landsspecifika lokaler. Till exempel, undvik `/en-us/` eller `/en/`.

- **Bildlagring**: Spara alla bilder i `./imgs`-mappen.

- **Beskrivande bildnamn**: Namnge bilder beskrivande med engelska tecken, siffror och bindestreck. Till exempel: `example-image.jpg`.

## GitHub-arbetsflöden

När du skickar in en pull request, kommer följande arbetsflöden att triggas för att validera ändringarna. Följ instruktionerna nedan för att säkerställa att din pull request klarar arbetsflödeskontrollerna:

- [Kontrollera brutna relativa sökvägar](../..)
- [Kontrollera att URL:er inte har lokal](../..)

### Kontrollera brutna relativa sökvägar

Detta arbetsflöde säkerställer att alla relativa sökvägar i dina filer är korrekta.

1. För att säkerställa att dina länkar fungerar korrekt, utför följande uppgifter med hjälp av VS Code:
    - Håll muspekaren över en länk i dina filer.
    - Tryck på **Ctrl + Klicka** för att navigera till länken.
    - Om du klickar på en länk och den inte fungerar lokalt, kommer det att trigga arbetsflödet och inte fungera på GitHub.

1. För att åtgärda detta problem, utför följande uppgifter med hjälp av sökvägsförslagen som tillhandahålls av VS Code:
    - Skriv `./` eller `../`.
    - VS Code kommer att uppmana dig att välja från de tillgängliga alternativen baserat på vad du skrev.
    - Följ sökvägen genom att klicka på önskad fil eller mapp för att säkerställa att din sökväg är korrekt.

När du har lagt till rätt relativ sökväg, spara och pusha dina ändringar.

### Kontrollera att URL:er inte har lokal

Detta arbetsflöde säkerställer att alla webbadresser inte innehåller en landsspecifik lokal. Eftersom detta repo är tillgängligt globalt är det viktigt att säkerställa att URL:er inte innehåller ditt lands lokal.

1. För att verifiera att dina URL:er inte har landslokaler, utför följande uppgifter:

    - Kontrollera text som `/en-us/`, `/en/` eller någon annan språk-lokal i URL:erna.
    - Om dessa inte finns i dina URL:er, kommer du att klara denna kontroll.

1. För att åtgärda detta problem, utför följande uppgifter:
    - Öppna filvägen som markerats av arbetsflödet.
    - Ta bort landslokalen från URL:erna.

När du har tagit bort landslokalen, spara och pusha dina ändringar.

### Kontrollera brutna URL:er

Detta arbetsflöde säkerställer att alla webbadresser i dina filer fungerar och returnerar statuskoden 200.

1. För att verifiera att dina URL:er fungerar korrekt, utför följande uppgifter:
    - Kontrollera statusen för URL:erna i dina filer.

2. För att åtgärda brutna URL:er, utför följande uppgifter:
    - Öppna filen som innehåller den brutna URL:en.
    - Uppdatera URL:en till den korrekta.

När du har åtgärdat URL:erna, spara och pusha dina ändringar.

> [!NOTE]
>
> Det kan finnas fall där URL-kontrollen misslyckas även om länken är tillgänglig. Detta kan hända av flera skäl, inklusive:
>
> - **Nätverksrestriktioner:** GitHub Actions-servrar kan ha nätverksrestriktioner som hindrar åtkomst till vissa URL:er.
> - **Timeout-problem:** URL:er som tar för lång tid att svara kan trigga ett timeout-fel i arbetsflödet.
> - **Tillfälliga serverproblem:** Tillfälliga driftstopp eller underhåll kan göra en URL tillfälligt otillgänglig under valideringen.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.