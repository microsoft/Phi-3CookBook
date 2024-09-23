# Usar la API de Azure con Phi-3

Este cuaderno muestra ejemplos de cómo utilizar las APIs Phi-3 ofrecidas por Microsoft Azure AI y Azure ML. Cubriremos:  
* Uso de la API de solicitudes HTTP para los modelos preentrenados y de chat de Phi-3 en CLI
* Uso de la API de solicitudes HTTP para los modelos preentrenados y de chat de Phi-3 en Python

Claro, aquí tienes una visión general de **Uso de la API de Solicitudes HTTP en CLI**:

## Uso de la API de Solicitudes HTTP en CLI

### Conceptos Básicos

Para usar la API REST, necesitarás tener una URL de Endpoint y una Clave de Autenticación asociada con ese endpoint. Estos se pueden adquirir de pasos anteriores.

En este ejemplo de completado de chat, utilizamos una simple llamada `curl` para ilustrar. Hay tres componentes principales:

1. **El `host-url`**: Esta es tu URL de endpoint con el esquema de completado de chat `/v1/chat/completions`.
2. **Los `headers`**: Esto define el tipo de contenido así como tu clave de API.
3. **El `payload` o `data`**: Esto incluye los detalles de tu prompt y los hiperparámetros del modelo.

### Ejemplo

Aquí tienes un ejemplo de cómo hacer una solicitud de completado de chat usando `curl`:

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}],
  "max_tokens": 50
}'
```

### Desglose

- **`-X POST`**: Especifica el método HTTP a usar, que en este caso es POST.
- **`https://api.example.com/v1/chat/completions`**: La URL del endpoint.
- **`-H "Content-Type: application/json"`**: Establece el tipo de contenido a JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Añade el encabezado de autorización con tu clave de API.
- **`-d '{...}'`**: El payload de datos, que incluye el modelo, los mensajes y otros parámetros.

### Consejos

- **URL del Endpoint**: Asegúrate de reemplazar `https://api.example.com` con tu URL de endpoint real.
- **Clave de API**: Reemplaza `YOUR_API_KEY` con tu clave de API real.
- **Payload**: Personaliza el payload según tus necesidades, incluyendo diferentes prompts, modelos y parámetros.

Consulta el ejemplo [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

Revisa la [documentación](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) para la familia de modelos Phi-3 en AI Studio y ML Studio para detalles sobre cómo aprovisionar endpoints de inferencia, disponibilidad regional, precios y referencia de esquema de inferencia.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.