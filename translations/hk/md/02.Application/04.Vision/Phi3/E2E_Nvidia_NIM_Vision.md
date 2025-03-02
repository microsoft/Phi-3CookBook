### 範例場景

假設你有一張圖片 (`demo.png`)，並希望生成處理這張圖片並保存新版本的 Python 程式碼 (`phi-3-vision.jpg`)。

上述程式碼會自動完成以下流程：

1. 設置環境和必要的配置。
2. 建立一個提示，指示模型生成所需的 Python 程式碼。
3. 將提示發送給模型並收集生成的程式碼。
4. 提取並執行生成的程式碼。
5. 顯示原始圖片和處理後的圖片。

這種方法利用 AI 的力量來自動化圖片處理任務，使得達成目標變得更簡單、更快速。

[範例程式碼解決方案](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

讓我們逐步解析整段程式碼的功能：

1. **安裝必要套件**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    這條指令安裝 `langchain_nvidia_ai_endpoints` 套件，並確保是最新版本。

2. **導入必要模組**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    這些導入會引入與 NVIDIA AI 端點互動、安全處理密碼、與作業系統交互，以及以 base64 格式編碼/解碼數據所需的模組。

3. **設置 API 金鑰**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    這段程式碼檢查是否已設置 `NVIDIA_API_KEY` 環境變數。如果沒有，會提示用戶安全地輸入他們的 API 金鑰。

4. **定義模型與圖片路徑**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    這裡設定了要使用的模型，創建了指定模型的 `ChatNVIDIA` 實例，並定義了圖片文件的路徑。

5. **建立文字提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    這段程式碼定義了一個文字提示，指示模型生成用於處理圖片的 Python 程式碼。

6. **將圖片編碼為 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    這段程式碼讀取圖片文件，將其編碼為 base64，並用編碼數據創建一個 HTML 圖片標籤。

7. **將文字與圖片結合到提示中**：
    ```python
    prompt = f"{text} {image}"
    ```
    這裡將文字提示和 HTML 圖片標籤結合成一個字串。

8. **使用 ChatNVIDIA 生成程式碼**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    這段程式碼將提示發送給 `ChatNVIDIA`，並將生成的內容儲存為 `code` 字串。

9. **從生成內容中提取 Python 程式碼**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    這裡透過移除 markdown 格式，提取出實際的 Python 程式碼。

10. **執行生成的程式碼**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    這段程式碼以子程序的方式執行提取出的 Python 程式碼，並捕獲其輸出。

11. **顯示圖片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    這幾行程式碼使用 `IPython.display` 模組來顯示圖片。

**免責聲明**：  
本文件使用機器翻譯人工智能服務進行翻譯。我們雖然努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對於因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。