### उदाहरण परिदृश्य

कल्पना करें कि आपके पास एक छवि है (`demo.png`) और आप ऐसा Python कोड बनाना चाहते हैं जो इस छवि को प्रोसेस करे और इसका एक नया संस्करण सेव करे (`phi-3-vision.jpg`)।

ऊपर दिया गया कोड इस प्रक्रिया को स्वचालित करता है:

1. पर्यावरण और आवश्यक कॉन्फ़िगरेशन सेट करना।
2. ऐसा प्रॉम्प्ट बनाना जो मॉडल को आवश्यक Python कोड जनरेट करने के लिए निर्देश दे।
3. प्रॉम्प्ट को मॉडल को भेजना और जनरेट किया हुआ कोड प्राप्त करना।
4. जनरेट किए गए कोड को निकालना और चलाना।
5. मूल और प्रोसेस की गई छवियों को प्रदर्शित करना।

यह दृष्टिकोण छवि प्रोसेसिंग कार्यों को स्वचालित करने के लिए AI की शक्ति का उपयोग करता है, जिससे आपके लक्ष्य को हासिल करना आसान और तेज़ हो जाता है।

[नमूना कोड समाधान](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

आइए पूरे कोड को चरण-दर-चरण तोड़कर समझें:

1. **आवश्यक पैकेज इंस्टॉल करें**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    यह कमांड `langchain_nvidia_ai_endpoints` पैकेज को इंस्टॉल करता है और सुनिश्चित करता है कि यह नवीनतम संस्करण है।

2. **आवश्यक मॉड्यूल इंपोर्ट करें**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ये इंपोर्ट NVIDIA AI एंडपॉइंट्स के साथ इंटरैक्ट करने, पासवर्ड को सुरक्षित रूप से संभालने, ऑपरेटिंग सिस्टम के साथ इंटरैक्ट करने, और डेटा को base64 फॉर्मेट में एन्कोड/डिकोड करने के लिए आवश्यक मॉड्यूल लाते हैं।

3. **API कुंजी सेट करें**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    यह कोड जांचता है कि `NVIDIA_API_KEY` पर्यावरण वेरिएबल सेट है या नहीं। यदि नहीं, तो यह उपयोगकर्ता को उनकी API कुंजी सुरक्षित रूप से दर्ज करने के लिए प्रेरित करता है।

4. **मॉडल और छवि पथ परिभाषित करें**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    यह उपयोग किए जाने वाले मॉडल को सेट करता है, निर्दिष्ट मॉडल के साथ `ChatNVIDIA` का एक उदाहरण बनाता है, और छवि फ़ाइल के पथ को परिभाषित करता है।

5. **टेक्स्ट प्रॉम्प्ट बनाएं**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    यह एक टेक्स्ट प्रॉम्प्ट परिभाषित करता है जो मॉडल को छवि प्रोसेस करने के लिए Python कोड जनरेट करने का निर्देश देता है।

6. **छवि को Base64 में एन्कोड करें**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    यह कोड छवि फ़ाइल को पढ़ता है, इसे base64 में एन्कोड करता है, और एन्कोड किए गए डेटा के साथ एक HTML छवि टैग बनाता है।

7. **टेक्स्ट और छवि को प्रॉम्प्ट में मिलाएं**:
    ```python
    prompt = f"{text} {image}"
    ```
    यह टेक्स्ट प्रॉम्प्ट और HTML छवि टैग को एक ही स्ट्रिंग में जोड़ता है।

8. **ChatNVIDIA का उपयोग करके कोड जनरेट करें**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    यह कोड प्रॉम्प्ट को `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` स्ट्रिंग में भेजता है।

9. **जनरेटेड सामग्री से Python कोड निकालें**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    यह जनरेटेड सामग्री से वास्तविक Python कोड को निकालता है और markdown फ़ॉर्मेटिंग को हटा देता है।

10. **जनरेटेड कोड चलाएं**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    यह निकाले गए Python कोड को एक subprocess के रूप में चलाता है और इसका आउटपुट कैप्चर करता है।

11. **छवियों को प्रदर्शित करें**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    ये लाइनें `IPython.display` मॉड्यूल का उपयोग करके छवियों को प्रदर्शित करती हैं।

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।  