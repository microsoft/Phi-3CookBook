# Dostosowanie i integracja niestandardowych modeli Phi-3 z Prompt flow w Azure AI Foundry

Ten kompleksowy przykład (E2E) oparty jest na przewodniku "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" opublikowanym w Microsoft Tech Community. Przedstawia procesy dostosowywania, wdrażania i integracji niestandardowych modeli Phi-3 z Prompt flow w Azure AI Foundry.  
W przeciwieństwie do przykładu E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", który wymagał uruchamiania kodu lokalnie, ten samouczek koncentruje się całkowicie na dostosowywaniu i integracji modelu w Azure AI / ML Studio.

## Przegląd

W tym kompleksowym przykładzie dowiesz się, jak dostosować model Phi-3 i zintegrować go z Prompt flow w Azure AI Foundry. Wykorzystując Azure AI / ML Studio, stworzysz przepływ pracy do wdrażania i korzystania z niestandardowych modeli AI. Ten przykład E2E jest podzielony na trzy scenariusze:

**Scenariusz 1: Konfiguracja zasobów Azure i przygotowanie do dostosowywania**

**Scenariusz 2: Dostosowanie modelu Phi-3 i wdrożenie w Azure Machine Learning Studio**

**Scenariusz 3: Integracja z Prompt flow i interakcja z niestandardowym modelem w Azure AI Foundry**

Poniżej przedstawiono przegląd tego kompleksowego przykładu.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.pl.png)

### Spis treści

1. **[Scenariusz 1: Konfiguracja zasobów Azure i przygotowanie do dostosowywania](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Utwórz Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Złóż wniosek o przydział GPU w subskrypcji Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Dodaj przypisanie roli](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Skonfiguruj projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Przygotuj zestaw danych do dostosowywania](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

2. **[Scenariusz 2: Dostosowanie modelu Phi-3 i wdrożenie w Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Dostosuj model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Wdróż dostosowany model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

3. **[Scenariusz 3: Integracja z Prompt flow i interakcja z niestandardowym modelem w Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Zintegruj niestandardowy model Phi-3 z Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Interakcja z niestandardowym modelem Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## Scenariusz 1: Konfiguracja zasobów Azure i przygotowanie do dostosowywania

### Utwórz Azure Machine Learning Workspace

1. Wpisz *azure machine learning* w **pasku wyszukiwania** na górze strony portalu i wybierz **Azure Machine Learning** z wyświetlonych opcji.

    ![Wpisz azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.pl.png)

2. Wybierz **+ Create** z menu nawigacyjnego.

3. Wybierz **New workspace** z menu nawigacyjnego.

    ![Wybierz new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.pl.png)

4. Wykonaj następujące kroki:

    - Wybierz swoją **Subskrypcję Azure**.  
    - Wybierz **Grupę zasobów**, której chcesz użyć (utwórz nową, jeśli potrzeba).  
    - Wprowadź **Nazwa przestrzeni roboczej**. Musi być unikalna.  
    - Wybierz **Region**, którego chcesz użyć.  
    - Wybierz **Konto magazynu**, którego chcesz użyć (utwórz nowe, jeśli potrzeba).  
    - Wybierz **Key vault**, którego chcesz użyć (utwórz nowy, jeśli potrzeba).  
    - Wybierz **Application insights**, którego chcesz użyć (utwórz nowy, jeśli potrzeba).  
    - Wybierz **Container registry**, którego chcesz użyć (utwórz nowy, jeśli potrzeba).  

    ![Wypełnij azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.pl.png)

5. Wybierz **Review + Create**.

6. Wybierz **Create**.

### Złóż wniosek o przydział GPU w subskrypcji Azure

W tym samouczku nauczysz się, jak dostosować i wdrożyć model Phi-3, używając GPU. Do dostosowywania użyjesz GPU *Standard_NC24ads_A100_v4*, który wymaga złożenia wniosku o przydział. Do wdrożenia użyjesz GPU *Standard_NC6s_v3*, który również wymaga wniosku o przydział.

> [!NOTE]  
> Tylko subskrypcje typu Pay-As-You-Go (standardowy typ subskrypcji) są uprawnione do przydziału GPU; subskrypcje z benefitami nie są obecnie wspierane.

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wykonaj następujące kroki, aby złożyć wniosek o przydział *Standard NCADSA100v4 Family*:

    - Wybierz **Quota** z lewego panelu.  
    - Wybierz **Virtual machine family**, której chcesz użyć. Na przykład, wybierz **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, który obejmuje GPU *Standard_NC24ads_A100_v4*.  
    - Wybierz **Request quota** z menu nawigacyjnego.  

        ![Złóż wniosek o przydział.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.pl.png)

    - Na stronie Request quota wprowadź **Nowy limit rdzeni**, którego chcesz użyć. Na przykład, 24.  
    - Na stronie Request quota wybierz **Submit**, aby złożyć wniosek o przydział GPU.

1. Wykonaj następujące kroki, aby złożyć wniosek o przydział *Standard NCSv3 Family*:

    - Wybierz **Quota** z lewego panelu.  
    - Wybierz **Virtual machine family**, której chcesz użyć. Na przykład, wybierz **Standard NCSv3 Family Cluster Dedicated vCPUs**, który obejmuje GPU *Standard_NC6s_v3*.  
    - Wybierz **Request quota** z menu nawigacyjnego.  
    - Na stronie Request quota wprowadź **Nowy limit rdzeni**, którego chcesz użyć. Na przykład, 24.  
    - Na stronie Request quota wybierz **Submit**, aby złożyć wniosek o przydział GPU.

### Dodaj przypisanie roli

Aby dostosować i wdrożyć swoje modele, musisz najpierw utworzyć Zarządzaną Tożsamość Użytkownika (UAI) i przypisać jej odpowiednie uprawnienia. Ta tożsamość UAI będzie używana do uwierzytelniania podczas wdrażania.

#### Utwórz Zarządzaną Tożsamość Użytkownika (UAI)

1. Wpisz *managed identities* w **pasku wyszukiwania** na górze strony portalu i wybierz **Managed Identities** z wyświetlonych opcji.

    ![Wpisz managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.pl.png)

1. Wybierz **+ Create**.

    ![Wybierz create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.pl.png)

1. Wykonaj następujące kroki:

    - Wybierz swoją **Subskrypcję Azure**.  
    - Wybierz **Grupę zasobów**, której chcesz użyć (utwórz nową, jeśli potrzeba).  
    - Wybierz **Region**, którego chcesz użyć.  
    - Wprowadź **Nazwę**. Musi być unikalna.  

    ![Wypełnij managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.pl.png)

1. Wybierz **Review + create**.

1. Wybierz **+ Create**.

#### Dodaj przypisanie roli Contributor do Zarządzanej Tożsamości

1. Przejdź do zasobu Managed Identity, który utworzyłeś.

1. Wybierz **Azure role assignments** z lewego panelu.

1. Wybierz **+Add role assignment** z menu nawigacyjnego.

1. Na stronie Add role assignment wykonaj następujące kroki:
    - Wybierz **Scope** na **Resource group**.  
    - Wybierz swoją **Subskrypcję Azure**.  
    - Wybierz **Grupę zasobów**, której chcesz użyć.  
    - Wybierz **Rolę** na **Contributor**.  

    ![Wypełnij rolę Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.pl.png)

2. Wybierz **Save**.

#### Dodaj przypisanie roli Storage Blob Data Reader do Zarządzanej Tożsamości

1. Wpisz *storage accounts* w **pasku wyszukiwania** na górze strony portalu i wybierz **Storage accounts** z wyświetlonych opcji.

    ![Wpisz storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.pl.png)

1. Wybierz konto magazynu powiązane z utworzoną przestrzenią roboczą Azure Machine Learning. Na przykład, *finetunephistorage*.  

1. Wykonaj następujące kroki, aby przejść do strony Add role assignment:

    - Przejdź do konta magazynu Azure, które utworzyłeś.  
    - Wybierz **Access Control (IAM)** z lewego panelu.  
    - Wybierz **+ Add** z menu nawigacyjnego.  
    - Wybierz **Add role assignment** z menu nawigacyjnego.  

    ![Dodaj rolę.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.pl.png)

1. Na stronie Add role assignment wykonaj następujące kroki:

    - Na stronie Role wpisz *Storage Blob Data Reader* w **pasku wyszukiwania** i wybierz **Storage Blob Data Reader** z wyświetlonych opcji.  
    - Na stronie Role wybierz **Next**.  
    - Na stronie Members wybierz **Assign access to** **Managed identity**.  
    - Na stronie Members wybierz **+ Select members**.  
    - Na stronie Select managed identities wybierz swoją **Subskrypcję Azure**.  
    - Na stronie Select managed identities wybierz **Managed identity** na **Manage Identity**.  
    - Na stronie Select managed identities wybierz Zarządzaną Tożsamość, którą utworzyłeś. Na przykład, *finetunephi-managedidentity*.  
    - Na stronie Select managed identities wybierz **Select**.  

    ![Wybierz Zarządzaną Tożsamość.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.pl.png)

1. Wybierz **Review + assign**.

#### Dodaj przypisanie roli AcrPull do Zarządzanej Tożsamości

1. Wpisz *container registries* w **pasku wyszukiwania** na górze strony portalu i wybierz **Container registries** z wyświetlonych opcji.

    ![Wpisz container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.pl.png)

1. Wybierz rejestr kontenerów powiązany z przestrzenią roboczą Azure Machine Learning. Na przykład, *finetunephicontainerregistry*.

1. Wykonaj następujące kroki, aby przejść do strony Add role assignment:

    - Wybierz **Access Control (IAM)** z lewego panelu.  
    - Wybierz **+ Add** z menu nawigacyjnego.  
    - Wybierz **Add role assignment** z menu nawigacyjnego.  

1. Na stronie Add role assignment wykonaj następujące kroki:

    - Na stronie Role wpisz *AcrPull* w **pasku wyszukiwania** i wybierz **AcrPull** z wyświetlonych opcji.  
    - Na stronie Role wybierz **Next**.  
    - Na stronie Members wybierz **Assign access to** **Managed identity**.  
    - Na stronie Members wybierz **+ Select members**.  
    - Na stronie Select managed identities wybierz swoją **Subskrypcję Azure**.  
    - Na stronie Select managed identities wybierz **Managed identity** na **Manage Identity**.  
    - Na stronie Select managed identities wybierz Zarządzaną Tożsamość, którą utworzyłeś. Na przykład, *finetunephi-managedidentity*.  
    - Na stronie Select managed identities wybierz **Select**.  
    - Wybierz **Review + assign**.

### Skonfiguruj projekt

Aby pobrać zestawy danych potrzebne do dostosowywania, skonfigurujesz środowisko lokalne.

W tym ćwiczeniu:

- Utworzysz folder do pracy.  
- Utworzysz wirtualne środowisko.  
- Zainstalujesz wymagane pakiety.  
- Utworzysz plik *download_dataset.py* do pobrania zestawu danych.

#### Utwórz folder do pracy

1. Otwórz okno terminala i wpisz następujące polecenie, aby utworzyć folder o nazwie *finetune-phi* w domyślnej ścieżce.

    ```console
    mkdir finetune-phi
    ```

2. Wpisz następujące polecenie w terminalu, aby przejść do utworzonego folderu *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Utwórz wirtualne środowisko

1. Wpisz następujące polecenie w terminalu, aby utworzyć wirtualne środowisko o nazwie *.venv*.

    ```console
    python -m venv .venv
    ```

2. Wpisz następujące polecenie w terminalu, aby aktywować wirtualne środowisko.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> Jeśli wszystko działa poprawnie, powinieneś zobaczyć *(.venv)* przed znakiem zachęty w terminalu.

#### Zainstaluj wymagane pakiety

1. Wpisz następujące polecenia w terminalu, aby zainstalować wymagane pakiety.

    ```console
    pip install datasets==2.19.1
    ```

#### Utwórz `download_dataset.py`

> [!NOTE]  
> Struktura folderów:  
> 
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otwórz **Visual Studio Code**.

1. Wybierz **File** z menu głównego.

1. Wybierz **Open Folder**.

1. Wybierz folder *finetune-phi*, który utworzyłeś, znajdujący się w *C:\Users\yourUserName\finetune-phi*.

    ![Wybierz utworzony folder.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.pl.png)

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **New File**, aby utworzyć nowy plik o nazwie *download_dataset.py*.

    ![Utwórz nowy plik.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.pl.png)

### Przygotuj zestaw danych do dostosowywania

W tym ćwiczeniu uruchomisz plik *download_dataset.py*, aby pobrać zestawy danych *ultrachat_200k* na swoje lokalne środowisko. Następnie użyjesz tych danych do dostosowania modelu Phi-3 w Azure Machine Learning.

W tym ćwiczeniu:

- Dodasz kod do pliku *download_dataset.py*, aby pobrać dane.  
-
1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wybierz **Compute** z menu po lewej stronie.

1. Wybierz **Compute clusters** z menu nawigacyjnego.

1. Kliknij **+ New**.

    ![Wybierz compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.pl.png)

1. Wykonaj następujące kroki:

    - Wybierz **Region**, którego chcesz użyć.
    - Ustaw **Virtual machine tier** na **Dedicated**.
    - Ustaw **Virtual machine type** na **GPU**.
    - Ustaw filtr **Virtual machine size** na **Select from all options**.
    - Wybierz **Virtual machine size** jako **Standard_NC24ads_A100_v4**.

    ![Utwórz klaster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.pl.png)

1. Kliknij **Next**.

1. Wykonaj następujące kroki:

    - Wprowadź **Compute name**. Musi być unikalny.
    - Ustaw **Minimum number of nodes** na **0**.
    - Ustaw **Maximum number of nodes** na **1**.
    - Ustaw **Idle seconds before scale down** na **120**.

    ![Utwórz klaster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.pl.png)

1. Kliknij **Create**.

#### Dostosowanie modelu Phi-3

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wybierz przestrzeń roboczą Azure Machine Learning, którą utworzyłeś.

    ![Wybierz utworzoną przestrzeń roboczą.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.pl.png)

1. Wykonaj następujące kroki:

    - Wybierz **Model catalog** z menu po lewej stronie.
    - Wpisz *phi-3-mini-4k* w **search bar** i wybierz **Phi-3-mini-4k-instruct** z dostępnych opcji.

    ![Wpisz phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.pl.png)

1. Wybierz **Fine-tune** z menu nawigacyjnego.

    ![Wybierz fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.pl.png)

1. Wykonaj następujące kroki:

    - Ustaw **Select task type** na **Chat completion**.
    - Kliknij **+ Select data**, aby przesłać **Traning data**.
    - Ustaw typ przesyłania danych walidacyjnych na **Provide different validation data**.
    - Kliknij **+ Select data**, aby przesłać **Validation data**.

    ![Wypełnij stronę dostosowywania.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.pl.png)

    > [!TIP]
    >
    > Możesz wybrać **Advanced settings**, aby dostosować konfiguracje, takie jak **learning_rate** i **lr_scheduler_type**, w celu zoptymalizowania procesu dostosowywania do swoich potrzeb.

1. Kliknij **Finish**.

1. W tym ćwiczeniu pomyślnie dostosowano model Phi-3 przy użyciu Azure Machine Learning. Należy pamiętać, że proces dostosowywania może zająć dużo czasu. Po uruchomieniu zadania dostosowywania musisz poczekać na jego zakończenie. Status zadania dostosowywania możesz monitorować, przechodząc do zakładki Jobs w menu po lewej stronie w przestrzeni roboczej Azure Machine Learning. W kolejnej części wdrożysz dostosowany model i zintegrowasz go z Prompt flow.

    ![Zobacz zadanie dostosowywania.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.pl.png)

### Wdróż dostosowany model Phi-3

Aby zintegrować dostosowany model Phi-3 z Prompt flow, musisz go wdrożyć, aby był dostępny do inferencji w czasie rzeczywistym. Proces ten obejmuje rejestrację modelu, utworzenie punktu końcowego online i wdrożenie modelu.

W tym ćwiczeniu:

- Zarejestrujesz dostosowany model w przestrzeni roboczej Azure Machine Learning.
- Utworzysz punkt końcowy online.
- Wdrożysz zarejestrowany dostosowany model Phi-3.

#### Zarejestruj dostosowany model

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wybierz przestrzeń roboczą Azure Machine Learning, którą utworzyłeś.

    ![Wybierz utworzoną przestrzeń roboczą.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.pl.png)

1. Wybierz **Models** z menu po lewej stronie.
1. Kliknij **+ Register**.
1. Wybierz **From a job output**.

    ![Zarejestruj model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.pl.png)

1. Wybierz zadanie, które utworzyłeś.

    ![Wybierz zadanie.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.pl.png)

1. Kliknij **Next**.

1. Ustaw **Model type** na **MLflow**.

1. Upewnij się, że **Job output** jest wybrane; powinno być automatycznie zaznaczone.

    ![Wybierz output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.pl.png)

2. Kliknij **Next**.

3. Kliknij **Register**.

    ![Kliknij register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.pl.png)

4. Możesz zobaczyć swój zarejestrowany model, przechodząc do menu **Models** w menu po lewej stronie.

    ![Zarejestrowany model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.pl.png)

#### Wdróż dostosowany model

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.

1. Wybierz **Endpoints** z menu po lewej stronie.

1. Wybierz **Real-time endpoints** z menu nawigacyjnego.

    ![Utwórz punkt końcowy.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.pl.png)

1. Kliknij **Create**.

1. Wybierz zarejestrowany model, który utworzyłeś.

    ![Wybierz zarejestrowany model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.pl.png)

1. Kliknij **Select**.

1. Wykonaj następujące kroki:

    - Ustaw **Virtual machine** na *Standard_NC6s_v3*.
    - Wybierz liczbę instancji **Instance count**, np. *1*.
    - Ustaw **Endpoint** na **New**, aby utworzyć punkt końcowy.
    - Wprowadź **Endpoint name**. Musi być unikalny.
    - Wprowadź **Deployment name**. Musi być unikalny.

    ![Wypełnij ustawienia wdrożenia.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.pl.png)

1. Kliknij **Deploy**.

> [!WARNING]
> Aby uniknąć dodatkowych opłat na swoim koncie, pamiętaj o usunięciu utworzonego punktu końcowego w przestrzeni roboczej Azure Machine Learning.
>

#### Sprawdź status wdrożenia w przestrzeni roboczej Azure Machine Learning

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.

1. Wybierz **Endpoints** z menu po lewej stronie.

1. Wybierz punkt końcowy, który utworzyłeś.

    ![Wybierz punkty końcowe.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.pl.png)

1. Na tej stronie możesz zarządzać punktami końcowymi podczas procesu wdrażania.

> [!NOTE]
> Po zakończeniu wdrożenia upewnij się, że **Live traffic** jest ustawione na **100%**. Jeśli nie jest, wybierz **Update traffic**, aby dostosować ustawienia ruchu. Pamiętaj, że nie możesz testować modelu, jeśli ruch jest ustawiony na 0%.
>
> ![Ustaw ruch.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.pl.png)
>
![Skopiuj klucz API i URI punktu końcowego.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.pl.png)

#### Dodaj niestandardowe połączenie

1. Odwiedź [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Przejdź do projektu Azure AI Foundry, który utworzyłeś.

1. W projekcie, który utworzyłeś, wybierz **Settings** z menu po lewej stronie.

1. Wybierz **+ New connection**.

    ![Wybierz nowe połączenie.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.pl.png)

1. Wybierz **Custom keys** z menu nawigacyjnego.

    ![Wybierz niestandardowe klucze.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.pl.png)

1. Wykonaj następujące kroki:

    - Wybierz **+ Add key value pairs**.
    - Dla nazwy klucza wprowadź **endpoint** i wklej punkt końcowy, który skopiowałeś z Azure ML Studio, w polu wartości.
    - Wybierz ponownie **+ Add key value pairs**.
    - Dla nazwy klucza wprowadź **key** i wklej klucz, który skopiowałeś z Azure ML Studio, w polu wartości.
    - Po dodaniu kluczy zaznacz **is secret**, aby zapobiec ujawnieniu klucza.

    ![Dodaj połączenie.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.pl.png)

1. Wybierz **Add connection**.

#### Utwórz Prompt flow

Dodałeś niestandardowe połączenie w Azure AI Foundry. Teraz utwórz Prompt flow, korzystając z poniższych kroków. Następnie połącz ten Prompt flow z niestandardowym połączeniem, aby móc używać modelu dostosowanego w Prompt flow.

1. Przejdź do projektu Azure AI Foundry, który utworzyłeś.

1. Wybierz **Prompt flow** z menu po lewej stronie.

1. Wybierz **+ Create** z menu nawigacyjnego.

    ![Wybierz Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.pl.png)

1. Wybierz **Chat flow** z menu nawigacyjnego.

    ![Wybierz chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.pl.png)

1. Wprowadź **Folder name**, którego chcesz użyć.

    ![Wprowadź nazwę.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.pl.png)

2. Wybierz **Create**.

#### Skonfiguruj Prompt flow do rozmowy z dostosowanym modelem Phi-3

Musisz zintegrować dostosowany model Phi-3 z Prompt flow. Jednak istniejący Prompt flow nie jest zaprojektowany do tego celu. Dlatego musisz przebudować Prompt flow, aby umożliwić integrację niestandardowego modelu.

1. W Prompt flow wykonaj następujące kroki, aby przebudować istniejący flow:

    - Wybierz **Raw file mode**.
    - Usuń cały istniejący kod z pliku *flow.dag.yml*.
    - Dodaj następujący kod do pliku *flow.dag.yml*.

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

    - Wybierz **Save**.

    ![Wybierz tryb raw file.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.pl.png)

1. Dodaj następujący kod do pliku *integrate_with_promptflow.py*, aby użyć niestandardowego modelu Phi-3 w Prompt flow.

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

    ![Wklej kod prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.pl.png)

> [!NOTE]
> Szczegółowe informacje na temat używania Prompt flow w Azure AI Foundry znajdziesz w [Prompt flow w Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Wybierz **Chat input**, **Chat output**, aby umożliwić rozmowę z modelem.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.pl.png)

1. Teraz możesz rozmawiać z dostosowanym modelem Phi-3. W następnym ćwiczeniu dowiesz się, jak uruchomić Prompt flow i używać go do rozmowy z dostosowanym modelem Phi-3.

> [!NOTE]
>
> Przebudowany flow powinien wyglądać jak na poniższym obrazku:
>
> ![Przykład flow.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.pl.png)
>

### Rozmowa z dostosowanym modelem Phi-3

Teraz, gdy dostosowałeś i zintegrowałeś swój model Phi-3 z Prompt flow, jesteś gotowy, aby rozpocząć interakcję z nim. To ćwiczenie przeprowadzi Cię przez proces konfiguracji i inicjowania rozmowy z modelem przy użyciu Prompt flow. Postępując zgodnie z tymi krokami, będziesz mógł w pełni wykorzystać możliwości swojego dostosowanego modelu Phi-3 do różnych zadań i rozmów.

- Rozmawiaj z dostosowanym modelem Phi-3 za pomocą Prompt flow.

#### Uruchom Prompt flow

1. Wybierz **Start compute sessions**, aby uruchomić Prompt flow.

    ![Uruchom sesję obliczeniową.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.pl.png)

1. Wybierz **Validate and parse input**, aby odświeżyć parametry.

    ![Zatwierdź dane wejściowe.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.pl.png)

1. Wybierz **Value** dla **connection** do niestandardowego połączenia, które utworzyłeś. Na przykład *connection*.

    ![Połączenie.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.pl.png)

#### Rozmowa z dostosowanym modelem

1. Wybierz **Chat**.

    ![Wybierz chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.pl.png)

1. Oto przykład wyników: Teraz możesz rozmawiać z dostosowanym modelem Phi-3. Zaleca się zadawanie pytań opartych na danych użytych do dostosowania.

    ![Rozmowa z prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.pl.png)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.