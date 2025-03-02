### Mfano wa Hali

Fikiria una picha (`demo.png`) na unataka kuzalisha msimbo wa Python ambao unashughulikia picha hii na kuhifadhi toleo jipya la picha hiyo (`phi-3-vision.jpg`).

Msimbo hapo juu unarahisisha mchakato huu kwa:

1. Kuandaa mazingira na mipangilio inayohitajika.
2. Kuunda maelekezo yanayomwelekeza mfano kuzalisha msimbo wa Python unaohitajika.
3. Kutuma maelekezo hayo kwa mfano na kukusanya msimbo uliotengenezwa.
4. Kuchukua na kuendesha msimbo uliotengenezwa.
5. Kuonyesha picha ya awali na ile iliyoshughulikiwa.

Njia hii inatumia uwezo wa AI kurahisisha kazi za usindikaji wa picha, na kufanya iwe rahisi na haraka kufanikisha malengo yako.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Tuchambue kile msimbo mzima unafanya hatua kwa hatua:

1. **Sakinisha Kifurushi Kinachohitajika**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Amri hii inasakinisha kifurushi cha `langchain_nvidia_ai_endpoints`, kuhakikisha kuwa ni toleo la hivi karibuni.

2. **Ingiza Moduli Zilizohitajika**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Uingizaji huu huleta moduli zinazohitajika kwa ajili ya kuingiliana na sehemu za mwisho za NVIDIA AI, kushughulikia nywila kwa usalama, kuingiliana na mfumo wa uendeshaji, na kusimba/kufasiri data kwa muundo wa base64.

3. **Sanidi API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Msimbo huu hukagua kama mazingira ya `NVIDIA_API_KEY` yamewekwa. Ikiwa hayapo, humuomba mtumiaji kuingiza API key yao kwa usalama.

4. **Taja Modeli na Njia ya Picha**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Hii huweka mfano wa kutumika, huunda mfano wa `ChatNVIDIA` na modeli maalum, na hufafanua njia ya faili la picha.

5. **Unda Maelekezo ya Maandishi**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Hii hufafanua maelekezo ya maandishi yanayoelekeza mfano kuzalisha msimbo wa Python wa kushughulikia picha.

6. **Fasiri Picha kwa Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Msimbo huu husoma faili la picha, hufasiri kwa base64, na huunda lebo ya HTML ya picha iliyo na data iliyosimbwa.

7. **Unganisha Maandishi na Picha kwenye Maelekezo**:
    ```python
    prompt = f"{text} {image}"
    ```
    Hii huunganisha maelekezo ya maandishi na lebo ya HTML ya picha kuwa kamba moja.

8. **Zalisha Msimbo kwa Kutumia ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Msimbo huu hutuma maelekezo kwa `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Chukua Msimbo wa Python kutoka kwa Yaliyotengenezwa**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Hii huchukua msimbo halisi wa Python kutoka kwa yaliyotengenezwa kwa kuondoa muundo wa markdown.

10. **Endesha Msimbo Uliotengenezwa**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Hii huendesha msimbo wa Python uliotolewa kama subprocess na kunasa matokeo yake.

11. **Onyesha Picha**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Mistari hii huonyesha picha kwa kutumia moduli ya `IPython.display`.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo rasmi. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.