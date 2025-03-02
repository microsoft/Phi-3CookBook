# VS Code Eklentisine Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, eklentiniz için gerekli tüm dosyaları içerir.
* `package.json` - bu, eklentinizi ve komutunuzu tanımladığınız manifest dosyasıdır.
  * Örnek eklenti bir komut kaydeder ve bunun başlığını ve komut adını tanımlar. Bu bilgilerle VS Code, komutu komut paletinde gösterebilir. Henüz eklentiyi yüklemesine gerek yoktur.
* `src/extension.ts` - bu, komutunuzun uygulamasını sağlayacağınız ana dosyadır.
  * Dosya, bir fonksiyon olan `activate`'yi dışa aktarır. Bu fonksiyon, eklentiniz ilk kez etkinleştirildiğinde (bu durumda komut çalıştırılarak) çağrılır. `activate` fonksiyonunun içinde `registerCommand`'ü çağırırız.
  * Komutun uygulamasını içeren fonksiyonu `registerCommand`'e ikinci parametre olarak geçiririz.

## Kurulum

* Önerilen eklentileri yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint)

## Hemen Çalışmaya Başlayın

* Eklentiniz yüklü olarak yeni bir pencere açmak için `F5` tuşuna basın.
* Komutunuzu komut paletinden (`Ctrl+Shift+P` veya Mac'te `Cmd+Shift+P` tuşlarına basarak) ve `Hello World` yazarak çalıştırın.
* Eklentinizi hata ayıklamak için `src/extension.ts` içinde kodunuzda kesme noktaları belirleyin.
* Eklentinizin çıktısını hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` dosyasındaki kodu değiştirdikten sonra hata ayıklama araç çubuğundan eklentiyi yeniden başlatabilirsiniz.
* Ayrıca, eklentinizi yüklemek için VS Code penceresini (`Ctrl+R` veya Mac'te `Cmd+R`) yeniden yükleyebilirsiniz.

## API'yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açtığınızda API'mizin tam setine erişebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) eklentisini yükleyin.
* **Tasks: Run Task** komutuyla "watch" görevini çalıştırın. Bunun çalıştığından emin olun, aksi takdirde testler bulunamayabilir.
* Etkinlik çubuğundaki Test Görünümünü açın ve "Run Test" butonuna tıklayın veya `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarının çıktısını Test Sonuçları görünümünde inceleyin.
* `src/test/extension.test.ts` üzerinde değişiklik yapın veya `test` klasörü içinde yeni test dosyaları oluşturun.
  * Sağlanan test çalıştırıcı, yalnızca `**.test.ts` ad düzenine uyan dosyaları dikkate alacaktır.
  * Testlerinizi istediğiniz şekilde yapılandırmak için `test` klasörü içinde alt klasörler oluşturabilirsiniz.

## Daha Fazlasını Yapın

* [Eklentinizi paketleyerek](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) eklenti boyutunu küçültün ve başlangıç süresini iyileştirin.
* Eklentinizi [VS Code eklenti pazarında yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) kurarak yapıları otomatikleştirin.

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.