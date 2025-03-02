Phi-3-mini WebGPU RAG Chatbot

## Bemutató a WebGPU és a RAG minta szemléltetésére
A Phi-3 Onnx Hosted modell RAG mintája a Visszakereséssel Kiegészített Generálás (Retrieval-Augmented Generation) megközelítésre épül, amely ötvözi a Phi-3 modellek erejét az ONNX hosztinggal a hatékony AI alkalmazások érdekében. Ez a minta kulcsfontosságú a modellek finomhangolásában speciális feladatokhoz, és egyesíti a minőséget, a költséghatékonyságot és a hosszú szövegek megértését. Az Azure AI kínálatának része, amely számos könnyen megtalálható, kipróbálható és használható modellt biztosít, különféle iparágak testreszabási igényeit kielégítve. A Phi-3 modellek, köztük a Phi-3-mini, Phi-3-small és Phi-3-medium, elérhetők az Azure AI Model Catalogban, és önállóan vagy platformokon, például HuggingFace-en és ONNX-on keresztül finomhangolhatók és telepíthetők, bemutatva a Microsoft elkötelezettségét a hozzáférhető és hatékony AI megoldások iránt.

## Mi az a WebGPU
A WebGPU egy modern webes grafikus API, amelyet arra terveztek, hogy hatékony hozzáférést biztosítson az eszköz grafikus feldolgozóegységéhez (GPU) közvetlenül a webböngészőkből. A WebGL utódjának szánják, számos kulcsfontosságú fejlesztéssel:

1. **Kompatibilitás modern GPU-kkal**: A WebGPU úgy készült, hogy zökkenőmentesen működjön a mai GPU-architektúrákkal, olyan rendszer-API-kat használva, mint a Vulkan, Metal és Direct3D 12.
2. **Fejlett teljesítmény**: Támogatja az általános célú GPU-számításokat és gyorsabb műveleteket, így alkalmas mind grafikai renderelésre, mind gépi tanulási feladatokra.
3. **Haladó funkciók**: A WebGPU hozzáférést biztosít fejlettebb GPU-képességekhez, lehetővé téve összetettebb és dinamikusabb grafikai és számítási munkafolyamatokat.
4. **Csökkentett JavaScript terhelés**: Azáltal, hogy több feladatot a GPU-ra hárít, a WebGPU jelentősen csökkenti a JavaScript terhelését, jobb teljesítményt és simább élményt biztosítva.

A WebGPU jelenleg olyan böngészőkben támogatott, mint a Google Chrome, és folyamatosan dolgoznak más platformok támogatásának bővítésén.

### 03.WebGPU
Szükséges környezet:

**Támogatott böngészők:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### A WebGPU engedélyezése:

- Chrome/Microsoft Edge böngészőben 

Engedélyezze a `chrome://flags/#enable-unsafe-webgpu` kapcsolót.

#### Nyissa meg a böngészőjét:
Indítsa el a Google Chrome-ot vagy a Microsoft Edge-et.

#### Lépjen a Flags oldalra:
Az URL-sávba írja be: `chrome://flags`, majd nyomja meg az Entert.

#### Keresés a kapcsolóra:
A keresőmezőbe írja be: 'enable-unsafe-webgpu'

#### Kapcsoló engedélyezése:
Keresse meg az #enable-unsafe-webgpu kapcsolót a találatok között.

Kattintson a mellette lévő legördülő menüre, és válassza az Enabled lehetőséget.

#### Böngésző újraindítása:

A kapcsoló engedélyezése után újra kell indítania a böngészőt, hogy az változások érvénybe lépjenek. Kattintson az oldal alján megjelenő Relaunch gombra.

- Linux esetén indítsa el a böngészőt a következő paranccsal: `--enable-features=Vulkan`.
- A Safari 18 (macOS 15) alapértelmezetten engedélyezett WebGPU-val rendelkezik.
- Firefox Nightly böngészőben írja be az about:config címet az URL-sávba, majd `set dom.webgpu.enabled to true`.

### GPU beállítása Microsoft Edge-hez 

Az alábbi lépések segítségével állíthatja be a nagy teljesítményű GPU-t a Microsoft Edge-hez Windows rendszeren:

- **Beállítások megnyitása:** Kattintson a Start menüre, majd válassza a Beállítások lehetőséget.
- **Rendszerbeállítások:** Lépjen a Rendszer, majd a Kijelző fülre.
- **Grafikai beállítások:** Görgessen le, és kattintson a Grafikai beállítások lehetőségre.
- **Alkalmazás kiválasztása:** Az „Alkalmazás kiválasztása a beállításokhoz” alatt válassza az Asztali alkalmazást, majd a Tallózás lehetőséget.
- **Edge kiválasztása:** Keresse meg az Edge telepítési mappáját (általában `C:\Program Files (x86)\Microsoft\Edge\Application`), majd válassza ki a `msedge.exe` fájlt.
- **Beállítások mentése:** Kattintson az Opciók gombra, válassza a Nagy teljesítmény lehetőséget, majd kattintson a Mentés gombra.
Ez biztosítja, hogy a Microsoft Edge a nagy teljesítményű GPU-t használja a jobb teljesítmény érdekében.
- **Indítsa újra** a számítógépét, hogy a beállítások érvénybe lépjenek.

### Kódterület megnyitása:
Navigáljon a GitHub-on lévő tárhelyéhez.
Kattintson a Kód gombra, majd válassza az Open with Codespaces lehetőséget.

Ha még nincs kódtere, létrehozhat egyet az Új kódterület gombra kattintva.

**Megjegyzés** Node környezet telepítése a kódterületen
Egy npm demó futtatása a GitHub kódterületéről remek módja a projekt tesztelésének és fejlesztésének. Íme egy lépésről-lépésre útmutató:

### Környezet beállítása:
Amint a kódtere megnyílik, győződjön meg róla, hogy a Node.js és az npm telepítve van. Ezt a következő parancsokkal ellenőrizheti:
```
node -v
```
```
npm -v
```

Ha nincsenek telepítve, az alábbi parancsokkal telepítheti őket:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigáljon a projekt könyvtárába:
Használja a terminált, hogy elnavigáljon abba a könyvtárba, ahol az npm projektje található:
```
cd path/to/your/project
```

### Függőségek telepítése:
Futtassa a következő parancsot az összes szükséges függőség telepítéséhez, amely a package.json fájlban van felsorolva:

```
npm install
```

### A demó futtatása:
Amint a függőségek telepítve vannak, futtathatja a demó scriptet. Ezt általában a package.json scripts szekciójában határozzák meg. Például, ha a demó script neve „start”, akkor futtassa:

```
npm run build
```
```
npm run dev
```

### A demó elérése:
Ha a demó egy webszervert tartalmaz, a kódterület URL-t biztosít annak eléréséhez. Keresse a figyelmeztetést, vagy ellenőrizze a Ports fület, hogy megtalálja az URL-t.

**Megjegyzés:** A modellnek a böngészőben kell tárolódnia, ezért betöltése eltarthat egy ideig.

### RAG Demó
Töltse fel az `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` markdown fájlt.

### Fájl kiválasztása:
Kattintson a „Fájl kiválasztása” gombra, hogy kiválassza a feltölteni kívánt dokumentumot.

### Dokumentum feltöltése:
A fájl kiválasztása után kattintson a „Feltöltés” gombra, hogy betöltse a dokumentumot a RAG (Visszakereséssel Kiegészített Generálás) számára.

### Chat indítása:
Miután a dokumentum feltöltésre került, elindíthat egy chatbeszélgetést a RAG segítségével, a dokumentum tartalma alapján.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.