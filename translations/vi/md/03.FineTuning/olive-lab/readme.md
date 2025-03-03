# Phòng thí nghiệm: Tối ưu hóa mô hình AI cho suy luận trên thiết bị

## Giới thiệu

> [!IMPORTANT]
> Phòng thí nghiệm này yêu cầu một **GPU Nvidia A10 hoặc A100** với driver và bộ công cụ CUDA (phiên bản 12+) đã được cài đặt.

> [!NOTE]
> Đây là một phòng thí nghiệm kéo dài **35 phút**, cung cấp cho bạn phần thực hành giới thiệu các khái niệm cốt lõi về tối ưu hóa mô hình cho suy luận trên thiết bị bằng OLIVE.

## Mục tiêu học tập

Sau khi hoàn thành phòng thí nghiệm này, bạn sẽ có thể sử dụng OLIVE để:

- Lượng tử hóa mô hình AI bằng phương pháp lượng tử hóa AWQ.
- Tinh chỉnh một mô hình AI cho một nhiệm vụ cụ thể.
- Tạo bộ điều hợp LoRA (mô hình tinh chỉnh) để suy luận hiệu quả trên thiết bị sử dụng ONNX Runtime.

### Olive là gì

Olive (*O*NNX *live*) là một bộ công cụ tối ưu hóa mô hình với giao diện dòng lệnh (CLI) đi kèm, giúp bạn triển khai các mô hình cho ONNX Runtime +++https://onnxruntime.ai+++ với chất lượng và hiệu năng cao.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.vi.png)

Đầu vào của Olive thường là một mô hình PyTorch hoặc Hugging Face, và đầu ra là một mô hình ONNX được tối ưu hóa để chạy trên thiết bị (mục tiêu triển khai) sử dụng ONNX Runtime. Olive sẽ tối ưu hóa mô hình cho bộ tăng tốc AI của thiết bị (NPU, GPU, CPU) do các nhà cung cấp phần cứng như Qualcomm, AMD, Nvidia hoặc Intel cung cấp.

Olive thực thi một *quy trình làm việc* - một chuỗi sắp xếp các nhiệm vụ tối ưu hóa mô hình riêng lẻ gọi là *pass*. Các ví dụ về pass bao gồm: nén mô hình, chụp đồ thị, lượng tử hóa, tối ưu hóa đồ thị. Mỗi pass có một tập hợp tham số có thể được tinh chỉnh để đạt được các chỉ số tốt nhất, chẳng hạn như độ chính xác và độ trễ, được đánh giá bởi bộ đánh giá tương ứng. Olive sử dụng chiến lược tìm kiếm với thuật toán tìm kiếm để tự động tinh chỉnh từng pass hoặc một tập hợp các pass.

#### Lợi ích của Olive

- **Giảm bớt sự thất vọng và thời gian** khi thử nghiệm thủ công bằng các kỹ thuật khác nhau để tối ưu hóa đồ thị, nén và lượng tử hóa. Định nghĩa các ràng buộc về chất lượng và hiệu năng của bạn và để Olive tự động tìm ra mô hình tốt nhất.
- **Hơn 40 thành phần tối ưu hóa mô hình tích hợp sẵn**, bao gồm các kỹ thuật tiên tiến về lượng tử hóa, nén, tối ưu hóa đồ thị và tinh chỉnh.
- **CLI dễ sử dụng** cho các nhiệm vụ tối ưu hóa mô hình thông thường. Ví dụ: olive quantize, olive auto-opt, olive finetune.
- Đóng gói và triển khai mô hình được tích hợp sẵn.
- Hỗ trợ tạo mô hình cho **Multi LoRA serving**.
- Xây dựng quy trình làm việc bằng YAML/JSON để điều phối các nhiệm vụ tối ưu hóa và triển khai mô hình.
- Tích hợp với **Hugging Face** và **Azure AI**.
- Cơ chế **bộ nhớ đệm** tích hợp để **tiết kiệm chi phí**.

## Hướng dẫn phòng thí nghiệm
> [!NOTE]
> Hãy đảm bảo bạn đã cung cấp Azure AI Hub và Project cũng như thiết lập máy tính A100 theo Phòng thí nghiệm 1.

### Bước 0: Kết nối với Azure AI Compute

Bạn sẽ kết nối với Azure AI Compute bằng tính năng điều khiển từ xa trong **VS Code.** 

1. Mở ứng dụng **VS Code** trên máy tính của bạn:
1. Mở **bảng lệnh** bằng cách nhấn **Shift+Ctrl+P**.
1. Trong bảng lệnh, tìm kiếm **AzureML - remote: Connect to compute instance in New Window**.
1. Làm theo hướng dẫn trên màn hình để kết nối với Compute. Điều này sẽ bao gồm việc chọn Azure Subscription, Resource Group, Project và Compute name mà bạn đã thiết lập trong Phòng thí nghiệm 1.
1. Khi bạn đã kết nối với Azure ML Compute node, thông tin này sẽ được hiển thị ở **góc dưới bên trái của Visual Code** `><Azure ML: Compute Name`

### Bước 1: Sao chép repo này

Trong VS Code, bạn có thể mở một terminal mới bằng **Ctrl+J** và sao chép repo này:

Trong terminal, bạn sẽ thấy lời nhắc

```
azureuser@computername:~/cloudfiles/code$ 
```
Sao chép giải pháp 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Bước 2: Mở thư mục trong VS Code

Để mở VS Code trong thư mục liên quan, thực hiện lệnh sau trong terminal, lệnh này sẽ mở một cửa sổ mới:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Hoặc, bạn có thể mở thư mục bằng cách chọn **File** > **Open Folder**. 

### Bước 3: Cài đặt các phụ thuộc

Mở cửa sổ terminal trong VS Code trong Azure AI Compute Instance (mẹo: **Ctrl+J**) và thực hiện các lệnh sau để cài đặt các phụ thuộc:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Việc cài đặt tất cả các phụ thuộc sẽ mất khoảng ~5 phút.

Trong phòng thí nghiệm này, bạn sẽ tải xuống và tải lên các mô hình vào danh mục mô hình Azure AI. Để truy cập danh mục mô hình, bạn cần đăng nhập vào Azure bằng:

```bash
az login
```

> [!NOTE]
> Khi đăng nhập, bạn sẽ được yêu cầu chọn subscription. Hãy đảm bảo chọn subscription được cung cấp cho phòng thí nghiệm này.

### Bước 4: Thực thi các lệnh Olive 

Mở cửa sổ terminal trong VS Code trong Azure AI Compute Instance (mẹo: **Ctrl+J**) và đảm bảo môi trường `olive-ai` của conda đã được kích hoạt:

```bash
conda activate olive-ai
```

Tiếp theo, thực thi các lệnh Olive sau trong dòng lệnh.

1. **Kiểm tra dữ liệu:** Trong ví dụ này, bạn sẽ tinh chỉnh mô hình Phi-3.5-Mini để nó chuyên trả lời các câu hỏi liên quan đến du lịch. Mã dưới đây hiển thị một vài bản ghi đầu tiên của tập dữ liệu, được định dạng theo JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Lượng tử hóa mô hình:** Trước khi huấn luyện mô hình, bạn sẽ lượng tử hóa bằng lệnh sau, sử dụng một kỹ thuật gọi là Lượng tử hóa Chủ động Nhận thức (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ lượng tử hóa trọng số của một mô hình bằng cách xem xét các kích hoạt được tạo ra trong quá trình suy luận. Điều này có nghĩa là quá trình lượng tử hóa tính đến phân phối dữ liệu thực tế trong các kích hoạt, dẫn đến việc bảo toàn độ chính xác của mô hình tốt hơn so với các phương pháp lượng tử hóa trọng số truyền thống.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Quá trình này mất **~8 phút** để hoàn thành lượng tử hóa AWQ, giúp **giảm kích thước mô hình từ ~7.5GB xuống ~2.5GB**.
   
    Trong phòng thí nghiệm này, chúng tôi sẽ chỉ cho bạn cách nhập mô hình từ Hugging Face (ví dụ: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` để tinh chỉnh mô hình đã lượng tử hóa. Lượng tử hóa mô hình *trước khi* tinh chỉnh thay vì sau đó sẽ mang lại độ chính xác tốt hơn vì quá trình tinh chỉnh phục hồi một số tổn thất từ lượng tử hóa.

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
    
    Quá trình tinh chỉnh mất **~6 phút** (với 100 bước).

1. **Tối ưu hóa:** Với mô hình đã được huấn luyện, bạn sẽ tối ưu hóa mô hình bằng lệnh `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` của Olive - nhưng trong phòng thí nghiệm này, chúng ta sẽ sử dụng CPU.

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
    
    Quá trình tối ưu hóa mất **~5 phút**.

### Bước 5: Kiểm tra nhanh suy luận mô hình

Để kiểm tra suy luận của mô hình, tạo một tệp Python trong thư mục của bạn với tên **app.py** và sao chép-dán đoạn mã sau:

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

Việc tải mô hình lên kho mô hình Azure AI giúp mô hình có thể chia sẻ với các thành viên khác trong nhóm phát triển của bạn và cũng xử lý việc kiểm soát phiên bản của mô hình. Để tải mô hình lên, chạy lệnh sau:

> [!NOTE]
> Cập nhật `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"và tên Dự án Azure AI, sau đó chạy lệnh sau 

```
az ml workspace show
```

Hoặc bằng cách truy cập +++ai.azure.com+++ và chọn **management center** **project** **overview**

Cập nhật các chỗ `{}` với tên nhóm tài nguyên và Tên Dự án Azure AI của bạn.

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
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.