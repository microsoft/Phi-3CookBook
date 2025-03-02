# Vitajte vo vašom rozšírení pre VS Code

## Čo obsahuje tento priečinok

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - toto je manifest súbor, v ktorom deklarujete svoje rozšírenie a príkaz.
  * Ukážkový plugin registruje príkaz a definuje jeho názov a meno príkazu. S týmito informáciami môže VS Code zobraziť príkaz v príkazovej palete. Plugin zatiaľ nie je potrebné načítať.
* `src/extension.ts` - toto je hlavný súbor, kde implementujete váš príkaz.
  * Súbor exportuje jednu funkciu, `activate`, ktorá sa volá prvýkrát, keď je vaše rozšírenie aktivované (v tomto prípade vykonaním príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* Nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint).

## Začnite okamžite

* Stlačte `F5` na otvorenie nového okna s vaším rozšírením načítaným.
* Spustite váš príkaz z príkazovej palety stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a zadaním `Hello World`.
* Nastavte body prerušenia vo vašom kóde v súbore `src/extension.ts` na ladenie vášho rozšírenia.
* Nájdite výstup z vášho rozšírenia v debug konzole.

## Urobte zmeny

* Po zmene kódu v `src/extension.ts` môžete znova spustiť rozšírenie z debugovacej lišty.
* Môžete tiež znova načítať (`Ctrl+R` alebo `Cmd+R` na Macu) okno VS Code s vaším rozšírením, aby sa načítali vaše zmeny.

## Preskúmajte API

* Celý súbor API si môžete otvoriť, keď otvoríte súbor `node_modules/@types/vscode/index.d.ts`.

## Spustite testy

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Spustite úlohu "watch" cez príkaz **Tasks: Run Task**. Uistite sa, že je spustená, inak testy nemusia byť objavené.
* Otvorte zobrazenie Testing z panela aktivít a kliknite na tlačidlo "Run Test", alebo použite klávesovú skratku `Ctrl/Cmd + ; A`.
* Výstup výsledkov testu si pozrite v zobrazení Test Results.
* Upravte `src/test/extension.test.ts` alebo vytvorte nové testovacie súbory v priečinku `test`.
  * Poskytnutý testovací runner bude zohľadňovať iba súbory, ktoré zodpovedajú názvovému vzoru `**.test.ts`.
  * Môžete vytvárať priečinky v priečinku `test` a štruktúrovať svoje testy podľa potreby.

## Choďte ďalej

* Zmenšite veľkosť rozšírenia a zlepšite čas spustenia [zabalením vášho rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte svoje rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code marketplace.
* Automatizujte buildy nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, prosím, vezmite na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.