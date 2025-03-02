# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo giới thiệu WebGPU và mô hình RAG Pattern

Mô hình RAG Pattern với Phi-3.5 Onnx Hosted sử dụng phương pháp Tạo sinh được tăng cường bởi truy xuất (Retrieval-Augmented Generation), kết hợp sức mạnh của các mô hình Phi-3.5 với ONNX hosting để triển khai AI hiệu quả. Mô hình này đóng vai trò quan trọng trong việc tinh chỉnh các mô hình cho các nhiệm vụ cụ thể theo từng lĩnh vực, mang lại sự kết hợp giữa chất lượng, hiệu quả chi phí và khả năng hiểu ngữ cảnh dài. Đây là một phần của bộ Azure AI, cung cấp một loạt các mô hình dễ dàng tìm kiếm, thử nghiệm và sử dụng, đáp ứng nhu cầu tùy chỉnh của nhiều ngành công nghiệp.

## WebGPU là gì
WebGPU là một API đồ họa web hiện đại được thiết kế để cung cấp quyền truy cập hiệu quả vào bộ xử lý đồ họa (GPU) của thiết bị trực tiếp từ các trình duyệt web. Nó được dự kiến sẽ thay thế WebGL, với nhiều cải tiến chính:

1. **Tương thích với GPU hiện đại**: WebGPU được xây dựng để hoạt động mượt mà với các kiến trúc GPU hiện đại, sử dụng các API hệ thống như Vulkan, Metal và Direct3D 12.
2. **Hiệu suất cải thiện**: Hỗ trợ các tính toán GPU đa dụng và các thao tác nhanh hơn, phù hợp cho cả việc dựng hình đồ họa và các nhiệm vụ học máy.
3. **Tính năng nâng cao**: WebGPU cung cấp quyền truy cập vào các khả năng GPU tiên tiến hơn, cho phép thực hiện các tác vụ đồ họa và tính toán phức tạp, linh hoạt hơn.
4. **Giảm tải cho JavaScript**: Bằng cách chuyển nhiều tác vụ hơn sang GPU, WebGPU giảm đáng kể khối lượng công việc trên JavaScript, mang lại hiệu suất tốt hơn và trải nghiệm mượt mà hơn.

Hiện tại, WebGPU được hỗ trợ trên các trình duyệt như Google Chrome, với các nỗ lực đang được tiến hành để mở rộng hỗ trợ trên các nền tảng khác.

### 03.WebGPU
Môi trường yêu cầu:

**Các trình duyệt được hỗ trợ:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Kích hoạt WebGPU:

- Trên Chrome/Microsoft Edge 

Kích hoạt cờ `chrome://flags/#enable-unsafe-webgpu`.

#### Mở trình duyệt:
Khởi chạy Google Chrome hoặc Microsoft Edge.

#### Truy cập trang Flags:
Trong thanh địa chỉ, gõ `chrome://flags` và nhấn Enter.

#### Tìm cờ:
Trong hộp tìm kiếm ở đầu trang, gõ 'enable-unsafe-webgpu'.

#### Kích hoạt cờ:
Tìm cờ #enable-unsafe-webgpu trong danh sách kết quả.

Nhấp vào menu thả xuống bên cạnh nó và chọn Enabled.

#### Khởi động lại trình duyệt:

Sau khi kích hoạt cờ, bạn cần khởi động lại trình duyệt để thay đổi có hiệu lực. Nhấp vào nút Relaunch xuất hiện ở cuối trang.

- Đối với Linux, khởi chạy trình duyệt với `--enable-features=Vulkan`.
- Safari 18 (macOS 15) đã bật WebGPU theo mặc định.
- Trên Firefox Nightly, nhập about:config vào thanh địa chỉ và `set dom.webgpu.enabled to true`.

### Cài đặt GPU cho Microsoft Edge 

Dưới đây là các bước để cài đặt GPU hiệu suất cao cho Microsoft Edge trên Windows:

- **Mở Cài đặt:** Nhấp vào menu Start và chọn Settings.
- **Cài đặt Hệ thống:** Đi tới System và sau đó là Display.
- **Cài đặt Đồ họa:** Cuộn xuống và nhấp vào Graphics settings.
- **Chọn Ứng dụng:** Dưới mục “Choose an app to set preference,” chọn Desktop app và sau đó nhấn Browse.
- **Chọn Edge:** Điều hướng đến thư mục cài đặt Edge (thường là `C:\Program Files (x86)\Microsoft\Edge\Application`) và chọn `msedge.exe`.
- **Cài đặt Ưu tiên:** Nhấp vào Options, chọn High performance, và sau đó nhấn Save.
Điều này sẽ đảm bảo rằng Microsoft Edge sử dụng GPU hiệu suất cao của bạn để mang lại hiệu suất tốt hơn.
- **Khởi động lại** máy tính của bạn để các cài đặt này có hiệu lực.

### Mẫu: Vui lòng [nhấn vào đây](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.