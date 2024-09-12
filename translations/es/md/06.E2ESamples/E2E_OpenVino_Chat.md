[OpenVino Chat Sample](../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Este código exporta un modelo al formato OpenVINO, lo carga y lo usa para generar una respuesta a un prompt dado.

1. **Exportando el Modelo**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Este comando utiliza la herramienta `optimum-cli` para exportar un modelo al formato OpenVINO, que está optimizado para una inferencia eficiente.
   - El modelo que se está exportando es `"microsoft/Phi-3-mini-4k-instruct"`, y está configurado para la tarea de generación de texto basada en contexto previo.
   - Los pesos del modelo se cuantizan a enteros de 4 bits (`int4`), lo que ayuda a reducir el tamaño del modelo y acelerar el procesamiento.
   - Otros parámetros como `group-size`, `ratio` y `sym` se utilizan para ajustar el proceso de cuantización.
   - El modelo exportado se guarda en el directorio `./model/phi3-instruct/int4`.

2. **Importando Bibliotecas Necesarias**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Estas líneas importan clases de la biblioteca `transformers` y del módulo `optimum.intel.openvino`, que son necesarias para cargar y usar el modelo.

3. **Configurando el Directorio del Modelo y la Configuración**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` especifica dónde se almacenan los archivos del modelo.
   - `ov_config` es un diccionario que configura el modelo OpenVINO para priorizar baja latencia, usar un flujo de inferencia y no usar un directorio de caché.

4. **Cargando el Modelo**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Esta línea carga el modelo desde el directorio especificado, utilizando las configuraciones definidas anteriormente. También permite la ejecución de código remoto si es necesario.

5. **Cargando el Tokenizador**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Esta línea carga el tokenizador, que es responsable de convertir texto en tokens que el modelo puede entender.

6. **Configurando Argumentos del Tokenizador**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Este diccionario especifica que no se deben agregar tokens especiales a la salida tokenizada.

7. **Definiendo el Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Esta cadena establece un prompt de conversación donde el usuario le pide al asistente de IA que se presente.

8. **Tokenizando el Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Esta línea convierte el prompt en tokens que el modelo puede procesar, devolviendo el resultado como tensores de PyTorch.

9. **Generando una Respuesta**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Esta línea usa el modelo para generar una respuesta basada en los tokens de entrada, con un máximo de 1024 nuevos tokens.

10. **Decodificando la Respuesta**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Esta línea convierte los tokens generados de nuevo en una cadena legible, omitiendo cualquier token especial, y recupera el primer resultado.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.