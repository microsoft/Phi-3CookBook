# Prilagodite in integrirajte prilagojene modele Phi-3 z uporabo Prompt flow v Azure AI Foundry

Ta celoviti (E2E) primer temelji na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community. Predstavlja postopke prilagajanja, uvajanja in integracije prilagojenih modelov Phi-3 z uporabo Prompt flow v Azure AI Foundry.  
Za razliko od E2E primera "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ki vključuje lokalno izvajanje kode, se ta vadnica osredotoča izključno na prilagajanje in integracijo vašega modela znotraj Azure AI / ML Studio.

## Pregled

V tem E2E primeru se boste naučili, kako prilagoditi model Phi-3 in ga integrirati z uporabo Prompt flow v Azure AI Foundry. Z izkoriščanjem Azure AI / ML Studio boste vzpostavili delovni tok za uvajanje in uporabo prilagojenih AI modelov. Ta E2E primer je razdeljen na tri scenarije:

**Scenarij 1: Nastavite Azure vire in se pripravite na prilagajanje**

**Scenarij 2: Prilagodite model Phi-3 in ga uvedite v Azure Machine Learning Studio**

**Scenarij 3: Integrirajte z uporabo Prompt flow in komunicirajte s svojim prilagojenim modelom v Azure AI Foundry**

Tukaj je pregled tega E2E primera.

![Phi-3-FineTuning_PromptFlow_Integration Pregled.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.sl.png)

### Kazalo

1. **[Scenarij 1: Nastavite Azure vire in se pripravite na prilagajanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ustvarite Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Zahtevajte GPU kvote v Azure naročnini](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dodajte vlogo](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nastavite projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pripravite podatkovni niz za prilagajanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarij 2: Prilagodite model Phi-3 in ga uvedite v Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Prilagodite model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Uvedite prilagojen model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarij 3: Integrirajte z uporabo Prompt flow in komunicirajte s svojim prilagojenim modelom v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrirajte prilagojen model Phi-3 z uporabo Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Komunicirajte s svojim prilagojenim modelom Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenarij 1: Nastavite Azure vire in se pripravite na prilagajanje

### Ustvarite Azure Machine Learning Workspace

1. V iskalni vrstici na vrhu portala vnesite *azure machine learning* in izberite **Azure Machine Learning** iz prikazanih možnosti.

    ![Vnesite azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.sl.png)

2. Izberite **+ Create** v navigacijskem meniju.

3. Izberite **New workspace** v navigacijskem meniju.

    ![Izberite new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.sl.png)

4. Izvedite naslednje naloge:

    - Izberite svojo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti (po potrebi ustvarite novo).
    - Vnesite **Workspace Name**. Mora biti edinstvena vrednost.
    - Izberite **Region**, ki ga želite uporabiti.
    - Izberite **Storage account**, ki ga želite uporabiti (po potrebi ustvarite novega).
    - Izberite **Key vault**, ki ga želite uporabiti (po potrebi ustvarite novega).
    - Izberite **Application insights**, ki jih želite uporabiti (po potrebi ustvarite novega).
    - Izberite **Container registry**, ki ga želite uporabiti (po potrebi ustvarite novega).

    ![Izpolnite azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.sl.png)

5. Izberite **Review + Create**.

6. Izberite **Create**.

### Zahtevajte GPU kvote v Azure naročnini

V tej vadnici se boste naučili, kako prilagoditi in uvesti model Phi-3 z uporabo GPU-jev. Za prilagajanje boste uporabili *Standard_NC24ads_A100_v4* GPU, ki zahteva zahtevo za kvoto. Za uvajanje boste uporabili *Standard_NC6s_v3* GPU, ki prav tako zahteva zahtevo za kvoto.

> [!NOTE]
>
> Samo naročnine Pay-As-You-Go (standardni tip naročnine) so primerne za dodelitev GPU-jev; naročnine z ugodnostmi trenutno niso podprte.
>

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izvedite naslednje naloge za zahtevo kvote za *Standard NCADSA100v4 Family*:

    - Izberite **Quota** v levem zavihku.
    - Izberite **Virtual machine family**, ki ga želite uporabiti. Na primer, izberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ki vključuje *Standard_NC24ads_A100_v4* GPU.
    - Izberite **Request quota** v navigacijskem meniju.

        ![Zahtevajte kvoto.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.sl.png)

    - Na strani za zahtevo kvote vnesite **New cores limit**, ki ga želite uporabiti. Na primer, 24.
    - Na strani za zahtevo kvote izberite **Submit** za zahtevo GPU kvote.

1. Izvedite naslednje naloge za zahtevo kvote za *Standard NCSv3 Family*:

    - Izberite **Quota** v levem zavihku.
    - Izberite **Virtual machine family**, ki ga želite uporabiti. Na primer, izberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, ki vključuje *Standard_NC6s_v3* GPU.
    - Izberite **Request quota** v navigacijskem meniju.
    - Na strani za zahtevo kvote vnesite **New cores limit**, ki ga želite uporabiti. Na primer, 24.
    - Na strani za zahtevo kvote izberite **Submit** za zahtevo GPU kvote.

### Dodajte vlogo

Za prilagajanje in uvajanje svojih modelov morate najprej ustvariti Uporabniško dodeljeno upravljano identiteto (UAI) in ji dodeliti ustrezna dovoljenja. Ta UAI bo uporabljena za avtentikacijo med uvajanjem.

#### Ustvarite Uporabniško dodeljeno upravljano identiteto (UAI)

1. V iskalni vrstici na vrhu portala vnesite *managed identities* in izberite **Managed Identities** iz prikazanih možnosti.

    ![Vnesite managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.sl.png)

1. Izberite **+ Create**.

    ![Izberite create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.sl.png)

1. Izvedite naslednje naloge:

    - Izberite svojo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti (po potrebi ustvarite novo).
    - Izberite **Region**, ki ga želite uporabiti.
    - Vnesite **Name**. Mora biti edinstvena vrednost.

    ![Izberite create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.sl.png)

1. Izberite **Review + create**.

1. Izberite **+ Create**.

#### Dodajte Contributor vlogo upravljani identiteti

1. Pomaknite se do vira Upravljane identitete, ki ste ga ustvarili.

1. Izberite **Azure role assignments** v levem zavihku.

1. Izberite **+Add role assignment** v navigacijskem meniju.

1. Na strani za dodajanje vloge izvedite naslednje naloge:
    - Izberite **Scope** na **Resource group**.
    - Izberite svojo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti.
    - Izberite **Role** na **Contributor**.

    ![Izpolnite Contributor vlogo.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.sl.png)

2. Izberite **Save**.
1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izberite **Compute** iz levega zavihka.

1. Izberite **Compute clusters** iz navigacijskega menija.

1. Izberite **+ New**.

    ![Izberite compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.sl.png)

1. Opravite naslednje naloge:

    - Izberite **Region**, ki ga želite uporabiti.
    - Nastavite **Virtual machine tier** na **Dedicated**.
    - Nastavite **Virtual machine type** na **GPU**.
    - Nastavite filter za **Virtual machine size** na **Select from all options**.
    - Izberite **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Ustvarite cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.sl.png)

1. Izberite **Next**.

1. Opravite naslednje naloge:

    - Vnesite **Compute name**. Ime mora biti edinstveno.
    - Nastavite **Minimum number of nodes** na **0**.
    - Nastavite **Maximum number of nodes** na **1**.
    - Nastavite **Idle seconds before scale down** na **120**.

    ![Ustvarite cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.sl.png)

1. Izberite **Create**.

#### Prilagodite model Phi-3

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izberite Azure Machine Learning delovni prostor, ki ste ga ustvarili.

    ![Izberite ustvarjen delovni prostor.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sl.png)

1. Opravite naslednje naloge:

    - Izberite **Model catalog** iz levega zavihka.
    - Vnesite *phi-3-mini-4k* v **iskalno vrstico** in izberite **Phi-3-mini-4k-instruct** iz prikazanih možnosti.

    ![Vnesite phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.sl.png)

1. Izberite **Fine-tune** iz navigacijskega menija.

    ![Izberite fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.sl.png)

1. Opravite naslednje naloge:

    - Nastavite **Select task type** na **Chat completion**.
    - Izberite **+ Select data** za nalaganje **Traning data**.
    - Nastavite način nalaganja validacijskih podatkov na **Provide different validation data**.
    - Izberite **+ Select data** za nalaganje **Validation data**.

    ![Izpolnite stran za prilagoditev.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.sl.png)

    > [!TIP]
    >
    > Izberete lahko **Advanced settings** za prilagoditev nastavitev, kot so **learning_rate** in **lr_scheduler_type**, da optimizirate proces prilagajanja glede na svoje specifične potrebe.

1. Izberite **Finish**.

1. V tej vaji ste uspešno prilagodili model Phi-3 z uporabo Azure Machine Learning. Upoštevajte, da lahko proces prilagajanja traja precej časa. Po zagonu prilagoditvene naloge morate počakati, da se dokonča. Status prilagoditvene naloge lahko spremljate v zavihku Jobs na levi strani vašega Azure Machine Learning delovnega prostora. V naslednji seriji boste model, ki ste ga prilagodili, implementirali in ga integrirali s Prompt flow.

    ![Poglejte prilagoditveno nalogo.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.sl.png)

### Implementirajte prilagojeni model Phi-3

Za integracijo prilagojenega modela Phi-3 s Prompt flow morate model implementirati, da bo dostopen za realnočasovno sklepanje. Ta proces vključuje registracijo modela, ustvarjanje spletne končne točke in implementacijo modela.

V tej vaji boste:

- Registrirali prilagojeni model v Azure Machine Learning delovnem prostoru.
- Ustvarili spletno končno točko.
- Implementirali registrirani prilagojeni model Phi-3.

#### Registrirajte prilagojeni model

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izberite Azure Machine Learning delovni prostor, ki ste ga ustvarili.

    ![Izberite ustvarjen delovni prostor.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sl.png)

1. Izberite **Models** iz levega zavihka.
1. Izberite **+ Register**.
1. Izberite **From a job output**.

    ![Registrirajte model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.sl.png)

1. Izberite nalogo, ki ste jo ustvarili.

    ![Izberite nalogo.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.sl.png)

1. Izberite **Next**.

1. Nastavite **Model type** na **MLflow**.

1. Prepričajte se, da je izbrana možnost **Job output**; ta bi morala biti samodejno izbrana.

    ![Izberite izhod.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.sl.png)

2. Izberite **Next**.

3. Izberite **Register**.

    ![Izberite register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.sl.png)

4. Svoj registrirani model si lahko ogledate z navigacijo do menija **Models** iz levega zavihka.

    ![Registrirani model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.sl.png)

#### Implementirajte prilagojeni model

1. Pojdite v Azure Machine Learning delovni prostor, ki ste ga ustvarili.

1. Izberite **Endpoints** iz levega zavihka.

1. Izberite **Real-time endpoints** iz navigacijskega menija.

    ![Ustvarite endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.sl.png)

1. Izberite **Create**.

1. Izberite registrirani model, ki ste ga ustvarili.

    ![Izberite registrirani model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.sl.png)

1. Izberite **Select**.

1. Opravite naslednje naloge:

    - Nastavite **Virtual machine** na *Standard_NC6s_v3*.
    - Izberite **Instance count**, ki ga želite uporabiti. Na primer, *1*.
    - Nastavite **Endpoint** na **New**, da ustvarite endpoint.
    - Vnesite **Endpoint name**. Ime mora biti edinstveno.
    - Vnesite **Deployment name**. Ime mora biti edinstveno.

    ![Izpolnite nastavitve implementacije.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.sl.png)

1. Izberite **Deploy**.

> [!WARNING]
> Da se izognete dodatnim stroškom na vašem računu, poskrbite, da izbrišete ustvarjeno končno točko v Azure Machine Learning delovnem prostoru.
>

#### Preverite status implementacije v Azure Machine Learning delovnem prostoru

1. Pojdite v Azure Machine Learning delovni prostor, ki ste ga ustvarili.

1. Izberite **Endpoints** iz levega zavihka.

1. Izberite končno točko, ki ste jo ustvarili.

    ![Izberite endpoints.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.sl.png)

1. Na tej strani lahko upravljate končne točke med procesom implementacije.

> [!NOTE]
> Ko je implementacija končana, poskrbite, da je **Live traffic** nastavljen na **100%**. Če ni, izberite **Update traffic**, da prilagodite nastavitve prometa. Upoštevajte, da modela ne morete testirati, če je promet nastavljen na 0%.
>
> ![Nastavite promet.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.sl.png)
>

## Scenarij 3: Integrirajte s Prompt flow in klepetajte s svojim prilagojenim modelom v Azure AI Foundry

### Integrirajte prilagojen model Phi-3 s Prompt flow

Ko uspešno implementirate svoj prilagojeni model, ga lahko zdaj integrirate s Prompt Flow, da ga uporabite v realnočasovnih aplikacijah, kar omogoča različne interaktivne naloge z vašim prilagojenim modelom Phi-3.

V tej vaji boste:

- Ustvarili Azure AI Foundry Hub.
- Ustvarili Azure AI Foundry Project.
- Ustvarili Prompt flow.
- Dodali prilagojeno povezavo za prilagojeni model Phi-3.
- Nastavili Prompt flow za klepetanje s svojim prilagojenim modelom Phi-3.

> [!NOTE]
> Prav tako lahko integrirate s Promptflow z uporabo Azure ML Studio. Enak proces integracije se lahko uporabi v Azure ML Studio.

#### Ustvarite Azure AI Foundry Hub

Pred ustvarjanjem projekta morate ustvariti Hub. Hub deluje kot skupina virov, ki vam omogoča organizacijo in upravljanje več projektov znotraj Azure AI Foundry.

1. Obiščite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Izberite **All hubs** iz levega zavihka.

1. Izberite **+ New hub** iz navigacijskega menija.

    ![Ustvarite hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.sl.png)

1. Opravite naslednje naloge:

    - Vnesite **Hub name**. Ime mora biti edinstveno.
    - Izberite svojo Azure **Subscription**.
    - Izberite **Resource group**, ki jo želite uporabiti (ustvarite novo, če je potrebno).
    - Izberite **Location**, ki jo želite uporabiti.
    - Izberite **Connect Azure AI Services**, ki jih želite uporabiti (ustvarite nove, če je potrebno).
    - Nastavite **Connect Azure AI Search** na **Skip connecting**.

    ![Izpolnite hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.sl.png)

1. Izberite **Next**.

#### Ustvarite Azure AI Foundry Project

1. V Hubu, ki ste ga ustvarili, izberite **All projects** iz levega zavihka.

1. Izberite **+ New project** iz navigacijskega menija.

    ![Izberite nov projekt.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.sl.png)

1. Vnesite **Project name**. Ime mora biti edinstveno.

    ![Ustvarite projekt.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.sl.png)

1. Izberite **Create a project**.

#### Dodajte prilagojeno povezavo za prilagojeni model Phi-3

Za integracijo vašega prilagojenega modela Phi-3 s Prompt flow morate shraniti končno točko modela in ključ v prilagojeni povezavi. Ta nastavitev omogoča dostop do vašega prilagojenega modela Phi-3 v Prompt flow.

#### Nastavite api ključ in endpoint uri za prilagojeni model Phi-3

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Pojdite v Azure Machine Learning delovni prostor, ki ste ga ustvarili.

1. Izberite **Endpoints** iz levega zavihka.

    ![Izberite endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.sl.png)

1. Izberite končno točko, ki ste jo ustvarili.

    ![Izberite endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.sl.png)

1. Izberite **Consume** iz navigacijskega menija.

1. Kopirajte svoj **REST endpoint** in **Primary key**.
![Kopiraj API ključ in URI končne točke.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.sl.png)

#### Dodajanje prilagojene povezave

1. Obiščite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pomaknite se do projekta Azure AI Foundry, ki ste ga ustvarili.

1. V projektu, ki ste ga ustvarili, izberite **Settings** na levi stranski vrstici.

1. Izberite **+ New connection**.

    ![Izberite novo povezavo.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.sl.png)

1. Izberite **Custom keys** iz navigacijskega menija.

    ![Izberite prilagojene ključe.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.sl.png)

1. Izvedite naslednje korake:

    - Izberite **+ Add key value pairs**.
    - Za ime ključa vnesite **endpoint** in prilepite končno točko, ki ste jo kopirali iz Azure ML Studio, v polje za vrednost.
    - Ponovno izberite **+ Add key value pairs**.
    - Za ime ključa vnesite **key** in prilepite ključ, ki ste ga kopirali iz Azure ML Studio, v polje za vrednost.
    - Po dodajanju ključev izberite **is secret**, da preprečite razkritje ključa.

    ![Dodajanje povezave.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.sl.png)

1. Izberite **Add connection**.

#### Ustvarjanje Prompt flow

Dodali ste prilagojeno povezavo v Azure AI Foundry. Zdaj ustvarimo Prompt flow s pomočjo naslednjih korakov. Nato boste povezali ta Prompt flow s prilagojeno povezavo, da boste lahko uporabili prilagojen model znotraj Prompt flow.

1. Pomaknite se do projekta Azure AI Foundry, ki ste ga ustvarili.

1. Izberite **Prompt flow** na levi stranski vrstici.

1. Izberite **+ Create** iz navigacijskega menija.

    ![Izberite Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.sl.png)

1. Izberite **Chat flow** iz navigacijskega menija.

    ![Izberite vrsto toka.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.sl.png)

1. Vnesite **Folder name**, ki ga želite uporabiti.

    ![Vnesite ime.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.sl.png)

2. Izberite **Create**.

#### Nastavitev Prompt flow za klepet s prilagojenim modelom Phi-3

Prilagojen model Phi-3 je potrebno vključiti v Prompt flow. Vendar trenutni Prompt flow, ki je na voljo, ni zasnovan za ta namen. Zato morate obstoječi Prompt flow preoblikovati, da omogočite integracijo prilagojenega modela.

1. V Prompt flow izvedite naslednje korake za preoblikovanje obstoječega toka:

    - Izberite **Raw file mode**.
    - Izbrišite vso obstoječo kodo v datoteki *flow.dag.yml*.
    - Dodajte naslednjo kodo v datoteko *flow.dag.yml*.

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

    - Izberite **Save**.

    ![Izberite način surove datoteke.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.sl.png)

1. Dodajte naslednjo kodo v datoteko *integrate_with_promptflow.py*, da uporabite prilagojen model Phi-3 v Prompt flow.

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

    ![Prilepite kodo Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.sl.png)

> [!NOTE]
> Za podrobnejše informacije o uporabi Prompt flow v Azure AI Foundry si lahko ogledate [Prompt flow v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izberite **Chat input**, **Chat output**, da omogočite klepet z vašim modelom.

    ![Vhod in izhod.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.sl.png)

1. Zdaj ste pripravljeni na klepet s svojim prilagojenim modelom Phi-3. V naslednji vaji se boste naučili, kako zagnati Prompt flow in ga uporabiti za klepet s svojim prilagojenim modelom Phi-3.

> [!NOTE]
>
> Preoblikovani tok naj bi izgledal kot na spodnji sliki:
>
> ![Primer toka.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.sl.png)
>

### Klepet s prilagojenim modelom Phi-3

Zdaj, ko ste prilagodili in vključili svoj model Phi-3 v Prompt flow, ste pripravljeni na interakcijo z njim. Ta vaja vas bo vodila skozi postopek nastavitve in začetka klepeta z vašim modelom z uporabo Prompt flow. Z upoštevanjem teh korakov boste lahko v celoti izkoristili zmožnosti vašega prilagojenega modela Phi-3 za različne naloge in pogovore.

- Klepetajte s svojim prilagojenim modelom Phi-3 z uporabo Prompt flow.

#### Zagon Prompt flow

1. Izberite **Start compute sessions**, da zaženete Prompt flow.

    ![Zaženite sejo računalništva.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.sl.png)

1. Izberite **Validate and parse input**, da osvežite parametre.

    ![Preverite vhod.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.sl.png)

1. Izberite **Value** za **connection** do prilagojene povezave, ki ste jo ustvarili. Na primer, *connection*.

    ![Povezava.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.sl.png)

#### Klepet s prilagojenim modelom

1. Izberite **Chat**.

    ![Izberite klepet.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.sl.png)

1. Tukaj je primer rezultatov: Zdaj lahko klepetate s svojim prilagojenim modelom Phi-3. Priporočljivo je, da postavljate vprašanja, ki temeljijo na podatkih, uporabljenih za prilagoditev.

    ![Klepet s Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.sl.png)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja, ki temeljijo na umetni inteligenci. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za kakršne koli nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.