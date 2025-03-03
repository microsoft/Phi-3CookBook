# Üdvözlünk a VS Code kiterjesztésedben

## Mi található a mappában

* Ez a mappa tartalmazza a kiterjesztésedhez szükséges összes fájlt.
* `package.json` - ez a manifest fájl, amelyben deklarálod a kiterjesztésedet és a parancsodat.
  * A példa plugin regisztrál egy parancsot, és meghatározza annak címét és nevét. Ezekkel az információkkal a VS Code meg tudja jeleníteni a parancsot a parancspalettában. A plugin betöltésére még nincs szükség.
* `src/extension.ts` - ez az a fő fájl, ahol megvalósítod a parancsodat.
  * A fájl egyetlen függvényt exportál, `activate`, amely akkor kerül meghívásra, amikor először aktiválódik a kiterjesztésed (ebben az esetben a parancs végrehajtásával). A `activate` függvényen belül meghívjuk a `registerCommand` függvényt.
  * A parancs megvalósítását tartalmazó függvényt második paraméterként adjuk át a `registerCommand`-nak.

## Beállítás

* Telepítsd az ajánlott kiterjesztéseket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner és dbaeumer.vscode-eslint)

## Azonnali indulás

* Nyomd meg a `F5` billentyűkombinációt, hogy megnyiss egy új ablakot a kiterjesztéseddel betöltve.
* Hajtsd végre a parancsodat a parancspalettán keresztül, a következő billentyűkombinációval: (`Ctrl+Shift+P` vagy `Cmd+Shift+P` Mac-en), majd írd be: `Hello World`.
* Állíts be töréspontokat a kódodban az `src/extension.ts` fájlon belül, hogy hibakeresést végezhess a kiterjesztéseden.
* Találd meg a kiterjesztésed kimenetét a hibakeresési konzolban.

## Változtatások végrehajtása

* A kiterjesztést újraindíthatod a hibakeresési eszköztárból, miután módosítottad az `src/extension.ts` fájlban lévő kódot.
* A VS Code ablakot is újratöltheted (`Ctrl+R` vagy `Cmd+R` Mac-en) a kiterjesztésed betöltéséhez, hogy érvényesítsd a változtatásokat.

## Az API felfedezése

* Az API teljes készletét megnyithatod az `node_modules/@types/vscode/index.d.ts` fájl megnyitásával.

## Tesztek futtatása

* Telepítsd az [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) kiterjesztést.
* Futtasd a "watch" feladatot a **Feladatok: Feladat futtatása** paranccsal. Győződj meg róla, hogy ez fut, különben a tesztek nem lesznek felismerhetők.
* Nyisd meg a Tesztelés nézetet az aktivitássávon, és kattints a "Teszt futtatása" gombra, vagy használd a gyorsbillentyűt: `Ctrl/Cmd + ; A`.
* Nézd meg a teszteredményeket a Teszt Eredmények nézetben.
* Végezhetsz módosításokat az `src/test/extension.test.ts` fájlban, vagy hozhatsz létre új tesztfájlokat az `test` mappán belül.
  * A biztosított tesztfuttató csak az `**.test.ts` név mintázatának megfelelő fájlokat veszi figyelembe.
  * Az `test` mappán belül mappákat hozhatsz létre, hogy bármilyen módon strukturálhasd a tesztjeidet.

## További lépések

* Csökkentsd a kiterjesztés méretét és javítsd az indítási időt a [kiterjesztés csomagolásával](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Tedd közzé a kiterjesztésedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) a VS Code kiterjesztés piacterén.
* Automatizáld az építéseket a [Folyamatos Integráció](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) beállításával.

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítószolgáltatások segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.