# Karibu kwenye Kiendelezi chako cha VS Code

## Kilicho ndani ya folda

* Folda hii ina faili zote muhimu kwa ajili ya kiendelezi chako.  
* `package.json` - hii ni faili ya manifest ambapo unatangaza kiendelezi chako na amri zake.  
  * Plugin ya mfano inasajili amri na kufafanua kichwa na jina la amri hiyo. Kwa taarifa hizi, VS Code inaweza kuonyesha amri kwenye orodha ya amri. Haijalazimika kupakia plugin bado.  
* `src/extension.ts` - hii ni faili kuu ambapo utatekeleza amri yako.  
  * Faili hii inasafirisha kazi moja, `activate`, ambayo inaitwa mara ya kwanza kabisa kiendelezi chako kinapoanzishwa (katika kesi hii kwa kutekeleza amri). Ndani ya kazi ya `activate` tunaita `registerCommand`.  
  * Tunapita kazi inayotekeleza amri kama parameter ya pili kwa `registerCommand`.  

## Mpangilio

* Sakinisha viendelezi vinavyopendekezwa (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, na dbaeumer.vscode-eslint)  

## Anza mara moja

* Bonyeza `F5` kufungua dirisha jipya ukiwa na kiendelezi chako kimepakiwa.  
* Tekeleza amri yako kutoka kwenye orodha ya amri kwa kubonyeza (`Ctrl+Shift+P` au `Cmd+Shift+P` kwenye Mac) na kuandika `Hello World`.  
* Weka sehemu za kusimama (breakpoints) kwenye msimbo wako ndani ya `src/extension.ts` ili kuchunguza kiendelezi chako.  
* Tafuta matokeo kutoka kwa kiendelezi chako kwenye kidirisha cha console ya uchunguzi.  

## Fanya mabadiliko

* Unaweza kuanzisha upya kiendelezi kutoka kwenye upau wa zana za uchunguzi baada ya kubadilisha msimbo ndani ya `src/extension.ts`.  
* Unaweza pia kupakia upya (`Ctrl+R` au `Cmd+R` kwenye Mac) dirisha la VS Code ukiwa na kiendelezi chako ili kupakia mabadiliko yako.  

## Chunguza API

* Unaweza kufungua seti kamili ya API yetu unapofungua faili `node_modules/@types/vscode/index.d.ts`.  

## Endesha majaribio

* Sakinisha [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)  
* Endesha kazi ya "watch" kupitia amri ya **Tasks: Run Task**. Hakikisha kazi hii inaendelea, la sivyo majaribio hayawezi kutambulika.  
* Fungua mwonekano wa Majaribio kutoka kwenye upau wa shughuli na bonyeza kitufe cha "Run Test", au tumia njia ya mkato `Ctrl/Cmd + ; A`  
* Angalia matokeo ya majaribio kwenye mwonekano wa Matokeo ya Majaribio.  
* Fanya mabadiliko kwa `src/test/extension.test.ts` au tengeneza faili mpya za majaribio ndani ya folda `test`.  
  * Kionyeshi cha majaribio kilichotolewa kitazingatia faili zinazolingana na muundo wa jina `**.test.ts` pekee.  
  * Unaweza kuunda folda ndani ya folda ya `test` ili kupanga majaribio yako jinsi unavyotaka.  

## Endelea zaidi

* Punguza ukubwa wa kiendelezi na boresha muda wa kuanzisha kwa [kufunga kiendelezi chako](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).  
* [Chapisha kiendelezi chako](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) kwenye soko la viendelezi vya VS Code.  
* Endesha mchakato wa ujenzi kiotomatiki kwa kusanidi [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).  

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri zinazotegemea AI. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.