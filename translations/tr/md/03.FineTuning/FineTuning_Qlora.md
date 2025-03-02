**Phi-3'ü QLoRA ile İnce Ayarlama**

Microsoft’un Phi-3 Mini dil modelini [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) kullanarak ince ayarlama.

QLoRA, konuşmaları daha iyi anlama ve yanıt üretimini geliştirmeye yardımcı olacaktır.

Transformers ve bitsandbytes ile modelleri 4 bit olarak yüklemek için, accelerate ve transformers'ı kaynaktan yüklemeniz ve bitsandbytes kütüphanesinin en son sürümüne sahip olduğunuzdan emin olmanız gerekir.

**Örnekler**
- [Bu örnek not defteriyle daha fazlasını öğrenin](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python İnce Ayar Örneği](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA ile Hugging Face Hub Üzerinde İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA ile Hugging Face Hub Üzerinde İnce Ayar Örneği](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, bağlayıcı kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yorumlamalar konusunda sorumluluk kabul etmiyoruz.