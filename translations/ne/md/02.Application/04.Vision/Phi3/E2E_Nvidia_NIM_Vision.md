### उदाहरण परिदृश्य

कल्पना गर्नुहोस् कि तपाईंसँग एउटा छवि छ (`demo.png`) र तपाईं यस छविलाई प्रोसेस गर्ने र यसको नयाँ संस्करण सुरक्षित गर्ने Python कोड उत्पादन गर्न चाहनुहुन्छ (`phi-3-vision.jpg`)।

माथिको कोडले यो प्रक्रिया स्वचालित गर्दछ:

1. वातावरण र आवश्यक कन्फिगरेसन सेटअप गर्ने।
2. मोडेललाई आवश्यक Python कोड उत्पादन गर्न निर्देशन दिने एउटा प्रॉम्प्ट बनाउने।
3. प्रॉम्प्टलाई मोडेलमा पठाउने र उत्पन्न भएको कोड सङ्कलन गर्ने।
4. उत्पन्न कोड निकाल्ने र चलाउने।
5. मूल र प्रोसेस गरिएका छविहरू प्रदर्शन गर्ने।

यो विधिले छवि प्रोसेसिङ कार्यहरू स्वचालित गर्न AI को शक्तिलाई उपयोग गर्छ, जसले गर्दा तपाईंका लक्ष्यहरू छिटो र सजिलै प्राप्त गर्न मद्दत गर्दछ।

[नमूना कोड समाधान](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

अब, सम्पूर्ण कोड के गर्छ भन्ने कुरा चरणबद्ध रूपमा बुझौँ:

1. **आवश्यक प्याकेज स्थापना गर्नुहोस्**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    यो कमाण्डले `langchain_nvidia_ai_endpoints` प्याकेज स्थापना गर्दछ, यो सुनिश्चित गर्दै कि यो नवीनतम संस्करण हो।

2. **आवश्यक मोड्युलहरू आयात गर्नुहोस्**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    यी आयातहरूले NVIDIA AI endpoints सँग अन्तरक्रिया गर्न, पासवर्ड सुरक्षित रूपमा ह्यान्डल गर्न, अपरेटिङ सिस्टमसँग अन्तरक्रिया गर्न, र base64 फर्म्याटमा डेटा एन्कोड/डिकोड गर्न आवश्यक मोड्युलहरू ल्याउँछन्।

3. **API कुञ्जी सेट गर्नुहोस्**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    यो कोडले `NVIDIA_API_KEY` वातावरण चर सेट गरिएको छ कि छैन जाँच्छ। यदि छैन भने, यो प्रयोगकर्तालाई सुरक्षित रूपमा आफ्नो API कुञ्जी प्रविष्ट गर्न संकेत गर्दछ।

4. **मोडेल र छवि पथ परिभाषित गर्नुहोस्**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    यसले प्रयोग गर्नुपर्ने मोडेल सेट गर्दछ, निर्दिष्ट मोडेलसँग `ChatNVIDIA` को उदाहरण सिर्जना गर्दछ, र छवि फाइलको पथ परिभाषित गर्दछ।

5. **पाठ प्रॉम्प्ट बनाउनुहोस्**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    यसले मोडेललाई छवि प्रोसेस गर्न Python कोड उत्पादन गर्न निर्देशन दिने पाठ प्रॉम्प्ट परिभाषित गर्दछ।

6. **छविलाई Base64 मा एन्कोड गर्नुहोस्**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    यो कोडले छवि फाइल पढ्छ, यसलाई base64 मा एन्कोड गर्दछ, र एन्कोड गरिएको डाटासँग HTML छवि ट्याग बनाउँछ।

7. **पाठ र छविलाई प्रॉम्प्टमा संयोजन गर्नुहोस्**:
    ```python
    prompt = f"{text} {image}"
    ```
    यसले पाठ प्रॉम्प्ट र HTML छवि ट्यागलाई एउटै स्ट्रिङमा संयोजन गर्छ।

8. **ChatNVIDIA प्रयोग गरेर कोड उत्पादन गर्नुहोस्**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    यो कोडले प्रॉम्प्टलाई `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` स्ट्रिङमा पठाउँछ।

9. **उत्पन्न सामग्रीबाट Python कोड निकाल्नुहोस्**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    यसले Markdown फर्म्याट हटाएर उत्पन्न सामग्रीबाट वास्तविक Python कोड निकाल्छ।

10. **उत्पन्न कोड चलाउनुहोस्**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    यसले निकालिएको Python कोडलाई सबप्रोसेसको रूपमा चलाउँछ र यसको आउटपुट क्याप्चर गर्छ।

11. **छविहरू प्रदर्शन गर्नुहोस्**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    यी पङ्क्तिहरूले `IPython.display` मोड्युल प्रयोग गरेर छविहरू प्रदर्शन गर्छ।

**अस्वीकरण**:  
यो दस्तावेज मेशिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। यद्यपि हामी शुद्धताका लागि प्रयास गर्दछौं, कृपया सचेत रहनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल भाषामा रहेको मूल दस्तावेजलाई प्रामाणिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यो अनुवाद प्रयोग गर्दा उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी उत्तरदायी हुनेछैनौं।  