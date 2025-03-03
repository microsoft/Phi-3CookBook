# Lab. AI Modellerini Cihaz Üzerinde Çalıştırma için Optimize Etme

## Giriş

> [!IMPORTANT]
> Bu laboratuvar, **Nvidia A10 veya A100 GPU** ile ilgili sürücüler ve CUDA araç seti (sürüm 12+) yüklü olarak gerektirir.

> [!NOTE]
> Bu laboratuvar, OLIVE kullanarak cihaz üzerinde çalıştırma için modelleri optimize etmenin temel kavramlarına pratik bir giriş sunan **35 dakikalık** bir çalışmadır.

## Öğrenme Hedefleri

Bu laboratuvarın sonunda OLIVE kullanarak şunları yapabileceksiniz:

- AWQ kuantizasyon yöntemini kullanarak bir AI modelini kuantize etmek.
- Belirli bir görev için bir AI modelini ince ayar yapmak.
- ONNX Runtime üzerinde verimli cihaz içi çalıştırma için LoRA adaptörleri (ince ayarlı model) oluşturmak.

### Olive Nedir?

Olive (*O*NNX *live*), ONNX runtime +++https://onnxruntime.ai+++ için modelleri dağıtmak amacıyla kullanılan bir model optimizasyon araç seti ve komut satırı arayüzüdür.

![Olive Akışı](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.tr.png)

Olive'e genellikle bir PyTorch veya Hugging Face modeli giriş olarak verilir ve çıkış, ONNX runtime çalıştıran bir cihazda (dağıtım hedefi) yürütülen optimize edilmiş bir ONNX modelidir. Olive, modeli donanım üreticisi (Qualcomm, AMD, Nvidia veya Intel gibi) tarafından sağlanan dağıtım hedefinin AI hızlandırıcısına (NPU, GPU, CPU) göre optimize eder.

Olive, *geçiş* adı verilen bireysel model optimizasyon görevlerinin sıralı bir dizisi olan bir *iş akışı* yürütür - örneğin model sıkıştırma, grafik yakalama, kuantizasyon, grafik optimizasyonu gibi geçişler. Her geçişin, doğruluk ve gecikme gibi en iyi metrikleri elde etmek için ayarlanabilecek bir dizi parametresi vardır ve bu metrikler ilgili değerlendirici tarafından değerlendirilir. Olive, her bir geçişi veya bir dizi geçişi otomatik olarak ayarlamak için bir arama algoritması kullanan bir arama stratejisi uygular.

#### Olive'in Avantajları

- Grafik optimizasyonu, sıkıştırma ve kuantizasyon için farklı tekniklerle deneme-yanılma sürecindeki **hayal kırıklığını ve zamanı azaltır**. Kalite ve performans kısıtlamalarınızı tanımlayın ve Olive sizin için en iyi modeli otomatik olarak bulsun.
- **40'tan fazla yerleşik model optimizasyon bileşeni**, kuantizasyon, sıkıştırma, grafik optimizasyonu ve ince ayar alanlarında en son teknikleri kapsar.
- Yaygın model optimizasyon görevleri için **kullanımı kolay bir CLI**. Örneğin, olive quantize, olive auto-opt, olive finetune.
- Model paketleme ve dağıtım yerleşik olarak mevcuttur.
- **Çoklu LoRA sunumu** için model üretimini destekler.
- Model optimizasyonu ve dağıtım görevlerini düzenlemek için YAML/JSON kullanarak iş akışları oluşturun.
- **Hugging Face** ve **Azure AI** Entegrasyonu.
- Maliyetleri **azaltmak** için yerleşik bir **önbellekleme** mekanizması.

## Laboratuvar Talimatları
> [!NOTE]
> Azure AI Hub ve Projenizi ayarladığınızdan ve A100 hesabınızı Lab 1'e göre yapılandırdığınızdan emin olun.

### Adım 0: Azure AI Compute'ye Bağlanın

**VS Code**'un uzaktan bağlantı özelliğini kullanarak Azure AI compute'ye bağlanacaksınız.

1. **VS Code** masaüstü uygulamanızı açın:
1. **Komut paletini** **Shift+Ctrl+P** ile açın.
1. Komut paletinde **AzureML - remote: Connect to compute instance in New Window** arayın.
1. Compute'a bağlanmak için ekrandaki talimatları izleyin. Bu, Lab 1'de ayarladığınız Azure Aboneliği, Kaynak Grubu, Proje ve Compute adını seçmeyi içerecektir.
1. Azure ML Compute düğümüne bağlandığınızda, bu **Visual Code'un sol alt köşesinde** gösterilecektir `><Azure ML: Compute Name`

### Adım 1: Bu Depoyu Klonlayın

VS Code'da, **Ctrl+J** ile yeni bir terminal açabilir ve bu depoyu klonlayabilirsiniz:

Terminalde aşağıdaki istemi göreceksiniz:

```
azureuser@computername:~/cloudfiles/code$ 
```
Çözümü klonlayın

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Adım 2: Klasörü VS Code'da Açın

İlgili klasörü VS Code'da açmak için terminalde aşağıdaki komutu çalıştırın; bu yeni bir pencere açacaktır:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternatif olarak, **Dosya** > **Klasör Aç** seçeneğini kullanarak klasörü açabilirsiniz.

### Adım 3: Bağımlılıklar

Azure AI Compute Instance'daki VS Code'da bir terminal penceresi açın (ipucu: **Ctrl+J**) ve bağımlılıkları yüklemek için şu komutları çalıştırın:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Tüm bağımlılıkların yüklenmesi yaklaşık **5 dakika** sürecektir.

Bu laboratuvarda, Azure AI Model kataloğuna modeller indirip yükleyeceksiniz. Model kataloğuna erişebilmek için şu komutu kullanarak Azure'da oturum açmanız gerekecek:

```bash
az login
```

> [!NOTE]
> Oturum açarken, aboneliğinizi seçmeniz istenecektir. Bu laboratuvar için sağlanan aboneliği seçtiğinizden emin olun.

### Adım 4: Olive Komutlarını Çalıştırın

Azure AI Compute Instance'daki VS Code'da bir terminal penceresi açın (ipucu: **Ctrl+J**) ve `olive-ai` conda ortamının etkinleştirildiğinden emin olun:

```bash
conda activate olive-ai
```

Sonrasında, komut satırında aşağıdaki Olive komutlarını çalıştırın.

1. **Veriyi inceleyin:** Bu örnekte, Phi-3.5-Mini modelini seyahatle ilgili soruları yanıtlamada uzmanlaşacak şekilde ince ayar yapacaksınız. Aşağıdaki kod, JSON satırları formatındaki veri kümesinin ilk birkaç kaydını görüntüler:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Modeli kuantize edin:** Modeli eğitmeden önce, Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ adlı bir teknik kullanan şu komutla kuantize edin. AWQ, ağırlıkları çıkarımlar sırasında üretilen aktivasyonları dikkate alarak kuantize eder. Bu, kuantizasyon işleminin aktivasyonlardaki gerçek veri dağılımını dikkate aldığı anlamına gelir ve bu da geleneksel ağırlık kuantizasyon yöntemlerine kıyasla model doğruluğunun daha iyi korunmasına yol açar.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ kuantizasyonunun tamamlanması **~8 dakika** sürer ve bu işlem, model boyutunu **~7.5GB'den ~2.5GB'ye** düşürür.
   
   Bu laboratuvarda, Hugging Face'ten modelleri nasıl girdi olarak alacağınızı göstereceğiz (örneğin: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` komutu, kuantize edilmiş modeli ince ayar yapar. Modeli ince ayar yapmadan önce kuantize etmek, sonrasında yapmaktan daha iyi doğruluk sağlar çünkü ince ayar işlemi kuantizasyondan kaynaklanan kayıpların bir kısmını geri kazanır.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    İnce ayar işlemi (100 adımla) **~6 dakika** sürer.

1. **Optimize Edin:** Model eğitildikten sonra, Olive'in `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` argümanlarını kullanarak modeli optimize edin - ancak bu laboratuvarın amaçları doğrultusunda CPU kullanacağız.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Optimizasyonun tamamlanması **~5 dakika** sürer.

### Adım 5: Model Çıkarımını Hızlı Test Etme

Modelin çıkarımını test etmek için, klasörünüzde **app.py** adlı bir Python dosyası oluşturun ve aşağıdaki kodu kopyalayıp yapıştırın:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Kodu şu komutla çalıştırın:

```bash
python app.py
```

### Adım 6: Azure AI'ye Model Yükleme

Modeli bir Azure AI model deposuna yüklemek, modeli geliştirme ekibinizin diğer üyeleriyle paylaşılabilir hale getirir ve ayrıca modelin sürüm kontrolünü sağlar. Modeli yüklemek için şu komutu çalıştırın:

> [!NOTE]
> `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` ve Azure AI Proje adını güncelleyerek şu komutu çalıştırın: 

```
az ml workspace show
```

Ya da +++ai.azure.com+++ adresine giderek **yönetim merkezi** > **proje** > **genel bakış** seçeneklerini seçebilirsiniz.

`{}` yer tutucularını, kaynak grubunuzun ve Azure AI Proje Adınızın adıyla güncelleyin.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Modelinizi yükledikten sonra, modelinizi şu adresten görebilir ve dağıtabilirsiniz: https://ml.azure.com/model/list

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.