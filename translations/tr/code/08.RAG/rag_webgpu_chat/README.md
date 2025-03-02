Phi-3-mini WebGPU RAG Chatbot

## WebGPU ve RAG Modeli Tanıtımı için Demo
Phi-3 Onnx barındırmalı model ile RAG Modeli, Retrieval-Augmented Generation (Bilgi Erişim Destekli Üretim) yaklaşımını kullanır. Bu model, Phi-3 modellerinin gücünü ONNX barındırma ile birleştirerek etkili bir yapay zeka dağıtımı sunar. Bu yapı, alan odaklı görevler için modelleri optimize etmekte önemli bir rol oynar ve kalite, maliyet etkinliği ve uzun bağlam anlayışını bir araya getirir. Azure AI'nın bir parçası olan bu model, çeşitli endüstrilerin özelleştirme ihtiyaçlarını karşılamak için kolayca bulunabilir, denenebilir ve kullanılabilir geniş bir model seçeneği sunar. Phi-3 modelleri, Phi-3-mini, Phi-3-small ve Phi-3-medium dahil olmak üzere Azure AI Model Catalog'da mevcuttur ve kendi kendine yönetimle veya HuggingFace ve ONNX gibi platformlar üzerinden özelleştirilebilir ve dağıtılabilir. Bu, Microsoft’un erişilebilir ve etkili yapay zeka çözümlerine olan bağlılığını göstermektedir.

## WebGPU Nedir?
WebGPU, web tarayıcılarından doğrudan bir cihazın grafik işlem birimine (GPU) verimli erişim sağlamak için tasarlanmış modern bir web grafik API'sidir. WebGL'nin halefi olarak tasarlanmış olup aşağıdaki önemli iyileştirmeleri sunar:

1. **Modern GPU'larla Uyumluluk**: WebGPU, Vulkan, Metal ve Direct3D 12 gibi sistem API'lerini kullanarak modern GPU mimarileriyle sorunsuz çalışmak üzere tasarlanmıştır.
2. **Gelişmiş Performans**: Genel amaçlı GPU hesaplamalarını ve daha hızlı işlemleri destekler, bu da hem grafik işleme hem de makine öğrenimi görevleri için uygun hale getirir.
3. **İleri Düzey Özellikler**: Daha karmaşık ve dinamik grafik ve hesaplama iş yüklerini mümkün kılan gelişmiş GPU özelliklerine erişim sağlar.
4. **Azaltılmış JavaScript İş Yükü**: Daha fazla görevi GPU'ya devrederek, JavaScript üzerindeki iş yükünü önemli ölçüde azaltır ve daha iyi performans ve daha akıcı deneyimler sunar.

WebGPU şu anda Google Chrome gibi tarayıcılarda desteklenmektedir ve diğer platformlara destek sağlama çalışmaları devam etmektedir.

### 03.WebGPU
Gerekli Ortam:

**Desteklenen Tarayıcılar:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly  

### WebGPU’yu Etkinleştirme:

- Chrome/Microsoft Edge’de  

`chrome://flags/#enable-unsafe-webgpu` bayrağını etkinleştirin.

#### Tarayıcınızı Açın:
Google Chrome veya Microsoft Edge’i başlatın.

#### Flags Sayfasına Erişin:
Adres çubuğuna `chrome://flags` yazın ve Enter tuşuna basın.

#### Bayrağı Arayın:
Sayfanın üst kısmındaki arama kutusuna 'enable-unsafe-webgpu' yazın.

#### Bayrağı Etkinleştirin:
Sonuçlar listesindeki #enable-unsafe-webgpu bayrağını bulun.  
Yanındaki açılır menüye tıklayın ve Etkinleştir’i seçin.

#### Tarayıcınızı Yeniden Başlatın:
Bayrağı etkinleştirdikten sonra değişikliklerin etkili olması için tarayıcınızı yeniden başlatmanız gerekecek. Sayfanın alt kısmında beliren Yeniden Başlat düğmesine tıklayın.

- Linux için tarayıcıyı `--enable-features=Vulkan` ile başlatın.  
- Safari 18 (macOS 15) varsayılan olarak WebGPU’yu etkinleştirmiştir.  
- Firefox Nightly’de, adres çubuğuna about:config yazın ve `set dom.webgpu.enabled to true`.

### Microsoft Edge için GPU Ayarlarını Yapılandırma

Windows’ta Microsoft Edge için yüksek performanslı bir GPU ayarlamak için şu adımları izleyin:

- **Ayarları Açın:** Başlat menüsüne tıklayın ve Ayarlar’ı seçin.  
- **Sistem Ayarları:** Sistem’e ve ardından Ekran’a gidin.  
- **Grafik Ayarları:** Aşağı kaydırın ve Grafik ayarları’na tıklayın.  
- **Uygulama Seçin:** “Tercih ayarlamak için bir uygulama seçin” altında Masaüstü uygulaması’nı seçin ve ardından Gözat’a tıklayın.  
- **Edge’i Seçin:** Edge kurulum klasörüne gidin (genellikle `C:\Program Files (x86)\Microsoft\Edge\Application`) ve `msedge.exe`’yi seçin.  
- **Tercihi Ayarlayın:** Seçenekler’e tıklayın, Yüksek performans’ı seçin ve ardından Kaydet’e tıklayın.  
Bu, Microsoft Edge’in daha iyi performans için yüksek performanslı GPU’nuzu kullanmasını sağlar.  
- **Makinenizi Yeniden Başlatın** bu ayarların etkili olması için.

### Kod Alanınızı Açın:
GitHub üzerindeki deponuza gidin.  
Kod düğmesine tıklayın ve Kod Alanları ile Aç’ı seçin.  

Henüz bir Kod Alanınız yoksa, Yeni kod alanı oluştur’a tıklayarak bir tane oluşturabilirsiniz.

**Not:** Kod alanınıza Node Ortamı Kurulumu  
GitHub Kod Alanından bir npm demosu çalıştırmak, projenizi test etmek ve geliştirmek için harika bir yoldur. İşte başlamanıza yardımcı olacak adım adım bir rehber:

### Ortamınızı Ayarlayın:
Kod alanınız açıkken, Node.js ve npm’nin kurulu olduğundan emin olun. Bunu kontrol etmek için şu komutları çalıştırabilirsiniz:  
```
node -v
```  
```
npm -v
```  

Eğer kurulu değillerse, şu komutlarla kurabilirsiniz:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```  

### Proje Dizininize Geçin:
Terminali kullanarak npm projenizin bulunduğu dizine geçin:  
```
cd path/to/your/project
```  

### Bağımlılıkları Kurun:
package.json dosyanızda listelenen tüm gerekli bağımlılıkları kurmak için şu komutu çalıştırın:  

```
npm install
```  

### Demoyu Çalıştırın:
Bağımlılıklar kurulduktan sonra demo scriptinizi çalıştırabilirsiniz. Bu genellikle package.json dosyanızın scripts bölümünde belirtilir. Örneğin, demo scriptinizin adı start ise, şu komutu çalıştırabilirsiniz:  

```
npm run build
```  
```
npm run dev
```  

### Demoya Erişim:
Eğer demonuz bir web sunucusunu içeriyorsa, Kod Alanları size ona erişim sağlayacak bir URL sunar. Bir bildirim arayın veya URL’yi bulmak için Ports sekmesini kontrol edin.

**Not:** Modelin tarayıcıda önbelleğe alınması gerekir, bu yüzden yüklenmesi biraz zaman alabilir.

### RAG Demo
`intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` markdown dosyasını yükleyin.

### Dosyanızı Seçin:
Yüklemek istediğiniz belgeyi seçmek için “Dosya Seç” düğmesine tıklayın.

### Belgeyi Yükleyin:
Belgenizi RAG (Bilgi Erişim Destekli Üretim) için yüklemek üzere “Yükle” düğmesine tıklayın.

### Sohbete Başlayın:
Belge yüklendikten sonra, belgenizin içeriğine dayalı olarak RAG kullanarak bir sohbet oturumu başlatabilirsiniz.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.