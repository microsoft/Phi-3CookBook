# **Generative AI एक्सटेंशन्स के साथ Phi परिवार को क्वांटाइज़ करना**

## **Generative AI एक्सटेंशन्स क्या है?**

ये एक्सटेंशन्स आपको ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) के साथ जनरेटिव AI चलाने में मदद करते हैं। यह ONNX मॉडल्स के लिए जनरेटिव AI लूप प्रदान करता है, जिसमें ONNX Runtime के साथ इनफरेंस, लॉजिट्स प्रोसेसिंग, सर्च और सैंपलिंग, और KV कैश मैनेजमेंट शामिल हैं। डेवलपर्स हाई-लेवल generate() मेथड का उपयोग कर सकते हैं, या मॉडल के प्रत्येक इटरेशन को लूप में चला सकते हैं, एक समय में एक टोकन जनरेट कर सकते हैं, और लूप के अंदर जनरेशन पैरामीटर्स को वैकल्पिक रूप से अपडेट कर सकते हैं। यह ग्रीडी/बीम सर्च और TopP, TopK सैंपलिंग के लिए सपोर्ट प्रदान करता है ताकि टोकन सीक्वेंस जनरेट किए जा सकें, और रिपीटीशन पेनल्टी जैसे बिल्ट-इन लॉजिट्स प्रोसेसिंग को सपोर्ट करता है। आप आसानी से कस्टम स्कोरिंग भी जोड़ सकते हैं।

एप्लिकेशन स्तर पर, आप C++/C#/Python का उपयोग करके जनरेटिव AI एक्सटेंशन्स का उपयोग करके एप्लिकेशन बना सकते हैं। मॉडल स्तर पर, आप इसे फाइन-ट्यून किए गए मॉडल्स को मर्ज करने और संबंधित क्वांटिटेटिव डिप्लॉयमेंट कार्य करने के लिए उपयोग कर सकते हैं। 

## **Generative AI एक्सटेंशन्स के साथ Phi-3.5 को क्वांटाइज़ करना**

### **सपोर्टेड मॉडल्स**

Generative AI एक्सटेंशन्स Microsoft Phi, Google Gemma, Mistral, Meta LLaMA के क्वांटाइज़ेशन रूपांतरण का समर्थन करता है।

### **Generative AI एक्सटेंशन्स में मॉडल बिल्डर**

मॉडल बिल्डर ONNX Runtime generate() API के साथ चलने वाले अनुकूलित और क्वांटाइज़्ड ONNX मॉडल्स को बनाने की प्रक्रिया को तेज़ करता है। 

मॉडल बिल्डर के माध्यम से, आप मॉडल को INT4, INT8, FP16, FP32 में क्वांटाइज़ कर सकते हैं और CPU, CUDA, DirectML, Mobile जैसे विभिन्न हार्डवेयर एक्सेलेरेशन विधियों को जोड़ सकते हैं।

मॉडल बिल्डर का उपयोग करने के लिए, आपको इसे इंस्टॉल करना होगा:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

इंस्टॉलेशन के बाद, आप टर्मिनल से मॉडल बिल्डर स्क्रिप्ट चला सकते हैं ताकि मॉडल फॉर्मेट और क्वांटाइज़ेशन रूपांतरण किया जा सके।

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

संबंधित पैरामीटर्स को समझें:

1. **model_name** यह Hugging Face पर मॉडल का नाम है, जैसे microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct आदि। यह वह पथ भी हो सकता है जहां आप मॉडल को स्टोर करते हैं।

2. **path_to_output_folder** क्वांटाइज़ रूपांतरण का सेव पथ।

3. **execution_provider** विभिन्न हार्डवेयर एक्सेलेरेशन का समर्थन, जैसे cpu, cuda, DirectML।

4. **cache_dir_to_save_hf_files** हम Hugging Face से मॉडल डाउनलोड करते हैं और इसे लोकल पर कैश करते हैं।

***नोट:***

## **मॉडल बिल्डर का उपयोग करके Phi-3.5 को कैसे क्वांटाइज़ करें**

मॉडल बिल्डर अब Phi-3.5 Instruct और Phi-3.5-Vision के लिए ONNX मॉडल क्वांटाइज़ेशन का समर्थन करता है।

### **Phi-3.5-Instruct**

**क्वांटाइज़ INT4 का CPU-एक्सेलेरेटेड रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**क्वांटाइज़ INT4 का CUDA-एक्सेलेरेटेड रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनल में एनवायरनमेंट सेट करें:

```bash

mkdir models

cd models 

```

2. मॉडल्स फोल्डर में microsoft/Phi-3.5-vision-instruct डाउनलोड करें:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया निम्नलिखित फाइल्स को अपने Phi-3.5-vision-instruct फोल्डर में डाउनलोड करें:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. इस फाइल को मॉडल्स फोल्डर में डाउनलोड करें:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनल पर जाएं:

    FP32 के साथ ONNX सपोर्ट में रूपांतरण करें:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **नोट:**

1. मॉडल बिल्डर फिलहाल Phi-3.5-Instruct और Phi-3.5-Vision के रूपांतरण का समर्थन करता है, लेकिन Phi-3.5-MoE का नहीं।

2. ONNX के क्वांटाइज़ मॉडल का उपयोग करने के लिए, आप इसे Generative AI एक्सटेंशन्स फॉर onnxruntime SDK के माध्यम से उपयोग कर सकते हैं।

3. हमें अधिक जिम्मेदार AI पर विचार करना चाहिए, इसलिए मॉडल क्वांटाइज़ेशन रूपांतरण के बाद, अधिक प्रभावी परिणाम परीक्षण करने की सिफारिश की जाती है।

4. CPU INT4 मॉडल को क्वांटाइज़ करके, हम इसे Edge Device पर डिप्लॉय कर सकते हैं, जो बेहतर एप्लिकेशन परिदृश्य प्रदान करता है। इसलिए, हमने INT4 के आसपास Phi-3.5-Instruct को पूरा किया है।

## **संसाधन**

1. Generative AI एक्सटेंशन्स के बारे में अधिक जानें:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI एक्सटेंशन्स के लिए onnxruntime GitHub रिपोज़िटरी:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।