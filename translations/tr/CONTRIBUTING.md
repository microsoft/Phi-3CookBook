# Katkıda Bulunma

Bu proje katkıları ve önerileri memnuniyetle karşılar. Çoğu katkı, bize katkınızı kullanma haklarını verdiğinizi ve buna hakkınız olduğunu beyan eden bir Katkıda Bulunma Lisans Anlaşması'nı (CLA) kabul etmenizi gerektirir. Ayrıntılar için [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com) adresini ziyaret edebilirsiniz.

Bir pull request gönderdiğinizde, bir CLA botu otomatik olarak bir CLA sağlayıp sağlamanız gerektiğini belirler ve PR'ı uygun şekilde işaretler (ör. durum kontrolü, yorum). Botun sağladığı talimatları takip etmeniz yeterlidir. Tüm CLA kullanan depolar için bunu yalnızca bir kez yapmanız gerekecek.

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kuralları'nı](https://opensource.microsoft.com/codeofconduct/) benimsemiştir. Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) adresini okuyabilir veya [opencode@microsoft.com](mailto:opencode@microsoft.com) adresine ek sorular veya yorumlar gönderebilirsiniz.

## Sorun Oluştururken Dikkat Edilmesi Gerekenler

Genel destek soruları için GitHub sorunları açmayınız, çünkü GitHub listesi özellik talepleri ve hata raporları için kullanılmalıdır. Bu şekilde, koddaki gerçek sorunları veya hataları daha kolay takip edebilir ve genel tartışmaları koddan ayrı tutabiliriz.

## Nasıl Katkıda Bulunulur

### Pull Request Rehberi

Phi-3 CookBook deposuna bir pull request (PR) gönderirken lütfen şu yönergeleri takip edin:

- **Depoyu Fork Edin**: Değişikliklerinizi yapmadan önce her zaman depoyu kendi hesabınıza fork edin.

- **Ayrı pull request'ler (PR)**:
  - Her tür değişikliği kendi pull request'inde gönderin. Örneğin, hata düzeltmeleri ve belge güncellemeleri ayrı PR'lar olarak gönderilmelidir.
  - Yazım hatası düzeltmeleri ve küçük belge güncellemeleri uygun olduğunda tek bir PR'de birleştirilebilir.

- **Birleşme çatışmalarını yönetin**: Pull request'iniz birleşme çatışmaları gösteriyorsa, yerel `main` dalınızı ana depoyla eşleştirmek için güncelleyin ve ardından değişikliklerinizi yapın.

- **Çeviri gönderimleri**: Bir çeviri PR'ı gönderirken, çeviri klasörünün orijinal klasördeki tüm dosyaların çevirilerini içerdiğinden emin olun.

### Çeviri Rehberi

> [!IMPORTANT]
>
> Bu depodaki metinleri çevirirken makine çevirisi kullanmayın. Yalnızca yetkin olduğunuz dillerde çeviri yapmayı gönüllü olarak üstlenin.

Eğer İngilizce dışındaki bir dilde yetkinseniz, içeriği çevirmeye yardımcı olabilirsiniz. Çeviri katkılarınızın doğru bir şekilde entegre edilmesini sağlamak için şu adımları izleyin:

- **Çeviri klasörü oluşturun**: Uygun bölüm klasörüne gidin ve katkıda bulunduğunuz dil için bir çeviri klasörü oluşturun. Örneğin:
  - Giriş bölümü için: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Hızlı başlangıç bölümü için: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Diğer bölümler için bu deseni sürdürün (03.Inference, 04.Finetuning, vb.)

- **Göreceli yolları güncelleyin**: Çeviri yaparken, markdown dosyalarındaki göreceli yolların başına `../../` ekleyerek klasör yapısını ayarlayın. Örneğin, aşağıdaki gibi değiştirin:
  - `(../../imgs/01/phi3aisafety.png)`'i `(../../../../imgs/01/phi3aisafety.png)` olarak değiştirin.

- **Çevirilerinizi düzenleyin**: Her çevrilmiş dosya, ilgili bölümün çeviri klasörüne yerleştirilmelidir. Örneğin, giriş bölümünü İspanyolcaya çeviriyorsanız, aşağıdaki gibi bir yapı oluşturun:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Tam bir PR gönderin**: Bir bölüm için tüm çevrilmiş dosyaların bir PR'de dahil edildiğinden emin olun. Bir bölüm için kısmi çeviriler kabul edilmez. Bir çeviri PR'ı gönderirken, çeviri klasörünün orijinal klasördeki tüm dosyaların çevirilerini içerdiğinden emin olun.

### Yazım Rehberi

Tüm belgelerde tutarlılığı sağlamak için lütfen şu yönergeleri kullanın:

- **URL formatı**: Tüm URL'leri köşeli parantez içine alın ve ardından parantez içinde yazın, etrafında veya içinde ekstra boşluk bırakmayın. Örneğin: `[example](https://www.microsoft.com)`.

- **Göreceli bağlantılar**: Mevcut dizindeki dosyalara veya klasörlere işaret eden bağlantılar için `./`, üst dizindeki dosyalara veya klasörlere işaret eden bağlantılar için `../` kullanın. Örneğin: `[example](../../path/to/file)` veya `[example](../../../path/to/file)`.

- **Ülkeye özgü olmayan yereller**: Bağlantılarınızın ülkeye özgü yereller içermediğinden emin olun. Örneğin, `/en-us/` veya `/en/` gibi bağlantılardan kaçının.

- **Görsellerin depolanması**: Tüm görselleri `./imgs` klasöründe saklayın.

- **Açıklayıcı görsel isimleri**: Görselleri, İngilizce karakterler, sayılar ve tireler kullanarak açıklayıcı şekilde adlandırın. Örneğin: `example-image.jpg`.

## GitHub İş Akışları

Bir pull request gönderdiğinizde, değişiklikleri doğrulamak için aşağıdaki iş akışları tetiklenecektir. Pull request'inizin iş akışı kontrollerinden geçmesini sağlamak için aşağıdaki talimatları izleyin:

- [Bozuk Göreceli Yolları Kontrol Et](../..)
- [Bağlantıların Yerel İçermediğini Kontrol Et](../..)

### Bozuk Göreceli Yolları Kontrol Et

Bu iş akışı, dosyalarınızdaki tüm göreceli yolların doğru olduğunu doğrular.

1. Bağlantılarınızın düzgün çalıştığından emin olmak için şu görevleri VS Code kullanarak gerçekleştirin:
    - Dosyalarınızdaki herhangi bir bağlantının üzerine gelin.
    - Bağlantıya gitmek için **Ctrl + Tıkla** yapın.
    - Bir bağlantıya tıklayıp yerel olarak çalışmıyorsa, bu iş akışı tetiklenir ve GitHub'da çalışmaz.

1. Bu sorunu düzeltmek için, VS Code tarafından sağlanan yol önerilerini kullanarak şu görevleri gerçekleştirin:
    - `./` veya `../` yazın.
    - VS Code, yazdıklarınıza göre mevcut seçeneklerden seçim yapmanızı isteyecektir.
    - Yolun doğru olduğundan emin olmak için istediğiniz dosya veya klasöre tıklayarak yolu takip edin.

Doğru göreceli yolu ekledikten sonra değişikliklerinizi kaydedin ve gönderin.

### Bağlantıların Yerel İçermediğini Kontrol Et

Bu iş akışı, herhangi bir web URL'sinin ülkeye özgü bir yerel içermediğini doğrular. Bu depo küresel olarak erişilebilir olduğu için, URL'lerin ülkenizin yerelini içermediğinden emin olmak önemlidir.

1. URL'lerinizin ülke yerellerini içermediğinden emin olmak için şu görevleri gerçekleştirin:

    - URL'lerde `/en-us/`, `/en/` veya başka bir dil yereli gibi metinler arayın.
    - Bu yereller URL'lerinizde yoksa, bu kontrolü geçeceksiniz.

1. Bu sorunu düzeltmek için şu görevleri gerçekleştirin:
    - İş akışı tarafından vurgulanan dosya yolunu açın.
    - URL'lerden ülke yerelini kaldırın.

Ülke yerelini kaldırdıktan sonra değişikliklerinizi kaydedin ve gönderin.

### Bozuk URL'leri Kontrol Et

Bu iş akışı, dosyalarınızdaki herhangi bir web URL'sinin çalıştığını ve 200 durum kodu döndürdüğünü doğrular.

1. URL'lerinizin doğru çalıştığını doğrulamak için şu görevleri gerçekleştirin:
    - Dosyalarınızdaki URL'lerin durumunu kontrol edin.

2. Bozuk URL'leri düzeltmek için şu görevleri gerçekleştirin:
    - Bozuk URL'yi içeren dosyayı açın.
    - URL'yi doğru olanla güncelleyin.

URL'leri düzelttikten sonra değişikliklerinizi kaydedin ve gönderin.

> [!NOTE]
>
> URL kontrolünün başarısız olabileceği ancak bağlantının erişilebilir olduğu durumlar olabilir. Bunun birkaç nedeni olabilir, örneğin:
>
> - **Ağ kısıtlamaları:** GitHub eylem sunucuları, belirli URL'lere erişimi engelleyen ağ kısıtlamalarına sahip olabilir.
> - **Zaman aşımı sorunları:** Yanıt vermesi çok uzun süren URL'ler, iş akışında zaman aşımı hatasına neden olabilir.
> - **Geçici sunucu sorunları:** Ara sıra sunucu kesintileri veya bakım, doğrulama sırasında bir URL'yi geçici olarak kullanılamaz hale getirebilir.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.