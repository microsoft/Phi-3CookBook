### Misali Senaryo

Tunan ka da hoton (`demo.png`) kuma kana son samar da lambar Python da za ta sarrafa wannan hoto kuma ta ajiye sabon sigar sa (`phi-3-vision.jpg`).

Lambar da ke sama tana sarrafa wannan tsari ta hanyar:

1. Sanya yanayi da kuma duk wasu saituna da ake bukata.
2. Kirkirar umarni wanda zai ba samfurin umarnin samar da lambar Python da ake bukata.
3. Tura umarnin zuwa ga samfurin sannan tattara lambar da aka samar.
4. Fitar da lambar da aka samar sannan gudanar da ita.
5. Nuna hoton asali da wanda aka sarrafa.

Wannan hanya tana amfani da karfin AI wajen sarrafa ayyukan sarrafa hoto, tana mai saukakewa da sauri wajen cimma burinka.

[Misalin Maganin Lamba](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Bari mu duba abin da duk lambar take yi mataki-mataki:

1. **Shigar da Kunshin da ake Bukata**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Wannan umarnin yana shigar da kunshin `langchain_nvidia_ai_endpoints`, yana tabbatar da cewa an yi amfani da sabon sigar sa.

2. **Shigo da Mahimman Modules**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Wadannan suna kawo modules masu mahimmanci don mu'amala da tashoshin NVIDIA AI, sarrafa kalmomin shiga cikin tsaro, mu'amala da tsarin aiki, da kuma loda/fitar da bayanai a cikin tsarin base64.

3. **Saita API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Wannan lambar tana tabbatar da cewa an saita maɓallin `NVIDIA_API_KEY` a yanayin tsarin. Idan ba haka ba, tana tambayar mai amfani don shigar da maɓallin API cikin tsaro.

4. **Bayyana Samfuri da Hanyar Hoto**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Wannan yana saita samfurin da za a yi amfani da shi, yana kirkirar wani abu na `ChatNVIDIA` tare da samfurin da aka bayyana, sannan yana bayyana hanyar fayil din hoton.

5. **Kirkirar Umarnin Rubutu**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Wannan yana bayyana wani umarnin rubutu wanda yake ba samfurin umarnin samar da lambar Python don sarrafa hoto.

6. **Loda Hoto a Tsarin Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Wannan lambar tana karanta fayil din hoto, tana loda shi a cikin tsarin base64, sannan tana kirkirar tag ɗin HTML na hoto tare da bayanan da aka loda.

7. **Hada Rubutu da Hoto a cikin Umarnin**:
    ```python
    prompt = f"{text} {image}"
    ```
    Wannan yana haɗa rubutun umarni da tag ɗin HTML na hoto a cikin igiyar rubutu guda.

8. **Samar da Lamba Ta Amfani da ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Wannan lambar tana tura umarnin zuwa ga `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Fitar da Lambar Python Daga Abun da Aka Samar**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Wannan yana fitar da ainihin lambar Python daga abun da aka samar ta hanyar cire tsarin markdown.

10. **Gudanar da Lambar da Aka Samar**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Wannan tana gudanar da lambar Python da aka fitar a matsayin wani subprocess sannan tana tattara sakamakon.

11. **Nuna Hotuna**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Wadannan layukan suna nuna hotunan ta amfani da `IPython.display` module.

It seems like you're asking for a translation into "mo," but it's unclear what "mo" refers to. Could you clarify the language or dialect you're requesting? For example, are you referring to Maori, Mongolian, or something else? Let me know so I can assist you accurately!