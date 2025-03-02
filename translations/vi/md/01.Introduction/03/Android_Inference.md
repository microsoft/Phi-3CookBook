# **Suy luận Phi-3 trên Android**

Hãy cùng khám phá cách bạn có thể thực hiện suy luận với Phi-3-mini trên các thiết bị Android. Phi-3-mini là một dòng mô hình mới từ Microsoft, cho phép triển khai các Mô hình Ngôn ngữ Lớn (LLMs) trên các thiết bị biên và thiết bị IoT.

## Semantic Kernel và Suy luận

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) là một khung ứng dụng giúp bạn tạo các ứng dụng tương thích với Azure OpenAI Service, các mô hình OpenAI, và thậm chí cả các mô hình cục bộ. Nếu bạn mới làm quen với Semantic Kernel, chúng tôi khuyên bạn nên tham khảo [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Truy cập Phi-3-mini bằng Semantic Kernel

Bạn có thể kết hợp nó với Hugging Face Connector trong Semantic Kernel. Tham khảo [Mẫu mã](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Theo mặc định, nó tương ứng với ID mô hình trên Hugging Face. Tuy nhiên, bạn cũng có thể kết nối với một máy chủ mô hình Phi-3-mini được xây dựng cục bộ.

### Gọi các Mô hình Đã Lượng tử hóa với Ollama hoặc LlamaEdge

Nhiều người dùng thích sử dụng các mô hình đã lượng tử hóa để chạy mô hình cục bộ. [Ollama](https://ollama.com/) và [LlamaEdge](https://llamaedge.com) cho phép người dùng cá nhân gọi các mô hình đã lượng tử hóa khác nhau:

#### Ollama

Bạn có thể chạy trực tiếp `ollama run Phi-3` hoặc cấu hình ngoại tuyến bằng cách tạo một `Modelfile` với đường dẫn đến tệp `.gguf` của bạn.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Mẫu mã](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Nếu bạn muốn sử dụng các tệp `.gguf` trên đám mây và trên các thiết bị biên đồng thời, LlamaEdge là một lựa chọn tuyệt vời. Bạn có thể tham khảo [mẫu mã](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) để bắt đầu.

### Cài đặt và Chạy trên Điện thoại Android

1. **Tải ứng dụng MLC Chat** (Miễn phí) cho điện thoại Android.  
2. Tải tệp APK (148MB) và cài đặt trên thiết bị của bạn.  
3. Khởi chạy ứng dụng MLC Chat. Bạn sẽ thấy danh sách các mô hình AI, bao gồm Phi-3-mini.

Tóm lại, Phi-3-mini mở ra những khả năng thú vị cho AI tạo sinh trên các thiết bị biên, và bạn có thể bắt đầu khám phá các tính năng của nó trên Android.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.