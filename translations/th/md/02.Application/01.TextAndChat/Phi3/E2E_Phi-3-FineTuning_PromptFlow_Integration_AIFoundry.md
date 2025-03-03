# ปรับแต่งและผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt Flow ใน Azure AI Foundry

ตัวอย่างแบบครบวงจร (E2E) นี้อ้างอิงจากคำแนะนำ "[ปรับแต่งและผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt Flow ใน Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" จาก Microsoft Tech Community โดยแนะนำกระบวนการปรับแต่ง, นำไปใช้งาน และผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt Flow ใน Azure AI Foundry  
ต่างจากตัวอย่าง E2E อื่น "[ปรับแต่งและผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" ที่ต้องรันโค้ดในเครื่องของคุณเอง บทเรียนนี้จะเน้นเฉพาะการปรับแต่งและผสานรวมโมเดลของคุณใน Azure AI / ML Studio เท่านั้น

## ภาพรวม

ในตัวอย่าง E2E นี้ คุณจะได้เรียนรู้วิธีปรับแต่งโมเดล Phi-3 และผสานรวมกับ Prompt Flow ใน Azure AI Foundry โดยใช้ Azure AI / ML Studio คุณจะสร้างเวิร์กโฟลว์สำหรับการนำโมเดล AI แบบกำหนดเองไปใช้งาน ตัวอย่างนี้แบ่งออกเป็น 3 สถานการณ์:

**สถานการณ์ที่ 1: ตั้งค่าทรัพยากร Azure และเตรียมสำหรับการปรับแต่ง**

**สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และนำไปใช้ใน Azure Machine Learning Studio**

**สถานการณ์ที่ 3: ผสานรวมกับ Prompt Flow และสนทนากับโมเดลแบบกำหนดเองใน Azure AI Foundry**

นี่คือภาพรวมของตัวอย่าง E2E นี้

![ภาพรวม Phi-3-FineTuning_PromptFlow_Integration](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.th.png)

### สารบัญ

1. **[สถานการณ์ที่ 1: ตั้งค่าทรัพยากร Azure และเตรียมสำหรับการปรับแต่ง](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [สร้าง Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ขอ GPU quotas ใน Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [เพิ่มการกำหนดสิทธิ์ (Role Assignment)](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ตั้งค่าโปรเจกต์](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [เตรียมชุดข้อมูลสำหรับการปรับแต่ง](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และนำไปใช้ใน Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ปรับแต่งโมเดล Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [นำโมเดล Phi-3 ที่ปรับแต่งแล้วไปใช้งาน](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[สถานการณ์ที่ 3: ผสานรวมกับ Prompt Flow และสนทนากับโมเดลแบบกำหนดเองใน Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [ผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [สนทนากับโมเดล Phi-3 แบบกำหนดเองของคุณ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## สถานการณ์ที่ 1: ตั้งค่าทรัพยากร Azure และเตรียมสำหรับการปรับแต่ง

### สร้าง Azure Machine Learning Workspace

1. พิมพ์ *azure machine learning* ใน **แถบค้นหา** ด้านบนของหน้าเว็บพอร์ทัล และเลือก **Azure Machine Learning** จากตัวเลือกที่ปรากฏ

    ![พิมพ์ azure machine learning](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.th.png)

2. เลือก **+ Create** จากเมนูนำทาง

3. เลือก **New workspace** จากเมนูนำทาง

    ![เลือก New workspace](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.th.png)

4. ทำตามขั้นตอนต่อไปนี้:

    - เลือก **Subscription** ของ Azure
    - เลือก **Resource group** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - ใส่ **Workspace Name** ซึ่งต้องไม่ซ้ำ
    - เลือก **Region** ที่ต้องการใช้
    - เลือก **Storage account** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Key vault** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Application insights** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Container registry** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)

    ![กรอกข้อมูล Azure Machine Learning](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.th.png)

5. เลือก **Review + Create**

6. เลือก **Create**

### ขอ GPU quotas ใน Azure Subscription

ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีปรับแต่งและนำโมเดล Phi-3 ไปใช้งานโดยใช้ GPU สำหรับการปรับแต่ง คุณจะใช้ GPU *Standard_NC24ads_A100_v4* ซึ่งต้องมีการขอ quota และสำหรับการนำไปใช้งาน คุณจะใช้ GPU *Standard_NC6s_v3* ซึ่งต้องมีการขอ quota เช่นกัน

> [!NOTE]
>
> มีเพียง Subscription แบบ Pay-As-You-Go เท่านั้นที่สามารถขอ GPU ได้ Subscription แบบ Benefit ยังไม่รองรับในขณะนี้

1. เยี่ยมชม [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ทำตามขั้นตอนต่อไปนี้เพื่อขอ quota *Standard NCADSA100v4 Family*:

    - เลือก **Quota** จากแท็บด้านซ้าย
    - เลือก **Virtual machine family** ที่ต้องการใช้ เช่น **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** ซึ่งรวมถึง GPU *Standard_NC24ads_A100_v4*
    - เลือก **Request quota** จากเมนูนำทาง

        ![ขอ quota](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.th.png)

    - ในหน้า Request quota ใส่ **New cores limit** ที่ต้องการใช้ เช่น 24
    - ในหน้า Request quota เลือก **Submit** เพื่อขอ GPU quota

1. ทำตามขั้นตอนเดียวกันเพื่อขอ quota *Standard NCSv3 Family*:

    - เลือก **Quota** จากแท็บด้านซ้าย
    - เลือก **Virtual machine family** ที่ต้องการใช้ เช่น **Standard NCSv3 Family Cluster Dedicated vCPUs** ซึ่งรวมถึง GPU *Standard_NC6s_v3*
    - เลือก **Request quota** จากเมนูนำทาง
    - ในหน้า Request quota ใส่ **New cores limit** ที่ต้องการใช้ เช่น 24
    - ในหน้า Request quota เลือก **Submit** เพื่อขอ GPU quota

### เพิ่มการกำหนดสิทธิ์ (Role Assignment)

เพื่อปรับแต่งและนำโมเดลไปใช้งาน คุณต้องสร้าง User Assigned Managed Identity (UAI) และกำหนดสิทธิ์ที่เหมาะสมให้กับมัน UAI นี้จะถูกใช้สำหรับการยืนยันตัวตนระหว่างการนำไปใช้งาน

#### สร้าง User Assigned Managed Identity (UAI)

1. พิมพ์ *managed identities* ใน **แถบค้นหา** ด้านบนของหน้าเว็บพอร์ทัล และเลือก **Managed Identities** จากตัวเลือกที่ปรากฏ

    ![พิมพ์ managed identities](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.th.png)

1. เลือก **+ Create**

    ![เลือก Create](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.th.png)

1. ทำตามขั้นตอนต่อไปนี้:

    - เลือก **Subscription** ของ Azure
    - เลือก **Resource group** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Region** ที่ต้องการใช้
    - ใส่ **Name** ซึ่งต้องไม่ซ้ำ

    ![กรอกข้อมูล Managed Identities](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.th.png)

1. เลือก **Review + create**

1. เลือก **+ Create**

#### เพิ่มสิทธิ์ Contributor ให้ Managed Identity

1. ไปที่ทรัพยากร Managed Identity ที่คุณสร้าง

1. เลือก **Azure role assignments** จากแท็บด้านซ้าย

1. เลือก **+Add role assignment** จากเมนูนำทาง

1. ในหน้า Add role assignment ทำตามขั้นตอนต่อไปนี้:
    - เลือก **Scope** เป็น **Resource group**
    - เลือก **Subscription** ของ Azure
    - เลือก **Resource group** ที่ต้องการใช้
    - เลือก **Role** เป็น **Contributor**

    ![กรอกข้อมูล Contributor Role](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.th.png)

2. เลือก **Save**

#### เพิ่มสิทธิ์ Storage Blob Data Reader ให้ Managed Identity

1. พิมพ์ *storage accounts* ใน **แถบค้นหา** ด้านบนของหน้าเว็บพอร์ทัล และเลือก **Storage accounts** จากตัวเลือกที่ปรากฏ

    ![พิมพ์ storage accounts](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.th.png)

1. เลือกบัญชีเก็บข้อมูลที่เชื่อมโยงกับ Azure Machine Learning Workspace ที่คุณสร้าง เช่น *finetunephistorage*

1. ทำตามขั้นตอนต่อไปนี้เพื่อไปที่หน้า Add role assignment:

    - ไปที่บัญชีเก็บข้อมูล Azure ที่คุณสร้าง
    - เลือก **Access Control (IAM)** จากแท็บด้านซ้าย
    - เลือก **+ Add** จากเมนูนำทาง
    - เลือก **Add role assignment** จากเมนูนำทาง

    ![เพิ่ม Role](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.th.png)

1. ในหน้า Add role assignment ทำตามขั้นตอนต่อไปนี้:

    - ในหน้า Role พิมพ์ *Storage Blob Data Reader* ใน **แถบค้นหา** และเลือก **Storage Blob Data Reader** จากตัวเลือกที่ปรากฏ
    - ในหน้า Role เลือก **Next**
    - ในหน้า Members เลือก **Assign access to** **Managed identity**
    - ในหน้า Members เลือก **+ Select members**
    - ในหน้า Select managed identities เลือก **Subscription** ของ Azure
    - ในหน้า Select managed identities เลือก **Managed identity** ที่คุณสร้าง เช่น *finetunephi-managedidentity*
    - ในหน้า Select managed identities เลือก **Select**

    ![เลือก Managed Identity](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.th.png)

1. เลือก **Review + assign**

#### เพิ่มสิทธิ์ AcrPull ให้ Managed Identity

1. พิมพ์ *container registries* ใน **แถบค้นหา** ด้านบนของหน้าเว็บพอร์ทัล และเลือก **Container registries** จากตัวเลือกที่ปรากฏ

    ![พิมพ์ container registries](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.th.png)

1. เลือก Container Registry ที่เชื่อมโยงกับ Azure Machine Learning Workspace เช่น *finetunephicontainerregistry*

1. ทำตามขั้นตอนต่อไปนี้เพื่อไปที่หน้า Add role assignment:

    - เลือก **Access Control (IAM)** จากแท็บด้านซ้าย
    - เลือก **+ Add** จากเมนูนำทาง
    - เลือก **Add role assignment** จากเมนูนำทาง

1. ในหน้า Add role assignment ทำตามขั้นตอนต่อไปนี้:

    - ในหน้า Role พิมพ์ *AcrPull* ใน **แถบค้นหา** และเลือก **AcrPull** จากตัวเลือกที่ปรากฏ
    - ในหน้า Role เลือก **Next**
    - ในหน้า Members เลือก **Assign access to** **Managed identity**
    - ในหน้า Members เลือก **+ Select members**
    - ในหน้า Select managed identities เลือก **Subscription** ของ Azure
    - ในหน้า Select managed identities เลือก **Managed identity** ที่คุณสร้าง เช่น *finetunephi-managedidentity*
    - ในหน้า Select managed identities เลือก **Select**
    - เลือก **Review + assign**

### ตั้งค่าโปรเจกต์

เพื่อดาวน์โหลดชุดข้อมูลที่จำเป็นสำหรับการปรับแต่ง คุณจะต้องตั้งค่าสภาพแวดล้อมในเครื่อง

ในบทเรียนนี้ คุณจะ:

- สร้างโฟลเดอร์เพื่อใช้งานภายใน
- สร้าง virtual environment
- ติดตั้งแพ็กเกจที่จำเป็น
- สร้างไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล

#### สร้างโฟลเดอร์เพื่อใช้งานภายใน

1. เปิดหน้าต่างเทอร์มินัลและพิมพ์คำสั่งต่อไปนี้เพื่อสร้างโฟลเดอร์ชื่อ *finetune-phi* ในเส้นทางเริ่มต้น

    ```console
    mkdir finetune-phi
    ```

2. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อไปยังโฟลเดอร์ *finetune-phi* ที่คุณสร้าง

    ```console
    cd finetune-phi
    ```

#### สร้าง virtual environment

1. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อสร้าง virtual environment ชื่อ *.venv*

    ```console
    python -m venv .venv
    ```

2. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อเปิดใช้งาน virtual environment

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> หากสำเร็จ คุณควรเห็น *(.venv)* ปรากฏอยู่ก่อนคำสั่งในเทอร์มินัล

#### ติดตั้งแพ็กเกจที่จำเป็น

1. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อติดตั้งแพ็กเกจที่จำเป็น

    ```console
    pip install datasets==2.19.1
    ```

#### สร้าง `download_dataset.py`

> [!NOTE]
> โครงสร้างโฟลเดอร์ที่สมบูรณ์:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. เปิด **Visual Studio Code**

1. เลือก **File** จากเมนูบาร์

1. เลือก **Open Folder**

1. เลือกโฟลเดอร์ *finetune-phi* ที่คุณสร้าง ซึ่งอยู่ที่ *C:\Users\yourUserName\finetune-phi*

    ![เลือกโฟลเดอร์ที่คุณสร้าง](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.th.png)

1. ในแผงด้านซ้ายของ Visual Studio Code คลิกขวาและเลือก **New File** เพื่อสร้างไฟล์ใหม่ชื่อ *download_dataset.py*

    ![สร้างไฟล์ใหม่](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.th.png)

### เตรียมชุดข้อมูลสำหรับการปรับแต่ง

ในบทเรียนนี้ คุณจะรันไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล *ultrachat_200k* ลงในสภาพแวดล้อมในเครื่องของคุณ จากนั้นคุณจะใช้ชุดข้อมูลนี้เพื่อปรับแต่งโมเดล Phi-3 ใน Azure Machine Learning

ในบทเรียนนี้ คุณจะ:

- เพิ่มโค้ดลงในไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูล
- รันไฟล์ *download_dataset.py* เพื่อดาวน์โหลดชุดข้อมูลลงในสภาพแวดล้อมในเครื่องของคุณ

#### ดาวน์โหลดชุดข้อมูลของคุณโดยใช้ *download_dataset.py*

1. เปิดไฟล์ *download_dataset.py* ใน Visual Studio Code

1. เพิ่มโค้ดต่อไปนี้ลงในไฟล์ *download_dataset.py*

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

1. พิมพ์คำสั่งต่อไปนี้ในเทอร์มินัลเพื่อรันสคริปต์และดาวน์โหลดชุดข้อมูลลงในสภาพแวดล้อมในเครื่องของคุณ

    ```console
    python download_dataset.py
    ```

1. ตรวจสอบว่าชุดข้อมูลถูกบันทึกลงในไดเรกทอรี *finetune-phi/data* ในเครื่องของคุณเรียบร้อยแล้ว

> [!NOTE]
>
> #### หมายเหตุเกี่ยวกับขนาดชุดข้อมูลและเวลาในการปรับแต่ง
>
> ในบทเรียนนี้ คุณใช้เพียง 1% ของชุดข้อมูล (`split='train[:1%]'`) ซึ่งช่วยลดปริมาณข้อมูลลงอย่างมาก ทำให้กระบวนการอัปโหลดและปรับแต่งเร็วขึ้น คุณสามารถปรับเปอร์เซ็นต์นี้เพื่อหาสมดุลระหว่างเวลาในการฝึกและประสิทธิภาพของโมเดล การใช้ชุดข้อมูลขนาดเล็กช่วยลดเวลาในการปรับแต่ง ทำให้กระบวนการนี้จัดการได้ง่ายขึ้นสำหรับบทเรียนนี้

## สถานการณ์ที่ 2: ปรับแต่งโมเดล Phi-3 และนำไปใช้ใน Azure Machine Learning Studio

### ปรับแต่งโมเดล Phi-3

ในบทเรียนนี้ คุณจะปรับแต
1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. เลือก **Compute** จากแถบด้านซ้าย

1. เลือก **Compute clusters** จากเมนูนำทาง

1. คลิก **+ New**

    ![เลือก compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.th.png)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Region** ที่คุณต้องการใช้งาน
    - ตั้งค่า **Virtual machine tier** เป็น **Dedicated**
    - ตั้งค่า **Virtual machine type** เป็น **GPU**
    - กรอง **Virtual machine size** เป็น **Select from all options**
    - เลือก **Virtual machine size** เป็น **Standard_NC24ads_A100_v4**

    ![สร้าง cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.th.png)

1. คลิก **Next**

1. ทำตามขั้นตอนดังนี้:

    - ใส่ **Compute name** (ต้องเป็นค่าที่ไม่ซ้ำ)
    - ตั้งค่า **Minimum number of nodes** เป็น **0**
    - ตั้งค่า **Maximum number of nodes** เป็น **1**
    - ตั้งค่า **Idle seconds before scale down** เป็น **120**

    ![สร้าง cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.th.png)

1. คลิก **Create**

#### ปรับแต่งโมเดล Phi-3

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. เลือก workspace ของ Azure Machine Learning ที่คุณสร้างไว้

    ![เลือก workspace ที่คุณสร้าง.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.th.png)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Model catalog** จากแถบด้านซ้าย
    - พิมพ์ *phi-3-mini-4k* ใน **search bar** แล้วเลือก **Phi-3-mini-4k-instruct** จากตัวเลือกที่แสดง

    ![พิมพ์ phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.th.png)

1. เลือก **Fine-tune** จากเมนูนำทาง

    ![เลือก fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.th.png)

1. ทำตามขั้นตอนดังนี้:

    - ตั้งค่า **Select task type** เป็น **Chat completion**
    - คลิก **+ Select data** เพื่ออัปโหลด **Training data**
    - ตั้งค่า Validation data upload type เป็น **Provide different validation data**
    - คลิก **+ Select data** เพื่ออัปโหลด **Validation data**

    ![กรอกหน้าปรับแต่ง.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.th.png)

    > [!TIP]
    >
    > คุณสามารถเลือก **Advanced settings** เพื่อปรับแต่งค่าต่าง ๆ เช่น **learning_rate** และ **lr_scheduler_type** เพื่อเพิ่มประสิทธิภาพกระบวนการปรับแต่งให้เหมาะสมกับความต้องการของคุณ

1. คลิก **Finish**

1. ในแบบฝึกหัดนี้ คุณได้ปรับแต่งโมเดล Phi-3 โดยใช้ Azure Machine Learning สำเร็จ โปรดทราบว่ากระบวนการปรับแต่งอาจใช้เวลานาน หลังจากรันงานปรับแต่ง คุณต้องรอให้กระบวนการเสร็จสมบูรณ์ คุณสามารถตรวจสอบสถานะของงานปรับแต่งได้โดยไปที่แท็บ Jobs ใน workspace ของ Azure Machine Learning ในชุดถัดไป คุณจะได้เรียนรู้วิธีการปรับใช้โมเดลที่ปรับแต่งแล้วและผสานรวมกับ Prompt flow

    ![ดูงานปรับแต่ง.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.th.png)

### ปรับใช้โมเดล Phi-3 ที่ปรับแต่งแล้ว

เพื่อผสานรวมโมเดล Phi-3 ที่ปรับแต่งแล้วกับ Prompt flow คุณต้องปรับใช้โมเดลเพื่อให้สามารถเข้าถึงสำหรับการทำนายผลแบบเรียลไทม์ได้ กระบวนการนี้รวมถึงการลงทะเบียนโมเดล การสร้าง endpoint แบบออนไลน์ และการปรับใช้โมเดล

ในแบบฝึกหัดนี้ คุณจะ:

- ลงทะเบียนโมเดลที่ปรับแต่งแล้วใน workspace ของ Azure Machine Learning
- สร้าง endpoint แบบออนไลน์
- ปรับใช้โมเดล Phi-3 ที่ลงทะเบียนไว้

#### ลงทะเบียนโมเดลที่ปรับแต่งแล้ว

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. เลือก workspace ของ Azure Machine Learning ที่คุณสร้างไว้

    ![เลือก workspace ที่คุณสร้าง.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.th.png)

1. เลือก **Models** จากแถบด้านซ้าย
1. คลิก **+ Register**
1. เลือก **From a job output**

    ![ลงทะเบียนโมเดล.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.th.png)

1. เลือกงานที่คุณสร้างไว้

    ![เลือกงาน.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.th.png)

1. คลิก **Next**

1. ตั้งค่า **Model type** เป็น **MLflow**

1. ตรวจสอบให้แน่ใจว่า **Job output** ถูกเลือกโดยอัตโนมัติ

    ![เลือก output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.th.png)

2. คลิก **Next**

3. คลิก **Register**

    ![เลือก register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.th.png)

4. คุณสามารถดูโมเดลที่ลงทะเบียนไว้ได้โดยไปที่เมนู **Models** จากแถบด้านซ้าย

    ![โมเดลที่ลงทะเบียน.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.th.png)

#### ปรับใช้โมเดลที่ปรับแต่งแล้ว

1. ไปที่ workspace ของ Azure Machine Learning ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแถบด้านซ้าย

1. เลือก **Real-time endpoints** จากเมนูนำทาง

    ![สร้าง endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.th.png)

1. คลิก **Create**

1. เลือกโมเดลที่ลงทะเบียนไว้

    ![เลือกโมเดลที่ลงทะเบียน.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.th.png)

1. คลิก **Select**

1. ทำตามขั้นตอนดังนี้:

    - ตั้งค่า **Virtual machine** เป็น *Standard_NC6s_v3*
    - เลือก **Instance count** ที่ต้องการใช้ เช่น *1*
    - ตั้งค่า **Endpoint** เป็น **New** เพื่อสร้าง endpoint ใหม่
    - ใส่ **Endpoint name** (ต้องเป็นค่าที่ไม่ซ้ำ)
    - ใส่ **Deployment name** (ต้องเป็นค่าที่ไม่ซ้ำ)

    ![กรอกการตั้งค่าการปรับใช้.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.th.png)

1. คลิก **Deploy**

> [!WARNING]
> เพื่อหลีกเลี่ยงค่าใช้จ่ายเพิ่มเติมในบัญชีของคุณ อย่าลืมลบ endpoint ที่สร้างไว้ใน workspace ของ Azure Machine Learning
>

#### ตรวจสอบสถานะการปรับใช้ใน Azure Machine Learning Workspace

1. ไปที่ workspace ของ Azure Machine Learning ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแถบด้านซ้าย

1. เลือก endpoint ที่คุณสร้างไว้

    ![เลือก endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.th.png)

1. ในหน้านี้ คุณสามารถจัดการ endpoint ระหว่างกระบวนการปรับใช้ได้

> [!NOTE]
> เมื่อการปรับใช้เสร็จสิ้น ให้ตรวจสอบว่า **Live traffic** ถูกตั้งค่าเป็น **100%** หากยังไม่ถูกตั้งค่า ให้เลือก **Update traffic** เพื่อปรับการตั้งค่าทราฟฟิก โปรดทราบว่าคุณไม่สามารถทดสอบโมเดลได้หากทราฟฟิกตั้งค่าเป็น 0%
>
> ![ตั้งค่าทราฟฟิก.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.th.png)
>

## สถานการณ์ที่ 3: ผสานรวมกับ Prompt flow และสนทนากับโมเดลที่ปรับแต่งใน Azure AI Foundry

### ผสานรวมโมเดล Phi-3 ที่ปรับแต่งแล้วกับ Prompt flow

หลังจากที่คุณปรับใช้โมเดลที่ปรับแต่งแล้วสำเร็จ คุณสามารถผสานรวมโมเดลกับ Prompt Flow เพื่อใช้งานโมเดลในแอปพลิเคชันแบบเรียลไทม์ ทำให้สามารถใช้งานฟังก์ชันโต้ตอบต่าง ๆ กับโมเดล Phi-3 ที่ปรับแต่งของคุณได้

ในแบบฝึกหัดนี้ คุณจะ:

- สร้าง Azure AI Foundry Hub
- สร้าง Azure AI Foundry Project
- สร้าง Prompt flow
- เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 ที่ปรับแต่ง
- ตั้งค่า Prompt flow เพื่อสนทนากับโมเดล Phi-3 ที่ปรับแต่งของคุณ

> [!NOTE]
> คุณสามารถผสานรวมกับ Promptflow โดยใช้ Azure ML Studio ได้เช่นกัน กระบวนการผสานรวมเดียวกันสามารถนำไปใช้กับ Azure ML Studio ได้

#### สร้าง Azure AI Foundry Hub

คุณต้องสร้าง Hub ก่อนที่จะสร้าง Project Hub ทำหน้าที่เหมือน Resource Group ช่วยให้คุณจัดระเบียบและจัดการ Projects หลายตัวใน Azure AI Foundry ได้

1. ไปที่ [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)

1. เลือก **All hubs** จากแถบด้านซ้าย

1. คลิก **+ New hub** จากเมนูนำทาง

    ![สร้าง hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.th.png)

1. ทำตามขั้นตอนดังนี้:

    - ใส่ **Hub name** (ต้องเป็นค่าที่ไม่ซ้ำ)
    - เลือก Azure **Subscription** ของคุณ
    - เลือก **Resource group** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - เลือก **Location** ที่ต้องการใช้
    - เลือก **Connect Azure AI Services** ที่ต้องการใช้ (สร้างใหม่หากจำเป็น)
    - ตั้งค่า **Connect Azure AI Search** เป็น **Skip connecting**

    ![กรอก hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.th.png)

1. คลิก **Next**

#### สร้าง Azure AI Foundry Project

1. ใน Hub ที่คุณสร้างไว้ เลือก **All projects** จากแถบด้านซ้าย

1. คลิก **+ New project** จากเมนูนำทาง

    ![เลือก new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.th.png)

1. ใส่ **Project name** (ต้องเป็นค่าที่ไม่ซ้ำ)

    ![สร้าง project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.th.png)

1. คลิก **Create a project**

#### เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 ที่ปรับแต่ง

เพื่อผสานรวมโมเดล Phi-3 ที่ปรับแต่งของคุณกับ Prompt flow คุณต้องบันทึก endpoint และคีย์ของโมเดลใน custom connection การตั้งค่านี้ช่วยให้เข้าถึงโมเดล Phi-3 ที่ปรับแต่งของคุณใน Prompt flow ได้

#### ตั้งค่า api key และ endpoint uri ของโมเดล Phi-3 ที่ปรับแต่ง

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)

1. ไปที่ workspace ของ Azure Machine Learning ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแถบด้านซ้าย

    ![เลือก endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.th.png)

1. เลือก endpoint ที่คุณสร้างไว้

    ![เลือก endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.th.png)

1. เลือก **Consume** จากเมนูนำทาง

1. คัดลอก **REST endpoint** และ **Primary key** ของคุณ
![คัดลอกคีย์ API และ Endpoint URI.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.th.png)

#### เพิ่มการเชื่อมต่อแบบกำหนดเอง

1. ไปที่ [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. ในโปรเจกต์ที่คุณสร้างไว้ ให้เลือก **Settings** จากแถบด้านซ้าย

1. เลือก **+ New connection**

    ![เลือก new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.th.png)

1. เลือก **Custom keys** จากเมนูนำทาง

    ![เลือก custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.th.png)

1. ดำเนินการดังนี้:

    - เลือก **+ Add key value pairs**
    - สำหรับชื่อคีย์ ให้ใส่ **endpoint** และวาง endpoint ที่คุณคัดลอกมาจาก Azure ML Studio ลงในช่องค่า
    - เลือก **+ Add key value pairs** อีกครั้ง
    - สำหรับชื่อคีย์ ให้ใส่ **key** และวางคีย์ที่คุณคัดลอกมาจาก Azure ML Studio ลงในช่องค่า
    - หลังจากเพิ่มคีย์แล้ว ให้เลือก **is secret** เพื่อป้องกันไม่ให้คีย์ถูกเปิดเผย

    ![เพิ่มการเชื่อมต่อ.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.th.png)

1. เลือก **Add connection**

#### สร้าง Prompt flow

คุณได้เพิ่มการเชื่อมต่อแบบกำหนดเองใน Azure AI Foundry แล้ว ตอนนี้มาสร้าง Prompt flow โดยทำตามขั้นตอนต่อไปนี้ จากนั้นคุณจะเชื่อมต่อ Prompt flow นี้กับการเชื่อมต่อแบบกำหนดเองเพื่อให้สามารถใช้งานโมเดลที่ปรับแต่งได้ภายใน Prompt flow

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. เลือก **Prompt flow** จากแถบด้านซ้าย

1. เลือก **+ Create** จากเมนูนำทาง

    ![เลือก Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.th.png)

1. เลือก **Chat flow** จากเมนูนำทาง

    ![เลือก chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.th.png)

1. ใส่ **Folder name** ที่ต้องการใช้

    ![ใส่ชื่อ.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.th.png)

2. เลือก **Create**

#### ตั้งค่า Prompt flow เพื่อสนทนากับโมเดล Phi-3 ที่ปรับแต่งของคุณ

คุณจำเป็นต้องผสานรวมโมเดล Phi-3 ที่ปรับแต่งแล้วเข้ากับ Prompt flow อย่างไรก็ตาม Prompt flow ที่มีอยู่ไม่เหมาะสำหรับการใช้งานนี้ ดังนั้นคุณต้องออกแบบ Prompt flow ใหม่เพื่อให้สามารถรวมโมเดลแบบกำหนดเองได้

1. ใน Prompt flow ให้ดำเนินการดังนี้เพื่อสร้าง flow ใหม่:

    - เลือก **Raw file mode**
    - ลบโค้ดทั้งหมดในไฟล์ *flow.dag.yml*
    - เพิ่มโค้ดดังต่อไปนี้ในไฟล์ *flow.dag.yml*

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

    - เลือก **Save**

    ![เลือก raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.th.png)

1. เพิ่มโค้ดต่อไปนี้ในไฟล์ *integrate_with_promptflow.py* เพื่อใช้งานโมเดล Phi-3 แบบกำหนดเองใน Prompt flow

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

    ![วางโค้ด prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.th.png)

> [!NOTE]  
> สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้งาน Prompt flow ใน Azure AI Foundry สามารถดูได้ที่ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)

1. เลือก **Chat input**, **Chat output** เพื่อเปิดใช้งานการสนทนากับโมเดลของคุณ

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.th.png)

1. ตอนนี้คุณพร้อมที่จะสนทนากับโมเดล Phi-3 แบบกำหนดเองของคุณแล้ว ในแบบฝึกหัดถัดไป คุณจะได้เรียนรู้วิธีเริ่ม Prompt flow และใช้งานเพื่อสนทนากับโมเดล Phi-3 ที่ปรับแต่งของคุณ

> [!NOTE]  
>  
> Flow ที่สร้างใหม่ควรมีลักษณะดังภาพด้านล่าง:  
>  
> ![ตัวอย่าง flow.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.th.png)

### สนทนากับโมเดล Phi-3 แบบกำหนดเองของคุณ

ตอนนี้คุณได้ปรับแต่งและผสานรวมโมเดล Phi-3 แบบกำหนดเองของคุณเข้ากับ Prompt flow แล้ว คุณพร้อมที่จะเริ่มต้นโต้ตอบกับมัน แบบฝึกหัดนี้จะแนะนำวิธีการตั้งค่าและเริ่มต้นการสนทนากับโมเดลของคุณโดยใช้ Prompt flow โดยการทำตามขั้นตอนเหล่านี้ คุณจะสามารถใช้ความสามารถของโมเดล Phi-3 ที่ปรับแต่งได้อย่างเต็มที่สำหรับงานและการสนทนาต่างๆ

- สนทนากับโมเดล Phi-3 แบบกำหนดเองของคุณโดยใช้ Prompt flow

#### เริ่ม Prompt flow

1. เลือก **Start compute sessions** เพื่อเริ่ม Prompt flow

    ![เริ่ม compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.th.png)

1. เลือก **Validate and parse input** เพื่อรีเฟรชพารามิเตอร์

    ![ตรวจสอบ input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.th.png)

1. เลือก **Value** ของ **connection** ไปยังการเชื่อมต่อแบบกำหนดเองที่คุณสร้างไว้ เช่น *connection*

    ![การเชื่อมต่อ.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.th.png)

#### สนทนากับโมเดลแบบกำหนดเองของคุณ

1. เลือก **Chat**

    ![เลือก chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.th.png)

1. นี่คือตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถสนทนากับโมเดล Phi-3 แบบกำหนดเองของคุณได้ ขอแนะนำให้ตั้งคำถามตามข้อมูลที่ใช้ในการปรับแต่ง

    ![สนทนาด้วย prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.th.png)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อให้การแปลถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องเกิดขึ้น เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้