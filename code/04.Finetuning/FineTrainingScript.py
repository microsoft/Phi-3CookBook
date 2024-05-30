# This code is for fine-tuning Phi-3 Models.
# Note thi requires 7.4 GB of GPU RAM for the process.
# Model available at https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3
# Model Names 
# microsoft/Phi-3-mini-4k-instruct
# microsoft/Phi-3-mini-128k-instruct
# microsoft/Phi-3-small-8k-instruct
# microsoft/Phi-3-small-128k-instruct
# microsoft/Phi-3-medium-4k-instruct
# microsoft/Phi-3-medium-128k-instruct
# microsoft/Phi-3-vision-128k-instruct
# microsoft/Phi-3-mini-4k-instruct-onnx
# microsoft/Phi-3-mini-4k-instruct-onnx-web
# microsoft/Phi-3-mini-128k-instruct-onnx
# microsoft/Phi-3-small-8k-instruct-onnx-cuda
# microsoft/Phi-3-small-128k-instruct-onnx-cuda
# microsoft/Phi-3-medium-4k-instruct-onnx-cpu
# microsoft/Phi-3-medium-4k-instruct-onnx-cuda
# microsoft/Phi-3-medium-4k-instruct-onnx-directml
# microsoft/Phi-3-medium-128k-instruct-onnx-cpu
# microsoft/Phi-3-medium-128k-instruct-onnx-cuda
# microsoft/Phi-3-medium-128k-instruct-onnx-directml
# microsoft/Phi-3-mini-4k-instruct-gguf

# Load the pre-trained model and tokenizer
model = AutoModelForCausalLM.from_pretrained('Model_Name', torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained('Mode_Name')

# Load the dataset for fine-tuning
dataset = load_dataset(DATASET_NAME, split="train")

# Define the formatting function for the prompts
def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = []
    mapper = {"system": "system\n", "human": "\nuser\n", "gpt": "\nassistant\n"}
    end_mapper = {"system": "", "human": "", "gpt": ""}
    for convo in convos:
        text = "".join(f"{mapper[(turn := x['from'])]} {x['value']}\n{end_mapper[turn]}" for x in convo)
        texts.append(f"{text}{tokenizer.eos_token}")
    return {"text": texts}

# Apply the formatting function to the dataset
dataset = dataset.map(formatting_prompts_func, batched=True)

# Define the training arguments
args = TrainingArguments(
    evaluation_strategy="steps",
    per_device_train_batch_size=7,
    gradient_accumulation_steps=4,
    gradient_checkpointing=True,
    learning_rate=1e-4,
    fp16=True,
    max_steps=-1,
    num_train_epochs=3,
    save_strategy="epoch",
    logging_steps=10,
    output_dir=NEW_MODEL_NAME,
    optim="paged_adamw_32bit",
    lr_scheduler_type="linear"
)

# Create the trainer
trainer = SFTTrainer(
    model=model,
    args=args,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=128,
    formatting_func=formatting_prompts_func
)

# Start the training process
trainer.train()