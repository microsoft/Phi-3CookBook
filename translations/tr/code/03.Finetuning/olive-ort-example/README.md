# Olive ile Phi3'ü İnce Ayar Yapma

Bu örnekte Olive'i kullanarak:

1. Bir LoRA adaptörünü, ifadeleri Üzgün, Neşe, Korku, Sürpriz olarak sınıflandırmak üzere ince ayar yapacaksınız.
2. Adaptör ağırlıklarını temel modele birleştireceksiniz.
3. Modeli `int4` formatında optimize edip kuantize edeceksiniz.

Ayrıca ince ayar yapılmış modeli ONNX Runtime (ORT) Generate API kullanarak nasıl çıkarım yapabileceğinizi de göstereceğiz.

> **⚠️ İnce Ayar için, uygun bir GPU'nuzun olması gereklidir - örneğin, A10, V100, A100.**

## 💾 Kurulum

Yeni bir Python sanal ortamı oluşturun (örneğin, `conda` kullanarak):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Daha sonra, Olive ve ince ayar iş akışı için gereken bağımlılıkları yükleyin:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ile Phi3'ü İnce Ayar Yapma
[Olive yapılandırma dosyası](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) aşağıdaki *geçişlerden* oluşan bir *iş akışı* içerir:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Bu iş akışı genel olarak şunları yapar:

1. Phi3'e, [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) verilerini kullanarak (150 adım boyunca, bunu değiştirebilirsiniz) ince ayar yapar.
2. LoRA adaptör ağırlıklarını temel modele birleştirir. Bu işlem, ONNX formatında tek bir model çıktısı elde etmenizi sağlar.
3. Model Builder, modeli ONNX runtime için optimize eder *ve* modeli `int4` formatında kuantize eder.

İş akışını çalıştırmak için şu komutu çalıştırın:

```bash
olive run --config phrase-classification.json
```

Olive tamamlandığında, optimize edilmiş `int4` ince ayar yapılmış Phi3 modeliniz şu konumda bulunabilir: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 İnce Ayar Yapılmış Phi3'ü Uygulamanıza Entegre Etme

Uygulamayı çalıştırmak için:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Bu yanıt, ifadenin tek kelimelik bir sınıflandırması olmalıdır (Üzgün/Neşe/Korku/Sürpriz).

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.