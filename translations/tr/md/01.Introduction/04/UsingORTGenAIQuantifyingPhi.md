# **Phi Ailesini onnxruntime için Generative AI Uzantıları ile Kuantize Etme**

## **Generative AI Uzantıları nedir?**

Bu uzantılar, ONNX Runtime ile generatif yapay zeka çalıştırmanıza yardımcı olur ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). ONNX modelleri için generatif yapay zeka döngüsü sağlar; bu, ONNX Runtime ile çıkarım, logits işleme, arama ve örnekleme ile KV önbellek yönetimini içerir. Geliştiriciler, yüksek seviyeli bir generate() metodunu çağırabilir veya modelin her iterasyonunu bir döngü içinde çalıştırarak her seferinde bir token üretebilir ve isteğe bağlı olarak döngü içinde üretim parametrelerini güncelleyebilir. Greedy/beam search ve TopP, TopK örnekleme ile token dizileri oluşturma ve tekrar cezası gibi yerleşik logits işleme desteklenir. Ayrıca özel puanlama eklemek kolaydır.

Uygulama seviyesinde, Generative AI uzantılarını C++/C#/Python kullanarak uygulamalar oluşturmak için kullanabilirsiniz. Model seviyesinde ise, ince ayar yapılmış modelleri birleştirmek ve ilgili kuantitatif dağıtım çalışmalarını gerçekleştirmek için kullanabilirsiniz.

## **Generative AI Uzantıları ile Phi-3.5'i Kuantize Etme**

### **Desteklenen Modeller**

Generative AI uzantıları, Microsoft Phi, Google Gemma, Mistral, Meta LLaMA'nın kuantizasyon dönüşümünü destekler.

### **Generative AI Uzantılarında Model Oluşturucu**

Model oluşturucu, ONNX Runtime generate() API'si ile çalışan optimize edilmiş ve kuantize edilmiş ONNX modelleri oluşturmayı büyük ölçüde hızlandırır.

Model oluşturucu aracılığıyla modeli INT4, INT8, FP16, FP32'ye kuantize edebilir ve CPU, CUDA, DirectML, Mobile gibi farklı donanım hızlandırma yöntemlerini birleştirebilirsiniz.

Model Oluşturucuyu kullanmak için şunları yüklemeniz gerekir:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Yükleme tamamlandıktan sonra, terminalden Model Oluşturucu betiğini çalıştırarak model formatı ve kuantizasyon dönüşümü gerçekleştirebilirsiniz.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

İlgili parametreleri anlayın:

1. **model_name** Bu, Hugging Face üzerindeki modeldir, örneğin microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct gibi. Ayrıca modeli depoladığınız yol da olabilir.

2. **path_to_output_folder** Kuantize edilmiş dönüşümün kaydedileceği yol.

3. **execution_provider** Farklı donanım hızlandırma desteği, örneğin cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Modeli Hugging Face'den indirir ve yerel olarak önbelleğe alır.

***Not:***  

## **Phi-3.5'i Kuantize Etmek için Model Oluşturucu Nasıl Kullanılır**

Model Oluşturucu artık Phi-3.5 Instruct ve Phi-3.5-Vision için ONNX model kuantizasyonunu desteklemektedir.

### **Phi-3.5-Instruct**

**Kuantize edilmiş INT4 için CPU hızlandırmalı dönüşüm**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Kuantize edilmiş INT4 için CUDA hızlandırmalı dönüşüm**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Terminalde ortamı ayarlayın:

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct modelini "models" klasörüne indirin:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Lütfen aşağıdaki dosyaları Phi-3.5-vision-instruct klasörünüze indirin:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Aşağıdaki dosyayı "models" klasörüne indirin:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Terminale gidin:  

    ONNX desteğini FP32 ile dönüştürün:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Notlar:**

1. Model Oluşturucu şu anda Phi-3.5-Instruct ve Phi-3.5-Vision'ın dönüşümünü desteklemektedir, ancak Phi-3.5-MoE'yi desteklememektedir.

2. ONNX'in kuantize edilmiş modelini kullanmak için Generative AI uzantıları SDK'sı aracılığıyla kullanabilirsiniz.

3. Daha sorumlu bir yapay zeka yaklaşımı düşünmemiz gerekiyor, bu yüzden model kuantizasyon dönüşümünden sonra daha etkili sonuç testleri yapılması önerilir.

4. CPU INT4 modelini kuantize ederek, onu Edge Device'a dağıtabiliriz; bu, daha iyi uygulama senaryoları sağlar. Bu nedenle Phi-3.5-Instruct'ı INT4 etrafında tamamladık.

## **Kaynaklar**

1. Generative AI uzantıları hakkında daha fazla bilgi edinin: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI uzantılarının GitHub deposu: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi ana dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.