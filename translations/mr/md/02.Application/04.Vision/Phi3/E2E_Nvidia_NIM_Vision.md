### उदाहरण परिदृश्य

कल्पना करा की तुमच्याकडे एक प्रतिमा आहे (`demo.png`) आणि तुम्हाला Python कोड तयार करायचा आहे जो ही प्रतिमा प्रक्रिया करतो आणि त्याचा एक नवीन आवृत्ती सेव्ह करतो (`phi-3-vision.jpg`).

वरील कोड हा प्रक्रिया स्वयंचलित करण्यासाठी वापरतो:

1. वातावरण आणि आवश्यक कॉन्फिगरेशन सेट करणे.
2. मॉडेलला आवश्यक Python कोड तयार करण्याचे निर्देश देणारा एक प्रॉम्प्ट तयार करणे.
3. प्रॉम्प्ट मॉडेलला पाठवणे आणि तयार केलेला कोड गोळा करणे.
4. तयार केलेला कोड काढणे आणि चालवणे.
5. मूळ आणि प्रक्रिया केलेल्या प्रतिमा दाखवणे.

ही पद्धत AI चा वापर करून प्रतिमा प्रक्रिया कामे स्वयंचलित करण्यासाठी मदत करते, ज्यामुळे तुमचे उद्दिष्ट साध्य करणे सोपे आणि जलद होते.

[नमुन्य कोड समाधान](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

आता आपण संपूर्ण कोड पायरी दर पायरीने समजून घेऊया:

1. **आवश्यक पॅकेज इंस्टॉल करा**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    हा आदेश `langchain_nvidia_ai_endpoints` पॅकेजची नवीनतम आवृत्ती इंस्टॉल करतो.

2. **आवश्यक मॉड्यूल आयात करा**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    हे आयात NVIDIA AI एंडपॉइंट्ससह संवाद साधण्यासाठी, पासवर्ड सुरक्षितपणे हाताळण्यासाठी, ऑपरेटिंग सिस्टमसह संवाद साधण्यासाठी, आणि base64 फॉरमॅटमध्ये डेटा एन्कोड/डिकोड करण्यासाठी आवश्यक मॉड्यूल्स आणतात.

3. **API की सेट करा**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    हा कोड तपासतो की `NVIDIA_API_KEY` पर्यावरणीय व्हेरिएबल सेट आहे की नाही. नसल्यास, तो वापरकर्त्याला त्यांची API की सुरक्षितपणे प्रविष्ट करण्यास सांगतो.

4. **मॉडेल आणि प्रतिमेचा मार्ग निश्चित करा**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    हे वापरण्यासाठी मॉडेल सेट करते, निर्दिष्ट मॉडेलसह `ChatNVIDIA` ची एक उदाहरण तयार करते, आणि प्रतिमा फाइलचा मार्ग परिभाषित करते.

5. **टेक्स्ट प्रॉम्प्ट तयार करा**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    हे मॉडेलला प्रतिमा प्रक्रिया करण्यासाठी Python कोड तयार करण्याचे निर्देश देणारा टेक्स्ट प्रॉम्प्ट परिभाषित करते.

6. **प्रतिमा base64 मध्ये एन्कोड करा**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    हा कोड प्रतिमा फाइल वाचतो, ती base64 मध्ये एन्कोड करतो, आणि एन्कोड केलेल्या डेटासह एक HTML प्रतिमा टॅग तयार करतो.

7. **टेक्स्ट आणि प्रतिमा प्रॉम्प्टमध्ये एकत्र करा**:
    ```python
    prompt = f"{text} {image}"
    ```
    हे टेक्स्ट प्रॉम्प्ट आणि HTML प्रतिमा टॅग एका सिंगल स्ट्रिंगमध्ये एकत्र करते.

8. **ChatNVIDIA वापरून कोड तयार करा**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    हा कोड प्रॉम्प्ट `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` स्ट्रिंगला पाठवतो.

9. **तयार केलेल्या सामग्रीमधून Python कोड काढा**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    हा तयार केलेल्या सामग्रीमधून Markdown स्वरूप काढून वास्तविक Python कोड काढतो.

10. **तयार केलेला कोड चालवा**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    हा काढलेला Python कोड subprocess म्हणून चालवतो आणि त्याचे आउटपुट कॅप्चर करतो.

11. **प्रतिमा दाखवा**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    हे ओळी `IPython.display` मॉड्यूल वापरून प्रतिमा दाखवतात.

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित एआय भाषांतर सेवा वापरून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा प्रामाणिक स्रोत मानावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानव-भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे निर्माण होणाऱ्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थ लावण्यासाठी आम्ही जबाबदार राहणार नाही.