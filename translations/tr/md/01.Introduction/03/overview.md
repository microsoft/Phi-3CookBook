Phi-3-mini bağlamında çıkarım, modelin giriş verilerine dayanarak tahminlerde bulunma veya çıktılar üretme sürecini ifade eder. Phi-3-mini ve çıkarım yetenekleri hakkında daha fazla bilgi verelim.

Phi-3-mini, Microsoft tarafından piyasaya sürülen Phi-3 model serisinin bir parçasıdır. Bu modeller, Küçük Dil Modelleri (SLM'ler) ile nelerin mümkün olduğunu yeniden tanımlamak için tasarlanmıştır.

İşte Phi-3-mini ve çıkarım yetenekleri hakkında bazı önemli noktalar:

## **Phi-3-mini Genel Bakış:**
- Phi-3-mini, 3.8 milyar parametre boyutuna sahiptir.
- Sadece geleneksel bilgi işlem cihazlarında değil, aynı zamanda mobil cihazlar ve IoT cihazları gibi uç cihazlarda da çalışabilir.
- Phi-3-mini’nin piyasaya sürülmesi, bireylerin ve işletmelerin SLM'leri farklı donanım cihazlarında, özellikle de kısıtlı kaynaklara sahip ortamlarda dağıtmasını mümkün kılar.
- Geleneksel PyTorch formatı, gguf formatının kuantize edilmiş versiyonu ve ONNX tabanlı kuantize edilmiş versiyon gibi çeşitli model formatlarını kapsar.

## **Phi-3-mini'ye Erişim:**
Phi-3-mini’ye erişmek için bir Copilot uygulamasında [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) kullanabilirsiniz. Semantic Kernel, genel olarak Azure OpenAI Hizmeti, Hugging Face üzerindeki açık kaynak modeller ve yerel modellerle uyumludur.  
Ayrıca kuantize edilmiş modellere çağrı yapmak için [Ollama](https://ollama.com) veya [LlamaEdge](https://llamaedge.com) kullanabilirsiniz. Ollama, bireysel kullanıcıların farklı kuantize edilmiş modellere çağrı yapmasına olanak tanırken, LlamaEdge GGUF modeller için çapraz platform kullanılabilirliği sunar.

## **Kuantize Edilmiş Modeller:**
Birçok kullanıcı yerel çıkarım için kuantize edilmiş modelleri tercih eder. Örneğin, doğrudan Ollama ile Phi-3 çalıştırabilir veya bunu bir Modelfile kullanarak çevrimdışı olarak yapılandırabilirsiniz. Modelfile, GGUF dosya yolunu ve istem formatını belirtir.

## **Üretken Yapay Zeka Olanakları:**
Phi-3-mini gibi SLM'lerin bir araya getirilmesi, üretken yapay zeka için yeni olanaklar sunar. Çıkarım sadece ilk adımdır; bu modeller, kısıtlı kaynaklara sahip, gecikme süresi sınırlı ve maliyet odaklı senaryolarda çeşitli görevler için kullanılabilir.

## **Phi-3-mini ile Üretken Yapay Zekanın Kilidini Açma: Çıkarım ve Dağıtım Rehberi**  
Phi-3-mini modellerine erişmek ve çıkarım yapmak için Semantic Kernel, Ollama/LlamaEdge ve ONNX Runtime kullanmayı öğrenin ve çeşitli uygulama senaryolarında üretken yapay zekanın olanaklarını keşfedin.

**Özellikler**  
Phi-3-mini modelini şu araçlarla çıkarın:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Özetle, Phi-3-mini, geliştiricilerin farklı model formatlarını keşfetmesine ve çeşitli uygulama senaryolarında üretken yapay zekadan yararlanmasına olanak tanır.

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.