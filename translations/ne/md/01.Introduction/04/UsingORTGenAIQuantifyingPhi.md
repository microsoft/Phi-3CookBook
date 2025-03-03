# **Generative AI extensions for onnxruntime प्रयोग गरेर Phi परिवारलाई क्वान्टाइज गर्ने**

## **Generative AI extensions for onnxruntime भनेको के हो?**

यो एक्स्टेन्सनले ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) प्रयोग गरेर जनरेटिभ AI चलाउन मद्दत गर्दछ। यसले ONNX मोडेलहरूको लागि जनरेटिभ AI लूप प्रदान गर्दछ, जसमा ONNX Runtime मार्फत इनफरेन्स, logits प्रोसेसिङ, सर्च र स्याम्पलिङ, र KV क्याच व्यवस्थापन समावेश छ। डेभलपरहरूले उच्च-स्तरको generate() मेथड प्रयोग गर्न सक्छन्, वा मोडेलको प्रत्येक पुनरावृत्ति लूपमा चलाउन सक्छन्, एक पटकमा एउटा टोकन जेनेरेट गर्दै, र लूपभित्र जेनेरेसन प्यारामिटरहरू अपडेट गर्न सक्ने सुविधा पनि उपलब्ध छ। यसले greedy/beam search र TopP, TopK स्याम्पलिङलाई सपोर्ट गर्दछ जसले टोकन सिक्वेन्सहरू जेनेरेट गर्दछ, साथै repetition penalties जस्ता बिल्ट-इन logits प्रोसेसिङ पनि उपलब्ध छ। तपाईं सजिलैसँग कस्टम स्कोरिङ पनि थप्न सक्नुहुन्छ।

एप्लिकेसन स्तरमा, तपाईं C++/C#/Python प्रयोग गरेर एप्लिकेसनहरू बनाउन Generative AI extensions for onnxruntime प्रयोग गर्न सक्नुहुन्छ। मोडेल स्तरमा, तपाईं यसलाई प्रयोग गरेर फाइन-ट्युन गरिएको मोडेलहरू मर्ज गर्न र सम्बन्धित परिमाणात्मक डिप्लोइमेन्ट कार्यहरू गर्न सक्नुहुन्छ।

## **Generative AI extensions for onnxruntime प्रयोग गरेर Phi-3.5 क्वान्टाइज गर्ने**

### **सपोर्ट मोडेलहरू**

Generative AI extensions for onnxruntime ले Microsoft Phi, Google Gemma, Mistral, Meta LLaMA को क्वान्टाइजेसन कन्भर्जनलाई सपोर्ट गर्दछ।

### **Generative AI extensions for onnxruntime मा मोडेल बिल्डर**

मोडेल बिल्डरले ONNX Runtime generate() API सँग चल्ने, अप्टिमाइज गरिएको र क्वान्टाइज गरिएको ONNX मोडेल निर्माण गर्ने प्रक्रिया तीव्र बनाउँछ।

मोडेल बिल्डरमार्फत, तपाईं मोडेललाई INT4, INT8, FP16, FP32 मा क्वान्टाइज गर्न सक्नुहुन्छ, र CPU, CUDA, DirectML, Mobile जस्ता विभिन्न हार्डवेयर एक्सेलेरेसन विधिहरूलाई संयोजन गर्न सक्नुहुन्छ।

मोडेल बिल्डर प्रयोग गर्न तपाईंले निम्न स्थापना गर्नुपर्छ:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

स्थापना पछि, तपाईं टर्मिनलबाट मोडेल बिल्डर स्क्रिप्ट चलाएर मोडेल फर्म्याट र क्वान्टाइजेसन कन्भर्जन गर्न सक्नुहुन्छ।

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

सम्बन्धित प्यारामिटरहरू बुझ्नुहोस्:

1. **model_name** यो Hugging Face मा रहेको मोडेल हो, जस्तै microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct आदि। यो तपाईंले मोडेल स्टोर गरेको पथ पनि हुन सक्छ।

2. **path_to_output_folder** क्वान्टाइज गरिएको कन्भर्जनको सेभ गर्ने पथ।

3. **execution_provider** CPU, CUDA, DirectML जस्ता विभिन्न हार्डवेयर एक्सेलेरेसन सपोर्ट।

4. **cache_dir_to_save_hf_files** हामी Hugging Face बाट मोडेल डाउनलोड गरी स्थानीय रूपमा क्याच गर्छौं।

***नोटः***

## **Phi-3.5 क्वान्टाइज गर्न मोडेल बिल्डर कसरी प्रयोग गर्ने**

मोडेल बिल्डरले अहिले Phi-3.5 Instruct र Phi-3.5-Vision को लागि ONNX मोडेल क्वान्टाइजेसनलाई सपोर्ट गर्दछ।

### **Phi-3.5-Instruct**

**CPU एक्सेलेरेटेड INT4 क्वान्टाइजेसन कन्भर्जन**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA एक्सेलेरेटेड INT4 क्वान्टाइजेसन कन्भर्जन**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनलमा वातावरण सेट गर्नुहोस्।

```bash

mkdir models

cd models 

```

2. models फोल्डरमा microsoft/Phi-3.5-vision-instruct डाउनलोड गर्नुहोस्।  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. यी फाइलहरू तपाईंको Phi-3.5-vision-instruct फोल्डरमा डाउनलोड गर्नुहोस्:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. यो फाइल models फोल्डरमा डाउनलोड गर्नुहोस्:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमा जानुहोस्।

   FP32 सपोर्टसहितको ONNX मा रूपान्तरण गर्नुहोस्।

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **नोटः**

1. मोडेल बिल्डरले अहिले Phi-3.5-Instruct र Phi-3.5-Vision को रूपान्तरणलाई मात्र सपोर्ट गर्दछ, तर Phi-3.5-MoE लाई सपोर्ट गर्दैन।

2. ONNX को क्वान्टाइज गरिएको मोडेल प्रयोग गर्न, तपाईं यसलाई Generative AI extensions for onnxruntime SDK मार्फत प्रयोग गर्न सक्नुहुन्छ।

3. हामीले जिम्मेवार AI को बारेमा ध्यान दिनुपर्छ, त्यसैले मोडेल क्वान्टाइजेसन रूपान्तरण पछि, प्रभावकारी नतिजा परीक्षण गर्न सिफारिस गरिन्छ।

4. CPU INT4 मोडेललाई क्वान्टाइज गरेर, हामी यसलाई Edge Device मा डिप्लोय गर्न सक्छौं, जसले राम्रो एप्लिकेसन परिदृश्यहरू प्रदान गर्दछ। त्यसैले, हामीले Phi-3.5-Instruct लाई INT4 मा केन्द्रित गरेर पूरा गरेका छौं।

## **स्रोतहरू**

1. Generative AI extensions for onnxruntime को बारेमा थप जान्नुहोस्: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime को GitHub Repo: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरी अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गरिरहेका छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा असंगतिहरू हुन सक्छ। यसको मौलिक भाषा भएको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुनेछैनौं।