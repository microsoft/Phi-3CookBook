[OpenVino Chat Eksempel](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Denne kode eksporterer en model til OpenVINO-formatet, indlæser den og bruger den til at generere et svar på en given prompt.

1. **Eksport af modellen**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Denne kommando bruger `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Import af nødvendige biblioteker**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Disse linjer importerer klasser fra `transformers` library and the `optimum.intel.openvino`-modulet, som er nødvendige for at indlæse og bruge modellen.

3. **Opsætning af modelmappe og konfiguration**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` er en ordbog, der konfigurerer OpenVINO-modellen til at prioritere lav latenstid, bruge én inferensstrøm og undlade at bruge en cachemappe.

4. **Indlæsning af modellen**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Denne linje indlæser modellen fra den angivne mappe ved hjælp af de tidligere definerede konfigurationsindstillinger. Den tillader også fjernudførelse af kode, hvis nødvendigt.

5. **Indlæsning af tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Denne linje indlæser tokenizeren, som er ansvarlig for at konvertere tekst til tokens, som modellen kan forstå.

6. **Opsætning af tokenizer-argumenter**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Denne ordbog angiver, at der ikke skal tilføjes specielle tokens til det tokeniserede output.

7. **Definition af prompten**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Denne streng opsætter en samtaleprompt, hvor brugeren beder AI-assistenten om at præsentere sig selv.

8. **Tokenisering af prompten**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Denne linje konverterer prompten til tokens, som modellen kan behandle, og returnerer resultatet som PyTorch-tensore.

9. **Generering af et svar**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Denne linje bruger modellen til at generere et svar baseret på input-tokens, med et maksimum på 1024 nye tokens.

10. **Dekodning af svaret**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Denne linje konverterer de genererede tokens tilbage til en læsbar tekst, springer specielle tokens over og henter det første resultat.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel human oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.