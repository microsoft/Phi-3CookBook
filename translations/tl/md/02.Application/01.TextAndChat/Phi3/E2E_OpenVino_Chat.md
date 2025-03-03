[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ang code na ito ay nag-e-export ng isang modelo sa OpenVINO format, ini-load ito, at ginagamit upang bumuo ng sagot sa isang ibinigay na prompt.

1. **Pag-e-export ng Modelo**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ang utos na ito ay gumagamit ng `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Pag-import ng Mga Kinakailangang Library**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ang mga linyang ito ay nag-i-import ng mga klase mula sa `transformers` library and the `optimum.intel.openvino` module, na kinakailangan upang i-load at gamitin ang modelo.

3. **Pag-set Up ng Model Directory at Configuration**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - Ang `model_dir` specifies where the model files are stored.
   - `ov_config` ay isang dictionary na nagko-configure sa OpenVINO model upang bigyang-priyoridad ang mababang latency, gumamit ng isang inference stream, at hindi gumamit ng cache directory.

4. **Pag-load ng Modelo**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ang linyang ito ay naglo-load ng modelo mula sa tinukoy na directory, gamit ang mga configuration setting na naitakda na. Pinapayagan din nito ang remote code execution kung kinakailangan.

5. **Pag-load ng Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ang linyang ito ay naglo-load ng tokenizer, na responsable sa pag-convert ng text sa mga token na maiintindihan ng modelo.

6. **Pag-set Up ng Tokenizer Arguments**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ang dictionary na ito ay nagsasaad na ang mga special token ay hindi dapat idagdag sa tokenized output.

7. **Pagde-define ng Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ang string na ito ay nagse-set up ng isang conversation prompt kung saan tinatanong ng user ang AI assistant na ipakilala ang sarili nito.

8. **Pag-tokenize ng Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ang linyang ito ay nagko-convert ng prompt sa mga token na maaaring iproseso ng modelo, at ibinabalik ang resulta bilang PyTorch tensors.

9. **Pagbuo ng Sagot**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ang linyang ito ay gumagamit ng modelo upang bumuo ng sagot base sa input tokens, na may maximum na 1024 bagong token.

10. **Pag-decode ng Sagot**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ang linyang ito ay nagko-convert ng mga na-generate na token pabalik sa isang string na madaling basahin, iniiwasan ang anumang special tokens, at kinukuha ang unang resulta.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na nakabatay sa makina. Bagama't pinagsisikapan naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.