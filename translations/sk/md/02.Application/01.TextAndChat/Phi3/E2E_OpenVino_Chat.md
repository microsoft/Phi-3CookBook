[OpenVino Chat Ukážka](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tento kód exportuje model do formátu OpenVINO, načíta ho a používa na generovanie odpovedí na zadané otázky.

1. **Exportovanie modelu**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tento príkaz používa `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importovanie potrebných knižníc**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Tieto riadky importujú triedy z modulu `transformers` library and the `optimum.intel.openvino`, ktoré sú potrebné na načítanie a používanie modelu.

3. **Nastavenie adresára modelu a konfigurácie**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je slovník, ktorý konfiguruje model OpenVINO tak, aby uprednostňoval nízku latenciu, používal jeden prúd inferencie a nepoužíval adresár pre cache.

4. **Načítanie modelu**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Tento riadok načíta model zo špecifikovaného adresára pomocou predtým definovaných konfiguračných nastavení. Taktiež umožňuje vzdialené vykonávanie kódu, ak je to potrebné.

5. **Načítanie tokenizeru**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tento riadok načíta tokenizer, ktorý je zodpovedný za konverziu textu na tokeny, ktoré model dokáže spracovať.

6. **Nastavenie argumentov pre tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tento slovník špecifikuje, že špeciálne tokeny by nemali byť pridané do tokenizovaného výstupu.

7. **Definovanie výzvy (promptu)**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tento reťazec nastavuje konverzačnú výzvu, kde používateľ požiada AI asistenta, aby sa predstavil.

8. **Tokenizácia výzvy**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Tento riadok konvertuje výzvu na tokeny, ktoré model dokáže spracovať, pričom výsledok vráti ako PyTorch tenzory.

9. **Generovanie odpovede**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tento riadok používa model na generovanie odpovede na základe vstupných tokenov, s maximálnym počtom 1024 nových tokenov.

10. **Dekódovanie odpovede**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tento riadok konvertuje vygenerované tokeny späť na čitateľný text, pričom preskočí akékoľvek špeciálne tokeny, a vráti prvý výsledok.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.