[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Questo codice esporta un modello nel formato OpenVINO, lo carica e lo utilizza per generare una risposta a un determinato prompt.

1. **Esportazione del Modello**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Questo comando utilizza il `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importazione delle Librerie Necessarie**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Queste righe importano classi dal modulo `transformers` library and the `optimum.intel.openvino`, necessarie per caricare e utilizzare il modello.

3. **Configurazione della Directory del Modello**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` è un dizionario che configura il modello OpenVINO per dare priorità alla bassa latenza, utilizzare un solo stream di inferenza e non usare una directory di cache.

4. **Caricamento del Modello**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Questa riga carica il modello dalla directory specificata, utilizzando le impostazioni di configurazione definite in precedenza. Consente anche l'esecuzione remota del codice, se necessario.

5. **Caricamento del Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Questa riga carica il tokenizer, responsabile della conversione del testo in token comprensibili per il modello.

6. **Impostazione degli Argomenti del Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Questo dizionario specifica che non devono essere aggiunti token speciali all'output tokenizzato.

7. **Definizione del Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Questa stringa imposta un prompt di conversazione in cui l'utente chiede all'assistente AI di presentarsi.

8. **Tokenizzazione del Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Questa riga converte il prompt in token che il modello può elaborare, restituendo il risultato come tensori PyTorch.

9. **Generazione di una Risposta**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Questa riga utilizza il modello per generare una risposta basata sui token di input, con un massimo di 1024 nuovi token.

10. **Decodifica della Risposta**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Questa riga converte i token generati in una stringa leggibile, ignorando eventuali token speciali, e restituisce il primo risultato.

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.