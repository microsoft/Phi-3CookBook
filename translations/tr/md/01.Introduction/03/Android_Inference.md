# **Android'de Phi-3 Çıkarımı**

Haydi, Phi-3-mini ile Android cihazlarda nasıl çıkarım yapabileceğinizi keşfedelim. Phi-3-mini, Microsoft'un Büyük Dil Modellerini (LLM'ler) uç cihazlar ve IoT cihazlarında kullanıma olanak tanıyan yeni bir model serisidir.

## Semantic Kernel ve Çıkarım

[Semantic Kernel](https://github.com/microsoft/semantic-kernel), Azure OpenAI Service, OpenAI modelleri ve hatta yerel modellerle uyumlu uygulamalar oluşturmanıza olanak tanıyan bir uygulama çerçevesidir. Semantic Kernel ile yeni tanışıyorsanız, [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) rehberine göz atmanızı öneririz.

### Semantic Kernel Kullanarak Phi-3-mini'ye Erişim

Bunu Semantic Kernel'deki Hugging Face Connector ile birleştirebilirsiniz. Bu [Örnek Kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) bağlantısına bakabilirsiniz.

Varsayılan olarak, Hugging Face üzerindeki model kimliğine karşılık gelir. Ancak, yerel olarak oluşturulmuş bir Phi-3-mini model sunucusuna da bağlanabilirsiniz.

### Ollama veya LlamaEdge ile Kuantize Modelleri Çağırma

Birçok kullanıcı, modelleri yerel olarak çalıştırmak için kuantize modelleri kullanmayı tercih eder. [Ollama](https://ollama.com/) ve [LlamaEdge](https://llamaedge.com), bireysel kullanıcıların farklı kuantize modelleri çağırmasına olanak tanır:

#### Ollama

`ollama run Phi-3` komutunu doğrudan çalıştırabilir veya `Modelfile` oluşturup `.gguf` dosyanızın yolunu belirterek çevrimdışı olarak yapılandırabilirsiniz.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Örnek Kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Eğer `.gguf` dosyalarını hem bulutta hem de uç cihazlarda aynı anda kullanmak istiyorsanız, LlamaEdge harika bir seçenektir. Başlamak için bu [örnek koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) göz atabilirsiniz.

### Android Telefonlara Kurulum ve Çalıştırma

1. **MLC Chat uygulamasını** (Ücretsiz) Android telefonlar için indirin.
2. APK dosyasını (148MB) indirin ve cihazınıza yükleyin.
3. MLC Chat uygulamasını başlatın. Phi-3-mini dahil olmak üzere bir dizi yapay zeka modelini göreceksiniz.

Özetle, Phi-3-mini uç cihazlarda üretken yapay zeka için heyecan verici olanaklar sunuyor ve Android'de yeteneklerini keşfetmeye başlayabilirsiniz.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul edilmez.