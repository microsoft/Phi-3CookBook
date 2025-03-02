# Vítejte ve své VS Code rozšíření

## Co je ve složce

* Tato složka obsahuje všechny soubory potřebné pro vaše rozšíření.
* `package.json` - to je manifestový soubor, ve kterém deklarujete své rozšíření a příkaz.
  * Ukázkový plugin registruje příkaz a definuje jeho název a jméno příkazu. Na základě těchto informací může VS Code zobrazit příkaz v příkazové paletě. Zatím není potřeba načítat plugin.
* `src/extension.ts` - to je hlavní soubor, kde implementujete svůj příkaz.
  * Tento soubor exportuje jednu funkci, `activate`, která je volána poprvé, když je vaše rozšíření aktivováno (v tomto případě spuštěním příkazu). Uvnitř funkce `activate` voláme `registerCommand`.
  * Funkci obsahující implementaci příkazu předáváme jako druhý parametr do `registerCommand`.

## Nastavení

* Nainstalujte doporučené rozšíření (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint).

## Začněte ihned

* Stiskněte `F5` pro otevření nového okna s vaším rozšířením.
* Spusťte svůj příkaz z příkazové palety stisknutím (`Ctrl+Shift+P` nebo `Cmd+Shift+P` na Macu) a zadáním `Hello World`.
* Nastavte body přerušení ve svém kódu uvnitř `src/extension.ts` pro ladění svého rozšíření.
* Najděte výstup z vašeho rozšíření v ladicí konzoli.

## Proveďte změny

* Po změně kódu v `src/extension.ts` můžete své rozšíření znovu spustit z ladicího panelu.
* Můžete také znovu načíst (`Ctrl+R` nebo `Cmd+R` na Macu) okno VS Code s vaším rozšířením, aby se načetly změny.

## Prozkoumejte API

* Můžete otevřít celou sadu našeho API otevřením souboru `node_modules/@types/vscode/index.d.ts`.

## Spusťte testy

* Nainstalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Spusťte úlohu "watch" přes příkaz **Tasks: Run Task**. Ujistěte se, že je spuštěná, jinak nemusí být testy rozpoznány.
* Otevřete zobrazení Testing na liště aktivit a klikněte na tlačítko "Run Test" nebo použijte klávesovou zkratku `Ctrl/Cmd + ; A`.
* Výsledky testů najdete v zobrazení Test Results.
* Proveďte změny v `src/test/extension.test.ts` nebo vytvořte nové testovací soubory ve složce `test`.
  * Poskytnutý testovací runner bude zpracovávat pouze soubory odpovídající vzoru názvu `**.test.ts`.
  * Ve složce `test` můžete vytvářet podsložky pro libovolné uspořádání testů.

## Jděte dál

* Zmenšete velikost rozšíření a zlepšete dobu spuštění [zabalením svého rozšíření](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte své rozšíření](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na marketplace rozšíření VS Code.
* Automatizujte sestavení nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladových služeb využívajících umělou inteligenci. I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální překlad lidským překladatelem. Nenese žádnou odpovědnost za nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.