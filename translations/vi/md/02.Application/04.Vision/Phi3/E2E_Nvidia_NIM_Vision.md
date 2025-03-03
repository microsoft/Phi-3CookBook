### Ví dụ Kịch bản

Hãy tưởng tượng bạn có một hình ảnh (`demo.png`) và bạn muốn tạo mã Python để xử lý hình ảnh này và lưu lại một phiên bản mới của nó (`phi-3-vision.jpg`).

Đoạn mã trên tự động hóa quá trình này bằng cách:

1. Thiết lập môi trường và cấu hình cần thiết.
2. Tạo một đoạn nhắc (prompt) hướng dẫn mô hình tạo mã Python cần thiết.
3. Gửi đoạn nhắc đến mô hình và thu thập mã được tạo ra.
4. Trích xuất và chạy mã đã được tạo.
5. Hiển thị hình ảnh gốc và hình ảnh đã được xử lý.

Cách tiếp cận này tận dụng sức mạnh của AI để tự động hóa các tác vụ xử lý hình ảnh, giúp bạn đạt được mục tiêu một cách dễ dàng và nhanh chóng hơn.

[Giải pháp Mã Mẫu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Hãy cùng phân tích từng bước mà toàn bộ đoạn mã thực hiện:

1. **Cài đặt Gói Cần Thiết**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Lệnh này cài đặt gói `langchain_nvidia_ai_endpoints`, đảm bảo rằng đó là phiên bản mới nhất.

2. **Nhập Các Module Cần Thiết**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Các lệnh nhập này mang vào các module cần thiết để tương tác với các điểm cuối AI của NVIDIA, xử lý mật khẩu một cách an toàn, tương tác với hệ điều hành và mã hóa/giải mã dữ liệu theo định dạng base64.

3. **Thiết Lập API Key**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Đoạn mã này kiểm tra xem biến môi trường `NVIDIA_API_KEY` đã được thiết lập chưa. Nếu chưa, nó sẽ yêu cầu người dùng nhập API key một cách an toàn.

4. **Định Nghĩa Mô Hình và Đường Dẫn Hình Ảnh**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Đoạn mã này thiết lập mô hình được sử dụng, tạo một thể hiện của `ChatNVIDIA` với mô hình đã chỉ định và định nghĩa đường dẫn đến tệp hình ảnh.

5. **Tạo Đoạn Nhắc Văn Bản**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Đoạn mã này định nghĩa một đoạn nhắc văn bản hướng dẫn mô hình tạo mã Python để xử lý hình ảnh.

6. **Mã Hóa Hình Ảnh theo Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Đoạn mã này đọc tệp hình ảnh, mã hóa nó theo base64 và tạo một thẻ hình ảnh HTML với dữ liệu đã mã hóa.

7. **Kết Hợp Văn Bản và Hình Ảnh Thành Đoạn Nhắc**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Đoạn mã này kết hợp đoạn nhắc văn bản và thẻ hình ảnh HTML thành một chuỗi duy nhất.

8. **Tạo Mã Sử Dụng ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Đoạn mã này gửi đoạn nhắc đến `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Trích Xuất Mã Python Từ Nội Dung Đã Tạo**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Đoạn mã này trích xuất mã Python thực tế từ nội dung đã tạo bằng cách loại bỏ định dạng markdown.

10. **Chạy Mã Đã Tạo**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Đoạn mã này chạy mã Python đã trích xuất dưới dạng một tiến trình con và thu thập kết quả đầu ra.

11. **Hiển Thị Hình Ảnh**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Các dòng mã này hiển thị hình ảnh bằng cách sử dụng module `IPython.display`.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.