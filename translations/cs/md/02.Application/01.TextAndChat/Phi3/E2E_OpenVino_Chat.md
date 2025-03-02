[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tento kód exportuje model do formátu OpenVINO, načte ho a použije k vygenerování odpovědi na zadaný podnět.

1. **Exportování modelu**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tento příkaz využívá `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importování potřebných knihoven**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Tyto řádky importují třídy z modulu `transformers` library and the `optimum.intel.openvino`, které jsou nezbytné pro načtení a použití modelu.

3. **Nastavení adresáře modelu a konfigurace**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je slovník, který konfiguruje model OpenVINO tak, aby upřednostňoval nízkou latenci, používal jeden inference stream a nepoužíval cache adresář.

4. **Načtení modelu**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Tento řádek načte model ze specifikovaného adresáře pomocí dříve definovaných konfiguračních nastavení. Umožňuje také vzdálené spuštění kódu, pokud je to nutné.

5. **Načtení tokenizeru**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tento řádek načte tokenizer, který je zodpovědný za převod textu na tokeny, kterým model rozumí.

6. **Nastavení argumentů tokenizeru**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tento slovník specifikuje, že do tokenizovaného výstupu nemají být přidány speciální tokeny.

7. **Definování podnětu (promptu)**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tento řetězec nastavuje konverzační podnět, ve kterém uživatel požádá AI asistenta, aby se představil.

8. **Tokenizace podnětu**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Tento řádek převádí podnět na tokeny, které model dokáže zpracovat, a vrací výsledek jako PyTorch tensory.

9. **Generování odpovědi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tento řádek využívá model k vygenerování odpovědi na základě vstupních tokenů, přičemž maximální počet nových tokenů je 1024.

10. **Dekódování odpovědi**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tento řádek převádí vygenerované tokeny zpět do čitelného textu, přeskakuje jakékoliv speciální tokeny a vrací první výsledek.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.