Bu demo, bir önceden eğitilmiş modeli kullanarak bir resim ve bir metin istemi temelinde Python kodu üretmeyi nasıl gerçekleştirebileceğinizi gösterir.

[Örnek Kod](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

İşte adım adım bir açıklama:

1. **İçe Aktarmalar ve Kurulum**:
   - Gerekli kütüphaneler ve modüller içe aktarılır, bunlar arasında `requests`, `PIL` görüntü işleme için ve `transformers` modelin işlenmesi ve kullanılması için bulunur.

2. **Görüntünün Yüklenmesi ve Gösterilmesi**:
   - `demo.png` kullanılarak bir görüntü dosyası açılır ve `PIL` kütüphanesi ile görüntülenir.

3. **İstemin Tanımlanması**:
   - Görüntüyü içeren ve görüntüyü işlemek ve `plt` (matplotlib) kullanarak kaydetmek için Python kodu üretme talebini içeren bir mesaj oluşturulur.

4. **İşleyicinin Yüklenmesi**:
   - `AutoProcessor`, `out_dir` dizini tarafından belirtilen bir önceden eğitilmiş modelden yüklenir. Bu işleyici, metin ve görüntü girdilerini işlemekten sorumludur.

5. **İstemin Oluşturulması**:
   - `apply_chat_template` yöntemi, mesajı modele uygun bir isteme dönüştürmek için kullanılır.

6. **Girdilerin İşlenmesi**:
   - İstem ve görüntü, modelin anlayabileceği tensörlere dönüştürülür.

7. **Üretim Argümanlarının Ayarlanması**:
   - Modelin üretim süreci için maksimum yeni token sayısı ve çıktı örneklemesinin yapılıp yapılmayacağı gibi argümanlar tanımlanır.

8. **Kodun Üretilmesi**:
   - Model, girdiler ve üretim argümanları temelinde Python kodu üretir. `TextStreamer`, istemi ve özel tokenları atlamak için çıktıyı işler.

9. **Çıktı**:
   - Üretilen kod yazdırılır; bu kod, görüntüyü işlemek ve istemde belirtildiği gibi kaydetmek için gerekli olan Python kodunu içermelidir.

Bu demo, OpenVino kullanarak bir önceden eğitilmiş modelden faydalanarak kullanıcı girdileri ve görüntülerine dayalı olarak dinamik şekilde kod üretmeyi nasıl gerçekleştirebileceğinizi göstermektedir.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, bağlayıcı kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yorumlamalardan sorumlu değiliz.