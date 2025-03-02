# **Định lượng Phi Family**

Định lượng mô hình (Model quantization) là quá trình ánh xạ các tham số (như trọng số và giá trị kích hoạt) trong một mô hình mạng nơ-ron từ một phạm vi giá trị lớn (thường là giá trị liên tục) sang một phạm vi giá trị nhỏ hơn và hữu hạn. Công nghệ này giúp giảm kích thước và độ phức tạp tính toán của mô hình, cải thiện hiệu suất hoạt động của mô hình trong các môi trường bị giới hạn tài nguyên, như thiết bị di động hoặc hệ thống nhúng. Định lượng mô hình đạt được sự nén bằng cách giảm độ chính xác của các tham số, nhưng điều này cũng gây ra một mức độ mất mát độ chính xác nhất định. Vì vậy, trong quá trình định lượng, cần cân bằng giữa kích thước mô hình, độ phức tạp tính toán và độ chính xác. Các phương pháp định lượng phổ biến bao gồm định lượng số nguyên cố định (fixed-point quantization), định lượng số thực (floating-point quantization), v.v. Bạn có thể chọn chiến lược định lượng phù hợp tùy theo tình huống cụ thể và nhu cầu.

Chúng tôi hy vọng triển khai mô hình GenAI trên các thiết bị biên và cho phép nhiều thiết bị tham gia vào các kịch bản GenAI hơn, như thiết bị di động, AI PC/Copilot+PC, và các thiết bị IoT truyền thống. Thông qua mô hình định lượng, chúng tôi có thể triển khai mô hình trên các thiết bị biên khác nhau dựa trên đặc điểm của từng thiết bị. Kết hợp với khung tăng tốc mô hình và mô hình định lượng do các nhà sản xuất phần cứng cung cấp, chúng tôi có thể xây dựng các kịch bản ứng dụng SLM tốt hơn.

Trong kịch bản định lượng, chúng tôi có các mức độ chính xác khác nhau (INT4, INT8, FP16, FP32). Dưới đây là giải thích về các mức độ chính xác định lượng thường được sử dụng.

### **INT4**

Định lượng INT4 là một phương pháp định lượng triệt để, trong đó các trọng số và giá trị kích hoạt của mô hình được định lượng thành số nguyên 4 bit. Định lượng INT4 thường dẫn đến mất mát độ chính xác lớn hơn do phạm vi biểu diễn nhỏ hơn và độ chính xác thấp hơn. Tuy nhiên, so với định lượng INT8, định lượng INT4 có thể giảm thêm yêu cầu lưu trữ và độ phức tạp tính toán của mô hình. Cần lưu ý rằng định lượng INT4 khá hiếm trong thực tế, vì độ chính xác quá thấp có thể gây suy giảm hiệu suất mô hình đáng kể. Ngoài ra, không phải tất cả phần cứng đều hỗ trợ các phép toán INT4, do đó cần cân nhắc khả năng tương thích phần cứng khi chọn phương pháp định lượng.

### **INT8**

Định lượng INT8 là quá trình chuyển đổi trọng số và giá trị kích hoạt của mô hình từ số thực sang số nguyên 8 bit. Mặc dù phạm vi số học được biểu diễn bởi số nguyên INT8 nhỏ hơn và ít chính xác hơn, nhưng nó có thể giảm đáng kể yêu cầu lưu trữ và tính toán. Trong định lượng INT8, các trọng số và giá trị kích hoạt của mô hình trải qua quá trình định lượng, bao gồm việc chia tỷ lệ (scaling) và dịch chuyển (offset), để giữ lại thông tin số thực ban đầu càng nhiều càng tốt. Trong quá trình suy luận, các giá trị đã định lượng này sẽ được khử định lượng (dequantized) trở lại số thực để tính toán, sau đó lại được định lượng trở lại INT8 cho bước tiếp theo. Phương pháp này có thể cung cấp độ chính xác đủ cho hầu hết các ứng dụng đồng thời duy trì hiệu suất tính toán cao.

### **FP16**

Định dạng FP16, tức là số thực 16 bit (float16), giúp giảm một nửa dung lượng bộ nhớ so với số thực 32 bit (float32), mang lại lợi thế đáng kể trong các ứng dụng học sâu quy mô lớn. Định dạng FP16 cho phép tải các mô hình lớn hơn hoặc xử lý nhiều dữ liệu hơn trong cùng giới hạn bộ nhớ GPU. Khi phần cứng GPU hiện đại ngày càng hỗ trợ các phép toán FP16, việc sử dụng định dạng FP16 cũng có thể mang lại cải thiện về tốc độ tính toán. Tuy nhiên, định dạng FP16 cũng có những nhược điểm cố hữu, cụ thể là độ chính xác thấp hơn, có thể dẫn đến sự bất ổn số học hoặc mất mát độ chính xác trong một số trường hợp.

### **FP32**

Định dạng FP32 cung cấp độ chính xác cao hơn và có thể biểu diễn chính xác một phạm vi giá trị rộng. Trong các kịch bản yêu cầu thực hiện các phép toán toán học phức tạp hoặc cần kết quả có độ chính xác cao, định dạng FP32 được ưu tiên sử dụng. Tuy nhiên, độ chính xác cao cũng đồng nghĩa với việc sử dụng nhiều bộ nhớ hơn và thời gian tính toán dài hơn. Đối với các mô hình học sâu quy mô lớn, đặc biệt khi có nhiều tham số mô hình và lượng dữ liệu lớn, định dạng FP32 có thể gây ra tình trạng thiếu bộ nhớ GPU hoặc giảm tốc độ suy luận.

Trên các thiết bị di động hoặc thiết bị IoT, chúng ta có thể chuyển đổi các mô hình Phi-3.x sang INT4, trong khi AI PC / Copilot PC có thể sử dụng độ chính xác cao hơn như INT8, FP16, FP32.

Hiện nay, các nhà sản xuất phần cứng khác nhau có các khung hỗ trợ mô hình sinh khác nhau, chẳng hạn như OpenVINO của Intel, QNN của Qualcomm, MLX của Apple, và CUDA của Nvidia, kết hợp với định lượng mô hình để hoàn thành triển khai cục bộ.

Về mặt công nghệ, chúng tôi có các định dạng hỗ trợ khác nhau sau khi định lượng, chẳng hạn như định dạng PyTorch / Tensorflow, GGUF, và ONNX. Tôi đã thực hiện so sánh định dạng và các kịch bản ứng dụng giữa GGUF và ONNX. Ở đây tôi khuyến nghị sử dụng định dạng định lượng ONNX, vì nó được hỗ trợ tốt từ khung mô hình đến phần cứng. Trong chương này, chúng tôi sẽ tập trung vào ONNX Runtime cho GenAI, OpenVINO, và Apple MLX để thực hiện định lượng mô hình (nếu bạn có cách tốt hơn, bạn cũng có thể gửi cho chúng tôi bằng cách nộp PR).

**Chương này bao gồm**

1. [Định lượng Phi-3.5 / 4 bằng llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Định lượng Phi-3.5 / 4 bằng các tiện ích mở rộng Generative AI cho onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Định lượng Phi-3.5 / 4 bằng Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Định lượng Phi-3.5 / 4 bằng Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi nỗ lực để đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin đáng tin cậy nhất. Đối với các thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.