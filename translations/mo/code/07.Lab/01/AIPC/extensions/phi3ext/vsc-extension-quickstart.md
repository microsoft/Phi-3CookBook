# VS Code Extension-ээ тавтай морилно уу

## Энэ хавтас юуг агуулж байна вэ?

* Энэ хавтас таны өргөтгөлийг бүтээхэд шаардлагатай бүх файлуудыг агуулна.  
* `package.json` - энэ нь таны өргөтгөл болон командуудаа тодорхойлох манифест файл юм.  
  * Жишээ плагин нь нэг командыг бүртгэж, түүний гарчиг болон командын нэрийг тодорхойлдог. Энэ мэдээллээр VS Code командын палеттад командыг харуулж чадна. Гэхдээ одоохондоо плагинийг ачаалах шаардлагагүй.  
* `src/extension.ts` - энэ нь таны командын хэрэгжилтийг өгөх үндсэн файл юм.  
  * Энэ файл нэг функцыг экспортолдог, `activate`, энэ нь таны өргөтгөл анх идэвхжсэн (энэ тохиолдолд командыг ажиллуулах замаар) үед дуудагддаг. `activate` функцийн дотор бид `registerCommand`-ийг дуудагдана.  
  * Командын хэрэгжилтийг агуулсан функцийг `registerCommand`-д хоёр дахь параметр болгон дамжуулдаг.  

## Тохиргоо

* Зөвлөж буй өргөтгөлүүдийг суулгаарай (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, болон dbaeumer.vscode-eslint).  

## Шууд ажиллуулах

* `F5` товчийг дарж таны өргөтгөл ачаалагдсан шинэ цонх нээнэ.  
* Командаа командын палеттаас (`Ctrl+Shift+P` эсвэл `Cmd+Shift+P` Mac дээр) `Hello World` гэж бичин ажиллуул.  
* `src/extension.ts` дотор коддоо завсрын цэгүүдийг тавьж өргөтгөлөө дебаг хийгээрэй.  
* Өргөтгөлөөс гарч буй үр дүнг дебаг консолоос олоорой.  

## Өөрчлөлт оруулах

* `src/extension.ts` дотор кодоо өөрчилсний дараа дебаг баараас өргөтгөлөө дахин ачаалж болно.  
* Мөн VS Code цонхыг (`Ctrl+R` эсвэл `Cmd+R` Mac дээр) дахин ачаалж өөрчлөлтүүдээ ачаалж болно.  

## API судлах

* `node_modules/@types/vscode/index.d.ts` файлыг нээхэд бидний API-ийг бүрэн харж болно.  

## Туршилт ажиллуулах

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)-ийг суулгана уу.  
* **Tasks: Run Task** командаар "watch" үүргийг ажиллуулна уу. Энэ ажиллаж байгаа эсэхийг шалгаарай, эс тэгвээс туршилтууд илрэхгүй байж магадгүй.  
* Үйл ажиллагааны цэснээс Testing харагдац руу орж "Run Test" товчийг дарна уу, эсвэл `Ctrl/Cmd + ; A` товчлуурыг ашиглана уу.  
* Туршилтын үр дүнг Test Results харагдацаас харна уу.  
* `src/test/extension.test.ts` дээр өөрчлөлт оруулах эсвэл `test` хавтас дотор шинэ туршилтын файлууд үүсгээрэй.  
  * Өгөгдсөн туршилтын ажиллуулагч зөвхөн `**.test.ts` нэрийн загварт тохирсон файлуудыг авч үзнэ.  
  * `test` хавтас дотор өөрийн туршилтуудыг дурын бүтэцтэй байлгахын тулд хавтас үүсгэж болно.  

## Цаашид үргэлжлүүлэх

* Өргөтгөлийн хэмжээг багасгаж, ачаалах хурдыг сайжруулахын тулд [өргөтгөлөө багцлах](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)-ыг судлаарай.  
* Өргөтгөлөө VS Code өргөтгөлийн зах зээл дээр [нийтлэх](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)-ийг сураарай.  
* [Тасралтгүй интеграцчилал](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)-ыг тохируулж, бүтээн байгуулалтуудыг автоматжуулаарай.  

It seems like you might be referring to "mo" as a language, but could you please clarify what you mean by "mo"? Are you referring to a specific language, such as Māori, Mongolian, or another? Let me know so I can assist you better!