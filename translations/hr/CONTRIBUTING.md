# Contribuiranje

Ovaj projekt prihvaća doprinose i prijedloge. Većina doprinosa zahtijeva da se složite s Ugovorom o licenci za suradnike (CLA) kojim potvrđujete da imate pravo i stvarno dajete prava za korištenje vašeg doprinosa. Za više informacija, posjetite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kada podnesete pull request, CLA bot će automatski utvrditi trebate li dostaviti CLA i označiti PR na odgovarajući način (npr. status provjere, komentar). Jednostavno slijedite upute koje pruža bot. Ovo trebate učiniti samo jednom za sve repozitorije koji koriste naš CLA.

## Pravila ponašanja

Ovaj projekt usvojio je [Microsoftov Kodeks ponašanja za otvoreni izvor](https://opensource.microsoft.com/codeofconduct/).  
Za više informacija pročitajte [Često postavljana pitanja o kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Napomene za kreiranje problema

Molimo vas da ne otvarate GitHub probleme za općenita pitanja podrške jer bi se GitHub popis trebao koristiti za zahtjeve za funkcionalnost i prijave grešaka. Na taj način možemo lakše pratiti stvarne probleme ili greške u kodu i držati opću raspravu odvojenom od stvarnog koda.

## Kako doprinijeti

### Smjernice za pull requestove

Kada podnosite pull request (PR) u Phi-3 CookBook repozitorij, koristite sljedeće smjernice:

- **Forkajte repozitorij**: Uvijek forkajte repozitorij na svoj račun prije nego što napravite izmjene.

- **Odvojeni pull requestovi (PR)**:
  - Svaku vrstu promjene podnesite u zasebnom pull requestu. Na primjer, ispravke grešaka i ažuriranja dokumentacije trebaju biti podneseni u odvojenim PR-ovima.
  - Ispravci tipfelera i manja ažuriranja dokumentacije mogu se kombinirati u jedan PR, gdje je to primjereno.

- **Rješavanje sukoba spajanja**: Ako vaš pull request pokazuje sukobe spajanja, ažurirajte svoju lokalnu granu `main` kako bi odražavala glavni repozitorij prije nego što napravite izmjene.

- **Podnošenje prijevoda**: Kada podnosite PR za prijevod, osigurajte da mapa za prijevod uključuje prijevode za sve datoteke u izvornom direktoriju.

### Smjernice za prijevode

> [!IMPORTANT]
>
> Kada prevodite tekst u ovom repozitoriju, nemojte koristiti strojno prevođenje. Prijavite se za prijevode samo na jezicima na kojima ste vješti.

Ako ste vješti u nekom neengleskom jeziku, možete pomoći prevesti sadržaj. Slijedite ove korake kako biste osigurali da su vaši prijevodi ispravno integrirani, koristeći sljedeće smjernice:

- **Kreirajte mapu za prijevod**: Navigirajte do odgovarajućeg direktorija i kreirajte mapu za prijevod jezika na kojem doprinosite. Na primjer:
  - Za uvodni odjeljak: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Za odjeljak za brzi početak: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Nastavite ovaj obrazac za ostale odjeljke (03.Inference, 04.Finetuning itd.)

- **Ažurirajte relativne putanje**: Prilikom prevođenja, prilagodite strukturu mapa dodavanjem `../../` na početak relativnih putanja unutar markdown datoteka kako bi veze ispravno funkcionirale. Na primjer, promijenite na sljedeći način:
  - Promijenite `(../../imgs/01/phi3aisafety.png)` u `(../../../../imgs/01/phi3aisafety.png)`

- **Organizirajte svoje prijevode**: Svaka prevedena datoteka treba biti smještena u odgovarajuću mapu prijevoda za taj odjeljak. Na primjer, ako prevodite uvodni odjeljak na španjolski, trebali biste kreirati sljedeće:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Podnesite cjelovit PR**: Osigurajte da su sve prevedene datoteke za određeni odjeljak uključene u jedan PR. Ne prihvaćamo djelomične prijevode za odjeljak. Kada podnosite PR za prijevod, provjerite da mapa prijevoda uključuje prijevode za sve datoteke iz izvornog direktorija.

### Smjernice za pisanje

Kako biste osigurali dosljednost u svim dokumentima, koristite sljedeće smjernice:

- **Formatiranje URL-ova**: Omotajte sve URL-ove u uglate zagrade praćene zagradama, bez dodatnih razmaka oko njih. Na primjer: `[example](https://example.com)`.

- **Relativne veze**: Koristite `./` za relativne veze koje upućuju na datoteke ili mape u trenutnom direktoriju i `../` za one u nadređenom direktoriju. Na primjer: `[example](../../path/to/file)` ili `[example](../../../path/to/file)`.

- **Izbjegavajte lokalne oznake specifične za zemlje**: Osigurajte da vaše veze ne uključuju lokalne oznake specifične za zemlje. Na primjer, izbjegavajte `/en-us/` ili `/en/`.

- **Pohrana slika**: Pohranite sve slike u mapu `./imgs`.

- **Opisni nazivi slika**: Imenujte slike opisno koristeći engleske znakove, brojeve i crtice. Na primjer: `example-image.jpg`.

## GitHub Workflowovi

Kada podnesete pull request, pokrenut će se sljedeći workflowovi kako bi se provjerile promjene. Slijedite upute ispod kako biste osigurali da vaš pull request prođe provjere workflowa:

- [Provjera neispravnih relativnih putanja](../..)
- [Provjera da URL-ovi nemaju lokalne oznake](../..)

### Provjera neispravnih relativnih putanja

Ovaj workflow osigurava da su sve relativne putanje u vašim datotekama ispravne.

1. Kako biste osigurali da veze ispravno funkcioniraju, izvršite sljedeće zadatke koristeći VS Code:
    - Zadržite pokazivač iznad bilo koje veze u vašim datotekama.
    - Pritisnite **Ctrl + Klik** kako biste navigirali do veze.
    - Ako kliknete na vezu i ona ne funkcionira lokalno, to će pokrenuti workflow i neće funkcionirati na GitHubu.

1. Kako biste riješili ovaj problem, izvršite sljedeće zadatke koristeći prijedloge putanja koje nudi VS Code:
    - Upišite `./` ili `../`.
    - VS Code će vas tražiti da odaberete dostupne opcije na temelju onoga što ste upisali.
    - Slijedite putanju klikom na željenu datoteku ili mapu kako biste osigurali ispravnost putanje.

Kada dodate ispravnu relativnu putanju, spremite i pošaljite svoje promjene.

### Provjera da URL-ovi nemaju lokalne oznake

Ovaj workflow osigurava da nijedan web URL ne uključuje lokalnu oznaku specifičnu za zemlju. Budući da je ovaj repozitorij dostupan globalno, važno je osigurati da URL-ovi ne sadrže lokalne oznake vaše zemlje.

1. Kako biste provjerili da vaši URL-ovi nemaju lokalne oznake, izvršite sljedeće zadatke:

    - Provjerite tekst poput `/en-us/`, `/en/` ili bilo koje druge jezične lokalne oznake u URL-ovima.
    - Ako ovakvi elementi nisu prisutni u vašim URL-ovima, proći ćete ovu provjeru.

1. Kako biste riješili ovaj problem, izvršite sljedeće zadatke:
    - Otvorite putanju datoteke koju je workflow označio.
    - Uklonite lokalnu oznaku iz URL-ova.

Kada uklonite lokalnu oznaku, spremite i pošaljite svoje promjene.

### Provjera neispravnih URL-ova

Ovaj workflow osigurava da bilo koji web URL u vašim datotekama ispravno funkcionira i vraća statusni kod 200.

1. Kako biste provjerili da vaši URL-ovi ispravno funkcioniraju, izvršite sljedeće zadatke:
    - Provjerite status URL-ova u vašim datotekama.

2. Kako biste popravili bilo koji neispravan URL, izvršite sljedeće zadatke:
    - Otvorite datoteku koja sadrži neispravan URL.
    - Ažurirajte URL na ispravan.

Kada popravite URL-ove, spremite i pošaljite svoje promjene.

> [!NOTE]
>
> Moguće je da provjera URL-a ne uspije iako je veza dostupna. To se može dogoditi iz nekoliko razloga, uključujući:
>
> - **Ograničenja mreže:** GitHub actions serveri mogu imati mrežna ograničenja koja onemogućuju pristup određenim URL-ovima.
> - **Problemi s vremenom odziva:** URL-ovi koji predugo odgovaraju mogu izazvati grešku vremenskog ograničenja u workflowu.
> - **Privremeni problemi sa serverom:** Povremeni prekidi rada servera ili održavanje mogu privremeno učiniti URL nedostupnim tijekom provjere.

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prijevoda. Iako nastojimo osigurati točnost, molimo imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.