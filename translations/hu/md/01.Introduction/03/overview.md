A Phi-3-mini kontextusában az „inferencia” arra a folyamatra utal, amely során a modell bemenetek alapján előrejelzéseket készít vagy kimeneteket generál. Hadd nyújtsak részletesebb információkat a Phi-3-mini-ről és annak inferencia képességeiről.

A Phi-3-mini a Microsoft által kiadott Phi-3 modellek sorozatának része. Ezeket a modelleket úgy tervezték, hogy újradefiniálják a Kis Nyelvi Modellek (SLM-ek) lehetőségeit.

Íme néhány kulcsfontosságú pont a Phi-3-mini-ről és az inferencia képességeiről:

## **Phi-3-mini áttekintés:**
- A Phi-3-mini 3,8 milliárd paraméterrel rendelkezik.
- Nemcsak hagyományos számítástechnikai eszközökön futtatható, hanem élvonalbeli eszközökön is, például mobil eszközökön és IoT eszközökön.
- A Phi-3-mini megjelenése lehetővé teszi magánszemélyek és vállalatok számára, hogy SLM-eket különböző hardvereszközökön alkalmazzanak, különösen erőforrás-korlátozott környezetekben.
- Különféle modellformátumokat támogat, beleértve a hagyományos PyTorch formátumot, a gguf formátum kvantált változatát, valamint az ONNX-alapú kvantált verziót.

## **A Phi-3-mini elérése:**
A Phi-3-mini eléréséhez használhatja a [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) eszközt egy Copilot alkalmazásban. A Semantic Kernel általában kompatibilis az Azure OpenAI Service-szel, a Hugging Face nyílt forráskódú modelljeivel és helyi modellekkel.
Továbbá használhatja az [Ollama](https://ollama.com) vagy a [LlamaEdge](https://llamaedge.com) eszközöket kvantált modellek futtatására. Az Ollama lehetővé teszi egyéni felhasználók számára különböző kvantált modellek használatát, míg a LlamaEdge platformokon átívelő elérhetőséget biztosít a GGUF modellek számára.

## **Kvantált modellek:**
Sok felhasználó előnyben részesíti a kvantált modellek használatát helyi inferenciához. Például közvetlenül futtathatja az Ollama run Phi-3 parancsot, vagy offline konfigurálhatja egy Modelfile segítségével. A Modelfile meghatározza a GGUF fájl elérési útját és a prompt formátumát.

## **Generatív MI lehetőségek:**
Az SLM-ek, például a Phi-3-mini kombinálása új lehetőségeket nyit meg a generatív MI számára. Az inferencia csak az első lépés; ezek a modellek különféle feladatokhoz használhatók erőforrás-korlátozott, késleltetés-érzékeny és költségkorlátozott környezetekben.

## **A generatív MI felszabadítása a Phi-3-mini segítségével: Útmutató az inferenciához és telepítéshez**
Ismerje meg, hogyan használhatja a Semantic Kernel, Ollama/LlamaEdge és ONNX Runtime eszközöket a Phi-3-mini modellek eléréséhez és inferenciájához, és fedezze fel a generatív MI lehetőségeit különféle alkalmazási forgatókönyvekben.

**Jellemzők**
Phi-3-mini modell inferenciája az alábbi eszközökben:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Összefoglalva, a Phi-3-mini lehetővé teszi a fejlesztők számára, hogy különböző modellformátumokat fedezzenek fel, és kihasználják a generatív MI előnyeit különböző alkalmazási forgatókönyvekben.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.