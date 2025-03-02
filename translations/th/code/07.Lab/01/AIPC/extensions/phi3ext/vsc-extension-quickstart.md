# ยินดีต้อนรับสู่ส่วนขยาย VS Code ของคุณ

## มีอะไรอยู่ในโฟลเดอร์นี้บ้าง

* โฟลเดอร์นี้มีไฟล์ทั้งหมดที่จำเป็นสำหรับส่วนขยายของคุณ
* `package.json` - ไฟล์ manifest ที่คุณใช้ประกาศส่วนขยายและคำสั่งของคุณ
  * ปลั๊กอินตัวอย่างจะลงทะเบียนคำสั่งและกำหนดชื่อและชื่อคำสั่ง ด้วยข้อมูลนี้ VS Code จะแสดงคำสั่งใน command palette โดยยังไม่จำเป็นต้องโหลดปลั๊กอิน
* `src/extension.ts` - ไฟล์หลักที่คุณจะใช้สำหรับการเขียนคำสั่งของคุณ
  * ไฟล์นี้จะ export ฟังก์ชันหนึ่งชื่อ `activate` ซึ่งจะถูกเรียกใช้เมื่อส่วนขยายของคุณถูกเปิดใช้งานครั้งแรก (ในกรณีนี้คือเมื่อรันคำสั่ง) ภายในฟังก์ชัน `activate` เราเรียก `registerCommand`
  * เราส่งฟังก์ชันที่มีการเขียนคำสั่งเป็นพารามิเตอร์ที่สองให้กับ `registerCommand`

## การตั้งค่า

* ติดตั้งส่วนขยายที่แนะนำ (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, และ dbaeumer.vscode-eslint)

## เริ่มต้นใช้งานทันที

* กด `F5` เพื่อเปิดหน้าต่างใหม่พร้อมโหลดส่วนขยายของคุณ
* รันคำสั่งของคุณจาก command palette โดยกด (`Ctrl+Shift+P` หรือ `Cmd+Shift+P` บน Mac) และพิมพ์ `Hello World`
* ตั้ง breakpoints ในโค้ดของคุณภายใน `src/extension.ts` เพื่อดีบักส่วนขยายของคุณ
* ดูผลลัพธ์จากส่วนขยายของคุณใน debug console

## การเปลี่ยนแปลง

* คุณสามารถ relaunch ส่วนขยายได้จาก debug toolbar หลังจากแก้ไขโค้ดใน `src/extension.ts`
* คุณยังสามารถ reload (`Ctrl+R` หรือ `Cmd+R` บน Mac) หน้าต่าง VS Code พร้อมส่วนขยายของคุณเพื่อโหลดการเปลี่ยนแปลง

## สำรวจ API

* คุณสามารถเปิดดู API ทั้งหมดได้เมื่อคุณเปิดไฟล์ `node_modules/@types/vscode/index.d.ts`

## รันการทดสอบ

* ติดตั้ง [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* รันงาน "watch" ผ่านคำสั่ง **Tasks: Run Task** ตรวจสอบให้แน่ใจว่างานนี้กำลังทำงาน มิฉะนั้นอาจไม่พบการทดสอบ
* เปิดมุมมอง Testing จาก activity bar และคลิกปุ่ม "Run Test" หรือใช้คีย์ลัด `Ctrl/Cmd + ; A`
* ดูผลลัพธ์ของการทดสอบใน Test Results view
* แก้ไข `src/test/extension.test.ts` หรือสร้างไฟล์ทดสอบใหม่ในโฟลเดอร์ `test`
  * ตัวทดสอบที่ให้มาจะพิจารณาเฉพาะไฟล์ที่ตรงกับรูปแบบชื่อ `**.test.ts`
  * คุณสามารถสร้างโฟลเดอร์ภายในโฟลเดอร์ `test` เพื่อจัดระเบียบการทดสอบในแบบที่คุณต้องการ

## ทำสิ่งเพิ่มเติม

* ลดขนาดส่วนขยายและปรับปรุงเวลาเริ่มต้นด้วยการ [bundling ส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)
* [เผยแพร่ส่วนขยายของคุณ](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) บน VS Code extension marketplace
* ทำให้การสร้างอัตโนมัติโดยการตั้งค่า [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์โดยผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้