# **Phi család kvantifikálása**

A modellkvantálás a paraméterek (például súlyok és aktivációs értékek) neuralis hálózati modellben való leképezésére utal, nagy értéktartományból (általában folyamatos értéktartományból) egy kisebb, véges értéktartományba. Ez a technológia csökkentheti a modell méretét és számítási komplexitását, valamint javíthatja a modell működési hatékonyságát erőforrás-korlátozott környezetekben, például mobil eszközökön vagy beágyazott rendszereken. A modellkvantálás a paraméterek pontosságának csökkentésével éri el a tömörítést, de egyúttal bizonyos pontosságveszteséget is bevezet. Ezért a kvantálási folyamat során egyensúlyt kell találni a modell mérete, számítási komplexitása és pontossága között. Gyakori kvantálási módszerek közé tartozik a fixpontos kvantálás, a lebegőpontos kvantálás stb. A megfelelő kvantálási stratégiát a konkrét helyzet és igények szerint választhatjuk ki.

Célunk, hogy a GenAI modellt peremhálózati eszközökön is elérhetővé tegyük, és több eszköz bevonását biztosítsuk a GenAI forgatókönyvekbe, például mobil eszközökön, AI PC / Copilot+PC-ken és hagyományos IoT eszközökön. A kvantált modell segítségével különböző peremhálózati eszközökön deployálhatjuk a modellt, az adott eszközhöz igazítva. A hardvergyártók által biztosított modellgyorsító keretrendszerekkel és kvantált modellekkel kombinálva jobb SLM alkalmazási forgatókönyveket építhetünk.

A kvantálási forgatókönyvben különböző pontossági szintek (INT4, INT8, FP16, FP32) állnak rendelkezésre. Az alábbiakban a leggyakrabban használt kvantálási pontosságokat ismertetjük.

### **INT4**

Az INT4 kvantálás egy radikális kvantálási módszer, amely a modell súlyait és aktivációs értékeit 4 bites egész számokká alakítja. Az INT4 kvantálás általában nagyobb pontosságveszteséget eredményez, mivel kisebb a reprezentációs tartomány és alacsonyabb a pontosság. Azonban az INT8 kvantáláshoz képest az INT4 kvantálás tovább csökkentheti a modell tárhelyigényét és számítási komplexitását. Fontos megjegyezni, hogy az INT4 kvantálás viszonylag ritka a gyakorlatban, mivel a túl alacsony pontosság jelentős teljesítményromlást okozhat a modellben. Ezenkívül nem minden hardver támogatja az INT4 műveleteket, ezért a kvantálási módszer kiválasztásakor figyelembe kell venni a hardver kompatibilitását.

### **INT8**

Az INT8 kvantálás folyamata során a modell súlyait és aktivációs értékeit lebegőpontos számokból 8 bites egész számokká alakítják. Bár az INT8 egész számok által képviselt numerikus tartomány kisebb és kevésbé pontos, jelentősen csökkentheti a tárolási és számítási igényeket. Az INT8 kvantálás során a modell súlyai és aktivációs értékei kvantálási folyamaton mennek keresztül, beleértve a skálázást és az eltolást, hogy az eredeti lebegőpontos információt a lehető legjobban megőrizzék. Az inferencia során ezek a kvantált értékek visszaalakításra kerülnek lebegőpontos számokká a számításokhoz, majd újra INT8 formátumba kvantálják a következő lépéshez. Ez a módszer a legtöbb alkalmazásban elegendő pontosságot biztosít, miközben fenntartja a magas számítási hatékonyságot.

### **FP16**

Az FP16 formátum, azaz 16 bites lebegőpontos számok (float16), a memóriahasználatot felére csökkenti a 32 bites lebegőpontos számokhoz (float32) képest, ami jelentős előnyökkel járhat nagy léptékű mélytanulási alkalmazásokban. Az FP16 formátum lehetővé teszi nagyobb modellek betöltését vagy több adat feldolgozását ugyanazon GPU memória korlátain belül. Ahogy a modern GPU hardverek egyre inkább támogatják az FP16 műveleteket, az FP16 formátum használata számítási sebességnövekedést is eredményezhet. Azonban az FP16 formátumnak megvannak a maga hátrányai is, nevezetesen az alacsonyabb pontosság, amely bizonyos esetekben numerikus instabilitáshoz vagy pontosságveszteséghez vezethet.

### **FP32**

Az FP32 formátum nagyobb pontosságot biztosít, és képes pontosan ábrázolni széles értéktartományt. Olyan forgatókönyvekben, ahol összetett matematikai műveleteket hajtanak végre, vagy nagy pontosságú eredmények szükségesek, az FP32 formátum az előnyös. Azonban a nagy pontosság egyúttal nagyobb memóriahasználatot és hosszabb számítási időt is jelent. Nagy léptékű mélytanulási modellek esetében, különösen amikor sok a modellparaméter és hatalmas az adatmennyiség, az FP32 formátum GPU memóriahiányt vagy az inferencia sebességének csökkenését okozhatja.

Mobil eszközökön vagy IoT eszközökön a Phi-3.x modelleket INT4 formátumba konvertálhatjuk, míg AI PC / Copilot PC esetében magasabb pontosságot, például INT8, FP16 vagy FP32 használhatunk.

Jelenleg különböző hardvergyártók eltérő keretrendszerekkel támogatják a generatív modelleket, például az Intel OpenVINO, a Qualcomm QNN, az Apple MLX és az Nvidia CUDA. Ezeket a keretrendszereket modellkvantálással kombinálva helyi deployálás végezhető el.

Technikai szempontból a kvantálás után különböző formátumok támogatottak, például PyTorch / Tensorflow formátum, GGUF és ONNX. Összehasonlítottam a GGUF és az ONNX formátumot, valamint alkalmazási forgatókönyveiket. Itt az ONNX kvantálási formátumot ajánlom, amely jó támogatást nyújt a modelltől a hardverig. Ebben a fejezetben az ONNX Runtime for GenAI-t, az OpenVINO-t és az Apple MLX-et fogjuk használni modellkvantáláshoz (ha van jobb módszered, azt PR-ben is benyújthatod nekünk).

**Ez a fejezet tartalmazza**

1. [Phi-3.5 / 4 kvantálása llama.cpp segítségével](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantálása Generative AI kiterjesztésekkel az onnxruntime-hoz](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantálása Intel OpenVINO-val](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantálása Apple MLX Framework segítségével](./UsingAppleMLXQuantifyingPhi.md)

**Felelősség kizárása**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.