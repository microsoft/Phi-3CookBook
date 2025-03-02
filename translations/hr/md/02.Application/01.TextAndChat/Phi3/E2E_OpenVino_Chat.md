[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ovaj kod izvozi model u OpenVINO format, učitava ga i koristi za generiranje odgovora na zadani upit.

1. **Izvoz modela**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ova naredba koristi `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Učitavanje potrebnih biblioteka**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ovi redovi uvoze klase iz modula `transformers` library and the `optimum.intel.openvino`, koje su potrebne za učitavanje i korištenje modela.

3. **Postavljanje direktorija modela i konfiguracije**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je rječnik koji konfigurira OpenVINO model da prioritizira nisku latenciju, koristi jedan tok inferencije i ne koristi direktorij za predmemoriju.

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
   - Ovaj red učitava model iz specificiranog direktorija koristeći ranije definirane postavke konfiguracije. Također omogućuje daljinsko izvršavanje koda ako je potrebno.

5. **Učitavanje tokenizatora**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ovaj red učitava tokenizator koji je odgovoran za pretvaranje teksta u tokene koje model može razumjeti.

6. **Postavljanje argumenata za tokenizator**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ovaj rječnik specificira da se posebni tokeni ne bi trebali dodavati u tokenizirani izlaz.

7. **Definiranje upita (prompt)**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ovaj string postavlja upit za razgovor u kojem korisnik traži AI asistenta da se predstavi.

8. **Tokenizacija upita**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ovaj red pretvara upit u tokene koje model može obraditi i vraća rezultat kao PyTorch tenzore.

9. **Generiranje odgovora**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ovaj red koristi model za generiranje odgovora na temelju ulaznih tokena, s maksimalno 1024 novih tokena.

10. **Dekodiranje odgovora**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ovaj red pretvara generirane tokene natrag u čitljiv tekst, preskačući posebne tokene, i dohvaća prvi rezultat.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prevođenja. Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.