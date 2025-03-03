# Přispívání

Tento projekt vítá příspěvky a návrhy. Většina příspěvků vyžaduje, abyste souhlasili s Dohodou o přispěvatelských právech (CLA), která potvrzuje, že máte právo a skutečně udělujete nám práva používat váš příspěvek. Podrobnosti naleznete na [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Když odešlete pull request, bot CLA automaticky určí, zda musíte poskytnout CLA, a odpovídajícím způsobem označí PR (např. kontrola stavu, komentář). Stačí postupovat podle pokynů bota. Toto musíte provést pouze jednou pro všechny repozitáře, které používají naši CLA.

## Kodex chování

Tento projekt přijal [Kodex chování pro open source od Microsoftu](https://opensource.microsoft.com/codeofconduct/). Další informace naleznete v [Často kladených otázkách ke Kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/) nebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s případnými dalšími dotazy či připomínkami.

## Upozornění při vytváření problémů

Nepoužívejte GitHub issues pro obecné dotazy na podporu, protože seznam na GitHubu by měl být použit pro žádosti o funkce a hlášení chyb. Tímto způsobem můžeme snáze sledovat skutečné problémy nebo chyby v kódu a oddělit obecnou diskusi od samotného kódu.

## Jak přispívat

### Pokyny pro Pull Requesty

Při odesílání pull requestu (PR) do repozitáře Phi-3 CookBook postupujte podle následujících pokynů:

- **Forkujte repozitář**: Vždy si vytvořte fork repozitáře do svého vlastního účtu, než provedete úpravy.

- **Oddělené pull requesty (PR)**:
  - Každý typ změny odesílejte v samostatném pull requestu. Například opravy chyb a aktualizace dokumentace by měly být odeslány v samostatných PR.
  - Opravy překlepů a drobné aktualizace dokumentace lze kombinovat do jednoho PR, pokud je to vhodné.

- **Řešení konfliktů při sloučení**: Pokud váš pull request ukazuje konflikty při sloučení, aktualizujte svou lokální větev `main` tak, aby odpovídala hlavnímu repozitáři, než provedete úpravy.

- **Příspěvky k překladům**: Při odesílání PR s překladem se ujistěte, že složka s překladem obsahuje překlady všech souborů v původní složce.

### Pokyny k překladům

> [!IMPORTANT]
>
> Při překládání textu v tomto repozitáři nepoužívejte strojový překlad. Překládejte pouze do jazyků, ve kterých jste zběhlí.

Pokud ovládáte jiný než anglický jazyk, můžete pomoci přeložit obsah. Postupujte podle těchto kroků, aby vaše překladatelské příspěvky byly správně integrovány:

- **Vytvořte složku pro překlady**: Přejděte do odpovídající sekce a vytvořte složku pro překlady do jazyka, do kterého přispíváte. Například:
  - Pro sekci úvod: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Pro sekci rychlý start: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Pokračujte v tomto vzoru pro další sekce (03.Inference, 04.Finetuning atd.)

- **Aktualizujte relativní cesty**: Při překládání upravte strukturu složek přidáním `../../` na začátek relativních cest v markdown souborech, aby odkazy fungovaly správně. Například změňte následující:
  - Změňte `(../../imgs/01/phi3aisafety.png)` na `(../../../../imgs/01/phi3aisafety.png)`

- **Organizace překladů**: Každý přeložený soubor by měl být umístěn do odpovídající složky sekce překladu. Například pokud překládáte úvodní sekci do španělštiny, vytvořte následující:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Odešlete kompletní PR**: Ujistěte se, že všechny přeložené soubory pro jednu sekci jsou zahrnuty v jednom PR. Nepřijímáme částečné překlady sekce. Při odesílání PR s překladem se ujistěte, že složka s překladem obsahuje překlady všech souborů v původní složce.

### Pokyny pro psaní

Pro zajištění konzistence ve všech dokumentech používejte následující pokyny:

- **Formátování URL**: Zabalte všechny URL do hranatých závorek následovaných závorkami, bez mezer kolem nebo uvnitř. Například: `[example](https://www.microsoft.com)`.

- **Relativní odkazy**: Používejte `./` pro relativní odkazy, které ukazují na soubory nebo složky v aktuálním adresáři, a `../` pro odkazy ve složce nadřazené. Například: `[example](../../path/to/file)` nebo `[example](../../../path/to/file)`.

- **Nepoužívejte lokální nastavení specifická pro zemi**: Ujistěte se, že vaše odkazy neobsahují lokální nastavení specifická pro zemi. Například se vyhněte `/en-us/` nebo `/en/`.

- **Ukládání obrázků**: Ukládejte všechny obrázky do složky `./imgs`.

- **Popisné názvy obrázků**: Pojmenovávejte obrázky popisně pomocí anglických znaků, čísel a spojovníků. Například: `example-image.jpg`.

## GitHub Workflows

Při odeslání pull requestu se spustí následující workflow, aby se ověřily změny. Postupujte podle níže uvedených pokynů, aby váš pull request prošel kontrolami workflow:

- [Kontrola nefunkčních relativních cest](../..)
- [Kontrola, zda URL neobsahují lokální nastavení](../..)

### Kontrola nefunkčních relativních cest

Tento workflow ověřuje, že všechny relativní cesty ve vašich souborech jsou správné.

1. Aby bylo zajištěno, že vaše odkazy fungují správně, proveďte následující úkoly pomocí VS Code:
    - Najetím kurzorem na jakýkoli odkaz ve vašich souborech.
    - Stiskněte **Ctrl + Klik** pro navigaci na odkaz.
    - Pokud kliknete na odkaz a nefunguje lokálně, workflow se spustí a nebude fungovat ani na GitHubu.

1. Chcete-li tento problém vyřešit, proveďte následující úkoly pomocí návrhů cest poskytovaných VS Code:
    - Zadejte `./` nebo `../`.
    - VS Code vás vyzve k výběru z dostupných možností na základě toho, co jste zadali.
    - Sledujte cestu kliknutím na požadovaný soubor nebo složku, abyste se ujistili, že je vaše cesta správná.

Jakmile přidáte správnou relativní cestu, uložte a pushněte své změny.

### Kontrola, zda URL neobsahují lokální nastavení

Tento workflow ověřuje, že žádná webová URL neobsahuje lokální nastavení specifické pro zemi. Protože je tento repozitář přístupný globálně, je důležité zajistit, aby URL neobsahovaly lokální nastavení vaší země.

1. Chcete-li ověřit, že vaše URL neobsahují lokální nastavení, proveďte následující úkoly:

    - Zkontrolujte text jako `/en-us/`, `/en/` nebo jakékoli jiné jazykové lokální nastavení v URL.
    - Pokud tyto nejsou přítomny ve vašich URL, projdete touto kontrolou.

1. Chcete-li tento problém vyřešit, proveďte následující úkoly:
    - Otevřete cestu k souboru zvýrazněnou workflowem.
    - Odstraňte lokální nastavení z URL.

Jakmile odstraníte lokální nastavení, uložte a pushněte své změny.

### Kontrola nefunkčních URL

Tento workflow ověřuje, že jakákoli webová URL ve vašich souborech funguje a vrací statusový kód 200.

1. Chcete-li ověřit, že vaše URL fungují správně, proveďte následující úkoly:
    - Zkontrolujte stav URL ve vašich souborech.

2. Chcete-li opravit nefunkční URL, proveďte následující úkoly:
    - Otevřete soubor, který obsahuje nefunkční URL.
    - Aktualizujte URL na správnou.

Jakmile opravíte URL, uložte a pushněte své změny.

> [!NOTE]
>
> Mohou nastat případy, kdy kontrola URL selže, i když je odkaz přístupný. To se může stát z několika důvodů, včetně:
>
> - **Omezení sítě:** Servery GitHub Actions mohou mít omezení sítě, která brání přístupu k určitým URL.
> - **Problémy s časovým limitem:** URL, které reagují příliš dlouho, mohou v workflow spustit chybu časového limitu.
> - **Dočasné problémy serveru:** Občasná nedostupnost serveru nebo údržba může způsobit, že URL bude během validace dočasně nedostupná.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladatelských služeb AI. Přestože se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nezodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.