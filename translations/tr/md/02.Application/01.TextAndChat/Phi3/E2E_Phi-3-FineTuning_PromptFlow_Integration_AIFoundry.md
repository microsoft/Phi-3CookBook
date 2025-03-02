# Azure AI Foundry'de Prompt Flow ile Özel Phi-3 Modellerini İnce Ayar Yapma ve Entegre Etme

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'deki "[Azure AI Foundry'de Prompt Flow ile Özel Phi-3 Modellerini İnce Ayar Yapma ve Entegre Etme](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" rehberine dayanmaktadır. Özel Phi-3 modellerinin ince ayar yapılması, dağıtılması ve Prompt Flow ile entegre edilmesi süreçlerini tanıtmaktadır.  
Bu öğretici, "[Prompt Flow ile Özel Phi-3 Modellerini İnce Ayar Yapma ve Entegre Etme](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" başlıklı E2E örneğinden farklı olarak, kodun yerel olarak çalıştırılmasını değil, modelinizin tamamen Azure AI / ML Studio içinde ince ayar yapılmasını ve entegre edilmesini ele alır.

## Genel Bakış

Bu E2E örneğinde, Phi-3 modeline nasıl ince ayar yapılacağını ve Azure AI Foundry'de Prompt Flow ile nasıl entegre edileceğini öğreneceksiniz. Azure AI / ML Studio'yu kullanarak, özel AI modellerini dağıtmak ve kullanmak için bir iş akışı oluşturacaksınız. Bu E2E örneği üç senaryoya ayrılmıştır:

**Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık yapma**

**Senaryo 2: Phi-3 modeline ince ayar yapma ve Azure Machine Learning Studio'da dağıtma**

**Senaryo 3: Prompt Flow ile entegre etme ve Azure AI Foundry'de özel modelinizle sohbet etme**

Bu E2E örneğinin genel bir görünümü aşağıda verilmiştir.

![Phi-3-FineTuning_PromptFlow_Integration Genel Bakış.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.tr.png)

### İçindekiler

1. **[Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık yapma](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Azure Machine Learning Çalışma Alanı oluşturma](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Azure Aboneliğinde GPU kotaları talep etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Rol ataması ekleme](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Projeyi kurma](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [İnce ayar için veri kümesini hazırlama](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Senaryo 2: Phi-3 modeline ince ayar yapma ve Azure Machine Learning Studio'da dağıtma](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Phi-3 modeline ince ayar yapma](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [İnce ayar yapılmış Phi-3 modelini dağıtma](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Senaryo 3: Prompt Flow ile entegre etme ve Azure AI Foundry'de özel modelinizle sohbet etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Özel Phi-3 modelini Prompt Flow ile entegre etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Özel Phi-3 modelinizle sohbet etme](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## Senaryo 1: Azure kaynaklarını kurma ve ince ayar için hazırlık yapma

### Azure Machine Learning Çalışma Alanı oluşturma

1. Portal sayfasının üst kısmındaki **arama çubuğuna** *azure machine learning* yazın ve çıkan seçeneklerden **Azure Machine Learning**'i seçin.

    ![Azure machine learning yazın.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.tr.png)

2. Gezinti menüsünden **+ Oluştur** seçeneğini seçin.

3. Gezinti menüsünden **Yeni çalışma alanı** seçeneğini seçin.

    ![Yeni çalışma alanı seçin.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.tr.png)

4. Aşağıdaki görevleri gerçekleştirin:

    - Azure **Aboneliğinizi** seçin.
    - Kullanmak istediğiniz **Kaynak grubunu** seçin (gerekirse yeni bir tane oluşturun).
    - **Çalışma Alanı Adı** girin. Bu değer benzersiz olmalıdır.
    - Kullanmak istediğiniz **Bölgeyi** seçin.
    - Kullanmak istediğiniz **Depolama hesabını** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Anahtar kasasını** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Uygulama içgörülerini** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Kapsayıcı kaydını** seçin (gerekirse yeni bir tane oluşturun).

    ![Azure machine learning bilgilerini doldurun.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.tr.png)

5. **Gözden Geçir + Oluştur** seçeneğini seçin.

6. **Oluştur** seçeneğini seçin.

### Azure Aboneliğinde GPU kotaları talep etme

Bu öğreticide, Phi-3 modeline ince ayar yapmayı ve bir GPU kullanarak dağıtmayı öğreneceksiniz. İnce ayar için *Standard_NC24ads_A100_v4* GPU'sunu kullanacaksınız, bu da bir kota talebi gerektirir. Dağıtım için ise *Standard_NC6s_v3* GPU'sunu kullanacaksınız, bu da bir kota talebi gerektirir.

> [!NOTE]  
> Yalnızca Kullan-Öde abonelikleri (standart abonelik türü) GPU tahsisi için uygundur; avantaj abonelikleri şu anda desteklenmemektedir.

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. *Standard NCADSA100v4 Family* kotası talep etmek için şu görevleri gerçekleştirin:

    - Sol taraftaki sekmeden **Kota** seçeneğini seçin.
    - Kullanmak istediğiniz **Sanal makine ailesini** seçin. Örneğin, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* seçeneğini seçin, bu *Standard_NC24ads_A100_v4* GPU'yu içerir.
    - Gezinti menüsünden **Kota talep et** seçeneğini seçin.

        ![Kota talep et.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.tr.png)

    - Kota talep etme sayfasında, kullanmak istediğiniz **Yeni çekirdek limiti** değerini girin. Örneğin, 24.
    - Kota talep etme sayfasında **Gönder** seçeneğini seçerek GPU kotasını talep edin.

1. *Standard NCSv3 Family* kotası talep etmek için şu görevleri gerçekleştirin:

    - Sol taraftaki sekmeden **Kota** seçeneğini seçin.
    - Kullanmak istediğiniz **Sanal makine ailesini** seçin. Örneğin, *Standard NCSv3 Family Cluster Dedicated vCPUs* seçeneğini seçin, bu *Standard_NC6s_v3* GPU'yu içerir.
    - Gezinti menüsünden **Kota talep et** seçeneğini seçin.
    - Kota talep etme sayfasında, kullanmak istediğiniz **Yeni çekirdek limiti** değerini girin. Örneğin, 24.
    - Kota talep etme sayfasında **Gönder** seçeneğini seçerek GPU kotasını talep edin.

### Rol ataması ekleme

Modellerinizi ince ayar yapmak ve dağıtmak için önce bir Kullanıcı Atamalı Yönetilen Kimlik (UAI) oluşturmanız ve uygun izinleri atamanız gerekir. Bu UAI, dağıtım sırasında kimlik doğrulama için kullanılacaktır.

#### Kullanıcı Atamalı Yönetilen Kimlik (UAI) Oluşturma

1. Portal sayfasının üst kısmındaki **arama çubuğuna** *managed identities* yazın ve çıkan seçeneklerden **Yönetilen Kimlikler**'i seçin.

    ![Yönetilen kimlikler yazın.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.tr.png)

1. **+ Oluştur** seçeneğini seçin.

    ![Oluştur'u seçin.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - Azure **Aboneliğinizi** seçin.
    - Kullanmak istediğiniz **Kaynak grubunu** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Bölgeyi** seçin.
    - **Ad** girin. Bu değer benzersiz olmalıdır.

    ![Yönetilen kimlik bilgilerini doldurun.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.tr.png)

1. **Gözden Geçir + Oluştur** seçeneğini seçin.

1. **+ Oluştur** seçeneğini seçin.

#### Yönetilen Kimlik için Katkıda Bulunan Rol Ataması Ekleme

1. Oluşturduğunuz Yönetilen Kimlik kaynağına gidin.

1. Sol taraftaki sekmeden **Azure rol atamaları** seçeneğini seçin.

1. Gezinti menüsünden **+Rol ataması ekle** seçeneğini seçin.

1. Rol atama sayfasında şu görevleri gerçekleştirin:
    - **Kapsamı** **Kaynak grubu** olarak seçin.
    - Azure **Aboneliğinizi** seçin.
    - Kullanmak istediğiniz **Kaynak grubunu** seçin.
    - **Rolü** **Katkıda Bulunan** olarak seçin.

    ![Katkıda bulunan rolü doldurun.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.tr.png)

2. **Kaydet** seçeneğini seçin. 

#### Storage Blob Veri Okuyucu Rol Ataması Ekleme

1. Portalın üst kısmındaki **arama çubuğuna** *storage accounts* yazın ve çıkan seçeneklerden **Depolama hesapları**'nı seçin.

    ![Depolama hesapları yazın.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.tr.png)

1. Azure Machine Learning çalışma alanınızla ilişkili depolama hesabını seçin. Örneğin, *finetunephistorage*.

1. Rol atama sayfasına gitmek için şu görevleri gerçekleştirin:

    - Oluşturduğunuz Azure Depolama hesabına gidin.
    - Sol taraftaki sekmeden **Erişim Kontrolü (IAM)** seçeneğini seçin.
    - Gezinti menüsünden **+ Ekle** seçeneğini seçin.
    - Gezinti menüsünden **Rol ataması ekle** seçeneğini seçin.

    ![Rol ekle.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.tr.png)

1. Rol atama sayfasında şu görevleri gerçekleştirin:

    - Rol sayfasında **Storage Blob Veri Okuyucu** yazın ve çıkan seçeneklerden **Storage Blob Veri Okuyucu**'yu seçin.
    - Rol sayfasında **İleri** seçeneğini seçin.
    - Üyeler sayfasında **Erişim atamasını** **Yönetilen kimlik** olarak seçin.
    - Üyeler sayfasında **+ Üyeleri seç** seçeneğini seçin.
    - Yönetilen kimlikleri seç sayfasında Azure **Aboneliğinizi** seçin.
    - Yönetilen kimlikleri seç sayfasında **Yönetilen kimliği** seçin.
    - Yönetilen kimlikleri seç sayfasında oluşturduğunuz Yönetilen Kimliği seçin. Örneğin, *finetunephi-managedidentity*.
    - Yönetilen kimlikleri seç sayfasında **Seç** seçeneğini seçin.

    ![Yönetilen kimliği seçin.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.tr.png)

1. **Gözden Geçir + Ata** seçeneğini seçin. 

#### AcrPull Rol Ataması Ekleme

1. Portalın üst kısmındaki **arama çubuğuna** *container registries* yazın ve çıkan seçeneklerden **Kapsayıcı kayıtları**'nı seçin.

    ![Kapsayıcı kayıtları yazın.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.tr.png)

1. Azure Machine Learning çalışma alanınızla ilişkili kapsayıcı kaydını seçin. Örneğin, *finetunephicontainerregistry*.

1. Rol atama sayfasına gitmek için şu görevleri gerçekleştirin:

    - Sol taraftaki sekmeden **Erişim Kontrolü (IAM)** seçeneğini seçin.
    - Gezinti menüsünden **+ Ekle** seçeneğini seçin.
    - Gezinti menüsünden **Rol ataması ekle** seçeneğini seçin.

1. Rol atama sayfasında şu görevleri gerçekleştirin:

    - Rol sayfasında **AcrPull** yazın ve çıkan seçeneklerden **AcrPull**'u seçin.
    - Rol sayfasında **İleri** seçeneğini seçin.
    - Üyeler sayfasında **Erişim atamasını** **Yönetilen kimlik** olarak seçin.
    - Üyeler sayfasında **+ Üyeleri seç** seçeneğini seçin.
    - Yönetilen kimlikleri seç sayfasında Azure **Aboneliğinizi** seçin.
    - Yönetilen kimlikleri seç sayfasında **Yönetilen kimliği** seçin.
    - Yönetilen kimlikleri seç sayfasında oluşturduğunuz Yönetilen Kimliği seçin. Örneğin, *finetunephi-managedidentity*.
    - Yönetilen kimlikleri seç sayfasında **Seç** seçeneğini seçin.
    - **Gözden Geçir + Ata** seçeneğini seçin.

### Projeyi Kurma

İnce ayar için gereken veri kümelerini indirmek amacıyla bir yerel ortam oluşturacaksınız.

Bu alıştırmada şunları yapacaksınız:

- Çalışmak için bir klasör oluşturma.
- Bir sanal ortam oluşturma.
- Gerekli paketleri yükleme.
- Veri setini indirmek için bir *download_dataset.py* dosyası oluşturma.

#### Çalışmak için bir klasör oluşturma

1. Bir terminal penceresi açın ve varsayılan yolda *finetune-phi* adlı bir klasör oluşturmak için aşağıdaki komutu yazın:

    ```console
    mkdir finetune-phi
    ```

2. Oluşturduğunuz *finetune-phi* klasörüne gitmek için terminalinize şu komutu yazın:

    ```console
    cd finetune-phi
    ```

#### Sanal ortam oluşturma

1. Terminalinize aşağıdaki komutu yazarak *.venv* adlı bir sanal ortam oluşturun:

    ```console
    python -m venv .venv
    ```

2. Terminalinize aşağıdaki komutu yazarak sanal ortamı etkinleştirin:

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> Eğer çalıştıysa, komut isteminden önce *(.venv)* görmelisiniz.

#### Gerekli paketleri yükleme

1. Terminalinize aşağıdaki komutları yazarak gerekli paketleri yükleyin:

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` Oluşturma

> [!NOTE]  
> Tam klasör yapısı:  
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**'u açın.

1. Menü çubuğundan **Dosya** seçeneğini seçin.

1. **Klasör Aç** seçeneğini seçin.

1. *C:\Users\yourUserName\finetune-phi* konumunda oluşturduğunuz *finetune-phi* klasörünü seçin.

    ![Oluşturduğunuz klasörü seçin.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.tr.png)

1. Visual Studio Code'un sol panelinde sağ tıklayın ve **Yeni Dosya** seçeneğini seçerek *download_dataset.py* adlı yeni bir dosya oluşturun.

    ![Yeni bir dosya oluşturun.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.tr.png)

### İnce Ayar için Veri Kümesini Hazırlama

Bu alıştırmada, *download_dataset.py* dosyasını çalıştırarak *ultrachat_200k* veri kümelerini yerel ortamınıza indireceksiniz. Daha sonra bu veri kümelerini Azure Machine Learning'de Phi-3 modeline ince ayar yapmak için kullanacaksınız.

Bu alıştırmada şunları yapacaksınız:

- Veri kümelerini indirmek için *download_dataset.py* dosyasına kod ekleme.
- Veri kümelerini yerel ortamınıza indirmek için *download_dataset.py* dosyasını çalıştırma.

#### *download_dataset.py* Kullanarak Veri Kümen
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Sol taraftaki sekmeden **Hesaplama** seçeneğini seçin.

1. Navigasyon menüsünden **Hesaplama kümeleri** seçeneğini seçin.

1. **+ Yeni** seçeneğini seçin.

    ![Hesaplama seçin.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - Kullanmak istediğiniz **Bölge**yi seçin.
    - **Sanal makine katmanı**nı **Dedicated** olarak ayarlayın.
    - **Sanal makine türü**nü **GPU** olarak ayarlayın.
    - **Sanal makine boyutu** filtresini **Tüm seçeneklerden seç** olarak ayarlayın.
    - **Sanal makine boyutu**nu **Standard_NC24ads_A100_v4** olarak seçin.

    ![Küme oluşturun.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.tr.png)

1. **İleri** seçeneğini seçin.

1. Aşağıdaki görevleri gerçekleştirin:

    - **Hesaplama adı** girin. Bu değer benzersiz olmalıdır.
    - **Düğüm sayısı (minimum)** değerini **0** olarak ayarlayın.
    - **Düğüm sayısı (maksimum)** değerini **1** olarak ayarlayın.
    - **İndirgenmeden önceki boşta geçen saniye** değerini **120** olarak ayarlayın.

    ![Küme oluşturun.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.tr.png)

1. **Oluştur** seçeneğini seçin.

#### Phi-3 Modelini İnce Ayar Yapma

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Oluşturduğunuz çalışma alanını seçin.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - Sol taraftaki sekmeden **Model kataloğu** seçeneğini seçin.
    - **Arama çubuğu**na *phi-3-mini-4k* yazın ve çıkan seçeneklerden **Phi-3-mini-4k-instruct** modelini seçin.

    ![phi-3-mini-4k yazın.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.tr.png)

1. Navigasyon menüsünden **İnce ayar yap** seçeneğini seçin.

    ![İnce ayar seçin.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - **Görev türü seçin** kısmını **Sohbet tamamlama** olarak ayarlayın.
    - **+ Veri seç** seçeneğini seçerek **Eğitim verilerini** yükleyin.
    - Doğrulama veri yükleme türünü **Farklı doğrulama verisi sağlayın** olarak ayarlayın.
    - **+ Veri seç** seçeneğini seçerek **Doğrulama verilerini** yükleyin.

    ![İnce ayar sayfasını doldurun.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.tr.png)

    > [!TIP]
    >
    > **Gelişmiş ayarlar** seçeneğini belirleyerek, ince ayar sürecini özel ihtiyaçlarınıza göre optimize etmek için **learning_rate** ve **lr_scheduler_type** gibi yapılandırmaları özelleştirebilirsiniz.

1. **Bitir** seçeneğini seçin.

1. Bu alıştırmada, Azure Machine Learning kullanarak Phi-3 modeline başarıyla ince ayar yaptınız. Lütfen ince ayar sürecinin oldukça uzun sürebileceğini unutmayın. İnce ayar işi çalıştırıldıktan sonra tamamlanmasını beklemeniz gerekecek. İnce ayar işinin durumunu, Azure Machine Learning Çalışma Alanınızdaki sol taraftaki **İşler** sekmesine giderek izleyebilirsiniz. Bir sonraki seride, ince ayar yapılan modeli dağıtacak ve Prompt flow ile entegre edeceksiniz.

    ![İnce ayar işini görün.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.tr.png)

### İnce Ayar Yapılmış Phi-3 Modelini Dağıtma

İnce ayar yapılmış Phi-3 modelini Prompt flow ile entegre etmek için modeli gerçek zamanlı tahminler için erişilebilir hale getirmek üzere dağıtmanız gerekir. Bu işlem, modeli kaydetmeyi, bir çevrimiçi uç nokta oluşturmayı ve modeli dağıtmayı içerir.

Bu alıştırmada:

- İnce ayar yapılmış modeli Azure Machine Learning çalışma alanına kaydedeceksiniz.
- Bir çevrimiçi uç nokta oluşturacaksınız.
- Kayıtlı ince ayar yapılmış Phi-3 modelini dağıtacaksınız.

#### İnce Ayar Yapılmış Modeli Kaydetme

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanını seçin.

    ![Oluşturduğunuz çalışma alanını seçin.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.tr.png)

1. Sol taraftaki sekmeden **Modeller** seçeneğini seçin.  
1. **+ Kaydet** seçeneğini seçin.  
1. **Bir iş çıktısından** seçeneğini seçin.

    ![Model kaydetme.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.tr.png)

1. Oluşturduğunuz işi seçin.

    ![İşi seçin.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.tr.png)

1. **İleri** seçeneğini seçin.

1. **Model türü**nü **MLflow** olarak seçin.

1. **İş çıktısı**nın seçili olduğundan emin olun; bu otomatik olarak seçilmiş olmalıdır.

    ![Çıktıyı seçin.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.tr.png)

2. **İleri** seçeneğini seçin.

3. **Kaydet** seçeneğini seçin.

    ![Kaydet seçeneğini seçin.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.tr.png)

4. Sol taraftaki sekmeden **Modeller** menüsüne giderek kaydedilen modelinizi görüntüleyebilirsiniz.

    ![Kaydedilmiş model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.tr.png)

#### İnce Ayar Yapılmış Modeli Dağıtma

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Uç Noktalar** seçeneğini seçin.

1. Navigasyon menüsünden **Gerçek zamanlı uç noktalar** seçeneğini seçin.

    ![Uç nokta oluşturma.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.tr.png)

1. **Oluştur** seçeneğini seçin.

1. Oluşturduğunuz kayıtlı modeli seçin.

    ![Kayıtlı modeli seçin.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.tr.png)

1. **Seç** seçeneğini seçin.

1. Aşağıdaki görevleri gerçekleştirin:

    - **Sanal makine**yi *Standard_NC6s_v3* olarak seçin.
    - Kullanmak istediğiniz **Örnek sayısı**nı seçin. Örneğin, *1*.
    - **Uç Nokta**yı **Yeni** olarak seçerek bir uç nokta oluşturun.
    - **Uç nokta adı** girin. Bu değer benzersiz olmalıdır.
    - **Dağıtım adı** girin. Bu değer benzersiz olmalıdır.

    ![Dağıtım ayarlarını doldurun.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.tr.png)

1. **Dağıt** seçeneğini seçin.

> [!WARNING]
> Hesabınıza ek ücret yansımaması için Azure Machine Learning çalışma alanında oluşturduğunuz uç noktayı silmeyi unutmayın.
>

#### Azure Machine Learning Çalışma Alanında Dağıtım Durumunu Kontrol Etme

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Uç Noktalar** seçeneğini seçin.

1. Oluşturduğunuz uç noktayı seçin.

    ![Uç noktaları seçin](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.tr.png)

1. Bu sayfadan, dağıtım süreci sırasında uç noktaları yönetebilirsiniz.

> [!NOTE]
> Dağıtım tamamlandıktan sonra, **Canlı trafik**in **%100** olarak ayarlandığından emin olun. Eğer değilse, trafik ayarlarını güncellemek için **Trafiği güncelle** seçeneğini seçin. Trafik %0 olarak ayarlanmışsa modeli test edemezsiniz.
>
> ![Trafiği ayarlayın.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.tr.png)
>

## Senaryo 3: Prompt Flow ile Entegre Edin ve Azure AI Foundry'de Özelleştirilmiş Modelinizle Sohbet Edin

### Özelleştirilmiş Phi-3 Modelini Prompt Flow ile Entegre Etme

İnce ayar yapılmış modelinizi başarıyla dağıttıktan sonra, Prompt Flow ile entegre ederek modelinizi gerçek zamanlı uygulamalarda kullanabilirsiniz. Bu, özelleştirilmiş Phi-3 modelinizle çeşitli etkileşimli görevleri gerçekleştirmenizi sağlar.

Bu alıştırmada:

- Azure AI Foundry Hub oluşturacaksınız.
- Azure AI Foundry Projesi oluşturacaksınız.
- Prompt Flow oluşturacaksınız.
- İnce ayar yapılmış Phi-3 modeli için özel bir bağlantı ekleyeceksiniz.
- Prompt Flow'u özelleştirilmiş Phi-3 modelinizle sohbet etmek için yapılandıracaksınız.

> [!NOTE]
> Azure ML Studio kullanarak da Promptflow ile entegrasyon yapabilirsiniz. Aynı entegrasyon süreci Azure ML Studio için de geçerlidir.

#### Azure AI Foundry Hub Oluşturma

Proje oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, bir Kaynak Grubu gibi davranır ve Azure AI Foundry'de birden fazla projeyi organize etmenizi ve yönetmenizi sağlar.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) adresini ziyaret edin.

1. Sol taraftaki sekmeden **Tüm hub'lar** seçeneğini seçin.

1. Navigasyon menüsünden **+ Yeni hub** seçeneğini seçin.

    ![Hub oluşturma.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - **Hub adı** girin. Bu değer benzersiz olmalıdır.
    - Azure **Aboneliğinizi** seçin.
    - Kullanmak istediğiniz **Kaynak grubunu** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Konumu** seçin.
    - Kullanmak istediğiniz **Azure AI Hizmetlerini Bağla** seçeneğini seçin (gerekirse yeni bir tane oluşturun).
    - **Azure AI Aramasını Bağla** seçeneğini **Bağlantıyı atla** olarak ayarlayın.

    ![Hub'ı doldurun.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.tr.png)

1. **İleri** seçeneğini seçin.

#### Azure AI Foundry Projesi Oluşturma

1. Oluşturduğunuz Hub'da, sol taraftaki sekmeden **Tüm projeler** seçeneğini seçin.

1. Navigasyon menüsünden **+ Yeni proje** seçeneğini seçin.

    ![Yeni proje seçin.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.tr.png)

1. **Proje adı** girin. Bu değer benzersiz olmalıdır.

    ![Proje oluşturun.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.tr.png)

1. **Bir proje oluşturun** seçeneğini seçin.

#### İnce Ayar Yapılmış Phi-3 Modeli için Özel Bir Bağlantı Ekleme

Özelleştirilmiş Phi-3 modelinizi Prompt Flow ile entegre etmek için modelin uç noktası ve anahtarını özel bir bağlantıya kaydetmeniz gerekir. Bu kurulum, özelleştirilmiş Phi-3 modelinize Prompt Flow üzerinden erişim sağlar.

#### İnce Ayar Yapılmış Phi-3 Modelinin API Anahtarını ve Uç Nokta URI'sini Ayarlama

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) adresini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol taraftaki sekmeden **Uç Noktalar** seçeneğini seçin.

    ![Uç noktaları seçin.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.tr.png)

1. Oluşturduğunuz uç noktayı seçin.

    ![Oluşturulan uç noktayı seçin.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.tr.png)

1. Navigasyon menüsünden **Tüketim** seçeneğini seçin.

1. **REST uç noktası** ve **Birincil anahtar** bilgilerinizi kopyalayın.
![API anahtarını ve uç nokta URI'sini kopyalayın.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.tr.png)

#### Özel Bağlantıyı Ekle

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) sayfasını ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Oluşturduğunuz projede, sol taraftaki sekmeden **Settings**'i seçin.

1. **+ New connection**'ı seçin.

    ![Yeni bağlantı seçin.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.tr.png)

1. Navigasyon menüsünden **Custom keys**'i seçin.

    ![Özel anahtarları seçin.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - **+ Add key value pairs**'i seçin.
    - Anahtar adı için **endpoint** girin ve Azure ML Studio'dan kopyaladığınız uç noktayı değer alanına yapıştırın.
    - Tekrar **+ Add key value pairs**'i seçin.
    - Anahtar adı için **key** girin ve Azure ML Studio'dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın görünmesini önlemek için **is secret** seçeneğini işaretleyin.

    ![Bağlantı ekleyin.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.tr.png)

1. **Add connection**'ı seçin.

#### Prompt Flow Oluşturun

Azure AI Foundry'de özel bir bağlantı eklediniz. Şimdi, aşağıdaki adımları izleyerek bir Prompt flow oluşturacağız. Daha sonra, bu Prompt flow'u özel bağlantıya bağlayarak, ince ayar yapılmış modeli Prompt flow içinde kullanabilirsiniz.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Sol taraftaki sekmeden **Prompt flow**'u seçin.

1. Navigasyon menüsünden **+ Create**'i seçin.

    ![Promptflow'u seçin.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.tr.png)

1. Navigasyon menüsünden **Chat flow**'u seçin.

    ![Chat flow'u seçin.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.tr.png)

1. Kullanmak istediğiniz **Folder name**'i girin.

    ![İsim girin.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.tr.png)

2. **Create**'i seçin.

#### Özel Phi-3 Modelinizle Sohbet Etmek İçin Prompt Flow'u Ayarlayın

İnce ayar yapılmış Phi-3 modelini bir Prompt flow'a entegre etmeniz gerekiyor. Ancak, mevcut Prompt flow bu amaç için tasarlanmamış. Bu nedenle, özel modeli entegre etmek için Prompt flow'u yeniden tasarlamanız gerekiyor.

1. Prompt flow içinde mevcut akışı yeniden oluşturmak için aşağıdaki görevleri gerçekleştirin:

    - **Raw file mode**'u seçin.
    - *flow.dag.yml* dosyasındaki mevcut tüm kodları silin.
    - Aşağıdaki kodu *flow.dag.yml* dosyasına ekleyin.

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

    - **Save**'i seçin.

    ![Raw file mode'u seçin.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.tr.png)

1. Özel Phi-3 modelini Prompt flow içinde kullanmak için aşağıdaki kodu *integrate_with_promptflow.py* dosyasına ekleyin.

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

    ![Prompt flow kodunu yapıştırın.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.tr.png)

> [!NOTE]
> Azure AI Foundry'de Prompt flow kullanımı hakkında daha ayrıntılı bilgi için [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) sayfasına başvurabilirsiniz.

1. Modelinizle sohbet etmek için **Chat input**, **Chat output**'u seçin.

    ![Giriş Çıkış.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.tr.png)

1. Artık özel Phi-3 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada, Prompt flow'u başlatmayı ve ince ayar yapılmış Phi-3 modelinizle sohbet etmeyi öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulan akış aşağıdaki gibi görünmelidir:
>
> ![Akış örneği.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.tr.png)
>

### Özel Phi-3 Modelinizle Sohbet Edin

Artık özel Phi-3 modelinizi ince ayar yaparak Prompt flow ile entegre ettiniz ve onunla etkileşime geçmeye hazırsınız. Bu alıştırma, modelinizle sohbet etmek için Prompt flow'u kurma ve başlatma sürecinde size rehberlik edecektir. Bu adımları izleyerek, ince ayar yapılmış Phi-3 modelinizin çeşitli görevler ve konuşmalar için tüm yeteneklerinden yararlanabilirsiniz.

- Prompt flow kullanarak özel Phi-3 modelinizle sohbet edin.

#### Prompt Flow'u Başlatın

1. Prompt flow'u başlatmak için **Start compute sessions**'ı seçin.

    ![Hesaplama oturumunu başlatın.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.tr.png)

1. Parametreleri yenilemek için **Validate and parse input**'u seçin.

    ![Girişi doğrulayın.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.tr.png)

1. Oluşturduğunuz özel bağlantıya ait **connection**'ın **Value** değerini seçin. Örneğin, *connection*.

    ![Bağlantı.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.tr.png)

#### Özel Modelinizle Sohbet Edin

1. **Chat**'i seçin.

    ![Sohbet seçin.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.tr.png)

1. İşte bir sonuç örneği: Artık özel Phi-3 modelinizle sohbet edebilirsiniz. İnce ayar sırasında kullanılan verilere dayalı sorular sormanız önerilir.

    ![Prompt flow ile sohbet edin.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.tr.png)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.