[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Acest cod exportă un model în format OpenVINO, îl încarcă și îl folosește pentru a genera un răspuns la un prompt dat.

1. **Exportarea Modelului**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Această comandă folosește `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importarea Bibliotecilor Necesare**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Aceste linii importă clase din modulul `transformers` library and the `optimum.intel.openvino`, necesare pentru a încărca și utiliza modelul.

3. **Configurarea Directorului Modelului și a Configurației**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` este un dicționar care configurează modelul OpenVINO pentru a prioritiza latența scăzută, a folosi un singur flux de inferență și a nu folosi un director de cache.

4. **Încărcarea Modelului**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Această linie încarcă modelul din directorul specificat, folosind setările de configurare definite anterior. De asemenea, permite execuția codului de la distanță, dacă este necesar.

5. **Încărcarea Tokenizer-ului**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Această linie încarcă tokenizer-ul, care este responsabil pentru conversia textului în tokeni pe care modelul îi poate înțelege.

6. **Configurarea Argumentelor Tokenizer-ului**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Acest dicționar specifică faptul că nu ar trebui adăugate tokeni speciali la ieșirea tokenizată.

7. **Definirea Prompt-ului**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Acest șir definește un prompt de conversație în care utilizatorul cere asistentului AI să se prezinte.

8. **Tokenizarea Prompt-ului**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Această linie convertește prompt-ul în tokeni pe care modelul îi poate procesa, returnând rezultatul sub formă de tensori PyTorch.

9. **Generarea unui Răspuns**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Această linie folosește modelul pentru a genera un răspuns bazat pe tokenii de intrare, cu un maxim de 1024 tokeni noi.

10. **Decodarea Răspunsului**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Această linie convertește tokenii generați înapoi într-un șir lizibil, omite orice tokeni speciali și returnează primul rezultat.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa natală, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.