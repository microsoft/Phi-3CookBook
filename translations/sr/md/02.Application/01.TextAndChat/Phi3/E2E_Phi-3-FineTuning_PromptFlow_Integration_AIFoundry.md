# Fino podešavanje i integracija prilagođenih Phi-3 modela sa Prompt flow u Azure AI Foundry

Ovaj kompletan primer (E2E) zasniva se na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech zajednice. U njemu se objašnjavaju procesi fino podešavanja, implementacije i integracije prilagođenih Phi-3 modela sa Prompt flow u Azure AI Foundry.  
Za razliku od E2E primera, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", koji podrazumeva lokalno pokretanje koda, ovaj vodič se u potpunosti fokusira na fino podešavanje i integraciju vašeg modela unutar Azure AI / ML Studija.

## Pregled

U ovom E2E primeru naučićete kako da fino podesite Phi-3 model i integrišete ga sa Prompt flow u Azure AI Foundry. Korišćenjem Azure AI / ML Studija, uspostavićete radni tok za implementaciju i korišćenje prilagođenih AI modela. Ovaj primer je podeljen na tri scenarija:

**Scenario 1: Postavljanje Azure resursa i priprema za fino podešavanje**

**Scenario 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studiju**

**Scenario 3: Integracija sa Prompt flow i komunikacija sa vašim prilagođenim modelom u Azure AI Foundry**

Evo pregleda ovog E2E primera.

![Phi-3-FineTuning_PromptFlow_Integration Pregled.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.sr.png)

### Sadržaj

1. **[Scenario 1: Postavljanje Azure resursa i priprema za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Kreiranje Azure Machine Learning radnog prostora](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Zahtev za GPU kvotama u Azure pretplati](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Dodavanje uloga](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Postavljanje projekta](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Priprema skupa podataka za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Scenario 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studiju](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Fino podešavanje Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Implementacija fino podešenog Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Scenario 3: Integracija sa Prompt flow i komunikacija sa vašim prilagođenim modelom u Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Integracija prilagođenog Phi-3 modela sa Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Komunikacija sa vašim prilagođenim Phi-3 modelom](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## Scenario 1: Postavljanje Azure resursa i priprema za fino podešavanje

### Kreiranje Azure Machine Learning radnog prostora

1. Upišite *azure machine learning* u **traku za pretragu** na vrhu portala i izaberite **Azure Machine Learning** iz ponuđenih opcija.  

    ![Upišite azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.sr.png)  

2. Izaberite **+ Create** iz menija za navigaciju.  

3. Izaberite **New workspace** iz menija za navigaciju.  

    ![Izaberite new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.sr.png)  

4. Uradite sledeće zadatke:  

    - Izaberite vašu Azure **pretplatu**.  
    - Izaberite **Resource group** koju želite koristiti (kreirajte novu ako je potrebno).  
    - Unesite **Ime radnog prostora**. Mora biti jedinstvena vrednost.  
    - Izaberite **Region** koji želite koristiti.  
    - Izaberite **Storage account** koji želite koristiti (kreirajte novi ako je potrebno).  
    - Izaberite **Key vault** koji želite koristiti (kreirajte novi ako je potrebno).  
    - Izaberite **Application insights** koji želite koristiti (kreirajte novi ako je potrebno).  
    - Izaberite **Container registry** koji želite koristiti (kreirajte novi ako je potrebno).  

    ![Popunite azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.sr.png)  

5. Izaberite **Review + Create**.  

6. Izaberite **Create**.  

### Zahtev za GPU kvotama u Azure pretplati

U ovom vodiču naučićete kako da fino podesite i implementirate Phi-3 model koristeći GPU-ove. Za fino podešavanje koristićete *Standard_NC24ads_A100_v4* GPU, koji zahteva zahtev za kvotu. Za implementaciju koristićete *Standard_NC6s_v3* GPU, koji takođe zahteva zahtev za kvotu.  

> [!NOTE]  
>  
> Samo Pay-As-You-Go pretplate (standardni tip pretplate) ispunjavaju uslove za GPU alokaciju; pretplate sa beneficijama trenutno nisu podržane.  

1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).  

1. Uradite sledeće zadatke za zahtev *Standard NCADSA100v4 Family* kvote:  

    - Izaberite **Quota** iz leve trake sa alatkama.  
    - Izaberite **Virtual machine family** koju želite koristiti. Na primer, izaberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, koja uključuje *Standard_NC24ads_A100_v4* GPU.  
    - Izaberite **Request quota** iz menija za navigaciju.  

        ![Zahtev za kvotu.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.sr.png)  

    - Na stranici Request quota, unesite **New cores limit** koji želite koristiti. Na primer, 24.  
    - Na stranici Request quota, izaberite **Submit** za zahtev za GPU kvotu.  

1. Uradite sledeće zadatke za zahtev *Standard NCSv3 Family* kvote:  

    - Izaberite **Quota** iz leve trake sa alatkama.  
    - Izaberite **Virtual machine family** koju želite koristiti. Na primer, izaberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, koja uključuje *Standard_NC6s_v3* GPU.  
    - Izaberite **Request quota** iz menija za navigaciju.  
    - Na stranici Request quota, unesite **New cores limit** koji želite koristiti. Na primer, 24.  
    - Na stranici Request quota, izaberite **Submit** za zahtev za GPU kvotu.  

### Dodavanje uloga

Za fino podešavanje i implementaciju vaših modela, prvo morate kreirati Managed Identity (UAI) i dodeliti joj odgovarajuće dozvole. Ova identifikacija će se koristiti za autentifikaciju tokom implementacije.  

#### Kreiranje Managed Identity (UAI)

1. Upišite *managed identities* u **traku za pretragu** na vrhu portala i izaberite **Managed Identities** iz ponuđenih opcija.  

    ![Upišite managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.sr.png)  

1. Izaberite **+ Create**.  

    ![Izaberite create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.sr.png)  

1. Uradite sledeće zadatke:  

    - Izaberite vašu Azure **pretplatu**.  
    - Izaberite **Resource group** koju želite koristiti (kreirajte novu ako je potrebno).  
    - Izaberite **Region** koji želite koristiti.  
    - Unesite **Ime**. Mora biti jedinstvena vrednost.  

    ![Izaberite create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.sr.png)  

1. Izaberite **Review + create**.  

1. Izaberite **+ Create**.  

#### Dodavanje Contributor uloge Managed Identity

1. Idite na Managed Identity resurs koji ste kreirali.  

1. Izaberite **Azure role assignments** iz leve trake sa alatkama.  

1. Izaberite **+Add role assignment** iz menija za navigaciju.  

1. Na stranici Add role assignment, uradite sledeće zadatke:  
    - Izaberite **Scope** kao **Resource group**.  
    - Izaberite vašu Azure **pretplatu**.  
    - Izaberite **Resource group** koju želite koristiti.  
    - Izaberite **Role** kao **Contributor**.  

    ![Popunite Contributor ulogu.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.sr.png)  

2. Izaberite **Save**.  

#### Dodavanje Storage Blob Data Reader uloge Managed Identity  

...  
1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izaberite **Compute** iz levog menija.

1. Izaberite **Compute clusters** iz navigacionog menija.

1. Kliknite na **+ New**.

    ![Izaberite compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.sr.png)

1. Uradite sledeće:

    - Izaberite **Region** koji želite da koristite.
    - Postavite **Virtual machine tier** na **Dedicated**.
    - Postavite **Virtual machine type** na **GPU**.
    - Postavite filter za **Virtual machine size** na **Select from all options**.
    - Izaberite **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Kreirajte klaster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.sr.png)

1. Kliknite na **Next**.

1. Uradite sledeće:

    - Unesite **Compute name**. Mora biti jedinstveno.
    - Postavite **Minimum number of nodes** na **0**.
    - Postavite **Maximum number of nodes** na **1**.
    - Postavite **Idle seconds before scale down** na **120**.

    ![Kreirajte klaster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.sr.png)

1. Kliknite na **Create**.

#### Fino podešavanje Phi-3 modela

1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izaberite Azure Machine Learning radni prostor koji ste kreirali.

    ![Izaberite kreirani radni prostor.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sr.png)

1. Uradite sledeće:

    - Izaberite **Model catalog** iz levog menija.
    - Upišite *phi-3-mini-4k* u **search bar** i izaberite **Phi-3-mini-4k-instruct** iz ponuđenih opcija.

    ![Upišite phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.sr.png)

1. Izaberite **Fine-tune** iz navigacionog menija.

    ![Izaberite fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.sr.png)

1. Uradite sledeće:

    - Postavite **Select task type** na **Chat completion**.
    - Kliknite na **+ Select data** da biste otpremili **Training data**.
    - Postavite opciju za otpremanje validacionih podataka na **Provide different validation data**.
    - Kliknite na **+ Select data** da biste otpremili **Validation data**.

    ![Popunite stranicu za fino podešavanje.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.sr.png)

    > [!TIP]
    >
    > Možete izabrati **Advanced settings** da prilagodite konfiguracije kao što su **learning_rate** i **lr_scheduler_type** kako biste optimizovali proces finog podešavanja prema vašim specifičnim potrebama.

1. Kliknite na **Finish**.

1. U ovom zadatku ste uspešno fino podesili Phi-3 model koristeći Azure Machine Learning. Imajte na umu da proces finog podešavanja može trajati značajno vreme. Nakon pokretanja posla za fino podešavanje, potrebno je sačekati da se završi. Status posla možete pratiti tako što ćete otići na karticu Jobs u levom meniju vašeg Azure Machine Learning radnog prostora. U sledećoj seriji, model će biti implementiran i integrisan sa Prompt flow.

    ![Pogledajte posao finog podešavanja.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.sr.png)

### Implementacija fino podešenog Phi-3 modela

Da biste integrisali fino podešen Phi-3 model sa Prompt flow, potrebno je da implementirate model kako bi bio dostupan za real-time inferenciju. Ovaj proces uključuje registrovanje modela, kreiranje online endpoint-a i implementaciju modela.

U ovom zadatku ćete:

- Registrovati fino podešen model u Azure Machine Learning radnom prostoru.
- Kreirati online endpoint.
- Implementirati registrovani fino podešen Phi-3 model.

#### Registrovanje fino podešenog modela

1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izaberite Azure Machine Learning radni prostor koji ste kreirali.

    ![Izaberite kreirani radni prostor.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sr.png)

1. Izaberite **Models** iz levog menija.
1. Kliknite na **+ Register**.
1. Izaberite **From a job output**.

    ![Registrujte model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.sr.png)

1. Izaberite posao koji ste kreirali.

    ![Izaberite posao.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.sr.png)

1. Kliknite na **Next**.

1. Postavite **Model type** na **MLflow**.

1. Uverite se da je **Job output** automatski izabran.

    ![Izaberite izlaz.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.sr.png)

2. Kliknite na **Next**.

3. Kliknite na **Register**.

    ![Izaberite register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.sr.png)

4. Registrovani model možete videti tako što ćete otići na meni **Models** u levom meniju.

    ![Registrovani model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.sr.png)

#### Implementacija fino podešenog modela

1. Idite u Azure Machine Learning radni prostor koji ste kreirali.

1. Izaberite **Endpoints** iz levog menija.

1. Izaberite **Real-time endpoints** iz navigacionog menija.

    ![Kreirajte endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.sr.png)

1. Kliknite na **Create**.

1. Izaberite registrovani model koji ste kreirali.

    ![Izaberite registrovani model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.sr.png)

1. Kliknite na **Select**.

1. Uradite sledeće:

    - Postavite **Virtual machine** na *Standard_NC6s_v3*.
    - Postavite **Instance count** na željeni broj, na primer, *1*.
    - Postavite **Endpoint** na **New** da biste kreirali novi endpoint.
    - Unesite **Endpoint name**. Mora biti jedinstveno.
    - Unesite **Deployment name**. Mora biti jedinstveno.

    ![Popunite podešavanja implementacije.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.sr.png)

1. Kliknite na **Deploy**.

> [!WARNING]
> Kako biste izbegli dodatne troškove na vašem nalogu, obavezno obrišite kreirani endpoint u Azure Machine Learning radnom prostoru.
>

#### Provera statusa implementacije u Azure Machine Learning radnom prostoru

1. Idite u Azure Machine Learning radni prostor koji ste kreirali.

1. Izaberite **Endpoints** iz levog menija.

1. Izaberite endpoint koji ste kreirali.

    ![Izaberite endpoint.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.sr.png)

1. Na ovoj stranici možete upravljati endpoint-ovima tokom procesa implementacije.

> [!NOTE]
> Kada implementacija bude završena, uverite se da je **Live traffic** postavljen na **100%**. Ako nije, izaberite **Update traffic** kako biste podesili postavke saobraćaja. Imajte na umu da ne možete testirati model ako je saobraćaj postavljen na 0%.
>
> ![Postavite saobraćaj.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.sr.png)
>

## Scenario 3: Integracija sa Prompt flow i razgovor sa vašim prilagođenim modelom u Azure AI Foundry

### Integracija prilagođenog Phi-3 modela sa Prompt flow

Nakon uspešne implementacije vašeg fino podešenog modela, sada možete da ga integrišete sa Prompt Flow kako biste koristili vaš model u real-time aplikacijama, omogućavajući različite interaktivne zadatke sa vašim prilagođenim Phi-3 modelom.

U ovom zadatku ćete:

- Kreirati Azure AI Foundry Hub.
- Kreirati Azure AI Foundry Project.
- Kreirati Prompt flow.
- Dodati prilagođenu konekciju za fino podešen Phi-3 model.
- Podesiti Prompt flow za razgovor sa vašim prilagođenim Phi-3 modelom.

> [!NOTE]
> Takođe možete integrisati sa Promptflow koristeći Azure ML Studio. Isti proces integracije može se primeniti i u Azure ML Studio.

#### Kreiranje Azure AI Foundry Hub-a

Pre nego što kreirate projekat, potrebno je da kreirate Hub. Hub funkcioniše kao Resource Group, omogućavajući organizaciju i upravljanje više projekata unutar Azure AI Foundry.

1. Posetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Izaberite **All hubs** iz levog menija.

1. Kliknite na **+ New hub** iz navigacionog menija.

    ![Kreirajte hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.sr.png)

1. Uradite sledeće:

    - Unesite **Hub name**. Mora biti jedinstveno.
    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Resource group** za korišćenje (kreirajte novu ako je potrebno).
    - Izaberite **Location** koji želite da koristite.
    - Izaberite **Connect Azure AI Services** za korišćenje (kreirajte novi ako je potrebno).
    - Izaberite **Connect Azure AI Search** na **Skip connecting**.

    ![Popunite hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.sr.png)

1. Kliknite na **Next**.

#### Kreiranje Azure AI Foundry Project-a

1. U okviru kreiranog Hub-a, izaberite **All projects** iz levog menija.

1. Kliknite na **+ New project** iz navigacionog menija.

    ![Izaberite novi projekat.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.sr.png)

1. Unesite **Project name**. Mora biti jedinstveno.

    ![Kreirajte projekat.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.sr.png)

1. Kliknite na **Create a project**.

#### Dodavanje prilagođene konekcije za fino podešen Phi-3 model

Da biste integrisali vaš prilagođeni Phi-3 model sa Prompt flow, potrebno je da sačuvate endpoint i ključ modela u prilagođenoj konekciji. Ova postavka obezbeđuje pristup vašem prilagođenom Phi-3 modelu u Prompt flow-u.

#### Postavljanje API ključa i endpoint URI-ja za fino podešen Phi-3 model

1. Posetite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Idite u Azure Machine Learning radni prostor koji ste kreirali.

1. Izaberite **Endpoints** iz levog menija.

    ![Izaberite endpoint.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.sr.png)

1. Izaberite endpoint koji ste kreirali.

    ![Izaberite endpoint.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.sr.png)

1. Izaberite **Consume** iz navigacionog menija.

1. Kopirajte vaš **REST endpoint** i **Primary key**.
![Kopiraj API ključ i URI krajnje tačke.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.sr.png)

#### Dodajte prilagođenu konekciju

1. Posetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Idite na projekat Azure AI Foundry koji ste kreirali.

1. U projektu koji ste kreirali, izaberite **Settings** sa leve strane.

1. Izaberite **+ New connection**.

    ![Izaberite novu konekciju.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.sr.png)

1. Izaberite **Custom keys** iz menija za navigaciju.

    ![Izaberite prilagođene ključeve.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.sr.png)

1. Uradite sledeće zadatke:

    - Izaberite **+ Add key value pairs**.
    - Za naziv ključa unesite **endpoint** i nalepite krajnju tačku koju ste kopirali iz Azure ML Studio u polje za vrednost.
    - Ponovo izaberite **+ Add key value pairs**.
    - Za naziv ključa unesite **key** i nalepite ključ koji ste kopirali iz Azure ML Studio u polje za vrednost.
    - Nakon dodavanja ključeva, izaberite **is secret** kako biste sprečili da ključ bude izložen.

    ![Dodajte konekciju.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.sr.png)

1. Izaberite **Add connection**.

#### Kreirajte Prompt flow

Dodali ste prilagođenu konekciju u Azure AI Foundry. Sada ćemo kreirati Prompt flow koristeći sledeće korake. Zatim ćete povezati ovaj Prompt flow sa prilagođenom konekcijom kako biste mogli da koristite model koji ste fino podesili unutar Prompt flow-a.

1. Idite na projekat Azure AI Foundry koji ste kreirali.

1. Izaberite **Prompt flow** sa leve strane.

1. Izaberite **+ Create** iz menija za navigaciju.

    ![Izaberite Prompt flow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.sr.png)

1. Izaberite **Chat flow** iz menija za navigaciju.

    ![Izaberite chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.sr.png)

1. Unesite **Folder name** koji želite da koristite.

    ![Unesite ime.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.sr.png)

2. Izaberite **Create**.

#### Postavite Prompt flow za razgovor sa vašim prilagođenim Phi-3 modelom

Potrebno je da integrišete fino podešeni Phi-3 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za ovu svrhu. Stoga, morate redizajnirati Prompt flow kako biste omogućili integraciju prilagođenog modela.

1. U Prompt flow-u, uradite sledeće zadatke kako biste rekonstruisali postojeći tok:

    - Izaberite **Raw file mode**.
    - Obrišite sav postojeći kod u datoteci *flow.dag.yml*.
    - Dodajte sledeći kod u datoteku *flow.dag.yml*.

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

    - Izaberite **Save**.

    ![Izaberite raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.sr.png)

1. Dodajte sledeći kod u datoteku *integrate_with_promptflow.py* kako biste koristili prilagođeni Phi-3 model u Prompt flow-u.

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

    ![Nalepite kod za Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.sr.png)

> [!NOTE]
> Za detaljnije informacije o korišćenju Prompt flow-a u Azure AI Foundry, pogledajte [Prompt flow u Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izaberite **Chat input**, **Chat output** kako biste omogućili razgovor sa vašim modelom.

    ![Ulaz i izlaz.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.sr.png)

1. Sada ste spremni da razgovarate sa svojim prilagođenim Phi-3 modelom. U sledećoj vežbi naučićete kako da pokrenete Prompt flow i koristite ga za razgovor sa fino podešenim Phi-3 modelom.

> [!NOTE]
>
> Rekonstruisani tok bi trebalo da izgleda kao na slici ispod:
>
> ![Primer toka.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.sr.png)
>

### Razgovarajte sa svojim prilagođenim Phi-3 modelom

Sada kada ste fino podesili i integrisali svoj prilagođeni Phi-3 model sa Prompt flow-om, spremni ste da počnete da komunicirate s njim. Ova vežba će vas voditi kroz proces postavljanja i pokretanja razgovora sa vašim modelom koristeći Prompt flow. Prateći ove korake, moći ćete u potpunosti da iskoristite mogućnosti svog fino podešenog Phi-3 modela za različite zadatke i razgovore.

- Razgovarajte sa svojim prilagođenim Phi-3 modelom koristeći Prompt flow.

#### Pokrenite Prompt flow

1. Izaberite **Start compute sessions** kako biste pokrenuli Prompt flow.

    ![Pokrenite compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.sr.png)

1. Izaberite **Validate and parse input** kako biste osvežili parametre.

    ![Validirajte unos.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.sr.png)

1. Izaberite **Value** za **connection** prema prilagođenoj konekciji koju ste kreirali. Na primer, *connection*.

    ![Konekcija.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.sr.png)

#### Razgovarajte sa svojim prilagođenim modelom

1. Izaberite **Chat**.

    ![Izaberite chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.sr.png)

1. Evo primera rezultata: Sada možete razgovarati sa svojim prilagođenim Phi-3 modelom. Preporučuje se da postavljate pitanja zasnovana na podacima korišćenim za fino podešavanje.

    ![Razgovor sa Prompt flow-om.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.sr.png)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из употребе овог превода.