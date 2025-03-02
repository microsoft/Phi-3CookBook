# Tinh chỉnh và tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow trong Azure AI Foundry

Ví dụ end-to-end (E2E) này dựa trên hướng dẫn "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" từ cộng đồng công nghệ Microsoft. Hướng dẫn này giới thiệu các quy trình tinh chỉnh, triển khai và tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow trong Azure AI Foundry.  
Không giống như ví dụ E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", vốn chạy mã cục bộ, hướng dẫn này tập trung hoàn toàn vào việc tinh chỉnh và tích hợp mô hình của bạn trong Azure AI / ML Studio.

## Tổng quan

Trong ví dụ E2E này, bạn sẽ học cách tinh chỉnh mô hình Phi-3 và tích hợp nó với Prompt flow trong Azure AI Foundry. Bằng cách tận dụng Azure AI / ML Studio, bạn sẽ xây dựng một quy trình làm việc để triển khai và sử dụng các mô hình AI tùy chỉnh. Ví dụ E2E này được chia thành ba kịch bản:

**Kịch bản 1: Thiết lập tài nguyên Azure và chuẩn bị cho tinh chỉnh**

**Kịch bản 2: Tinh chỉnh mô hình Phi-3 và triển khai trong Azure Machine Learning Studio**

**Kịch bản 3: Tích hợp với Prompt flow và trò chuyện với mô hình tùy chỉnh của bạn trong Azure AI Foundry**

Dưới đây là tổng quan về ví dụ E2E này.

![Tổng quan về Phi-3-FineTuning_PromptFlow_Integration.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.vi.png)

### Mục lục

1. **[Kịch bản 1: Thiết lập tài nguyên Azure và chuẩn bị cho tinh chỉnh](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Tạo Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Yêu cầu GPU quotas trong Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Thêm role assignment](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Thiết lập dự án](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chuẩn bị dataset cho tinh chỉnh](../../../../../../md/02.Application/01.TextAndChat/Phi3)

2. **[Kịch bản 2: Tinh chỉnh mô hình Phi-3 và triển khai trong Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Tinh chỉnh mô hình Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Triển khai mô hình Phi-3 đã tinh chỉnh](../../../../../../md/02.Application/01.TextAndChat/Phi3)

3. **[Kịch bản 3: Tích hợp với Prompt flow và trò chuyện với mô hình tùy chỉnh của bạn trong Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Trò chuyện với mô hình Phi-3 tùy chỉnh của bạn](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Kịch bản 1: Thiết lập tài nguyên Azure và chuẩn bị cho tinh chỉnh

### Tạo Azure Machine Learning Workspace

1. Gõ *azure machine learning* vào **thanh tìm kiếm** ở đầu trang portal và chọn **Azure Machine Learning** từ các tùy chọn hiện ra.

    ![Gõ azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.vi.png)

2. Chọn **+ Create** từ menu điều hướng.

3. Chọn **New workspace** từ menu điều hướng.

    ![Chọn new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.vi.png)

4. Thực hiện các bước sau:

    - Chọn **Subscription** của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Nhập **Workspace Name**. Tên này phải là giá trị duy nhất.
    - Chọn **Region** bạn muốn sử dụng.
    - Chọn **Storage account** để sử dụng (tạo mới nếu cần).
    - Chọn **Key vault** để sử dụng (tạo mới nếu cần).
    - Chọn **Application insights** để sử dụng (tạo mới nếu cần).
    - Chọn **Container registry** để sử dụng (tạo mới nếu cần).

    ![Điền thông tin azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.vi.png)

5. Chọn **Review + Create**.

6. Chọn **Create**.

### Yêu cầu GPU quotas trong Azure Subscription

Trong hướng dẫn này, bạn sẽ học cách tinh chỉnh và triển khai mô hình Phi-3, sử dụng GPU. Để tinh chỉnh, bạn sẽ sử dụng GPU *Standard_NC24ads_A100_v4*, yêu cầu gửi yêu cầu quota. Để triển khai, bạn sẽ sử dụng GPU *Standard_NC6s_v3*, cũng yêu cầu gửi yêu cầu quota.

> [!NOTE]
>
> Chỉ các subscription loại Pay-As-You-Go (loại subscription tiêu chuẩn) đủ điều kiện để phân bổ GPU; các subscription có lợi ích không được hỗ trợ hiện tại.
>

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

2. Thực hiện các bước sau để yêu cầu quota *Standard NCADSA100v4 Family*:

    - Chọn **Quota** từ thanh điều hướng bên trái.
    - Chọn **Virtual machine family** để sử dụng. Ví dụ, chọn **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, bao gồm GPU *Standard_NC24ads_A100_v4*.
    - Chọn **Request quota** từ menu điều hướng.

        ![Yêu cầu quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.vi.png)

    - Trong trang Request quota, nhập **New cores limit** bạn muốn sử dụng. Ví dụ, 24.
    - Trong trang Request quota, chọn **Submit** để yêu cầu GPU quota.

3. Thực hiện các bước sau để yêu cầu quota *Standard NCSv3 Family*:

    - Chọn **Quota** từ thanh điều hướng bên trái.
    - Chọn **Virtual machine family** để sử dụng. Ví dụ, chọn **Standard NCSv3 Family Cluster Dedicated vCPUs**, bao gồm GPU *Standard_NC6s_v3*.
    - Chọn **Request quota** từ menu điều hướng.
    - Trong trang Request quota, nhập **New cores limit** bạn muốn sử dụng. Ví dụ, 24.
    - Trong trang Request quota, chọn **Submit** để yêu cầu GPU quota.

### Thêm role assignment

Để tinh chỉnh và triển khai mô hình của bạn, trước tiên bạn phải tạo một User Assigned Managed Identity (UAI) và gán quyền phù hợp. UAI này sẽ được sử dụng để xác thực trong quá trình triển khai.

#### Tạo User Assigned Managed Identity (UAI)

1. Gõ *managed identities* vào **thanh tìm kiếm** ở đầu trang portal và chọn **Managed Identities** từ các tùy chọn hiện ra.

    ![Gõ managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.vi.png)

2. Chọn **+ Create**.

    ![Chọn create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.vi.png)

3. Thực hiện các bước sau:

    - Chọn **Subscription** của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Region** bạn muốn sử dụng.
    - Nhập **Name**. Tên này phải là giá trị duy nhất.

    ![Chọn create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.vi.png)

4. Chọn **Review + create**.

5. Chọn **+ Create**.

#### Thêm quyền Contributor vào Managed Identity

1. Điều hướng đến tài nguyên Managed Identity mà bạn đã tạo.

2. Chọn **Azure role assignments** từ thanh điều hướng bên trái.

3. Chọn **+Add role assignment** từ menu điều hướng.

4. Trong trang Add role assignment, thực hiện các bước sau:
    - Chọn **Scope** là **Resource group**.
    - Chọn **Subscription** của bạn.
    - Chọn **Resource group** để sử dụng.
    - Chọn **Role** là **Contributor**.

    ![Điền quyền contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.vi.png)

5. Chọn **Save**.

#### Thêm quyền Storage Blob Data Reader vào Managed Identity

1. Gõ *storage accounts* vào **thanh tìm kiếm** ở đầu trang portal và chọn **Storage accounts** từ các tùy chọn hiện ra.

    ![Gõ storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.vi.png)

2. Chọn tài khoản lưu trữ được liên kết với Azure Machine Learning workspace mà bạn đã tạo. Ví dụ, *finetunephistorage*.

3. Thực hiện các bước sau để điều hướng đến trang Add role assignment:

    - Điều hướng đến tài khoản lưu trữ Azure mà bạn đã tạo.
    - Chọn **Access Control (IAM)** từ thanh điều hướng bên trái.
    - Chọn **+ Add** từ menu điều hướng.
    - Chọn **Add role assignment** từ menu điều hướng.

    ![Thêm quyền.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.vi.png)

4. Trong trang Add role assignment, thực hiện các bước sau:

    - Trong trang Role, gõ *Storage Blob Data Reader* vào **thanh tìm kiếm** và chọn **Storage Blob Data Reader** từ các tùy chọn hiện ra.
    - Trong trang Role, chọn **Next**.
    - Trong trang Members, chọn **Assign access to** **Managed identity**.
    - Trong trang Members, chọn **+ Select members**.
    - Trong trang Select managed identities, chọn **Subscription** của bạn.
    - Trong trang Select managed identities, chọn **Managed identity** là **Manage Identity**.
    - Trong trang Select managed identities, chọn Managed Identity mà bạn đã tạo. Ví dụ, *finetunephi-managedidentity*.
    - Trong trang Select managed identities, chọn **Select**.

    ![Chọn managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.vi.png)

5. Chọn **Review + assign**.

#### Thêm quyền AcrPull vào Managed Identity

1. Gõ *container registries* vào **thanh tìm kiếm** ở đầu trang portal và chọn **Container registries** từ các tùy chọn hiện ra.

    ![Gõ container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.vi.png)

2. Chọn container registry được liên kết với Azure Machine Learning workspace. Ví dụ, *finetunephicontainerregistry*.

3. Thực hiện các bước sau để điều hướng đến trang Add role assignment:

    - Chọn **Access Control (IAM)** từ thanh điều hướng bên trái.
    - Chọn **+ Add** từ menu điều hướng.
    - Chọn **Add role assignment** từ menu điều hướng.

4. Trong trang Add role assignment, thực hiện các bước sau:

    - Trong trang Role, gõ *AcrPull* vào **thanh tìm kiếm** và chọn **AcrPull** từ các tùy chọn hiện ra.
    - Trong trang Role, chọn **Next**.
    - Trong trang Members, chọn **Assign access to** **Managed identity**.
    - Trong trang Members, chọn **+ Select members**.
    - Trong trang Select managed identities, chọn **Subscription** của bạn.
    - Trong trang Select managed identities, chọn **Managed identity** là **Manage Identity**.
    - Trong trang Select managed identities, chọn Managed Identity mà bạn đã tạo. Ví dụ, *finetunephi-managedidentity*.
    - Trong trang Select managed identities, chọn **Select**.
    - Chọn **Review + assign**.

### Thiết lập dự án

Để tải xuống dataset cần thiết cho việc tinh chỉnh, bạn sẽ thiết lập môi trường cục bộ.

Trong bài tập này, bạn sẽ:

- Tạo một thư mục để làm việc bên trong.
- Tạo một môi trường ảo.
- Cài đặt các gói cần thiết.
- Tạo tệp *download_dataset.py* để tải dataset.

#### Tạo thư mục để làm việc bên trong

1. Mở cửa sổ terminal và gõ lệnh sau để tạo thư mục tên *finetune-phi* trong đường dẫn mặc định.

    ```console
    mkdir finetune-phi
    ```

2. Gõ lệnh sau trong terminal để chuyển đến thư mục *finetune-phi* mà bạn đã tạo.

    ```console
    cd finetune-phi
    ```

#### Tạo môi trường ảo

1. Gõ lệnh sau trong terminal để tạo môi trường ảo tên *.venv*.

    ```console
    python -m venv .venv
    ```

2. Gõ lệnh sau trong terminal để kích hoạt môi trường ảo.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Nếu thành công, bạn sẽ thấy *(.venv)* xuất hiện trước dấu nhắc lệnh.

#### Cài đặt các gói cần thiết

1. Gõ các lệnh sau trong terminal để cài đặt các gói cần thiết.

    ```console
    pip install datasets==2.19.1
    ```

#### Tạo `download_dataset.py`

> [!NOTE]
> Cấu trúc thư mục hoàn chỉnh:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Mở **Visual Studio Code**.

2. Chọn **File** từ thanh menu.

3. Chọn **Open Folder**.

4. Chọn thư mục *finetune-phi* mà bạn đã tạo, nằm tại *C:\Users\yourUserName\finetune-phi*.

    ![Chọn thư mục bạn đã tạo.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.vi.png)

5. Trong khung bên trái của Visual Studio Code, nhấp chuột phải và chọn **New File** để tạo tệp mới tên *download_dataset.py*.

    ![Tạo tệp mới.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.vi.png)

### Chuẩn bị dataset cho tinh chỉnh

Trong bài tập này, bạn sẽ chạy tệp *download_dataset.py* để tải dataset *ultrachat_200k* về môi trường cục bộ. Bạn sẽ sử dụng dataset này để tinh chỉnh mô hình Phi-3 trong Azure Machine Learning.

Trong bài tập này, bạn sẽ:

- Thêm mã vào tệp *download_dataset.py* để tải dataset.
- Chạy tệp *download_dataset.py* để tải dataset về môi trường cục bộ.

#### Tải dataset bằng *download_dataset.py*

1. Mở tệp *download_dataset.py* trong Visual Studio Code.

2. Thêm mã sau vào tệp *download_dataset.py*.

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

3. Gõ lệnh sau trong terminal để chạy script và tải dataset về môi trường cục bộ.

    ```console
    python download_dataset.py
    ```

4. Kiểm tra xem dataset đã được lưu thành công vào thư mục *finetune-phi/data* trên máy cục bộ của bạn.

> [!NOTE]
>
> #### Lưu ý về kích thước dataset và thời gian tinh chỉnh
>
> Trong hướng dẫn này, bạn chỉ sử dụng 1% dataset (`split='train[:1%]'`). Điều này giúp giảm đáng kể lượng dữ liệu, tăng tốc quá trình tải lên và tinh chỉnh. Bạn có thể điều chỉnh tỷ lệ phần trăm để cân bằng giữa thời gian huấn luyện và hiệu suất mô hình. Sử dụng một phần nhỏ dataset giúp rút ngắn thời gian tinh chỉnh, làm cho quy trình dễ quản lý hơn trong một hướng dẫn.

## Kịch bản 2: Tinh chỉnh mô hình Phi-3 và triển khai trong Azure Machine Learning Studio

### Tinh chỉnh mô hình Phi-3

Trong bài tập này, bạn sẽ tinh chỉnh mô hình Phi-3 trong Azure Machine Learning Studio.

Trong bài tập này, bạn sẽ:

- Tạo computer cluster cho tinh chỉnh.
- Tinh chỉnh mô hình Phi-3 trong Azure Machine Learning Studio.

#### Tạo computer cluster cho tinh chỉnh
1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chọn **Compute** từ thanh tab bên trái.

1. Chọn **Compute clusters** từ menu điều hướng.

1. Chọn **+ New**.

    ![Chọn compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.vi.png)

1. Thực hiện các tác vụ sau:

    - Chọn **Region** mà bạn muốn sử dụng.
    - Chọn **Virtual machine tier** thành **Dedicated**.
    - Chọn **Virtual machine type** thành **GPU**.
    - Chọn bộ lọc **Virtual machine size** thành **Select from all options**.
    - Chọn **Virtual machine size** thành **Standard_NC24ads_A100_v4**.

    ![Tạo cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.vi.png)

1. Chọn **Next**.

1. Thực hiện các tác vụ sau:

    - Nhập **Compute name**. Giá trị này phải là duy nhất.
    - Chọn **Minimum number of nodes** thành **0**.
    - Chọn **Maximum number of nodes** thành **1**.
    - Chọn **Idle seconds before scale down** thành **120**.

    ![Tạo cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.vi.png)

1. Chọn **Create**.

#### Tinh chỉnh mô hình Phi-3

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chọn không gian làm việc Azure Machine Learning mà bạn đã tạo.

    ![Chọn workspace mà bạn đã tạo.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.vi.png)

1. Thực hiện các tác vụ sau:

    - Chọn **Model catalog** từ thanh tab bên trái.
    - Nhập *phi-3-mini-4k* vào **thanh tìm kiếm** và chọn **Phi-3-mini-4k-instruct** từ các tùy chọn xuất hiện.

    ![Nhập phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.vi.png)

1. Chọn **Fine-tune** từ menu điều hướng.

    ![Chọn fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.vi.png)

1. Thực hiện các tác vụ sau:

    - Chọn **Select task type** thành **Chat completion**.
    - Chọn **+ Select data** để tải lên **Training data**.
    - Chọn loại tải lên Validation data thành **Provide different validation data**.
    - Chọn **+ Select data** để tải lên **Validation data**.

    ![Điền trang fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.vi.png)

    > [!TIP]
    >
    > Bạn có thể chọn **Advanced settings** để tùy chỉnh các cấu hình như **learning_rate** và **lr_scheduler_type** để tối ưu hóa quá trình tinh chỉnh theo nhu cầu cụ thể của bạn.

1. Chọn **Finish**.

1. Trong bài tập này, bạn đã tinh chỉnh thành công mô hình Phi-3 bằng Azure Machine Learning. Lưu ý rằng quá trình tinh chỉnh có thể mất khá nhiều thời gian. Sau khi chạy công việc tinh chỉnh, bạn cần đợi nó hoàn thành. Bạn có thể theo dõi trạng thái công việc tinh chỉnh bằng cách điều hướng đến tab Jobs trong không gian làm việc Azure Machine Learning của bạn. Trong loạt bài tiếp theo, bạn sẽ triển khai mô hình đã tinh chỉnh và tích hợp nó với Prompt flow.

    ![Xem công việc tinh chỉnh.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.vi.png)

### Triển khai mô hình Phi-3 đã tinh chỉnh

Để tích hợp mô hình Phi-3 đã tinh chỉnh với Prompt flow, bạn cần triển khai mô hình để có thể truy cập nó cho suy luận thời gian thực. Quá trình này bao gồm đăng ký mô hình, tạo một endpoint trực tuyến và triển khai mô hình.

Trong bài tập này, bạn sẽ:

- Đăng ký mô hình đã tinh chỉnh trong không gian làm việc Azure Machine Learning.
- Tạo một endpoint trực tuyến.
- Triển khai mô hình Phi-3 đã tinh chỉnh được đăng ký.

#### Đăng ký mô hình đã tinh chỉnh

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chọn không gian làm việc Azure Machine Learning mà bạn đã tạo.

    ![Chọn workspace mà bạn đã tạo.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.vi.png)

1. Chọn **Models** từ thanh tab bên trái.
1. Chọn **+ Register**.
1. Chọn **From a job output**.

    ![Đăng ký mô hình.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.vi.png)

1. Chọn công việc mà bạn đã tạo.

    ![Chọn công việc.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.vi.png)

1. Chọn **Next**.

1. Chọn **Model type** thành **MLflow**.

1. Đảm bảo rằng **Job output** được chọn; nó sẽ được chọn tự động.

    ![Chọn output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.vi.png)

2. Chọn **Next**.

3. Chọn **Register**.

    ![Chọn register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.vi.png)

4. Bạn có thể xem mô hình đã đăng ký của mình bằng cách điều hướng đến menu **Models** từ thanh tab bên trái.

    ![Mô hình đã đăng ký.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.vi.png)

#### Triển khai mô hình đã tinh chỉnh

1. Điều hướng đến không gian làm việc Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ thanh tab bên trái.

1. Chọn **Real-time endpoints** từ menu điều hướng.

    ![Tạo endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.vi.png)

1. Chọn **Create**.

1. Chọn mô hình đã đăng ký mà bạn đã tạo.

    ![Chọn mô hình đã đăng ký.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.vi.png)

1. Chọn **Select**.

1. Thực hiện các tác vụ sau:

    - Chọn **Virtual machine** thành *Standard_NC6s_v3*.
    - Chọn **Instance count** mà bạn muốn sử dụng. Ví dụ, *1*.
    - Chọn **Endpoint** thành **New** để tạo một endpoint.
    - Nhập **Endpoint name**. Giá trị này phải là duy nhất.
    - Nhập **Deployment name**. Giá trị này phải là duy nhất.

    ![Điền cài đặt triển khai.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.vi.png)

1. Chọn **Deploy**.

> [!WARNING]
> Để tránh các khoản phí bổ sung vào tài khoản của bạn, hãy đảm bảo xóa endpoint đã tạo trong không gian làm việc Azure Machine Learning.
>

#### Kiểm tra trạng thái triển khai trong Azure Machine Learning Workspace

1. Điều hướng đến không gian làm việc Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ thanh tab bên trái.

1. Chọn endpoint mà bạn đã tạo.

    ![Chọn endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.vi.png)

1. Trên trang này, bạn có thể quản lý các endpoint trong quá trình triển khai.

> [!NOTE]
> Sau khi triển khai hoàn tất, đảm bảo rằng **Live traffic** được đặt thành **100%**. Nếu không, chọn **Update traffic** để điều chỉnh cài đặt lưu lượng. Lưu ý rằng bạn không thể kiểm tra mô hình nếu lưu lượng được đặt thành 0%.
>
> ![Đặt lưu lượng.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.vi.png)
>

## Tình huống 3: Tích hợp với Prompt flow và trò chuyện với mô hình tùy chỉnh của bạn trong Azure AI Foundry

### Tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow

Sau khi triển khai thành công mô hình đã tinh chỉnh, bạn có thể tích hợp nó với Prompt Flow để sử dụng mô hình của mình trong các ứng dụng thời gian thực, cho phép thực hiện nhiều tác vụ tương tác với mô hình Phi-3 tùy chỉnh của bạn.

Trong bài tập này, bạn sẽ:

- Tạo Azure AI Foundry Hub.
- Tạo Azure AI Foundry Project.
- Tạo Prompt flow.
- Thêm một kết nối tùy chỉnh cho mô hình Phi-3 đã tinh chỉnh.
- Thiết lập Prompt flow để trò chuyện với mô hình Phi-3 tùy chỉnh của bạn.

> [!NOTE]
> Bạn cũng có thể tích hợp với Promptflow bằng Azure ML Studio. Quá trình tích hợp tương tự có thể được áp dụng cho Azure ML Studio.

#### Tạo Azure AI Foundry Hub

Bạn cần tạo một Hub trước khi tạo Project. Hub hoạt động như một Nhóm Tài nguyên, cho phép bạn tổ chức và quản lý nhiều Dự án trong Azure AI Foundry.

1. Truy cập [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Chọn **All hubs** từ thanh tab bên trái.

1. Chọn **+ New hub** từ menu điều hướng.

    ![Tạo hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.vi.png)

1. Thực hiện các tác vụ sau:

    - Nhập **Hub name**. Giá trị này phải là duy nhất.
    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Location** mà bạn muốn sử dụng.
    - Chọn **Connect Azure AI Services** để sử dụng (tạo mới nếu cần).
    - Chọn **Connect Azure AI Search** thành **Skip connecting**.

    ![Điền thông tin hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.vi.png)

1. Chọn **Next**.

#### Tạo Azure AI Foundry Project

1. Trong Hub mà bạn đã tạo, chọn **All projects** từ thanh tab bên trái.

1. Chọn **+ New project** từ menu điều hướng.

    ![Chọn dự án mới.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.vi.png)

1. Nhập **Project name**. Giá trị này phải là duy nhất.

    ![Tạo dự án.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.vi.png)

1. Chọn **Create a project**.

#### Thêm một kết nối tùy chỉnh cho mô hình Phi-3 đã tinh chỉnh

Để tích hợp mô hình Phi-3 tùy chỉnh của bạn với Prompt flow, bạn cần lưu endpoint và key của mô hình vào một kết nối tùy chỉnh. Thiết lập này đảm bảo quyền truy cập vào mô hình Phi-3 tùy chỉnh của bạn trong Prompt flow.

#### Đặt api key và endpoint uri của mô hình Phi-3 đã tinh chỉnh

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Điều hướng đến không gian làm việc Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ thanh tab bên trái.

    ![Chọn endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.vi.png)

1. Chọn endpoint mà bạn đã tạo.

    ![Chọn endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.vi.png)

1. Chọn **Consume** từ menu điều hướng.

1. Sao chép **REST endpoint** và **Primary key** của bạn.
![Sao chép khóa API và URI endpoint.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.vi.png)

#### Thêm Kết Nối Tùy Chỉnh

1. Truy cập [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Điều hướng đến dự án Azure AI Foundry mà bạn đã tạo.

1. Trong dự án mà bạn đã tạo, chọn **Settings** từ thanh bên trái.

1. Chọn **+ New connection**.

    ![Chọn kết nối mới.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.vi.png)

1. Chọn **Custom keys** từ menu điều hướng.

    ![Chọn khóa tùy chỉnh.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.vi.png)

1. Thực hiện các bước sau:

    - Chọn **+ Add key value pairs**.
    - Đối với tên khóa, nhập **endpoint** và dán endpoint mà bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Chọn **+ Add key value pairs** một lần nữa.
    - Đối với tên khóa, nhập **key** và dán khóa mà bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Sau khi thêm các khóa, chọn **is secret** để ngăn khóa bị lộ.

    ![Thêm kết nối.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.vi.png)

1. Chọn **Add connection**.

#### Tạo Prompt flow

Bạn đã thêm một kết nối tùy chỉnh trong Azure AI Foundry. Bây giờ, hãy tạo một Prompt flow bằng các bước sau. Sau đó, bạn sẽ kết nối Prompt flow này với kết nối tùy chỉnh để sử dụng mô hình đã tinh chỉnh trong Prompt flow.

1. Điều hướng đến dự án Azure AI Foundry mà bạn đã tạo.

1. Chọn **Prompt flow** từ thanh bên trái.

1. Chọn **+ Create** từ menu điều hướng.

    ![Chọn Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.vi.png)

1. Chọn **Chat flow** từ menu điều hướng.

    ![Chọn loại chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.vi.png)

1. Nhập **Tên thư mục** mà bạn muốn sử dụng.

    ![Nhập tên.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.vi.png)

2. Chọn **Create**.

#### Thiết lập Prompt flow để trò chuyện với mô hình Phi-3 tùy chỉnh của bạn

Bạn cần tích hợp mô hình Phi-3 đã tinh chỉnh vào một Prompt flow. Tuy nhiên, Prompt flow hiện tại không được thiết kế cho mục đích này. Do đó, bạn phải thiết kế lại Prompt flow để tích hợp mô hình tùy chỉnh.

1. Trong Prompt flow, thực hiện các bước sau để xây dựng lại flow hiện tại:

    - Chọn **Raw file mode**.
    - Xóa toàn bộ mã hiện có trong tệp *flow.dag.yml*.
    - Thêm đoạn mã sau vào tệp *flow.dag.yml*.

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

    - Chọn **Save**.

    ![Chọn chế độ raw file.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.vi.png)

1. Thêm đoạn mã sau vào tệp *integrate_with_promptflow.py* để sử dụng mô hình Phi-3 tùy chỉnh trong Prompt flow.

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

    ![Dán mã Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.vi.png)

> [!NOTE]
> Để biết thêm thông tin chi tiết về cách sử dụng Prompt flow trong Azure AI Foundry, bạn có thể tham khảo [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chọn **Chat input**, **Chat output** để bật trò chuyện với mô hình của bạn.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.vi.png)

1. Bây giờ bạn đã sẵn sàng để trò chuyện với mô hình Phi-3 tùy chỉnh của mình. Trong bài tập tiếp theo, bạn sẽ học cách khởi động Prompt flow và sử dụng nó để trò chuyện với mô hình Phi-3 đã tinh chỉnh của bạn.

> [!NOTE]
>
> Flow được xây dựng lại sẽ trông giống như hình dưới đây:
>
> ![Ví dụ về flow.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.vi.png)
>

### Trò chuyện với mô hình Phi-3 tùy chỉnh của bạn

Bây giờ bạn đã tinh chỉnh và tích hợp mô hình Phi-3 tùy chỉnh của mình với Prompt flow, bạn đã sẵn sàng để bắt đầu tương tác với nó. Bài tập này sẽ hướng dẫn bạn cách thiết lập và khởi động một cuộc trò chuyện với mô hình của bạn bằng Prompt flow. Bằng cách làm theo các bước này, bạn sẽ có thể tận dụng tối đa khả năng của mô hình Phi-3 đã tinh chỉnh cho nhiều tác vụ và cuộc trò chuyện khác nhau.

- Trò chuyện với mô hình Phi-3 tùy chỉnh của bạn bằng Prompt flow.

#### Khởi động Prompt flow

1. Chọn **Start compute sessions** để khởi động Prompt flow.

    ![Khởi động compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.vi.png)

1. Chọn **Validate and parse input** để làm mới các tham số.

    ![Xác thực input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.vi.png)

1. Chọn **Value** của **connection** đến kết nối tùy chỉnh mà bạn đã tạo. Ví dụ: *connection*.

    ![Kết nối.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.vi.png)

#### Trò chuyện với mô hình tùy chỉnh của bạn

1. Chọn **Chat**.

    ![Chọn chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.vi.png)

1. Đây là một ví dụ về kết quả: Bây giờ bạn có thể trò chuyện với mô hình Phi-3 tùy chỉnh của mình. Khuyến khích đặt câu hỏi dựa trên dữ liệu được sử dụng để tinh chỉnh.

    ![Trò chuyện với prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.vi.png)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.