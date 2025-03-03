# Vitajte vo vašom rozšírení pre VS Code

## Čo sa nachádza v priečinku

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - toto je manifest súbor, v ktorom deklarujete svoje rozšírenie a príkaz.
  * Ukážkový plugin registruje príkaz a definuje jeho názov a meno príkazu. Na základe týchto informácií môže VS Code zobraziť príkaz v príkazovej palete. Zatiaľ nie je potrebné načítať plugin.
* `src/extension.ts` - toto je hlavný súbor, kde poskytnete implementáciu svojho príkazu.
  * Súbor exportuje jednu funkciu, `activate`, ktorá sa volá pri prvom aktivovaní vášho rozšírenia (v tomto prípade vykonaním príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* Nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint).

## Začnite okamžite

* Stlačte `F5` na otvorenie nového okna s načítaným rozšírením.
* Spustite svoj príkaz z príkazovej palety stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a napísaním `Hello World`.
* Nastavte breakpointy vo svojom kóde v `src/extension.ts` na ladenie svojho rozšírenia.
* Výstup z vášho rozšírenia nájdete v debug konzole.

## Urobte zmeny

* Môžete znova spustiť rozšírenie z debug nástrojovej lišty po zmene kódu v `src/extension.ts`.
* Môžete tiež znova načítať (`Ctrl+R` alebo `Cmd+R` na Macu) okno VS Code s vaším rozšírením, aby sa načítali vaše zmeny.

## Preskúmajte API

* Celý súbor nášho API si môžete otvoriť, keď otvoríte súbor `node_modules/@types/vscode/index.d.ts`.

## Spustite testy

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Spustite úlohu "watch" cez príkaz **Tasks: Run Task**. Uistite sa, že je spustená, inak testy nemusia byť objavené.
* Otvorte zobrazenie Testing na paneli aktivít a kliknite na tlačidlo "Run Test", alebo použite klávesovú skratku `Ctrl/Cmd + ; A`.
* Výsledky testov si pozrite v zobrazení Test Results.
* Urobte zmeny v `src/test/extension.test.ts` alebo vytvorte nové testovacie súbory v priečinku `test`.
  * Poskytnutý testovací runner bude brať do úvahy iba súbory, ktoré zodpovedajú názvovému vzoru `**.test.ts`.
  * V priečinku `test` môžete vytvárať podpriečinky na štruktúrovanie testov podľa vašich potrieb.

## Choďte ďalej

* Znížte veľkosť rozšírenia a zlepšite čas spustenia [zbalením vášho rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikujte svoje rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na trhu rozšírení VS Code.
* Automatizujte buildy nastavením [kontinuálnej integrácie](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladových služieb založených na umelej inteligencii. Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.