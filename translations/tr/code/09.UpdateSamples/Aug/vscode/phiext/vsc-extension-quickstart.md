# VS Code Eklentisine Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, eklentiniz için gerekli olan tüm dosyaları içerir.
* `package.json` - bu, eklentinizi ve komutunuzu tanımladığınız manifest dosyasıdır.
  * Örnek eklenti bir komut kaydeder ve bunun başlığını ve komut adını tanımlar. Bu bilgilerle VS Code komutu komut paletinde gösterebilir. Henüz eklentiyi yüklemesi gerekmez.
* `src/extension.ts` - bu, komutunuzun uygulamasını sağlayacağınız ana dosyadır.
  * Dosya, eklentiniz ilk kez etkinleştirildiğinde (bu durumda komut çalıştırılarak) çağrılan `activate` adlı bir fonksiyon dışa aktarır. `activate` fonksiyonunun içinde `registerCommand` çağrılır.
  * Komutun uygulamasını içeren fonksiyonu, `registerCommand`'e ikinci parametre olarak geçiririz.

## Kurulum

* Önerilen eklentileri yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint).

## Hemen Başlayın

* Eklentiniz yüklü olarak yeni bir pencere açmak için `F5` tuşuna basın.
* Komutunuzu komut paletinden (`Ctrl+Shift+P` veya Mac'te `Cmd+Shift+P`) tuşlarına basarak ve `Hello World` yazarak çalıştırın.
* Eklentinizi hata ayıklamak için `src/extension.ts` içinde kodunuza kesme noktaları ekleyin.
* Eklentinizin çıktısını hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` dosyasındaki kodu değiştirdikten sonra hata ayıklama araç çubuğundan eklentiyi yeniden başlatabilirsiniz.
* Ayrıca, eklentinizi yüklemek için VS Code penceresini yeniden yükleyebilirsiniz (`Ctrl+R` veya Mac'te `Cmd+R`).

## API'yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açtığınızda API'nin tam setini görebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) eklentisini yükleyin.
* **Tasks: Run Task** komutuyla "watch" görevini çalıştırın. Bunun çalıştığından emin olun, aksi takdirde testler algılanamayabilir.
* Aktivite çubuğundan Testing görünümünü açın ve "Run Test" düğmesine tıklayın ya da `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarının çıktısını Test Sonuçları görünümünde görün.
* `src/test/extension.test.ts` üzerinde değişiklikler yapın veya `test` klasörü içinde yeni test dosyaları oluşturun.
  * Sağlanan test çalıştırıcı, yalnızca `**.test.ts` ad düzenine uyan dosyaları dikkate alacaktır.
  * Testlerinizi istediğiniz şekilde düzenlemek için `test` klasörü içinde alt klasörler oluşturabilirsiniz.

## Daha İleri Gidin

* [Eklentinizi paketleyerek](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) eklenti boyutunu küçültün ve başlangıç süresini iyileştirin.
* Eklentinizi [VS Code eklenti pazarında yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) kurarak otomatik derlemeler yapın.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, bağlayıcı kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.