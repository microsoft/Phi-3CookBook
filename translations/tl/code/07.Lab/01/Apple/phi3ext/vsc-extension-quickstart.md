# Maligayang Pagdating sa iyong VS Code Extension

## Ano ang nasa folder

* Ang folder na ito ay naglalaman ng lahat ng kinakailangang file para sa iyong extension.
* `package.json` - ito ang manifest file kung saan idinedeklara mo ang iyong extension at command.
  * Ang sample plugin ay nagrerehistro ng isang command at tinutukoy ang pamagat at pangalan nito. Sa impormasyong ito, maipapakita ng VS Code ang command sa command palette. Hindi pa kailangang i-load ang plugin.
* `src/extension.ts` - ito ang pangunahing file kung saan mo ilalagay ang implementasyon ng iyong command.
  * Ang file ay nag-e-export ng isang function, ang `activate`, na unang tinatawag kapag na-activate ang iyong extension (sa kasong ito, sa pamamagitan ng pag-execute ng command). Sa loob ng function na `activate`, tinatawag natin ang `registerCommand`.
  * Ipinapasa natin ang function na naglalaman ng implementasyon ng command bilang ikalawang parameter sa `registerCommand`.

## Setup

* I-install ang mga inirerekomendang extension (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, at dbaeumer.vscode-eslint)

## Simulan agad

* Pindutin ang `F5` upang magbukas ng bagong window na may naka-load na iyong extension.
* I-run ang iyong command mula sa command palette sa pamamagitan ng pagpindot sa (`Ctrl+Shift+P` o `Cmd+Shift+P` sa Mac) at pag-type ng `Hello World`.
* Maglagay ng breakpoints sa iyong code sa loob ng `src/extension.ts` upang i-debug ang iyong extension.
* Hanapin ang output mula sa iyong extension sa debug console.

## Gumawa ng mga pagbabago

* Maaari mong i-relaunch ang extension mula sa debug toolbar pagkatapos baguhin ang code sa `src/extension.ts`.
* Maaari mo ring i-reload (`Ctrl+R` o `Cmd+R` sa Mac) ang VS Code window na may iyong extension upang i-load ang iyong mga pagbabago.

## Tuklasin ang API

* Maaari mong buksan ang buong set ng aming API kapag binuksan mo ang file na `node_modules/@types/vscode/index.d.ts`.

## Magpatakbo ng mga test

* I-install ang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* I-run ang "watch" task gamit ang command na **Tasks: Run Task**. Siguraduhing ito ay tumatakbo, kung hindi, maaaring hindi ma-detect ang mga test.
* Buksan ang Testing view mula sa activity bar at i-click ang "Run Test" button, o gamitin ang hotkey na `Ctrl/Cmd + ; A`.
* Tingnan ang output ng resulta ng test sa Test Results view.
* Gumawa ng mga pagbabago sa `src/test/extension.test.ts` o gumawa ng bagong mga test file sa loob ng folder na `test`.
  * Ang ibinigay na test runner ay isasaalang-alang lamang ang mga file na tumutugma sa pattern ng pangalan na `**.test.ts`.
  * Maaari kang gumawa ng mga folder sa loob ng `test` upang ayusin ang iyong mga test sa anumang paraan na gusto mo.

## Mas malalim pang kaalaman

* Bawasan ang laki ng extension at pagandahin ang oras ng pagsisimula sa pamamagitan ng [pag-bundle ng iyong extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [I-publish ang iyong extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) sa VS Code extension marketplace.
* I-automate ang builds sa pamamagitan ng pag-set up ng [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng machine-based AI translation. Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.