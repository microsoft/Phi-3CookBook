# Tinh chỉnh Phi3 bằng Olive

Trong ví dụ này, bạn sẽ sử dụng Olive để:

1. Tinh chỉnh một bộ chuyển đổi LoRA để phân loại các cụm từ thành Sad, Joy, Fear, Surprise.
2. Gộp trọng số của bộ chuyển đổi vào mô hình gốc.
3. Tối ưu hóa và lượng tử hóa mô hình thành `int4`.

Chúng tôi cũng sẽ hướng dẫn bạn cách suy luận mô hình đã được tinh chỉnh bằng cách sử dụng ONNX Runtime (ORT) Generate API.

> **⚠️ Để tinh chỉnh, bạn cần có một GPU phù hợp - ví dụ, A10, V100, A100.**

## 💾 Cài đặt

Tạo một môi trường ảo Python mới (ví dụ, sử dụng `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Tiếp theo, cài đặt Olive và các thư viện phụ thuộc cần thiết cho quy trình tinh chỉnh:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Tinh chỉnh Phi3 bằng Olive
Tệp [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) chứa một *workflow* với các *passes* sau:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Ở mức cao, workflow này sẽ:

1. Tinh chỉnh Phi3 (trong 150 bước, bạn có thể thay đổi) sử dụng dữ liệu từ [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Gộp trọng số của bộ chuyển đổi LoRA vào mô hình gốc. Điều này sẽ tạo ra một tệp mô hình duy nhất ở định dạng ONNX.
3. Model Builder sẽ tối ưu hóa mô hình cho ONNX runtime *và* lượng tử hóa mô hình thành `int4`.

Để thực thi workflow, chạy lệnh:

```bash
olive run --config phrase-classification.json
```

Khi Olive hoàn thành, mô hình Phi3 đã được tinh chỉnh và tối ưu hóa `int4` của bạn sẽ có sẵn tại: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Tích hợp Phi3 đã tinh chỉnh vào ứng dụng của bạn 

Để chạy ứng dụng:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Phản hồi sẽ là một kết quả phân loại đơn từ cụm từ (Sad/Joy/Fear/Surprise).

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn đáng tin cậy nhất. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.