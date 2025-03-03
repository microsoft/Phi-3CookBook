# **Phi-3'ü Lora ile İnce Ayar Yapma**

Microsoft'un Phi-3 Mini dil modelini özel bir sohbet talimatı veri seti üzerinde [LoRA (Düşük Dereceli Uyarlama)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) kullanarak ince ayar yapma.

LORA, sohbet anlama ve yanıt oluşturma yeteneklerini geliştirmeye yardımcı olacaktır.

## Phi-3 Mini'yi ince ayar yapma adım adım rehberi:

**Kütüphanelerin İçe Aktarılması ve Kurulum** 

loralib yükleniyor

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Gerekli kütüphaneleri (ör. datasets, transformers, peft, trl ve torch) içe aktararak başlayın. Eğitim sürecini izlemek için günlük kaydını ayarlayın.

Bazı katmanları, loralib'de uygulanmış muadilleriyle değiştirerek uyarlamayı seçebilirsiniz. Şu anda yalnızca nn.Linear, nn.Embedding ve nn.Conv2d desteklenmektedir. Ayrıca, tek bir nn.Linear'ın birden fazla katmanı temsil ettiği durumlar için bir MergedLinear da desteklenmektedir; örneğin, dikkat qkv projeksiyonunun bazı uygulamalarında (daha fazla bilgi için Ek Notlar'a bakın).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Eğitim döngüsü başlamadan önce, yalnızca LoRA parametrelerini eğitilebilir olarak işaretleyin.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Bir kontrol noktası kaydedilirken, yalnızca LoRA parametrelerini içeren bir state_dict oluşturun.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict kullanarak bir kontrol noktası yüklerken, strict=False olarak ayarladığınızdan emin olun.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Artık eğitim normal şekilde devam edebilir.

**Hiperparametreler** 

training_config ve peft_config olmak üzere iki sözlük tanımlayın. training_config, öğrenme hızı, batch boyutu ve günlük kaydı ayarları gibi eğitim için hiperparametreleri içerir.

peft_config, rank, dropout ve görev türü gibi LoRA ile ilgili parametreleri belirtir.

**Model ve Tokenizer Yükleme** 

Önceden eğitilmiş Phi-3 modelinin yolunu belirtin (ör. "microsoft/Phi-3-mini-4k-instruct"). Model ayarlarını yapılandırın; önbellek kullanımı, veri türü (karma hassasiyet için bfloat16) ve dikkat uygulaması gibi.

**Eğitim** 

Phi-3 modelini özel sohbet talimatı veri seti üzerinde ince ayar yapın. Verimli uyarlama için peft_config'teki LoRA ayarlarını kullanın. Belirtilen günlük kaydı stratejisini kullanarak eğitim ilerlemesini izleyin.
Değerlendirme ve Kaydetme: İnce ayar yapılmış modeli değerlendirin.
Daha sonra kullanmak üzere eğitim sırasında kontrol noktalarını kaydedin.

**Örnekler**
- [Bu örnek notebook ile daha fazlasını öğrenin](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ile İnce Ayar Örneği](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub ile LORA İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Kartı - LORA İnce Ayar Örneği](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA ile Hugging Face Hub İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.