Trong ngữ cảnh của Phi-3-mini, suy luận (inference) đề cập đến quá trình sử dụng mô hình để đưa ra dự đoán hoặc tạo đầu ra dựa trên dữ liệu đầu vào. Hãy để tôi cung cấp thêm chi tiết về Phi-3-mini và khả năng suy luận của nó.

Phi-3-mini là một phần của dòng mô hình Phi-3 do Microsoft phát hành. Các mô hình này được thiết kế để định nghĩa lại những gì có thể với Mô hình Ngôn ngữ Nhỏ (SLM).

Dưới đây là một số điểm chính về Phi-3-mini và khả năng suy luận của nó:

## **Tổng quan về Phi-3-mini:**
- Phi-3-mini có kích thước tham số là 3.8 tỷ.
- Nó có thể chạy không chỉ trên các thiết bị máy tính truyền thống mà còn trên các thiết bị biên như thiết bị di động và thiết bị IoT.
- Việc phát hành Phi-3-mini cho phép cá nhân và doanh nghiệp triển khai SLM trên các thiết bị phần cứng khác nhau, đặc biệt trong các môi trường có tài nguyên hạn chế.
- Nó hỗ trợ nhiều định dạng mô hình, bao gồm định dạng PyTorch truyền thống, phiên bản lượng tử hóa của định dạng gguf, và phiên bản lượng tử hóa dựa trên ONNX.

## **Truy cập Phi-3-mini:**
Để truy cập Phi-3-mini, bạn có thể sử dụng [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) trong một ứng dụng Copilot. Semantic Kernel tương thích với Azure OpenAI Service, các mô hình mã nguồn mở trên Hugging Face, và các mô hình cục bộ.  
Bạn cũng có thể sử dụng [Ollama](https://ollama.com) hoặc [LlamaEdge](https://llamaedge.com) để gọi các mô hình đã được lượng tử hóa. Ollama cho phép người dùng cá nhân gọi các mô hình lượng tử hóa khác nhau, trong khi LlamaEdge cung cấp khả năng hoạt động đa nền tảng cho các mô hình GGUF.

## **Mô hình lượng tử hóa:**
Nhiều người dùng thích sử dụng các mô hình lượng tử hóa để suy luận cục bộ. Ví dụ, bạn có thể chạy trực tiếp lệnh Ollama run Phi-3 hoặc cấu hình nó ngoại tuyến bằng Modelfile. Modelfile xác định đường dẫn tệp GGUF và định dạng prompt.

## **Khả năng AI sinh tạo:**
Kết hợp các SLM như Phi-3-mini mở ra những khả năng mới cho AI sinh tạo. Suy luận chỉ là bước đầu tiên; các mô hình này có thể được sử dụng cho nhiều tác vụ trong các tình huống hạn chế tài nguyên, yêu cầu độ trễ thấp, và chi phí hạn chế.

## **Khám phá AI sinh tạo với Phi-3-mini: Hướng dẫn suy luận và triển khai**
Tìm hiểu cách sử dụng Semantic Kernel, Ollama/LlamaEdge, và ONNX Runtime để truy cập và suy luận các mô hình Phi-3-mini, đồng thời khám phá các khả năng của AI sinh tạo trong nhiều tình huống ứng dụng khác nhau.

**Tính năng**  
Suy luận mô hình phi3-mini trong:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Tóm lại, Phi-3-mini cho phép các nhà phát triển khám phá các định dạng mô hình khác nhau và tận dụng AI sinh tạo trong nhiều tình huống ứng dụng.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.