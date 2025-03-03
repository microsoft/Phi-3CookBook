[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Dieser Code exportiert ein Modell in das OpenVINO-Format, lädt es und nutzt es, um eine Antwort auf eine gegebene Eingabeaufforderung zu generieren.

1. **Exportieren des Modells**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Dieser Befehl verwendet `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importieren der benötigten Bibliotheken**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Diese Zeilen importieren Klassen aus dem Modul `transformers` library and the `optimum.intel.openvino`, die benötigt werden, um das Modell zu laden und zu verwenden.

3. **Einrichten des Modellverzeichnisses und der Konfiguration**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ist ein Wörterbuch, das das OpenVINO-Modell so konfiguriert, dass es niedrige Latenz priorisiert, einen Inferenz-Stream verwendet und kein Cache-Verzeichnis nutzt.

4. **Laden des Modells**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Diese Zeile lädt das Modell aus dem angegebenen Verzeichnis, unter Verwendung der zuvor definierten Konfigurationseinstellungen. Sie ermöglicht auch die Ausführung von Remote-Code, falls erforderlich.

5. **Laden des Tokenizers**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Diese Zeile lädt den Tokenizer, der dafür verantwortlich ist, Text in Token umzuwandeln, die das Modell verstehen kann.

6. **Einrichten der Tokenizer-Argumente**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Dieses Wörterbuch gibt an, dass keine speziellen Token zur tokenisierten Ausgabe hinzugefügt werden sollen.

7. **Definieren der Eingabeaufforderung**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Dieser String legt eine Gesprächseingabe fest, bei der der Benutzer die KI-Assistenz bittet, sich vorzustellen.

8. **Tokenisieren der Eingabeaufforderung**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Diese Zeile wandelt die Eingabeaufforderung in Token um, die das Modell verarbeiten kann, und gibt das Ergebnis als PyTorch-Tensoren zurück.

9. **Generieren einer Antwort**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Diese Zeile verwendet das Modell, um basierend auf den Eingabetoken eine Antwort zu generieren, mit maximal 1024 neuen Token.

10. **Dekodieren der Antwort**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Diese Zeile wandelt die generierten Token zurück in einen menschenlesbaren String, überspringt dabei spezielle Token und gibt das erste Ergebnis zurück.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.