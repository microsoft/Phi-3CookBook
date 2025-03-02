Phi-3-mini WebGPU RAG Chatbot

## Demo giới thiệu WebGPU và Mô hình RAG
Mô hình RAG với Phi-3 Onnx Hosted tận dụng phương pháp Retrieval-Augmented Generation, kết hợp sức mạnh của các mô hình Phi-3 với hosting ONNX để triển khai AI hiệu quả. Mô hình này đóng vai trò quan trọng trong việc tinh chỉnh các mô hình cho các nhiệm vụ cụ thể theo ngành, mang lại sự kết hợp giữa chất lượng, chi phí hợp lý và khả năng hiểu ngữ cảnh dài. Đây là một phần trong bộ Azure AI, cung cấp một loạt các mô hình dễ tìm, thử nghiệm và sử dụng, đáp ứng nhu cầu tùy chỉnh của nhiều ngành công nghiệp. Các mô hình Phi-3, bao gồm Phi-3-mini, Phi-3-small và Phi-3-medium, có sẵn trên Azure AI Model Catalog và có thể được tinh chỉnh và triển khai tự quản lý hoặc qua các nền tảng như HuggingFace và ONNX, thể hiện cam kết của Microsoft trong việc cung cấp các giải pháp AI dễ tiếp cận và hiệu quả.

## WebGPU là gì?
WebGPU là một API đồ họa web hiện đại được thiết kế để cung cấp truy cập hiệu quả vào đơn vị xử lý đồ họa (GPU) của thiết bị trực tiếp từ trình duyệt web. Đây là sự kế thừa của WebGL, mang lại một số cải tiến chính:

1. **Tương thích với GPU hiện đại**: WebGPU được xây dựng để hoạt động liền mạch với các kiến trúc GPU hiện đại, tận dụng các API hệ thống như Vulkan, Metal và Direct3D 12.
2. **Hiệu suất nâng cao**: Hỗ trợ các tính toán GPU đa mục đích và hoạt động nhanh hơn, phù hợp cho cả kết xuất đồ họa và các tác vụ học máy.
3. **Tính năng nâng cao**: WebGPU cung cấp quyền truy cập vào các khả năng GPU tiên tiến hơn, cho phép thực hiện các tác vụ đồ họa và tính toán phức tạp hơn.
4. **Giảm tải cho JavaScript**: Bằng cách chuyển nhiều tác vụ sang GPU, WebGPU giảm đáng kể tải công việc cho JavaScript, mang lại hiệu suất tốt hơn và trải nghiệm mượt mà hơn.

Hiện tại, WebGPU được hỗ trợ trên các trình duyệt như Google Chrome, với công việc đang được tiếp tục để mở rộng hỗ trợ sang các nền tảng khác.

### 03.WebGPU
Môi trường yêu cầu:

**Trình duyệt được hỗ trợ:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Kích hoạt WebGPU:

- Trong Chrome/Microsoft Edge 

Kích hoạt cờ `chrome://flags/#enable-unsafe-webgpu`.

#### Mở Trình Duyệt của Bạn:
Khởi chạy Google Chrome hoặc Microsoft Edge.

#### Truy cập Trang Flags:
Trong thanh địa chỉ, nhập `chrome://flags` và nhấn Enter.

#### Tìm kiếm Cờ:
Trong hộp tìm kiếm ở đầu trang, nhập 'enable-unsafe-webgpu'.

#### Kích hoạt Cờ:
Tìm cờ #enable-unsafe-webgpu trong danh sách kết quả.

Nhấp vào menu thả xuống bên cạnh nó và chọn Enabled.

#### Khởi động lại Trình Duyệt:

Sau khi kích hoạt cờ, bạn sẽ cần khởi động lại trình duyệt để các thay đổi có hiệu lực. Nhấp vào nút Relaunch xuất hiện ở cuối trang.

- Đối với Linux, khởi chạy trình duyệt với `--enable-features=Vulkan`.
- Safari 18 (macOS 15) đã kích hoạt WebGPU mặc định.
- Trong Firefox Nightly, nhập about:config vào thanh địa chỉ và `set dom.webgpu.enabled to true`.

### Cài đặt GPU cho Microsoft Edge 

Dưới đây là các bước để cài đặt GPU hiệu suất cao cho Microsoft Edge trên Windows:

- **Mở Cài Đặt:** Nhấp vào menu Start và chọn Cài đặt.
- **Cài Đặt Hệ Thống:** Đi tới Hệ thống, sau đó chọn Màn hình.
- **Cài Đặt Đồ Họa:** Cuộn xuống và nhấp vào Cài đặt đồ họa.
- **Chọn Ứng Dụng:** Dưới mục “Chọn ứng dụng để đặt ưu tiên,” chọn Ứng dụng máy tính để bàn và sau đó Duyệt.
- **Chọn Edge:** Điều hướng đến thư mục cài đặt Edge (thường là `C:\Program Files (x86)\Microsoft\Edge\Application`) và chọn `msedge.exe`.
- **Đặt Ưu Tiên:** Nhấp vào Tùy chọn, chọn Hiệu suất cao, và sau đó nhấp Lưu.
Điều này sẽ đảm bảo rằng Microsoft Edge sử dụng GPU hiệu suất cao của bạn để có hiệu suất tốt hơn.
- **Khởi động lại** máy để các cài đặt này có hiệu lực.

### Mở Codespace của Bạn:
Điều hướng đến repository của bạn trên GitHub.
Nhấp vào nút Code và chọn Mở với Codespaces.

Nếu bạn chưa có Codespace, bạn có thể tạo một cái bằng cách nhấp vào Codespace mới.

**Lưu ý** Cài đặt môi trường Node trong Codespace của bạn
Chạy một demo npm từ GitHub Codespace là một cách tuyệt vời để kiểm tra và phát triển dự án của bạn. Dưới đây là hướng dẫn từng bước để giúp bạn bắt đầu:

### Cài Đặt Môi Trường:
Khi Codespace của bạn được mở, đảm bảo rằng bạn đã cài đặt Node.js và npm. Bạn có thể kiểm tra bằng cách chạy:
```
node -v
```
```
npm -v
```

Nếu chúng chưa được cài đặt, bạn có thể cài đặt bằng cách chạy:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Điều Hướng Đến Thư Mục Dự Án:
Sử dụng terminal để điều hướng đến thư mục nơi dự án npm của bạn được đặt:
```
cd path/to/your/project
```

### Cài Đặt Các Phụ Thuộc:
Chạy lệnh sau để cài đặt tất cả các phụ thuộc cần thiết được liệt kê trong tệp package.json của bạn:

```
npm install
```

### Chạy Demo:
Sau khi các phụ thuộc được cài đặt, bạn có thể chạy script demo của mình. Thông thường, script này được chỉ định trong phần scripts của tệp package.json. Ví dụ, nếu script demo của bạn có tên là start, bạn có thể chạy:

```
npm run build
```
```
npm run dev
```

### Truy Cập Demo:
Nếu demo của bạn liên quan đến một máy chủ web, Codespaces sẽ cung cấp một URL để truy cập nó. Hãy tìm thông báo hoặc kiểm tra tab Ports để tìm URL.

**Lưu ý:** Mô hình cần được lưu trong bộ nhớ cache của trình duyệt, vì vậy có thể mất một chút thời gian để tải.

### Demo RAG
Tải lên tệp markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Chọn Tệp của Bạn:
Nhấp vào nút có nội dung “Chọn Tệp” để chọn tài liệu bạn muốn tải lên.

### Tải Lên Tài Liệu:
Sau khi chọn tệp của bạn, nhấp vào nút “Tải Lên” để tải tài liệu của bạn cho RAG (Retrieval-Augmented Generation).

### Bắt Đầu Cuộc Trò Chuyện:
Khi tài liệu đã được tải lên, bạn có thể bắt đầu một phiên trò chuyện sử dụng RAG dựa trên nội dung của tài liệu.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.