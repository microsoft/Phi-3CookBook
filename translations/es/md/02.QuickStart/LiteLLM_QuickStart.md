Usar [LiteLLM](https://docs.litellm.ai/) para el modelo Phi-3 puede ser una gran elección, especialmente si buscas integrarlo en varias aplicaciones. LiteLLM actúa como un middleware que traduce llamadas API en solicitudes compatibles con diferentes modelos, incluyendo Phi-3.

Phi-3 es un pequeño modelo de lenguaje (SLM) desarrollado por Microsoft, diseñado para ser eficiente y capaz de ejecutarse en máquinas con recursos limitados. Puede operar en CPUs con soporte AVX y con tan solo 4 GB de RAM, lo que lo convierte en una buena opción para inferencia local sin necesidad de GPUs.

Aquí tienes algunos pasos para comenzar con LiteLLM para Phi-3:

1. **Instalar LiteLLM**: Puedes instalar LiteLLM usando pip:
   ```bash
   pip install litellm
   ```

2. **Configurar Variables de Entorno**: Configura tus claves API y otras variables de entorno necesarias.
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. **Realizar Llamadas API**: Usa LiteLLM para realizar llamadas API al modelo Phi-3.
   ```python
   from litellm import completion

   response = completion(
       model="phi-3",
       messages=[{"role": "user", "content": "Hello, how are you?"}]
   )
   print(response)
   ```

4. **Integración**: Puedes integrar LiteLLM con varias plataformas como Nextcloud Assistant, permitiéndote usar Phi-3 para generación de texto y otras tareas.

**Ejemplo Completo de Código para LLMLite**
[Ejemplo de Código para LLMLite](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/litellm.ipynb)

        **Descargo de responsabilidad**:
        Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.