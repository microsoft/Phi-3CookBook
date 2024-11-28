### Example Scenario

想像一下你有一張圖片 (`demo.png`)，並且你想生成 Python 程式碼來處理這張圖片並保存其新版本 (`phi-3-vision.jpg`)。

上面的程式碼自動化了這個過程：

1. 設置環境和必要的配置。
2. 創建一個提示，指示模型生成所需的 Python 程式碼。
3. 將提示發送給模型並收集生成的程式碼。
4. 提取並運行生成的程式碼。
5. 顯示原始和處理後的圖片。

這種方法利用 AI 的力量自動化圖像處理任務，使你更輕鬆快速地實現目標。

[Sample Code Solution](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

讓我們一步一步地解析整個程式碼的作用：

1. **安裝所需套件**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    此命令安裝 `langchain_nvidia_ai_endpoints` 套件，確保其為最新版本。

2. **導入必要的模組**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    這些導入將帶入與 NVIDIA AI 端點互動、安全處理密碼、與操作系統互動以及以 base64 格式編碼/解碼數據所需的模組。

3. **設置 API 密鑰**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    此程式碼檢查是否設置了 `NVIDIA_API_KEY` 環境變量。如果沒有，它會提示用戶安全地輸入他們的 API 密鑰。

4. **定義模型和圖片路徑**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    這設置了要使用的模型，創建了 `ChatNVIDIA` 的實例，並定義了圖片文件的路徑。

5. **創建文本提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    這定義了一個文本提示，指示模型生成用於處理圖片的 Python 程式碼。

6. **將圖片編碼為 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    這段程式碼讀取圖片文件，將其編碼為 base64，並創建一個帶有編碼數據的 HTML 圖片標籤。

7. **將文本和圖片結合成提示**：
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
    這段程式碼將提示發送給 `ChatNVIDIA` 並收集生成的程式碼字符串。

9. **從生成的內容中提取 Python 程式碼**：
    ```python
    begin = code.index('```
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    這通過去除 markdown 格式提取實際的 Python 程式碼。

10. **運行生成的程式碼**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    這將提取的 Python 程式碼作為子進程運行並捕獲其輸出。

11. **顯示圖片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    這些行使用 `IPython.display` 模組顯示圖片。

**免責聲明**：
本文件已使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件作為權威來源。對於關鍵信息，建議進行專業的人類翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。