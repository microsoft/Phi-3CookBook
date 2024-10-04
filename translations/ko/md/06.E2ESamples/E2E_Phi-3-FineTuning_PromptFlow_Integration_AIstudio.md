# Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Studio

이 끝에서 끝까지(E2E) 샘플은 Microsoft Tech Community의 가이드 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)"를 기반으로 합니다. 이 샘플은 Azure AI Studio에서 Prompt flow와 함께 사용자 지정 Phi-3 모델을 미세 조정, 배포 및 통합하는 과정을 소개합니다. 
"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" 샘플과 달리, 이 튜토리얼은 Azure AI / ML Studio 내에서 모델을 미세 조정하고 통합하는 것에만 초점을 맞춥니다.

## 개요

이 E2E 샘플에서는 Phi-3 모델을 미세 조정하고 Azure AI Studio에서 Prompt flow와 통합하는 방법을 배웁니다. Azure AI / ML Studio를 활용하여 사용자 지정 AI 모델을 배포하고 활용하는 워크플로를 설정하게 됩니다. 이 E2E 샘플은 세 가지 시나리오로 나뉩니다:

**시나리오 1: Azure 리소스 설정 및 미세 조정 준비**

**시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포**

**시나리오 3: Prompt flow와 통합 및 Azure AI Studio에서 사용자 지정 모델과 채팅**

다음은 이 E2E 샘플의 개요입니다.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../translated_images/00-01-architecture.fa40b38b29f795863378026c4dcc3007b0938b0b43afaf8c331906d03742b2e6.ko.png)

### 목차

1. **[시나리오 1: Azure 리소스 설정 및 미세 조정 준비](../../../../md/06.E2ESamples)**
    - [Azure Machine Learning 작업 영역 생성](../../../../md/06.E2ESamples)
    - [Azure 구독에서 GPU 할당량 요청](../../../../md/06.E2ESamples)
    - [역할 할당 추가](../../../../md/06.E2ESamples)
    - [프로젝트 설정](../../../../md/06.E2ESamples)
    - [미세 조정을 위한 데이터셋 준비](../../../../md/06.E2ESamples)

1. **[시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포](../../../../md/06.E2ESamples)**
    - [Phi-3 모델 미세 조정](../../../../md/06.E2ESamples)
    - [미세 조정된 Phi-3 모델 배포](../../../../md/06.E2ESamples)

1. **[시나리오 3: Prompt flow와 통합 및 Azure AI Studio에서 사용자 지정 모델과 채팅](../../../../md/06.E2ESamples)**
    - [사용자 지정 Phi-3 모델을 Prompt flow와 통합](../../../../md/06.E2ESamples)
    - [사용자 지정 Phi-3 모델과 채팅](../../../../md/06.E2ESamples)

## 시나리오 1: Azure 리소스 설정 및 미세 조정 준비

### Azure Machine Learning 작업 영역 생성

1. 포털 페이지 상단의 **검색 창**에 *azure machine learning*을 입력하고 나타나는 옵션에서 **Azure Machine Learning**을 선택합니다.

    ![Type azure machine learning.](../../../../translated_images/01-01-type-azml.98b3003c07da4dbb6885400f66988b3ae05767edb5e8b8ef480e584abe379ca7.ko.png)

2. 탐색 메뉴에서 **+ 생성**을 선택합니다.

3. 탐색 메뉴에서 **새 작업 영역**을 선택합니다.

    ![Select new workspace.](../../../../translated_images/01-02-select-new-workspace.7648b384cbd786565740c0e5ea203d4710889d5ef23a2abf08428444f6d1a2a6.ko.png)

4. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다 (필요한 경우 새로 만듭니다).
    - **작업 영역 이름**을 입력합니다. 고유한 값이어야 합니다.
    - 사용할 **지역**을 선택합니다.
    - 사용할 **스토리지 계정**을 선택합니다 (필요한 경우 새로 만듭니다).
    - 사용할 **키 볼트**를 선택합니다 (필요한 경우 새로 만듭니다).
    - 사용할 **애플리케이션 인사이트**를 선택합니다 (필요한 경우 새로 만듭니다).
    - 사용할 **컨테이너 레지스트리**를 선택합니다 (필요한 경우 새로 만듭니다).

    ![Fill azure machine learning.](../../../../translated_images/01-03-fill-AZML.a3f644231a76859c7d92134b7dea1dd0d4df1c11cc615351c95be5a2c7056b03.ko.png)

5. **검토 + 생성**을 선택합니다.

6. **생성**을 선택합니다.

### Azure 구독에서 GPU 할당량 요청

이 튜토리얼에서는 GPU를 사용하여 Phi-3 모델을 미세 조정하고 배포하는 방법을 배웁니다. 미세 조정을 위해 *Standard_NC24ads_A100_v4* GPU를 사용하며, 이는 할당량 요청이 필요합니다. 배포를 위해 *Standard_NC6s_v3* GPU를 사용하며, 이 또한 할당량 요청이 필요합니다.

> [!NOTE]
>
> GPU 할당은 Pay-As-You-Go 구독(표준 구독 유형)만 가능합니다; 혜택 구독은 현재 지원되지 않습니다.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)를 방문합니다.

1. *Standard NCADSA100v4 Family* 할당량을 요청하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **할당량**을 선택합니다.
    - 사용할 **가상 머신 패밀리**를 선택합니다. 예를 들어, *Standard_NC24ads_A100_v4* GPU를 포함하는 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**를 선택합니다.
    - 탐색 메뉴에서 **할당량 요청**을 선택합니다.

        ![Request quota.](../../../../translated_images/02-02-request-quota.55f797113d95ad20ca91943eed637488d0aa51d61f3bbe7f080ec466b2ae0666.ko.png)

    - 할당량 요청 페이지에서 사용할 **새 코어 제한**을 입력합니다. 예를 들어, 24.
    - 할당량 요청 페이지에서 **제출**을 선택하여 GPU 할당량을 요청합니다.

1. *Standard NCSv3 Family* 할당량을 요청하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **할당량**을 선택합니다.
    - 사용할 **가상 머신 패밀리**를 선택합니다. 예를 들어, *Standard_NC6s_v3* GPU를 포함하는 **Standard NCSv3 Family Cluster Dedicated vCPUs**를 선택합니다.
    - 탐색 메뉴에서 **할당량 요청**을 선택합니다.
    - 할당량 요청 페이지에서 사용할 **새 코어 제한**을 입력합니다. 예를 들어, 24.
    - 할당량 요청 페이지에서 **제출**을 선택하여 GPU 할당량을 요청합니다.

### 역할 할당 추가

모델을 미세 조정하고 배포하려면 먼저 사용자 할당 관리 ID(UAI)를 생성하고 적절한 권한을 부여해야 합니다. 이 UAI는 배포 중 인증에 사용됩니다.

#### 사용자 할당 관리 ID(UAI) 생성

1. 포털 페이지 상단의 **검색 창**에 *managed identities*를 입력하고 나타나는 옵션에서 **Managed Identities**를 선택합니다.

    ![Type managed identities.](../../../../translated_images/03-01-type-managed-identities.2f7b07daa34dc15303b6a3f8c364bc0b7e892dd18aaff361440a030621b540b8.ko.png)

1. **+ 생성**을 선택합니다.

    ![Select create.](../../../../translated_images/03-02-select-create.0bde775b318f4adba24a7637b31f00f9b685214ed225c5123845a215a260ac71.ko.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다 (필요한 경우 새로 만듭니다).
    - 사용할 **지역**을 선택합니다.
    - **이름**을 입력합니다. 고유한 값이어야 합니다.

    ![Select create.](../../../../translated_images/03-03-fill-managed-identities-1.688009e629c1e6952853b94022d3fe97c659c34e29908db17218a5cab6d6add1.ko.png)

1. **검토 + 생성**을 선택합니다.

1. **+ 생성**을 선택합니다.

#### Managed Identity에 기여자 역할 할당 추가

1. 생성한 Managed Identity 리소스로 이동합니다.

1. 왼쪽 탭에서 **Azure 역할 할당**을 선택합니다.

1. 탐색 메뉴에서 **+ 역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:
    - **범위**를 **리소스 그룹**으로 설정합니다.
    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다.
    - **역할**을 **기여자**로 설정합니다.

    ![Fill contributor role.](../../../../translated_images/03-04-fill-contributor-role.8bc54b3ac8f64842c82b3379f3c3e9f8d778abf28c00e5b7b471935a86d3ae64.ko.png)

1. **저장**을 선택합니다.

#### Managed Identity에 Storage Blob Data Reader 역할 할당 추가

1. 포털 페이지 상단의 **검색 창**에 *storage accounts*를 입력하고 나타나는 옵션에서 **Storage accounts**를 선택합니다.

    ![Type storage accounts.](../../../../translated_images/03-05-type-storage-accounts.236987db35ba863124c6de8dd16533fe35b96ee4e2dcb9d67e6b279a285f0e6d.ko.png)

1. 생성한 Azure Machine Learning 작업 영역과 연관된 스토리지 계정을 선택합니다. 예를 들어, *finetunephistorage*.

1. 역할 할당 추가 페이지로 이동하려면 다음 작업을 수행합니다:

    - 생성한 Azure Storage 계정으로 이동합니다.
    - 왼쪽 탭에서 **액세스 제어 (IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - 탐색 메뉴에서 **역할 할당 추가**를 선택합니다.

    ![Add role.](../../../../translated_images/03-06-add-role.dde49177fe7ce1cd1604f620ca5c8ac6442fc516effb057e9f74645f35f9d038.ko.png)

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지에서 **검색 창**에 *Storage Blob Data Reader*를 입력하고 나타나는 옵션에서 **Storage Blob Data Reader**를 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 구성원 페이지에서 **액세스 할당 대상**을 **Managed identity**로 설정합니다.
    - 구성원 페이지에서 **+ 구성원 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 **Manage Identity**로 설정합니다.
    - 관리 ID 선택 페이지에서 생성한 Managed Identity를 선택합니다. 예를 들어, *finetunephi-managedidentity*.
    - 관리 ID 선택 페이지에서 **선택**을 선택합니다.

    ![Select managed identity.](../../../../translated_images/03-08-select-managed-identity.f9a44699bf247a4583e2d377e304de8c3d8a602b7d3fed52b9ae790e64e94fe9.ko.png)

1. **검토 + 할당**을 선택합니다.

#### Managed Identity에 AcrPull 역할 할당 추가

1. 포털 페이지 상단의 **검색 창**에 *container registries*를 입력하고 나타나는 옵션에서 **Container registries**를 선택합니다.

    ![Type container registries.](../../../../translated_images/03-09-type-container-registries.b5519f1fbf49bff0c0d4c95deecd2ef0c61b4870119886c3661014435e2b7095.ko.png)

1. Azure Machine Learning 작업 영역과 연관된 컨테이너 레지스트리를 선택합니다. 예를 들어, *finetunephicontainerregistry*.

1. 역할 할당 추가 페이지로 이동하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **액세스 제어 (IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - 탐색 메뉴에서 **역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지에서 **검색 창**에 *AcrPull*을 입력하고 나타나는 옵션에서 **AcrPull**을 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 구성원 페이지에서 **액세스 할당 대상**을 **Managed identity**로 설정합니다.
    - 구성원 페이지에서 **+ 구성원 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 **Manage Identity**로 설정합니다.
    - 관리 ID 선택 페이지에서 생성한 Managed Identity를 선택합니다. 예를 들어, *finetunephi-managedidentity*.
    - 관리 ID 선택 페이지에서 **선택**을 선택합니다.
    - **검토 + 할당**을 선택합니다.

### 프로젝트 설정

미세 조정을 위해 필요한 데이터셋을 다운로드하려면 로컬 환경을 설정해야 합니다.

이 연습에서는 다음을 수행합니다:

- 작업할 폴더를 생성합니다.
- 가상 환경을 생성합니다.
- 필요한 패키지를 설치합니다.
- 데이터셋을 다운로드하기 위한 *download_dataset.py* 파일을 생성합니다.

#### 작업할 폴더 생성

1. 터미널 창을 열고 기본 경로에 *finetune-phi* 폴더를 생성하려면 다음 명령을 입력합니다.

    ```console
    mkdir finetune-phi
    ```

2. 생성한 *finetune-phi* 폴더로 이동하려면 터미널에서 다음 명령을 입력합니다.

    ```console
    cd finetune-phi
    ```

#### 가상 환경 생성

1. 터미널에서 다음 명령을 입력하여 *.venv*라는 가상 환경을 생성합니다.

    ```console
    python -m venv .venv
    ```

2. 터미널에서 다음 명령을 입력하여 가상 환경을 활성화합니다.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 잘 작동하면 명령 프롬프트 앞에 *(.venv)*가 표시됩니다.

#### 필요한 패키지 설치

1. 터미널에서 다음 명령을 입력하여 필요한 패키지를 설치합니다.

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` 생성

> [!NOTE]
> 폴더 구조 전체:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**를 엽니다.

1. 메뉴 바에서 **파일**을 선택합니다.

1. **폴더 열기**를 선택합니다.

1. 생성한 *finetune-phi* 폴더를 선택합니다. 경로는 *C:\Users\yourUserName\finetune-phi*입니다.

    ![Select the folder that you created.](../../../../translated_images/04-01-open-project-folder.f5e2b4ce1cb596eae857303b12909dc0174fd99129d6944c41079f24ee17eed2.ko.png)

1. Visual Studio Code의 왼쪽 창에서 마우스 오른쪽 버튼을 클릭하고 **새 파일**을 선택하여 *download_dataset.py*라는 새 파일을 만듭니다.

    ![Create a new file.](../../../../translated_images/04-02-create-new-file.7c51fabe5e84788e34e43f951164471eb07df8363993ce69badc8908f1033613.ko.png)

### 미세 조정을 위한 데이터셋 준비

이 연습에서는 *download_dataset.py* 파일을 실행하여 *ultrachat_200k* 데이터셋을 로컬 환경에 다운로드합니다. 그런 다음 이 데이터셋을 사용하여 Azure Machine Learning에서 Phi-3 모델을 미세 조정합니다.

이 연습에서는 다음을 수행합니다:

- *download_dataset.py* 파일에 데이터셋을 다운로드하는 코드를 추가합니다.
- *download_dataset.py* 파일을 실행하여 로컬 환경에 데이터셋을 다운로드합니다.

#### *download_dataset.py*를 사용하여 데이터셋 다운로드

1. Visual Studio Code에서 *download_dataset.py* 파일을 엽니다.

1. *download_dataset.py* 파일에 다음 코드를 추가합니다.

    ```python
    import json
    import os
    from datasets import load_dataset

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
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 터미널에서 다음 명령을 입력하여 스크립트를 실행하고 로컬 환경에 데이터셋을 다운로드합니다.

    ```console
    python download_dataset.py
    ```

1. 데이터셋이 로컬 *finetune-phi/data* 디렉토리에 성공적으로 저장되었는지 확인합니다.

> [!NOTE]
>
> #### 데이터셋 크기 및 미세 조정 시간에 대한 참고 사항
>
> 이 튜토리얼에서는 데이터셋의 1%만 사용합니다 (`split='train[:1%]'`). 이는 데이터 양을 크게 줄여 업로드 및 미세 조정 과정을 빠르게 만듭니다. 데이터셋의 비율을 조정하여 훈련 시간과 모델 성능 간의 균형을 찾을 수 있습니다. 데이터셋의 작은 부분을 사용하면 미세 조정에 필요한 시간이 줄어들어 튜토리얼을 보다 관리하기 쉽게 만듭니다.

## 시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포

### Phi-3 모델 미세 조정

이 연습에서는 Azure Machine Learning Studio에서 Phi-3 모델을 미세 조정합니다.

이 연습에서는 다음을 수행합니다:

- 미세 조정을 위한 컴퓨터 클러스터를 생성합니다.
- Azure Machine Learning Studio에서 Phi-3 모델을 미세 조정합니다.

#### 미세 조정을 위한 컴퓨터 클러스터 생성
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 방문.

1. 왼쪽 탭에서 **Compute** 선택.

1. 탐색 메뉴에서 **Compute clusters** 선택.

1. **+ New** 선택.

    ![Select compute.](../../../../translated_images/06-01-select-compute.69422609cf19921fb16f550b2566e00870f63ba0caf66b0d26b34e6b0ed21a68.ko.png)

1. 다음 작업 수행:

    - 사용할 **Region** 선택.
    - **Virtual machine tier**를 **Dedicated**로 선택.
    - **Virtual machine type**를 **GPU**로 선택.
    - **Virtual machine size** 필터를 **Select from all options**로 선택.
    - **Virtual machine size**를 **Standard_NC24ads_A100_v4**로 선택.

    ![Create cluster.](../../../../translated_images/06-02-create-cluster.ad68bcb0914b62972408da8f925632977c54248ff99d2c45761f7e3d33f40fe1.ko.png)

1. **Next** 선택.

1. 다음 작업 수행:

    - **Compute name** 입력. 고유한 값이어야 함.
    - **Minimum number of nodes**를 **0**으로 선택.
    - **Maximum number of nodes**를 **1**로 선택.
    - **Idle seconds before scale down**를 **120**으로 선택.

    ![Create cluster.](../../../../translated_images/06-03-create-cluster.f36399780462ff69f62b9bdf22180d6824b00cdc913fe2a639dde3e4b9eaa43e.ko.png)

1. **Create** 선택.

#### Phi-3 모델 미세 조정

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 방문.

1. 생성한 Azure Machine Learning 작업 공간 선택.

    ![Select workspace that you created.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.ko.png)

1. 다음 작업 수행:

    - 왼쪽 탭에서 **Model catalog** 선택.
    - **검색창**에 *phi-3-mini-4k* 입력 후 나타나는 옵션에서 **Phi-3-mini-4k-instruct** 선택.

    ![Type phi-3-mini-4k.](../../../../translated_images/06-05-type-phi-3-mini-4k.7461addd95ede137f6f018a29681762f85e063477ded6043aafbdf6d742a54e8.ko.png)

1. 탐색 메뉴에서 **Fine-tune** 선택.

    ![Select fine tune.](../../../../translated_images/06-06-select-fine-tune.2c678a7f33294c16ae3ad30ce5d4a78600013dc3a0227e8d341a1962f3aff84d.ko.png)

1. 다음 작업 수행:

    - **Select task type**를 **Chat completion**으로 선택.
    - **+ Select data**를 선택하여 **Training data** 업로드.
    - 검증 데이터 업로드 유형을 **Provide different validation data**로 선택.
    - **+ Select data**를 선택하여 **Validation data** 업로드.

    ![Fill fine-tuning page.](../../../../translated_images/06-07-fill-finetuning.c76431cc247b6398fb9d33da62841adf87d5eebaa92cd79e80bd7bcbed49f1d3.ko.png)

    > [!TIP]
    >
    > **Advanced settings**를 선택하여 **learning_rate** 및 **lr_scheduler_type**과 같은 설정을 조정하여 미세 조정 프로세스를 최적화할 수 있습니다.

1. **Finish** 선택.

1. 이번 실습에서는 Azure Machine Learning을 사용하여 Phi-3 모델을 성공적으로 미세 조정했습니다. 미세 조정 작업이 완료되기까지 시간이 걸릴 수 있습니다. 미세 조정 작업을 실행한 후 완료될 때까지 기다려야 합니다. 작업 공간의 왼쪽 탭에서 Jobs 탭으로 이동하여 미세 조정 작업의 상태를 모니터링할 수 있습니다. 다음 단계에서는 미세 조정된 모델을 배포하고 Prompt flow와 통합할 것입니다.

    ![See finetuning job.](../../../../translated_images/06-08-output.9f9cf6f9e9e83533b793a5ff3066b09475e299999fead6f98dfb102f48db0061.ko.png)

### 미세 조정된 Phi-3 모델 배포

미세 조정된 Phi-3 모델을 Prompt flow와 통합하려면 실시간 추론을 위해 모델을 배포해야 합니다. 이 과정에는 모델 등록, 온라인 엔드포인트 생성, 모델 배포가 포함됩니다.

이번 실습에서는 다음을 수행합니다:

- Azure Machine Learning 작업 공간에 미세 조정된 모델 등록.
- 온라인 엔드포인트 생성.
- 등록된 미세 조정된 Phi-3 모델 배포.

#### 미세 조정된 모델 등록

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 방문.

1. 생성한 Azure Machine Learning 작업 공간 선택.

    ![Select workspace that you created.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.ko.png)

1. 왼쪽 탭에서 **Models** 선택.
1. **+ Register** 선택.
1. **From a job output** 선택.

    ![Register model.](../../../../translated_images/07-01-register-model.9b64d29736e0be32343b36a503d7e38c47c22d9edfa554aae179352982fdf96b.ko.png)

1. 생성한 작업 선택.

    ![Select job.](../../../../translated_images/07-02-select-job.712abf18cdae5256776907df3ed30df53d297ff8d475fb64d5c03e92304db6ef.ko.png)

1. **Next** 선택.

1. **Model type**을 **MLflow**로 선택.

1. **Job output**이 선택된 상태인지 확인; 자동으로 선택되어 있어야 합니다.

    ![Select output.](../../../../translated_images/07-03-select-output.45098161b7ddfda4b8d4d62676da0488a32a16e838ff03f37bfd71b9886da798.ko.png)

1. **Next** 선택.

1. **Register** 선택.

    ![Select register.](../../../../translated_images/07-04-register.3403ed7976f07fbfc27210550cf2f793d9cf778032ea276ecb287bd9df88f188.ko.png)

1. 왼쪽 탭에서 **Models** 메뉴로 이동하여 등록된 모델을 확인할 수 있습니다.

    ![Registered model.](../../../../translated_images/07-05-registered-model.90693749513e55231e8904304e4ea1f9e29ab659bc1926ea69dffd25e77ffb2d.ko.png)

#### 미세 조정된 모델 배포

1. 생성한 Azure Machine Learning 작업 공간으로 이동.

1. 왼쪽 탭에서 **Endpoints** 선택.

1. 탐색 메뉴에서 **Real-time endpoints** 선택.

    ![Create endpoint.](../../../../translated_images/07-06-create-endpoint.28687e4d01bffed741bf461bbb36ceef441ed5d049ca5d091aab511ced67a804.ko.png)

1. **Create** 선택.

1. 생성한 등록된 모델 선택.

    ![Select registered model.](../../../../translated_images/07-07-select-registered-model.5190ae13400cc09a6410f891a62e6b2ccc2c2bd7f419b0df4ea964731e72407f.ko.png)

1. **Select** 선택.

1. 다음 작업 수행:

    - **Virtual machine**을 *Standard_NC6s_v3*로 선택.
    - 사용할 **Instance count** 선택. 예: *1*.
    - **Endpoint**를 **New**로 선택하여 엔드포인트 생성.
    - **Endpoint name** 입력. 고유한 값이어야 함.
    - **Deployment name** 입력. 고유한 값이어야 함.

    ![Fill the deployment setting.](../../../../translated_images/07-08-deployment-setting.5449edf53b27f5457cc68d2285d355a7d364b01423a51e5af63e7c52374a3a79.ko.png)

1. **Deploy** 선택.

> [!WARNING]
> 추가 요금을 방지하기 위해 Azure Machine Learning 작업 공간에서 생성된 엔드포인트를 삭제하십시오.
>

#### Azure Machine Learning 작업 공간에서 배포 상태 확인

1. 생성한 Azure Machine Learning 작업 공간으로 이동.

1. 왼쪽 탭에서 **Endpoints** 선택.

1. 생성한 엔드포인트 선택.

    ![Select endpoints](../../../../translated_images/07-09-check-deployment.8e4465a7585b3c22db5fc9d5757269a919b5104fdeb5f736fa573ca9b3e16abe.ko.png)

1. 이 페이지에서 배포 과정 동안 엔드포인트를 관리할 수 있습니다.

> [!NOTE]
> 배포가 완료되면 **Live traffic**이 **100%**로 설정되어 있는지 확인하십시오. 그렇지 않은 경우 **Update traffic**을 선택하여 트래픽 설정을 조정하십시오. 트래픽이 0%로 설정되어 있으면 모델을 테스트할 수 없습니다.
>
> ![Set traffic.](../../../../translated_images/07-10-set-traffic.1d1b24b39c7ec80451c99fe05298fac636f0cd449e7be282736f6c06a1a70875.ko.png)
>

## 시나리오 3: Prompt flow와 통합하여 Azure AI Studio에서 사용자 정의 모델과 채팅하기

### 사용자 정의 Phi-3 모델을 Prompt flow와 통합

미세 조정된 모델을 성공적으로 배포한 후, 이제 Prompt Flow와 통합하여 실시간 애플리케이션에서 모델을 사용할 수 있습니다. 이를 통해 사용자 정의 Phi-3 모델과 다양한 상호작용 작업을 수행할 수 있습니다.

이번 실습에서는 다음을 수행합니다:

- Azure AI Studio Hub 생성.
- Azure AI Studio 프로젝트 생성.
- Prompt flow 생성.
- 미세 조정된 Phi-3 모델에 대한 사용자 정의 연결 추가.
- 사용자 정의 Phi-3 모델과 채팅할 수 있도록 Prompt flow 설정.

> [!NOTE]
> Azure ML Studio를 사용하여 Promptflow와 통합할 수도 있습니다. 동일한 통합 프로세스가 Azure ML Studio에 적용될 수 있습니다.

#### Azure AI Studio Hub 생성

프로젝트를 생성하기 전에 Hub를 생성해야 합니다. Hub는 Resource Group과 유사하게 여러 프로젝트를 조직하고 관리할 수 있는 역할을 합니다.

1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 방문.

1. 왼쪽 탭에서 **All hubs** 선택.

1. 탐색 메뉴에서 **+ New hub** 선택.

    ![Create hub.](../../../../translated_images/08-01-create-hub.1df80696bf3376f0e56ffa90de1fc35962acf2fc3c1a3a6b254015b8b993e55e.ko.png)

1. 다음 작업 수행:

    - **Hub name** 입력. 고유한 값이어야 함.
    - Azure **Subscription** 선택.
    - 사용할 **Resource group** 선택 (필요 시 새로 생성).
    - 사용할 **Location** 선택.
    - 사용할 **Connect Azure AI Services** 선택 (필요 시 새로 생성).
    - **Connect Azure AI Search**를 **Skip connecting**으로 선택.

    ![Fill hub.](../../../../translated_images/08-02-fill-hub.fc194526614a5811e7b57e699911be39babdc95aa425b6c4a72f064948865ce3.ko.png)

1. **Next** 선택.

#### Azure AI Studio 프로젝트 생성

1. 생성한 Hub에서 왼쪽 탭에서 **All projects** 선택.

1. 탐색 메뉴에서 **+ New project** 선택.

    ![Select new project.](../../../../translated_images/08-04-select-new-project.dc11f26658c3c3f9d0fcf3232a954abfc115de5eb74da21d5be229c9c1be2875.ko.png)

1. **Project name** 입력. 고유한 값이어야 함.

    ![Create project.](../../../../translated_images/08-05-create-project.61caaa28c1b9b696bf29de6b002bbb2040dbaeb764adab161dcb3472fe789aea.ko.png)

1. **Create a project** 선택.

#### 미세 조정된 Phi-3 모델에 대한 사용자 정의 연결 추가

사용자 정의 Phi-3 모델을 Prompt flow와 통합하려면 모델의 엔드포인트와 키를 사용자 정의 연결에 저장해야 합니다. 이를 통해 Prompt flow에서 사용자 정의 Phi-3 모델에 접근할 수 있습니다.

#### 미세 조정된 Phi-3 모델의 API 키와 엔드포인트 URI 설정

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) 방문.

1. 생성한 Azure Machine learning 작업 공간으로 이동.

1. 왼쪽 탭에서 **Endpoints** 선택.

    ![Select endpoints.](../../../../translated_images/08-06-select-endpoints.75d3bdd7f0b17da0367370d1293f7e7f7b2a65fb7e17390997be0460e8f0b82b.ko.png)

1. 생성한 엔드포인트 선택.

    ![Select endpoints.](../../../../translated_images/08-07-select-endpoint-created.851b32efc6058e5863aa62ae8d576a6c20792e24f1862dc6857b9f24a2949f96.ko.png)

1. 탐색 메뉴에서 **Consume** 선택.

1. **REST endpoint**와 **Primary key** 복사.
![Copy api key and endpoint uri.](../../../../translated_images/08-08-copy-endpoint-key.947512a4c95b5dd9fc5a606bad4244bf9b136929c1fab06570c463311ef29df1.ko.png)

#### 사용자 정의 연결 추가

1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)를 방문합니다.

1. 생성한 Azure AI Studio 프로젝트로 이동합니다.

1. 생성한 프로젝트에서 왼쪽 탭에서 **Settings**를 선택합니다.

1. **+ New connection**을 선택합니다.

    ![새 연결 선택.](../../../../translated_images/08-09-select-new-connection.b5e93c85028739875916f34a1821b0b086f0e993b8d7d7388c100e3a38b70bbd.ko.png)

1. 네비게이션 메뉴에서 **Custom keys**를 선택합니다.

    ![사용자 정의 키 선택.](../../../../translated_images/08-10-select-custom-keys.077f17a1a49b8f76e446453b6a68c09c2aa08291818d98edcf39e3013c5b45ac.ko.png)

1. 다음 작업을 수행합니다:

    - **+ Add key value pairs**를 선택합니다.
    - 키 이름에 **endpoint**를 입력하고 Azure ML Studio에서 복사한 endpoint를 값 필드에 붙여넣습니다.
    - **+ Add key value pairs**를 다시 선택합니다.
    - 키 이름에 **key**를 입력하고 Azure ML Studio에서 복사한 키를 값 필드에 붙여넣습니다.
    - 키를 추가한 후 **is secret**을 선택하여 키가 노출되지 않도록 합니다.

    ![연결 추가.](../../../../translated_images/08-11-add-connection.01279deb77ede4d195b17ecabae70979976834892e9dbb3354f504bb6edaa6e1.ko.png)

1. **Add connection**을 선택합니다.

#### 프롬프트 플로우 생성

Azure AI Studio에 사용자 정의 연결을 추가했습니다. 이제 다음 단계를 따라 프롬프트 플로우를 생성해 보겠습니다. 그런 다음, 이 프롬프트 플로우를 사용자 정의 연결에 연결하여 프롬프트 플로우 내에서 미세 조정된 모델을 사용할 수 있도록 할 것입니다.

1. 생성한 Azure AI Studio 프로젝트로 이동합니다.

1. 왼쪽 탭에서 **Prompt flow**를 선택합니다.

1. 네비게이션 메뉴에서 **+ Create**를 선택합니다.

    ![프롬프트 플로우 선택.](../../../../translated_images/08-12-select-promptflow.5e0527f1e5102c604e0e8a34f2321e28f8c815ec2908ae7038f012a088ff2bbc.ko.png)

1. 네비게이션 메뉴에서 **Chat flow**를 선택합니다.

    ![채팅 플로우 선택.](../../../../translated_images/08-13-select-flow-type.e3fb41375041faa4d058304c319329d5f45f87139143b384f056bb500076ca73.ko.png)

1. 사용할 **Folder name**을 입력합니다.

    ![이름 입력.](../../../../translated_images/08-14-enter-name.90db481f18468cfd78b281825cb5484ab7236cfa29d59d287b7b0f423516e6ea.ko.png)

1. **Create**를 선택합니다.

#### 사용자 정의 Phi-3 모델과 채팅하는 프롬프트 플로우 설정

미세 조정된 Phi-3 모델을 프롬프트 플로우에 통합해야 합니다. 그러나 제공된 기존 프롬프트 플로우는 이 목적에 맞게 설계되지 않았습니다. 따라서 사용자 정의 모델 통합을 가능하게 하려면 프롬프트 플로우를 재설계해야 합니다.

1. 프롬프트 플로우에서 다음 작업을 수행하여 기존 플로우를 재구성합니다:

    - **Raw file mode**를 선택합니다.
    - *flow.dag.yml* 파일의 기존 코드를 모두 삭제합니다.
    - 다음 코드를 *flow.dag.yml* 파일에 추가합니다.

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

    - **Save**를 선택합니다.

    ![원시 파일 모드 선택.](../../../../translated_images/08-15-select-raw-file-mode.28d80142df9d540c66c37d17825cec921bb1f7b54e386223bb4ad38df10e5e2d.ko.png)

1. 프롬프트 플로우에서 사용자 정의 Phi-3 모델을 사용하기 위해 *integrate_with_promptflow.py* 파일에 다음 코드를 추가합니다.

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

    ![프롬프트 플로우 코드 붙여넣기.](../../../../translated_images/08-16-paste-promptflow-code.c27a93ed6134adbe7ce618ffad7300923f3c02defedef0b5598eab5a6ee2afc2.ko.png)

> [!NOTE]
> Azure AI Studio에서 프롬프트 플로우 사용에 대한 자세한 정보는 [Azure AI Studio에서 프롬프트 플로우](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)를 참조하세요.

1. **Chat input**, **Chat output**을 선택하여 모델과 채팅을 활성화합니다.

    ![입력 출력.](../../../../translated_images/08-17-select-input-output.d188ea79fc21d29e615b6cc50d638214a2dcbc3b3ccb16009aa67698227d2765.ko.png)

1. 이제 사용자 정의 Phi-3 모델과 채팅할 준비가 되었습니다. 다음 실습에서는 프롬프트 플로우를 시작하고 미세 조정된 Phi-3 모델과 채팅하는 방법을 배우게 됩니다.

> [!NOTE]
>
> 재구성된 플로우는 아래 이미지와 같아야 합니다:
>
> ![플로우 예시.](../../../../translated_images/08-18-graph-example.48c427864370ac7dd02e500bc3a0ff49785d4480e489b4dfe25e529da99f193f.ko.png)
>

### 사용자 정의 Phi-3 모델과 채팅하기

이제 사용자 정의 Phi-3 모델을 미세 조정하고 프롬프트 플로우와 통합했으므로, 모델과 상호작용을 시작할 준비가 되었습니다. 이 실습에서는 프롬프트 플로우를 사용하여 모델과 채팅을 설정하고 시작하는 과정을 안내합니다. 이 단계를 따르면, 다양한 작업과 대화에서 미세 조정된 Phi-3 모델의 기능을 완전히 활용할 수 있습니다.

- 프롬프트 플로우를 사용하여 사용자 정의 Phi-3 모델과 채팅합니다.

#### 프롬프트 플로우 시작

1. 프롬프트 플로우를 시작하려면 **Start compute sessions**을 선택합니다.

    ![컴퓨팅 세션 시작.](../../../../translated_images/09-01-start-compute-session.9d080c30a6fc78a8b23ac54e7c8b11aeecc005d3da03cb0f9bd8afc298151ffa.ko.png)

1. 매개변수를 갱신하려면 **Validate and parse input**을 선택합니다.

    ![입력 유효성 검사.](../../../../translated_images/09-02-validate-input.db05a40e29a21b333848b7c03542b0ec521ce9c6fbe12fba51c2addcb1c07c68.ko.png)

1. 생성한 사용자 정의 연결의 **connection**의 **Value**를 선택합니다. 예를 들어, *connection*.

    ![연결.](../../../../translated_images/09-03-select-connection.de0137da33c86e581425cef4a25957d86140d1605968f6f7c98207b8e715cca8.ko.png)

#### 사용자 정의 모델과 채팅하기

1. **Chat**을 선택합니다.

    ![채팅 선택.](../../../../translated_images/09-04-select-chat.87b90a2f41e38714f40dedde608d349bfaca00a75f08166816dddb92de711e32.ko.png)

1. 다음은 결과 예시입니다: 이제 사용자 정의 Phi-3 모델과 채팅할 수 있습니다. 미세 조정에 사용된 데이터를 기반으로 질문하는 것이 좋습니다.

    ![프롬프트 플로우와 채팅.](../../../../translated_images/09-05-chat-with-promptflow.46c9fdf0e6de0e15e9618f654830e52bd8ead4aec0de57bb960206321d2bd0bd.ko.png)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.