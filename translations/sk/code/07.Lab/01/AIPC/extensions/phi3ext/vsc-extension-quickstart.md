# Vitajte vo vašom rozšírení pre VS Code

## Čo sa nachádza v priečinku

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - toto je manifest súbor, v ktorom deklarujete vaše rozšírenie a príkaz.
  * Ukážkový plugin registruje príkaz a definuje jeho názov a názov príkazu. S týmito informáciami môže VS Code zobraziť príkaz v príkazovej palete. Plugin sa zatiaľ nemusí načítať.
* `src/extension.ts` - toto je hlavný súbor, kde poskytnete implementáciu vášho príkazu.
  * Súbor exportuje jednu funkciu, `activate`, ktorá je volaná prvýkrát, keď je vaše rozšírenie aktivované (v tomto prípade vykonaním príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* Nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint).

## Začnite hneď pracovať

* Stlačte `F5` na otvorenie nového okna s vaším rozšírením.
* Spustite váš príkaz z príkazovej palety stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a napísaním `Hello World`.
* Nastavte zarážky vo vašom kóde v `src/extension.ts` na ladenie vášho rozšírenia.
* Výstup z vášho rozšírenia nájdete v debug konzole.

## Robte zmeny

* Po zmene kódu v `src/extension.ts` môžete znova spustiť rozšírenie z debug nástrojovej lišty.
* Okno VS Code s vaším rozšírením môžete tiež znova načítať (`Ctrl+R` alebo `Cmd+R` na Macu), aby sa načítali vaše zmeny.

## Preskúmajte API

* Kompletnú sadu nášho API môžete otvoriť otvorením súboru `node_modules/@types/vscode/index.d.ts`.

## Spustite testy

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Spustite úlohu "watch" prostredníctvom príkazu **Tasks: Run Task**. Uistite sa, že je táto úloha spustená, inak sa testy nemusia objaviť.
* Otvorte zobrazenie Testing z aktivity lišty a kliknite na tlačidlo "Run Test" alebo použite klávesovú skratku `Ctrl/Cmd + ; A`.
* Výsledky testov nájdete v zobrazení výsledkov testov.
* Upravte `src/test/extension.test.ts` alebo vytvorte nové testovacie súbory v priečinku `test`.
  * Poskytnutý testovací runner bude brať do úvahy iba súbory, ktoré zodpovedajú názvovému vzoru `**.test.ts`.
  * V priečinku `test` môžete vytvárať priečinky a štruktúrovať vaše testy podľa potreby.

## Choďte ďalej

* Zmenšite veľkosť rozšírenia a zlepšite čas spúšťania [zbalením vášho rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikujte vaše rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na trhovisku rozšírení pre VS Code.
* Automatizujte zostavovanie nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.