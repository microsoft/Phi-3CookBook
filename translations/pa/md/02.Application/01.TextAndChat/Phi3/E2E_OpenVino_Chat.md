[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

ਇਹ ਕੋਡ ਇੱਕ ਮਾਡਲ ਨੂੰ OpenVINO ਫਾਰਮੈਟ ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਦਾ ਹੈ, ਇਸਨੂੰ ਲੋਡ ਕਰਦਾ ਹੈ, ਅਤੇ ਦਿੱਤੇ ਗਏ ਪ੍ਰਸ਼ਨ ਦਾ ਜਵਾਬ ਤਿਆਰ ਕਰਨ ਲਈ ਇਸਦਾ ਇਸਤੇਮਾਲ ਕਰਦਾ ਹੈ।

1. **ਮਾਡਲ ਐਕਸਪੋਰਟ ਕਰਨਾ**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - ਇਹ ਕਮਾਂਡ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ।

2. **ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਨਾ**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - ਇਹ ਲਾਈਨਾਂ `transformers` library and the `optimum.intel.openvino` ਮੋਡਿਊਲ ਤੋਂ ਕਲਾਸਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦੀਆਂ ਹਨ, ਜੋ ਮਾਡਲ ਨੂੰ ਲੋਡ ਕਰਨ ਅਤੇ ਵਰਤਣ ਲਈ ਲੋੜੀਂਦੀਆਂ ਹਨ।

3. **ਮਾਡਲ ਡਾਇਰੈਕਟਰੀ ਅਤੇ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟ ਕਰਨਾ**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੈ ਜੋ OpenVINO ਮਾਡਲ ਨੂੰ ਘੱਟ ਲੇਟੈਂਸੀ ਨੂੰ ਤਰਜੀਹ ਦੇਣ, ਇੱਕ ਇਨਫਰੈਂਸ ਸਟ੍ਰੀਮ ਵਰਤਣ, ਅਤੇ ਕੈਸ਼ ਡਾਇਰੈਕਟਰੀ ਨੂੰ ਨਾ ਵਰਤਣ ਲਈ ਕਨਫਿਗਰ ਕਰਦਾ ਹੈ।

4. **ਮਾਡਲ ਨੂੰ ਲੋਡ ਕਰਨਾ**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - ਇਹ ਲਾਈਨ ਮਾਡਲ ਨੂੰ ਨਿਰਧਾਰਤ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਲੋਡ ਕਰਦੀ ਹੈ, ਜੋ ਪਹਿਲਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈਟਿੰਗਾਂ ਨੂੰ ਵਰਤਦੀ ਹੈ। ਜਰੂਰਤ ਪੈਣ ‘ਤੇ ਰਿਮੋਟ ਕੋਡ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਦੀ ਇਜਾਜ਼ਤ ਵੀ ਦਿੰਦੀ ਹੈ।

5. **ਟੋਕਨਾਈਜ਼ਰ ਨੂੰ ਲੋਡ ਕਰਨਾ**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - ਇਹ ਲਾਈਨ ਟੋਕਨਾਈਜ਼ਰ ਨੂੰ ਲੋਡ ਕਰਦੀ ਹੈ, ਜੋ ਟੈਕਸਟ ਨੂੰ ਟੋਕਨ ਵਿੱਚ ਬਦਲਣ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੈ, ਜਿਸਨੂੰ ਮਾਡਲ ਸਮਝ ਸਕਦਾ ਹੈ।

6. **ਟੋਕਨਾਈਜ਼ਰ ਅਰਗੁਮੈਂਟਸ ਸੈਟ ਕਰਨਾ**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - ਇਹ ਡਿਕਸ਼ਨਰੀ ਇਹ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ ਕਿ ਟੋਕਨਾਈਜ਼ਡ ਆਉਟਪੁਟ ਵਿੱਚ ਖਾਸ ਟੋਕਨ ਨਹੀਂ ਜੋੜੇ ਜਾਣੇ ਚਾਹੀਦੇ।

7. **ਪ੍ਰੰਪਟ ਪਰਿਭਾਸ਼ਤ ਕਰਨਾ**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - ਇਹ ਸਟਰਿੰਗ ਇੱਕ ਗੱਲਬਾਤ ਪ੍ਰੰਪਟ ਸੈਟ ਕਰਦੀ ਹੈ, ਜਿੱਥੇ ਯੂਜ਼ਰ AI ਸਹਾਇਕ ਨੂੰ ਆਪਣੇ ਆਪ ਦਾ ਪਰੀਚੇ ਦੇਣ ਲਈ ਕਹਿੰਦਾ ਹੈ।

8. **ਪ੍ਰੰਪਟ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰਨਾ**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - ਇਹ ਲਾਈਨ ਪ੍ਰੰਪਟ ਨੂੰ ਟੋਕਨ ਵਿੱਚ ਬਦਲਦੀ ਹੈ, ਜਿਸਨੂੰ ਮਾਡਲ ਪ੍ਰਕਿਰਿਆ ਕਰ ਸਕਦਾ ਹੈ, ਅਤੇ ਨਤੀਜਾ PyTorch ਟੈਂਸਰ ਦੇ ਰੂਪ ਵਿੱਚ ਵਾਪਸ ਕਰਦੀ ਹੈ।

9. **ਜਵਾਬ ਤਿਆਰ ਕਰਨਾ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - ਇਹ ਲਾਈਨ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਪੁਟ ਟੋਕਨ ਦੇ ਆਧਾਰ ‘ਤੇ ਇੱਕ ਜਵਾਬ ਤਿਆਰ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਵੱਧ ਤੋਂ ਵੱਧ 1024 ਨਵੇਂ ਟੋਕਨ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ।

10. **ਜਵਾਬ ਨੂੰ ਡੀਕੋਡ ਕਰਨਾ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - ਇਹ ਲਾਈਨ ਤਿਆਰ ਕੀਤੇ ਗਏ ਟੋਕਨ ਨੂੰ ਮੁੜ ਪੜ੍ਹਨਯੋਗ ਸਟਰਿੰਗ ਵਿੱਚ ਬਦਲਦੀ ਹੈ, ਕਿਸੇ ਵੀ ਖਾਸ ਟੋਕਨ ਨੂੰ ਛੱਡ ਦਿੰਦੀ ਹੈ, ਅਤੇ ਪਹਿਲਾ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਕਰਦੀ ਹੈ।

**ਅਸਵੀਕਾਰਣਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।