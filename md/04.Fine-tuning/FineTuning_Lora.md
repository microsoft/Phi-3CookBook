# **Fine-tuning Phi-3**

Fine-tuning Microsoft’s Phi-3 Mini language model using [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA) on a custom chat instruction dataset. 

LORA will help improve conversational understanding and response generation. 

## Step-by-step guide on how to fine-tune Phi-3 Mini:

**Imports and Setup** 

Installing loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Begin by importing necessary libraries such as datasets, transformers, peft, trl, and torch.
Set up logging to track the training process.

You can choose to adapt some layers by replacing them with counterparts implemented in loralib. We only support nn.Linear, nn.Embedding, and nn.Conv2d for now. We also support a MergedLinear for cases where a single nn.Linear represents more than one layers, such as in some implementations of the attention qkv projection (see Additional Notes for more).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Before the training loop begins, mark only LoRA parameters as trainable.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

When saving a checkpoint, generate a state_dict that only contains LoRA parameters.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

When loading a checkpoint using load_state_dict, be sure to set strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Now training can proceed as usual.

**Hyperparameters** 

Define two dictionaries: training_config and peft_config. training_config includes hyperparameters for training, such as learning rate, batch size, and logging settings.

peft_config specifies LoRA-related parameters like rank, dropout, and task type.

**Model and Tokenizer Loading** 

Specify the path to the pre-trained Phi-3 model (e.g., "microsoft/Phi-3-mini-4k-instruct"). Configure model settings, including cache usage, data type (bfloat16 for mixed precision), and attention implementation.

**Training** 

Fine-tune the Phi-3 model using the custom chat instruction dataset. Utilize the LoRA settings from peft_config for efficient adaptation. Monitor training progress using the specified logging strategy.
Evaluation and Saving: Evaluate the fine-tuned model.
Save checkpoints during training for later use.

## Fine-Tuning Phi-3 with Azure AI Studio

### Set Up Your Environment 

**Azure AI Studio** 

If you haven’t already, sign in to [Azure AI Studio](https://ai.azure.com).

**Create a New Project** 

Click on “New” and create a new project. Choose the appropriate settings based on your use case.

**Dataset Selection** 

Gather or create a dataset that aligns with your task. This could be chat instructions, question-answer pairs, or any relevant text data.

**Data Preprocessing** 

Clean and preprocess your data. Remove noise, handle missing values, and tokenize the text.

**Model Selection**

Phi-3 Mini: You’ll be fine-tuning the pre-trained Phi-3 Mini model. Make sure you have access to the model checkpoint (e.g., "microsoft/Phi-3-mini-128k-instruct").

**Fine-Tuning Configuration - Hyperparameters** 

Define hyperparameters such as learning rate, batch size, and number of training epochs.
Loss Function: Choose an appropriate loss function for your task (e.g., cross-entropy).

**Optimizer** 

Select an optimizer (e.g., Adam) for gradient updates during training.

**Fine-Tuning Process - Load Pre-Trained Model** 

Load the Phi-3 Mini checkpoint.

**Add Custom Layers** 

Add task-specific layers (e.g., classification head for chat instructions).

**Train the Model** 

Fine-tune the model using your prepared dataset. Monitor training progress and adjust hyperparameters as needed.

**Evaluation and Validation - Validation Set** 

Split your data into training and validation sets.
Evaluate Performance: Use metrics like accuracy, F1-score, or perplexity to assess model performance.

**Save Fine-Tuned Model Checkpoint** 

Save the fine-tuned model checkpoint for future use.

**Deployment** 

Deploy as a Web Service: Deploy your fine-tuned model as a web service in Azure AI Studio.
Test the Endpoint: Send test queries to the deployed endpoint to verify its functionality.
Iterate and Improve: Iterate: If the performance isn’t satisfactory, iterate by adjusting hyperparameters, adding more data, or fine-tuning for additional epochs.
Monitor and Refine: Continuously monitor the model’s behavior and refine as needed.

**Customize and Extend: Custom Tasks** 

Phi-3 Mini can be fine-tuned for various tasks beyond chat instructions. Explore other use cases!

**Experiment** 

Try different architectures, layer combinations, and techniques to enhance performance.

***Note***: Fine-tuning is an iterative process. Experiment, learn, and adapt your model to achieve the best results for your specific task. Fine-tuning allows you to adapt Phi-3 Mini to specific tasks, making it even more powerful and context-aware. 