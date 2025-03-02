## Ajuste fino vs RAG

## Generación Aumentada por Recuperación

RAG es la combinación de recuperación de datos + generación de texto. Los datos estructurados y no estructurados de la empresa se almacenan en la base de datos vectorial. Al buscar contenido relevante, se encuentra el resumen y contenido relacionados para formar un contexto, y se combina con la capacidad de finalización de texto de LLM/SLM para generar contenido.

## Proceso de RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.es.png)

## Ajuste fino
El ajuste fino se basa en la mejora de un modelo en particular. No es necesario comenzar desde el algoritmo del modelo, pero se necesita acumular datos de manera continua. Si buscas una terminología más precisa y una expresión de lenguaje específica para aplicaciones industriales, el ajuste fino es tu mejor opción. Sin embargo, si tus datos cambian con frecuencia, el ajuste fino puede volverse complicado.

## Cómo elegir
Si nuestra respuesta requiere la introducción de datos externos, RAG es la mejor elección.

Si necesitas generar conocimiento industrial estable y preciso, el ajuste fino será una buena opción. RAG da prioridad a extraer contenido relevante, pero podría no captar siempre las sutilezas especializadas.

El ajuste fino requiere un conjunto de datos de alta calidad, y si se trata de un rango pequeño de datos, no habrá mucha diferencia. RAG es más flexible.  
El ajuste fino es como una caja negra, una especie de metafísica, y es difícil entender su mecanismo interno. Pero RAG facilita encontrar la fuente de los datos, lo que permite ajustar eficazmente alucinaciones o errores de contenido y ofrecer una mejor transparencia.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.