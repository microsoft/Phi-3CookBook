# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

The Interactive Phi 3 Mini 4K Instruct Chatbot is a tool that allows users to interact with the Microsoft Phi 3 Mini 4K instruct demo using text or audio input. The chatbot can be used for a variety of tasks, such as translation, weather updates, and general information gathering.

### Getting Started

To use this chatbot, simply follow these instructions:

1. Open a new [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb))
2. In the main window of the notebook, you'll see a chatbox interface with a text input box and a "Send" button.
3. To use the text-based chatbot, simply type your message into the text input box and click the "Send" button. The chatbot will respond with an audio file that can be played directly from within the notebook.

**Note**: This tool requires a GPU and access to the Microsoft Phi-3 and OpenAI Whisper models, which is used for speech recognition and translation.

### GPU Requirements

To run this demo you need 12Gb of GPU memory.

The memory requirements for running the **Microsoft-Phi-3-Mini-4K instruct** demo on a GPU will depend on several factors, such as the size of the input data (audio or text), the language used for translation, the speed of the model, and the available memory on the GPU.

In general, the Whisper model is designed to run on GPUs. The recommended minimum amount of GPU memory for running the Whisper model is 8 GB, but it can handle larger amounts of memory if needed.

It's important to note that running a large amount of data or a high volume of requests on the model may require more GPU memory and/or may cause performance issues. It's recommended to test your use case with different configurations and monitor the memory usage to determine the optimal settings for your specific needs.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

The jupyter notebook titled [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrates how to use the Microsoft Phi 3 Mini 4K instruct Demo to generate text from audio or written text input The notebook defines several functions:

1. `tts_file_name(text)`: This function generates a file name based on the input text for saving the generated audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: This function uses the Edge TTS API to generate an audio file from a list of chunks of input text. The input parameters are the list of chunks, the speech rate, the voice name, and the output path for saving the generated audio file.
1. `talk(input_text)`: This function generates an audio file by using the Edge TTS API and saving it to a random file name in the /content/audio directory. The input parameter is the input text to be converted to speech.
1. `run_text_prompt(message, chat_history)`: This function uses the Microsoft Phi 3 Mini 4K instruct demo to generate an audio file from a message input and appends it to the chat history.
1. `run_audio_prompt(audio, chat_history)`: This function converts an audio file into text using the Whisper model API and passes it to the `run_text_prompt()` function.
1. The code launches a Gradio app that allows users to interact with the Phi 3 Mini 4K instruct demo by either typing in messages or uploading audio files. The output is displayed as a text message within the app.

## Troubleshooting

Installing Cuda GPU drivers

1. Ensure your Linux application are upto date

    ```bash
    sudo apt update
    ```

1. Install Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Register the cuda driver location

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Checking Nvidia GPU memory size (Required 12GB of GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Empty Cache: If you’re using PyTorch, you can call torch.cuda.empty_cache() to release all unused cached memory so that it can be used by other GPU applications

    ```python
    torch.cuda.empty_cache() 
    ```

1. Checking Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Perform the following tasks to create a Hugging Face token.

    - Navigate to the [Hugging Face Token Settings page](https://huggingface.co/settings/tokens).
    - Select **New token**.
    - Enter project **Name** you want to use.
    - Select **Type** to **Write**.

> **Note**
>
> If you encounter the following error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> To resolve this, type the following command inside your terminal.
>
> ```bash
> sudo ldconfig
> ```
