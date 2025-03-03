[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Denne koden eksporterer en modell til OpenVINO-formatet, laster den inn og bruker den til å generere et svar på en gitt forespørsel.

1. **Eksportere modellen**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Denne kommandoen bruker `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importere nødvendige biblioteker**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Disse linjene importerer klasser fra `transformers` library and the `optimum.intel.openvino`-modulen, som trengs for å laste inn og bruke modellen.

3. **Sette opp modellkatalogen og konfigurasjonen**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` er en ordbok som konfigurerer OpenVINO-modellen til å prioritere lav ventetid, bruke én inferensstrøm og ikke benytte en cache-katalog.

4. **Laste inn modellen**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Denne linjen laster inn modellen fra den angitte katalogen, ved å bruke konfigurasjonsinnstillingene som ble definert tidligere. Den tillater også fjernkjøring av kode hvis nødvendig.

5. **Laste inn tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Denne linjen laster inn tokenizer-en, som er ansvarlig for å konvertere tekst til tokens som modellen kan forstå.

6. **Sette opp tokenizer-argumenter**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Denne ordboken spesifiserer at spesialtegn ikke skal legges til i den tokeniserte utdataen.

7. **Definere forespørselen**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Denne strengen setter opp en samtaleforespørsel der brukeren ber AI-assistenten om å introdusere seg selv.

8. **Tokenisere forespørselen**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Denne linjen konverterer forespørselen til tokens som modellen kan behandle, og returnerer resultatet som PyTorch-tensorklasser.

9. **Generere et svar**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Denne linjen bruker modellen til å generere et svar basert på inndata-tokens, med en maksimal lengde på 1024 nye tokens.

10. **Dekode svaret**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Denne linjen konverterer de genererte tokens tilbake til en lesbar tekststreng, hopper over spesialtegn og henter det første resultatet.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.