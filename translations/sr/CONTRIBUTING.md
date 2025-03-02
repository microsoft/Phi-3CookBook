# Doprinose

Ovaj projekat pozdravlja doprinose i sugestije. Većina doprinosa zahteva da se složite sa Ugovorom o licenci za doprinos (CLA), kojim potvrđujete da imate pravo da nam date prava na korišćenje vašeg doprinosa. Za više detalja, posetite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kada pošaljete zahtev za povlačenje (pull request), CLA bot će automatski utvrditi da li je potrebno da obezbedite CLA i označiti PR na odgovarajući način (npr. provera statusa, komentar). Jednostavno pratite uputstva koja bot pruži. Ovo ćete morati da uradite samo jednom za sve repozitorijume koji koriste naš CLA.

## Kodeks ponašanja

Ovaj projekat je usvojio [Kodeks ponašanja za Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).  
Za više informacija pročitajte [Često postavljana pitanja o kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/) ili kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Napomene za kreiranje problema

Molimo vas da ne otvarate GitHub probleme za opšta pitanja podrške, jer GitHub lista treba da se koristi za zahteve za funkcionalnosti i prijavljivanje grešaka. Na ovaj način možemo lakše pratiti stvarne probleme ili greške u kodu i odvojiti opštu diskusiju od stvarnog koda.

## Kako doprineti

### Smernice za zahteve za povlačenje

Kada podnosite zahtev za povlačenje (PR) u Phi-3 CookBook repozitorijum, molimo vas da sledite sledeće smernice:

- **Forkujte repozitorijum**: Uvek forkujte repozitorijum na svoj nalog pre nego što napravite izmene.

- **Odvojeni zahtevi za povlačenje (PR)**:
  - Podnesite svaku vrstu izmene u zasebnom zahtevu za povlačenje. Na primer, ispravke grešaka i ažuriranja dokumentacije treba podnositi u odvojenim PR-ovima.
  - Ispravke tipografskih grešaka i manja ažuriranja dokumentacije mogu se kombinovati u jedan PR, gde je to prikladno.

- **Rešavanje konflikata pri spajanju**: Ako vaš zahtev za povlačenje pokazuje konflikte pri spajanju, ažurirajte vašu lokalnu granu `main` kako bi odražavala glavni repozitorijum pre nego što napravite izmene.

- **Podnošenje prevoda**: Kada podnosite PR za prevod, uverite se da folder za prevode uključuje prevode za sve fajlove iz originalnog foldera.

### Smernice za prevod

> [!IMPORTANT]
>
> Kada prevodite tekst u ovom repozitorijumu, nemojte koristiti mašinski prevod. Prijavite se za prevode samo na jezicima na kojima ste stručni.

Ako ste stručni za neki jezik osim engleskog, možete pomoći u prevođenju sadržaja. Da biste osigurali pravilnu integraciju vaših prevoda, molimo vas da sledite sledeće smernice:

- **Kreirajte folder za prevod**: Idite do odgovarajuće sekcije i kreirajte folder za prevod jezika na koji doprinosite. Na primer:
  - Za uvodnu sekciju: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Za sekciju brzog početka: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Nastavite ovaj obrazac za ostale sekcije (03.Inference, 04.Finetuning, itd.)

- **Ažurirajte relativne putanje**: Prilikom prevođenja, prilagodite strukturu foldera dodavanjem `../../` na početak relativnih putanja unutar markdown fajlova kako bi linkovi pravilno funkcionisali. Na primer, promenite na sledeći način:
  - Promenite `(../../imgs/01/phi3aisafety.png)` u `(../../../../imgs/01/phi3aisafety.png)`

- **Organizujte svoje prevode**: Svaki prevedeni fajl treba da bude smešten u odgovarajući folder za prevod sekcije. Na primer, ako prevodite uvodnu sekciju na španski, kreiraćete na sledeći način:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Podnesite kompletan PR**: Uverite se da svi prevedeni fajlovi za jednu sekciju budu uključeni u jedan PR. Ne prihvatamo delimične prevode za sekciju. Kada podnosite PR za prevod, uverite se da folder za prevod uključuje prevode za sve fajlove iz originalnog foldera.

### Smernice za pisanje

Kako bismo osigurali doslednost u svim dokumentima, molimo vas da sledite sledeće smernice:

- **Formatiranje URL-ova**: Obavijte sve URL-ove u uglaste zagrade praćene zagradama, bez dodatnih razmaka oko ili unutar njih. Na primer: `[example](https://example.com)`.

- **Relativni linkovi**: Koristite `./` za relativne linkove koji upućuju na fajlove ili foldere u trenutnom direktorijumu i `../` za one u nadređenom direktorijumu. Na primer: `[example](../../path/to/file)` ili `[example](../../../path/to/file)`.

- **Bez lokalnih oznaka specifičnih za zemlju**: Uverite se da vaši linkovi ne uključuju lokalne oznake specifične za zemlju. Na primer, izbegavajte `/en-us/` ili `/en/`.

- **Skladištenje slika**: Sve slike čuvajte u folderu `./imgs`.

- **Opisni nazivi slika**: Nazivajte slike opisno koristeći engleske karaktere, brojeve i crtice. Na primer: `example-image.jpg`.

## GitHub tokovi rada

Kada podnesete zahtev za povlačenje, sledeći tokovi rada će se pokrenuti kako bi se validirale izmene. Pratite dole navedena uputstva kako biste osigurali da vaš zahtev za povlačenje prođe provere tokova rada:

- [Proverite pokidane relativne putanje](../..)
- [Proverite da URL-ovi nemaju lokalne oznake](../..)

### Proverite pokidane relativne putanje

Ovaj tok rada osigurava da su sve relativne putanje u vašim fajlovima ispravne.

1. Da biste se uverili da vaši linkovi ispravno funkcionišu, izvršite sledeće zadatke koristeći VS Code:
    - Pređite mišem preko bilo kog linka u vašim fajlovima.
    - Pritisnite **Ctrl + Klik** da biste otišli na link.
    - Ako kliknete na link i on ne funkcioniše lokalno, to će pokrenuti tok rada i neće raditi na GitHub-u.

1. Da biste rešili ovaj problem, izvršite sledeće zadatke koristeći predloge putanja koje pruža VS Code:
    - Upišite `./` ili `../`.
    - VS Code će vam ponuditi dostupne opcije na osnovu onoga što ste uneli.
    - Pratite putanju klikom na željeni fajl ili folder kako biste osigurali da je vaša putanja ispravna.

Kada dodate ispravnu relativnu putanju, sačuvajte i pošaljite svoje izmene.

### Proverite da URL-ovi nemaju lokalne oznake

Ovaj tok rada osigurava da nijedan web URL ne sadrži lokalnu oznaku specifičnu za zemlju. Pošto je ovaj repozitorijum globalno dostupan, važno je osigurati da URL-ovi ne sadrže lokalne oznake vaše zemlje.

1. Da biste proverili da li vaši URL-ovi nemaju lokalne oznake, izvršite sledeće zadatke:

    - Proverite tekst poput `/en-us/`, `/en/` ili bilo koje druge jezičke oznake u URL-ovima.
    - Ako ove oznake nisu prisutne u vašim URL-ovima, proći ćete ovu proveru.

1. Da biste rešili ovaj problem, izvršite sledeće zadatke:
    - Otvorite putanju fajla koju je označio tok rada.
    - Uklonite lokalnu oznaku iz URL-ova.

Kada uklonite lokalnu oznaku, sačuvajte i pošaljite svoje izmene.

### Proverite pokidane URL-ove

Ovaj tok rada osigurava da svaki web URL u vašim fajlovima funkcioniše i vraća statusni kod 200.

1. Da biste proverili da li vaši URL-ovi ispravno funkcionišu, izvršite sledeće zadatke:
    - Proverite status URL-ova u vašim fajlovima.

2. Da biste popravili bilo koje pokidane URL-ove, izvršite sledeće zadatke:
    - Otvorite fajl koji sadrži pokidani URL.
    - Ažurirajte URL na ispravan.

Kada popravite URL-ove, sačuvajte i pošaljite svoje izmene.

> [!NOTE]
>
> Mogu postojati slučajevi kada provera URL-a ne uspe, iako je link dostupan. Ovo se može desiti iz nekoliko razloga, uključujući:
>
> - **Ograničenja mreže:** GitHub akcioni serveri mogu imati mrežna ograničenja koja sprečavaju pristup određenim URL-ovima.
> - **Problemi sa vremenom isteka:** URL-ovi koji predugo odgovaraju mogu izazvati grešku isteka vremena u toku rada.
> - **Privremeni problemi sa serverom:** Povremeni prekid rada servera ili održavanje može privremeno učiniti URL nedostupnim tokom validacije.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења на бази вештачке интелигенције. Иако тежимо тачности, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу настати употребом овог превода.