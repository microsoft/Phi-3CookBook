# Prispevanje

Ta projekt sprejema prispevke in predloge. Večina prispevkov zahteva, da se strinjate s Pogodbo o licenci za prispevke (CLA), ki potrjuje, da imate pravico in dejansko dodeljujete pravice za uporabo vašega prispevka. Za podrobnosti obiščite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Ko oddate zahtevo za združitev (pull request), bo bot CLA samodejno preveril, ali morate predložiti CLA, in ustrezno označil PR (npr. preverjanje stanja, komentar). Preprosto sledite navodilom, ki jih poda bot. To boste morali storiti le enkrat za vse repozitorije, ki uporabljajo naš CLA.

## Kodeks ravnanja

Ta projekt je sprejel [Kodeks ravnanja za odprtokodno programsko opremo Microsoft](https://opensource.microsoft.com/codeofconduct/). Za več informacij preberite [Pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/) ali se obrnite na [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Opozorila pri ustvarjanju težav

Prosimo, ne odpirajte GitHub težav za splošna vprašanja o podpori, saj naj bi bil seznam GitHub uporabljen za zahteve za funkcionalnosti in prijave napak. Na ta način lahko lažje sledimo dejanskim težavam ali napakam v kodi in ločimo splošne razprave od dejanske kode.

## Kako prispevati

### Smernice za zahteve za združitev

Pri oddaji zahteve za združitev (PR) v repozitorij Phi-3 CookBook upoštevajte naslednje smernice:

- **Razvejite repozitorij**: Vedno razvejite repozitorij na svoj račun, preden izvedete spremembe.

- **Ločene zahteve za združitev (PR)**:
  - Vsako vrsto spremembe oddajte v ločeni zahtevi za združitev. Na primer, popravki napak in posodobitve dokumentacije naj bodo oddani v ločenih PR.
  - Popravki tipkarskih napak in manjše posodobitve dokumentacije se lahko po potrebi združijo v en sam PR.

- **Reševanje konfliktov pri združevanju**: Če vaša zahteva za združitev pokaže konflikte pri združevanju, posodobite svojo lokalno vejo `main`, da bo odražala glavni repozitorij, preden izvedete spremembe.

- **Oddaje prevodov**: Pri oddaji prevoda v PR zagotovite, da mapa za prevode vključuje prevode vseh datotek v izvirni mapi.

### Smernice za prevajanje

> [!IMPORTANT]
>
> Pri prevajanju besedila v tem repozitoriju ne uporabljajte strojnega prevajanja. Prostovoljno prevajajte le v jezike, v katerih ste vešči.

Če ste vešči v neangleškem jeziku, lahko pomagate pri prevajanju vsebine. Za zagotovitev pravilne integracije vaših prevodov sledite tem korakom in smernicam:

- **Ustvarite mapo za prevode**: Pojdite v ustrezno mapo oddelka in ustvarite mapo za prevode za jezik, v katerega prispevate. Na primer:
  - Za uvodni oddelek: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Za oddelek hitrega začetka: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Nadaljujte s tem vzorcem za druge oddelke (03.Inference, 04.Finetuning itd.)

- **Posodobite relativne poti**: Pri prevajanju prilagodite strukturo mape z dodajanjem `../../` na začetek relativnih poti znotraj markdown datotek, da zagotovite pravilno delovanje povezav. Na primer, spremenite na naslednji način:
  - Spremenite `(../../imgs/01/phi3aisafety.png)` v `(../../../../imgs/01/phi3aisafety.png)`

- **Organizirajte svoje prevode**: Vsaka prevedena datoteka mora biti nameščena v ustrezni mapi za prevode oddelka. Na primer, če prevajate uvodni oddelek v španščino, ustvarite naslednje:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Oddajte celovit PR**: Poskrbite, da bodo vse prevedene datoteke za določen oddelek vključene v en PR. Ne sprejemamo delnih prevodov za oddelek. Pri oddaji prevoda v PR poskrbite, da mapa za prevode vključuje prevode vseh datotek v izvirni mapi.

### Smernice za pisanje

Za zagotavljanje doslednosti med vsemi dokumenti uporabite naslednje smernice:

- **Formatiranje URL-jev**: Vse URL-je zavijte v oglate oklepaje, ki jim sledijo okrogli oklepaji, brez dodatnih presledkov okoli ali znotraj njih. Na primer: `[example](https://example.com)`.

- **Relativne povezave**: Uporabite `./` za relativne povezave, ki kažejo na datoteke ali mape v trenutni mapi, in `../` za tiste v nadrejeni mapi. Na primer: `[example](../../path/to/file)` ali `[example](../../../path/to/file)`.

- **Ne specifične za države**: Poskrbite, da vaše povezave ne vključujejo lokalizacij, specifičnih za države. Na primer, izogibajte se `/en-us/` ali `/en/`.

- **Shranjevanje slik**: Vse slike shranite v mapo `./imgs`.

- **Opisna imena slik**: Poimenujte slike opisno z uporabo angleških znakov, številk in vezajev. Na primer: `example-image.jpg`.

## GitHub poteki dela

Ko oddate zahtevo za združitev, bodo sproženi naslednji poteki dela za validacijo sprememb. Sledite spodnjim navodilom, da zagotovite uspešno preverjanje vaše zahteve za združitev:

- [Preverjanje pokvarjenih relativnih poti](../..)
- [Preverjanje, da URL-ji nimajo lokalizacije](../..)

### Preverjanje pokvarjenih relativnih poti

Ta potek dela zagotavlja, da so vse relativne poti v vaših datotekah pravilne.

1. Za zagotovitev pravilnega delovanja povezav izvedite naslednje naloge z uporabo VS Code:
    - Z miško se pomaknite na katero koli povezavo v svojih datotekah.
    - Pritisnite **Ctrl + klik**, da odprete povezavo.
    - Če kliknete povezavo in ta lokalno ne deluje, bo to sprožilo potek dela in povezava ne bo delovala na GitHubu.

1. Za odpravo te težave izvedite naslednje naloge z uporabo predlog poti, ki jih ponuja VS Code:
    - Vnesite `./` ali `../`.
    - VS Code vam bo ponudil možnosti glede na vneseno.
    - Sledite poti s klikom na želeno datoteko ali mapo, da zagotovite pravilnost poti.

Ko dodate pravilno relativno pot, shranite in potisnite svoje spremembe.

### Preverjanje, da URL-ji nimajo lokalizacije

Ta potek dela zagotavlja, da noben spletni URL ne vključuje lokalizacije, specifične za države. Ker je ta repozitorij dostopen globalno, je pomembno, da URL-ji ne vsebujejo lokalizacij vaše države.

1. Za preverjanje, da vaši URL-ji nimajo lokalizacij, izvedite naslednje naloge:

    - Preverite, ali vaši URL-ji vsebujejo besedilo, kot je `/en-us/`, `/en/` ali katero koli drugo lokalizacijo jezika.
    - Če teh ni v vaših URL-jih, boste uspešno opravili to preverjanje.

1. Za odpravo te težave izvedite naslednje naloge:
    - Odprite pot datoteke, ki jo izpostavi potek dela.
    - Odstranite lokalizacijo iz URL-jev.

Ko odstranite lokalizacijo, shranite in potisnite svoje spremembe.

### Preverjanje pokvarjenih URL-jev

Ta potek dela zagotavlja, da vsi spletni URL-ji v vaših datotekah delujejo in vračajo statusno kodo 200.

1. Za preverjanje pravilnega delovanja vaših URL-jev izvedite naslednje naloge:
    - Preverite status URL-jev v svojih datotekah.

2. Za odpravo pokvarjenih URL-jev izvedite naslednje naloge:
    - Odprite datoteko, ki vsebuje pokvarjen URL.
    - Posodobite URL na pravilnega.

Ko popravite URL-je, shranite in potisnite svoje spremembe.

> [!NOTE]
>
> Obstajajo lahko primeri, ko preverjanje URL-jev ne uspe, čeprav je povezava dostopna. To se lahko zgodi iz več razlogov, vključno z:
>
> - **Omejitve omrežja:** Strežniki GitHub Actions imajo lahko omrežne omejitve, ki preprečujejo dostop do določenih URL-jev.
> - **Težave s časovno omejitvijo:** URL-ji, ki potrebujejo preveč časa za odziv, lahko sprožijo napako časovne omejitve v poteku dela.
> - **Začasne težave s strežnikom:** Občasni izpadi ali vzdrževanje strežnika lahko začasno onemogočijo URL med preverjanjem.

**Zavrnitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije priporočamo profesionalni prevod s strani človeškega prevajalca. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.