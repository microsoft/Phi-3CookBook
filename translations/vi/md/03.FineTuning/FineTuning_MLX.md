# **Tinh chỉnh Phi-3 với Apple MLX Framework**

Chúng ta có thể thực hiện tinh chỉnh kết hợp với Lora thông qua dòng lệnh của Apple MLX Framework. (Nếu bạn muốn biết thêm về cách hoạt động của MLX Framework, vui lòng đọc [Inference Phi-3 với Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Chuẩn bị dữ liệu**

Theo mặc định, MLX Framework yêu cầu định dạng jsonl cho train, test và eval, và kết hợp với Lora để hoàn thành các công việc tinh chỉnh.

### ***Lưu ý:***

1. Định dạng dữ liệu jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Ví dụ của chúng tôi sử dụng [dữ liệu của TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), nhưng lượng dữ liệu tương đối ít, vì vậy kết quả tinh chỉnh có thể không phải là tốt nhất. Khuyến nghị rằng người học nên sử dụng dữ liệu tốt hơn dựa trên các kịch bản của mình để thực hiện.

3. Định dạng dữ liệu được kết hợp với mẫu của Phi-3.

Vui lòng tải dữ liệu từ [đường dẫn này](../../../../code/04.Finetuning/mlx), vui lòng bao gồm tất cả các tệp .jsonl trong thư mục ***data***.

## **2. Tinh chỉnh trên terminal**

Vui lòng chạy lệnh này trên terminal:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***Lưu ý:***

1. Đây là tinh chỉnh LoRA, MLX Framework chưa công bố QLoRA.

2. Bạn có thể chỉnh sửa config.yaml để thay đổi một số tham số, chẳng hạn như:

```yaml


# The path to the local model directory or Hugging Face repo.
model: "microsoft/Phi-3-mini-4k-instruct"
# Whether or not to train (boolean)
train: true

# Directory with {train, valid, test}.jsonl files
data: "data"

# The PRNG seed
seed: 0

# Number of layers to fine-tune
lora_layers: 32

# Minibatch size.
batch_size: 1

# Iterations to train for.
iters: 1000

# Number of validation batches, -1 uses the entire validation set.
val_batches: 25

# Adam learning rate.
learning_rate: 1e-6

# Number of training steps between loss reporting.
steps_per_report: 10

# Number of training steps between validations.
steps_per_eval: 200

# Load path to resume training with the given adapter weights.
resume_adapter_file: null

# Save/load path for the trained adapter weights.
adapter_path: "adapters"

# Save the model every N iterations.
save_every: 1000

# Evaluate on the test set after training
test: false

# Number of test set batches, -1 uses the entire test set.
test_batches: 100

# Maximum sequence length.
max_seq_length: 2048

# Use gradient checkpointing to reduce memory use.
grad_checkpoint: true

# LoRA parameters can only be specified in a config file
lora_parameters:
  # The layer keys to apply LoRA to.
  # These will be applied for the last lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  scale: 1
  dropout: 0.1


```

Vui lòng chạy lệnh này trên terminal:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Chạy adapter tinh chỉnh để kiểm tra**

Bạn có thể chạy adapter tinh chỉnh trên terminal, như sau:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

và chạy mô hình gốc để so sánh kết quả:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Bạn có thể thử so sánh kết quả của tinh chỉnh với mô hình gốc.

## **4. Hợp nhất adapter để tạo mô hình mới**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Chạy mô hình tinh chỉnh đã lượng hóa bằng ollama**

Trước khi sử dụng, vui lòng cấu hình môi trường llama.cpp của bạn:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Lưu ý:***

1. Hiện hỗ trợ chuyển đổi lượng hóa từ fp32, fp16 và INT 8.

2. Mô hình đã hợp nhất bị thiếu tokenizer.model, vui lòng tải xuống từ https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Cài đặt tệp Ollama Model (Nếu chưa cài đặt ollama, vui lòng đọc [Ollama QuickStart](https://ollama.com/)):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Chạy lệnh trên terminal:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Chúc mừng! Bạn đã thành thạo tinh chỉnh với MLX Framework.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.