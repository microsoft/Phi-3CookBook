# Chào mừng bạn đến với Tiện ích mở rộng VS Code của mình

## Những gì có trong thư mục này

* Thư mục này chứa tất cả các tệp cần thiết cho tiện ích mở rộng của bạn.
* `package.json` - đây là tệp manifest nơi bạn khai báo tiện ích mở rộng và lệnh của mình.
  * Plugin mẫu đăng ký một lệnh và định nghĩa tiêu đề cũng như tên lệnh của nó. Với thông tin này, VS Code có thể hiển thị lệnh trong bảng lệnh. Nó chưa cần tải plugin.
* `src/extension.ts` - đây là tệp chính nơi bạn sẽ triển khai lệnh của mình.
  * Tệp xuất ra một hàm, `activate`, được gọi ngay lần đầu tiên tiện ích mở rộng của bạn được kích hoạt (trong trường hợp này là khi thực thi lệnh). Bên trong hàm `activate`, chúng ta gọi `registerCommand`.
  * Chúng ta truyền hàm chứa phần triển khai của lệnh làm tham số thứ hai cho `registerCommand`.

## Thiết lập

* Cài đặt các tiện ích mở rộng được khuyến nghị (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, và dbaeumer.vscode-eslint).

## Bắt đầu và chạy ngay lập tức

* Nhấn `F5` để mở một cửa sổ mới với tiện ích mở rộng của bạn đã được tải.
* Chạy lệnh của bạn từ bảng lệnh bằng cách nhấn (`Ctrl+Shift+P` hoặc `Cmd+Shift+P` trên Mac) và gõ `Hello World`.
* Đặt điểm dừng trong mã của bạn bên trong `src/extension.ts` để gỡ lỗi tiện ích mở rộng của bạn.
* Tìm đầu ra từ tiện ích mở rộng của bạn trong bảng điều khiển gỡ lỗi.

## Thực hiện thay đổi

* Bạn có thể khởi động lại tiện ích mở rộng từ thanh công cụ gỡ lỗi sau khi thay đổi mã trong `src/extension.ts`.
* Bạn cũng có thể tải lại (`Ctrl+R` hoặc `Cmd+R` trên Mac) cửa sổ VS Code với tiện ích mở rộng của bạn để tải các thay đổi.

## Khám phá API

* Bạn có thể mở toàn bộ bộ API của chúng tôi khi bạn mở tệp `node_modules/@types/vscode/index.d.ts`.

## Chạy kiểm tra

* Cài đặt [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Chạy tác vụ "watch" thông qua lệnh **Tasks: Run Task**. Đảm bảo rằng tác vụ này đang chạy, nếu không các bài kiểm tra có thể không được phát hiện.
* Mở tab Testing từ thanh hoạt động và nhấp vào nút "Run Test", hoặc sử dụng phím tắt `Ctrl/Cmd + ; A`.
* Xem kết quả kiểm tra trong tab Test Results.
* Thực hiện thay đổi trong `src/test/extension.test.ts` hoặc tạo các tệp kiểm tra mới trong thư mục `test`.
  * Trình kiểm tra được cung cấp sẽ chỉ xem xét các tệp khớp với mẫu tên `**.test.ts`.
  * Bạn có thể tạo các thư mục bên trong thư mục `test` để cấu trúc các bài kiểm tra của mình theo cách bạn muốn.

## Đi xa hơn

* Giảm kích thước tiện ích mở rộng và cải thiện thời gian khởi động bằng cách [đóng gói tiện ích mở rộng của bạn](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Xuất bản tiện ích mở rộng của bạn](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) trên thị trường tiện ích mở rộng VS Code.
* Tự động hóa quy trình xây dựng bằng cách thiết lập [Tích hợp liên tục](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.