# **使用 Apple MLX 框架微调 Phi-3**

我们可以通过 Apple MLX 框架命令行完成与 Lora 结合的微调。（如果你想了解更多关于 MLX 框架的操作，请阅读 [Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md)

## **1. 数据准备**

默认情况下，MLX 框架需要 train、test 和 eval 的 jsonl 格式数据，并结合 Lora 完成微调任务。

### ***注意:***

1. jsonl 数据格式：

```json

{"text": "<|user|>\n铁处女在什么时候常用？ <|end|>\n<|assistant|> \n铁处女从未被常用 <|end|>"}
{"text": "<|user|>\n人类是从什么进化来的？ <|end|>\n<|assistant|> \n人类和猿类有共同的祖先 <|end|>"}
{"text": "<|user|>\n91 是质数吗？ <|end|>\n<|assistant|> \n不，91 不是质数 <|end|>"}
....

```

2. 我们的示例使用了 [TruthfulQA 的数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但数据量相对不足，因此微调结果不一定是最好的。建议学习者根据自己的场景使用更好的数据完成。

3. 数据格式结合 Phi-3 模板

请从这个 [链接](../../../../code/04.Finetuning/mlx) 下载数据，请将所有 .jsonl 文件放入 ***data*** 文件夹中。

## **2. 在终端进行微调**

请在终端运行以下命令：

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***注意:***

1. 这是 LoRA 微调，MLX 框架尚未发布 QLoRA

2. 你可以通过设置 config.yaml 来更改一些参数，例如：

```yaml

# 本地模型目录或 Hugging Face repo 的路径。
model: "microsoft/Phi-3-mini-4k-instruct"
# 是否训练（布尔值）
train: true

# 包含 {train, valid, test}.jsonl 文件的目录
data: "data"

# PRNG 种子
seed: 0

# 微调的层数
lora_layers: 32

# 小批量大小
batch_size: 1

# 训练迭代次数
iters: 1000

# 验证批次数量，-1 使用整个验证集
val_batches: 25

# Adam 学习率
learning_rate: 1e-6

# 每隔多少训练步骤报告一次损失
steps_per_report: 10

# 每隔多少训练步骤进行一次验证
steps_per_eval: 200

# 加载路径以恢复带有给定适配器权重的训练
resume_adapter_file: null

# 训练适配器权重的保存/加载路径
adapter_path: "adapters"

# 每 N 次迭代保存一次模型
save_every: 1000

# 训练后在测试集上评估
test: false

# 测试集批次数量，-1 使用整个测试集
test_batches: 100

# 最大序列长度
max_seq_length: 2048

# 使用梯度检查点减少内存使用
grad_checkpoint: true

# LoRA 参数只能在配置文件中指定
lora_parameters:
  # 应用 LoRA 的层键
  # 这些将应用于最后的 lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  alpha: 64
  dropout: 0.1

```

请在终端运行以下命令：

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 运行微调适配器进行测试**

你可以在终端运行微调适配器，如下所示：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "变色龙为什么会变色？" --eos-token "<|end|>"    

```

然后运行原始模型进行结果比较：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "变色龙为什么会变色？" --eos-token "<|end|>"    

```

你可以尝试比较微调后的结果与原始模型的结果。

## **4. 合并适配器生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 ollama 运行量化微调模型**

使用前，请配置你的 llama.cpp 环境：

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:*** 

1. 现在支持 fp32、fp16 和 INT 8 的量化转换

2. 合并后的模型缺少 tokenizer.model，请从 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下载

设置 Ollma 模型文件（如果未安装 ollama，请阅读 [Ollama 快速入门](../02.QuickStart/Ollama_QuickStart.md)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在终端运行命令：

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "变色龙为什么会变色？" 

```

恭喜你！掌握了使用 MLX 框架进行微调。

免责声明：此翻译由人工智能模型从原文翻译而来，可能并不完美。请审阅输出并进行必要的修改。