### Guidance-AI y Phi Models como Servicio (MaaS)
Estamos llevando [Guidance](https://github.com/guidance-ai/guidance) al endpoint sin servidor Phi-3.5-mini en Azure AI Studio para hacer que los resultados sean más predecibles al definir la estructura adaptada a una aplicación. Con Guidance, puedes eliminar reintentos costosos y, por ejemplo, restringir el modelo a seleccionar de listas predefinidas (por ejemplo, códigos médicos), limitar las salidas a citas directas del contexto proporcionado, o seguir cualquier regex. Guidance dirige el modelo token por token en la pila de inferencia, reduciendo el costo y la latencia en un 30-50%, lo que lo convierte en un complemento único y valioso para el [endpoint sin servidor Phi-3-mini](https://aka.ms/try-phi3.5mini).

## [**Guidance-AI**](https://github.com/guidance-ai/guidance) es un marco de trabajo diseñado para ayudar a los desarrolladores a crear y desplegar modelos de IA de manera eficiente. Se enfoca en proporcionar herramientas y mejores prácticas para construir aplicaciones de IA robustas.

Cuando se combina con **Phi Models como Servicio (MaaS)**, ofrece una solución poderosa para desplegar modelos de lenguaje pequeños (SLMs) que son tanto rentables como de alto rendimiento.

**Guidance-AI** es un marco de programación diseñado para ayudar a los desarrolladores a controlar y dirigir modelos de lenguaje grandes (LLMs) de manera más efectiva. Permite una estructuración precisa de los resultados, reduciendo la latencia y el costo en comparación con los métodos tradicionales de prompting o fine-tuning.

### Características Principales de Guidance-AI:
- **Control Eficiente**: Permite a los desarrolladores controlar cómo el modelo de lenguaje genera texto, asegurando resultados de alta calidad y relevancia.
- **Reducción de Costos y Latencia**: Optimiza el proceso de generación para ser más rentable y rápido.
- **Integración Flexible**: Funciona con varios backends, incluidos Transformers, llama.cpp, AzureAI, VertexAI y OpenAI.
- **Estructuras de Salida Ricas**: Soporta estructuras de salida complejas como condicionales, bucles y uso de herramientas, facilitando la generación de resultados claros y analizables.
- **Compatibilidad**: Permite que un solo programa de Guidance se ejecute en múltiples backends, mejorando la flexibilidad y facilidad de uso.

### Casos de Uso Ejemplares:
- **Generación Restringida**: Usando expresiones regulares y gramáticas libres de contexto para guiar la salida del modelo.
- **Integración de Herramientas**: Intercalando automáticamente control y generación, como usar una calculadora dentro de una tarea de generación de texto.

Para información más detallada y ejemplos, puedes consultar el [repositorio GitHub de Guidance-AI](https://github.com/guidance-ai/guidance).

[Consulta el Ejemplo de Phi-3.5](../../../../code/01.Introduce/guidance.ipynb)

### Características Principales de Phi Models:
1. **Rentable**: Diseñado para ser asequible manteniendo un alto rendimiento.
2. **Baja Latencia**: Ideal para aplicaciones en tiempo real que requieren respuestas rápidas.
3. **Flexibilidad**: Puede ser desplegado en varios entornos, incluyendo la nube, el edge y escenarios offline.
4. **Personalización**: Los modelos pueden ser ajustados con datos específicos del dominio para mejorar el rendimiento.
5. **Seguridad y Cumplimiento**: Construido con los principios de IA de Microsoft, asegurando responsabilidad, transparencia, equidad, fiabilidad, seguridad, privacidad e inclusión.

### Phi Models como Servicio (MaaS):
Los modelos Phi están disponibles a través de un sistema de facturación de pago por uso mediante APIs de inferencia, lo que facilita su integración en tus aplicaciones sin costos iniciales significativos.

### Comenzando con Phi-3:
Para comenzar a usar los modelos Phi, puedes explorar el [catálogo de modelos de Azure AI](https://ai.azure.com/explore/models) o los [Modelos del Marketplace de GitHub](https://github.com/marketplace/models) que ofrecen modelos preconstruidos y personalizables. Además, puedes usar herramientas como [Azure AI Studio](https://ai.azure.com) para desarrollar y desplegar tus aplicaciones de IA.

### Recursos
[Notebook de Ejemplo para comenzar con Guidance](../../../../code/01.Introduce/guidance.ipynb)

