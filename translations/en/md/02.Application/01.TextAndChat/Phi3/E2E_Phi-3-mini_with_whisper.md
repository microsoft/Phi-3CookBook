# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Overview

The Interactive Phi 3 Mini 4K Instruct Chatbot is a tool that lets users engage with the Microsoft Phi 3 Mini 4K instruct demo through text or audio input. It can be used for various tasks like translation, weather updates, and retrieving general information.

### Getting Started

Follow these steps to use the chatbot:

1. Open the [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. In the notebook's main interface, you'll find a chatbox with a text input field and a "Send" button.
3. To interact via text, type your message in the input field and click "Send." The chatbot will respond with an audio file that you can play directly in the notebook.

**Note**: This tool requires a GPU and access to Microsoft Phi-3 and OpenAI Whisper models, which are used for speech recognition and translation.

### GPU Requirements

You’ll need a GPU with 12GB of memory to run this demo.

The GPU memory required for running the **Microsoft-Phi-3-Mini-4K instruct** demo depends on several factors, including input data size (audio or text), the language used for translation, model speed, and available GPU memory.

Generally, the Whisper model is designed to operate on GPUs. While 8GB of GPU memory is the minimum recommended, having more memory can improve performance.

Keep in mind that processing large data volumes or handling many requests may demand more GPU memory and could affect performance. It’s advisable to test your specific use case with different configurations and monitor memory usage to determine the best setup for your needs.

## E2E Sample for Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

The Jupyter notebook titled [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrates how to use the Microsoft Phi 3 Mini 4K instruct demo to generate text from audio or written input. The notebook defines several functions:

1. `tts_file_name(text)`: Generates a filename based on the input text to save the generated audio file.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Uses the Edge TTS API to create an audio file from a list of input text chunks. Parameters include the list of chunks, speech rate, voice name, and the output path for saving the audio.
3. `talk(input_text)`: Generates an audio file using the Edge TTS API and saves it with a random filename in the /content/audio directory. The input parameter is the text to be converted into speech.
4. `run_text_prompt(message, chat_history)`: Utilizes the Microsoft Phi 3 Mini 4K instruct demo to generate an audio file from a message input and appends it to the chat history.
5. `run_audio_prompt(audio, chat_history)`: Converts an audio file into text using the Whisper model API and passes it to the `run_text_prompt()` function.
6. Launches a Gradio app that allows users to interact with the Phi 3 Mini 4K instruct demo by typing messages or uploading audio files. Outputs are displayed as text messages within the app.

## Troubleshooting

Installing CUDA GPU drivers

1. Make sure your Linux applications are up to date:

    ```bash
    sudo apt update
    ```

2. Install CUDA drivers:

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Register the CUDA driver location:

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Check Nvidia GPU memory size (12GB of GPU memory required):

    ```bash
    nvidia-smi
    ```

5. Empty the cache: If using PyTorch, call `torch.cuda.empty_cache()` to release unused cached memory for other GPU applications.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Check Nvidia CUDA:

    ```bash
    nvcc --version
    ```

7. Follow these steps to create a Hugging Face token:

    - Go to the [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Click **New token**.
    - Enter the project **Name** you want to use.
    - Set the **Type** to **Write**.

> **Note**
>
> If you encounter the following error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> To fix it, run this command in your terminal:
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.