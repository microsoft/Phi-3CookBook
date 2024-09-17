# Seguridad de la IA para modelos Phi-3

La familia de modelos Phi-3 se desarrolló de acuerdo con el [Estándar de IA Responsable de Microsoft](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE5cmFl?culture=en-us&country=us), que es un conjunto de requisitos a nivel de la empresa basado en los siguientes seis principios: responsabilidad, transparencia, equidad, fiabilidad y seguridad, privacidad y seguridad, e inclusividad que forman los [principios de IA Responsable de Microsoft](https://www.microsoft.com/ai/responsible-ai).

Al igual que los modelos Phi-3 anteriores, se adoptó un enfoque multifacético de evaluación de seguridad y post-entrenamiento de seguridad, con medidas adicionales para tener en cuenta las capacidades multilingües de esta versión. Nuestro enfoque para el entrenamiento y evaluaciones de seguridad, incluyendo pruebas en múltiples idiomas y categorías de riesgo, se describe en el [Documento de Post-Entrenamiento de Seguridad de Phi-3](https://arxiv.org/abs/2407.13833). Aunque los modelos Phi-3 se benefician de este enfoque, los desarrolladores deben aplicar las mejores prácticas de IA responsable, incluyendo mapear, medir y mitigar los riesgos asociados con su caso de uso específico y contexto cultural y lingüístico.

## Mejores Prácticas

Al igual que otros modelos, la familia de modelos Phi puede comportarse de maneras que sean injustas, poco fiables u ofensivas.

Algunos de los comportamientos limitantes de SLM y LLM que debes tener en cuenta incluyen:

- **Calidad del Servicio:** Los modelos Phi están entrenados principalmente en texto en inglés. Los idiomas distintos al inglés experimentarán un peor rendimiento. Las variedades del inglés con menos representación en los datos de entrenamiento podrían experimentar un rendimiento peor que el inglés americano estándar.
- **Representación de Daños y Perpetuación de Estereotipos:** Estos modelos pueden sobre-representar o infra-representar a grupos de personas, borrar la representación de algunos grupos, o reforzar estereotipos degradantes o negativos. A pesar del post-entrenamiento de seguridad, estas limitaciones pueden seguir presentes debido a los diferentes niveles de representación de distintos grupos o la prevalencia de ejemplos de estereotipos negativos en los datos de entrenamiento que reflejan patrones del mundo real y sesgos sociales.
- **Contenido Inapropiado u Ofensivo:** Estos modelos pueden producir otros tipos de contenido inapropiado u ofensivo, lo que puede hacer que sea inapropiado desplegarlos en contextos sensibles sin mitigaciones adicionales específicas para el caso de uso.
- **Fiabilidad de la Información:** Los modelos de lenguaje pueden generar contenido sin sentido o fabricar contenido que pueda sonar razonable pero que sea inexacto o desactualizado.
- **Alcance Limitado para Código:** La mayoría de los datos de entrenamiento de Phi-3 están basados en Python y usan paquetes comunes como "typing, math, random, collections, datetime, itertools". Si el modelo genera scripts de Python que utilizan otros paquetes o scripts en otros lenguajes, recomendamos encarecidamente a los usuarios verificar manualmente todos los usos de API.

Los desarrolladores deben aplicar las mejores prácticas de IA responsable y son responsables de asegurarse de que un caso de uso específico cumpla con las leyes y regulaciones relevantes (por ejemplo, privacidad, comercio, etc.).

## Consideraciones de IA Responsable

Al igual que otros modelos de lenguaje, los modelos de la serie Phi pueden comportarse de maneras que sean injustas, poco fiables u ofensivas. Algunos de los comportamientos limitantes que debes tener en cuenta incluyen:

**Calidad del Servicio:** Los modelos Phi están entrenados principalmente en texto en inglés. Los idiomas distintos al inglés experimentarán un peor rendimiento. Las variedades del inglés con menos representación en los datos de entrenamiento podrían experimentar un rendimiento peor que el inglés americano estándar.

**Representación de Daños y Perpetuación de Estereotipos:** Estos modelos pueden sobre-representar o infra-representar a grupos de personas, borrar la representación de algunos grupos, o reforzar estereotipos degradantes o negativos. A pesar del post-entrenamiento de seguridad, estas limitaciones pueden seguir presentes debido a los diferentes niveles de representación de distintos grupos o la prevalencia de ejemplos de estereotipos negativos en los datos de entrenamiento que reflejan patrones del mundo real y sesgos sociales.

**Contenido Inapropiado u Ofensivo:** Estos modelos pueden producir otros tipos de contenido inapropiado u ofensivo, lo que puede hacer que sea inapropiado desplegarlos en contextos sensibles sin mitigaciones adicionales específicas para el caso de uso. Fiabilidad de la Información: Los modelos de lenguaje pueden generar contenido sin sentido o fabricar contenido que pueda sonar razonable pero que sea inexacto o desactualizado.

**Alcance Limitado para Código:** La mayoría de los datos de entrenamiento de Phi-3 están basados en Python y usan paquetes comunes como "typing, math, random, collections, datetime, itertools". Si el modelo genera scripts de Python que utilizan otros paquetes o scripts en otros lenguajes, recomendamos encarecidamente a los usuarios verificar manualmente todos los usos de API.

Los desarrolladores deben aplicar las mejores prácticas de IA responsable y son responsables de asegurarse de que un caso de uso específico cumpla con las leyes y regulaciones relevantes (por ejemplo, privacidad, comercio, etc.). Áreas importantes para considerar incluyen:

**Asignación:** Los modelos pueden no ser adecuados para escenarios que podrían tener un impacto consecuente en el estado legal o la asignación de recursos u oportunidades de vida (por ejemplo, vivienda, empleo, crédito, etc.) sin evaluaciones adicionales y técnicas adicionales de desescalado.

**Escenarios de Alto Riesgo:** Los desarrolladores deben evaluar la idoneidad de usar modelos en escenarios de alto riesgo donde salidas injustas, poco fiables u ofensivas podrían ser extremadamente costosas o causar daño. Esto incluye proporcionar asesoramiento en dominios sensibles o expertos donde la precisión y fiabilidad son críticas (por ejemplo, asesoramiento legal o de salud). Se deben implementar salvaguardas adicionales a nivel de aplicación de acuerdo con el contexto de implementación.

**Desinformación:** Los modelos pueden producir información inexacta. Los desarrolladores deben seguir las mejores prácticas de transparencia e informar a los usuarios finales que están interactuando con un sistema de IA. A nivel de aplicación, los desarrolladores pueden construir mecanismos de retroalimentación y tuberías para fundamentar las respuestas en información contextual específica del caso de uso, una técnica conocida como Generación Aumentada por Recuperación (RAG).

**Generación de Contenido Dañino:** Los desarrolladores deben evaluar las salidas para su contexto y usar clasificadores de seguridad disponibles o soluciones personalizadas adecuadas para su caso de uso.

**Uso Indebido:** Otras formas de uso indebido como fraude, spam o producción de malware pueden ser posibles, y los desarrolladores deben asegurarse de que sus aplicaciones no violen las leyes y regulaciones aplicables.

### Ajuste Fino y Seguridad de Contenido de IA

Después de ajustar finamente un modelo, recomendamos encarecidamente aprovechar las medidas de [Seguridad de Contenido de Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) para monitorear el contenido generado por los modelos, identificar y bloquear posibles riesgos, amenazas y problemas de calidad.

![Phi3AISafety](../../../../translated_images/phi3aisafety.dc76a5bdb07ffc178e8e6d6be94d55a847ad1477d379bc28055823c777e3b06f.es.png)

[Seguridad de Contenido de Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) soporta tanto contenido de texto como de imagen. Puede ser desplegado en la nube, contenedores desconectados y en dispositivos de borde/embebidos.

## Descripción General de la Seguridad de Contenido de Azure AI

La Seguridad de Contenido de Azure AI no es una solución única para todos; puede ser personalizada para alinearse con las políticas específicas de las empresas. Además, sus modelos multilingües le permiten entender múltiples idiomas simultáneamente.

![AIContentSafety](../../../../translated_images/AIcontentsafety.2319fe2f8154f2594e16643d4a4696100b7bb74af96b7a82b8f3327618d81122.es.png)

- **Seguridad de Contenido de Azure AI**
- **Microsoft Developer**
- **5 videos**

El servicio de Seguridad de Contenido de Azure AI detecta contenido dañino generado por usuarios y por IA en aplicaciones y servicios. Incluye APIs de texto e imagen que permiten detectar material dañino o inapropiado.

[Lista de Reproducción de Seguridad de Contenido de IA](https://www.youtube.com/playlist?list=PLlrxD0HtieHjaQ9bJjyp1T7FeCbmVcPkQ)

