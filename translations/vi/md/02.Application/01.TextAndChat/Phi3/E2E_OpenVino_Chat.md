[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Đoạn mã này xuất mô hình sang định dạng OpenVINO, tải nó và sử dụng để tạo phản hồi cho một lời nhắc đã cho.

1. **Xuất mô hình**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Lệnh này sử dụng `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Nhập các thư viện cần thiết**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Các dòng này nhập các lớp từ module `transformers` library and the `optimum.intel.openvino`, cần thiết để tải và sử dụng mô hình.

3. **Thiết lập thư mục và cấu hình mô hình**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` là một dictionary cấu hình mô hình OpenVINO để ưu tiên độ trễ thấp, sử dụng một luồng suy luận, và không sử dụng thư mục bộ nhớ đệm.

4. **Tải mô hình**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Dòng này tải mô hình từ thư mục đã chỉ định, sử dụng các cài đặt cấu hình được định nghĩa trước đó. Nó cũng cho phép thực thi mã từ xa nếu cần thiết.

5. **Tải tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Dòng này tải tokenizer, chịu trách nhiệm chuyển đổi văn bản thành các token mà mô hình có thể hiểu.

6. **Thiết lập các tham số cho tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Dictionary này chỉ định rằng không nên thêm các token đặc biệt vào kết quả đã được token hóa.

7. **Định nghĩa lời nhắc**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Chuỗi này thiết lập một lời nhắc hội thoại, trong đó người dùng yêu cầu trợ lý AI tự giới thiệu.

8. **Token hóa lời nhắc**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Dòng này chuyển lời nhắc thành các token mà mô hình có thể xử lý, trả về kết quả dưới dạng tensor PyTorch.

9. **Tạo phản hồi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Dòng này sử dụng mô hình để tạo phản hồi dựa trên các token đầu vào, với tối đa 1024 token mới.

10. **Giải mã phản hồi**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Dòng này chuyển đổi các token đã tạo thành chuỗi có thể đọc được, bỏ qua các token đặc biệt, và lấy kết quả đầu tiên.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.