### 範例情境

假設你有一張圖片 (`demo.png`)，你想生成處理這張圖片並保存新版本 (`phi-3-vision.jpg`) 的 Python 程式碼。

上面的程式碼自動化了這個過程，具體步驟如下：

1. 設置環境和必要的配置。
2. 創建一個提示，指示模型生成所需的 Python 程式碼。
3. 將提示發送給模型並收集生成的程式碼。
4. 提取並運行生成的程式碼。
5. 顯示原始圖片和處理後的圖片。

這種方法利用 AI 的力量來自動化圖像處理任務，使你更輕鬆快捷地達成目標。

[範例程式碼解決方案](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

讓我們一步一步拆解整個程式碼的功能：

1. **安裝所需套件**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    這條命令安裝 `langchain_nvidia_ai_endpoints` 套件，確保它是最新版本。

2. **導入必要模組**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    這些導入語句引入了與 NVIDIA AI 端點互動、保護密碼、操作系統互動以及 base64 編碼/解碼數據所需的模組。

3. **設置 API 金鑰**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    這段程式碼檢查 `NVIDIA_API_KEY` 環境變量是否已設置。如果沒有，則提示用戶安全地輸入他們的 API 金鑰。

4. **定義模型和圖片路徑**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    這設置了要使用的模型，創建一個 `ChatNVIDIA` 實例並指定模型，並定義圖片文件的路徑。

5. **創建文本提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    這定義了一個文本提示，指示模型生成用於處理圖像的 Python 程式碼。

6. **將圖片編碼為 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'
    ```
    這段程式碼讀取圖片文件，將其編碼為 base64，並創建一個包含編碼數據的 HTML 圖片標籤。

7. **將文本和圖片結合到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    這將文本提示和 HTML 圖片標籤結合成一個字符串。

8. **使用 ChatNVIDIA 生成程式碼**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    這段程式碼將提示發送給 `ChatNVIDIA` 模型，並分塊收集生成的程式碼，打印並追加每個塊到 `code` 字符串。

9. **從生成的內容中提取 Python 程式碼**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    這從生成的內容中提取實際的 Python 程式碼，移除 markdown 格式。

10. **運行生成的程式碼**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    這運行提取的 Python 程式碼作為子進程，並捕獲其輸出。

11. **顯示圖片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    這些行使用 `IPython.display` 模組顯示圖片。

免責聲明：此翻譯是由人工智慧模型從原文翻譯而來，可能不完全準確。請檢查輸出並進行任何必要的修正。