### 示例场景

假设你有一张图片 (`demo.png`)，你想生成处理这张图片并保存新版本 (`phi-3-vision.jpg`) 的Python代码。

上面的代码自动化了这个过程：

1. 设置环境和必要的配置。
2. 创建一个提示，指示模型生成所需的Python代码。
3. 将提示发送给模型并收集生成的代码。
4. 提取并运行生成的代码。
5. 显示原始和处理后的图片。

这种方法利用AI的力量来自动化图像处理任务，使你更轻松快捷地实现目标。

[示例代码解决方案](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

让我们逐步分解整个代码的功能：

1. **安装所需的包**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    这个命令安装`langchain_nvidia_ai_endpoints`包，确保它是最新版本。

2. **导入必要的模块**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    这些导入引入了与NVIDIA AI端点交互、安全处理密码、与操作系统交互以及以base64格式编码/解码数据所需的模块。

3. **设置API密钥**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    这段代码检查`NVIDIA_API_KEY`环境变量是否已设置。如果没有，它会提示用户安全地输入他们的API密钥。

4. **定义模型和图片路径**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    这设置了要使用的模型，创建了一个带有指定模型的`ChatNVIDIA`实例，并定义了图片文件的路径。

5. **创建文本提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    这定义了一个文本提示，指示模型生成用于处理图片的Python代码。

6. **将图片编码为Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'
    ```
    这段代码读取图片文件，将其编码为base64，并创建一个带有编码数据的HTML图片标签。

7. **将文本和图片合并为提示**：
    ```python
    prompt = f"{text} {image}"
    ```
    这将文本提示和HTML图片标签合并为一个字符串。

8. **使用ChatNVIDIA生成代码**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    这段代码将提示发送给`ChatNVIDIA`模型，并分块收集生成的代码，打印并将每个块附加到`code`字符串。

9. **从生成的内容中提取Python代码**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    这段代码通过去除Markdown格式提取实际的Python代码。

10. **运行生成的代码**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    这段代码以子进程的形式运行提取的Python代码，并捕获其输出。

11. **显示图片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    这些行使用`IPython.display`模块显示图片。

免责声明：本翻译由AI模型从原文翻译而来，可能不够完美。请审核输出内容并进行必要的修正。