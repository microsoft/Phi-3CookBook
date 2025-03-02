[OpenVino Chat Minta](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ez a kód egy modellt exportál OpenVINO formátumba, betölti azt, és választ generál egy adott kérésre.

1. **A Modell Exportálása**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ez a parancs az `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` használatával működik.

2. **Szükséges Könyvtárak Importálása**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ezek a sorok importálják a `transformers` library and the `optimum.intel.openvino` modul osztályait, amelyek a modell betöltéséhez és használatához szükségesek.

3. **A Modell Könyvtárának és Konfigurációjának Beállítása**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - A `model_dir` specifies where the model files are stored.
   - `ov_config` egy szótár, amely az OpenVINO modellt úgy konfigurálja, hogy az alacsony késleltetést részesítse előnyben, egyetlen előrejelzési szálat használjon, és ne használjon gyorsítótár könyvtárat.

4. **A Modell Betöltése**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ez a sor a korábban megadott könyvtárból tölti be a modellt, az előzőleg definiált konfigurációs beállításokkal. Szükség esetén lehetőséget biztosít távoli kódvégrehajtásra is.

5. **A Tokenizer Betöltése**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ez a sor betölti a tokenizálót, amely a szöveget olyan tokenekké alakítja, amelyeket a modell megért.

6. **A Tokenizáló Argumentumainak Beállítása**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ez a szótár meghatározza, hogy ne adjon hozzá speciális tokeneket a tokenizált kimenethez.

7. **A Kérés Meghatározása**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ez a szöveg egy beszélgetési kérést állít be, amelyben a felhasználó arra kéri az AI asszisztenst, hogy mutatkozzon be.

8. **A Kérés Tokenizálása**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ez a sor a kérést olyan tokenekké alakítja, amelyeket a modell feldolgozhat, és az eredményt PyTorch tenzorként adja vissza.

9. **Válasz Generálása**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ez a sor a modellt használja arra, hogy választ generáljon a bemeneti tokenek alapján, legfeljebb 1024 új tokennel.

10. **A Válasz Dekódolása**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ez a sor a generált tokeneket visszaalakítja ember által olvasható szöveggé, kihagyva a speciális tokeneket, és az első eredményt adja vissza.

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.