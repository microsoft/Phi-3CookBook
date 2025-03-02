# Fino podešavanje i integracija prilagođenih Phi-3 modela s Prompt flow u Azure AI Foundry

Ovaj uzorak "od početka do kraja" (E2E) temelji se na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community. Prikazuje procese fino podešavanja, implementacije i integracije prilagođenih Phi-3 modela s Prompt flow u Azure AI Foundry.  
Za razliku od uzorka "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", koji uključuje lokalno pokretanje koda, ovaj vodič se u potpunosti fokusira na fino podešavanje i integraciju modela unutar Azure AI / ML Studija.

## Pregled

U ovom E2E uzorku naučit ćete kako fino podesiti Phi-3 model i integrirati ga s Prompt flow u Azure AI Foundry. Korištenjem Azure AI / ML Studija, uspostavit ćete tijek rada za implementaciju i korištenje prilagođenih AI modela. Ovaj uzorak podijeljen je u tri scenarija:

**Scenarij 1: Postavljanje Azure resursa i priprema za fino podešavanje**  
**Scenarij 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio**  
**Scenarij 3: Integracija s Prompt flow i razgovor s prilagođenim modelom u Azure AI Foundry**

Evo pregleda ovog E2E uzorka.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.hr.png)

### Sadržaj

1. **[Scenarij 1: Postavljanje Azure resursa i priprema za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Kreiranje Azure Machine Learning radnog prostora](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Zahtjev za GPU kvotama u Azure pretplati](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Dodavanje uloga](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Postavljanje projekta](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Priprema skupa podataka za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)

2. **[Scenarij 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Fino podešavanje Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Implementacija fino podešenog Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)

3. **[Scenarij 3: Integracija s Prompt flow i razgovor s vašim prilagođenim modelom u Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Integracija prilagođenog Phi-3 modela s Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Razgovor s vašim prilagođenim Phi-3 modelom](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenarij 1: Postavljanje Azure resursa i priprema za fino podešavanje

### Kreiranje Azure Machine Learning radnog prostora

1. U gornjoj **tražilici** na portalu upišite *azure machine learning* i odaberite **Azure Machine Learning** iz ponuđenih opcija.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.hr.png)

2. Kliknite na **+ Create** u navigacijskom izborniku.

3. Izaberite **New workspace** u navigacijskom izborniku.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.hr.png)

4. Izvršite sljedeće zadatke:

    - Odaberite svoju Azure **pretplatu**.  
    - Odaberite **grupu resursa** koju ćete koristiti (kreirajte novu ako je potrebno).  
    - Unesite **Naziv radnog prostora**. Vrijednost mora biti jedinstvena.  
    - Odaberite **Regiju** koju želite koristiti.  
    - Odaberite **Storage account** (kreirajte novi ako je potrebno).  
    - Odaberite **Key vault** (kreirajte novi ako je potrebno).  
    - Odaberite **Application insights** (kreirajte novi ako je potrebno).  
    - Odaberite **Container registry** (kreirajte novi ako je potrebno).  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.hr.png)

5. Kliknite na **Review + Create**.

6. Kliknite na **Create**.

### Zahtjev za GPU kvotama u Azure pretplati

U ovom vodiču naučit ćete kako fino podesiti i implementirati Phi-3 model koristeći GPU-ove. Za fino podešavanje koristit ćete *Standard_NC24ads_A100_v4* GPU, koji zahtijeva zahtjev za kvotom. Za implementaciju koristit ćete *Standard_NC6s_v3* GPU, koji također zahtijeva zahtjev za kvotom.

> [!NOTE]  
> Samo pretplate s modelom Pay-As-You-Go (standardni tip pretplate) imaju pravo na GPU dodjelu; pretplate s benefitima trenutno nisu podržane.

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izvršite sljedeće korake za zahtjev kvote za *Standard NCADSA100v4 Family*:

    - Odaberite **Quota** s lijeve strane.  
    - Odaberite **Virtual machine family** koju želite koristiti. Na primjer, odaberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, koji uključuje *Standard_NC24ads_A100_v4* GPU.  
    - Kliknite na **Request quota** u navigacijskom izborniku.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.hr.png)

    - Na stranici Zahtjev kvote unesite **Novi limit jezgri** koji želite koristiti. Na primjer, 24.  
    - Kliknite na **Submit** za podnošenje zahtjeva za GPU kvotu.

1. Izvršite sljedeće korake za zahtjev kvote za *Standard NCSv3 Family*:

    - Odaberite **Quota** s lijeve strane.  
    - Odaberite **Virtual machine family** koju želite koristiti. Na primjer, odaberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, koji uključuje *Standard_NC6s_v3* GPU.  
    - Kliknite na **Request quota** u navigacijskom izborniku.  
    - Na stranici Zahtjev kvote unesite **Novi limit jezgri** koji želite koristiti. Na primjer, 24.  
    - Kliknite na **Submit** za podnošenje zahtjeva za GPU kvotu.

### Dodavanje uloga

Kako biste fino podesili i implementirali svoje modele, prvo morate kreirati User Assigned Managed Identity (UAI) i dodijeliti mu odgovarajuće dozvole. Ovaj UAI će se koristiti za autentifikaciju tijekom implementacije.

#### Kreiranje User Assigned Managed Identity (UAI)

1. U gornjoj **tražilici** na portalu upišite *managed identities* i odaberite **Managed Identities** iz ponuđenih opcija.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.hr.png)

1. Kliknite na **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.hr.png)

1. Izvršite sljedeće zadatke:

    - Odaberite svoju Azure **pretplatu**.  
    - Odaberite **grupu resursa** koju ćete koristiti (kreirajte novu ako je potrebno).  
    - Odaberite **Regiju** koju želite koristiti.  
    - Unesite **Naziv**. Vrijednost mora biti jedinstvena.  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.hr.png)

1. Kliknite na **Review + create**.

1. Kliknite na **+ Create**.

#### Dodavanje Contributor uloge Managed Identity

1. Navigirajte do resursa Managed Identity koji ste kreirali.  

1. Odaberite **Azure role assignments** s lijeve strane.  

1. Kliknite na **+Add role assignment** u navigacijskom izborniku.  

1. Na stranici Dodavanje uloge izvršite sljedeće zadatke:  
    - Odaberite **Opseg** kao **Resource group**.  
    - Odaberite svoju Azure **pretplatu**.  
    - Odaberite **grupu resursa** koju želite koristiti.  
    - Odaberite **Ulogu** kao **Contributor**.  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.hr.png)

2. Kliknite na **Save**.

...
1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite **Compute** s lijeve trake.

1. Odaberite **Compute clusters** iz navigacijskog izbornika.

1. Odaberite **+ New**.

    ![Odaberite compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.hr.png)

1. Izvršite sljedeće zadatke:

    - Odaberite **Region** koji želite koristiti.
    - Postavite **Virtual machine tier** na **Dedicated**.
    - Postavite **Virtual machine type** na **GPU**.
    - Postavite filtar **Virtual machine size** na **Select from all options**.
    - Odaberite **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Kreirajte cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.hr.png)

1. Odaberite **Next**.

1. Izvršite sljedeće zadatke:

    - Unesite **Compute name**. Vrijednost mora biti jedinstvena.
    - Postavite **Minimum number of nodes** na **0**.
    - Postavite **Maximum number of nodes** na **1**.
    - Postavite **Idle seconds before scale down** na **120**.

    ![Kreirajte cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.hr.png)

1. Odaberite **Create**.

#### Fino podešavanje Phi-3 modela

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite Azure Machine Learning radni prostor koji ste kreirali.

    ![Odaberite radni prostor koji ste kreirali.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hr.png)

1. Izvršite sljedeće zadatke:

    - Odaberite **Model catalog** s lijeve trake.
    - Upišite *phi-3-mini-4k* u **search bar** i odaberite **Phi-3-mini-4k-instruct** iz ponuđenih opcija.

    ![Upišite phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.hr.png)

1. Odaberite **Fine-tune** iz navigacijskog izbornika.

    ![Odaberite fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.hr.png)

1. Izvršite sljedeće zadatke:

    - Postavite **Select task type** na **Chat completion**.
    - Odaberite **+ Select data** za učitavanje **Training data**.
    - Postavite vrstu učitavanja Validation data na **Provide different validation data**.
    - Odaberite **+ Select data** za učitavanje **Validation data**.

    ![Ispunite stranicu za fino podešavanje.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.hr.png)

    > [!TIP]
    >
    > Možete odabrati **Advanced settings** za prilagodbu konfiguracija poput **learning_rate** i **lr_scheduler_type** kako biste optimizirali proces finog podešavanja prema vašim specifičnim potrebama.

1. Odaberite **Finish**.

1. U ovoj vježbi uspješno ste fino podesili Phi-3 model koristeći Azure Machine Learning. Imajte na umu da proces finog podešavanja može potrajati. Nakon pokretanja zadatka finog podešavanja, trebate pričekati dok se ne završi. Status zadatka možete pratiti odlaskom na karticu Jobs s lijeve strane u vašem Azure Machine Learning radnom prostoru. U sljedećem dijelu, implementirat ćete fino podešeni model i integrirati ga s Prompt flowom.

    ![Pogledajte zadatak finog podešavanja.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.hr.png)

### Implementacija fino podešenog Phi-3 modela

Kako biste integrirali fino podešeni Phi-3 model s Prompt flowom, trebate ga implementirati kako bi bio dostupan za stvarnu inferenciju. Ovaj proces uključuje registraciju modela, kreiranje online endpointa i implementaciju modela.

U ovoj vježbi ćete:

- Registrirati fino podešeni model u Azure Machine Learning radnom prostoru.
- Kreirati online endpoint.
- Implementirati registrirani fino podešeni Phi-3 model.

#### Registracija fino podešenog modela

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite Azure Machine Learning radni prostor koji ste kreirali.

    ![Odaberite radni prostor koji ste kreirali.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hr.png)

1. Odaberite **Models** s lijeve trake.
1. Odaberite **+ Register**.
1. Odaberite **From a job output**.

    ![Registrirajte model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.hr.png)

1. Odaberite zadatak koji ste kreirali.

    ![Odaberite zadatak.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.hr.png)

1. Odaberite **Next**.

1. Postavite **Model type** na **MLflow**.

1. Provjerite je li **Job output** odabran; trebao bi biti automatski odabran.

    ![Odaberite izlaz.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.hr.png)

2. Odaberite **Next**.

3. Odaberite **Register**.

    ![Odaberite register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.hr.png)

4. Svoj registrirani model možete vidjeti odlaskom na izbornik **Models** s lijeve strane.

    ![Registrirani model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.hr.png)

#### Implementacija fino podešenog modela

1. Idite u Azure Machine Learning radni prostor koji ste kreirali.

1. Odaberite **Endpoints** s lijeve trake.

1. Odaberite **Real-time endpoints** iz navigacijskog izbornika.

    ![Kreirajte endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.hr.png)

1. Odaberite **Create**.

1. Odaberite registrirani model koji ste kreirali.

    ![Odaberite registrirani model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.hr.png)

1. Odaberite **Select**.

1. Izvršite sljedeće zadatke:

    - Postavite **Virtual machine** na *Standard_NC6s_v3*.
    - Odaberite broj **Instance count** koji želite koristiti, primjerice *1*.
    - Postavite **Endpoint** na **New** za kreiranje endpointa.
    - Unesite **Endpoint name**. Vrijednost mora biti jedinstvena.
    - Unesite **Deployment name**. Vrijednost mora biti jedinstvena.

    ![Ispunite postavke implementacije.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.hr.png)

1. Odaberite **Deploy**.

> [!WARNING]
> Kako biste izbjegli dodatne troškove na vašem računu, obavezno izbrišite kreirani endpoint u Azure Machine Learning radnom prostoru.
>

#### Provjera statusa implementacije u Azure Machine Learning radnom prostoru

1. Idite u Azure Machine Learning radni prostor koji ste kreirali.

1. Odaberite **Endpoints** s lijeve trake.

1. Odaberite endpoint koji ste kreirali.

    ![Odaberite endpoint.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.hr.png)

1. Na ovoj stranici možete upravljati endpointima tijekom procesa implementacije.

> [!NOTE]
> Nakon što je implementacija dovršena, provjerite je li **Live traffic** postavljen na **100%**. Ako nije, odaberite **Update traffic** kako biste prilagodili postavke prometa. Imajte na umu da ne možete testirati model ako je promet postavljen na 0%.
>
> ![Postavite promet.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.hr.png)
>
![Kopiraj API ključ i URI krajnje točke.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.hr.png)

#### Dodavanje prilagožene veze

1. Posjetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Otvorite projekt Azure AI Foundry koji ste kreirali.

1. U projektu koji ste kreirali odaberite **Postavke** na lijevoj bočnoj traci.

1. Odaberite **+ Nova veza**.

    ![Odaberite novu vezu.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.hr.png)

1. Iz izbornika odaberite **Prilagođeni ključevi**.

    ![Odaberite prilagođene ključeve.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.hr.png)

1. Izvršite sljedeće zadatke:

    - Odaberite **+ Dodaj parove ključ-vrijednost**.
    - Za naziv ključa unesite **endpoint** i zalijepite krajnju točku koju ste kopirali iz Azure ML Studija u polje za vrijednost.
    - Ponovno odaberite **+ Dodaj parove ključ-vrijednost**.
    - Za naziv ključa unesite **key** i zalijepite ključ koji ste kopirali iz Azure ML Studija u polje za vrijednost.
    - Nakon dodavanja ključeva, označite **je tajno** kako biste spriječili izlaganje ključa.

    ![Dodajte vezu.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.hr.png)

1. Odaberite **Dodaj vezu**.

#### Kreiranje Prompt flowa

Dodali ste prilagoženu vezu u Azure AI Foundry. Sada ćemo kreirati Prompt flow koristeći sljedeće korake. Zatim ćete povezati ovaj Prompt flow s prilagođenom vezom kako biste mogli koristiti fino podešeni model unutar Prompt flowa.

1. Otvorite projekt Azure AI Foundry koji ste kreirali.

1. Odaberite **Prompt flow** na lijevoj bočnoj traci.

1. Odaberite **+ Kreiraj** iz navigacijskog izbornika.

    ![Odaberite Prompt flow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.hr.png)

1. Iz izbornika odaberite **Chat flow**.

    ![Odaberite chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.hr.png)

1. Unesite **Naziv mape** koju želite koristiti.

    ![Unesite naziv.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.hr.png)

2. Odaberite **Kreiraj**.

#### Postavljanje Prompt flowa za razgovor s prilagođenim Phi-3 modelom

Potrebno je integrirati fino podešeni Phi-3 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za ovu svrhu. Stoga morate redizajnirati Prompt flow kako biste omogućili integraciju prilagođenog modela.

1. U Prompt flowu izvršite sljedeće zadatke za ponovno kreiranje postojećeg toka:

    - Odaberite **Način rada s izvornom datotekom**.
    - Obrišite sav postojeći kod u datoteci *flow.dag.yml*.
    - Dodajte sljedeći kod u datoteku *flow.dag.yml*.

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

    - Odaberite **Spremi**.

    ![Odaberite način rada s izvornom datotekom.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.hr.png)

1. Dodajte sljedeći kod u datoteku *integrate_with_promptflow.py* kako biste koristili prilagođeni Phi-3 model u Prompt flowu.

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

    ![Zalijepite kod za Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.hr.png)

> [!NOTE]
> Za detaljnije informacije o korištenju Prompt flowa u Azure AI Foundry, pogledajte [Prompt flow u Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Odaberite **Unos za chat**, **Izlaz za chat** kako biste omogućili razgovor s vašim modelom.

    ![Unos i izlaz.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.hr.png)

1. Sada ste spremni za razgovor s vašim prilagođenim Phi-3 modelom. U sljedećoj vježbi naučit ćete kako pokrenuti Prompt flow i koristiti ga za razgovor s vašim fino podešenim Phi-3 modelom.

> [!NOTE]
>
> Redizajnirani tok trebao bi izgledati kao na slici ispod:
>
> ![Primjer toka.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.hr.png)
>

### Razgovor s vašim prilagođenim Phi-3 modelom

Sada kada ste fino podesili i integrirali vaš prilagođeni Phi-3 model s Prompt flowom, spremni ste za početak interakcije s njim. Ova vježba vodi vas kroz proces postavljanja i pokretanja razgovora s vašim modelom koristeći Prompt flow. Slijedeći ove korake, moći ćete u potpunosti iskoristiti mogućnosti vašeg fino podešenog Phi-3 modela za razne zadatke i razgovore.

- Razgovarajte s vašim prilagođenim Phi-3 modelom koristeći Prompt flow.

#### Pokretanje Prompt flowa

1. Odaberite **Pokreni sesije računalne obrade** za pokretanje Prompt flowa.

    ![Pokrenite sesiju računalne obrade.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.hr.png)

1. Odaberite **Potvrdi i parsiraj unos** za ažuriranje parametara.

    ![Potvrdite unos.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.hr.png)

1. Odaberite **Vrijednost** prilagođene veze koju ste kreirali. Na primjer, *connection*.

    ![Veza.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.hr.png)

#### Razgovor s vašim prilagođenim modelom

1. Odaberite **Chat**.

    ![Odaberite chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.hr.png)

1. Evo primjera rezultata: Sada možete razgovarati s vašim prilagođenim Phi-3 modelom. Preporučuje se postavljati pitanja temeljena na podacima korištenim za fino podešavanje.

    ![Razgovor s Prompt flowom.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću usluga strojno baziranog AI prevođenja. Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.