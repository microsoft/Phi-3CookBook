# **onnxruntime साठी Generative AI विस्तारांचा वापर करून Phi कुटुंबाचे क्वांटायझेशन**

## **onnxruntime साठी Generative AI विस्तार म्हणजे काय**

हे विस्तार तुम्हाला ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) च्या मदतीने जनरेटिव्ह AI चालवण्यास मदत करतात. हे ONNX मॉडेलसाठी जनरेटिव्ह AI लूप प्रदान करतात, ज्यामध्ये ONNX Runtime सह अनुमान, logits प्रक्रिया, शोध आणि सॅम्पलिंग, आणि KV कॅश व्यवस्थापन यांचा समावेश आहे. विकसक उच्च-स्तरीय generate() पद्धतीला कॉल करू शकतात किंवा मॉडेलच्या प्रत्येक पुनरावृत्ती लूपमध्ये चालवू शकतात, एका वेळी एक टोकन तयार करू शकतात आणि लूपच्या आत जनरेशन पॅरामीटर्स अपडेट करण्याचा पर्याय देखील ठेवू शकतात. हे लोभस/बीम शोध आणि TopP, TopK सॅम्पलिंगसाठी टोकन अनुक्रम तयार करण्यासाठी समर्थन प्रदान करते आणि पुनरावृत्ती दंडांसारख्या अंगभूत logits प्रक्रिया समाविष्ट करते. तुम्ही सहजपणे सानुकूल स्कोअरिंग देखील जोडू शकता.

अ‍ॅप्लिकेशन स्तरावर, तुम्ही C++/ C# / Python वापरून अ‍ॅप्लिकेशन्स तयार करण्यासाठी onnxruntime साठी Generative AI विस्तार वापरू शकता. मॉडेल स्तरावर, तुम्ही त्याचा वापर फाइन-ट्यून केलेली मॉडेल्स मर्ज करण्यासाठी आणि संबंधित क्वांटिटेटिव्ह डिप्लॉयमेंट कार्य करण्यासाठी करू शकता.

## **onnxruntime साठी Generative AI विस्तार वापरून Phi-3.5 चे क्वांटायझेशन**

### **समर्थित मॉडेल्स**

onnxruntime साठी Generative AI विस्तार Microsoft Phi, Google Gemma, Mistral, Meta LLaMA यांसारख्या मॉडेल्सच्या क्वांटायझेशन रूपांतरणास समर्थन देतो।

### **onnxruntime साठी Generative AI विस्तारांमधील मॉडेल बिल्डर**

मॉडेल बिल्डर ONNX Runtime generate() API सह चालणाऱ्या ऑप्टिमाइझ आणि क्वांटायझ केलेल्या ONNX मॉडेल्स तयार करण्याची प्रक्रिया खूप गतीमान करतो.

मॉडेल बिल्डरद्वारे, तुम्ही मॉडेलला INT4, INT8, FP16, FP32 मध्ये क्वांटायझ करू शकता आणि CPU, CUDA, DirectML, Mobile इत्यादीसारख्या वेगवेगळ्या हार्डवेअर प्रवेगक पद्धती एकत्र करू शकता.

मॉडेल बिल्डर वापरण्यासाठी तुम्हाला हे स्थापित करावे लागेल:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

स्थापनेनंतर, तुम्ही मॉडेल फॉरमॅट आणि क्वांटायझेशन रूपांतरण करण्यासाठी टर्मिनलवरून मॉडेल बिल्डर स्क्रिप्ट चालवू शकता.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

संबंधित पॅरामीटर्स समजून घ्या:

1. **model_name** हे Hugging Face वरील मॉडेल आहे, जसे की microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct इत्यादी. हे तुमच्या मॉडेल साठवलेल्या मार्गाचे ठिकाण देखील असू शकते.

2. **path_to_output_folder** क्वांटायझ्ड रूपांतरण जतन करण्याचा मार्ग.

3. **execution_provider** वेगवेगळ्या हार्डवेअर प्रवेगकांसाठी समर्थन, जसे की CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** आम्ही Hugging Face वरून मॉडेल डाउनलोड करतो आणि ते स्थानिक पातळीवर कॅश करतो.

***टीपः***  

## **Phi-3.5 चे क्वांटायझेशन करण्यासाठी मॉडेल बिल्डर कसा वापरायचा**

मॉडेल बिल्डर आता Phi-3.5 Instruct आणि Phi-3.5-Vision साठी ONNX मॉडेल क्वांटायझेशनला समर्थन देतो.

### **Phi-3.5-Instruct**

**क्वांटायझ्ड INT 4 चे CPU प्रवेगित रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**क्वांटायझ्ड INT 4 चे CUDA प्रवेगित रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनलमध्ये पर्यावरण सेट करा:

```bash

mkdir models

cd models 

```

2. मॉडेल्स फोल्डरमध्ये microsoft/Phi-3.5-vision-instruct डाउनलोड करा:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया खालील फाइल्स तुमच्या Phi-3.5-vision-instruct फोल्डरमध्ये डाउनलोड करा:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. खालील फाइल मॉडेल्स फोल्डरमध्ये डाउनलोड करा:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमध्ये जा:

   FP32 सह ONNX समर्थनामध्ये रूपांतरण करा:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **टीपः**

1. मॉडेल बिल्डर सध्या Phi-3.5-Instruct आणि Phi-3.5-Vision चे रूपांतरण समर्थित करतो, परंतु Phi-3.5-MoE चे नाही.

2. ONNX चे क्वांटायझ्ड मॉडेल वापरण्यासाठी, तुम्ही ते onnxruntime साठी Generative AI विस्तार SDK च्या माध्यमातून वापरू शकता.

3. अधिक जबाबदार AI विचारात घेण्यासाठी, मॉडेल क्वांटायझेशन रूपांतरणानंतर अधिक प्रभावी निकाल चाचणी करणे सुचवले जाते.

4. CPU INT4 मॉडेलचे क्वांटायझेशन करून, आपण ते Edge Device वर तैनात करू शकतो, ज्यामध्ये चांगल्या अनुप्रयोग परिस्थिती आहेत. म्हणूनच, आम्ही Phi-3.5-Instruct चे INT 4 च्या आसपासचे काम पूर्ण केले आहे.

## **स्रोत**

1. onnxruntime साठी Generative AI विस्तारांबद्दल अधिक जाणून घ्या:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime साठी Generative AI विस्तार GitHub रेपो:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकृति:**  
हे दस्तऐवज मशीन-आधारित एआय अनुवाद सेवांचा वापर करून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वपूर्ण माहितीसाठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.