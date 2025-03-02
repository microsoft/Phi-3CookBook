# **Lượng tử hóa Phi Family bằng Generative AI extensions cho onnxruntime**

## **Generative AI extensions cho onnxruntime là gì**

Phần mở rộng này giúp bạn chạy AI tạo sinh với ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Nó cung cấp vòng lặp AI tạo sinh cho các mô hình ONNX, bao gồm suy luận với ONNX Runtime, xử lý logits, tìm kiếm và lấy mẫu, cũng như quản lý bộ nhớ đệm KV. Các nhà phát triển có thể gọi phương thức cấp cao generate(), hoặc chạy từng vòng lặp của mô hình để tạo từng token một, và tùy ý cập nhật các tham số tạo sinh trong vòng lặp. Phần mở rộng này hỗ trợ tìm kiếm greedy/beam và lấy mẫu TopP, TopK để tạo chuỗi token, cũng như xử lý logits tích hợp như áp dụng hình phạt lặp lại. Bạn cũng có thể dễ dàng thêm cách chấm điểm tùy chỉnh.

Ở cấp độ ứng dụng, bạn có thể sử dụng Generative AI extensions cho onnxruntime để xây dựng ứng dụng bằng C++/C#/Python. Ở cấp độ mô hình, bạn có thể sử dụng nó để hợp nhất các mô hình đã tinh chỉnh và thực hiện công việc triển khai định lượng liên quan.

## **Lượng tử hóa Phi-3.5 với Generative AI extensions cho onnxruntime**

### **Hỗ trợ các mô hình**

Generative AI extensions cho onnxruntime hỗ trợ chuyển đổi lượng tử hóa cho Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder trong Generative AI extensions cho onnxruntime**

Model Builder giúp tăng tốc đáng kể việc tạo các mô hình ONNX được tối ưu hóa và lượng tử hóa để chạy với API generate() của ONNX Runtime.

Thông qua Model Builder, bạn có thể lượng tử hóa mô hình xuống INT4, INT8, FP16, FP32, và kết hợp các phương pháp tăng tốc phần cứng khác nhau như CPU, CUDA, DirectML, Mobile, v.v.

Để sử dụng Model Builder, bạn cần cài đặt

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Sau khi cài đặt, bạn có thể chạy script Model Builder từ terminal để thực hiện chuyển đổi định dạng và lượng tử hóa mô hình.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Hiểu các tham số liên quan:

1. **model_name** Đây là mô hình trên Hugging Face, chẳng hạn như microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, v.v. Nó cũng có thể là đường dẫn nơi bạn lưu trữ mô hình.

2. **path_to_output_folder** Đường dẫn lưu kết quả chuyển đổi lượng tử hóa.

3. **execution_provider** Hỗ trợ tăng tốc phần cứng khác nhau, như cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Chúng tôi tải mô hình từ Hugging Face và lưu trữ tạm thời trên máy cục bộ.

***Lưu ý:***

## **Cách sử dụng Model Builder để lượng tử hóa Phi-3.5**

Model Builder hiện hỗ trợ lượng tử hóa mô hình ONNX cho Phi-3.5 Instruct và Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Chuyển đổi lượng tử hóa INT4 với tăng tốc CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Chuyển đổi lượng tử hóa INT4 với tăng tốc CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Thiết lập môi trường trong terminal

```bash

mkdir models

cd models 

```

2. Tải microsoft/Phi-3.5-vision-instruct vào thư mục models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Tải các file sau vào thư mục Phi-3.5-vision-instruct của bạn:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Tải file này vào thư mục models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Mở terminal

   Chuyển đổi ONNX hỗ trợ FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Lưu ý:**

1. Model Builder hiện chỉ hỗ trợ chuyển đổi Phi-3.5-Instruct và Phi-3.5-Vision, chưa hỗ trợ Phi-3.5-MoE.

2. Để sử dụng mô hình ONNX đã lượng tử hóa, bạn có thể sử dụng thông qua Generative AI extensions cho onnxruntime SDK.

3. Chúng ta cần xem xét trách nhiệm AI nhiều hơn, vì vậy sau khi chuyển đổi lượng tử hóa mô hình, nên tiến hành kiểm tra kết quả hiệu quả hơn.

4. Bằng cách lượng tử hóa mô hình CPU INT4, chúng ta có thể triển khai nó trên các thiết bị Edge, mang lại các kịch bản ứng dụng tốt hơn. Vì vậy, chúng tôi đã hoàn thành Phi-3.5-Instruct với INT4.

## **Tài nguyên**

1. Tìm hiểu thêm về Generative AI extensions cho onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Kho GitHub của Generative AI extensions cho onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin có thẩm quyền. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.