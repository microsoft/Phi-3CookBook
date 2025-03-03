### 範例情境

假設你有一張圖片 (`demo.png`)，你希望生成一段處理這張圖片並儲存新版本的 Python 程式碼 (`phi-3-vision.jpg`)。

上述程式碼自動化了這個過程，其步驟如下：

1. 設定環境和必要的配置。
2. 建立一個提示，用來指導模型生成所需的 Python 程式碼。
3. 將提示發送給模型並收集生成的程式碼。
4. 提取並執行生成的程式碼。
5. 顯示原始圖片和處理後的圖片。

這種方法利用了 AI 的強大功能來自動化圖片處理任務，使目標的實現變得更加簡單快捷。

[範例程式碼解決方案](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

以下是對整段程式碼的逐步解析：

1. **安裝所需套件**：
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    這條指令安裝了 `langchain_nvidia_ai_endpoints` 套件，並確保是最新版本。

2. **匯入必要模組**：
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    這些匯入帶入了與 NVIDIA AI 端點互動、安全處理密碼、操作系統互動，以及以 base64 格式編碼/解碼資料所需的模組。

3. **設定 API 金鑰**：
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    這段程式碼檢查 `NVIDIA_API_KEY` 環境變數是否已設定。如果未設定，則提示使用者安全地輸入其 API 金鑰。

4. **定義模型與圖片路徑**：
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    這裡設定了將使用的模型，建立了一個指定模型的 `ChatNVIDIA` 實例，並定義了圖片檔案的路徑。

5. **建立文字提示**：
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    這段程式碼定義了一個文字提示，指導模型生成用於處理圖片的 Python 程式碼。

6. **將圖片編碼為 Base64**：
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    這段程式碼讀取圖片檔案，將其編碼為 Base64，並建立一個帶有編碼資料的 HTML 圖片標籤。

7. **將文字和圖片結合為提示**：
    ```python
    prompt = f"{text} {image}"
    ```
    這裡將文字提示和 HTML 圖片標籤結合為單一字串。

8. **使用 ChatNVIDIA 生成程式碼**：
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    這段程式碼將提示發送給 `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` 字串。

9. **從生成內容中提取 Python 程式碼**：
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    這段程式碼透過移除 Markdown 格式，提取生成內容中的實際 Python 程式碼。

10. **執行生成的程式碼**：
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    這段程式碼將提取的 Python 程式碼作為子程序執行，並捕獲其輸出。

11. **顯示圖片**：
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    這些程式碼行使用 `IPython.display` 模組來顯示圖片。

**免責聲明**：  
本文件是使用基於機器的人工智能翻譯服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議使用專業的人工作翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋概不負責。