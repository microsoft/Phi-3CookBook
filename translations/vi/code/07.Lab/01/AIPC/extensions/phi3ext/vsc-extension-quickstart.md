# Chào mừng bạn đến với tiện ích mở rộng VS Code của mình

## Những gì có trong thư mục này

* Thư mục này chứa tất cả các tệp cần thiết cho tiện ích mở rộng của bạn.
* `package.json` - đây là tệp manifest, nơi bạn khai báo tiện ích mở rộng và lệnh của mình.
  * Plugin mẫu đăng ký một lệnh và định nghĩa tiêu đề cũng như tên lệnh. Với thông tin này, VS Code có thể hiển thị lệnh trong bảng lệnh. Nó chưa cần tải plugin.
* `src/extension.ts` - đây là tệp chính nơi bạn sẽ cung cấp triển khai cho lệnh của mình.
  * Tệp này xuất một hàm, `activate`, được gọi lần đầu tiên khi tiện ích mở rộng của bạn được kích hoạt (trong trường hợp này là bằng cách thực thi lệnh). Bên trong hàm `activate`, chúng ta gọi `registerCommand`.
  * Chúng ta truyền hàm chứa triển khai của lệnh làm tham số thứ hai cho `registerCommand`.

## Thiết lập

* Cài đặt các tiện ích mở rộng được khuyến nghị (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, và dbaeumer.vscode-eslint).

## Bắt đầu ngay lập tức

* Nhấn `F5` để mở một cửa sổ mới với tiện ích mở rộng của bạn đã được tải.
* Chạy lệnh của bạn từ bảng lệnh bằng cách nhấn (`Ctrl+Shift+P` hoặc `Cmd+Shift+P` trên Mac) và nhập `Hello World`.
* Đặt các điểm ngắt (breakpoint) trong mã của bạn bên trong `src/extension.ts` để gỡ lỗi tiện ích mở rộng của bạn.
* Tìm đầu ra từ tiện ích mở rộng của bạn trong bảng điều khiển gỡ lỗi.

## Thực hiện thay đổi

* Bạn có thể khởi động lại tiện ích mở rộng từ thanh công cụ gỡ lỗi sau khi thay đổi mã trong `src/extension.ts`.
* Bạn cũng có thể tải lại (`Ctrl+R` hoặc `Cmd+R` trên Mac) cửa sổ VS Code với tiện ích mở rộng của mình để tải các thay đổi.

## Khám phá API

* Bạn có thể mở toàn bộ bộ API của chúng tôi khi mở tệp `node_modules/@types/vscode/index.d.ts`.

## Chạy thử nghiệm

* Cài đặt [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Chạy tác vụ "watch" thông qua lệnh **Tasks: Run Task**. Đảm bảo rằng tác vụ này đang chạy, nếu không các thử nghiệm có thể không được phát hiện.
* Mở chế độ xem Testing từ thanh hoạt động và nhấp vào nút "Run Test", hoặc sử dụng phím tắt `Ctrl/Cmd + ; A`.
* Xem kết quả thử nghiệm trong chế độ xem Test Results.
* Thực hiện thay đổi đối với `src/test/extension.test.ts` hoặc tạo các tệp thử nghiệm mới bên trong thư mục `test`.
  * Trình chạy thử nghiệm được cung cấp chỉ xem xét các tệp khớp với mẫu tên `**.test.ts`.
  * Bạn có thể tạo các thư mục bên trong thư mục `test` để tổ chức các thử nghiệm theo cách bạn muốn.

## Đi xa hơn

* Giảm kích thước tiện ích mở rộng và cải thiện thời gian khởi động bằng cách [đóng gói tiện ích mở rộng của bạn](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Xuất bản tiện ích mở rộng của bạn](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) trên chợ tiện ích mở rộng của VS Code.
* Tự động hóa quá trình xây dựng bằng cách thiết lập [Tích hợp liên tục](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.