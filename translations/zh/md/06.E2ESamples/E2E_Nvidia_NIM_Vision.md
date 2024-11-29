### 示例场景

假设你有一张图片 (`demo.png`)，并且你想生成处理这张图片并保存其新版本的 Python 代码 (`phi-3-vision.jpg`)。

上述代码自动化了这个过程，具体步骤如下：

1. 设置环境和必要的配置。
2. 创建一个提示，指示模型生成所需的 Python 代码。
3. 将提示发送给模型并收集生成的代码。
4. 提取并运行生成的代码。
5. 显示原始图像和处理后的图像。

这种方法利用 AI 的力量来自动化图像处理任务，使你更容易和更快速地实现目标。

[示例代码解决方案](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

让我们逐步解析整个代码的作用：

1. **安装所需的包**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    这个命令安装了 `langchain_nvidia_ai_endpoints` 包，确保它是最新版本。

2. **导入必要的模块**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    这些导入将必要的模块引入，以便与 NVIDIA AI 端点交互、安全地处理密码、与操作系统交互以及以 base64 格式编码/解码数据。

3. **设置 API 密钥**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    这段代码检查 `NVIDIA_API_KEY` 环境变量是否已设置。如果没有，它会提示用户安全地输入他们的 API 密钥。

4. **定义模型和图像路径**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    这段代码设置要使用的模型，创建一个带有指定模型的 `ChatNVIDIA` 实例，并定义图像文件的路径。

5. **创建文本提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    这段代码定义了一个文本提示，指示模型生成用于处理图像的 Python 代码。

6. **以 Base64 编码图像**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    这段代码读取图像文件，将其编码为 base64，并创建一个带有编码数据的 HTML 图像标签。

7. **将文本和图像合并到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    这段代码将文本提示和 HTML 图像标签合并为一个字符串。

8. **使用 ChatNVIDIA 生成代码**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    这段代码将提示发送给 `ChatNVIDIA` 模型，并收集生成的代码字符串。

9. **从生成的内容中提取 Python 代码**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    这段代码通过移除 markdown 格式，从生成的内容中提取实际的 Python 代码。

10. **运行生成的代码**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    这段代码将提取的 Python 代码作为子进程运行，并捕获其输出。

11. **显示图像**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    这些代码行使用 `IPython.display` 模块显示图像。

**免责声明**:
本文档是使用机器翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档视为权威来源。对于关键信息，建议进行专业的人力翻译。对于因使用此翻译而引起的任何误解或误释，我们概不负责。