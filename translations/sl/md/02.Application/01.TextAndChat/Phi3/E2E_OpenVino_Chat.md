[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ta koda izvozi model v format OpenVINO, ga naloži in uporabi za generiranje odgovora na dano vprašanje.

1. **Izvoz modela**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ta ukaz uporablja `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Uvoz potrebnih knjižnic**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Te vrstice uvozijo razrede iz modula `transformers` library and the `optimum.intel.openvino`, ki so potrebni za nalaganje in uporabo modela.

3. **Nastavitev direktorija modela in konfiguracije**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je slovar, ki konfigurira OpenVINO model za prednostno obravnavo nizke zakasnitve, uporabo enega toka inferenc in neuporabo predpomnilniškega direktorija.

4. **Nalaganje modela**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ta vrstica naloži model iz določenega direktorija z uporabo prej definiranih nastavitev konfiguracije. Prav tako omogoča oddaljeno izvajanje kode, če je to potrebno.

5. **Nalaganje tokenizatorja**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ta vrstica naloži tokenizator, ki je odgovoren za pretvorbo besedila v tokene, ki jih model razume.

6. **Nastavitev argumentov za tokenizator**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ta slovar določa, da se posebni tokeni ne smejo dodajati k tokeniziranemu izhodu.

7. **Definiranje vprašanja**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ta niz nastavi pogovorno vprašanje, kjer uporabnik prosi AI asistenta, naj se predstavi.

8. **Tokenizacija vprašanja**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ta vrstica pretvori vprašanje v tokene, ki jih model lahko obdela, in vrne rezultat kot PyTorch tenzorje.

9. **Generiranje odgovora**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ta vrstica uporabi model za generiranje odgovora na podlagi vhodnih tokenov, pri čemer je omejitev največ 1024 novih tokenov.

10. **Dekodiranje odgovora**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ta vrstica pretvori generirane tokene nazaj v čitljiv niz, preskoči posebne tokene in pridobi prvi rezultat.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo strojnih prevajalskih storitev umetne inteligence. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.