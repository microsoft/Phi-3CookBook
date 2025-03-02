### Halimbawa ng Senaryo

Isipin na mayroon kang isang imahe (`demo.png`) at gusto mong gumawa ng Python code na magpoproseso ng imaheng ito at magse-save ng bagong bersyon nito (`phi-3-vision.jpg`).

Ang code sa itaas ay ina-automate ang prosesong ito sa pamamagitan ng:

1. Pagsasaayos ng environment at mga kinakailangang configuration.
2. Paglikha ng prompt na nagbibigay ng instruksyon sa modelo na gumawa ng kinakailangang Python code.
3. Pagpapadala ng prompt sa modelo at pagkolekta ng nabuong code.
4. Pagkuha at pagpapatakbo ng nabuong code.
5. Pagpapakita ng orihinal at naprosesong mga imahe.

Ang pamamaraang ito ay gumagamit ng lakas ng AI upang i-automate ang mga gawain sa pagpoproseso ng imahe, na nagpapadali at nagpapabilis ng pag-abot sa iyong mga layunin.

[Halimbawang Solusyon ng Code](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Tingnan natin ang bawat hakbang ng buong code:

1. **Mag-Install ng Kinakailangang Package**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ang utos na ito ay nag-i-install ng `langchain_nvidia_ai_endpoints` package, tinitiyak na ito ay nasa pinakabagong bersyon.

2. **I-import ang mga Kinakailangang Module**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ang mga import na ito ay nagdadala ng mga kinakailangang module para makipag-ugnayan sa NVIDIA AI endpoints, ligtas na paghawak ng mga password, pakikipag-ugnayan sa operating system, at pag-encode/decoding ng data sa base64 format.

3. **I-set Up ang API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ang code na ito ay nagche-check kung ang environment variable na `NVIDIA_API_KEY` ay naka-set. Kung hindi, hinihiling nito sa user na ligtas na ilagay ang kanilang API key.

4. **I-define ang Model at Path ng Imahe**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Itinatakda nito ang modelong gagamitin, gumagawa ng instance ng `ChatNVIDIA` gamit ang tinukoy na modelo, at itinatakda ang path sa file ng imahe.

5. **Gumawa ng Text Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Tinutukoy nito ang isang text prompt na nagbibigay ng instruksyon sa modelo na gumawa ng Python code para sa pagpoproseso ng imahe.

6. **I-encode ang Imahe sa Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Binabasa ng code na ito ang file ng imahe, ini-encode ito sa base64, at gumagawa ng isang HTML image tag gamit ang encoded data.

7. **Pagsamahin ang Text at Imahe sa Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Pinagsasama nito ang text prompt at ang HTML image tag sa iisang string.

8. **Gumamit ng ChatNVIDIA para Gumawa ng Code**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ang code na ito ay nagpapadala ng prompt sa `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **I-extract ang Python Code mula sa Nabuong Content**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Inaalis nito ang markdown formatting upang makuha ang aktwal na Python code mula sa nabuong content.

10. **Patakbuhin ang Nabuong Code**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Pinapatakbo nito ang nabuong Python code bilang isang subprocess at kinukuha ang output nito.

11. **Ipakita ang mga Imahe**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ang mga linyang ito ay nagpapakita ng mga imahe gamit ang `IPython.display` module.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na batay sa makina. Bagama't pinagsisikapan naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.