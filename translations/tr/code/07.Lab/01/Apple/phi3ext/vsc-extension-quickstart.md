# VS Code Uzantınıza Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, uzantınız için gerekli tüm dosyaları içerir.
* `package.json` - uzantınızı ve komutunuzu tanımladığınız manifest dosyasıdır.
  * Örnek eklenti bir komut kaydeder ve onun başlığını ve komut adını tanımlar. Bu bilgilerle VS Code, komutu komut paletinde gösterebilir. Henüz eklentiyi yüklemesine gerek yoktur.
* `src/extension.ts` - komutunuzun uygulanmasını sağlayacağınız ana dosyadır.
  * Dosya, uzantınız ilk kez etkinleştirildiğinde (bu durumda komut çalıştırılarak) çağrılan `activate` adlı bir fonksiyonu dışa aktarır. `activate` fonksiyonu içinde `registerCommand` çağrılır.
  * Komutun uygulanmasını içeren fonksiyonu, `registerCommand` fonksiyonuna ikinci parametre olarak geçiririz.

## Kurulum

* Önerilen uzantıları yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint).

## Hemen Başlayın

* Uzantınız yüklü halde yeni bir pencere açmak için `F5` tuşlarına basın.
* Komut paletinden (`Ctrl+Shift+P` veya Mac'te `Cmd+Shift+P`) tuşlarına basarak ve `Hello World` yazarak komutunuzu çalıştırın.
* Uzantınızı hata ayıklamak için `src/extension.ts` içindeki kodda kesme noktaları ayarlayın.
* Uzantınızdan gelen çıktıyı hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` dosyasındaki kodu değiştirdikten sonra uzantıyı hata ayıklama araç çubuğundan yeniden başlatabilirsiniz.
* Ayrıca, uzantınızı yüklemek için VS Code penceresini (`Ctrl+R` veya Mac'te `Cmd+R`) yeniden yükleyebilirsiniz.

## API'yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açtığınızda API'mizin tam setini görebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) uzantısını yükleyin.
* **Tasks: Run Task** komutuyla "watch" görevini çalıştırın. Bunun çalıştığından emin olun, aksi takdirde testler algılanamayabilir.
* Aktivite çubuğundan Test Görünümünü açın ve "Run Test" butonuna tıklayın ya da `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarının çıktısını Test Sonuçları görünümünde görebilirsiniz.
* `src/test/extension.test.ts` üzerinde değişiklikler yapın veya `test` klasörü içinde yeni test dosyaları oluşturun.
  * Sağlanan test çalıştırıcı, yalnızca `**.test.ts` ad desenine uyan dosyaları dikkate alacaktır.
  * Testlerinizi istediğiniz şekilde düzenlemek için `test` klasörü içinde klasörler oluşturabilirsiniz.

## Daha İleriye Gidin

* Uzantınızın boyutunu azaltın ve başlangıç süresini iyileştirin: [Uzantınızı paketleyin](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* Uzantınızı VS Code uzantı pazarında [yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) kurarak yapıları otomatikleştirin.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.