# Azure AI Foundry'de Microsoft'un Sorumlu Yapay Zeka İlkelerine Odaklanarak Fine-tune Edilmiş Phi-3 / Phi-3.5 Modelini Değerlendirin

Bu uçtan uca (E2E) örnek, Microsoft Tech Community'deki "[Azure AI Foundry'de Fine-tune Edilmiş Phi-3 / 3.5 Modellerini Değerlendirin: Microsoft'un Sorumlu Yapay Zeka İlkelerine Odaklanarak](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" rehberine dayanmaktadır.

## Genel Bakış

### Azure AI Foundry'de Fine-tune Edilmiş Phi-3 / Phi-3.5 Modelinin Güvenliğini ve Performansını Nasıl Değerlendirebilirsiniz?

Bir modeli fine-tune etmek bazen istenmeyen veya beklenmeyen yanıtlar oluşturmasına neden olabilir. Modelin güvenli ve etkili kalmasını sağlamak için zararlı içerik üretme potansiyelini ve doğru, ilgili ve tutarlı yanıtlar üretme yeteneğini değerlendirmek önemlidir. Bu eğitimde, Azure AI Foundry'de Prompt flow ile entegre edilmiş fine-tune edilmiş Phi-3 / Phi-3.5 modelinin güvenliğini ve performansını nasıl değerlendireceğinizi öğreneceksiniz.

İşte Azure AI Foundry'nin değerlendirme süreci.

![Eğitim mimarisi.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tr.png)

*Görsel Kaynağı: [Yaratıcı Yapay Zeka Uygulamalarının Değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Daha fazla bilgi ve Phi-3 / Phi-3.5 hakkında ek kaynakları keşfetmek için lütfen [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) adresini ziyaret edin.

### Gereksinimler

- [Python](https://www.python.org/downloads)
- [Azure aboneliği](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tune edilmiş Phi-3 / Phi-3.5 modeli

### İçindekiler

1. [**Senaryo 1: Azure AI Foundry'nin Prompt flow değerlendirmesine giriş**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Güvenlik değerlendirmesine giriş](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Performans değerlendirmesine giriş](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Senaryo 2: Azure AI Foundry'de Phi-3 / Phi-3.5 modelini değerlendirme**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Başlamadan önce](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 modelini değerlendirmek için Azure OpenAI'yi dağıtma](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry'nin Prompt flow değerlendirmesini kullanarak fine-tune edilmiş Phi-3 / Phi-3.5 modelini değerlendirme](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Tebrikler!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Senaryo 1: Azure AI Foundry'nin Prompt flow değerlendirmesine giriş**

### Güvenlik değerlendirmesine giriş

Yapay zeka modelinizin etik ve güvenli olduğundan emin olmak için Microsoft'un Sorumlu Yapay Zeka İlkelerine karşı değerlendirilmesi önemlidir. Azure AI Foundry'de güvenlik değerlendirmeleri, modelinizin jailbreak saldırılarına karşı savunmasızlığını ve zararlı içerik üretme potansiyelini değerlendirmenizi sağlar; bu da bu ilkelere doğrudan uyumlu bir süreçtir.

![Güvenlik değerlendirmesi.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.tr.png)

*Görsel Kaynağı: [Yaratıcı Yapay Zeka Uygulamalarının Değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft’un Sorumlu Yapay Zeka İlkeleri

Teknik adımlara başlamadan önce, Microsoft'un Sorumlu Yapay Zeka İlkelerini anlamak önemlidir. Bu etik çerçeve, yapay zeka sistemlerinin sorumlu bir şekilde geliştirilmesi, dağıtılması ve işletilmesini yönlendirmek için tasarlanmıştır. Bu ilkeler, yapay zeka teknolojilerinin adil, şeffaf ve kapsayıcı bir şekilde oluşturulmasını sağlar ve modellerin güvenliğini değerlendirme sürecinin temelini oluşturur.

Microsoft'un Sorumlu Yapay Zeka İlkeleri şunları içerir:

- **Adalet ve Kapsayıcılık**: Yapay zeka sistemleri herkese adil davranmalı ve benzer durumdaki grupları farklı şekilde etkilemekten kaçınmalıdır. Örneğin, bir yapay zeka sistemi tıbbi tedavi, kredi başvuruları veya işe alım konusunda rehberlik sağlarken, benzer semptomlara, mali koşullara veya mesleki niteliklere sahip olan herkese aynı önerilerde bulunmalıdır.

- **Güvenilirlik ve Güvenlik**: Güven oluşturmak için, yapay zeka sistemlerinin güvenilir, güvenli ve tutarlı bir şekilde çalışması kritik öneme sahiptir. Bu sistemler, başlangıçta tasarlandıkları şekilde çalışabilmeli, beklenmedik durumlara güvenli bir şekilde yanıt verebilmeli ve zararlı manipülasyonlara direnç gösterebilmelidir.

- **Şeffaflık**: Yapay zeka sistemleri, insanların hayatlarını büyük ölçüde etkileyen kararları bilgilendirdiğinde, bu kararların nasıl alındığını insanların anlaması kritik öneme sahiptir. Örneğin, bir banka bir kişinin krediye uygun olup olmadığını belirlemek için bir yapay zeka sistemi kullanabilir. Bir şirket, en nitelikli adayları belirlemek için bir yapay zeka sistemi kullanabilir.

- **Gizlilik ve Güvenlik**: Yapay zeka daha yaygın hale geldikçe, gizliliği korumak ve kişisel ve ticari bilgileri güvence altına almak daha önemli ve karmaşık hale geliyor. Yapay zeka ile gizlilik ve veri güvenliği, doğru ve bilgilendirici tahminler ve kararlar almak için verilere erişimin gerekli olması nedeniyle yakın dikkat gerektirir.

- **Hesap Verebilirlik**: Yapay zeka sistemlerini tasarlayan ve dağıtan kişiler, sistemlerinin nasıl çalıştığından sorumlu olmalıdır. Kuruluşlar, hesap verebilirlik normlarını geliştirmek için sektör standartlarından yararlanmalıdır. Bu normlar, yapay zeka sistemlerinin insanların hayatlarını etkileyen herhangi bir kararda nihai otorite olmamasını sağlayabilir.

![Sorumlu Yapay Zeka Merkezi.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.tr.png)

*Görsel Kaynağı: [Sorumlu Yapay Zeka Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft'un Sorumlu Yapay Zeka İlkeleri hakkında daha fazla bilgi edinmek için [Sorumlu Yapay Zeka Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) adresini ziyaret edin.

#### Güvenlik ölçütleri

Bu eğitimde, Azure AI Foundry'nin güvenlik ölçütlerini kullanarak fine-tune edilmiş Phi-3 modelinin güvenliğini değerlendireceksiniz. Bu ölçütler, modelin zararlı içerik üretme potansiyelini ve jailbreak saldırılarına karşı savunmasızlığını değerlendirmenize yardımcı olur. Güvenlik ölçütleri şunları içerir:

- **Kendine zarar verme ile ilgili içerik**: Modelin kendine zarar verme ile ilgili içerik üretme eğilimini değerlendirir.
- **Nefret dolu ve adaletsiz içerik**: Modelin nefret dolu veya adaletsiz içerik üretme eğilimini değerlendirir.
- **Şiddet içeren içerik**: Modelin şiddet içeren içerik üretme eğilimini değerlendirir.
- **Cinsel içerik**: Modelin uygunsuz cinsel içerik üretme eğilimini değerlendirir.

Bu yönleri değerlendirmek, yapay zeka modelinin zararlı veya saldırgan içerik üretmemesini sağlar ve toplumsal değerler ve yasal düzenlemelerle uyumlu hale getirir.

![Güvenlik temelinde değerlendirme.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.tr.png)

### Performans değerlendirmesine giriş

Yapay zeka modelinizin beklenildiği gibi çalıştığından emin olmak için performans ölçütlerine karşı değerlendirilmesi önemlidir. Azure AI Foundry'de performans değerlendirmeleri, modelinizin doğru, ilgili ve tutarlı yanıtlar üretme etkinliğini değerlendirmenizi sağlar.

![Performans değerlendirmesi.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.tr.png)

*Görsel Kaynağı: [Yaratıcı Yapay Zeka Uygulamalarının Değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performans ölçütleri

Bu eğitimde, Azure AI Foundry'nin performans ölçütlerini kullanarak fine-tune edilmiş Phi-3 / Phi-3.5 modelinin performansını değerlendireceksiniz. Bu ölçütler, modelin doğru, ilgili ve tutarlı yanıtlar üretme etkinliğini değerlendirmenize yardımcı olur. Performans ölçütleri şunları içerir:

- **Dayanaklılık**: Üretilen yanıtların giriş kaynağındaki bilgilerle ne kadar uyumlu olduğunu değerlendirir.
- **Alaka düzeyi**: Üretilen yanıtların verilen sorularla ne kadar ilgili olduğunu değerlendirir.
- **Tutarlılık**: Üretilen metnin ne kadar akıcı, doğal okunduğunu ve insan benzeri bir dil oluşturduğunu değerlendirir.
- **Akıcılık**: Üretilen metnin dil yeterliliğini değerlendirir.
- **GPT Benzerliği**: Üretilen yanıtı, gerçeğe uygun olanla benzerlik açısından karşılaştırır.
- **F1 Skoru**: Üretilen yanıt ile kaynak veriler arasındaki ortak kelimelerin oranını hesaplar.

Bu ölçütler, modelin doğru, ilgili ve tutarlı yanıtlar üretme etkinliğini değerlendirmenize yardımcı olur.

![Performans temelinde değerlendirme.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.tr.png)

## **Senaryo 2: Azure AI Foundry'de Phi-3 / Phi-3.5 modelini değerlendirme**

### Başlamadan önce

Bu eğitim, önceki blog yazılarının devamıdır: "[Özel Phi-3 Modellerini Prompt Flow ile Fine-tune Etme ve Entegre Etme: Adım Adım Rehber](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ve "[Azure AI Foundry'de Özel Phi-3 Modellerini Prompt Flow ile Fine-tune Etme ve Entegre Etme](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Bu yazılarda, Azure AI Foundry'de Phi-3 / Phi-3.5 modelini fine-tune etme ve Prompt flow ile entegre etme sürecini ele aldık.

Bu eğitimde, Azure AI Foundry'de bir değerlendirme aracı olarak bir Azure OpenAI modeli dağıtacak ve fine-tune edilmiş Phi-3 / Phi-3.5 modelinizi değerlendirmek için kullanacaksınız.

Bu eğitime başlamadan önce, önceki eğitimlerde açıklanan aşağıdaki gereksinimlere sahip olduğunuzdan emin olun:

1. Fine-tune edilmiş Phi-3 / Phi-3.5 modelini değerlendirmek için hazırlanmış bir veri seti.
1. Azure Machine Learning'e fine-tune edilmiş ve dağıtılmış bir Phi-3 / Phi-3.5 modeli.
1. Azure AI Foundry'de Prompt flow ile entegre edilmiş bir fine-tune edilmiş Phi-3 / Phi-3.5 modeli.

> [!NOTE]
> Fine-tune edilmiş Phi-3 / Phi-3.5 modelini değerlendirmek için, önceki blog yazılarında indirilen **ULTRACHAT_200k** veri setindeki veri klasöründe bulunan *test_data.jsonl* dosyasını kullanacaksınız.

#### Özel Phi-3 / Phi-3.5 modelini Azure AI Foundry'deki Prompt flow ile entegre etme (Kod öncelikli yaklaşım)

> [!NOTE]
> "[Azure AI Foundry'de Özel Phi-3 Modellerini Prompt Flow ile Fine-tune Etme ve Entegre Etme](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" başlıklı düşük kod yaklaşımını izlediyseniz, bu egzersizi atlayıp bir sonrakine geçebilirsiniz. Ancak, "[Özel Phi-3 Modellerini Prompt Flow ile Fine-tune Etme ve Entegre Etme: Adım Adım Rehber](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" başlıklı kod öncelikli yaklaşımı izlediyseniz, modelinizi Prompt flow'a bağlama süreci biraz farklıdır. Bu egzersizde bu süreci öğreneceksiniz.

Fine-tune edilmiş Phi-3 / Phi-3.5 modelinizi Azure AI Foundry'deki Prompt flow'a entegre etmeniz gerekmektedir.

#### Azure AI Foundry Hub Oluşturma

Projeyi oluşturmadan önce bir Hub oluşturmanız gerekir. Hub, bir Kaynak Grubu gibi çalışır ve Azure AI Foundry'de birden fazla Projeyi organize etmenize ve yönetmenize olanak tanır.

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresine giriş yapın.

1. Sol taraftaki sekmeden **Tüm hub'lar** seçeneğini seçin.

1. Navigasyon menüsünden **+ Yeni hub** seçeneğini seçin.

    ![Hub oluşturma.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.tr.png)

1. Şu görevleri gerçekleştirin:

    - **Hub adı** girin. Benzersiz bir değer olmalıdır.
    - Azure **Aboneliğinizi** seçin.
    - Kullanmak için **Kaynak grubu** seçin (gerekirse yeni bir tane oluşturun).
    - Kullanmak istediğiniz **Konumu** seçin.
    - Kullanmak için **Azure AI Hizmetlerini Bağla** seçeneğini seçin (gerekirse yeni bir tane oluşturun).
    - **Azure AI Arama Bağlantısını Atla** seçeneğini seçin.
![Hub'u doldurun.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.tr.png)

1. **Next** seçeneğini seçin.

#### Azure AI Foundry Projesi Oluşturun

1. Oluşturduğunuz Hub'da, sol sekmeden **All projects** seçeneğini seçin.

1. Navigasyon menüsünden **+ New project** seçeneğini seçin.

    ![Yeni proje seçin.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.tr.png)

1. **Proje adı** girin. Bu değer benzersiz olmalıdır.

    ![Proje oluşturun.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.tr.png)

1. **Create a project** seçeneğini seçin.

#### Phi-3 / Phi-3.5 modeline özel bir bağlantı ekleyin

Özelleştirilmiş Phi-3 / Phi-3.5 modelinizi Prompt flow ile entegre etmek için modelin uç noktası ve anahtarını özel bir bağlantıda kaydetmeniz gerekir. Bu kurulum, özelleştirilmiş Phi-3 / Phi-3.5 modelinize Prompt flow içinde erişimi garanti eder.

#### Özelleştirilmiş Phi-3 / Phi-3.5 modeli için api anahtarı ve uç nokta uri'si ayarlayın

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure Machine Learning çalışma alanına gidin.

1. Sol sekmeden **Endpoints** seçeneğini seçin.

    ![Endpoints seçin.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.tr.png)

1. Oluşturduğunuz uç noktayı seçin.

    ![Oluşturulan uç noktayı seçin.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.tr.png)

1. Navigasyon menüsünden **Consume** seçeneğini seçin.

1. **REST endpoint** ve **Primary key** bilgilerinizi kopyalayın.

    ![Api anahtarını ve uç nokta uri'sini kopyalayın.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.tr.png)

#### Özel Bağlantı Ekleyin

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Oluşturduğunuz Projede, sol sekmeden **Settings** seçeneğini seçin.

1. **+ New connection** seçeneğini seçin.

    ![Yeni bağlantı seçin.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.tr.png)

1. Navigasyon menüsünden **Custom keys** seçeneğini seçin.

    ![Özel anahtarlar seçin.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.tr.png)

1. Şu görevleri gerçekleştirin:

    - **+ Add key value pairs** seçeneğini seçin.
    - Anahtar adı için **endpoint** girin ve Azure ML Studio'dan kopyaladığınız uç noktayı değer alanına yapıştırın.
    - **+ Add key value pairs** seçeneğini tekrar seçin.
    - Anahtar adı için **key** girin ve Azure ML Studio'dan kopyaladığınız anahtarı değer alanına yapıştırın.
    - Anahtarları ekledikten sonra, anahtarın görünmesini engellemek için **is secret** seçeneğini işaretleyin.

    ![Bağlantı ekleyin.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.tr.png)

1. **Add connection** seçeneğini seçin.

#### Prompt flow oluşturun

Azure AI Foundry'e özel bir bağlantı eklediniz. Şimdi, aşağıdaki adımları kullanarak bir Prompt flow oluşturacağız. Daha sonra bu Prompt flow'u özel bağlantıya bağlayarak özelleştirilmiş modeli Prompt flow içinde kullanabileceksiniz.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

1. Sol sekmeden **Prompt flow** seçeneğini seçin.

1. Navigasyon menüsünden **+ Create** seçeneğini seçin.

    ![Promptflow seçin.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.tr.png)

1. Navigasyon menüsünden **Chat flow** seçeneğini seçin.

    ![Chat flow seçin.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.tr.png)

1. Kullanmak için bir **Klasör adı** girin.

    ![Chat flow seçin.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.tr.png)

1. **Create** seçeneğini seçin.

#### Özelleştirilmiş Phi-3 / Phi-3.5 modeliyle sohbet etmek için Prompt flow'u ayarlayın

Özelleştirilmiş Phi-3 / Phi-3.5 modelini bir Prompt flow'a entegre etmeniz gerekir. Ancak, mevcut Prompt flow bu amaç için tasarlanmamıştır. Bu nedenle, özel modeli entegre etmek için Prompt flow'u yeniden tasarlamanız gerekecek.

1. Prompt flow içinde, mevcut akışı yeniden oluşturmak için şu görevleri gerçekleştirin:

    - **Raw file mode** seçeneğini seçin.
    - *flow.dag.yml* dosyasındaki tüm mevcut kodları silin.
    - *flow.dag.yml* dosyasına aşağıdaki kodu ekleyin.

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

    - **Save** seçeneğini seçin.

    ![Raw file mode seçin.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.tr.png)

1. Özelleştirilmiş Phi-3 / Phi-3.5 modelini Prompt flow içinde kullanmak için *integrate_with_promptflow.py* dosyasına aşağıdaki kodu ekleyin.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow kodunu yapıştırın.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.tr.png)

> [!NOTE]
> Azure AI Foundry'de Prompt flow kullanımı hakkında daha fazla bilgi için [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) sayfasına başvurabilirsiniz.

1. **Chat input**, **Chat output** seçeneklerini seçerek modelinizle sohbeti etkinleştirin.

    ![Giriş ve Çıkış seçin.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.tr.png)

1. Artık özelleştirilmiş Phi-3 / Phi-3.5 modelinizle sohbet etmeye hazırsınız. Bir sonraki alıştırmada, Prompt flow'u başlatmayı ve özelleştirilmiş modelinizle sohbet etmeyi öğreneceksiniz.

> [!NOTE]
>
> Yeniden oluşturulan akış aşağıdaki gibi görünmelidir:
>
> ![Akış örneği](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.tr.png)
>

#### Prompt flow'u başlatın

1. Prompt flow'u başlatmak için **Start compute sessions** seçeneğini seçin.

    ![Hesaplama oturumunu başlatın.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.tr.png)

1. Parametreleri yenilemek için **Validate and parse input** seçeneğini seçin.

    ![Girdiyi doğrulayın.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.tr.png)

1. Oluşturduğunuz özel bağlantının **connection** değerini seçin. Örneğin, *connection*.

    ![Bağlantı seçin.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.tr.png)

#### Özelleştirilmiş Phi-3 / Phi-3.5 modelinizle sohbet edin

1. **Chat** seçeneğini seçin.

    ![Chat seçin.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.tr.png)

1. İşte sonuçlardan bir örnek: Artık özelleştirilmiş Phi-3 / Phi-3.5 modelinizle sohbet edebilirsiniz. İnce ayar sırasında kullanılan verilere dayalı sorular sormanız önerilir.

    ![Prompt flow ile sohbet edin.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.tr.png)

### Phi-3 / Phi-3.5 modelini değerlendirmek için Azure OpenAI'yi dağıtın

Azure AI Foundry'de Phi-3 / Phi-3.5 modelini değerlendirmek için bir Azure OpenAI modeli dağıtmanız gerekir. Bu model, Phi-3 / Phi-3.5 modelinin performansını değerlendirmek için kullanılacaktır.

#### Azure OpenAI'yi dağıtın

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresine giriş yapın.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

    ![Proje seçin.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tr.png)

1. Oluşturduğunuz Projede, sol sekmeden **Deployments** seçeneğini seçin.

1. Navigasyon menüsünden **+ Deploy model** seçeneğini seçin.

1. **Deploy base model** seçeneğini seçin.

    ![Dağıtımları seçin.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.tr.png)

1. Kullanmak istediğiniz Azure OpenAI modelini seçin. Örneğin, **gpt-4o**.

    ![Kullanmak istediğiniz Azure OpenAI modelini seçin.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.tr.png)

1. **Confirm** seçeneğini seçin.

### Azure AI Foundry'nin Prompt flow değerlendirmesini kullanarak özelleştirilmiş Phi-3 / Phi-3.5 modelini değerlendirin

### Yeni bir değerlendirme başlatın

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) adresini ziyaret edin.

1. Oluşturduğunuz Azure AI Foundry projesine gidin.

    ![Proje seçin.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tr.png)

1. Oluşturduğunuz Projede, sol sekmeden **Evaluation** seçeneğini seçin.

1. Navigasyon menüsünden **+ New evaluation** seçeneğini seçin.
![Değerlendirmeyi seçin.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.tr.png)

1. **Prompt flow** değerlendirmesini seçin.

    ![Prompt flow değerlendirmesini seçin.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.tr.png)

1. Aşağıdaki görevleri gerçekleştirin:

    - Değerlendirme adını girin. Bu, benzersiz bir değer olmalıdır.
    - Görev türü olarak **Bağlam olmadan soru ve cevap** seçin. Çünkü bu eğitimde kullanılan **ULTRACHAT_200k** veri seti bağlam içermemektedir.
    - Değerlendirmek istediğiniz prompt flow'u seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.tr.png)

1. **İleri**'yi seçin.

1. Aşağıdaki görevleri gerçekleştirin:

    - Veri setini yüklemek için **Veri setinizi ekleyin** seçeneğini seçin. Örneğin, **ULTRACHAT_200k** veri setini indirdiğinizde dahil edilen *test_data.json1* gibi test veri seti dosyasını yükleyebilirsiniz.
    - Veri setinizle eşleşen uygun **Veri seti sütununu** seçin. Örneğin, **ULTRACHAT_200k** veri setini kullanıyorsanız, veri seti sütunu olarak **${data.prompt}** seçeneğini seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.tr.png)

1. **İleri**'yi seçin.

1. Performans ve kalite metriklerini yapılandırmak için aşağıdaki görevleri gerçekleştirin:

    - Kullanmak istediğiniz performans ve kalite metriklerini seçin.
    - Değerlendirme için oluşturduğunuz Azure OpenAI modelini seçin. Örneğin, **gpt-4o** seçeneğini seçin.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.tr.png)

1. Risk ve güvenlik metriklerini yapılandırmak için aşağıdaki görevleri gerçekleştirin:

    - Kullanmak istediğiniz risk ve güvenlik metriklerini seçin.
    - Kullanmak istediğiniz hata oranını hesaplamak için eşiği seçin. Örneğin, **Orta** seçeneğini seçin.
    - **Soru** için, **Veri kaynağını** **{$data.prompt}** olarak ayarlayın.
    - **Cevap** için, **Veri kaynağını** **{$run.outputs.answer}** olarak ayarlayın.
    - **Doğru yanıt (ground_truth)** için, **Veri kaynağını** **{$data.message}** olarak ayarlayın.

    ![Prompt flow değerlendirmesi.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.tr.png)

1. **İleri**'yi seçin.

1. Değerlendirmeyi başlatmak için **Gönder**'i seçin.

1. Değerlendirme tamamlanana kadar biraz zaman alacaktır. İlerlemeyi **Değerlendirme** sekmesinde izleyebilirsiniz.

### Değerlendirme Sonuçlarını İnceleyin

> [!NOTE]
> Aşağıda sunulan sonuçlar, değerlendirme sürecini göstermek amacıyla verilmiştir. Bu eğitimde, nispeten küçük bir veri setiyle ince ayar yapılmış bir model kullanılmıştır, bu da optimal olmayan sonuçlara yol açabilir. Gerçek sonuçlar, kullanılan veri setinin boyutuna, kalitesine ve çeşitliliğine, ayrıca modelin özel yapılandırmasına bağlı olarak önemli ölçüde değişebilir.

Değerlendirme tamamlandıktan sonra hem performans hem de güvenlik metrikleri için sonuçları inceleyebilirsiniz.

1. Performans ve kalite metrikleri:

    - Modelin tutarlı, akıcı ve ilgili yanıtlar üretme konusundaki etkinliğini değerlendirin.

    ![Değerlendirme sonucu.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.tr.png)

1. Risk ve güvenlik metrikleri:

    - Modelin çıktılarının güvenli olduğundan ve Zararsız AI İlkeleri ile uyumlu olduğundan emin olun, zararlı veya saldırgan içerikten kaçının.

    ![Değerlendirme sonucu.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.tr.png)

1. **Detaylı metrik sonuçlarını** görmek için aşağı kaydırabilirsiniz.

    ![Değerlendirme sonucu.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.tr.png)

1. Özel Phi-3 / Phi-3.5 modelinizi hem performans hem de güvenlik metriklerine göre değerlendirerek, modelin yalnızca etkili olmadığını, aynı zamanda sorumlu AI uygulamalarına uygun olduğunu doğrulayabilirsiniz. Bu, modeli gerçek dünya uygulamaları için hazır hale getirir.

## Tebrikler!

### Bu eğitimi tamamladınız

Azure AI Foundry'de Prompt flow ile entegre edilmiş ince ayarlı Phi-3 modelini başarıyla değerlendirdiniz. Bu, AI modellerinizin yalnızca iyi performans göstermesini değil, aynı zamanda Microsoft'un Sorumlu AI ilkelerine uygun olmasını sağlamak için önemli bir adımdır. Bu, güvenilir ve güvenilir AI uygulamaları oluşturmanıza yardımcı olur.

![Mimari.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tr.png)

## Azure Kaynaklarını Temizleme

Hesabınıza ek maliyetler gelmesini önlemek için Azure kaynaklarınızı temizleyin. Azure portalına gidin ve aşağıdaki kaynakları silin:

- Azure Machine Learning kaynağı.
- Azure Machine Learning model uç noktası.
- Azure AI Foundry Proje kaynağı.
- Azure AI Foundry Prompt flow kaynağı.

### Sonraki Adımlar

#### Dokümantasyon

- [Responsible AI panosu kullanarak AI sistemlerini değerlendirme](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Üretken AI için değerlendirme ve izleme metrikleri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry dokümantasyonu](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokümantasyonu](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Eğitim İçeriği

- [Microsoft'un Sorumlu AI Yaklaşımına Giriş](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry'ye Giriş](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referans

- [Sorumlu AI Nedir?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Daha güvenli ve güvenilir üretken AI uygulamaları oluşturmanıza yardımcı olacak Azure AI'deki yeni araçların duyurusu](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Üretken AI uygulamalarının değerlendirilmesi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanabilecek yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.