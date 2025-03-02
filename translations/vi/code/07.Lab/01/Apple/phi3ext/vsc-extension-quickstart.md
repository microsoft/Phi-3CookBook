# Chào mừng bạn đến với tiện ích mở rộng VS Code của mình

## Có gì trong thư mục này

* Thư mục này chứa tất cả các tệp cần thiết cho tiện ích mở rộng của bạn.
* `package.json` - đây là tệp manifest, nơi bạn khai báo tiện ích mở rộng và lệnh của mình.
  * Plugin mẫu đăng ký một lệnh và định nghĩa tiêu đề cũng như tên lệnh của nó. Với thông tin này, VS Code có thể hiển thị lệnh trong bảng lệnh. Hiện tại, nó chưa cần tải plugin.
* `src/extension.ts` - đây là tệp chính nơi bạn sẽ triển khai lệnh của mình.
  * Tệp này xuất một hàm, `activate`, được gọi lần đầu tiên khi tiện ích mở rộng của bạn được kích hoạt (trong trường hợp này là khi thực thi lệnh). Bên trong hàm `activate`, chúng ta gọi `registerCommand`.
  * Chúng ta truyền hàm chứa việc triển khai lệnh làm tham số thứ hai cho `registerCommand`.

## Thiết lập

* Cài đặt các tiện ích mở rộng được đề xuất (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner và dbaeumer.vscode-eslint).

## Bắt đầu và chạy ngay

* Nhấn `F5` để mở một cửa sổ mới với tiện ích mở rộng của bạn được tải.
* Chạy lệnh của bạn từ bảng lệnh bằng cách nhấn (`Ctrl+Shift+P` hoặc `Cmd+Shift+P` trên Mac) và nhập `Hello World`.
* Đặt các điểm dừng (breakpoints) trong mã của bạn bên trong `src/extension.ts` để gỡ lỗi tiện ích mở rộng của bạn.
* Tìm đầu ra từ tiện ích mở rộng của bạn trong bảng điều khiển gỡ lỗi.

## Thực hiện thay đổi

* Bạn có thể khởi động lại tiện ích mở rộng từ thanh công cụ gỡ lỗi sau khi thay đổi mã trong `src/extension.ts`.
* Bạn cũng có thể tải lại (`Ctrl+R` hoặc `Cmd+R` trên Mac) cửa sổ VS Code với tiện ích mở rộng của mình để áp dụng các thay đổi.

## Khám phá API

* Bạn có thể mở toàn bộ bộ API của chúng tôi khi mở tệp `node_modules/@types/vscode/index.d.ts`.

## Chạy kiểm thử

* Cài đặt [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Chạy tác vụ "watch" thông qua lệnh **Tasks: Run Task**. Đảm bảo tác vụ này đang chạy, nếu không các bài kiểm tra có thể không được phát hiện.
* Mở chế độ Testing từ thanh hoạt động và nhấp vào nút "Run Test", hoặc sử dụng phím tắt `Ctrl/Cmd + ; A`.
* Xem kết quả kiểm thử trong chế độ xem Test Results.
* Thực hiện thay đổi trong `src/test/extension.test.ts` hoặc tạo các tệp kiểm thử mới bên trong thư mục `test`.
  * Bộ chạy kiểm thử được cung cấp chỉ xem xét các tệp có mẫu tên `**.test.ts`.
  * Bạn có thể tạo các thư mục bên trong thư mục `test` để cấu trúc các kiểm thử theo ý muốn.

## Đi xa hơn

* Giảm kích thước tiện ích mở rộng và cải thiện thời gian khởi động bằng cách [gói tiện ích mở rộng của bạn](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Xuất bản tiện ích mở rộng của bạn](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) trên chợ tiện ích mở rộng VS Code.
* Tự động hóa các bản dựng bằng cách thiết lập [Tích hợp liên tục](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.