[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ten kod eksportuje model do formatu OpenVINO, ładuje go i wykorzystuje do generowania odpowiedzi na podany prompt.

1. **Eksportowanie modelu**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ta komenda używa `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importowanie niezbędnych bibliotek**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Te linie importują klasy z modułu `transformers` library and the `optimum.intel.openvino`, które są potrzebne do załadowania i używania modelu.

3. **Konfigurowanie katalogu modelu i ustawień**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` to słownik, który konfiguruje model OpenVINO, aby priorytetowo traktować niskie opóźnienia, używać jednego strumienia inferencji i nie korzystać z katalogu cache.

4. **Ładowanie modelu**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ta linia ładuje model z określonego katalogu, korzystając z wcześniej zdefiniowanych ustawień konfiguracji. Umożliwia także zdalne wykonywanie kodu, jeśli to konieczne.

5. **Ładowanie tokenizatora**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ta linia ładuje tokenizator, który odpowiada za konwertowanie tekstu na tokeny zrozumiałe dla modelu.

6. **Konfigurowanie argumentów tokenizatora**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ten słownik określa, że do wynikowego tokenizowanego tekstu nie powinny być dodawane specjalne tokeny.

7. **Definiowanie promptu**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ten ciąg tekstowy ustawia prompt konwersacyjny, w którym użytkownik prosi asystenta AI o przedstawienie się.

8. **Tokenizowanie promptu**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ta linia konwertuje prompt na tokeny, które model może przetworzyć, zwracając wynik w postaci tensora PyTorch.

9. **Generowanie odpowiedzi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ta linia wykorzystuje model do wygenerowania odpowiedzi na podstawie wejściowych tokenów, z limitem maksymalnie 1024 nowych tokenów.

10. **Dekodowanie odpowiedzi**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ta linia konwertuje wygenerowane tokeny z powrotem na czytelny dla człowieka tekst, pomijając specjalne tokeny, i zwraca pierwszy wynik.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.