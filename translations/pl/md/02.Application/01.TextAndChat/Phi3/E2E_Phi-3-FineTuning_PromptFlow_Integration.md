# Dostosowanie i integracja modeli Phi-3 z Prompt flow

Ten kompleksowy przykład (E2E) oparty jest na przewodniku "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Przedstawia procesy dostosowywania, wdrażania i integracji niestandardowych modeli Phi-3 z Prompt flow.

## Przegląd

W tym kompleksowym przykładzie nauczysz się, jak dostosować model Phi-3 i zintegrować go z Prompt flow. Wykorzystując Azure Machine Learning oraz Prompt flow, stworzysz przepływ pracy umożliwiający wdrażanie i korzystanie z niestandardowych modeli AI. Przykład ten podzielony jest na trzy scenariusze:

**Scenariusz 1: Skonfiguruj zasoby Azure i przygotuj się do dostosowywania**

**Scenariusz 2: Dostosuj model Phi-3 i wdrażaj w Azure Machine Learning Studio**

**Scenariusz 3: Zintegruj z Prompt flow i rozmawiaj z niestandardowym modelem**

Poniżej znajduje się przegląd tego kompleksowego przykładu.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.pl.png)

### Spis treści

1. **[Scenariusz 1: Skonfiguruj zasoby Azure i przygotuj się do dostosowywania](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Utwórz Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Poproś o przydziały GPU w subskrypcji Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dodaj przypisanie ról](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Skonfiguruj projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Przygotuj zbiór danych do dostosowywania](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariusz 2: Dostosuj model Phi-3 i wdrażaj w Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Skonfiguruj Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dostosuj model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Wdrażaj dostosowany model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenariusz 3: Zintegruj z Prompt flow i rozmawiaj z niestandardowym modelem](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Zintegruj niestandardowy model Phi-3 z Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rozmawiaj z niestandardowym modelem](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenariusz 1: Skonfiguruj zasoby Azure i przygotuj się do dostosowywania

### Utwórz Azure Machine Learning Workspace

1. Wpisz *azure machine learning* w **pasku wyszukiwania** u góry strony portalu i wybierz **Azure Machine Learning** z dostępnych opcji.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.pl.png)

1. Wybierz **+ Create** z menu nawigacyjnego.

1. Wybierz **New workspace** z menu nawigacyjnego.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.pl.png)

1. Wykonaj następujące czynności:

    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć (utwórz nową, jeśli to konieczne).
    - Wprowadź **Workspace Name**. Musi to być unikalna wartość.
    - Wybierz **Region**, z którego chcesz korzystać.
    - Wybierz **Storage account**, którego chcesz użyć (utwórz nowe, jeśli to konieczne).
    - Wybierz **Key vault**, którego chcesz użyć (utwórz nowe, jeśli to konieczne).
    - Wybierz **Application insights**, którego chcesz użyć (utwórz nowe, jeśli to konieczne).
    - Wybierz **Container registry**, którego chcesz użyć (utwórz nowe, jeśli to konieczne).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.pl.png)

1. Wybierz **Review + Create**.

1. Wybierz **Create**.

### Poproś o przydziały GPU w subskrypcji Azure

W tym kompleksowym przykładzie użyjesz GPU *Standard_NC24ads_A100_v4* do dostosowywania, które wymaga złożenia wniosku o przydział, oraz CPU *Standard_E4s_v3* do wdrażania, które nie wymaga wniosku o przydział.

> [!NOTE]
>
> Przydziały GPU są dostępne tylko dla subskrypcji Pay-As-You-Go (standardowy typ subskrypcji); subskrypcje benefitowe obecnie nie są wspierane.
>
> Dla osób korzystających z subskrypcji benefitowych (np. Visual Studio Enterprise Subscription) lub chcących szybko przetestować proces dostosowywania i wdrażania, ten przewodnik zawiera również wskazówki dotyczące dostosowywania z minimalnym zbiorem danych przy użyciu CPU. Jednakże wyniki dostosowywania są znacznie lepsze przy użyciu GPU z większymi zbiorami danych.

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wykonaj następujące czynności, aby złożyć wniosek o przydział GPU *Standard NCADSA100v4 Family*:

    - Wybierz **Quota** z lewego paska nawigacyjnego.
    - Wybierz **Virtual machine family**, której chcesz użyć. Na przykład wybierz **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, który obejmuje GPU *Standard_NC24ads_A100_v4*.
    - Wybierz **Request quota** z menu nawigacyjnego.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.pl.png)

    - Na stronie Request quota wprowadź **New cores limit**, który chcesz wykorzystać. Na przykład 24.
    - Na stronie Request quota wybierz **Submit**, aby złożyć wniosek o przydział GPU.

> [!NOTE]
> Możesz wybrać odpowiedni GPU lub CPU dla swoich potrzeb, zapoznając się z dokumentem [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Dodaj przypisanie ról

Aby dostosowywać i wdrażać swoje modele, musisz najpierw utworzyć User Assigned Managed Identity (UAI) i przypisać jej odpowiednie uprawnienia. UAI będzie używane do uwierzytelniania podczas wdrażania.

#### Utwórz User Assigned Managed Identity (UAI)

1. Wpisz *managed identities* w **pasku wyszukiwania** u góry strony portalu i wybierz **Managed Identities** z dostępnych opcji.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.pl.png)

1. Wybierz **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.pl.png)

1. Wykonaj następujące czynności:

    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć (utwórz nową, jeśli to konieczne).
    - Wybierz **Region**, z którego chcesz korzystać.
    - Wprowadź **Name**. Musi to być unikalna wartość.

1. Wybierz **Review + create**.

1. Wybierz **+ Create**.

#### Dodaj przypisanie roli Contributor do Managed Identity

1. Przejdź do zasobu Managed Identity, który utworzyłeś.

1. Wybierz **Azure role assignments** z lewego paska nawigacyjnego.

1. Wybierz **+Add role assignment** z menu nawigacyjnego.

1. Na stronie Add role assignment wykonaj następujące czynności:
    - Wybierz **Scope** jako **Resource group**.
    - Wybierz swoją subskrypcję Azure **Subscription**.
    - Wybierz **Resource group**, której chcesz użyć.
    - Wybierz **Role** jako **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.pl.png)

1. Wybierz **Save**.

#### Dodaj przypisanie roli Storage Blob Data Reader do Managed Identity

1. Wpisz *storage accounts* w **pasku wyszukiwania** u góry strony portalu i wybierz **Storage accounts** z dostępnych opcji.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.pl.png)

1. Wybierz konto magazynu powiązane z utworzonym Azure Machine Learning workspace. Na przykład *finetunephistorage*.

1. Wykonaj następujące czynności, aby przejść do strony Add role assignment:

    - Przejdź do konta magazynu Azure, które utworzyłeś.
    - Wybierz **Access Control (IAM)** z lewego paska nawigacyjnego.
    - Wybierz **+ Add** z menu nawigacyjnego.
    - Wybierz **Add role assignment** z menu nawigacyjnego.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.pl.png)

1. Na stronie Add role assignment wykonaj następujące czynności:

    - Na stronie Role wpisz *Storage Blob Data Reader* w **pasku wyszukiwania** i wybierz **Storage Blob Data Reader** z dostępnych opcji.
    - Na stronie Role wybierz **Next**.
    - Na stronie Members wybierz **Assign access to** **Managed identity**.
    - Na stronie Members wybierz **+ Select members**.
    - Na stronie Select managed identities wybierz swoją subskrypcję Azure **Subscription**.
    - Na stronie Select managed identities wybierz **Managed identity** jako **Manage Identity**.
    - Na stronie Select managed identities wybierz Managed Identity, które utworzyłeś. Na przykład *finetunephi-managedidentity*.
    - Na stronie Select managed identities wybierz **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.pl.png)

1. Wybierz **Review + assign**.

#### Dodaj przypisanie roli AcrPull do Managed Identity

1. Wpisz *container registries* w **pasku wyszukiwania** u góry strony portalu i wybierz **Container registries** z dostępnych opcji.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.pl.png)

1. Wybierz rejestr kontenerów powiązany z Azure Machine Learning workspace. Na przykład *finetunephicontainerregistries*

1. Wykonaj następujące czynności, aby przejść do strony Add role assignment:

    - Wybierz **Access Control (IAM)** z lewego paska nawigacyjnego.
    - Wybierz **+ Add** z menu nawigacyjnego.
    - Wybierz **Add role assignment** z menu nawigacyjnego.

1. Na stronie Add role assignment wykonaj następujące czynności:

    - Na stronie Role wpisz *AcrPull* w **pasku wyszukiwania** i wybierz **AcrPull** z dostępnych opcji.
    - Na stronie Role wybierz **Next**.
    - Na stronie Members wybierz **Assign access to** **Managed identity**.
    - Na stronie Members wybierz **+ Select members**.
    - Na stronie Select managed identities wybierz swoją subskrypcję Azure **Subscription**.
    - Na stronie Select managed identities wybierz **Managed identity** jako **Manage Identity**.
    - Na stronie Select managed identities wybierz Managed Identity, które utworzyłeś. Na przykład *finetunephi-managedidentity*.
    - Na stronie Select managed identities wybierz **Select**.
    - Wybierz **Review + assign**.

### Skonfiguruj projekt

Teraz utworzysz folder roboczy i skonfigurujesz wirtualne środowisko do rozwijania programu, który wchodzi w interakcje z użytkownikami i wykorzystuje przechowywaną historię rozmów z Azure Cosmos DB do informowania odpowiedzi.

#### Utwórz folder roboczy

1. Otwórz terminal i wpisz następujące polecenie, aby utworzyć folder o nazwie *finetune-phi* w domyślnej ścieżce.

    ```console
    mkdir finetune-phi
    ```

1. Wpisz następujące polecenie w terminalu, aby przejść do utworzonego folderu *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Utwórz wirtualne środowisko

1. Wpisz następujące polecenie w terminalu, aby utworzyć wirtualne środowisko o nazwie *.venv*.

    ```console
    python -m venv .venv
    ```

1. Wpisz następujące polecenie w terminalu, aby aktywować wirtualne środowisko.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Jeśli wszystko działa, przed znakiem zachęty powinno pojawić się *(.venv)*.

#### Zainstaluj wymagane pakiety

1. Wpisz następujące polecenia w terminalu, aby zainstalować wymagane pakiety.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Utwórz pliki projektu

W tym ćwiczeniu utworzysz podstawowe pliki projektu. Pliki te obejmują skrypty do pobierania zbioru danych, konfigurowania środowiska Azure Machine Learning, dostosowywania modelu Phi-3 oraz wdrażania dostosowanego modelu. Stworzysz także plik *conda.yml* do skonfigurowania środowiska dostosowywania.

W tym ćwiczeniu wykonasz:

- Utworzenie pliku *download_dataset.py* do pobierania zbioru danych.
- Utworzenie pliku *setup_ml.py* do konfigurowania środowiska Azure Machine Learning.
- Utworzenie pliku *fine_tune.py* w folderze *finetuning_dir* do dostosowywania modelu Phi-3 za pomocą zbioru danych.
- Utworzenie pliku *conda.yml* do konfiguracji środowiska dostosowywania.
- Utworzenie pliku *deploy_model.py* do wdrażania dostosowanego modelu.
- Utworzenie pliku *integrate_with_promptflow.py* do integracji dostosowanego modelu i jego uruchamiania za pomocą Prompt flow.
- Utworzenie pliku *flow.dag.yml* do konfiguracji struktury przepływu pracy dla Prompt flow.
- Utworzenie pliku *config.py* do wprowadzenia informacji o Azure.

> [!NOTE]
>
> Kompletny układ folderów:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Otwórz **Visual Studio Code**.

1. Wybierz **File** z menu.

1. Wybierz **Open Folder**.

1. Wybierz folder *finetune-phi*, który utworzyłeś, znajdujący się pod ścieżką *C:\Users\yourUserName\finetune-phi*.

    ![Open project folder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.pl.png)

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **New File**, aby utworzyć nowy plik o nazwie *download_dataset.py*.

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **New File**, aby utworzyć nowy plik o nazwie *setup_ml.py*.

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **New File**, aby utworzyć nowy plik o nazwie *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.pl.png)

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **New Folder**, aby utworzyć nowy folder o nazwie *finetuning_dir*.

1. W folderze *finetuning_dir* utwórz nowy plik o nazwie *fine_tune.py*.

#### Utwórz i skonfiguruj plik *conda.yml*

1. W lewym panelu Visual Studio Code kliknij prawym przyciskiem myszy i wybierz **New File**, aby utworzyć nowy plik
![Znajdź identyfikator subskrypcji.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.pl.png)

1. Wykonaj poniższe kroki, aby dodać nazwę Azure Workspace:

    - Przejdź do zasobu Azure Machine Learning, który utworzyłeś.
    - Skopiuj i wklej nazwę swojego konta do pliku *config.py*.

    ![Znajdź nazwę Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.pl.png)

1. Wykonaj poniższe kroki, aby dodać nazwę grupy zasobów Azure:

    - Przejdź do zasobu Azure Machine Learning, który utworzyłeś.
    - Skopiuj i wklej nazwę swojej grupy zasobów Azure do pliku *config.py*.

    ![Znajdź nazwę grupy zasobów.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.pl.png)

2. Wykonaj poniższe kroki, aby dodać nazwę Azure Managed Identity:

    - Przejdź do zasobu Managed Identities, który utworzyłeś.
    - Skopiuj i wklej nazwę swojej Azure Managed Identity do pliku *config.py*.

    ![Znajdź UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.pl.png)

### Przygotowanie zestawu danych do fine-tuningu

W tym ćwiczeniu uruchomisz plik *download_dataset.py*, aby pobrać zestawy danych *ULTRACHAT_200k* do swojego lokalnego środowiska. Następnie wykorzystasz te zestawy danych do fine-tuningu modelu Phi-3 w Azure Machine Learning.

#### Pobierz zestaw danych za pomocą *download_dataset.py*

1. Otwórz plik *download_dataset.py* w Visual Studio Code.

1. Dodaj poniższy kod do pliku *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Wskazówki dotyczące fine-tuningu z minimalnym zestawem danych przy użyciu CPU**
>
> Jeśli chcesz użyć CPU do fine-tuningu, ta metoda jest idealna dla osób posiadających subskrypcje benefitowe (np. Visual Studio Enterprise Subscription) lub chcących szybko przetestować proces fine-tuningu i wdrażania.
>
> Zamień `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Wpisz poniższą komendę w terminalu, aby uruchomić skrypt i pobrać zestaw danych do lokalnego środowiska.

    ```console
    python download_data.py
    ```

1. Zweryfikuj, czy zestawy danych zostały pomyślnie zapisane w lokalnym katalogu *finetune-phi/data*.

> [!NOTE]
>
> **Rozmiar zestawu danych i czas fine-tuningu**
>
> W tym przykładzie E2E używasz tylko 1% zestawu danych (`train_sft[:1%]`). Znacząco zmniejsza to ilość danych, przyspieszając procesy przesyłania i fine-tuningu. Możesz dostosować procent, aby znaleźć odpowiedni balans między czasem treningu a wydajnością modelu. Użycie mniejszego podzbioru zestawu danych skraca czas potrzebny na fine-tuning, co czyni proces bardziej przystępnym w przykładzie E2E.

## Scenariusz 2: Fine-tuning modelu Phi-3 i wdrażanie w Azure Machine Learning Studio

### Konfiguracja Azure CLI

Musisz skonfigurować Azure CLI, aby uwierzytelnić swoje środowisko. Azure CLI pozwala zarządzać zasobami Azure bezpośrednio z wiersza poleceń i dostarcza dane uwierzytelniające niezbędne do uzyskania dostępu do tych zasobów przez Azure Machine Learning. Aby rozpocząć, zainstaluj [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

1. Otwórz okno terminala i wpisz poniższą komendę, aby zalogować się na swoje konto Azure.

    ```console
    az login
    ```

1. Wybierz swoje konto Azure do użycia.

1. Wybierz subskrypcję Azure do użycia.

    ![Znajdź nazwę grupy zasobów.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.pl.png)

> [!TIP]
>
> Jeśli masz problemy z logowaniem do Azure, spróbuj użyć kodu urządzenia. Otwórz okno terminala i wpisz poniższą komendę, aby zalogować się na swoje konto Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tuning modelu Phi-3

W tym ćwiczeniu przeprowadzisz fine-tuning modelu Phi-3 za pomocą dostarczonego zestawu danych. Najpierw zdefiniujesz proces fine-tuningu w pliku *fine_tune.py*. Następnie skonfigurujesz środowisko Azure Machine Learning i zainicjujesz proces fine-tuningu, uruchamiając plik *setup_ml.py*. Ten skrypt zapewnia, że fine-tuning odbywa się w środowisku Azure Machine Learning.

Uruchamiając *setup_ml.py*, uruchomisz proces fine-tuningu w środowisku Azure Machine Learning.

#### Dodaj kod do pliku *fine_tune.py*

1. Przejdź do folderu *finetuning_dir* i otwórz plik *fine_tune.py* w Visual Studio Code.

1. Dodaj poniższy kod do pliku *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Zapisz i zamknij plik *fine_tune.py*.

> [!TIP]
> **Możesz przeprowadzić fine-tuning modelu Phi-3.5**
>
> W pliku *fine_tune.py* możesz zmienić pole `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` w swoim skrypcie.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tuning Phi-3.5.":::
>

#### Dodaj kod do pliku *setup_ml.py*

1. Otwórz plik *setup_ml.py* w Visual Studio Code.

1. Dodaj poniższy kod do pliku *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Zamień `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` na swoje szczegóły.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Wskazówki dotyczące fine-tuningu z minimalnym zestawem danych przy użyciu CPU**
>
> Jeśli chcesz użyć CPU do fine-tuningu, ta metoda jest idealna dla osób posiadających subskrypcje benefitowe (np. Visual Studio Enterprise Subscription) lub chcących szybko przetestować proces fine-tuningu i wdrażania.
>
> 1. Otwórz plik *setup_ml*.
> 1. Zamień `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` na swoje szczegóły.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Wpisz poniższą komendę, aby uruchomić skrypt *setup_ml.py* i rozpocząć proces fine-tuningu w Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. W tym ćwiczeniu pomyślnie przeprowadziłeś fine-tuning modelu Phi-3 w Azure Machine Learning. Uruchamiając skrypt *setup_ml.py*, skonfigurowałeś środowisko Azure Machine Learning i zainicjowałeś proces fine-tuningu zdefiniowany w pliku *fine_tune.py*. Pamiętaj, że proces fine-tuningu może zająć dużo czasu. Po uruchomieniu `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.pl.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` z wybraną nazwą dla wdrożenia.

#### Dodaj kod do pliku *deploy_model.py*

Uruchomienie pliku *deploy_model.py* automatyzuje cały proces wdrażania. Rejestruje model, tworzy punkt końcowy i wykonuje wdrożenie na podstawie ustawień określonych w pliku config.py, które obejmują nazwę modelu, nazwę punktu końcowego i nazwę wdrożenia.

1. Otwórz plik *deploy_model.py* w Visual Studio Code.

1. Dodaj poniższy kod do pliku *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Wykonaj poniższe kroki, aby uzyskać `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` z odpowiednimi szczegółami.

1. Wpisz poniższą komendę, aby uruchomić skrypt *deploy_model.py* i rozpocząć proces wdrażania w Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Aby uniknąć dodatkowych kosztów na swoim koncie, upewnij się, że usunąłeś utworzony punkt końcowy w przestrzeni roboczej Azure Machine Learning.
>

#### Sprawdź status wdrożenia w przestrzeni roboczej Azure Machine Learning

1. Odwiedź [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.

1. Wybierz **Studio web URL**, aby otworzyć przestrzeń roboczą Azure Machine Learning.

1. Wybierz **Endpoints** z zakładki po lewej stronie.

    ![Wybierz punkty końcowe.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.pl.png)

2. Wybierz punkt końcowy, który utworzyłeś.

    ![Wybierz punkty końcowe, które utworzyłeś.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.pl.png)

3. Na tej stronie możesz zarządzać punktami końcowymi utworzonymi podczas procesu wdrażania.

## Scenariusz 3: Integracja z Prompt Flow i rozmowa z niestandardowym modelem

### Integracja niestandardowego modelu Phi-3 z Prompt Flow

Po pomyślnym wdrożeniu swojego fine-tunowanego modelu możesz teraz zintegrować go z Prompt Flow, aby używać swojego modelu w aplikacjach czasu rzeczywistego, umożliwiając różnorodne zadania interaktywne z Twoim niestandardowym modelem Phi-3.

#### Ustaw klucz API i URI punktu końcowego dla fine-tunowanego modelu Phi-3

1. Przejdź do przestrzeni roboczej Azure Machine Learning, którą utworzyłeś.
1. Wybierz **Endpoints** z zakładki po lewej stronie.
1. Wybierz punkt końcowy, który utworzyłeś.
1. Wybierz **Consume** z menu nawigacyjnego.
1. Skopiuj i wklej swój **REST endpoint** do pliku *config.py*, zastępując `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` swoim **Primary key**.

    ![Skopiuj klucz API i URI punktu końcowego.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.pl.png)

#### Dodaj kod do pliku *flow.dag.yml*

1. Otwórz plik *flow.dag.yml* w Visual Studio Code.

1. Dodaj poniższy kod do pliku *flow.dag.yml*.

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

#### Dodaj kod do pliku *integrate_with_promptflow.py*

1. Otwórz plik *integrate_with_promptflow.py* w Visual Studio Code.

1. Dodaj poniższy kod do pliku *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Rozmowa z niestandardowym modelem

1. Wpisz poniższą komendę, aby uruchomić skrypt *deploy_model.py* i rozpocząć proces wdrażania w Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Oto przykład wyników: Teraz możesz rozmawiać z niestandardowym modelem Phi-3. Zaleca się zadawanie pytań opartych na danych użytych do fine-tuningu.

    ![Przykład Prompt Flow.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.pl.png)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za wiążące źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.