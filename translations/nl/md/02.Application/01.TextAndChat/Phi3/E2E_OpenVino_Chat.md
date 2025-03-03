[OpenVino Chat Voorbeeld](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Deze code exporteert een model naar het OpenVINO-formaat, laadt het en gebruikt het om een reactie te genereren op een gegeven prompt.

1. **Het Model Exporteren**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Deze opdracht gebruikt de `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Benodigde Bibliotheken Importeren**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Deze regels importeren klassen uit de `transformers` library and the `optimum.intel.openvino` module, die nodig zijn om het model te laden en te gebruiken.

3. **Instellen van de Modelmap en Configuratie**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` is een woordenboek dat het OpenVINO-model configureert om prioriteit te geven aan lage latentie, één inferentiestroom te gebruiken en geen cachemap te gebruiken.

4. **Het Model Laden**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Deze regel laadt het model vanuit de opgegeven map, met behulp van de eerder gedefinieerde configuratie-instellingen. Het staat ook uitvoering van externe code toe indien nodig.

5. **De Tokenizer Laden**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Deze regel laadt de tokenizer, die verantwoordelijk is voor het omzetten van tekst in tokens die het model kan begrijpen.

6. **Tokenizer Argumenten Instellen**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Dit woordenboek specificeert dat speciale tokens niet moeten worden toegevoegd aan de getokeniseerde uitvoer.

7. **De Prompt Definiëren**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Deze string stelt een gespreksprompt op waarin de gebruiker de AI-assistent vraagt om zichzelf voor te stellen.

8. **De Prompt Tokeniseren**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Deze regel zet de prompt om in tokens die het model kan verwerken en geeft het resultaat terug als PyTorch-tensors.

9. **Een Reactie Genereren**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Deze regel gebruikt het model om een reactie te genereren op basis van de invoertokens, met een maximum van 1024 nieuwe tokens.

10. **De Reactie Decoderen**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Deze regel zet de gegenereerde tokens terug om in een menselijk leesbare string, waarbij speciale tokens worden overgeslagen, en haalt het eerste resultaat op.

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.