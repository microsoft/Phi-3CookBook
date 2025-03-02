[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Hii ni msimbo wa kubadilisha mfano kuwa muundo wa OpenVINO, kuupakia, na kuutumia kuunda jibu kwa swali lililotolewa.

1. **Kubadilisha Mfano**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Amri hii inatumia `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Kuagiza Maktaba Muhimu**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Mistari hii inaagiza madarasa kutoka moduli ya `transformers` library and the `optimum.intel.openvino`, ambayo inahitajika kupakia na kutumia mfano.

3. **Kuandaa Saraka ya Mfano na Usanidi**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ni kamusi inayosanidi mfano wa OpenVINO kuweka kipaumbele kwa ucheleweshaji mdogo, kutumia mkondo mmoja wa inference, na kutotumia saraka ya cache.

4. **Kupakia Mfano**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Mstari huu unapakua mfano kutoka kwenye saraka maalum, ukitumia mipangilio ya usanidi iliyotajwa awali. Pia inaruhusu utekelezaji wa msimbo wa mbali ikiwa inahitajika.

5. **Kupakia Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Mstari huu unapakia tokenizer, ambayo inahusika na kubadilisha maandishi kuwa tokeni ambazo mfano unaweza kuelewa.

6. **Kuandaa Hoja za Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Kamusi hii inaeleza kuwa tokeni maalum hazipaswi kuongezwa kwenye matokeo ya tokenization.

7. **Kufafanua Swali**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Mstari huu unaunda swali la mazungumzo ambapo mtumiaji anamwuliza msaidizi wa AI kujitambulisha.

8. **Kuweka Tokeni kwa Swali**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Mstari huu hubadilisha swali kuwa tokeni ambazo mfano unaweza kushughulikia, na kurudisha matokeo kama tensors za PyTorch.

9. **Kuzalisha Jibu**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Mstari huu unatumia mfano kuunda jibu kulingana na tokeni za ingizo, kwa kiwango cha juu cha tokeni mpya 1024.

10. **Kutafsiri Jibu**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Mstari huu hubadilisha tokeni zilizozalishwa kuwa maandishi yanayosomeka na binadamu, ukiruka tokeni maalum, na kupata matokeo ya kwanza.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kibinadamu ya kitaalamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.