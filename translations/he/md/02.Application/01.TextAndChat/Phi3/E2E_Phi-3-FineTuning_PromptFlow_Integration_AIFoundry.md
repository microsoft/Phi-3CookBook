# כוונון והתממשקות של מודלים מותאמים אישית Phi-3 עם Prompt flow ב-Azure AI Foundry

המדריך המלא הזה מבוסס על המאמר "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" מקהילת הטכנולוגיה של Microsoft. הוא מציג את התהליכים של כוונון, פריסה והתממשקות של מודלים מותאמים אישית Phi-3 עם Prompt flow ב-Azure AI Foundry.  
בניגוד לדוגמת E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", אשר כללה הרצת קוד מקומית, מדריך זה מתמקד לחלוטין בכוונון והתממשקות של המודל בתוך Azure AI / ML Studio.

## סקירה כללית

בדוגמת E2E זו, תלמדו כיצד לכוון את מודל Phi-3 ולהתממשק איתו באמצעות Prompt flow ב-Azure AI Foundry. על ידי שימוש ב-Azure AI / ML Studio, תבנו תהליך עבודה לפריסה ושימוש במודלים מותאמים אישית של AI. דוגמת E2E זו מחולקת לשלושה תרחישים:

**תרחיש 1: הקמת משאבי Azure והכנה לכוונון**

**תרחיש 2: כוונון מודל Phi-3 ופריסתו ב-Azure Machine Learning Studio**

**תרחיש 3: התממשקות עם Prompt flow ושיחה עם המודל המותאם שלכם ב-Azure AI Foundry**

להלן סקירה כללית של דוגמת E2E זו.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.he.png)

### תוכן עניינים

1. **[תרחיש 1: הקמת משאבי Azure והכנה לכוונון](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [יצירת Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [בקשת מכסות GPU במנוי Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [הוספת הרשאות תפקיד](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [הגדרת פרויקט](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [הכנת מערכי נתונים לכוונון](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[תרחיש 2: כוונון מודל Phi-3 ופריסתו ב-Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [כוונון מודל Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [פריסת מודל Phi-3 המכוונן](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[תרחיש 3: התממשקות עם Prompt flow ושיחה עם המודל המותאם שלכם ב-Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [התממשקות של מודל Phi-3 המותאם עם Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [שיחה עם מודל Phi-3 המותאם שלכם](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## תרחיש 1: הקמת משאבי Azure והכנה לכוונון

### יצירת Azure Machine Learning Workspace

1. הקלידו *azure machine learning* בשורת החיפוש בראש דף הפורטל ובחרו **Azure Machine Learning** מתוך האפשרויות המופיעות.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.he.png)

2. בחרו **+ Create** מתוך תפריט הניווט.

3. בחרו **New workspace** מתוך תפריט הניווט.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.he.png)

4. בצעו את הפעולות הבאות:

    - בחרו את **מנוי Azure** שלכם.  
    - בחרו את **קבוצת המשאבים** לשימוש (צרו אחת חדשה אם צריך).  
    - הזינו **שם סביבת עבודה**. עליו להיות ייחודי.  
    - בחרו את **האזור** בו תרצו להשתמש.  
    - בחרו את **חשבון האחסון** לשימוש (צרו אחד חדש אם צריך).  
    - בחרו את **Key vault** לשימוש (צרו אחד חדש אם צריך).  
    - בחרו את **Application insights** לשימוש (צרו אחד חדש אם צריך).  
    - בחרו את **Container registry** לשימוש (צרו אחד חדש אם צריך).  

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.he.png)

5. בחרו **Review + Create**.

6. בחרו **Create**.

### בקשת מכסות GPU במנוי Azure

במדריך זה תלמדו כיצד לכוון ולפרוס מודל Phi-3 תוך שימוש ב-GPU. לצורך כוונון, תשתמשו ב-*Standard_NC24ads_A100_v4* GPU, הדורש בקשת מכסה. לצורך פריסה, תשתמשו ב-*Standard_NC6s_v3* GPU, שגם הוא דורש בקשת מכסה.

> [!NOTE]
>
> רק מנויים מסוג Pay-As-You-Go (המנוי הסטנדרטי) זכאים להקצאת GPU; מנויי הטבה אינם נתמכים כרגע.

1. בקרו ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בצעו את הפעולות הבאות כדי לבקש מכסת *Standard NCADSA100v4 Family*:

    - בחרו **Quota** מתפריט הצד השמאלי.  
    - בחרו את **Virtual machine family** לשימוש. לדוגמה, בחרו **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, הכולל את ה-*Standard_NC24ads_A100_v4* GPU.  
    - בחרו **Request quota** מתפריט הניווט.  

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.he.png)

    - בתוך דף בקשת המכסה, הזינו את **New cores limit** הרצוי. לדוגמה, 24.  
    - בתוך דף בקשת המכסה, בחרו **Submit** כדי לבקש את מכסת ה-GPU.

1. בצעו את הפעולות הבאות כדי לבקש מכסת *Standard NCSv3 Family*:

    - בחרו **Quota** מתפריט הצד השמאלי.  
    - בחרו את **Virtual machine family** לשימוש. לדוגמה, בחרו **Standard NCSv3 Family Cluster Dedicated vCPUs**, הכולל את ה-*Standard_NC6s_v3* GPU.  
    - בחרו **Request quota** מתפריט הניווט.  
    - בתוך דף בקשת המכסה, הזינו את **New cores limit** הרצוי. לדוגמה, 24.  
    - בתוך דף בקשת המכסה, בחרו **Submit** כדי לבקש את מכסת ה-GPU.

### הוספת הרשאות תפקיד

כדי לכוון ולפרוס את המודלים שלכם, עליכם תחילה ליצור Managed Identity ייעודי (UAI) ולהקצות לו הרשאות מתאימות. זה ישמש לאימות במהלך הפריסה.

#### יצירת Managed Identity (UAI)

1. הקלידו *managed identities* בשורת החיפוש בראש דף הפורטל ובחרו **Managed Identities** מתוך האפשרויות המופיעות.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.he.png)

1. בחרו **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.he.png)

1. בצעו את הפעולות הבאות:

    - בחרו את **מנוי Azure** שלכם.  
    - בחרו את **קבוצת המשאבים** לשימוש (צרו אחת חדשה אם צריך).  
    - בחרו את **האזור** בו תרצו להשתמש.  
    - הזינו **שם** ייחודי.  

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.he.png)

1. בחרו **Review + create**.

1. בחרו **+ Create**.

#### הוספת הרשאת Contributor ל-Managed Identity

1. נווטו למשאב Managed Identity שיצרתם.

1. בחרו **Azure role assignments** מתפריט הצד השמאלי.

1. בחרו **+Add role assignment** מתפריט הניווט.

1. בתוך דף Add role assignment, בצעו את הפעולות הבאות:
    - בחרו **Scope** ל-**Resource group**.  
    - בחרו את **מנוי Azure** שלכם.  
    - בחרו את **קבוצת המשאבים** לשימוש.  
    - בחרו **Role** ל-**Contributor**.  

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.he.png)

2. בחרו **Save**.

#### הוספת הרשאת Storage Blob Data Reader ל-Managed Identity

1. הקלידו *storage accounts* בשורת החיפוש בראש דף הפורטל ובחרו **Storage accounts** מתוך האפשרויות המופיעות.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.he.png)

1. בחרו את חשבון האחסון המשויך ל-Azure Machine Learning workspace שיצרתם. לדוגמה, *finetunephistorage*.  

1. בצעו את הפעולות הבאות כדי לנווט לדף Add role assignment:

    - נווטו לחשבון האחסון שיצרתם.  
    - בחרו **Access Control (IAM)** מתפריט הצד השמאלי.  
    - בחרו **+ Add** מתפריט הניווט.  
    - בחרו **Add role assignment** מתפריט הניווט.  

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.he.png)

1. בתוך דף Add role assignment, בצעו את הפעולות הבאות:

    - הקלידו *Storage Blob Data Reader* בשורת החיפוש ובחרו **Storage Blob Data Reader** מתוך האפשרויות המופיעות.  
    - בחרו **Next**.  
    - בחרו **Assign access to** ל-**Managed identity**.  
    - בחרו **+ Select members**.  
    - בחרו את **מנוי Azure** שלכם.  
    - בחרו את **Managed identity** שיצרתם. לדוגמה, *finetunephi-managedidentity*.  
    - בחרו **Select**.  

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.he.png)

1. בחרו **Review + assign**.

#### הוספת הרשאת AcrPull ל-Managed Identity

1. הקלידו *container registries* בשורת החיפוש בראש דף הפורטל ובחרו **Container registries** מתוך האפשרויות המופיעות.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.he.png)

1. בחרו את ה-Container registry המשויך ל-Azure Machine Learning workspace. לדוגמה, *finetunephicontainerregistry*.

1. בצעו את הפעולות הבאות כדי לנווט לדף Add role assignment:

    - בחרו **Access Control (IAM)** מתפריט הצד השמאלי.  
    - בחרו **+ Add** מתפריט הניווט.  
    - בחרו **Add role assignment** מתפריט הניווט.  

1. בתוך דף Add role assignment, בצעו את הפעולות הבאות:

    - הקלידו *AcrPull* בשורת החיפוש ובחרו **AcrPull** מתוך האפשרויות המופיעות.  
    - בחרו **Next**.  
    - בחרו **Assign access to** ל-**Managed identity**.  
    - בחרו **+ Select members**.  
    - בחרו את **מנוי Azure** שלכם.  
    - בחרו את **Managed identity** שיצרתם. לדוגמה, *finetunephi-managedidentity*.  
    - בחרו **Select**.  
    - בחרו **Review + assign**.

### הגדרת פרויקט

להורדת מערכי הנתונים הנדרשים לכוונון, תגדירו סביבת עבודה מקומית.

בתרגיל זה תבצעו:

- יצירת תיקייה לעבודה בתוכה.  
- יצירת סביבת עבודה וירטואלית.  
- התקנת חבילות נדרשות.  
- יצירת קובץ *download_dataset.py* להורדת מערכי הנתונים.

#### יצירת תיקייה לעבודה בתוכה

1. פתחו חלון טרמינל והקלידו את הפקודה הבאה ליצירת תיקייה בשם *finetune-phi* בנתיב ברירת המחדל.

    ```console
    mkdir finetune-phi
    ```

2. הקלידו את הפקודה הבאה בטרמינל כדי לנווט לתיקיית *finetune-phi* שיצרתם.

    ```console
    cd finetune-phi
    ```

#### יצירת סביבת עבודה וירטואלית

1. הקלידו את הפקודה הבאה בטרמינל ליצירת סביבת עבודה וירטואלית בשם *.venv*.

    ```console
    python -m venv .venv
    ```

2. הקלידו את הפקודה הבאה בטרמינל להפעלת סביבת העבודה הווירטואלית.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> אם זה עבד, תראו *(.venv)* לפני שורת הפקודה.

#### התקנת חבילות נדרשות

1. הקלידו את הפקודות הבאות בטרמינל להתקנת החבילות הנדרשות.

    ```console
    pip install datasets==2.19.1
    ```

#### יצירת `download_dataset.py`

> [!NOTE]  
> מבנה התיקיות המלא:  
>  
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. פתחו את **Visual Studio Code**.

1. בחרו **File** משורת התפריט.

1. בחרו **Open Folder**.

1. בחרו את התיקייה *finetune-phi* שיצרתם, הממוקמת ב-*C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.he.png)

1. בחלונית השמאלית של Visual Studio Code, לחצו לחצן ימני ובחרו **New File** ליצירת קובץ חדש בשם *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.he.png)

### הכנת מערכי נתונים לכוונון

בתרגיל זה תריצו את קובץ *download_dataset.py* להורדת מערכי נתונים *ultrachat_200k* לסביבה המקומית שלכם. לאחר מכן תשתמשו במערכי נתונים אלו לכוונון מודל Phi-3 ב-Azure Machine Learning.

בתרגיל זה תבצעו:

- הוספת קוד לקובץ *download_dataset.py* להורדת מערכי הנתונים.  
- הרצת קובץ *download_dataset.py* להורדת מערכי נתונים לסביבה המקומית.

#### הורדת מערכי נתונים באמצעות *download_dataset.py*

1. פתחו את קובץ *download_dataset.py* ב-Visual Studio Code.

1. הוסיפו את הקוד הבא לקובץ *download_dataset.py*.

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

1. הקלידו את הפקודה הבאה בטרמינל להרצת הסקריפט ולהורדת מערכי הנתונים לסביבה המקומית.

    ```console
    python download_dataset.py
    ```

1. ודאו שמערכי הנתונים נשמרו בהצלחה בתיקיית *finetune-phi/data* המקומית שלכם.

> [!NOTE]  
>
> #### הערה על גודל מערך הנתונים וזמן הכוונון  
>
> במדריך זה, תשתמשו רק ב-1% ממערך הנתונים (`split='train[:1%]'`). זה מפחית משמעותית את כמות הנתונים, ומזרז את תהליכי ההעלאה והכוונון. ניתן להתאים את האחוז למציאת האיזון בין זמן הכשרה לביצועי המודל. שימוש בתת-קבוצה קטנה של מערך הנתונים מקצר את זמן הכוונון, מה שהופך את התהליך לנוח יותר עבור מדריך זה.

## תרחיש 2: כוונון מודל Phi-3 ופריסתו ב-Azure Machine Learning Studio

### כוונון מודל Phi-3

בתרגיל
1. בקרו ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחרו **Compute** מתפריט הצד השמאלי.

1. בחרו **Compute clusters** מתפריט הניווט.

1. בחרו **+ New**.

    ![בחרו Compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.he.png)

1. בצעו את הפעולות הבאות:

    - בחרו את ה-**Region** שבו תרצו להשתמש.
    - בחרו את **Virtual machine tier** ל-**Dedicated**.
    - בחרו את **Virtual machine type** ל-**GPU**.
    - הגדירו את מסנן **Virtual machine size** ל-**Select from all options**.
    - בחרו את **Virtual machine size** ל-**Standard_NC24ads_A100_v4**.

    ![צרו Cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.he.png)

1. בחרו **Next**.

1. בצעו את הפעולות הבאות:

    - הזינו **Compute name**. יש לוודא שהוא ייחודי.
    - הגדירו את **Minimum number of nodes** ל-**0**.
    - הגדירו את **Maximum number of nodes** ל-**1**.
    - הגדירו את **Idle seconds before scale down** ל-**120**.

    ![צרו Cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.he.png)

1. בחרו **Create**.

#### כוונון עדין למודל Phi-3

1. בקרו ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחרו את סביבת העבודה של Azure Machine Learning שיצרתם.

    ![בחרו את סביבת העבודה שיצרתם.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.he.png)

1. בצעו את הפעולות הבאות:

    - בחרו **Model catalog** מתפריט הצד השמאלי.
    - הקלידו *phi-3-mini-4k* ב-**search bar** ובחרו **Phi-3-mini-4k-instruct** מהאפשרויות שמופיעות.

    ![הקלידו phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.he.png)

1. בחרו **Fine-tune** מתפריט הניווט.

    ![בחרו Fine-tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.he.png)

1. בצעו את הפעולות הבאות:

    - בחרו **Select task type** ל-**Chat completion**.
    - בחרו **+ Select data** להעלאת **Training data**.
    - בחרו את סוג העלאת נתוני האימות ל-**Provide different validation data**.
    - בחרו **+ Select data** להעלאת **Validation data**.

    ![מלאו את עמודת הכוונון העדין.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.he.png)

    > [!TIP]
    >
    > ניתן לבחור **Advanced settings** כדי להתאים אישית הגדרות כמו **learning_rate** ו-**lr_scheduler_type** לשיפור תהליך הכוונון העדין בהתאם לצרכים שלכם.

1. בחרו **Finish**.

1. בתרגיל זה, ביצעתם כוונון עדין למודל Phi-3 באמצעות Azure Machine Learning. שימו לב שתהליך הכוונון העדין עשוי לקחת זמן רב. לאחר הרצת משימת הכוונון העדין, תצטרכו להמתין לסיומה. ניתן לעקוב אחר סטטוס משימת הכוונון העדין על ידי מעבר ללשונית Jobs בצד השמאלי של סביבת העבודה של Azure Machine Learning. בסדרה הבאה, תפרסו את המודל שעבר כוונון ותשלבו אותו עם Prompt Flow.

    ![ראו את משימת הכוונון העדין.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.he.png)

### פריסת המודל Phi-3 שעבר כוונון עדין

כדי לשלב את המודל Phi-3 שעבר כוונון עדין עם Prompt Flow, יש לפרוס את המודל כך שיהיה נגיש להסקת מסקנות בזמן אמת. תהליך זה כולל רישום המודל, יצירת נקודת קצה מקוונת ופריסת המודל.

בתרגיל זה, תבצעו את השלבים הבאים:

- תרשמו את המודל שעבר כוונון עדין בסביבת העבודה של Azure Machine Learning.
- תיצרו נקודת קצה מקוונת.
- תפרסו את המודל Phi-3 שעבר כוונון עדין.

#### רישום המודל שעבר כוונון עדין

1. בקרו ב-[Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. בחרו את סביבת העבודה של Azure Machine Learning שיצרתם.

    ![בחרו את סביבת העבודה שיצרתם.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.he.png)

1. בחרו **Models** מתפריט הצד השמאלי.
1. בחרו **+ Register**.
1. בחרו **From a job output**.

    ![רשמו מודל.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.he.png)

1. בחרו את המשימה שיצרתם.

    ![בחרו משימה.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.he.png)

1. בחרו **Next**.

1. בחרו **Model type** ל-**MLflow**.

1. ודאו ש-**Job output** נבחר; הוא אמור להיבחר אוטומטית.

    ![בחרו Output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.he.png)

2. בחרו **Next**.

3. בחרו **Register**.

    ![בחרו Register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.he.png)

4. ניתן לראות את המודל הרשום על ידי מעבר לתפריט **Models** מתפריט הצד השמאלי.

    ![מודל רשום.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.he.png)

#### פריסת המודל שעבר כוונון עדין

1. עברו לסביבת העבודה של Azure Machine Learning שיצרתם.

1. בחרו **Endpoints** מתפריט הצד השמאלי.

1. בחרו **Real-time endpoints** מתפריט הניווט.

    ![צרו נקודת קצה.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.he.png)

1. בחרו **Create**.

1. בחרו את המודל הרשום שיצרתם.

    ![בחרו מודל רשום.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.he.png)

1. בחרו **Select**.

1. בצעו את הפעולות הבאות:

    - בחרו **Virtual machine** ל-*Standard_NC6s_v3*.
    - בחרו את מספר ה-**Instance count** שבו תרצו להשתמש, לדוגמה, *1*.
    - בחרו את **Endpoint** ל-**New** כדי ליצור נקודת קצה.
    - הזינו **Endpoint name**. יש לוודא שהוא ייחודי.
    - הזינו **Deployment name**. יש לוודא שהוא ייחודי.

    ![מלאו את הגדרות הפריסה.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.he.png)

1. בחרו **Deploy**.

> [!WARNING]
> כדי להימנע מחיובים נוספים בחשבונכם, ודאו שאתם מוחקים את נקודת הקצה שיצרתם בסביבת העבודה של Azure Machine Learning.
>

#### בדיקת סטטוס הפריסה בסביבת העבודה של Azure Machine Learning

1. עברו לסביבת העבודה של Azure Machine Learning שיצרתם.

1. בחרו **Endpoints** מתפריט הצד השמאלי.

1. בחרו את נקודת הקצה שיצרתם.

    ![בחרו נקודות קצה.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.he.png)

1. בעמוד זה, תוכלו לנהל את נקודות הקצה במהלך תהליך הפריסה.

> [!NOTE]
> לאחר השלמת הפריסה, ודאו ש-**Live traffic** מוגדר ל-**100%**. אם לא, בחרו **Update traffic** כדי להתאים את הגדרות התעבורה. שימו לב שלא ניתן לבדוק את המודל אם התעבורה מוגדרת ל-0%.
>
> ![הגדירו תעבורה.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.he.png)
>

## תרחיש 3: שילוב עם Prompt Flow ושיחה עם המודל המותאם אישית שלכם ב-Azure AI Foundry

### שילוב המודל Phi-3 המותאם אישית עם Prompt Flow

לאחר פריסת המודל שעבר כוונון עדין, ניתן לשלב אותו עם Prompt Flow לשימוש בזמן אמת, המאפשר מגוון משימות אינטראקטיביות עם המודל Phi-3 המותאם אישית שלכם.

בתרגיל זה, תבצעו את השלבים הבאים:

- תיצרו Hub ב-Azure AI Foundry.
- תיצרו פרויקט ב-Azure AI Foundry.
- תיצרו Prompt Flow.
- תוסיפו חיבור מותאם אישית למודל Phi-3 המותאם אישית.
- תגדירו את Prompt Flow לשיחה עם המודל Phi-3 המותאם אישית שלכם.

> [!NOTE]
> ניתן גם לשלב עם Prompt Flow באמצעות Azure ML Studio. תהליך השילוב זהה גם ב-Azure ML Studio.

#### יצירת Hub ב-Azure AI Foundry

יש ליצור Hub לפני יצירת פרויקט. Hub פועל כקבוצת משאבים, ומאפשר לארגן ולנהל פרויקטים מרובים ב-Azure AI Foundry.

1. בקרו ב-[Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. בחרו **All hubs** מתפריט הצד השמאלי.

1. בחרו **+ New hub** מתפריט הניווט.

    ![צרו Hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.he.png)

1. בצעו את הפעולות הבאות:

    - הזינו **Hub name**. יש לוודא שהוא ייחודי.
    - בחרו את **Subscription** שלכם ב-Azure.
    - בחרו את קבוצת המשאבים (**Resource group**) לשימוש (צרו חדשה במידת הצורך).
    - בחרו את **Location** שבו תרצו להשתמש.
    - בחרו את **Connect Azure AI Services** לשימוש (צרו חדש במידת הצורך).
    - בחרו **Connect Azure AI Search** ל-**Skip connecting**.

    ![מלאו את פרטי ה-Hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.he.png)

1. בחרו **Next**.

#### יצירת פרויקט ב-Azure AI Foundry

1. ב-Hub שיצרתם, בחרו **All projects** מתפריט הצד השמאלי.

1. בחרו **+ New project** מתפריט הניווט.

    ![בחרו פרויקט חדש.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.he.png)

1. הזינו **Project name**. יש לוודא שהוא ייחודי.

    ![צרו פרויקט.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.he.png)

1. בחרו **Create a project**.

#### הוספת חיבור מותאם אישית למודל Phi-3 המותאם אישית

כדי לשלב את המודל Phi-3 המותאם אישית שלכם עם Prompt Flow, עליכם לשמור את נקודת הקצה והמפתח של המודל בחיבור מותאם אישית. הגדרה זו מבטיחה גישה למודל המותאם אישית שלכם ב-Prompt Flow.

#### הגדרת מפתח API וכתובת URI של נקודת הקצה למודל Phi-3 המותאם אישית

1. בקרו ב-[Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. עברו לסביבת העבודה של Azure Machine Learning שיצרתם.

1. בחרו **Endpoints** מתפריט הצד השמאלי.

    ![בחרו נקודות קצה.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.he.png)

1. בחרו את נקודת הקצה שיצרתם.

    ![בחרו נקודות קצה.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.he.png)

1. בחרו **Consume** מתפריט הניווט.

1. העתיקו את **REST endpoint** ואת **Primary key** שלכם.
![העתקת מפתח API וכתובת URI של נקודת קצה.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.he.png)

#### הוספת חיבור מותאם אישית

1. בקרו ב-[Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. נווטו לפרויקט Azure AI Foundry שיצרתם.

1. בפרויקט שיצרתם, בחרו **Settings** מהתפריט בצד שמאל.

1. בחרו **+ New connection**.

    ![בחרו חיבור חדש.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.he.png)

1. בחרו **Custom keys** מתפריט הניווט.

    ![בחרו מפתחות מותאמים אישית.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.he.png)

1. בצעו את המשימות הבאות:

    - בחרו **+ Add key value pairs**.
    - בשם המפתח, הזינו **endpoint** והדביקו את נקודת הקצה שהעתקתם מ-Azure ML Studio לשדה הערך.
    - בחרו **+ Add key value pairs** שוב.
    - בשם המפתח, הזינו **key** והדביקו את המפתח שהעתקתם מ-Azure ML Studio לשדה הערך.
    - לאחר הוספת המפתחות, בחרו **is secret** כדי למנוע חשיפת המפתח.

    ![הוספת חיבור.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.he.png)

1. בחרו **Add connection**.

#### יצירת Prompt flow

הוספתם חיבור מותאם אישית ב-Azure AI Foundry. עכשיו, בואו ניצור Prompt flow באמצעות השלבים הבאים. לאחר מכן, תחברו את ה-Prompt flow לחיבור המותאם כדי שתוכלו להשתמש במודל המותאם אישית בתוך ה-Prompt flow.

1. נווטו לפרויקט Azure AI Foundry שיצרתם.

1. בחרו **Prompt flow** מהתפריט בצד שמאל.

1. בחרו **+ Create** מתפריט הניווט.

    ![בחרו Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.he.png)

1. בחרו **Chat flow** מתפריט הניווט.

    ![בחרו Chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.he.png)

1. הזינו **Folder name** לשימוש.

    ![הזנת שם.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.he.png)

2. בחרו **Create**.

#### הגדרת Prompt flow לצ'אט עם מודל Phi-3 המותאם אישית שלכם

עליכם לשלב את מודל Phi-3 המותאם אישית ב-Prompt flow. עם זאת, ה-Prompt flow הקיים אינו מותאם למטרה זו. לכן, יש לעצב מחדש את ה-Prompt flow כדי לאפשר את שילוב המודל המותאם.

1. ב-Prompt flow, בצעו את המשימות הבאות כדי לבנות מחדש את הזרימה הקיימת:

    - בחרו **Raw file mode**.
    - מחקו את כל הקוד הקיים בקובץ *flow.dag.yml*.
    - הוסיפו את הקוד הבא לקובץ *flow.dag.yml*.

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

    - בחרו **Save**.

    ![בחרו מצב קובץ גולמי.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.he.png)

1. הוסיפו את הקוד הבא לקובץ *integrate_with_promptflow.py* כדי להשתמש במודל Phi-3 המותאם אישית ב-Prompt flow.

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

    ![הדבקת קוד Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.he.png)

> [!NOTE]
> למידע מפורט יותר על השימוש ב-Prompt flow ב-Azure AI Foundry, ניתן לעיין ב-[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. בחרו **Chat input**, **Chat output** כדי לאפשר צ'אט עם המודל שלכם.

    ![קלט ופלט.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.he.png)

1. כעת אתם מוכנים לצ'אט עם מודל Phi-3 המותאם אישית שלכם. בתרגיל הבא תלמדו כיצד להפעיל את ה-Prompt flow ולהשתמש בו לצ'אט עם המודל המותאם.

> [!NOTE]
>
> הזרימה החדשה צריכה להיראות כמו בתמונה למטה:
>
> ![דוגמה לזרימה.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.he.png)
>

### צ'אט עם מודל Phi-3 המותאם אישית שלכם

כעת, לאחר שהתאמתם ושילבתם את מודל Phi-3 המותאם אישית שלכם עם Prompt flow, אתם מוכנים להתחיל לתקשר איתו. תרגיל זה ינחה אתכם בתהליך ההגדרה וההפעלה של צ'אט עם המודל שלכם באמצעות Prompt flow. על ידי ביצוע השלבים, תוכלו לנצל את היכולות של מודל Phi-3 המותאם שלכם למשימות ושיחות שונות.

- צ'אט עם מודל Phi-3 המותאם אישית שלכם באמצעות Prompt flow.

#### הפעלת Prompt flow

1. בחרו **Start compute sessions** כדי להפעיל את ה-Prompt flow.

    ![הפעלת session חישוב.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.he.png)

1. בחרו **Validate and parse input** כדי לחדש פרמטרים.

    ![אימות קלט.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.he.png)

1. בחרו את **Value** של ה-**connection** לחיבור המותאם שיצרתם. לדוגמה, *connection*.

    ![חיבור.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.he.png)

#### צ'אט עם המודל המותאם אישית שלכם

1. בחרו **Chat**.

    ![בחרו Chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.he.png)

1. דוגמה לתוצאות: כעת תוכלו לצ'אט עם מודל Phi-3 המותאם אישית שלכם. מומלץ לשאול שאלות המבוססות על הנתונים ששימשו להתאמה.

    ![צ'אט עם Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. אנו לא נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.