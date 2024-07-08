## 带有 Whisper 的交互式 Phi 3 Mini 4K Instruct 聊天机器人

### 介绍

交互式 Phi 3 Mini 4K 聊天机器人是一款工具，允许用户使用文本或音频输入与微软 Phi 3 Mini 4K Instruct 演示进行互动。该聊天机器人可用于各种任务，如翻译、天气更新和一般信息收集。

### 入门

要使用这个聊天机器人，请按照以下说明操作：

1. 打开一个新的 [Jupyter 笔记本并运行提供的代码](E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)。
2. 在笔记本的主窗口中，你会看到一个带有文本输入框和“发送”按钮的聊天框界面。
3. 要使用基于文本的聊天机器人，只需在文本输入框中输入你的消息，然后点击“发送”按钮。聊天机器人会回复一个可以直接在笔记本中播放的音频文件。

**注意**：此工具需要 GPU 以及对微软 Phi-3 和 OpenAI Whisper 模型的访问权限，这些模型用于语音识别和翻译。

### GPU 要求

运行此演示所需的 GPU 内存取决于多个因素，例如输入数据的大小（音频或文本）、用于翻译的语言、模型的速度以及 GPU 上的可用内存。但一般来说你需要 12GB 的 GPU 内存。

一般来说，Whisper 模型设计用于在 GPU 上运行。运行 Whisper 模型的推荐最低 GPU 内存为 8 GB，但如果可以的话，它可以处理更大的内存。

需要注意的是，在模型上运行大量数据或高量请求可能需要更多的 GPU 内存，这可能会导致性能问题。建议用不同的配置测试你的使用情况，并监控内存使用情况，以确定适合你具体需求的最佳设置。

### Jupyter 笔记本，用音频或书面文本作为输入运行微软 Phi 3 Mini 4K Instruct 演示，并生成文本

代码定义了几个函数：

[E2E 示例 Phi-3 和 Whisper](E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)

1. `tts_file_name(text)`: 该函数根据输入文本生成一个文件名，用于保存生成的音频文件。
2. `edge_free_tts(chunks_list, speed, voice_name, save_path)`: 该函数使用 Edge TTS API 从输入文本列表生成一个音频文件。输入参数包括文本块列表、语速、语音名称和保存生成音频文件的输出路径。
3. `talk(input_text)`: 该函数使用 Edge TTS API 生成一个音频文件，并将其保存到 /content/audio 目录中的随机文件名。输入参数是要转换为语音的输入文本。
4. `run_text_prompt(message, chat_history)`: 该函数使用微软 Phi 3 Mini 4K 指令演示从消息输入生成音频文件，并将其附加到聊天历史记录中。
5. `run_audio_prompt(audio, chat_history)`: 该函数使用 Whisper 模型 API 将音频文件转换为文本，并将其传递给 `run_text_prompt()` 函数。
6. 该代码启动了一个 Gradio 应用，允许用户通过输入消息或上传音频文件与 Phi 3 Mini 4K 指令演示进行互动。输出显示为应用中的一条文本消息。

### 故障排除

安装 Cuda GPU 驱动程序

1. 确保你的 Linux 应用程序是最新的
```bash
sudo apt update
```
2. 安装 Cuda 驱动程序
```bash
sudo apt install nvidia-cuda-toolkit
```
3. 注册 cuda 驱动程序位置
```bash
echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
```
4. 检查 Nvidia GPU 内存大小（需要 12GB 的 GPU 内存）

```bash
nvidia-smi
```
5. 清空缓存：如果你正在使用 PyTorch，可以调用 torch.cuda.empty_cache() 释放所有未使用的缓存内存，以便其他 GPU 应用程序使用
```python
torch.cuda.empty_cache()
```
6. 检查 Nvidia Cuda
```bash 
nvcc --version
```
7. 创建一个 Hugging Face 令牌

https://huggingface.co/settings/tokens
- 名称 = 项目名称 
- 类型 = Write

8. 如果你遇到以下错误

```bash
/sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
```

运行
```bash
sudo ldconfig
```