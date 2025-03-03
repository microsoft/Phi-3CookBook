# Phi-3.5-Instruct WebGPU RAG Chatbot

## Bemutató a WebGPU és a RAG minta bemutatására

A RAG minta a Phi-3.5 Onnx Hosted modellel a Visszakeresés-Alapú Generálás (Retrieval-Augmented Generation) megközelítést alkalmazza, amely a Phi-3.5 modellek erejét ötvözi az ONNX hosztolással a hatékony AI telepítések érdekében. Ez a minta kulcsfontosságú a modellek domain-specifikus feladatokra való finomhangolásában, minőséget, költséghatékonyságot és hosszú szövegek megértését kínálva. Az Azure AI kínálatának része, amely széles modellválasztékot nyújt, amelyeket könnyű megtalálni, kipróbálni és használni, különböző iparágak testreszabási igényeihez igazítva.

## Mi az a WebGPU?
A WebGPU egy modern webes grafikai API, amely lehetővé teszi a webes böngészők számára, hogy közvetlenül hozzáférjenek az eszköz grafikus feldolgozóegységéhez (GPU). Ez a WebGL utódjának szánt API számos kulcsfontosságú fejlesztést kínál:

1. **Kompatibilitás a modern GPU-kkal**: A WebGPU-t úgy tervezték, hogy zökkenőmentesen működjön a korszerű GPU-architektúrákkal, olyan rendszer-API-kat használva, mint a Vulkan, Metal és Direct3D 12.
2. **Javított teljesítmény**: Támogatja az általános célú GPU-számításokat és gyorsabb műveleteket, ami alkalmassá teszi mind grafikai renderelésre, mind gépi tanulási feladatokra.
3. **Fejlett funkciók**: A WebGPU hozzáférést biztosít fejlettebb GPU-képességekhez, lehetővé téve összetettebb és dinamikusabb grafikai és számítási munkaterheléseket.
4. **Csökkentett JavaScript-terhelés**: Azáltal, hogy több feladatot a GPU-ra hárít, a WebGPU jelentősen csökkenti a JavaScript terhelését, jobb teljesítményt és gördülékenyebb élményt nyújtva.

A WebGPU jelenleg támogatott olyan böngészőkben, mint a Google Chrome, és folyamatosan dolgoznak a támogatás kiterjesztésén más platformokra is.

### 03.WebGPU
Szükséges környezet:

**Támogatott böngészők:**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU engedélyezése:

- Chrome/Microsoft Edge böngészőben 

Engedélyezze a `chrome://flags/#enable-unsafe-webgpu` zászlót.

#### Nyissa meg a böngészőjét:
Indítsa el a Google Chrome-ot vagy a Microsoft Edge-et.

#### Lépjen a zászlók oldalára:
Írja be a címsorba a `chrome://flags` parancsot, majd nyomja meg az Enter billentyűt.

#### Keresés a zászlóra:
Az oldal tetején található keresőmezőbe írja be: 'enable-unsafe-webgpu'

#### A zászló engedélyezése:
Keresse meg a #enable-unsafe-webgpu zászlót az eredmények között.

Kattintson a mellette lévő legördülő menüre, és válassza az Engedélyezett opciót.

#### Indítsa újra a böngészőt:

A zászló engedélyezése után újra kell indítania a böngészőt, hogy a változtatások életbe lépjenek. Kattintson az oldal alján megjelenő Újraindítás gombra.

- Linux esetén indítsa el a böngészőt a `--enable-features=Vulkan` paranccsal.
- A Safari 18 (macOS 15) alapértelmezés szerint engedélyezve van a WebGPU.
- Firefox Nightly böngészőben írja be az about:config parancsot a címsorba, majd `set dom.webgpu.enabled to true`.

### GPU beállítása Microsoft Edge-hez

Az alábbi lépések segítenek a nagy teljesítményű GPU beállításában Microsoft Edge-hez Windows rendszeren:

- **Nyissa meg a Beállításokat:** Kattintson a Start menüre, majd válassza a Beállítások lehetőséget.
- **Rendszerbeállítások:** Lépjen a Rendszer, majd a Kijelző menüpontra.
- **Grafikai beállítások:** Görgessen le, és kattintson a Grafikai beállítások lehetőségre.
- **Alkalmazás kiválasztása:** Az „Alkalmazás kiválasztása az előny beállításához” alatt válassza az Asztali alkalmazás opciót, majd kattintson a Tallózás gombra.
- **Edge kiválasztása:** Navigáljon az Edge telepítési mappájába (általában `C:\Program Files (x86)\Microsoft\Edge\Application`), és válassza ki a `msedge.exe` fájlt.
- **Beállítások mentése:** Kattintson a Beállítások gombra, válassza a Nagy teljesítmény opciót, majd kattintson a Mentés gombra.
Ez biztosítja, hogy a Microsoft Edge a nagy teljesítményű GPU-t használja a jobb teljesítmény érdekében.
- **Indítsa újra** a gépét, hogy ezek a beállítások érvénybe lépjenek.

### Példák: Kérjük, [kattintson erre a linkre](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatások segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.