# Prispievanie

Tento projekt víta príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste súhlasili s Dohodou o licencii prispievateľa (CLA), ktorá potvrdzuje, že máte právo poskytnúť nám práva na použitie vášho príspevku. Podrobnosti nájdete na stránke [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Keď odošlete pull request, bot CLA automaticky určí, či musíte poskytnúť CLA, a správne označí PR (napr. kontrola stavu, komentár). Jednoducho postupujte podľa pokynov, ktoré vám bot poskytne. Tento proces musíte vykonať iba raz pre všetky repozitáre, ktoré využívajú náš CLA.

## Kódex správania

Tento projekt prijal [Kódex správania pre open source od Microsoftu](https://opensource.microsoft.com/codeofconduct/). Pre viac informácií si prečítajte [FAQ ku kódexu správania](https://opensource.microsoft.com/codeofconduct/faq/) alebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Upozornenia pri vytváraní issue

Prosím, nevytvárajte GitHub issue pre všeobecné otázky podpory, pretože zoznam GitHub by mal byť používaný na požiadavky na funkcie a hlásenia chýb. Týmto spôsobom môžeme jednoduchšie sledovať skutočné problémy alebo chyby z kódu a oddeliť všeobecnú diskusiu od samotného kódu.

## Ako prispieť

### Pokyny pre pull requesty

Pri odosielaní pull requestu (PR) do repozitára Phi-3 CookBook dodržujte nasledujúce pokyny:

- **Forknite repozitár**: Vždy si forknite repozitár do svojho účtu predtým, než urobíte úpravy.

- **Oddelené pull requesty (PR)**:
  - Každý typ zmeny odosielajte v samostatnom pull requeste. Napríklad opravy chýb a aktualizácie dokumentácie by mali byť odoslané v samostatných PR.
  - Opravy preklepov a drobné aktualizácie dokumentácie je možné kombinovať do jedného PR, ak je to vhodné.

- **Riešenie konfliktov pri zlúčení**: Ak váš pull request obsahuje konflikty pri zlúčení, aktualizujte svoju lokálnu vetvu `main` tak, aby zodpovedala hlavnému repozitáru, predtým než urobíte úpravy.

- **Príspevky na preklady**: Pri odosielaní PR s prekladom sa uistite, že priečinok s prekladmi obsahuje preklady všetkých súborov z pôvodného priečinka.

### Pokyny pre preklady

> [!IMPORTANT]
>
> Pri preklade textu v tomto repozitári nepoužívajte strojový preklad. Prekladajte iba do jazykov, v ktorých ste plynulí.

Ak ovládate iný než anglický jazyk, môžete pomôcť s prekladom obsahu. Na zabezpečenie správnej integrácie vašich príspevkov postupujte podľa týchto pokynov:

- **Vytvorte priečinok pre preklad**: Prejdite do príslušnej sekcie a vytvorte priečinok pre jazyk, do ktorého prispievate. Napríklad:
  - Pre sekciu úvod: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Pre sekciu rýchly začiatok: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Pokračujte v tomto vzore pre ďalšie sekcie (03.Inference, 04.Finetuning atď.).

- **Aktualizujte relatívne cesty**: Pri preklade upravte štruktúru priečinkov pridaním `../../` na začiatok relatívnych ciest v markdown súboroch, aby odkazy fungovali správne. Napríklad, zmeňte nasledovne:
  - Z `(../../imgs/01/phi3aisafety.png)` na `(../../../../imgs/01/phi3aisafety.png)`

- **Organizujte svoje preklady**: Každý preložený súbor by mal byť umiestnený v zodpovedajúcom priečinku sekcie. Napríklad, ak prekladáte sekciu úvod do španielčiny, vytvorte priečinok nasledovne:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Odošlite kompletný PR**: Uistite sa, že všetky preložené súbory pre danú sekciu sú zahrnuté v jednom PR. Neprekladáme čiastočné príspevky pre sekciu. Pri odosielaní PR s prekladom sa uistite, že priečinok s prekladmi obsahuje preklady všetkých súborov z pôvodného priečinka.

### Pokyny pre písanie

Na zabezpečenie konzistencie vo všetkých dokumentoch používajte nasledujúce pokyny:

- **Formátovanie URL**: Všetky URL obalte do hranatých zátvoriek nasledovaných okrúhlymi zátvorkami, bez akýchkoľvek medzier okolo alebo vo vnútri. Napríklad: `[example](https://example.com)`.

- **Relatívne odkazy**: Používajte `./` pre relatívne odkazy smerujúce na súbory alebo priečinky v aktuálnom adresári a `../` pre odkazy na nadradený adresár. Napríklad: `[example](../../path/to/file)` alebo `[example](../../../path/to/file)`.

- **Nie špecifické pre krajiny**: Uistite sa, že vaše odkazy neobsahujú špecifické lokálne nastavenia pre krajiny. Napríklad, vyhnite sa `/en-us/` alebo `/en/`.

- **Ukladanie obrázkov**: Ukladajte všetky obrázky do priečinka `./imgs`.

- **Popisné názvy obrázkov**: Pomenúvajte obrázky popisne pomocou anglických znakov, čísel a pomlčiek. Napríklad: `example-image.jpg`.

## GitHub Workflows

Keď odošlete pull request, spustia sa nasledujúce pracovné postupy na validáciu zmien. Postupujte podľa pokynov nižšie, aby váš pull request prešiel kontrolami pracovného postupu:

- [Kontrola nefunkčných relatívnych ciest](../..)
- [Kontrola, že URL neobsahujú lokalizáciu](../..)

### Kontrola nefunkčných relatívnych ciest

Tento pracovný postup zabezpečuje, že všetky relatívne cesty vo vašich súboroch sú správne.

1. Na overenie funkčnosti odkazov vykonajte nasledujúce úlohy v VS Code:
    - Prejdite myšou na akýkoľvek odkaz vo vašich súboroch.
    - Stlačte **Ctrl + Klik** na navigáciu na odkaz.
    - Ak kliknete na odkaz a nefunguje lokálne, spustí to pracovný postup a nebude fungovať ani na GitHube.

1. Na opravu tohto problému vykonajte nasledujúce úlohy pomocou návrhov ciest poskytnutých VS Code:
    - Napíšte `./` alebo `../`.
    - VS Code vám navrhne dostupné možnosti na základe toho, čo ste napísali.
    - Sledujte cestu kliknutím na požadovaný súbor alebo priečinok, aby ste sa uistili, že vaša cesta je správna.

Keď pridáte správnu relatívnu cestu, uložte a odošlite svoje zmeny.

### Kontrola, že URL neobsahujú lokalizáciu

Tento pracovný postup zabezpečuje, že žiadna webová URL neobsahuje lokalizáciu špecifickú pre krajinu. Pretože tento repozitár je prístupný globálne, je dôležité zabezpečiť, aby URL neobsahovali lokalizáciu vašej krajiny.

1. Na overenie, že vaše URL neobsahujú lokalizácie krajín, vykonajte nasledujúce úlohy:

    - Skontrolujte text ako `/en-us/`, `/en/` alebo akékoľvek iné jazykové lokalizácie v URL.
    - Ak tieto lokalizácie nie sú prítomné vo vašich URL, prejdete touto kontrolou.

1. Na opravu tohto problému vykonajte nasledujúce úlohy:
    - Otvorte cestu súboru zvýraznenú pracovným postupom.
    - Odstráňte lokalizáciu krajiny z URL.

Keď odstránite lokalizáciu krajiny, uložte a odošlite svoje zmeny.

### Kontrola nefunkčných URL

Tento pracovný postup zabezpečuje, že každá webová URL vo vašich súboroch funguje a vracia stavový kód 200.

1. Na overenie, že vaše URL fungujú správne, vykonajte nasledujúce úlohy:
    - Skontrolujte stav URL vo vašich súboroch.

2. Na opravu nefunkčných URL vykonajte nasledujúce úlohy:
    - Otvorte súbor, ktorý obsahuje nefunkčnú URL.
    - Aktualizujte URL na správnu.

Keď opravíte URL, uložte a odošlite svoje zmeny.

> [!NOTE]
>
> Môžu nastať prípady, keď kontrola URL zlyhá, aj keď je odkaz prístupný. Môže sa to stať z viacerých dôvodov, vrátane:
>
> - **Obmedzenia siete:** Servery GitHub Actions môžu mať obmedzenia siete, ktoré zabraňujú prístupu k určitým URL.
> - **Problémy s časovým limitom:** URL, ktoré reagujú príliš dlho, môžu spôsobiť chybu časového limitu v pracovnom postupe.
> - **Dočasné problémy servera:** Občasné výpadky servera alebo údržba môžu spôsobiť, že URL budú počas validácie dočasne nedostupné.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.