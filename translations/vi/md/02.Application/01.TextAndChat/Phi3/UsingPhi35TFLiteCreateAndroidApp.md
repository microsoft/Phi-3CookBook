# **Sử dụng Microsoft Phi-3.5 tflite để tạo ứng dụng Android**

Đây là một mẫu ứng dụng Android sử dụng các mô hình Microsoft Phi-3.5 tflite.

## **📚 Kiến thức**

API Android LLM Inference cho phép bạn chạy các mô hình ngôn ngữ lớn (LLMs) hoàn toàn trên thiết bị cho các ứng dụng Android, giúp bạn thực hiện nhiều tác vụ khác nhau như tạo văn bản, truy xuất thông tin bằng ngôn ngữ tự nhiên và tóm tắt tài liệu. Tác vụ này hỗ trợ sẵn cho nhiều mô hình ngôn ngữ lớn dạng text-to-text, vì vậy bạn có thể áp dụng các mô hình AI tạo sinh mới nhất trên thiết bị vào các ứng dụng Android của mình.

Google AI Edge Torch là một thư viện Python hỗ trợ chuyển đổi các mô hình PyTorch sang định dạng .tflite, sau đó có thể chạy với TensorFlow Lite và MediaPipe. Điều này cho phép các ứng dụng trên Android, iOS và IoT chạy các mô hình hoàn toàn trên thiết bị. AI Edge Torch cung cấp hỗ trợ rộng rãi cho CPU, với hỗ trợ ban đầu cho GPU và NPU. AI Edge Torch hướng đến tích hợp chặt chẽ với PyTorch, xây dựng trên nền tảng torch.export() và cung cấp hỗ trợ tốt cho các toán tử Core ATen.

## **🪬 Hướng dẫn**

### **🔥 Chuyển đổi Microsoft Phi-3.5 sang tflite**

0. Mẫu này dành cho Android 14+

1. Cài đặt Python 3.10.12

***Gợi ý:*** sử dụng conda để cài đặt môi trường Python của bạn

2. Ubuntu 20.04 / 22.04 (hãy tập trung vào [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Gợi ý:*** Sử dụng Azure Linux VM hoặc máy ảo đám mây của bên thứ ba để tạo môi trường của bạn

3. Mở bash trên Linux, cài đặt thư viện Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Tải Microsoft-3.5-Instruct từ Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Chuyển đổi Microsoft Phi-3.5 sang tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Chuyển đổi sang gói Mediapipe của Microsoft Phi-3.5**

Hãy cài đặt mediapipe trước tiên

```bash

pip install mediapipe

```

Chạy đoạn mã này trong [notebook của bạn](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 Sử dụng adb push để chuyển mô hình tác vụ vào đường dẫn trên thiết bị Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Chạy mã Android của bạn**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.vi.png)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.