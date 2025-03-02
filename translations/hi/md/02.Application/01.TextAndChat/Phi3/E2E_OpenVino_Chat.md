[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

यह कोड एक मॉडल को OpenVINO फॉर्मेट में एक्सपोर्ट करता है, उसे लोड करता है, और दिए गए प्रॉम्प्ट के आधार पर प्रतिक्रिया उत्पन्न करता है। 

1. **मॉडल को एक्सपोर्ट करना**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - यह कमांड `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` का उपयोग करता है।

2. **आवश्यक लाइब्रेरी इंपोर्ट करना**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - इन लाइनों में `transformers` library and the `optimum.intel.openvino` मॉड्यूल से क्लासेस इंपोर्ट की जाती हैं, जो मॉडल को लोड और उपयोग करने के लिए आवश्यक हैं।

3. **मॉडल डायरेक्टरी और कॉन्फ़िगरेशन सेट करना**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` एक डिक्शनरी है जो OpenVINO मॉडल को लो लेटेंसी प्राथमिकता देने, एक इनफेरेंस स्ट्रीम का उपयोग करने, और कैश डायरेक्टरी का उपयोग न करने के लिए कॉन्फ़िगर करती है।

4. **मॉडल को लोड करना**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - यह लाइन निर्दिष्ट डायरेक्टरी से मॉडल को लोड करती है, और पहले से परिभाषित कॉन्फ़िगरेशन सेटिंग्स का उपयोग करती है। यह आवश्यकता पड़ने पर रिमोट कोड निष्पादन की अनुमति भी देती है।

5. **टोकनाइज़र को लोड करना**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - यह लाइन टोकनाइज़र को लोड करती है, जो टेक्स्ट को ऐसे टोकन में बदलने के लिए जिम्मेदार होता है जिसे मॉडल समझ सके।

6. **टोकनाइज़र आर्गुमेंट्स सेट करना**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - यह डिक्शनरी निर्दिष्ट करती है कि टोकनाइज़ किए गए आउटपुट में विशेष टोकन नहीं जोड़े जाने चाहिए।

7. **प्रॉम्प्ट को परिभाषित करना**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - यह स्ट्रिंग एक बातचीत प्रॉम्प्ट सेट करती है, जिसमें उपयोगकर्ता AI असिस्टेंट से अपना परिचय देने के लिए कहता है।

8. **प्रॉम्प्ट को टोकनाइज़ करना**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - यह लाइन प्रॉम्प्ट को ऐसे टोकन में बदलती है जिसे मॉडल प्रोसेस कर सके, और परिणाम को PyTorch टेन्सर्स के रूप में लौटाती है।

9. **प्रतिक्रिया उत्पन्न करना**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - यह लाइन इनपुट टोकन के आधार पर प्रतिक्रिया उत्पन्न करने के लिए मॉडल का उपयोग करती है, जिसमें अधिकतम 1024 नए टोकन हो सकते हैं।

10. **प्रतिक्रिया को डिकोड करना**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - यह लाइन उत्पन्न टोकन को वापस एक मानव-पढ़ने योग्य स्ट्रिंग में बदलती है, किसी भी विशेष टोकन को छोड़ते हुए, और पहला परिणाम प्राप्त करती है।

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या गलतियां हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।