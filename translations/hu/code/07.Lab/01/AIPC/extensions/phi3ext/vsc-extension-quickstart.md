# Üdvözlünk a VS Code bővítményedben

## Mi található a mappában

* Ez a mappa tartalmazza a bővítményedhez szükséges összes fájlt.
* `package.json` - ez a manifest fájl, amelyben deklarálod a bővítményedet és a parancsot.
  * A példa plugin regisztrál egy parancsot, és meghatározza annak címét és nevét. Ezekkel az információkkal a VS Code meg tudja jeleníteni a parancsot a parancspalettában. A plugin betöltése még nem szükséges.
* `src/extension.ts` - ez a fő fájl, ahol a parancsod implementációját biztosítod.
  * A fájl egyetlen függvényt exportál, `activate`, amelyet először hívnak meg, amikor a bővítményed aktiválódik (jelen esetben a parancs végrehajtásával). A `activate` függvényen belül meghívjuk a `registerCommand`-t.
  * A parancs implementációját tartalmazó függvényt második paraméterként adjuk át a `registerCommand`-nak.

## Beállítás

* Telepítsd az ajánlott bővítményeket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner és dbaeumer.vscode-eslint).

## Kezdd el azonnal

* Nyomd meg a `F5` billentyűkombinációt egy új ablak megnyitásához a bővítményeddel betöltve.
* Futtasd a parancsodat a parancspalettából a (`Ctrl+Shift+P` vagy `Cmd+Shift+P` Mac-en) billentyűkombinációval, és írd be a `Hello World`-t.
* Állíts be töréspontokat a kódodban a `src/extension.ts` fájlon belül, hogy hibakeresést végezhess a bővítményeden.
* Találd meg a bővítményed kimenetét a hibakeresési konzolon.

## Változtatások végrehajtása

* Újraindíthatod a bővítményt a hibakeresési eszköztárról, miután módosítottad a kódot a `src/extension.ts` fájlban.
* Emellett újratöltheted (`Ctrl+R` vagy `Cmd+R` Mac-en) a VS Code ablakot a bővítményeddel, hogy betöltsd a változtatásokat.

## Az API felfedezése

* Megnyithatod az API teljes készletét, ha megnyitod a `node_modules/@types/vscode/index.d.ts` fájlt.

## Tesztek futtatása

* Telepítsd a [Bővítmény Tesztfuttatót](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Futtasd a "watch" feladatot a **Feladatok: Feladat futtatása** parancson keresztül. Győződj meg róla, hogy ez fut, különben előfordulhat, hogy a teszteket nem találja meg.
* Nyisd meg a Tesztelés nézetet az aktivitás sávból, és kattints a "Teszt futtatása" gombra, vagy használd a `Ctrl/Cmd + ; A` gyorsbillentyűt.
* Nézd meg a teszteredmények kimenetét a Teszteredmények nézetben.
* Végezhetsz módosításokat a `src/test/extension.test.ts` fájlban, vagy létrehozhatsz új tesztfájlokat a `test` mappán belül.
  * A biztosított tesztfuttató csak azokat a fájlokat veszi figyelembe, amelyek megfelelnek a `**.test.ts` névmintának.
  * Hozhatsz létre mappákat a `test` mappán belül, hogy tetszés szerint strukturáld a tesztjeidet.

## Haladj tovább

* Csökkentsd a bővítmény méretét, és javítsd az indítási időt a [bővítmény csomagolásával](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikáld a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) a VS Code bővítménypiacán.
* Automatizáld az építéseket a [Folyamatos Integráció](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) beállításával.

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.