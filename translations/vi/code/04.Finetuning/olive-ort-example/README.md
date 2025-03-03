# Tinh chỉnh Phi3 bằng Olive

Trong ví dụ này, bạn sẽ sử dụng Olive để:

1. Tinh chỉnh một bộ điều hợp LoRA để phân loại các cụm từ thành Sad, Joy, Fear, Surprise.
2. Hợp nhất trọng số của bộ điều hợp vào mô hình gốc.
3. Tối ưu hóa và lượng tử hóa mô hình thành `int4`.

Chúng tôi cũng sẽ hướng dẫn bạn cách suy luận với mô hình đã được tinh chỉnh bằng API Generate của ONNX Runtime (ORT).

> **⚠️ Để tinh chỉnh, bạn cần có GPU phù hợp - ví dụ như A10, V100, A100.**

## 💾 Cài đặt

Tạo một môi trường ảo Python mới (ví dụ, sử dụng `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Tiếp theo, cài đặt Olive và các phụ thuộc cần thiết cho quy trình tinh chỉnh:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Tinh chỉnh Phi3 bằng Olive
[File cấu hình Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) chứa một *workflow* với các *passes* sau:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Ở mức cao, workflow này sẽ:

1. Tinh chỉnh Phi3 (trong 150 bước, bạn có thể thay đổi) sử dụng dữ liệu từ [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Hợp nhất trọng số của bộ điều hợp LoRA vào mô hình gốc. Điều này sẽ tạo ra một mô hình duy nhất ở định dạng ONNX.
3. Model Builder sẽ tối ưu hóa mô hình cho ONNX runtime *và* lượng tử hóa mô hình thành `int4`.

Để thực thi workflow, chạy:

```bash
olive run --config phrase-classification.json
```

Khi Olive hoàn tất, mô hình Phi3 đã tinh chỉnh và tối ưu hóa `int4` của bạn sẽ có sẵn tại: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Tích hợp Phi3 đã tinh chỉnh vào ứng dụng của bạn 

Để chạy ứng dụng:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Kết quả trả về sẽ là một phân loại từ đơn của cụm từ (Sad/Joy/Fear/Surprise).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn tham khảo đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.