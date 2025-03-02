# VS Code Extension-ээ тавтай морил

## Хавтасны агуулга

* Энэ хавтас таны өргөтгөлд шаардлагатай бүх файлуудыг агуулдаг.
* `package.json` - энэ нь таны өргөтгөл болон командуудыг тодорхойлдог манифест файл юм.
  * Жишээ плагин нь нэг команд бүртгэж, түүний гарчиг болон командын нэрийг тодорхойлсон. Энэ мэдээллээр VS Code командын палеттад командыг харуулж чадна. Гэхдээ одоогоор плагинийг ачаалах шаардлагагүй.
* `src/extension.ts` - энэ бол таны командын хэрэгжүүлэлтийг өгөх үндсэн файл.
  * Файл нь `activate` нэртэй нэг функцыг экспортолдог бөгөөд энэ нь өргөтгөл идэвхжих үед хамгийн анх дуудагддаг (энэ тохиолдолд командыг ажиллуулах замаар). `activate` функц дотор бид `registerCommand`-г дууддаг.
  * Бид командын хэрэгжүүлэлтийг агуулсан функцийг `registerCommand`-д хоёр дахь параметр болгон дамжуулдаг.

## Тохиргоо

* Санал болгосон өргөтгөлүүдийг суулгаарай (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, болон dbaeumer.vscode-eslint)

## Шууд ажиллуулах

* Таны өргөтгөл ачаалагдсан шинэ цонх нээхийн тулд `F5` товчийг дар.
* Командаа командын палеттаас ажиллуулахын тулд (`Ctrl+Shift+P` эсвэл Mac дээр `Cmd+Shift+P`) дарж `Hello World` гэж бич.
* Таны өргөтгөлийн `src/extension.ts` доторх кодонд breakpoints тавьж дебаг хийх.
* Таны өргөтгөлөөс гарч буй үр дүнг дебаг консол дээрээс олж харах.

## Өөрчлөлт хийх

* `src/extension.ts` доторх кодыг өөрчилсний дараа дебагийн баараас өргөтгөлөө дахин ачаалж болно.
* Мөн VS Code цонхыг дахин ачаалж (`Ctrl+R` эсвэл Mac дээр `Cmd+R`) өөрчлөлтүүдээ ачаалж болно.

## API-г судлах

* `node_modules/@types/vscode/index.d.ts` файлыг нээж API-гийн бүх багцыг үзэж болно.

## Тест ажиллуулах

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)-г суулга.
* **Tasks: Run Task** командаар "watch" даалгаврыг ажиллуул. Энэ ажиллаж байгаа эсэхийг шалгаарай, эс бөгөөс тестүүд илрэхгүй байж магадгүй.
* Үйл ажиллагааны самбар дээрх Testing харагдацаас "Run Test" товчийг дарж эсвэл `Ctrl/Cmd + ; A` товчийг ашиглан тестээ ажиллуул.
* Тестийн үр дүнг Test Results харагдац дээрээс үзээрэй.
* `src/test/extension.test.ts` дээр өөрчлөлт хийж эсвэл `test` хавтас дотор шинэ тестийн файлууд үүсгээрэй.
  * Өгөгдсөн тестийн ажиллуулагч нь зөвхөн `**.test.ts` нэрийн загварт тохирсон файлуудыг тооцох болно.
  * Тестүүдээ хүссэнээрээ зохион байгуулахын тулд `test` хавтас дотор дэд хавтас үүсгэж болно.

## Цааш үргэлжлүүлэх

* Өргөтгөлөө [багцалж](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) өргөтгөлийн хэмжээг багасгаж, ачаалах хугацааг сайжруулаарай.
* Өргөтгөлөө [VS Code өргөтгөлүүдийн зах зээлд нийтэлнэ](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [Үргэлжилсэн интеграц](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)-ыг тохируулж, бүтээлүүдийг автоматжуул.

It seems like "mo" could refer to a specific language or abbreviation, but it's unclear which one you mean. Could you clarify the target language or provide more context? For example, "mo" might refer to Māori, Mongolian, or something else. Let me know so I can assist you better!