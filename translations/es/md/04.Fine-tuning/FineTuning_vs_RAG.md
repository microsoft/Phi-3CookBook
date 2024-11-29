## Ajuste fino vs RAG

## Generación Aumentada por Recuperación

RAG es la recuperación de datos + generación de texto. Los datos estructurados y no estructurados de la empresa se almacenan en la base de datos vectorial. Al buscar contenido relevante, se encuentra el resumen y contenido relevante para formar un contexto, y se combina la capacidad de completado de texto de LLM/SLM para generar contenido.

## Proceso RAG
![FinetuningvsRAG](../../../../translated_images/rag.20124d5657be35073dd1dbc93411c24ed912cbcc3bab5d37d28e648e6f175b7e.es.png)

## Ajuste fino
El ajuste fino se basa en la mejora de un modelo determinado. No es necesario comenzar con el algoritmo del modelo, pero se necesita acumular datos de manera continua. Si deseas una terminología y expresión de lenguaje más precisa en aplicaciones industriales, el ajuste fino es tu mejor opción. Pero si tus datos cambian frecuentemente, el ajuste fino puede volverse complicado.

## Cómo elegir
Si nuestra respuesta requiere la introducción de datos externos, RAG es la mejor opción.

Si necesitas generar conocimiento industrial estable y preciso, el ajuste fino será una buena elección. RAG prioriza extraer contenido relevante, pero podría no captar siempre los matices especializados.

El ajuste fino requiere un conjunto de datos de alta calidad, y si solo es un pequeño rango de datos, no hará mucha diferencia. RAG es más flexible.
El ajuste fino es una caja negra, una metafísica, y es difícil entender el mecanismo interno. Pero RAG puede facilitar encontrar la fuente de los datos, ajustando efectivamente alucinaciones o errores de contenido y proporcionando mejor transparencia.

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.