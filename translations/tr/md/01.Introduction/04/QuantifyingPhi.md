# **Phi Ailesini Sayısallaştırma**

Model sayısallaştırma, bir sinir ağı modelindeki parametrelerin (örneğin ağırlıklar ve aktivasyon değerleri) geniş bir değer aralığından (genellikle sürekli bir değer aralığı) daha küçük, sonlu bir değer aralığına eşlenmesi işlemidir. Bu teknoloji, modelin boyutunu ve hesaplama karmaşıklığını azaltabilir ve mobil cihazlar veya gömülü sistemler gibi kaynak kısıtlı ortamlarda modelin çalışma verimliliğini artırabilir. Model sayısallaştırma, parametrelerin hassasiyetini azaltarak sıkıştırmayı sağlar, ancak bu aynı zamanda belirli bir hassasiyet kaybını da beraberinde getirir. Bu nedenle, sayısallaştırma sürecinde model boyutu, hesaplama karmaşıklığı ve hassasiyet arasında bir denge kurulması gerekir. Yaygın sayısallaştırma yöntemleri arasında sabit nokta sayısallaştırması, kayan nokta sayısallaştırması vb. bulunur. Belirli senaryo ve ihtiyaçlara göre uygun bir sayısallaştırma stratejisi seçebilirsiniz.

GenAI modelini uç cihazlara dağıtmayı ve mobil cihazlar, AI PC / Copilot+PC ve geleneksel IoT cihazları gibi daha fazla cihazın GenAI senaryolarına katılmasını sağlamayı hedefliyoruz. Sayısallaştırılmış model sayesinde, farklı cihazlara dayalı olarak modeli farklı uç cihazlara dağıtabiliriz. Donanım üreticilerinin sağladığı model hızlandırma çerçevesi ve sayısallaştırılmış model ile birleştirerek daha iyi SLM uygulama senaryoları oluşturabiliriz.

Sayısallaştırma senaryosunda, farklı hassasiyetlere sahibiz (INT4, INT8, FP16, FP32). Aşağıda yaygın kullanılan sayısallaştırma hassasiyetlerinin açıklamaları bulunmaktadır:

### **INT4**

INT4 sayısallaştırması, modelin ağırlıklarını ve aktivasyon değerlerini 4 bitlik tamsayılara dönüştüren radikal bir sayısallaştırma yöntemidir. Daha küçük temsil aralığı ve daha düşük hassasiyet nedeniyle INT4 sayısallaştırması genellikle daha büyük bir hassasiyet kaybına yol açar. Ancak, INT8 sayısallaştırmasıyla karşılaştırıldığında, INT4 sayısallaştırması modelin depolama gereksinimlerini ve hesaplama karmaşıklığını daha da azaltabilir. Bununla birlikte, INT4 sayısallaştırması pratik uygulamalarda nispeten nadirdir, çünkü çok düşük hassasiyet model performansında önemli bir düşüşe neden olabilir. Ayrıca, tüm donanımlar INT4 işlemlerini desteklemez, bu nedenle bir sayısallaştırma yöntemi seçerken donanım uyumluluğu dikkate alınmalıdır.

### **INT8**

INT8 sayısallaştırması, bir modelin ağırlıklarını ve aktivasyonlarını kayan noktalı sayılardan 8 bitlik tamsayılara dönüştürme işlemidir. INT8 tamsayılarının temsil ettiği sayısal aralık daha küçük ve daha az hassas olmasına rağmen, depolama ve hesaplama gereksinimlerini önemli ölçüde azaltabilir. INT8 sayısallaştırmasında, modelin ağırlıkları ve aktivasyon değerleri bir sayısallaştırma sürecinden geçer; bu süreç, ölçeklendirme ve kaydırmayı içererek orijinal kayan nokta bilgisini mümkün olduğunca korumayı amaçlar. Çıkarım sırasında, bu sayısallaştırılmış değerler hesaplama için tekrar kayan nokta sayılara dönüştürülür ve ardından bir sonraki adım için tekrar INT8'e sayısallaştırılır. Bu yöntem, çoğu uygulamada yeterli hassasiyet sağlarken yüksek hesaplama verimliliğini koruyabilir.

### **FP16**

FP16 formatı, yani 16 bitlik kayan nokta sayılar (float16), 32 bitlik kayan nokta sayılara (float32) kıyasla bellek kullanımını yarıya indirir ve bu, büyük ölçekli derin öğrenme uygulamalarında önemli avantajlar sunar. FP16 formatı, aynı GPU bellek sınırlamaları dahilinde daha büyük modellerin yüklenmesine veya daha fazla verinin işlenmesine olanak tanır. Modern GPU donanımları FP16 işlemlerini desteklemeye devam ettikçe, FP16 formatını kullanmak hesaplama hızında da iyileşmeler sağlayabilir. Ancak, FP16 formatının doğal dezavantajları da vardır; daha düşük hassasiyet, bazı durumlarda sayısal kararsızlık veya hassasiyet kaybına yol açabilir.

### **FP32**

FP32 formatı, daha yüksek hassasiyet sağlar ve geniş bir değer aralığını doğru bir şekilde temsil edebilir. Karmaşık matematiksel işlemlerin gerçekleştirildiği veya yüksek hassasiyetli sonuçların gerektiği senaryolarda, FP32 formatı tercih edilir. Ancak, yüksek hassasiyet aynı zamanda daha fazla bellek kullanımı ve daha uzun hesaplama süresi anlamına gelir. Büyük ölçekli derin öğrenme modellerinde, özellikle çok sayıda model parametresi ve büyük miktarda veri olduğunda, FP32 formatı GPU belleğinin yetersiz kalmasına veya çıkarım hızının düşmesine neden olabilir.

Mobil cihazlarda veya IoT cihazlarında, Phi-3.x modellerini INT4'e dönüştürebiliriz, AI PC / Copilot PC gibi cihazlarda ise INT8, FP16, FP32 gibi daha yüksek hassasiyetler kullanılabilir.

Şu anda, farklı donanım üreticilerinin jeneratif modelleri desteklemek için farklı çerçeveleri bulunmaktadır, örneğin Intel'in OpenVINO'su, Qualcomm'un QNN'si, Apple'ın MLX'i ve Nvidia'nın CUDA'sı gibi. Model sayısallaştırma ile birleştirildiğinde, yerel dağıtım tamamlanabilir.

Teknoloji açısından, sayısallaştırma sonrasında PyTorch / Tensorflow formatı, GGUF ve ONNX gibi farklı format desteklerimiz bulunmaktadır. GGUF ve ONNX arasında bir format karşılaştırması ve uygulama senaryoları yaptım. Burada, model çerçevesinden donanıma kadar iyi bir destek sunan ONNX sayısallaştırma formatını öneriyorum. Bu bölümde, GenAI için ONNX Runtime, OpenVINO ve Apple MLX kullanarak model sayısallaştırma işlemini ele alacağız (daha iyi bir yönteminiz varsa, bize PR göndererek iletebilirsiniz).

**Bu bölüm şunları içerir:**

1. [Phi-3.5 / 4'ü llama.cpp kullanarak sayısallaştırma](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4'ü onnxruntime için Generative AI uzantılarını kullanarak sayısallaştırma](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4'ü Intel OpenVINO kullanarak sayısallaştırma](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4'ü Apple MLX Framework kullanarak sayısallaştırma](./UsingAppleMLXQuantifyingPhi.md)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal diliyle hazırlanmış hali, bağlayıcı kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanabilecek yanlış anlama veya yorumlamalardan sorumlu değiliz.