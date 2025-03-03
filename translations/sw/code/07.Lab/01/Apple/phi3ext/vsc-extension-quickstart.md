# Karibu kwenye Kiendelezi chako cha VS Code

## Nini kipo kwenye folda

* Folda hii ina faili zote muhimu kwa ajili ya kiendelezi chako.
* `package.json` - hili ni faili la manifest ambapo unatangaza kiendelezi chako na amri.
  * Plugin ya mfano inasajili amri na kufafanua jina lake na jina la amri. Kwa kutumia taarifa hizi, VS Code inaweza kuonyesha amri kwenye palette ya amri. Haijahitaji kupakia plugin bado.
* `src/extension.ts` - hili ni faili kuu ambapo utatoa utekelezaji wa amri yako.
  * Faili inasafirisha kazi moja, `activate`, ambayo inaitwa mara ya kwanza kabisa kiendelezi chako kinapoanzishwa (katika hali hii kwa kutekeleza amri). Ndani ya kazi ya `activate` tunaita `registerCommand`.
  * Tunapitia kazi inayojumuisha utekelezaji wa amri kama parameter ya pili kwa `registerCommand`.

## Usanidi

* Sakinisha viendelezi vinavyopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint).

## Anza mara moja

* Bonyeza `F5` kufungua dirisha jipya ukiwa na kiendelezi chako kimepakuliwa.
* Tekeleza amri yako kutoka kwenye palette ya amri kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.
* Weka alama za kuvunjika (breakpoints) kwenye msimbo wako ndani ya `src/extension.ts` ili kufuatilia kiendelezi chako.
* Tafuta matokeo kutoka kwa kiendelezi chako kwenye console ya kufuatilia.

## Fanya mabadiliko

* Unaweza kuanzisha tena kiendelezi kutoka kwenye toolbar ya kufuatilia baada ya kubadilisha msimbo ndani ya `src/extension.ts`.
* Unaweza pia kupakia upya (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code ukiwa na kiendelezi chako ili kupakia mabadiliko yako.

## Chunguza API

* Unaweza kufungua seti kamili ya API yetu unapofungua faili `node_modules/@types/vscode/index.d.ts`.

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Tekeleza kazi ya "watch" kupitia amri ya **Tasks: Run Task**. Hakikisha hii inaendelea, la sivyo majaribio hayawezi kugunduliwa.
* Fungua mwonekano wa Majaribio kutoka kwenye activity bar na bonyeza kitufe cha "Run Test," au tumia njia ya mkato `Ctrl/Cmd + ; A`.
* Tazama matokeo ya majaribio kwenye mwonekano wa Matokeo ya Majaribio.
* Fanya mabadiliko kwenye `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda `test`.
  * Kifuatiliaji cha majaribio kilichotolewa kitazingatia tu faili zinazolingana na muundo wa jina `**.test.ts`.
  * Unaweza kuunda folda ndani ya folda `test` ili kupanga majaribio yako kwa njia yoyote unayotaka.

## Nenda mbali zaidi

* Punguza ukubwa wa kiendelezi na boresha muda wa kuanzishwa kwa [kufungasha kiendelezi chako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Chapisha kiendelezi chako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) kwenye soko la viendelezi la VS Code.
* Fanya ujenzi kuwa wa kiotomatiki kwa kusanidi [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.