# Finomhangolás és egyedi Phi-3 modellek integrálása Prompt flow-val az Azure AI Foundry-ban

Ez az elejétől a végéig (E2E) példa a Microsoft Tech Community "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" című útmutatóján alapul. Bemutatja az egyedi Phi-3 modellek finomhangolásának, telepítésének és Prompt flow-val való integrációjának folyamatait az Azure AI Foundry-ban. 
Ellentétben az E2E példával, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", amely a kód helyi futtatását igényelte, ez az útmutató kizárólag az Azure AI / ML Studio-n belüli finomhangolásra és integrációra összpontosít.

## Áttekintés

Ebben az E2E példában megtanulhatod, hogyan kell finomhangolni a Phi-3 modellt, és integrálni azt a Prompt flow-val az Azure AI Foundry-ban. Az Azure AI / ML Studio használatával létrehozol egy munkafolyamatot az egyedi AI modellek telepítéséhez és használatához. Ez az E2E példa három forgatókönyvre van osztva:

**Forgatókönyv 1: Azure erőforrások beállítása és előkészítés a finomhangoláshoz**

**Forgatókönyv 2: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studio-ban**

**Forgatókönyv 3: Integráció a Prompt flow-val és csevegés az egyedi modelleddel az Azure AI Foundry-ban**

Íme egy áttekintés erről az E2E példáról.

![Phi-3-FineTuning_PromptFlow_Integration Áttekintés.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.hu.png)

### Tartalomjegyzék

1. **[Forgatókönyv 1: Azure erőforrások beállítása és előkészítés a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace létrehozása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvóták igénylése az Azure előfizetésben](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Szerepkör-hozzárendelés hozzáadása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt beállítása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Adatkészlet előkészítése a finomhangoláshoz](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Forgatókönyv 2: Phi-3 modell finomhangolása és telepítése az Azure Machine Learning Studio-ban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 modell finomhangolása](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Finomhangolt Phi-3 modell telepítése](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Forgatókönyv 3: Integráció a Prompt flow-val és csevegés az egyedi modelleddel az Azure AI Foundry-ban](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Egyedi Phi-3 modell integrálása a Prompt flow-val](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Csevegés az egyedi Phi-3 modelleddel](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Forgatókönyv 1: Azure erőforrások beállítása és előkészítés a finomhangoláshoz

### Azure Machine Learning Workspace létrehozása

1. Írd be *azure machine learning*-et a portál oldal tetején található **keresősávba**, és válaszd ki az **Azure Machine Learning** opciót a megjelenő lehetőségek közül.

    ![Írd be: azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.hu.png)

2. Válaszd ki a **+ Létrehozás** opciót a navigációs menüből.

3. Válaszd ki az **Új munkaterület** lehetőséget a navigációs menüből.

    ![Válaszd az új munkaterületet.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.hu.png)

4. Végezze el a következő feladatokat:

    - Válaszd ki az Azure **Előfizetésed**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot** (szükség esetén hozz létre egy újat).
    - Add meg a **Munkaterület nevét**. Egyedi értéknek kell lennie.
    - Válaszd ki a használni kívánt **Régiót**.
    - Válaszd ki a használni kívánt **Tárolófiókot** (szükség esetén hozz létre egy újat).
    - Válaszd ki a használni kívánt **Kulcstárolót** (szükség esetén hozz létre egy újat).
    - Válaszd ki a használni kívánt **Alkalmazásfigyelést** (szükség esetén hozz létre egy újat).
    - Válaszd ki a használni kívánt **Tárolóregisztert** (szükség esetén hozz létre egy újat).

    ![Töltsd ki az Azure gépi tanulást.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.hu.png)

5. Válaszd ki a **Felülvizsgálat + Létrehozás** lehetőséget.

6. Válaszd ki a **Létrehozás** opciót.

### GPU kvóták igénylése az Azure előfizetésben

Ebben az oktatóanyagban megtanulhatod, hogyan kell finomhangolni és telepíteni egy Phi-3 modellt GPU-k használatával. A finomhangoláshoz a *Standard_NC24ads_A100_v4* GPU-t fogod használni, amely kvótakérést igényel. A telepítéshez a *Standard_NC6s_v3* GPU-t fogod használni, amely szintén kvótakérést igényel.

> [!NOTE]
>
> Csak a Pay-As-You-Go előfizetések (az alapértelmezett előfizetési típus) jogosultak GPU-elosztásra; az előnyelőfizetések jelenleg nem támogatottak.
>

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Végezd el a következő feladatokat a *Standard NCADSA100v4 Family* kvóta igényléséhez:

    - Válaszd ki a **Kvóta** lehetőséget a bal oldali menüből.
    - Válaszd ki a használni kívánt **Virtuális gépcsaládot**. Például válaszd ki a **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**-t, amely tartalmazza a *Standard_NC24ads_A100_v4* GPU-t.
    - Válaszd ki a **Kvóta igénylése** opciót a navigációs menüből.

        ![Kvóta igénylése.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.hu.png)

    - A Kvóta igénylése oldalon add meg az **Új magkorlát** értékét, amelyet használni szeretnél. Például 24-et.
    - A Kvóta igénylése oldalon válaszd ki a **Beküldés** opciót a GPU kvóta igényléséhez.

1. Végezd el a következő feladatokat a *Standard NCSv3 Family* kvóta igényléséhez:

    - Válaszd ki a **Kvóta** lehetőséget a bal oldali menüből.
    - Válaszd ki a használni kívánt **Virtuális gépcsaládot**. Például válaszd ki a **Standard NCSv3 Family Cluster Dedicated vCPUs**-t, amely tartalmazza a *Standard_NC6s_v3* GPU-t.
    - Válaszd ki a **Kvóta igénylése** opciót a navigációs menüből.
    - A Kvóta igénylése oldalon add meg az **Új magkorlát** értékét, amelyet használni szeretnél. Például 24-et.
    - A Kvóta igénylése oldalon válaszd ki a **Beküldés** opciót a GPU kvóta igényléséhez.

### Szerepkör-hozzárendelés hozzáadása

Ahhoz, hogy finomhangolhasd és telepíthesd a modelleket, először létre kell hoznod egy Felhasználó által hozzárendelt Kezelt Identitást (UAI), és hozzá kell rendelned a megfelelő jogosultságokat. Ezt a Kezelt Identitást fogod használni az autentikációhoz a telepítés során. 

#### Felhasználó által hozzárendelt Kezelt Identitás létrehozása (UAI)

1. Írd be *kezelt identitások* a portál tetején található **keresősávba**, és válaszd ki a **Kezelt Identitások** opciót a megjelenő lehetőségek közül.

    ![Írd be: kezelt identitások.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.hu.png)

1. Válaszd ki a **+ Létrehozás** opciót.

    ![Válaszd ki a létrehozást.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.hu.png)

1. Végezd el a következő feladatokat:

    - Válaszd ki az Azure **Előfizetésed**.
    - Válaszd ki a használni kívánt **Erőforráscsoportot** (szükség esetén hozz létre egy újat).
    - Válaszd ki a használni kívánt **Régiót**.
    - Add meg az **Identitás nevét**. Egyedi értéknek kell lennie.

    ![Töltsd ki az adatokat.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.hu.png)

1. Válaszd ki a **Felülvizsgálat + Létrehozás** opciót.

1. Válaszd ki a **Létrehozás** opciót.
1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki a bal oldali sávból a **Compute** lehetőséget.

1. A navigációs menüben válaszd a **Compute clusters** lehetőséget.

1. Kattints a **+ New** gombra.

    ![Válaszd a compute-t.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.hu.png)

1. Végezze el az alábbi feladatokat:

    - Válaszd ki a használni kívánt **Region**-t.
    - Állítsd a **Virtual machine tier** értékét **Dedicated**-re.
    - Állítsd a **Virtual machine type** értékét **GPU**-ra.
    - A **Virtual machine size** szűrőt állítsd **Select from all options**-ra.
    - Állítsd a **Virtual machine size** értékét **Standard_NC24ads_A100_v4**-re.

    ![Hozz létre egy klasztert.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.hu.png)

1. Kattints a **Next** gombra.

1. Végezze el az alábbi feladatokat:

    - Add meg a **Compute name**-et. Egyedi értéknek kell lennie.
    - Állítsd a **Minimum number of nodes** értékét **0**-ra.
    - Állítsd a **Maximum number of nodes** értékét **1**-re.
    - Állítsd az **Idle seconds before scale down** értékét **120**-ra.

    ![Hozz létre egy klasztert.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.hu.png)

1. Kattints a **Create** gombra.

#### Phi-3 modell finomhangolása

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki a létrehozott Azure Machine Learning munkaterületet.

    ![Válaszd ki a létrehozott munkaterületet.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hu.png)

1. Végezze el az alábbi feladatokat:

    - A bal oldali sávban válaszd ki a **Model catalog** lehetőséget.
    - Írd be a **keresősávba**: *phi-3-mini-4k*, majd válaszd ki a megjelenő lehetőségek közül a **Phi-3-mini-4k-instruct** modellt.

    ![Írd be: phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.hu.png)

1. Válaszd ki a **Fine-tune** lehetőséget a navigációs menüben.

    ![Válaszd a finomhangolást.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.hu.png)

1. Végezze el az alábbi feladatokat:

    - Állítsd a **Select task type** értékét **Chat completion**-re.
    - Kattints a **+ Select data** gombra a **Traning data** feltöltéséhez.
    - Állítsd a Validációs adat feltöltési típusát **Provide different validation data**-ra.
    - Kattints a **+ Select data** gombra a **Validation data** feltöltéséhez.

    ![Töltsd ki a finomhangolási oldalt.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.hu.png)

    > [!TIP]
    >
    > A **Advanced settings** lehetőség kiválasztásával testreszabhatod a konfigurációkat, például a **learning_rate** és **lr_scheduler_type** beállításokat, hogy optimalizáld a finomhangolási folyamatot az egyedi igényeidhez.

1. Kattints a **Finish** gombra.

1. Ebben a gyakorlatban sikeresen finomhangoltad a Phi-3 modellt az Azure Machine Learning segítségével. Ne feledd, hogy a finomhangolási folyamat jelentős időt vehet igénybe. A finomhangolási feladat futtatása után várd meg, amíg befejeződik. A finomhangolási feladat állapotát a bal oldali sávban található **Jobs** fülre navigálva követheted nyomon az Azure Machine Learning munkaterületen. A következő sorozatban a finomhangolt modellt telepíted, és integrálod a Prompt flow-val.

    ![Nézd meg a finomhangolási feladatot.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.hu.png)

### A finomhangolt Phi-3 modell telepítése

Ahhoz, hogy a finomhangolt Phi-3 modellt integráld a Prompt flow-val, telepíteni kell a modellt, hogy valós idejű előrejelzéshez elérhető legyen. Ez a folyamat magában foglalja a modell regisztrálását, egy online végpont létrehozását és a modell telepítését.

Ebben a gyakorlatban:

- Regisztrálod a finomhangolt modellt az Azure Machine Learning munkaterületen.
- Létrehozol egy online végpontot.
- Telepíted a regisztrált finomhangolt Phi-3 modellt.

#### A finomhangolt modell regisztrálása

1. Látogass el az [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) oldalra.

1. Válaszd ki a létrehozott Azure Machine Learning munkaterületet.

    ![Válaszd ki a létrehozott munkaterületet.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hu.png)

1. Válaszd ki a bal oldali sávból a **Models** lehetőséget.
1. Kattints a **+ Register** gombra.
1. Válaszd a **From a job output** lehetőséget.

    ![Modell regisztrálása.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.hu.png)

1. Válaszd ki a létrehozott feladatot.

    ![Feladat kiválasztása.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.hu.png)

1. Kattints a **Next** gombra.

1. Állítsd a **Model type** értékét **MLflow**-ra.

1. Győződj meg arról, hogy a **Job output** ki van választva; ez automatikusan ki kell legyen választva.

    ![Kimenet kiválasztása.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.hu.png)

2. Kattints a **Next** gombra.

3. Kattints a **Register** gombra.

    ![Regisztráció kiválasztása.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.hu.png)

4. A regisztrált modellt a bal oldali sáv **Models** menüjében tekintheted meg.

    ![Regisztrált modell.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.hu.png)

#### A finomhangolt modell telepítése

1. Navigálj a létrehozott Azure Machine Learning munkaterületre.

1. Válaszd ki a bal oldali sávból az **Endpoints** lehetőséget.

1. A navigációs menüben válaszd a **Real-time endpoints** lehetőséget.

    ![Végpont létrehozása.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.hu.png)

1. Kattints a **Create** gombra.

1. Válaszd ki a létrehozott regisztrált modellt.

    ![Regisztrált modell kiválasztása.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.hu.png)

1. Kattints a **Select** gombra.

1. Végezze el az alábbi feladatokat:

    - Állítsd a **Virtual machine** értékét *Standard_NC6s_v3*-ra.
    - Állítsd be a használni kívánt **Instance count** értékét. Például: *1*.
    - Állítsd az **Endpoint** értékét **New**-re, hogy új végpontot hozz létre.
    - Add meg az **Endpoint name**-et. Egyedi értéknek kell lennie.
    - Add meg a **Deployment name**-et. Egyedi értéknek kell lennie.

    ![Töltsd ki a telepítési beállításokat.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.hu.png)

1. Kattints a **Deploy** gombra.

> [!WARNING]
> A további költségek elkerülése érdekében győződj meg arról, hogy törlöd a létrehozott végpontot az Azure Machine Learning munkaterületen.
>

#### A telepítési állapot ellenőrzése az Azure Machine Learning munkaterületen

1. Navigálj a létrehozott Azure Machine Learning munkaterületre.

1. Válaszd ki a bal oldali sávból az **Endpoints** lehetőséget.

1. Válaszd ki a létrehozott végpontot.

    ![Végpontok kiválasztása.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.hu.png)

1. Ezen az oldalon kezelheted a végpontokat a telepítési folyamat során.

> [!NOTE]
> A telepítés befejezése után győződj meg arról, hogy a **Live traffic** értéke **100%**. Ha nem az, válaszd az **Update traffic** lehetőséget a forgalmi beállítások módosításához. Ne feledd, hogy a modellt nem tudod tesztelni, ha a forgalom 0%-ra van állítva.
>
> ![Forgalom beállítása.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.hu.png)
>
![Másold az API kulcsot és az végpont URI-t.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.hu.png)

#### Egyéni kapcsolat hozzáadása

1. Látogass el az [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) oldalára.

1. Navigálj az általad létrehozott Azure AI Foundry projekthez.

1. A létrehozott projektben válaszd ki a bal oldali menüből a **Beállítások** opciót.

1. Válaszd a **+ Új kapcsolat** lehetőséget.

    ![Új kapcsolat kiválasztása.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.hu.png)

1. A navigációs menüben válaszd az **Egyéni kulcsok** lehetőséget.

    ![Egyéni kulcsok kiválasztása.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.hu.png)

1. Hajtsd végre a következő lépéseket:

    - Válaszd a **+ Kulcs-érték párok hozzáadása** opciót.
    - A kulcs neve mezőbe írd be, hogy **endpoint**, és illeszd be az Azure ML Studio-ból másolt végpontot az érték mezőbe.
    - Ismét válaszd a **+ Kulcs-érték párok hozzáadása** opciót.
    - A kulcs neve mezőbe írd be, hogy **key**, és illeszd be az Azure ML Studio-ból másolt kulcsot az érték mezőbe.
    - Miután hozzáadtad a kulcsokat, jelöld be az **is secret** opciót, hogy a kulcs ne legyen látható.

    ![Kapcsolat hozzáadása.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.hu.png)

1. Válaszd a **Kapcsolat hozzáadása** opciót.

#### Prompt flow létrehozása

Most, hogy egyéni kapcsolatot hoztál létre az Azure AI Foundry-ban, létrehozunk egy Prompt flow-t az alábbi lépésekkel. Ezt követően csatlakoztatjuk a Prompt flow-t az egyéni kapcsolathoz, hogy használni tudd a finomhangolt modellt a Prompt flow-ban.

1. Navigálj az általad létrehozott Azure AI Foundry projekthez.

1. A bal oldali menüben válaszd a **Prompt flow** opciót.

1. A navigációs menüben válaszd a **+ Létrehozás** opciót.

    ![Promptflow kiválasztása.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.hu.png)

1. A navigációs menüben válaszd a **Chat flow** opciót.

    ![Chat flow kiválasztása.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.hu.png)

1. Add meg a használni kívánt **Mappa nevet**.

    ![Név megadása.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.hu.png)

2. Válaszd a **Létrehozás** opciót.

#### Prompt flow beállítása az egyéni Phi-3 modellel való csevegéshez

Integrálnod kell a finomhangolt Phi-3 modellt egy Prompt flow-ba. Azonban a meglévő Prompt flow nem erre a célra készült. Ezért újra kell tervezned a Prompt flow-t, hogy lehetővé tedd az egyéni modell integrációját.

1. A Prompt flow-ban hajtsd végre a következő lépéseket a meglévő folyamat újratervezéséhez:

    - Válaszd a **Nyers fájl mód** opciót.
    - Töröld az összes meglévő kódot a *flow.dag.yml* fájlból.
    - Add hozzá a következő kódot a *flow.dag.yml* fájlhoz.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Válaszd a **Mentés** opciót.

    ![Nyers fájl mód kiválasztása.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.hu.png)

1. Add hozzá a következő kódot az *integrate_with_promptflow.py* fájlhoz, hogy az egyéni Phi-3 modellt használhasd a Prompt flow-ban.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow kód beillesztése.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.hu.png)

> [!NOTE]
> További részletekért a Prompt flow használatáról az Azure AI Foundry-ban, látogass el ide: [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Válaszd ki a **Chat input** és **Chat output** opciókat, hogy lehetővé tedd a csevegést a modellel.

    ![Bemenet és kimenet kiválasztása.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.hu.png)

1. Most már készen állsz arra, hogy csevegj az egyéni Phi-3 modellel. A következő gyakorlatban megtanulod, hogyan indítsd el a Prompt flow-t, és hogyan használd a finomhangolt Phi-3 modellel való csevegéshez.

> [!NOTE]
>
> Az újratervezett folyamatnak az alábbi képen látható módon kell kinéznie:
>
> ![Folyamat példa.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.hu.png)
>

### Csevegés az egyéni Phi-3 modellel

Most, hogy finomhangoltad és integráltad az egyéni Phi-3 modellt a Prompt flow-val, készen állsz arra, hogy elkezdd a vele való interakciót. Ez a gyakorlat végigvezet a modell beállításának és csevegésének folyamatán a Prompt flow használatával. A lépések követésével teljes mértékben kihasználhatod a finomhangolt Phi-3 modell képességeit különféle feladatok és beszélgetések során.

- Csevegj az egyéni Phi-3 modellel a Prompt flow használatával.

#### Prompt flow indítása

1. Válaszd a **Számítási munkamenet indítása** opciót a Prompt flow elindításához.

    ![Számítási munkamenet indítása.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.hu.png)

1. Válaszd a **Bemenet érvényesítése és feldolgozása** opciót a paraméterek frissítéséhez.

    ![Bemenet érvényesítése.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.hu.png)

1. Válaszd ki a **Kapcsolat** **Értékét** az általad létrehozott egyéni kapcsolathoz. Például *connection*.

    ![Kapcsolat kiválasztása.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.hu.png)

#### Csevegés az egyéni modellel

1. Válaszd a **Chat** opciót.

    ![Chat kiválasztása.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.hu.png)

1. Íme egy példa az eredményekre: Most már cseveghetsz az egyéni Phi-3 modellel. Javasolt olyan kérdéseket feltenni, amelyek az adatokon alapulnak, amelyeket a finomhangoláshoz használtál.

    ![Csevegés a Prompt flow-val.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.hu.png)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatások segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.