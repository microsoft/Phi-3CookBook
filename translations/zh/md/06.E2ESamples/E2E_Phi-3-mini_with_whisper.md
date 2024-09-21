# 互动 Phi 3 Mini 4K Instruct Chatbot 配合 Whisper

## 概述

互动 Phi 3 Mini 4K Instruct Chatbot 是一个工具，允许用户通过文本或音频输入与微软的 Phi 3 Mini 4K instruct 演示进行互动。这个聊天机器人可以用于多种任务，如翻译、天气更新和一般信息收集。

### 入门指南

要使用此聊天机器人，请按照以下步骤操作：

1. 打开一个新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在笔记本的主窗口中，你会看到一个带有文本输入框和“发送”按钮的聊天框界面。
3. 要使用基于文本的聊天机器人，只需在文本输入框中输入你的消息并点击“发送”按钮。聊天机器人会回复一个可以直接在笔记本中播放的音频文件。

**注意**: 这个工具需要 GPU 和访问微软 Phi-3 以及 OpenAI Whisper 模型，用于语音识别和翻译。

### GPU 要求

要运行此演示，你需要 12GB 的 GPU 内存。

在 GPU 上运行 **Microsoft-Phi-3-Mini-4K instruct** 演示的内存要求将取决于多个因素，如输入数据的大小（音频或文本）、翻译所用的语言、模型的速度以及 GPU 上的可用内存。

一般来说，Whisper 模型设计用于在 GPU 上运行。运行 Whisper 模型的推荐最低 GPU 内存为 8 GB，但如果需要，它可以处理更大的内存。

需要注意的是，运行大量数据或高频率请求可能需要更多的 GPU 内存和/或可能导致性能问题。建议用不同的配置测试你的用例，并监控内存使用情况，以确定你的具体需求的最佳设置。

## 互动 Phi 3 Mini 4K Instruct Chatbot 配合 Whisper 的端到端示例

名为 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 jupyter 笔记本演示了如何使用微软的 Phi 3 Mini 4K instruct 演示从音频或书面文本输入生成文本。笔记本定义了几个函数：

1. `tts_file_name(text)`: 这个函数根据输入文本生成一个文件名，用于保存生成的音频文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 这个函数使用 Edge TTS API 从一组输入文本块生成音频文件。输入参数包括块列表、语速、语音名称和保存生成音频文件的输出路径。
1. `talk(input_text)`: 这个函数使用 Edge TTS API 生成一个音频文件，并将其保存到 /content/audio 目录中的随机文件名。输入参数是要转换为语音的输入文本。
1. `run_text_prompt(message, chat_history)`: 这个函数使用微软的 Phi 3 Mini 4K instruct 演示从消息输入生成音频文件，并将其附加到聊天历史记录中。
1. `run_audio_prompt(audio, chat_history)`: 这个函数使用 Whisper 模型 API 将音频文件转换为文本，并将其传递给 `run_text_prompt()` 函数。
1. 代码启动了一个 Gradio 应用程序，允许用户通过输入消息或上传音频文件与 Phi 3 Mini 4K instruct 演示进行互动。输出以文本消息的形式显示在应用程序中。

## 故障排除

安装 Cuda GPU 驱动

1. 确保你的 Linux 应用程序是最新的

    ```bash
    sudo apt update
    ```

1. 安装 Cuda 驱动

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 注册 cuda 驱动位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 检查 Nvidia GPU 内存大小（需要 12GB 的 GPU 内存）

    ```bash
    nvidia-smi
    ```

1. 清空缓存：如果你使用的是 PyTorch，可以调用 torch.cuda.empty_cache() 释放所有未使用的缓存内存，以便其他 GPU 应用程序使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 检查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 执行以下任务以创建 Hugging Face 令牌。

    - 导航到 [Hugging Face Token 设置页面](https://huggingface.co/settings/tokens).
    - 选择 **New token**.
    - 输入你想使用的项目 **Name**.
    - 选择 **Type** 为 **Write**.

> **Note**
>
> 如果你遇到以下错误：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 要解决此问题，请在终端内输入以下命令。
>
> ```bash
> sudo ldconfig
> ```

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请仔细审查输出内容并进行必要的修改。