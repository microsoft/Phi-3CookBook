### ਉਦਾਹਰਨ ਸਨਾਰਿਓ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਚਿੱਤਰ (`demo.png`) ਹੈ ਅਤੇ ਤੁਸੀਂ Python ਕੋਡ ਤਿਆਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਇਸ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਦਾ ਹੈ ਅਤੇ ਇਸਦੀ ਨਵੀਂ ਵਰਜਨ ਨੂੰ ਸੇਵ ਕਰਦਾ ਹੈ (`phi-3-vision.jpg`)।

ਉਪਰੋਕਤ ਕੋਡ ਇਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ:

1. ਵਾਤਾਵਰਣ ਅਤੇ ਜ਼ਰੂਰੀ ਸੰਰਚਨਾਵਾਂ ਸੈਟ ਕਰਨਾ।
2. ਇੱਕ ਪ੍ਰਾਂਪਟ ਬਣਾਉਣਾ ਜੋ ਮਾਡਲ ਨੂੰ ਲੋੜੀਂਦੇ Python ਕੋਡ ਤਿਆਰ ਕਰਨ ਲਈ ਨਿਰਦੇਸ਼ ਦਿੰਦਾ ਹੈ।
3. ਪ੍ਰਾਂਪਟ ਨੂੰ ਮਾਡਲ ਨੂੰ ਭੇਜਣਾ ਅਤੇ ਤਿਆਰ ਕੀਤਾ ਕੋਡ ਇਕੱਠਾ ਕਰਨਾ।
4. ਤਿਆਰ ਕੀਤੇ ਕੋਡ ਨੂੰ ਕੱਢਣਾ ਅਤੇ ਚਲਾਉਣਾ।
5. ਮੂਲ ਅਤੇ ਪ੍ਰਕਿਰਿਆ ਕੀਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਦਿਖਾਉਣਾ।

ਇਹ ਪਹੁੰਚ AI ਦੀ ਸ਼ਕਤੀ ਦਾ ਲਾਭ ਉਠਾਉਂਦੀ ਹੈ ਤਾਂ ਜੋ ਚਿੱਤਰ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਵਾਲੇ ਕੰਮਾਂ ਨੂੰ ਆਸਾਨ ਅਤੇ ਤੇਜ਼ ਬਣਾਇਆ ਜਾ ਸਕੇ। 

[ਨਮੂਨਾ ਕੋਡ ਹੱਲ](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

ਆਓ ਪੂਰੇ ਕੋਡ ਨੂੰ ਕਦਮ ਦਰ ਕਦਮ ਤੋੜ ਕੇ ਸਮਝੀਏ:

1. **ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    ਇਹ ਕਮਾਂਡ `langchain_nvidia_ai_endpoints` ਪੈਕੇਜ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦੀ ਹੈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀਆਂ ਕਿ ਇਹ ਨਵੀਂਤਮ ਵਰਜਨ ਹੈ।

2. **ਜ਼ਰੂਰੀ ਮਾਡਿਊਲਸ ਇੰਪੋਰਟ ਕਰੋ**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ਇਹ ਇੰਪੋਰਟ NVIDIA AI ਐਂਡਪੋਇੰਟਸ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਨ, ਪਾਸਵਰਡ ਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਣ, ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨਾਲ ਇੰਟਰਐਕਟ ਕਰਨ, ਅਤੇ ਡਾਟਾ ਨੂੰ base64 ਫਾਰਮੈਟ ਵਿੱਚ ਐਨਕੋਡ/ਡੀਕੋਡ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਮਾਡਿਊਲਸ ਨੂੰ ਲਿਆਉਂਦੇ ਹਨ।

3. **API ਕੁੰਜੀ ਸੈਟ ਕਰੋ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    ਇਹ ਕੋਡ ਜਾਂਚਦਾ ਹੈ ਕਿ ਕੀ `NVIDIA_API_KEY` ਐਨਵਾਇਰਮੈਂਟ ਵੇਰੀਏਬਲ ਸੈਟ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ ਇਹ ਯੂਜ਼ਰ ਨੂੰ ਆਪਣੀ API ਕੁੰਜੀ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਦਾਖਲ ਕਰਨ ਲਈ ਕਹਿੰਦਾ ਹੈ।

4. **ਮਾਡਲ ਅਤੇ ਚਿੱਤਰ ਦਾ ਪਾਥ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    ਇਹ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਮਾਡਲ ਨੂੰ ਸੈਟ ਕਰਦਾ ਹੈ, `ChatNVIDIA` ਦਾ ਇੱਕ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਨਿਰਧਾਰਿਤ ਮਾਡਲ ਹੈ, ਅਤੇ ਚਿੱਤਰ ਫਾਈਲ ਦੇ ਪਾਥ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ।

5. **ਪਾਠ ਪ੍ਰਾਂਪਟ ਬਣਾਓ**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    ਇਹ ਇੱਕ ਪਾਠ ਪ੍ਰਾਂਪਟ ਤਿਆਰ ਕਰਦਾ ਹੈ ਜੋ ਮਾਡਲ ਨੂੰ ਚਿੱਤਰ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਲਈ Python ਕੋਡ ਤਿਆਰ ਕਰਨ ਲਈ ਨਿਰਦੇਸ਼ ਦਿੰਦਾ ਹੈ।

6. **ਚਿੱਤਰ ਨੂੰ Base64 ਵਿੱਚ ਐਨਕੋਡ ਕਰੋ**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    ਇਹ ਕੋਡ ਚਿੱਤਰ ਫਾਈਲ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ, ਇਸਨੂੰ base64 ਵਿੱਚ ਐਨਕੋਡ ਕਰਦਾ ਹੈ, ਅਤੇ ਐਨਕੋਡ ਕੀਤੇ ਡਾਟਾ ਨਾਲ ਇੱਕ HTML ਚਿੱਤਰ ਟੈਗ ਬਣਾਉਂਦਾ ਹੈ।

7. **ਪਾਠ ਅਤੇ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਜੋੜੋ**:
    ```python
    prompt = f"{text} {image}"
    ```
    ਇਹ ਪਾਠ ਪ੍ਰਾਂਪਟ ਅਤੇ HTML ਚਿੱਤਰ ਟੈਗ ਨੂੰ ਇੱਕ ਸਿੰਗਲ ਸਤਰ ਵਿੱਚ ਜੋੜਦਾ ਹੈ।

8. **ChatNVIDIA ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੋਡ ਤਿਆਰ ਕਰੋ**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    ਇਹ ਕੋਡ ਪ੍ਰਾਂਪਟ ਨੂੰ `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` ਸਤਰ ਨੂੰ ਭੇਜਦਾ ਹੈ।

9. **ਤਿਆਰ ਕੀਤੇ ਸਮੱਗਰੀ ਤੋਂ Python ਕੋਡ ਕੱਢੋ**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    ਇਹ ਤਿਆਰ ਕੀਤੇ ਸਮੱਗਰੀ ਵਿੱਚੋਂ ਅਸਲ Python ਕੋਡ ਨੂੰ ਕੱਢਦਾ ਹੈ ਅਤੇ ਮਾਰਕਡਾਊਨ ਫਾਰਮੈਟਿੰਗ ਨੂੰ ਹਟਾਉਂਦਾ ਹੈ।

10. **ਤਿਆਰ ਕੀਤਾ ਕੋਡ ਚਲਾਓ**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    ਇਹ ਤਿਆਰ ਕੀਤੇ Python ਕੋਡ ਨੂੰ ਇੱਕ subprocess ਵਜੋਂ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਇਸ ਦਾ ਆਉਟਪੁੱਟ ਕੈਪਚਰ ਕਰਦਾ ਹੈ।

11. **ਚਿੱਤਰ ਦਿਖਾਓ**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    ਇਹ ਲਾਈਨਾਂ `IPython.display` ਮਾਡਿਊਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਨੂੰ ਦਿਖਾਉਂਦੀਆਂ ਹਨ।

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਚੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਨਾਲ ਉਤਪੰਨ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।