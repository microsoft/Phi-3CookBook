# Karibu kwenye Kiendelezi chako cha VS Code

## Kilichomo kwenye folda

* Folda hii ina faili zote muhimu kwa ajili ya kiendelezi chako.
* `package.json` - hili ni faili la manifest ambapo unatangaza kiendelezi chako na amri.
  * Plugin ya mfano husajili amri na kufafanua jina lake na amri husika. Kwa taarifa hii, VS Code inaweza kuonyesha amri kwenye orodha ya amri. Hata hivyo, bado haitahitaji kupakia plugin.
* `src/extension.ts` - hili ni faili kuu ambapo utatekeleza amri yako.
  * Faili inatoa nje kazi moja, `activate`, ambayo inaitwa mara ya kwanza kabisa kiendelezi chako kinapowashwa (katika kesi hii kwa kutekeleza amri). Ndani ya kazi ya `activate` tunaita `registerCommand`.
  * Tunapitisha kazi iliyo na utekelezaji wa amri kama parameter ya pili kwa `registerCommand`.

## Usanidi

* Sakinisha viendelezi vilivyopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint)

## Anza haraka

* Bonyeza `F5` kufungua dirisha jipya na kiendelezi chako kikiwa kimepakiwa.
* Tekeleza amri yako kutoka kwenye orodha ya amri kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.
* Weka alama za kusimamisha (breakpoints) kwenye msimbo wako ndani ya `src/extension.ts` ili kufanya usuluhishi wa matatizo (debugging) kwa kiendelezi chako.
* Pata matokeo kutoka kwa kiendelezi chako kwenye sehemu ya console ya debug.

## Fanya mabadiliko

* Unaweza kuwasha tena kiendelezi kutoka kwenye upau wa zana wa debug baada ya kufanya mabadiliko kwenye `src/extension.ts`.
* Unaweza pia kupakia upya (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code pamoja na kiendelezi chako ili kupakia mabadiliko yako.

## Chunguza API

* Unaweza kufungua seti nzima ya API yetu unapofungua faili `node_modules/@types/vscode/index.d.ts`.

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Endesha kazi ya "watch" kupitia amri ya **Tasks: Run Task**. Hakikisha hii inafanya kazi, la sivyo majaribio hayataweza kutambuliwa.
* Fungua sehemu ya Testing kutoka kwenye upau wa shughuli na ubofye kitufe cha "Run Test," au tumia kitufe cha mkato `Ctrl/Cmd + ; A`.
* Angalia matokeo ya majaribio kwenye sehemu ya Test Results.
* Fanya mabadiliko kwenye `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda `test`.
  * Kionyeshi cha majaribio kilichotolewa kitazingatia tu faili zinazolingana na muundo wa jina `**.test.ts`.
  * Unaweza kutengeneza folda ndani ya folda ya `test` kupanga majaribio yako kwa namna yoyote unavyotaka.

## Endelea zaidi

* Punguza ukubwa wa kiendelezi na boresha muda wa kuwasha kwa [kufunga kiendelezi chako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Chapisha kiendelezi chako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) kwenye soko la viendelezi vya VS Code.
* Fanya ujenzi wa kiotomatiki kwa kusanidi [Muendelezo wa Ujumuishaji](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo rasmi. Kwa taarifa muhimu, inashauriwa kutumia huduma za watafsiri wa kibinadamu wenye taaluma. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.