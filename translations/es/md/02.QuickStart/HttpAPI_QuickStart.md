# Uso de la API de Azure con Phi-3

Este notebook muestra ejemplos de cómo utilizar las APIs Phi-3 ofrecidas por Microsoft Azure AI y Azure ML. Cubriremos:  
* Uso de la API de solicitudes HTTP para modelos preentrenados y de chat de Phi-3 en CLI
* Uso de la API de solicitudes HTTP para modelos preentrenados y de chat de Phi-3 en Python

Claro, aquí hay una descripción general del **Uso de la API de Solicitudes HTTP en CLI**:

## Uso de la API de Solicitudes HTTP en CLI

### Conceptos Básicos

Para usar la API REST, necesitarás tener una URL de Endpoint y una Clave de Autenticación asociada con ese endpoint. Estos pueden ser adquiridos en pasos anteriores.

En este ejemplo de finalización de chat, usamos una simple llamada `curl` para ilustrar. Hay tres componentes principales:

1. **El `host-url`**: Esta es tu URL de endpoint con el esquema de finalización de chat `/v1/chat/completions`.
2. **El `headers`**: Esto define el tipo de contenido así como tu clave de API.
3. **El `payload` o `data`**: Esto incluye los detalles de tu prompt y los hiperparámetros del modelo.

### Ejemplo

Aquí hay un ejemplo de cómo hacer una solicitud de finalización de chat usando `curl`:

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "max_tokens": 50
}'
```

### Desglose

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY` con tu clave de API real.
- **Payload**: Personaliza el payload según tus necesidades, incluyendo diferentes prompts, modelos y parámetros.

Consulta el ejemplo [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

Revisa la [documentación](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) para la familia de modelos Phi-3 en AI Studio y ML Studio para obtener detalles sobre cómo aprovisionar endpoints de inferencia, disponibilidad regional, precios y referencia de esquemas de inferencia.

        **Descargo de responsabilidad**: 
        Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.