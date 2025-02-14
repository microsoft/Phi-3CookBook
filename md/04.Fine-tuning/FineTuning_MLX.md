# **Fine-tuning Phi-3 with Apple MLX Framework**

Fine-tuning with **LoRA** can be performed using the **Apple MLX framework** via the command line.  
For more details on how the MLX framework works, refer to [Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md).


## 1. Data preparation

By default, the **MLX framework** requires training, testing, and evaluation data in **JSONL** format. It uses **LoRA** to perform fine-tuning.

### JSONL Data Format
   
```json
{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
```

Our example dataset is based on [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv). However, this dataset is relatively small, so the fine-tuning results may not be optimal. We recommend using higher-quality datasets tailored to your specific use case for better results.

The dataset follows the **Phi-3 format**.

### Download data

You can download the dataset from this [link](../../code/04.Finetuning/mlx/) .
Make sure to place all `.jsonl` files inside the ***data*** folder.

## 2. Fine-tuning in your terminal

Run the following command in your terminal:

```bash
python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 
```

> **💡 Note:**
> This implementation performs LoRA fine-tuning using the MLX framework. It is not the officially published QLoRA method.
> To modify the training configuration, update the parameters in `config.yaml`, such as:
.
> ```yaml
># The path to the local model directory or Hugging Face repo.
>model: "microsoft/Phi-3-mini-4k-instruct"
># Whether or not to train (boolean)
>train: true
>
># Directory with {train, valid, test}.jsonl files
>data: "data"
>
># The PRNG seed
>seed: 0
>
># Number of layers to fine-tune
>lora_layers: 32
>
># Minibatch size.
>batch_size: 1
>
># Iterations to train for.
>iters: 1000
>
># Number of validation batches, -1 uses the entire validation set.
>val_batches: 25
>
># Adam learning rate.
>learning_rate: 1e-6
>
># Number of training steps between loss reporting.
>steps_per_report: 10
>
># Number of training steps between validations.
>steps_per_eval: 200
>
># Load path to resume training with the given adapter weights.
>resume_adapter_file: null
>
># Save/load path for the trained adapter weights.
>adapter_path: "adapters"
>
># Save the model every N iterations.
>save_every: 1000
>
># Evaluate on the test set after training
>test: false
>
># Number of test set batches, -1 uses the entire test set.
>test_batches: 100
>
># Maximum sequence length.
>max_seq_length: 2048
>
># Use gradient checkpointing to reduce memory use.
>grad_checkpoint: true
>
># LoRA parameters can only be specified in a config file
>lora_parameters:
>  # The layer keys to apply LoRA to.
>  # These will be applied for the last lora_layers
>  keys: ["o_proj","qkv_proj"]
>  rank: 64
>  scale: 1
>  dropout: 0.1
> ```
>
> In that case, please run this command in the terminal:
>
> ```bash
> python -m mlx_lm.lora --config lora_config.yaml
> ```

## 3. Run Fine-Tuning Adapter to Test

You can run the fine-tuned adapter in the terminal using the following command:

```bash
python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors?" --eos-token "<|end|>"
```

To compare the results, run the original model without fine-tuning:

```bash
python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors?" --eos-token "<|end|>"
```

Try comparing the output from the fine-tuned model with the original model to see the differences.

## 4. Merge Adapters to Generate a New Model

To merge the fine-tuned adapters into a new model, run the following command:

```bash
python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct
```

## 5. Run Inference on the Merged Model

After merging the adapters, you can run inference on the newly generated model using the following command:

```bash
python -m mlx_lm.generate --model ./fused_model --max-token 2048 --prompt "What is the happiest place on Earth?" --eos-token "<|end|>"
```

The model can now be used for inference with any framework that supports the **SafeTensors** format.
🎉 **Congratulations!** You’ve successfully mastered fine-tuning with the **MLX Framework**!

## 6. (optional) Running Quantized Fine-Tuned Models Using Ollama

First configure your `llama.cpp` environment:

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
pip install -r requirements.txt
```

Now convert from the SafeTensors format to the Ollama format:

```bash
python convert_hf_to_gguf.py 'Your merged model path' --outfile phi-3-mini-ft.gguf --outtype q4_0
```

>
> **💡 Note:**
> 1. The conversion process supports exporting the model in **fp32, fp16**, and various quantized formats such as **q4_0, q4_1, q8_0, and INT8**.
> 2. The merged model is missing `tokenizer.model`. Please download it from [Hugging Face](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct).  


### Set Up Ollama Model File

If you haven’t installed Ollama yet, refer to the [Ollama QuickStart Guide](../02.QuickStart/Ollama_QuickStart.md).

Create a `Modelfile` with the following content:

```txt
FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"
```

### Run the Model in Your Terminal

Execute the following commands to create and run the fine-tuned model in Ollama:

```bash
ollama create phi3ft -f Modelfile
ollama run phi3ft "Why do chameleons change colors?"
```
