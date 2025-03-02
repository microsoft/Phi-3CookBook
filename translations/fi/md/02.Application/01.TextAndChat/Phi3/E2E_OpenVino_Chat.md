[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tämä koodi vie mallin OpenVINO-muotoon, lataa sen ja käyttää sitä vastaamaan annettuun kysymykseen.

1. **Mallin vieminen**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tämä komento käyttää `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Tarvittavien kirjastojen tuonti**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Nämä rivit tuovat luokkia `transformers` library and the `optimum.intel.openvino`-moduulista, joita tarvitaan mallin lataamiseen ja käyttöön.

3. **Mallihakemiston ja konfiguraation määrittäminen**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` on sanakirja, joka määrittää OpenVINO-mallin priorisoimaan matalan viiveen, käyttämään yhtä inferenssivirtaa ja olemaan käyttämättä välimuistihakemistoa.

4. **Mallin lataaminen**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Tämä rivi lataa mallin määritetystä hakemistosta, käyttäen aiemmin määriteltyjä asetuksia. Se sallii myös etäkoodin suorittamisen tarvittaessa.

5. **Tokenisaattorin lataaminen**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tämä rivi lataa tokenisaattorin, joka muuntaa tekstin mallin ymmärtämiin tokeneihin.

6. **Tokenisaattorin argumenttien määrittäminen**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tämä sanakirja määrittää, ettei tokenisoituun tulokseen lisätä erikoistokeneita.

7. **Kehotteen määrittäminen**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tämä merkkijono luo keskustelukehotteen, jossa käyttäjä pyytää tekoälyavustajaa esittelemään itsensä.

8. **Kehotteen tokenisointi**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Tämä rivi muuntaa kehotteen tokeneiksi, joita malli voi käsitellä, ja palauttaa tuloksen PyTorch-tensoreina.

9. **Vastauksen generointi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tämä rivi käyttää mallia luomaan vastauksen syötettyjen tokenien perusteella, enintään 1024 uutta tokenia.

10. **Vastauksen dekoodaus**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tämä rivi muuntaa generoidut tokenit takaisin ihmisen luettavaan merkkijonoon, ohittaen erikoistokenit, ja palauttaa ensimmäisen tuloksen.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisten tekoälykäännöspalveluiden avulla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virheellisistä tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.