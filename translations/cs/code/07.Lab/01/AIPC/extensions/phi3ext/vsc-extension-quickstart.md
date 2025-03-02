# Vítejte ve své VS Code Rozšíření

## Co obsahuje složka

* Tato složka obsahuje všechny soubory potřebné pro vaše rozšíření.
* `package.json` - toto je manifestový soubor, ve kterém deklarujete své rozšíření a příkaz.
  * Ukázkový plugin registruje příkaz a definuje jeho název a příkazové jméno. Díky těmto informacím může VS Code zobrazit příkaz v příkazové paletě. Zatím není nutné plugin načítat.
* `src/extension.ts` - toto je hlavní soubor, kde implementujete svůj příkaz.
  * Soubor exportuje jednu funkci, `activate`, která je volána při první aktivaci vašeho rozšíření (v tomto případě spuštěním příkazu). Uvnitř funkce `activate` voláme `registerCommand`.
  * Funkci obsahující implementaci příkazu předáváme jako druhý parametr do `registerCommand`.

## Nastavení

* Nainstalujte doporučené rozšíření (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint)

## Rychlé spuštění

* Stiskněte `F5` pro otevření nového okna s vaším načteným rozšířením.
* Spusťte svůj příkaz z příkazové palety stisknutím (`Ctrl+Shift+P` nebo `Cmd+Shift+P` na Macu) a napište `Hello World`.
* Nastavte zarážky ve svém kódu uvnitř `src/extension.ts` pro ladění vašeho rozšíření.
* Výstup z vašeho rozšíření naleznete v ladicím konzoli.

## Proveďte změny

* Po změně kódu v `src/extension.ts` můžete znovu spustit rozšíření z ladicího panelu.
* Můžete také znovu načíst (`Ctrl+R` nebo `Cmd+R` na Macu) okno VS Code s vaším rozšířením, abyste načetli změny.

## Prozkoumejte API

* Plnou sadu našeho API můžete otevřít, když otevřete soubor `node_modules/@types/vscode/index.d.ts`.

## Spusťte testy

* Nainstalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Spusťte úlohu "watch" pomocí příkazu **Tasks: Run Task**. Ujistěte se, že běží, jinak nemusí být testy objeveny.
* Otevřete zobrazení Testing na panelu aktivit a klikněte na tlačítko "Run Test", nebo použijte klávesovou zkratku `Ctrl/Cmd + ; A`.
* Výsledek testu naleznete ve zobrazení výsledků testů.
* Proveďte změny v `src/test/extension.test.ts` nebo vytvořte nové testovací soubory ve složce `test`.
  * Poskytnutý testovací běh bude zohledňovat pouze soubory odpovídající názvovému vzoru `**.test.ts`.
  * Ve složce `test` můžete vytvořit podsložky a strukturovat své testy podle potřeby.

## Pokračujte dále

* Zmenšete velikost rozšíření a zlepšete čas spuštění pomocí [balíčkování vašeho rozšíření](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikujte své rozšíření](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na tržišti rozšíření VS Code.
* Automatizujte buildy nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. Přestože se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.