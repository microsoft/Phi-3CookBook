### 示例场景

假设你有一张图片 (`demo.png`)，并希望生成用于处理这张图片并保存其新版本的 Python 代码 (`phi-3-vision.jpg`)。

上述代码通过以下方式实现了这个过程的自动化：

1. 设置环境和必要的配置。
2. 创建一个提示，指示模型生成所需的 Python 代码。
3. 将提示发送给模型并收集生成的代码。
4. 提取并运行生成的代码。
5. 显示原始图片和处理后的图片。

这种方法利用了 AI 的强大功能，自动化了图像处理任务，使得实现目标更加简单快捷。

[示例代码解决方案](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

让我们逐步解析整个代码的功能：

1. **安装所需的包**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    此命令安装 `langchain_nvidia_ai_endpoints` 包，并确保是最新版本。

2. **导入必要的模块**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    这些导入引入了与 NVIDIA AI 端点交互、密码安全处理、操作系统交互以及以 base64 格式编码/解码数据所需的模块。

3. **设置 API 密钥**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    这段代码检查是否设置了 `NVIDIA_API_KEY` 环境变量。如果没有，它会提示用户安全地输入他们的 API 密钥。

4. **定义模型和图片路径**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    这段代码设置了要使用的模型，创建了一个 `ChatNVIDIA` 实例，并定义了图片文件的路径。

5. **创建文本提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    这段代码定义了一个文本提示，指示模型生成用于处理图片的 Python 代码。

6. **将图片编码为 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    这段代码读取图片文件，将其编码为 base64，并创建一个带有编码数据的 HTML 图片标签。

7. **将文本和图片合并到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    这段代码将文本提示和 HTML 图片标签合并为一个字符串。

8. **使用 ChatNVIDIA 生成代码**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    这段代码将提示发送给 `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` 字符串。

9. **从生成内容中提取 Python 代码**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    这段代码通过去除 markdown 格式，从生成的内容中提取实际的 Python 代码。

10. **运行生成的代码**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    这段代码将提取的 Python 代码作为子进程运行，并捕获其输出。

11. **显示图片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    这些代码行使用 `IPython.display` 模块显示图片。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或错误解释不承担责任。