# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU ve RAG Modelini Tanıtan Demo

Phi-3.5 Onnx Hosted modeliyle kullanılan RAG Modeli, Retrieval-Augmented Generation yaklaşımından yararlanarak, Phi-3.5 modellerinin gücünü ONNX hosting ile birleştirerek verimli yapay zeka dağıtımları sağlar. Bu model, alanına özgü görevler için modellerin ince ayarını yapmakta etkili olup, kalite, maliyet etkinliği ve uzun bağlam anlama özelliklerini bir araya getirir. Azure AI'nin sunduğu geniş model yelpazesinin bir parçası olan bu model, çeşitli sektörlerin özelleştirme ihtiyaçlarına hitap eden, bulması, denemesi ve kullanması kolay çözümler sunar.

## WebGPU Nedir
WebGPU, modern bir web grafik API'sidir ve web tarayıcılarından doğrudan bir cihazın grafik işlem birimine (GPU) verimli erişim sağlamak için tasarlanmıştır. WebGL'nin halefi olması amaçlanan WebGPU, birkaç önemli iyileştirme sunar:

1. **Modern GPU’larla Uyumluluk**: WebGPU, çağdaş GPU mimarileriyle sorunsuz çalışacak şekilde tasarlanmıştır ve Vulkan, Metal ve Direct3D 12 gibi sistem API'lerini kullanır.
2. **Geliştirilmiş Performans**: Genel amaçlı GPU hesaplamalarını ve daha hızlı işlemleri destekler, bu da onu hem grafik işleme hem de makine öğrenimi görevleri için uygun hale getirir.
3. **Gelişmiş Özellikler**: Daha karmaşık ve dinamik grafik ve hesaplama iş yüklerini mümkün kılan gelişmiş GPU yeteneklerine erişim sağlar.
4. **Azaltılmış JavaScript İş Yükü**: Daha fazla görevi GPU'ya devrederek, JavaScript üzerindeki yükü önemli ölçüde azaltır ve daha iyi performans ve daha akıcı deneyimler sunar.

WebGPU şu anda Google Chrome gibi tarayıcılarda desteklenmektedir ve diğer platformlara destek genişletmek için çalışmalar devam etmektedir.

### 03.WebGPU
Gerekli Ortam:

**Desteklenen tarayıcılar:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU’yu Etkinleştirme:

- Chrome/Microsoft Edge’de 

`chrome://flags/#enable-unsafe-webgpu` bayrağını etkinleştirin.

#### Tarayıcınızı Açın:
Google Chrome veya Microsoft Edge’i başlatın.

#### Bayraklar Sayfasına Erişin:
Adres çubuğuna `chrome://flags` yazın ve Enter tuşuna basın.

#### Bayrağı Arayın:
Sayfanın üst kısmındaki arama kutusuna 'enable-unsafe-webgpu' yazın.

#### Bayrağı Etkinleştirin:
Sonuçlar listesindeki #enable-unsafe-webgpu bayrağını bulun.

Yanındaki açılır menüye tıklayın ve Etkin seçeneğini seçin.

#### Tarayıcınızı Yeniden Başlatın:

Bayrağı etkinleştirdikten sonra, değişikliklerin geçerli olması için tarayıcınızı yeniden başlatmanız gerekecek. Sayfanın alt kısmında beliren Yeniden Başlat düğmesine tıklayın.

- Linux için, tarayıcıyı `--enable-features=Vulkan` ile başlatın.
- Safari 18 (macOS 15), WebGPU’yu varsayılan olarak etkinleştirir.
- Firefox Nightly’de, adres çubuğuna about:config yazın ve `set dom.webgpu.enabled to true`.

### Microsoft Edge için GPU Ayarı Yapma 

Windows'ta Microsoft Edge için yüksek performanslı GPU ayarlamak için şu adımları izleyin:

- **Ayarları Açın:** Başlat menüsüne tıklayın ve Ayarlar’ı seçin.
- **Sistem Ayarları:** Sistem’e ve ardından Ekran’a gidin.
- **Grafik Ayarları:** Aşağı kaydırın ve Grafik ayarları’na tıklayın.
- **Uygulama Seçin:** “Tercih belirlemek için bir uygulama seçin” altında Masaüstü uygulaması’nı seçin ve ardından Gözat’a tıklayın.
- **Edge’i Seçin:** Edge kurulum klasörüne gidin (genellikle `C:\Program Files (x86)\Microsoft\Edge\Application`) ve `msedge.exe`’yi seçin.
- **Tercih Belirleyin:** Seçenekler’e tıklayın, Yüksek performans’ı seçin ve ardından Kaydet’e tıklayın.
Bu, Microsoft Edge’in daha iyi performans için yüksek performanslı GPU’nuzu kullanmasını sağlayacaktır.
- Bu ayarların geçerli olması için **bilgisayarınızı yeniden başlatın**.

### Örnekler: Lütfen [bu bağlantıya tıklayın](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki versiyonu, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.