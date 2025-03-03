# Üdvözlünk a VS Code bővítményedben

## Mi található a mappában

* Ez a mappa tartalmazza az összes fájlt, amely szükséges a bővítményedhez.
* `package.json` - ez a manifest fájl, amelyben deklarálod a bővítményedet és a parancsot.
  * A minta bővítmény regisztrál egy parancsot, és meghatározza annak címét és nevét. Ezen információk alapján a VS Code meg tudja jeleníteni a parancsot a parancspalettában. Egyelőre még nem szükséges betölteni a bővítményt.
* `src/extension.ts` - ez a fő fájl, ahol megvalósítod a parancsodat.
  * A fájl egyetlen függvényt exportál, `activate`, amelyet először akkor hív meg a rendszer, amikor a bővítményed aktiválódik (jelen esetben a parancs végrehajtásával). A `activate` függvényen belül meghívjuk a `registerCommand`-et.
  * A parancs megvalósítását tartalmazó függvényt második paraméterként adjuk át a `registerCommand`-nek.

## Beállítás

* Telepítsd az ajánlott bővítményeket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner és dbaeumer.vscode-eslint).

## Kezdj el azonnal dolgozni

* Nyomd meg a `F5` billentyűkombinációt, hogy megnyiss egy új ablakot a bővítményed betöltésével.
* Hajtsd végre a parancsodat a parancspalettában (`Ctrl+Shift+P` vagy `Cmd+Shift+P` Mac-en), és írd be a `Hello World`-t.
* Állíts be töréspontokat a kódodban a `src/extension.ts` fájlban, hogy hibakeresést végezhess a bővítményeden.
* A bővítményed kimenetét megtalálod a hibakeresési konzolban.

## Végezzen módosításokat

* A hibakeresési eszköztárról újraindíthatod a bővítményt, miután módosítottad a kódot a `src/extension.ts` fájlban.
* A VS Code ablakot is újratöltheted (`Ctrl+R` vagy `Cmd+R` Mac-en) a bővítményed frissítéséhez.

## Fedezd fel az API-t

* Megnyithatod az API teljes dokumentációját a `node_modules/@types/vscode/index.d.ts` fájl megnyitásával.

## Tesztek futtatása

* Telepítsd az [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) bővítményt.
* Futtasd a "watch" feladatot a **Tasks: Run Task** parancs segítségével. Győződj meg róla, hogy ez fut, különben előfordulhat, hogy a teszteket nem találja meg a rendszer.
* Nyisd meg a Tesztelési nézetet az aktivitás sávból, és kattints a "Run Test" gombra, vagy használd a `Ctrl/Cmd + ; A` gyorsbillentyűt.
* A teszteredmények kimenetét a Teszt Eredmények nézetben találod.
* Végezz módosításokat a `src/test/extension.test.ts` fájlban, vagy hozz létre új tesztfájlokat a `test` mappán belül.
  * A biztosított tesztfuttató csak azokat a fájlokat veszi figyelembe, amelyek illeszkednek a `**.test.ts` név mintára.
  * A `test` mappán belül tetszőlegesen létrehozhatsz almappákat a tesztjeid strukturálásához.

## Haladj tovább

* Csökkentsd a bővítmény méretét és javítsd az indítási időt a [bővítmény csomagolásával](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Tedd közzé a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) a VS Code bővítmény piacterén.
* Automatizáld a buildelést [folyamatos integráció](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) beállításával.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatások használatával készült fordítás. Bár igyekszünk a pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.