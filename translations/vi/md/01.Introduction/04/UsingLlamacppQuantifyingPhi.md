# **Lượng tử hóa Phi Family bằng llama.cpp**

## **Llama.cpp là gì**

llama.cpp là một thư viện phần mềm mã nguồn mở chủ yếu được viết bằng C++ để thực hiện suy luận trên các Mô hình Ngôn ngữ Lớn (LLMs), như Llama. Mục tiêu chính của nó là cung cấp hiệu suất hàng đầu cho suy luận LLM trên nhiều loại phần cứng với thiết lập tối thiểu. Ngoài ra, thư viện này còn có các ràng buộc Python, cung cấp API cấp cao cho việc hoàn thành văn bản và một máy chủ web tương thích với OpenAI.

Mục tiêu chính của llama.cpp là cho phép suy luận LLM với thiết lập tối thiểu và hiệu suất hàng đầu trên nhiều loại phần cứng - cả tại chỗ và trên đám mây.

- Triển khai bằng C/C++ thuần túy, không có bất kỳ phụ thuộc nào
- Apple silicon là công dân hạng nhất - được tối ưu hóa thông qua ARM NEON, Accelerate và Metal frameworks
- Hỗ trợ AVX, AVX2 và AVX512 cho các kiến trúc x86
- Lượng tử hóa số nguyên 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, và 8-bit để suy luận nhanh hơn và giảm sử dụng bộ nhớ
- Kernel CUDA tùy chỉnh để chạy LLMs trên GPU NVIDIA (hỗ trợ GPU AMD thông qua HIP)
- Hỗ trợ backend Vulkan và SYCL
- Suy luận kết hợp CPU+GPU để tăng tốc một phần các mô hình lớn hơn tổng dung lượng VRAM

## **Lượng tử hóa Phi-3.5 bằng llama.cpp**

Mô hình Phi-3.5-Instruct có thể được lượng tử hóa bằng llama.cpp, nhưng Phi-3.5-Vision và Phi-3.5-MoE hiện chưa được hỗ trợ. Định dạng được chuyển đổi bởi llama.cpp là gguf, đây cũng là định dạng lượng tử hóa được sử dụng rộng rãi nhất.

Có rất nhiều mô hình định dạng GGUF lượng tử hóa trên Hugging Face. AI Foundry, Ollama, và LlamaEdge dựa vào llama.cpp, vì vậy các mô hình GGUF cũng thường được sử dụng.

### **GGUF là gì**

GGUF là một định dạng nhị phân được tối ưu hóa để tải và lưu mô hình nhanh chóng, khiến nó trở nên rất hiệu quả cho mục đích suy luận. GGUF được thiết kế để sử dụng với GGML và các bộ thực thi khác. GGUF được phát triển bởi @ggerganov, người cũng là nhà phát triển của llama.cpp, một framework suy luận LLM bằng C/C++ phổ biến. Các mô hình ban đầu được phát triển trong các framework như PyTorch có thể được chuyển đổi sang định dạng GGUF để sử dụng với các công cụ đó.

### **ONNX so với GGUF**

ONNX là một định dạng học máy/học sâu truyền thống, được hỗ trợ tốt trong các Framework AI khác nhau và có nhiều trường hợp sử dụng tốt trên các thiết bị biên. Về phần GGUF, nó dựa trên llama.cpp và có thể được coi là sản phẩm của kỷ nguyên GenAI. Hai định dạng này có cách sử dụng tương tự nhau. Nếu bạn muốn hiệu suất tốt hơn trên phần cứng nhúng và các tầng ứng dụng, ONNX có thể là lựa chọn của bạn. Nếu bạn sử dụng các framework và công nghệ phát sinh từ llama.cpp, thì GGUF có thể phù hợp hơn.

### **Lượng tử hóa Phi-3.5-Instruct bằng llama.cpp**

**1. Cấu hình môi trường**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. Lượng tử hóa**

Sử dụng llama.cpp để chuyển đổi Phi-3.5-Instruct sang FP16 GGUF

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Lượng tử hóa Phi-3.5 sang INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. Kiểm tra**

Cài đặt llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***Lưu ý*** 

Nếu bạn sử dụng Apple Silicon, hãy cài đặt llama-cpp-python như sau

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Kiểm tra

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **Tài nguyên**

1. Tìm hiểu thêm về llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Tìm hiểu thêm về GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.