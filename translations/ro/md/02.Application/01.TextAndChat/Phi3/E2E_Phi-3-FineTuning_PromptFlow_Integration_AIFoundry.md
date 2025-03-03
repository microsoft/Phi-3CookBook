# Ajuste fin și integrare a modelelor personalizate Phi-3 cu Prompt Flow în Azure AI Foundry

Acest exemplu complet (E2E) se bazează pe ghidul "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" din Microsoft Tech Community. Ghidul introduce procesele de ajustare fină, implementare și integrare a modelelor personalizate Phi-3 cu Prompt Flow în Azure AI Foundry.  
Spre deosebire de exemplul complet "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", care presupunea rularea codului local, acest tutorial se concentrează exclusiv pe ajustarea fină și integrarea modelului în cadrul Azure AI / ML Studio.

## Prezentare generală

În acest exemplu complet, vei învăța cum să ajustezi fin modelul Phi-3 și să îl integrezi cu Prompt Flow în Azure AI Foundry. Prin utilizarea Azure AI / ML Studio, vei stabili un flux de lucru pentru implementarea și utilizarea modelelor AI personalizate. Acest exemplu complet este împărțit în trei scenarii:

**Scenariul 1: Configurarea resurselor Azure și pregătirea pentru ajustare fină**  
**Scenariul 2: Ajustarea fină a modelului Phi-3 și implementarea în Azure Machine Learning Studio**  
**Scenariul 3: Integrarea cu Prompt Flow și interacțiunea cu modelul personalizat în Azure AI Foundry**

Iată o prezentare generală a acestui exemplu complet.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ro.png)

### Cuprins

1. **[Scenariul 1: Configurarea resurselor Azure și pregătirea pentru ajustare fină](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Crearea unui Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Solicitarea cotelor GPU în abonamentul Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Adăugarea unei asignări de rol](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Configurarea proiectului](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Pregătirea setului de date pentru ajustare fină](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariul 2: Ajustarea fină a modelului Phi-3 și implementarea în Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Ajustarea fină a modelului Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Implementarea modelului Phi-3 ajustat fin](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariul 3: Integrarea cu Prompt Flow și interacțiunea cu modelul personalizat în Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Integrarea modelului personalizat Phi-3 cu Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Interacțiunea cu modelul personalizat Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenariul 1: Configurarea resurselor Azure și pregătirea pentru ajustare fină

### Crearea unui Azure Machine Learning Workspace

1. Tastează *azure machine learning* în **bara de căutare** din partea de sus a paginii portalului și selectează **Azure Machine Learning** din opțiunile care apar.

    ![Tastează azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ro.png)

2. Selectează **+ Create** din meniul de navigare.

3. Selectează **New workspace** din meniul de navigare.

    ![Selectează new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ro.png)

4. Realizează următoarele acțiuni:

    - Selectează **Abonamentul Azure**.
    - Selectează **Grupul de resurse** pe care dorești să îl utilizezi (creează unul nou, dacă este necesar).
    - Introdu **Numele Workspace-ului**. Trebuie să fie un nume unic.
    - Selectează **Regiunea** pe care dorești să o utilizezi.
    - Selectează **Contul de stocare** pe care dorești să îl utilizezi (creează unul nou, dacă este necesar).
    - Selectează **Key Vault** pe care dorești să îl utilizezi (creează unul nou, dacă este necesar).
    - Selectează **Application Insights** pe care dorești să îl utilizezi (creează unul nou, dacă este necesar).
    - Selectează **Container Registry** pe care dorești să îl utilizezi (creează unul nou, dacă este necesar).

    ![Completează detaliile pentru Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ro.png)

5. Selectează **Review + Create**.

6. Selectează **Create**.

### Solicitarea cotelor GPU în abonamentul Azure

În acest tutorial, vei învăța cum să ajustezi fin și să implementezi un model Phi-3 utilizând GPU-uri. Pentru ajustarea fină, vei utiliza GPU-ul *Standard_NC24ads_A100_v4*, care necesită o solicitare de cotă. Pentru implementare, vei utiliza GPU-ul *Standard_NC6s_v3*, care de asemenea necesită o solicitare de cotă.

> [!NOTE]
>
> Doar abonamentele de tip Pay-As-You-Go (tipul standard de abonament) sunt eligibile pentru alocarea GPU-urilor; abonamentele de tip beneficii nu sunt momentan suportate.
>

1. Vizitează [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Realizează următoarele acțiuni pentru a solicita cota pentru familia *Standard NCADSA100v4*:

    - Selectează **Quota** din bara laterală stângă.
    - Selectează **Familia de mașini virtuale** pe care dorești să o utilizezi. De exemplu, selectează **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, care include GPU-ul *Standard_NC24ads_A100_v4*.
    - Selectează **Request quota** din meniul de navigare.

        ![Solicită cota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ro.png)

    - În pagina de solicitare a cotei, introdu **Limita de nuclee noi** pe care dorești să o utilizezi. De exemplu, 24.
    - În pagina de solicitare a cotei, selectează **Submit** pentru a solicita cota GPU.

1. Realizează următoarele acțiuni pentru a solicita cota pentru familia *Standard NCSv3*:

    - Selectează **Quota** din bara laterală stângă.
    - Selectează **Familia de mașini virtuale** pe care dorești să o utilizezi. De exemplu, selectează **Standard NCSv3 Family Cluster Dedicated vCPUs**, care include GPU-ul *Standard_NC6s_v3*.
    - Selectează **Request quota** din meniul de navigare.
    - În pagina de solicitare a cotei, introdu **Limita de nuclee noi** pe care dorești să o utilizezi. De exemplu, 24.
    - În pagina de solicitare a cotei, selectează **Submit** pentru a solicita cota GPU.

### Adăugarea unei asignări de rol

Pentru a ajusta fin și implementa modelele tale, trebuie mai întâi să creezi o Identitate Gestionată Atribuită Utilizatorului (UAI) și să îi atribui permisiunile corespunzătoare. Această UAI va fi utilizată pentru autentificare în timpul implementării.

#### Crearea unei Identități Gestionate Atribuite Utilizatorului (UAI)

1. Tastează *managed identities* în **bara de căutare** din partea de sus a paginii portalului și selectează **Managed Identities** din opțiunile care apar.

    ![Tastează managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ro.png)

1. Selectează **+ Create**.

    ![Selectează create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ro.png)

1. Realizează următoarele acțiuni:

    - Selectează **Abonamentul Azure**.
    - Selectează **Grupul de resurse** pe care dorești să îl utilizezi (creează unul nou, dacă este necesar).
    - Selectează **Regiunea** pe care dorești să o utilizezi.
    - Introdu **Numele**. Trebuie să fie un nume unic.

    ![Completează detaliile pentru identitatea gestionată.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ro.png)

1. Selectează **Review + create**.

1. Selectează **+ Create**.

#### Adăugarea rolului Contributor la Identitatea Gestionată

1. Navighează la resursa Identitate Gestionată pe care ai creat-o.

1. Selectează **Azure role assignments** din bara laterală stângă.

1. Selectează **+Add role assignment** din meniul de navigare.

1. În pagina de adăugare a rolului, realizează următoarele acțiuni:
    - Selectează **Scope** ca **Resource group**.
    - Selectează **Abonamentul Azure**.
    - Selectează **Grupul de resurse** pe care dorești să îl utilizezi.
    - Selectează **Rolul** ca **Contributor**.

    ![Completează detaliile pentru rolul Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ro.png)

2. Selectează **Save**.

#### Adăugarea rolului Storage Blob Data Reader la Identitatea Gestionată

1. Tastează *storage accounts* în **bara de căutare** din partea de sus a paginii portalului și selectează **Storage accounts** din opțiunile care apar.

    ![Tastează storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ro.png)

1. Selectează contul de stocare asociat cu workspace-ul Azure Machine Learning pe care l-ai creat. De exemplu, *finetunephistorage*.

1. Realizează următoarele acțiuni pentru a naviga la pagina de adăugare a rolului:

    - Navighează la contul Azure Storage pe care l-ai creat.
    - Selectează **Access Control (IAM)** din bara laterală stângă.
    - Selectează **+ Add** din meniul de navigare.
    - Selectează **Add role assignment** din meniul de navigare.

    ![Adaugă rol.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ro.png)

1. În pagina de adăugare a rolului, realizează următoarele acțiuni:

    - În pagina Rol, tastează *Storage Blob Data Reader* în **bara de căutare** și selectează **Storage Blob Data Reader** din opțiunile care apar.
    - În pagina Rol, selectează **Next**.
    - În pagina Members, selectează **Assign access to** **Managed identity**.
    - În pagina Members, selectează **+ Select members**.
    - În pagina Select managed identities, selectează **Abonamentul Azure**.
    - În pagina Select managed identities, selectează **Identitatea Gestionată**.
    - În pagina Select managed identities, selectează Identitatea Gestionată pe care ai creat-o. De exemplu, *finetunephi-managedidentity*.
    - În pagina Select managed identities, selectează **Select**.

    ![Selectează identitatea gestionată.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ro.png)

1. Selectează **Review + assign**.

#### Adăugarea rolului AcrPull la Identitatea Gestionată

1. Tastează *container registries* în **bara de căutare** din partea de sus a paginii portalului și selectează **Container registries** din opțiunile care apar.

    ![Tastează container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ro.png)

1. Selectează registrul de containere asociat cu workspace-ul Azure Machine Learning. De exemplu, *finetunephicontainerregistry*.

1. Realizează următoarele acțiuni pentru a naviga la pagina de adăugare a rolului:

    - Selectează **Access Control (IAM)** din bara laterală stângă.
    - Selectează **+ Add** din meniul de navigare.
    - Selectează **Add role assignment** din meniul de navigare.

1. În pagina de adăugare a rolului, realizează următoarele acțiuni:

    - În pagina Rol, tastează *AcrPull* în **bara de căutare** și selectează **AcrPull** din opțiunile care apar.
    - În pagina Rol, selectează **Next**.
    - În pagina Members, selectează **Assign access to** **Managed identity**.
    - În pagina Members, selectează **+ Select members**.
    - În pagina Select managed identities, selectează **Abonamentul Azure**.
    - În pagina Select managed identities, selectează **Identitatea Gestionată**.
    - În pagina Select managed identities, selectează Identitatea Gestionată pe care ai creat-o. De exemplu, *finetunephi-managedidentity*.
    - În pagina Select managed identities, selectează **Select**.
    - Selectează **Review + assign**.

### Configurarea proiectului

Pentru a descărca seturile de date necesare pentru ajustare fină, vei configura un mediu local.

În acest exercițiu, vei:

- Crea un folder pentru a lucra în el.
- Crea un mediu virtual.
- Instala pachetele necesare.
- Crea un fișier *download_dataset.py* pentru a descărca setul de date.

#### Crearea unui folder pentru a lucra în el

1. Deschide o fereastră de terminal și tastează următoarea comandă pentru a crea un folder numit *finetune-phi* în calea implicită.

    ```console
    mkdir finetune-phi
    ```

2. Tastează următoarea comandă în terminal pentru a naviga la folderul *finetune-phi* pe care l-ai creat.

    ```console
    cd finetune-phi
    ```

#### Crearea unui mediu virtual

1. Tastează următoarea comandă în terminal pentru a crea un mediu virtual numit *.venv*.

    ```console
    python -m venv .venv
    ```

2. Tastează următoarea comandă în terminal pentru a activa mediul virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> Dacă a funcționat, ar trebui să vezi *(.venv)* înainte de promptul terminalului.

#### Instalarea pachetelor necesare

1. Tastează următoarele comenzi în terminal pentru a instala pachetele necesare.

    ```console
    pip install datasets==2.19.1
    ```

#### Crearea fișierului `download_dataset.py`

> [!NOTE]  
> Structura completă a folderului:  
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Deschide **Visual Studio Code**.

1. Selectează **File** din bara de meniu.

1. Selectează **Open Folder**.

1. Selectează folderul *finetune-phi* pe care l-ai creat, situat la *C:\Users\yourUserName\finetune-phi*.

    ![Selectează folderul creat.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.ro.png)

1. În panoul din stânga al Visual Studio Code, fă clic dreapta și selectează **New File** pentru a crea un fișier nou numit *download_dataset.py*.

    ![Creează un fișier nou.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.ro.png)

### Pregătirea setului de date pentru ajustare fină

În acest exercițiu, vei rula fișierul *download_dataset.py* pentru a descărca seturile de date *ultrachat_200k* în mediul tău local. Vei utiliza apoi aceste seturi de date pentru a ajusta fin modelul Phi-3 în Azure Machine Learning.

În acest exercițiu, vei:

- Adăuga cod în fișierul *download_dataset.py* pentru a descărca seturile de date.
- Rula fișierul *download_dataset.py* pentru a descărca seturile de date în mediul tău local.

#### Descărcarea setului de date folosind *download_dataset.py*

1. Deschide fișierul *
1. Accesați [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectați **Compute** din bara laterală stângă.

1. Selectați **Compute clusters** din meniul de navigare.

1. Selectați **+ New**.

    ![Selectați compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ro.png)

1. Efectuați următoarele acțiuni:

    - Selectați **Region** pe care doriți să o utilizați.
    - Selectați **Virtual machine tier** la **Dedicated**.
    - Selectați **Virtual machine type** la **GPU**.
    - Filtrați **Virtual machine size** la **Select from all options**.
    - Selectați **Virtual machine size** la **Standard_NC24ads_A100_v4**.

    ![Creați cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ro.png)

1. Selectați **Next**.

1. Efectuați următoarele acțiuni:

    - Introduceți **Compute name**. Acesta trebuie să fie unic.
    - Setați **Minimum number of nodes** la **0**.
    - Setați **Maximum number of nodes** la **1**.
    - Setați **Idle seconds before scale down** la **120**.

    ![Creați cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ro.png)

1. Selectați **Create**.

#### Ajustarea modelului Phi-3

1. Accesați [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectați spațiul de lucru Azure Machine Learning pe care l-ați creat.

    ![Selectați spațiul de lucru creat.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ro.png)

1. Efectuați următoarele acțiuni:

    - Selectați **Model catalog** din bara laterală stângă.
    - Introduceți *phi-3-mini-4k* în **bara de căutare** și selectați **Phi-3-mini-4k-instruct** din opțiunile afișate.

    ![Introduceți phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ro.png)

1. Selectați **Fine-tune** din meniul de navigare.

    ![Selectați fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ro.png)

1. Efectuați următoarele acțiuni:

    - Setați **Select task type** la **Chat completion**.
    - Selectați **+ Select data** pentru a încărca **Traning data**.
    - Setați tipul de încărcare pentru Validation data la **Provide different validation data**.
    - Selectați **+ Select data** pentru a încărca **Validation data**.

    ![Completați pagina de fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ro.png)

    > [!TIP]
    >
    > Puteți selecta **Advanced settings** pentru a personaliza configurările, precum **learning_rate** și **lr_scheduler_type**, pentru a optimiza procesul de ajustare în funcție de nevoile dvs.

1. Selectați **Finish**.

1. În acest exercițiu, ați ajustat cu succes modelul Phi-3 utilizând Azure Machine Learning. Rețineți că procesul de ajustare poate dura mult timp. După lansarea job-ului de ajustare, va trebui să așteptați finalizarea acestuia. Puteți monitoriza starea job-ului navigând la fila Jobs din bara laterală a spațiului dvs. de lucru Azure Machine Learning. În seria următoare, veți implementa modelul ajustat și îl veți integra cu Prompt flow.

    ![Vizualizați job-ul de fine-tuning.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ro.png)

### Implementarea modelului Phi-3 ajustat

Pentru a integra modelul ajustat Phi-3 cu Prompt flow, trebuie să implementați modelul pentru a-l face accesibil pentru inferență în timp real. Acest proces implică înregistrarea modelului, crearea unui endpoint online și implementarea modelului.

În acest exercițiu, veți:

- Înregistra modelul ajustat în spațiul de lucru Azure Machine Learning.
- Crea un endpoint online.
- Implementa modelul Phi-3 ajustat.

#### Înregistrarea modelului ajustat

1. Accesați [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selectați spațiul de lucru Azure Machine Learning pe care l-ați creat.

    ![Selectați spațiul de lucru creat.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ro.png)

1. Selectați **Models** din bara laterală stângă.
1. Selectați **+ Register**.
1. Selectați **From a job output**.

    ![Înregistrați modelul.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ro.png)

1. Selectați job-ul pe care l-ați creat.

    ![Selectați job-ul.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ro.png)

1. Selectați **Next**.

1. Setați **Model type** la **MLflow**.

1. Asigurați-vă că **Job output** este selectat; ar trebui să fie selectat automat.

    ![Selectați output-ul.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ro.png)

2. Selectați **Next**.

3. Selectați **Register**.

    ![Selectați register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ro.png)

4. Puteți vizualiza modelul înregistrat navigând la meniul **Models** din bara laterală.

    ![Model înregistrat.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ro.png)

#### Implementarea modelului ajustat

1. Navigați la spațiul de lucru Azure Machine Learning pe care l-ați creat.

1. Selectați **Endpoints** din bara laterală stângă.

1. Selectați **Real-time endpoints** din meniul de navigare.

    ![Creați endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ro.png)

1. Selectați **Create**.

1. Selectați modelul înregistrat pe care l-ați creat.

    ![Selectați modelul înregistrat.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ro.png)

1. Selectați **Select**.

1. Efectuați următoarele acțiuni:

    - Setați **Virtual machine** la *Standard_NC6s_v3*.
    - Setați **Instance count** pe care doriți să îl utilizați. De exemplu, *1*.
    - Setați **Endpoint** la **New** pentru a crea un endpoint.
    - Introduceți **Endpoint name**. Acesta trebuie să fie unic.
    - Introduceți **Deployment name**. Acesta trebuie să fie unic.

    ![Completați setările de implementare.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ro.png)

1. Selectați **Deploy**.

> [!WARNING]
> Pentru a evita costuri suplimentare în contul dvs., asigurați-vă că ștergeți endpoint-ul creat în spațiul de lucru Azure Machine Learning.
>

#### Verificați starea implementării în Azure Machine Learning Workspace

1. Navigați la spațiul de lucru Azure Machine Learning pe care l-ați creat.

1. Selectați **Endpoints** din bara laterală stângă.

1. Selectați endpoint-ul pe care l-ați creat.

    ![Selectați endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ro.png)

1. Pe această pagină, puteți gestiona endpoint-urile pe durata procesului de implementare.

> [!NOTE]
> Odată ce implementarea este completă, asigurați-vă că **Live traffic** este setat la **100%**. Dacă nu este, selectați **Update traffic** pentru a ajusta setările de trafic. Rețineți că nu puteți testa modelul dacă traficul este setat la 0%.
>
> ![Setați traficul.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ro.png)
>

## Scenariul 3: Integrarea cu Prompt flow și interacțiunea cu modelul personalizat în Azure AI Foundry

### Integrarea modelului personalizat Phi-3 cu Prompt flow

După implementarea cu succes a modelului ajustat, acum îl puteți integra cu Prompt Flow pentru a-l utiliza în aplicații în timp real, permițând diverse sarcini interactive cu modelul dvs. personalizat Phi-3.

În acest exercițiu, veți:

- Crea un Hub Azure AI Foundry.
- Crea un Proiect Azure AI Foundry.
- Configura Prompt flow.
- Adăuga o conexiune personalizată pentru modelul ajustat Phi-3.
- Configura Prompt flow pentru a interacționa cu modelul dvs. personalizat Phi-3.

> [!NOTE]
> Puteți integra și cu Promptflow utilizând Azure ML Studio. Procesul de integrare este același și în Azure ML Studio.

#### Crearea unui Hub Azure AI Foundry

Trebuie să creați un Hub înainte de a crea un Proiect. Un Hub funcționează ca un Grup de Resurse, permițându-vă să organizați și să gestionați mai multe Proiecte în cadrul Azure AI Foundry.

1. Accesați [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selectați **All hubs** din bara laterală stângă.

1. Selectați **+ New hub** din meniul de navigare.

    ![Creați hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ro.png)

1. Efectuați următoarele acțiuni:

    - Introduceți **Hub name**. Acesta trebuie să fie unic.
    - Selectați **Subscription** Azure.
    - Alegeți **Resource group** pe care doriți să îl utilizați (creați unul nou dacă este necesar).
    - Selectați **Location** pe care doriți să o utilizați.
    - Conectați **Azure AI Services** (creați unul nou dacă este necesar).
    - Setați **Connect Azure AI Search** la **Skip connecting**.

    ![Completați hub-ul.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ro.png)

1. Selectați **Next**.

#### Crearea unui Proiect Azure AI Foundry

1. În Hub-ul pe care l-ați creat, selectați **All projects** din bara laterală stângă.

1. Selectați **+ New project** din meniul de navigare.

    ![Selectați proiect nou.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ro.png)

1. Introduceți **Project name**. Acesta trebuie să fie unic.

    ![Creați proiect.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ro.png)

1. Selectați **Create a project**.

#### Adăugarea unei conexiuni personalizate pentru modelul ajustat Phi-3

Pentru a integra modelul personalizat Phi-3 cu Prompt flow, trebuie să salvați endpoint-ul și cheia modelului într-o conexiune personalizată. Această configurare asigură accesul la modelul dvs. personalizat Phi-3 în Prompt flow.

#### Setarea cheii API și a URI-ului endpoint-ului pentru modelul ajustat Phi-3

1. Accesați [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigați la spațiul de lucru Azure Machine Learning pe care l-ați creat.

1. Selectați **Endpoints** din bara laterală stângă.

    ![Selectați endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ro.png)

1. Selectați endpoint-ul pe care l-ați creat.

    ![Selectați endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ro.png)

1. Selectați **Consume** din meniul de navigare.

1. Copiați **REST endpoint** și **Primary key**.
![Copiați cheia API și URI-ul endpoint-ului.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ro.png)

#### Adăugați Conexiunea Personalizată

1. Vizitați [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigați la proiectul Azure AI Foundry pe care l-ați creat.

1. În proiectul creat, selectați **Settings** din meniul din stânga.

1. Selectați **+ New connection**.

    ![Selectați noua conexiune.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ro.png)

1. Selectați **Custom keys** din meniul de navigare.

    ![Selectați chei personalizate.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ro.png)

1. Realizați următoarele acțiuni:

    - Selectați **+ Add key value pairs**.
    - Pentru numele cheii, introduceți **endpoint** și lipiți endpoint-ul copiat din Azure ML Studio în câmpul valorii.
    - Selectați din nou **+ Add key value pairs**.
    - Pentru numele cheii, introduceți **key** și lipiți cheia copiată din Azure ML Studio în câmpul valorii.
    - După adăugarea cheilor, selectați **is secret** pentru a preveni expunerea cheii.

    ![Adăugați conexiunea.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ro.png)

1. Selectați **Add connection**.

#### Creați Prompt flow

Ați adăugat o conexiune personalizată în Azure AI Foundry. Acum, să creăm un Prompt flow folosind pașii următori. Ulterior, veți conecta acest Prompt flow la conexiunea personalizată pentru a putea utiliza modelul ajustat în Prompt flow.

1. Navigați la proiectul Azure AI Foundry pe care l-ați creat.

1. Selectați **Prompt flow** din meniul din stânga.

1. Selectați **+ Create** din meniul de navigare.

    ![Selectați Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ro.png)

1. Selectați **Chat flow** din meniul de navigare.

    ![Selectați chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ro.png)

1. Introduceți **Folder name** pentru utilizare.

    ![Introduceți numele.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ro.png)

2. Selectați **Create**.

#### Configurați Prompt flow pentru a comunica cu modelul personalizat Phi-3

Trebuie să integrați modelul ajustat Phi-3 într-un Prompt flow. Totuși, Prompt flow-ul existent nu este conceput pentru acest scop. Prin urmare, trebuie să reconstruiți Prompt flow-ul pentru a permite integrarea modelului personalizat.

1. În Prompt flow, realizați următoarele acțiuni pentru a reconstrui fluxul existent:

    - Selectați **Raw file mode**.
    - Ștergeți tot codul existent din fișierul *flow.dag.yml*.
    - Adăugați următorul cod în fișierul *flow.dag.yml*.

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

    - Selectați **Save**.

    ![Selectați modul fișier brut.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ro.png)

1. Adăugați următorul cod în fișierul *integrate_with_promptflow.py* pentru a utiliza modelul personalizat Phi-3 în Prompt flow.

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

    ![Lipiți codul prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ro.png)

> [!NOTE]
> Pentru informații mai detaliate despre utilizarea Prompt flow în Azure AI Foundry, consultați [Prompt flow în Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selectați **Chat input**, **Chat output** pentru a activa chat-ul cu modelul dvs.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ro.png)

1. Acum sunteți pregătit să comunicați cu modelul dvs. personalizat Phi-3. În următorul exercițiu, veți învăța cum să porniți Prompt flow și să îl utilizați pentru a comunica cu modelul ajustat Phi-3.

> [!NOTE]
>
> Fluxul reconstruit ar trebui să arate astfel:
>
> ![Exemplu flux.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ro.png)
>

### Comunicați cu modelul dvs. personalizat Phi-3

Acum că ați ajustat și integrat modelul dvs. personalizat Phi-3 cu Prompt flow, sunteți gata să începeți să interacționați cu el. Acest exercițiu vă va ghida prin procesul de configurare și inițiere a unei sesiuni de chat cu modelul dvs. Urmând acești pași, veți putea utiliza pe deplin capabilitățile modelului dvs. ajustat Phi-3 pentru diverse sarcini și conversații.

- Comunicați cu modelul dvs. personalizat Phi-3 folosind Prompt flow.

#### Porniți Prompt flow

1. Selectați **Start compute sessions** pentru a porni Prompt flow.

    ![Porniți sesiunea de calcul.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ro.png)

1. Selectați **Validate and parse input** pentru a reînnoi parametrii.

    ![Validați input-ul.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ro.png)

1. Selectați **Value** al **connection** pentru conexiunea personalizată pe care ați creat-o. De exemplu, *connection*.

    ![Conexiune.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ro.png)

#### Comunicați cu modelul dvs. personalizat

1. Selectați **Chat**.

    ![Selectați chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ro.png)

1. Iată un exemplu de rezultate: Acum puteți comunica cu modelul dvs. personalizat Phi-3. Este recomandat să puneți întrebări bazate pe datele utilizate pentru ajustare.

    ![Chat cu prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ro.png)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa de autoritate. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.