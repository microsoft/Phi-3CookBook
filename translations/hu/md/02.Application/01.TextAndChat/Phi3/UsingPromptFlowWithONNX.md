# Windows GPU használata Prompt Flow megoldás létrehozásához Phi-3.5-Instruct ONNX segítségével

Az alábbi dokumentum bemutatja, hogyan használható a PromptFlow az ONNX (Open Neural Network Exchange) segítségével AI-alkalmazások fejlesztéséhez Phi-3 modellek alapján.

A PromptFlow egy fejlesztői eszközkészlet, amely az LLM-alapú (Large Language Model) AI-alkalmazások teljes fejlesztési ciklusát leegyszerűsíti, az ötleteléstől és prototípus-készítéstől kezdve a tesztelésen és értékelésen át.

A PromptFlow és az ONNX integrálásával a fejlesztők a következőket érhetik el:

- **Modellek teljesítményének optimalizálása**: Az ONNX segítségével hatékonyabb modell-inferenciát és -telepítést valósíthatnak meg.
- **Fejlesztés egyszerűsítése**: A PromptFlow segítségével kezelhetik a munkafolyamatokat és automatizálhatják az ismétlődő feladatokat.
- **Együttműködés javítása**: Egységes fejlesztési környezet biztosításával megkönnyíthetik a csapaton belüli együttműködést.

A **Prompt Flow** egy fejlesztői eszközkészlet, amely az LLM-alapú AI-alkalmazások teljes fejlesztési ciklusát leegyszerűsíti, az ötleteléstől, prototípus-készítéstől, teszteléstől, értékeléstől egészen a gyártási telepítésig és monitorozásig. Lehetővé teszi a prompt engineering egyszerűbbé tételét, és segít olyan LLM-alkalmazások létrehozásában, amelyek gyártási minőségűek.

A Prompt Flow képes kapcsolódni az OpenAI-hoz, az Azure OpenAI Service-hez és testreszabható modellekhez (Huggingface, helyi LLM/SLM). A célunk a Phi-3.5 kvantált ONNX modell helyi alkalmazásokhoz történő telepítése. A Prompt Flow segít jobban megtervezni üzleti folyamatainkat és helyi megoldásokat létrehozni Phi-3.5 alapján. Ebben a példában az ONNX Runtime GenAI Library-t fogjuk használni, hogy elkészítsük a Prompt Flow megoldást Windows GPU-n.

## **Telepítés**

### **ONNX Runtime GenAI Windows GPU-hoz**

Olvasd el ezt az útmutatót az ONNX Runtime GenAI Windows GPU-hoz való beállításához [kattints ide](./ORTWindowGPUGuideline.md)

### **Prompt Flow beállítása VSCode-ban**

1. Telepítsd a Prompt Flow VS Code bővítményt.

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.hu.png)

2. Miután telepítetted a Prompt Flow VS Code bővítményt, kattints a bővítményre, majd válaszd a **Telepítési függőségek** opciót, és kövesd az útmutatót a Prompt Flow SDK környezetedbe való telepítéséhez.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.hu.png)

3. Töltsd le a [Minta Kódot](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf), és nyisd meg a VS Code-ban.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.hu.png)

4. Nyisd meg a **flow.dag.yaml** fájlt, és válaszd ki a Python környezetedet.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.hu.png)

   Nyisd meg a **chat_phi3_ort.py** fájlt, és állítsd be a Phi-3.5-instruct ONNX modell helyét.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.hu.png)

5. Futtasd a Prompt Flow-t tesztelés céljából.

Nyisd meg a **flow.dag.yaml** fájlt, és kattints a vizuális szerkesztőre.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.hu.png)

Kattints rá, majd futtasd a teszteléshez.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.hu.png)

1. Futtathatsz batch folyamatokat a terminálban további eredmények ellenőrzéséhez.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Ellenőrizheted az eredményeket az alapértelmezett böngésződben.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.hu.png)

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.