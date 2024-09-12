## Ajuste fino vs RAG

## Generación Aumentada por Recuperación

RAG es la combinación de recuperación de datos y generación de texto. Los datos estructurados y no estructurados de la empresa se almacenan en la base de datos vectorial. Al buscar contenido relevante, se encuentra el resumen y contenido pertinente para formar un contexto, y se combina con la capacidad de completar texto de LLM/SLM para generar contenido.

## Proceso RAG
![FinetuningvsRAG](../../../../translated_images/rag.20124d5657be35073dd1dbc93411c24ed912cbcc3bab5d37d28e648e6f175b7e.es.png)

## Ajuste fino
El ajuste fino se basa en la mejora de un modelo específico. No necesita comenzar desde el algoritmo del modelo, pero requiere acumulación continua de datos. Si deseas una terminología y expresión de lenguaje más precisa en aplicaciones industriales, el ajuste fino es tu mejor opción. Pero si tus datos cambian con frecuencia, el ajuste fino puede volverse complicado.

## Cómo elegir
Si nuestra respuesta requiere la introducción de datos externos, RAG es la mejor elección.

Si necesitas output estable y preciso de conocimiento industrial, el ajuste fino será una buena opción. RAG prioriza extraer contenido relevante, pero puede no captar siempre los matices especializados.

El ajuste fino requiere un conjunto de datos de alta calidad, y si es solo un pequeño rango de datos, no hará mucha diferencia. RAG es más flexible.
El ajuste fino es una caja negra, una metafísica, y es difícil entender el mecanismo interno. Pero RAG puede facilitar encontrar la fuente de los datos, ajustando efectivamente alucinaciones o errores de contenido y proporcionando mejor transparencia.

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.