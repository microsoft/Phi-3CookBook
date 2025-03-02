# Vítejte ve vašem rozšíření pro VS Code

## Co obsahuje tato složka

* Tato složka obsahuje všechny soubory potřebné pro vaše rozšíření.
* `package.json` - to je manifestový soubor, ve kterém deklarujete vaše rozšíření a příkaz.
  * Ukázkový plugin registruje příkaz a definuje jeho název a jméno příkazu. Díky těmto informacím může VS Code zobrazit příkaz v paletě příkazů. Plugin zatím nemusí být načten.
* `src/extension.ts` - to je hlavní soubor, kde implementujete váš příkaz.
  * Soubor exportuje jednu funkci, `activate`, která se volá poprvé, když je vaše rozšíření aktivováno (v tomto případě provedením příkazu). Uvnitř funkce `activate` voláme `registerCommand`.
  * Jako druhý parametr předáváme funkci obsahující implementaci příkazu do `registerCommand`.

## Nastavení

* Nainstalujte doporučené rozšíření (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint).

## Rychlý start

* Stiskněte `F5` pro otevření nového okna s vaším načteným rozšířením.
* Spusťte váš příkaz z palety příkazů stisknutím (`Ctrl+Shift+P` nebo `Cmd+Shift+P` na Macu) a zadejte `Hello World`.
* Nastavte body přerušení ve vašem kódu uvnitř `src/extension.ts` pro ladění vašeho rozšíření.
* Výstup z vašeho rozšíření naleznete v ladicím konzoli.

## Úpravy

* Po změně kódu v `src/extension.ts` můžete znovu spustit rozšíření z ladicího panelu.
* Můžete také znovu načíst (`Ctrl+R` nebo `Cmd+R` na Macu) okno VS Code s vaším rozšířením pro načtení změn.

## Prozkoumejte API

* Plnou sadu našeho API můžete otevřít, když otevřete soubor `node_modules/@types/vscode/index.d.ts`.

## Spuštění testů

* Nainstalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Spusťte úlohu "watch" přes příkaz **Tasks: Run Task**. Ujistěte se, že běží, jinak nemusí být testy objeveny.
* Otevřete zobrazení Testing z panelu aktivit a klikněte na tlačítko "Run Test", nebo použijte klávesovou zkratku `Ctrl/Cmd + ; A`.
* Výsledky testů naleznete ve zobrazení Test Results.
* Proveďte změny v `src/test/extension.test.ts` nebo vytvořte nové testovací soubory uvnitř složky `test`.
  * Poskytnutý testovací nástroj zohledňuje pouze soubory odpovídající názvovému vzoru `**.test.ts`.
  * Můžete vytvářet složky uvnitř složky `test` a strukturovat své testy dle libosti.

## Další kroky

* Zmenšete velikost rozšíření a zlepšete dobu spuštění [zabalením vašeho rozšíření](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte vaše rozšíření](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na tržišti rozšíření pro VS Code.
* Automatizujte sestavení nastavením [kontinuální integrace](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Ačkoli se snažíme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.