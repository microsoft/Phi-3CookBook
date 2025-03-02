[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

हे कोड मॉडेल OpenVINO फॉरमॅटमध्ये निर्यात करतो, ते लोड करतो आणि दिलेल्या प्रॉम्प्टवर आधारित प्रतिसाद तयार करण्यासाठी वापरतो.

1. **मॉडेल निर्यात करणे**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ही कमांड `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` वापरते.

2. **आवश्यक लायब्ररी आयात करणे**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - या ओळी `transformers` library and the `optimum.intel.openvino` मॉड्यूलमधील क्लासेस आयात करतात, जे मॉडेल लोड आणि वापरण्यासाठी आवश्यक आहेत.

3. **मॉडेल डिरेक्टरी आणि कॉन्फिगरेशन सेट करणे**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` हा शब्दकोश OpenVINO मॉडेलला कमी विलंबावर प्राधान्य देण्यासाठी, एकच इनफरन्स स्ट्रीम वापरण्यासाठी आणि कॅशे डिरेक्टरी न वापरण्यासाठी कॉन्फिगर करतो.

4. **मॉडेल लोड करणे**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - ही ओळ दिलेल्या डिरेक्टरीमधून, आधी ठरवलेल्या कॉन्फिगरेशन सेटिंग्ज वापरून मॉडेल लोड करते. तसेच, आवश्यक असल्यास रिमोट कोड अंमलबजावणीस परवानगी देते.

5. **टोकनायझर लोड करणे**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ही ओळ टोकनायझर लोड करते, जो मजकूर टोकनमध्ये रूपांतरित करण्यासाठी जबाबदार असतो, ज्याला मॉडेल समजू शकते.

6. **टोकनायझरचे आर्ग्युमेंट सेट करणे**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - हा शब्दकोश टोकनाइज्ड आउटपुटमध्ये विशेष टोकन्स जोडले जाऊ नयेत हे निर्दिष्ट करतो.

7. **प्रॉम्प्ट परिभाषित करणे**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - हा स्ट्रिंग एक संभाषण प्रॉम्प्ट सेट करतो, जिथे वापरकर्ता AI सहाय्यकाला स्वतःची ओळख करून देण्यास सांगतो.

8. **प्रॉम्प्ट टोकनाइज करणे**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ही ओळ प्रॉम्प्टला टोकनमध्ये रूपांतरित करते, जे मॉडेल प्रक्रिया करू शकते, आणि परिणाम PyTorch टेन्सर्स म्हणून परत करते.

9. **प्रतिसाद तयार करणे**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ही ओळ इनपुट टोकन्सवर आधारित मॉडेल वापरून प्रतिसाद तयार करते, जास्तीत जास्त 1024 नवीन टोकन्ससह.

10. **प्रतिसाद डिकोड करणे**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ही ओळ तयार केलेल्या टोकन्सना पुन्हा मानवी-वाचनीय स्ट्रिंगमध्ये रूपांतरित करते, कोणतेही विशेष टोकन्स वगळून, आणि पहिला परिणाम परत करते.

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित AI भाषांतर सेवा वापरून भाषांतरित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.