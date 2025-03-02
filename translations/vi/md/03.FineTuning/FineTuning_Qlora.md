**Tinh chỉnh Phi-3 với QLoRA**

Tinh chỉnh mô hình ngôn ngữ Phi-3 Mini của Microsoft bằng [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA sẽ giúp cải thiện khả năng hiểu hội thoại và tạo phản hồi.

Để tải mô hình ở định dạng 4bits bằng transformers và bitsandbytes, bạn cần cài đặt accelerate và transformers từ mã nguồn, đồng thời đảm bảo bạn đang sử dụng phiên bản mới nhất của thư viện bitsandbytes.

**Ví dụ**
- [Tìm hiểu thêm với notebook mẫu này](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ví dụ về mẫu FineTuning bằng Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Ví dụ về tinh chỉnh trên Hugging Face Hub với LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Ví dụ về tinh chỉnh trên Hugging Face Hub với QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin có thẩm quyền. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.