[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

यो कोडले एउटा मोडललाई OpenVINO ढाँचामा निर्यात गर्छ, त्यसलाई लोड गर्छ, र दिएको प्रॉम्प्टको आधारमा प्रतिक्रिया उत्पन्न गर्न प्रयोग गर्छ।

1. **मोडल निर्यात गर्दै**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - यो कमाण्डले `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` प्रयोग गर्छ।

2. **आवश्यक लाइब्रेरीहरू आयात गर्दै**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - यी लाइनहरूले `transformers` library and the `optimum.intel.openvino` मोड्युलबाट क्लासहरू आयात गर्छन्, जसले मोडल लोड र प्रयोग गर्न आवश्यक हुन्छ।

3. **मोडल निर्देशिका र कन्फिगरेसन सेटअप गर्दै**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` एउटा डिक्सनरी हो जसले OpenVINO मोडललाई कम ढिलाइ प्राथमिकतामा राख्न, एउटा इन्फरेन्स स्ट्रिम प्रयोग गर्न, र क्यासे डिरेक्टरी प्रयोग नगर्न कन्फिगर गर्छ।

4. **मोडल लोड गर्दै**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - यो लाइनले पहिल्यै निर्दिष्ट गरिएको निर्देशिकाबाट मोडल लोड गर्छ, र पहिला परिभाषित कन्फिगरेसन सेटिङहरू प्रयोग गर्छ। यो आवश्यक परेमा रिमोट कोड कार्यान्वयनलाई पनि अनुमति दिन्छ।

5. **टोकनाइजर लोड गर्दै**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - यो लाइनले टोकनाइजर लोड गर्छ, जसले पाठलाई टोकनमा रूपान्तरण गर्न जिम्मेवार हुन्छ, जसलाई मोडलले बुझ्न सक्छ।

6. **टोकनाइजरका आर्गुमेन्टहरू सेटअप गर्दै**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - यो डिक्सनरीले टोकनाइज गरिएको आउटपुटमा विशेष टोकनहरू थप्न नहुने कुरा निर्दिष्ट गर्छ।

7. **प्रॉम्प्ट परिभाषित गर्दै**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - यो स्ट्रिङले एउटा कुराकानी प्रॉम्प्ट सेटअप गर्छ जहाँ प्रयोगकर्ताले एआई सहायकलाई आफ्नो परिचय दिन अनुरोध गर्छ।

8. **प्रॉम्प्ट टोकनाइज गर्दै**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - यो लाइनले प्रॉम्प्टलाई टोकनमा रूपान्तरण गर्छ, जसलाई मोडलले प्रक्रिया गर्न सक्छ, र नतिजालाई PyTorch टेन्सरको रूपमा फिर्ता गर्छ।

9. **प्रतिक्रिया उत्पन्न गर्दै**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - यो लाइनले इनपुट टोकनहरूको आधारमा मोडल प्रयोग गरेर प्रतिक्रिया उत्पन्न गर्छ, अधिकतम 1024 नयाँ टोकनहरू सहित।

10. **प्रतिक्रिया डिकोड गर्दै**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - यो लाइनले उत्पन्न भएका टोकनहरूलाई फेरी मानवले पढ्न मिल्ने स्ट्रिङमा रूपान्तरण गर्छ, विशेष टोकनहरू हटाउँछ, र पहिलो नतिजा फिर्ता गर्छ।

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मौलिक भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।