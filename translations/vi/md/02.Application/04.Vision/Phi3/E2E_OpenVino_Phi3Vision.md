Bản demo này minh họa cách sử dụng một mô hình đã được huấn luyện trước để tạo mã Python dựa trên hình ảnh và một đoạn gợi ý bằng văn bản.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Dưới đây là giải thích từng bước:

1. **Nhập và Thiết lập**:
   - Các thư viện và module cần thiết được nhập, bao gồm `requests`, `PIL` để xử lý hình ảnh, và `transformers` để xử lý mô hình và xử lý dữ liệu.

2. **Tải và Hiển thị Hình Ảnh**:
   - Một tệp hình ảnh (`demo.png`) được mở bằng thư viện `PIL` và được hiển thị.

3. **Xác Định Gợi Ý**:
   - Một thông điệp được tạo bao gồm hình ảnh và yêu cầu tạo mã Python để xử lý hình ảnh và lưu nó bằng `plt` (matplotlib).

4. **Tải Bộ Xử Lý**:
   - `AutoProcessor` được tải từ một mô hình đã được huấn luyện trước được chỉ định bởi thư mục `out_dir`. Bộ xử lý này sẽ xử lý đầu vào là văn bản và hình ảnh.

5. **Tạo Gợi Ý**:
   - Phương thức `apply_chat_template` được sử dụng để định dạng thông điệp thành một gợi ý phù hợp với mô hình.

6. **Xử Lý Dữ Liệu Đầu Vào**:
   - Gợi ý và hình ảnh được xử lý thành các tensor mà mô hình có thể hiểu.

7. **Đặt Tham Số Sinh Mã**:
   - Các tham số cho quá trình sinh mã của mô hình được định nghĩa, bao gồm số lượng token tối đa cần sinh và có sử dụng phương pháp lấy mẫu đầu ra hay không.

8. **Tạo Mã**:
   - Mô hình tạo mã Python dựa trên đầu vào và các tham số sinh. `TextStreamer` được sử dụng để xử lý đầu ra, bỏ qua gợi ý và các token đặc biệt.

9. **Kết Quả**:
   - Mã được tạo sẽ được in ra, bao gồm mã Python để xử lý hình ảnh và lưu nó như đã chỉ định trong gợi ý.

Bản demo này minh họa cách tận dụng một mô hình đã được huấn luyện trước sử dụng OpenVino để tạo mã động dựa trên đầu vào từ người dùng và hình ảnh.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.