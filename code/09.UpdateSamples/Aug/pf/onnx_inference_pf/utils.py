# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import os
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, TextStreamer
from peft import PeftModel

def get_device_map():
    num_gpus = torch.cuda.device_count()

    if num_gpus > 1:
        print("More than one GPU found. Setting device_map to use CUDA device 0.")
        return 'cuda:0'
    else:
        return 'auto'

def check_adapter_path(adapters_name):
    """
    Checks if the adapter path is correctly set and not a placeholder.
    Args:
    adapters_name (str): The file path for the adapters.
    Raises:
    ValueError: If the adapters_name contains placeholder characters.
    """
    if '<' in adapters_name or '>' in adapters_name:
        raise ValueError("The adapter path has not been set correctly.")

def load_tokenizer(model_name):
    """
    Loads and returns a tokenizer for the specified model.
    Args:
    model_name (str): The name of the model for which to load the tokenizer.
    Returns:
    AutoTokenizer: The loaded tokenizer with special tokens added and padding side set.
    """
    tok = AutoTokenizer.from_pretrained(model_name, device_map=get_device_map(), trust_remote_code=True)
    tok.add_special_tokens({'pad_token': '[PAD]'})
    tok.padding_side = 'right'  # TRL requires right padding
    return tok

def load_model(model_name, torch_dtype, quant_type):
    """
    Loads and returns a model with the specified quantization configuration.
    If more than one GPU is available, wraps the model with DataParallel.
    Args:
    model_name (str): The name of the model to load.
    torch_dtype (torch.dtype): The data type for model weights (e.g., torch.float16).
    quant_type (str): The quantization type to use.
    Returns:
    AutoModelForCausalLM: The loaded model possibly wrapped with DataParallel.
    """
    try:
        model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_name,
            trust_remote_code=True,
            device_map=get_device_map(),
            torch_dtype=torch_dtype,
            quantization_config=BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch_dtype,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type=quant_type
            ),
        )
      
        return model
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")

def resize_embeddings(model, tokenizer):
    """
    Resizes the token embeddings in the model to account for new tokens.
    Args:
    model (AutoModelForCausalLM): The model whose token embeddings will be resized.
    tokenizer (AutoTokenizer): The tokenizer corresponding to the model.
    """
    model.resize_token_embeddings(len(tokenizer))

def load_peft_model(model, adapters_name):
    """
    Loads the PEFT model from the pretrained model and specified adapters.
    Args:
    model (AutoModelForCausalLM): The base model.
    adapters_name (str): Path to the adapters file.
    Returns:
    PeftModel: The PEFT model with the loaded adapters.
    """
    return PeftModel.from_pretrained(model, adapters_name)

def get_device():
    """
    Determines and returns the device to use for computations.
    If CUDA is available, returns a CUDA device, otherwise returns a CPU device.
    Prints the number of GPUs available if CUDA is used.
    Returns:
    torch.device: The device to use.
    """
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Number of GPUs available: {torch.cuda.device_count()}")
    else:
        device = torch.device("cpu")
    return device

def run_prompt(model, tokenizer, device, template):
    """
    Runs an interactive prompt where the user can enter text to get generated responses.
    Continues to prompt the user for input until '#end' is entered.
    Args:
    model (AutoModelForCausalLM): The model to use for text generation.
    tokenizer (AutoTokenizer): The tokenizer to use for encoding the input text.
    device (torch.device): The device on which to perform the computation.
    template (str): The template string to format the input text.
    """
    while True:
        new_input = input("Enter your text (type #end to stop): ")
        if new_input == "#end":
            break

        try:
            _ = generate_text(model, tokenizer, device, new_input, template)
        except Exception as e:
            print(f"An error occurred during text generation: {e}")
            
def generate_text(model, tokenizer, device, input_text, template):
    """
    Generates and returns text using the provided model and tokenizer for the input text.
    Args:
    model (AutoModelForCausalLM): The model to use for text generation.
    tokenizer (AutoTokenizer): The tokenizer to use for encoding the input text.
    device (torch.device): The device on which to perform the computation.
    input_text (str): The input text to generate responses for.
    template (str): The template string to format the input text.
    Returns:
    torch.Tensor: The generated text tensor.
    """
    inputs = tokenizer(template.format(input_text), return_tensors="pt")
    inputs = inputs.to(device)  # Move input tensors to the device
    streamer = TextStreamer(tokenizer)
    return model.generate(**inputs, streamer=streamer,
                          max_new_tokens=1024,
                          pad_token_id=tokenizer.pad_token_id,
                          eos_token_id=tokenizer.eos_token_id)

def get_last_folder_alphabetically(directory_path):
    """
    Finds the last folder alphabetically in a specified directory.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        str: The path to the last folder found alphabetically.
        If the directory does not exist or contains no folders, a descriptive string is returned.
    """
    if not os.path.exists(directory_path):
        return "Directory does not exist."

    all_files_and_folders = os.listdir(directory_path)
    only_folders = [f for f in all_files_and_folders if os.path.isdir(os.path.join(directory_path, f))]
    if not only_folders:
        return "No folders found in the directory."

    only_folders.sort(key=natural_sort_key)
    last_folder = only_folders[-1]
    return os.path.join(directory_path, last_folder)

def natural_sort_key(s):
    """
    Generates a key for sorting strings that contain numbers where the numbers should be sorted numerically,
    and the rest alphabetically.

    Args:
        s (str): The string to be sorted.

    Returns:
        list: A list of strings and integers derived from the input string.
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]
