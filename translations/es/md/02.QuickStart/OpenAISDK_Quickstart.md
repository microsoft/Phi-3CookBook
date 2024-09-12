# Usar OpenAI SDK con Phi-3 en Azure AI y Azure ML

Usa el SDK de `openai` para consumir despliegues de Phi-3 en Azure AI y Azure ML. La familia de modelos Phi-3 en Azure AI y Azure ML ofrece una API compatible con la OpenAI Chat Completion API. Esto permite a los clientes y usuarios hacer una transición sin problemas desde los modelos de OpenAI a los LLMs de Phi-3.

La API puede usarse directamente con las bibliotecas cliente de OpenAI o herramientas de terceros, como LangChain o LlamaIndex.

El siguiente ejemplo muestra cómo hacer esta transición utilizando la Biblioteca de Python de OpenAI. Nota que Phi-3 solo soporta la API de chat completions.

Para usar el modelo Phi-3 con el SDK de OpenAI, necesitarás seguir unos pasos para configurar tu entorno y hacer llamadas a la API. Aquí tienes una guía para empezar:

1. **Instalar el SDK de OpenAI**: Primero, necesitas instalar el paquete de Python de OpenAI si aún no lo has hecho.
   ```bash
   pip install openai
   ```

2. **Configura tu clave API**: Asegúrate de tener tu clave API de OpenAI. Puedes configurarla en tus variables de entorno o directamente en tu código.
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **Hacer llamadas a la API**: Usa el SDK de OpenAI para interactuar con el modelo Phi-3. Aquí tienes un ejemplo de cómo hacer una solicitud de completado:
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **Manejar las respuestas**: Procesa las respuestas del modelo según sea necesario para tu aplicación.

Aquí tienes un ejemplo más detallado:
```python
import openai

# Configura tu clave API
openai.api_key = "your-api-key"

# Define el prompt
prompt = "Write a short story about a brave knight."

# Haz la llamada a la API
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Imprime la respuesta
print(response.choices[0].text.strip())
```

Esto generará una historia corta basada en el prompt proporcionado. Puedes ajustar el parámetro `max_tokens` para controlar la longitud del resultado.

[See A complete Notebook Sample for Phi-3 Models](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

Revisa la [documentación](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) para la familia de modelos Phi-3 en AI Studio y ML Studio para detalles sobre cómo provisionar puntos de inferencia, disponibilidad regional, precios y referencia del esquema de inferencia.

        Descargo de responsabilidad: La traducción fue realizada por un modelo de IA y puede no ser perfecta.
        Por favor, revise el resultado y haga las correcciones necesarias.