# Phòng thí nghiệm: Tối ưu hóa mô hình AI cho suy luận trên thiết bị

## Giới thiệu

> [!IMPORTANT]
> Phòng thí nghiệm này yêu cầu một **GPU Nvidia A10 hoặc A100** cùng với các driver và bộ công cụ CUDA (phiên bản 12+) đã được cài đặt.

> [!NOTE]
> Đây là một phòng thí nghiệm kéo dài **35 phút** cung cấp cho bạn trải nghiệm thực hành về các khái niệm cốt lõi trong việc tối ưu hóa mô hình cho suy luận trên thiết bị bằng OLIVE.

## Mục tiêu học tập

Kết thúc phòng thí nghiệm này, bạn sẽ có thể sử dụng OLIVE để:

- Lượng tử hóa một mô hình AI bằng phương pháp lượng tử hóa AWQ.
- Tinh chỉnh một mô hình AI cho một nhiệm vụ cụ thể.
- Tạo các adapter LoRA (mô hình đã tinh chỉnh) để suy luận hiệu quả trên thiết bị với ONNX Runtime.

### Olive là gì?

Olive (*O*NNX *live*) là một bộ công cụ tối ưu hóa mô hình đi kèm với giao diện dòng lệnh (CLI), cho phép bạn triển khai các mô hình cho ONNX runtime +++https://onnxruntime.ai+++ với chất lượng và hiệu suất cao.

![Luồng hoạt động của Olive](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.vi.png)

Đầu vào cho Olive thường là một mô hình PyTorch hoặc Hugging Face, và đầu ra là một mô hình ONNX đã được tối ưu hóa để chạy trên thiết bị (mục tiêu triển khai) sử dụng ONNX runtime. Olive sẽ tối ưu hóa mô hình cho bộ tăng tốc AI (NPU, GPU, CPU) của thiết bị, được cung cấp bởi các nhà sản xuất phần cứng như Qualcomm, AMD, Nvidia hoặc Intel.

Olive thực thi một *workflow* (quy trình làm việc), là một chuỗi các nhiệm vụ tối ưu hóa mô hình riêng lẻ được gọi là *passes* (lượt) - ví dụ: nén mô hình, chụp đồ thị, lượng tử hóa, tối ưu hóa đồ thị. Mỗi lượt có một tập hợp các tham số có thể được điều chỉnh để đạt được các chỉ số tốt nhất, chẳng hạn như độ chính xác và độ trễ, được đánh giá bởi các trình đánh giá tương ứng. Olive sử dụng một chiến lược tìm kiếm với thuật toán tìm kiếm để tự động điều chỉnh từng lượt hoặc một nhóm lượt cùng nhau.

#### Lợi ích của Olive

- **Giảm sự thất vọng và thời gian** thử nghiệm thủ công với các kỹ thuật khác nhau như tối ưu hóa đồ thị, nén và lượng tử hóa. Định nghĩa các ràng buộc về chất lượng và hiệu suất của bạn, và để Olive tự động tìm ra mô hình tốt nhất cho bạn.
- **Hơn 40 thành phần tối ưu hóa mô hình tích hợp sẵn** bao gồm các kỹ thuật tiên tiến trong lượng tử hóa, nén, tối ưu hóa đồ thị và tinh chỉnh.
- **CLI dễ sử dụng** cho các nhiệm vụ tối ưu hóa mô hình phổ biến. Ví dụ: `olive quantize`, `olive auto-opt`, `olive finetune`.
- Tích hợp đóng gói và triển khai mô hình.
- Hỗ trợ tạo mô hình cho **Multi LoRA serving**.
- Xây dựng quy trình làm việc bằng YAML/JSON để sắp xếp các nhiệm vụ tối ưu hóa và triển khai mô hình.
- Tích hợp với **Hugging Face** và **Azure AI**.
- Cơ chế **bộ nhớ đệm tích hợp** để **tiết kiệm chi phí**.

## Hướng dẫn phòng thí nghiệm
> [!NOTE]
> Hãy đảm bảo bạn đã chuẩn bị Azure AI Hub và Dự án, đồng thời thiết lập tài nguyên tính toán A100 như trong Phòng thí nghiệm 1.

### Bước 0: Kết nối với Azure AI Compute

Bạn sẽ kết nối với tài nguyên tính toán Azure AI bằng tính năng kết nối từ xa trong **VS Code.**

1. Mở ứng dụng **VS Code** trên máy tính của bạn:
2. Mở **command palette** bằng **Shift+Ctrl+P**.
3. Trong command palette, tìm kiếm **AzureML - remote: Connect to compute instance in New Window**.
4. Làm theo hướng dẫn trên màn hình để kết nối với Compute. Quá trình này sẽ yêu cầu bạn chọn Subscription, Resource Group, Project và Compute name mà bạn đã thiết lập trong Phòng thí nghiệm 1.
5. Khi bạn đã kết nối thành công với Azure ML Compute node, thông tin này sẽ hiển thị ở **góc dưới bên trái của Visual Code** `><Azure ML: Compute Name`.

### Bước 1: Clone repo này

Trong VS Code, bạn có thể mở một terminal mới bằng **Ctrl+J** và clone repo này:

Trong terminal, bạn sẽ thấy prompt:

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone repo:

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Bước 2: Mở thư mục trong VS Code

Để mở thư mục liên quan trong VS Code, thực thi lệnh sau trong terminal, lệnh này sẽ mở một cửa sổ mới:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Ngoài ra, bạn có thể mở thư mục bằng cách chọn **File** > **Open Folder**.

### Bước 3: Cài đặt các phụ thuộc

Mở cửa sổ terminal trong VS Code trên Azure AI Compute Instance của bạn (gợi ý: **Ctrl+J**) và thực thi các lệnh sau để cài đặt các phụ thuộc:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Quá trình cài đặt các phụ thuộc sẽ mất khoảng **5 phút**.

Trong phòng thí nghiệm này, bạn sẽ tải xuống và tải lên các mô hình vào danh mục mô hình Azure AI. Để truy cập danh mục mô hình, bạn cần đăng nhập vào Azure bằng lệnh:

```bash
az login
```

> [!NOTE]
> Khi đăng nhập, bạn sẽ được yêu cầu chọn Subscription. Hãy đảm bảo chọn Subscription được cung cấp cho phòng thí nghiệm này.

### Bước 4: Thực thi các lệnh của Olive

Mở cửa sổ terminal trong VS Code trên Azure AI Compute Instance của bạn (gợi ý: **Ctrl+J**) và đảm bảo môi trường `olive-ai` conda đã được kích hoạt:

```bash
conda activate olive-ai
```

Tiếp theo, thực thi các lệnh Olive sau trên dòng lệnh.

1. **Kiểm tra dữ liệu:** Trong ví dụ này, bạn sẽ tinh chỉnh mô hình Phi-3.5-Mini để nó chuyên trả lời các câu hỏi liên quan đến du lịch. Mã dưới đây hiển thị vài bản ghi đầu tiên của tập dữ liệu, được lưu ở định dạng JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```
2. **Lượng tử hóa mô hình:** Trước khi huấn luyện mô hình, bạn cần lượng tử hóa mô hình với lệnh sau, sử dụng kỹ thuật gọi là Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ lượng tử hóa các trọng số của mô hình bằng cách xem xét các kích hoạt được tạo ra trong quá trình suy luận. Điều này giúp duy trì độ chính xác của mô hình tốt hơn so với các phương pháp lượng tử hóa trọng số truyền thống.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Quá trình này mất khoảng **8 phút** để hoàn thành và sẽ **giảm kích thước mô hình từ ~7.5GB xuống ~2.5GB**.
   
    Trong phòng thí nghiệm này, chúng ta sẽ sử dụng mô hình từ Hugging Face (ví dụ: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` lệnh này tinh chỉnh mô hình đã được lượng tử hóa. Lượng tử hóa mô hình *trước* khi tinh chỉnh thay vì sau đó sẽ cho độ chính xác tốt hơn vì quá trình tinh chỉnh sẽ phục hồi một phần mất mát từ lượng tử hóa.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Quá trình tinh chỉnh mất khoảng **6 phút** (với 100 bước).

3. **Tối ưu hóa:** Sau khi mô hình được huấn luyện, bạn sẽ tối ưu hóa mô hình bằng lệnh `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` của Olive - nhưng trong phòng thí nghiệm này, chúng ta sẽ sử dụng CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Quá trình tối ưu hóa mất khoảng **5 phút**.

### Bước 5: Kiểm tra suy luận mô hình nhanh chóng

Để kiểm tra suy luận của mô hình, tạo một tệp Python trong thư mục của bạn có tên **app.py** và sao chép-dán đoạn mã sau:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Thực thi mã bằng lệnh:

```bash
python app.py
```

### Bước 6: Tải mô hình lên Azure AI

Việc tải mô hình lên kho mô hình Azure AI giúp chia sẻ mô hình với các thành viên khác trong nhóm phát triển của bạn và cũng xử lý việc kiểm soát phiên bản của mô hình. Để tải mô hình lên, chạy lệnh sau:

> [!NOTE]
> Cập nhật `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"và tên Dự án Azure AI, sau đó chạy lệnh sau:

```
az ml workspace show
```

Hoặc truy cập +++ai.azure.com+++ và chọn **management center** **project** **overview**.

Cập nhật các `{}` bằng tên nhóm tài nguyên (resource group) và tên dự án Azure AI của bạn.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Bạn có thể xem mô hình đã tải lên và triển khai mô hình tại https://ml.azure.com/model/list

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.