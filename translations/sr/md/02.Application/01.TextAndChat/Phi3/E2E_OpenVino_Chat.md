[OpenVino Chat Primer](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ovaj kod izvozi model u OpenVINO format, učitava ga i koristi za generisanje odgovora na zadati upit.

1. **Izvoz modela**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ova komanda koristi `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Uvoz neophodnih biblioteka**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ove linije uvoze klase iz modula `transformers` library and the `optimum.intel.openvino`, koje su potrebne za učitavanje i korišćenje modela.

3. **Podešavanje direktorijuma modela i konfiguracije**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je rečnik koji konfiguriše OpenVINO model da daje prioritet niskoj latenciji, koristi jedan tok inferencije i ne koristi direktorijum za keširanje.

4. **Učitavanje modela**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ova linija učitava model iz specificiranog direktorijuma, koristeći ranije definisane postavke konfiguracije. Takođe omogućava izvršavanje udaljenog koda ako je potrebno.

5. **Učitavanje tokenizatora**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ova linija učitava tokenizator, koji je odgovoran za konvertovanje teksta u tokene koje model može da razume.

6. **Podešavanje argumenata za tokenizator**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ovaj rečnik specificira da specijalni tokeni ne treba da budu dodati tokenizovanom izlazu.

7. **Definisanje upita**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ovaj string postavlja upit za razgovor, gde korisnik traži od AI asistenta da se predstavi.

8. **Tokenizacija upita**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ova linija konvertuje upit u tokene koje model može da obradi, vraćajući rezultat kao PyTorch tensore.

9. **Generisanje odgovora**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ova linija koristi model za generisanje odgovora na osnovu ulaznih tokena, sa maksimalno 1024 nova tokena.

10. **Dekodiranje odgovora**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ova linija konvertuje generisane tokene nazad u čitljiv tekst, preskačući sve specijalne tokene, i dobija prvi rezultat.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења базираног на вештачкој интелигенцији. Иако тежимо тачности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.