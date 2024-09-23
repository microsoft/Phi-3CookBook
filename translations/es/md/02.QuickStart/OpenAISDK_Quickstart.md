# Usa el SDK de OpenAI con Phi-3 en Azure AI y Azure ML

Usa el SDK de `openai` para consumir despliegues de Phi-3 en Azure AI y Azure ML. La familia de modelos Phi-3 en Azure AI y Azure ML ofrece una API compatible con la API de Chat Completion de OpenAI. Permite a los clientes y usuarios hacer la transición sin problemas de los modelos de OpenAI a los LLMs de Phi-3.

La API se puede usar directamente con las bibliotecas cliente de OpenAI o herramientas de terceros, como LangChain o LlamaIndex.

El siguiente ejemplo muestra cómo hacer esta transición utilizando la Biblioteca de Python de OpenAI. Observa que Phi-3 solo admite la API de completaciones de chat.

Para usar el modelo Phi-3 con el SDK de OpenAI, necesitarás seguir algunos pasos para configurar tu entorno y realizar llamadas a la API. Aquí tienes una guía para ayudarte a comenzar:

1. **Instala el SDK de OpenAI**: Primero, necesitarás instalar el paquete de Python de OpenAI si aún no lo has hecho.
   ```bash
   pip install openai
   ```

2. **Configura tu clave API**: Asegúrate de tener tu clave API de OpenAI. Puedes configurarla en tus variables de entorno o directamente en tu código.
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **Realiza llamadas a la API**: Usa el SDK de OpenAI para interactuar con el modelo Phi-3. Aquí tienes un ejemplo de cómo hacer una solicitud de completación:
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **Maneja las respuestas**: Procesa las respuestas del modelo según sea necesario para tu aplicación.

Aquí tienes un ejemplo más detallado:
```python
import openai

# Configura tu clave API
openai.api_key = "your-api-key"

# Define el prompt
prompt = "Write a short story about a brave knight."

# Realiza la llamada a la API
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Imprime la respuesta
print(response.choices[0].text.strip())
```

Esto generará una historia corta basada en el prompt proporcionado. Puedes ajustar el parámetro `max_tokens` para controlar la longitud de la salida.

[Ver un ejemplo completo en Notebook para modelos Phi-3](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

Revisa la [documentación](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) para la familia de modelos Phi-3 en AI Studio y ML Studio para obtener detalles sobre cómo provisionar puntos finales de inferencia, disponibilidad regional, precios y referencia de esquema de inferencia.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.