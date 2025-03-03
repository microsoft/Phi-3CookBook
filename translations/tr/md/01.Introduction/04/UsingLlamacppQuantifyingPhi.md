# **Phi Ailesini llama.cpp ile Kuantize Etme**

## **llama.cpp Nedir?**

llama.cpp, C++ dilinde yazılmış açık kaynaklı bir yazılım kütüphanesidir ve Llama gibi çeşitli Büyük Dil Modelleri'nde (LLM) çıkarım yapar. Ana amacı, geniş bir donanım yelpazesinde minimum kurulumla LLM çıkarımı için en son performansı sağlamaktır. Ayrıca, bu kütüphane için metin tamamlama ve OpenAI uyumlu bir web sunucusu için yüksek seviyeli bir API sunan Python bağlayıcıları da mevcuttur.

llama.cpp'nin ana hedefi, yerel ve bulut ortamlarında geniş bir donanım yelpazesinde minimum kurulum ve en son performans ile LLM çıkarımı sağlamaktır.

- Herhangi bir bağımlılık olmadan düz C/C++ uygulaması
- Apple Silicon birinci sınıf bir vatandaş - ARM NEON, Accelerate ve Metal framework'leri ile optimize edilmiştir
- x86 mimarileri için AVX, AVX2 ve AVX512 desteği
- Daha hızlı çıkarım ve azaltılmış bellek kullanımı için 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit ve 8-bit tamsayı kuantizasyonu
- NVIDIA GPU'larda LLM'leri çalıştırmak için özel CUDA çekirdekleri (AMD GPU'lar için HIP desteği)
- Vulkan ve SYCL arka uç desteği
- Toplam VRAM kapasitesinden daha büyük modelleri kısmen hızlandırmak için CPU+GPU hibrit çıkarımı

## **Phi-3.5'i llama.cpp ile Kuantize Etme**

Phi-3.5-Instruct modeli llama.cpp kullanılarak kuantize edilebilir, ancak Phi-3.5-Vision ve Phi-3.5-MoE henüz desteklenmemektedir. llama.cpp tarafından dönüştürülen format gguf olup, bu format aynı zamanda en yaygın kullanılan kuantizasyon formatıdır.

Hugging Face üzerinde çok sayıda kuantize edilmiş GGUF formatında model bulunmaktadır. AI Foundry, Ollama ve LlamaEdge llama.cpp'ye dayanır, bu nedenle GGUF modelleri de sıkça kullanılmaktadır.

### **GGUF Nedir?**

GGUF, modellerin hızlı yüklenmesi ve kaydedilmesi için optimize edilmiş bir ikili formattır ve çıkarım amaçları için son derece verimlidir. GGUF, GGML ve diğer yürütücülerle kullanım için tasarlanmıştır. GGUF, popüler bir C/C++ LLM çıkarım framework'ü olan llama.cpp'nin geliştiricisi @ggerganov tarafından geliştirilmiştir. PyTorch gibi framework'lerde başlangıçta geliştirilen modeller, bu motorlarla kullanılmak üzere GGUF formatına dönüştürülebilir.

### **ONNX vs GGUF**

ONNX, farklı AI Framework'lerinde iyi desteklenen geleneksel bir makine öğrenimi/derin öğrenme formatıdır ve uç cihazlarda iyi kullanım senaryolarına sahiptir. GGUF ise llama.cpp'ye dayalıdır ve GenAI çağında üretilmiş denilebilir. İkisi de benzer kullanım alanlarına sahiptir. Gömülü donanım ve uygulama katmanlarında daha iyi performans istiyorsanız, ONNX sizin tercihiniz olabilir. Eğer llama.cpp'nin türev framework'ü ve teknolojisini kullanıyorsanız, GGUF daha iyi bir seçenek olabilir.

### **Phi-3.5-Instruct'ı llama.cpp ile Kuantize Etme**

**1. Ortam Yapılandırması**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. Kuantizasyon**

Phi-3.5-Instruct'ı FP16 GGUF formatına dönüştürmek için llama.cpp kullanma

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5'i INT4'e kuantize etme

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. Test**

llama-cpp-python yükleyin

```bash

pip install llama-cpp-python -U

```

***Not***

Apple Silicon kullanıyorsanız, lütfen llama-cpp-python'u şu şekilde yükleyin:

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test Etme

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **Kaynaklar**

1. llama.cpp hakkında daha fazla bilgi edinin [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GGUF hakkında daha fazla bilgi edinin [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, esas kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.