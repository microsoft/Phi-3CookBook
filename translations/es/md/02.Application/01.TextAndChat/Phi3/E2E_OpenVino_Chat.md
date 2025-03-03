[Ejemplo de Chat con OpenVINO](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Este código exporta un modelo al formato OpenVINO, lo carga y lo utiliza para generar una respuesta a un mensaje dado.

1. **Exportar el Modelo**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Este comando utiliza `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importar las Librerías Necesarias**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Estas líneas importan clases del módulo `transformers` library and the `optimum.intel.openvino`, que son necesarias para cargar y usar el modelo.

3. **Configurar el Directorio del Modelo y la Configuración**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` es un diccionario que configura el modelo OpenVINO para priorizar baja latencia, usar un solo flujo de inferencia y no utilizar un directorio de caché.

4. **Cargar el Modelo**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Esta línea carga el modelo desde el directorio especificado, utilizando las configuraciones definidas anteriormente. También permite la ejecución remota de código si es necesario.

5. **Cargar el Tokenizador**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Esta línea carga el tokenizador, que se encarga de convertir texto en tokens que el modelo pueda entender.

6. **Configurar los Argumentos del Tokenizador**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Este diccionario especifica que no se deben añadir tokens especiales al resultado tokenizado.

7. **Definir el Mensaje**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Este string establece un mensaje de conversación donde el usuario le pide al asistente de IA que se presente.

8. **Tokenizar el Mensaje**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Esta línea convierte el mensaje en tokens que el modelo puede procesar, devolviendo el resultado como tensores de PyTorch.

9. **Generar una Respuesta**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Esta línea utiliza el modelo para generar una respuesta basada en los tokens de entrada, con un máximo de 1024 nuevos tokens.

10. **Decodificar la Respuesta**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Esta línea convierte los tokens generados de nuevo en un string legible, omitiendo cualquier token especial, y obtiene el primer resultado.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.