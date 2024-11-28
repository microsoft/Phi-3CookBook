# **Deja que Phi-3 se convierta en un experto de la industria**

Para integrar el modelo Phi-3 en una industria, necesitas añadir datos de negocios de la industria al modelo Phi-3. Tenemos dos opciones diferentes, la primera es RAG (Generación Aumentada por Recuperación) y la segunda es el Ajuste Fino.

## **RAG vs Ajuste Fino**

### **Generación Aumentada por Recuperación**

RAG es la recuperación de datos + generación de texto. Los datos estructurados y no estructurados de la empresa se almacenan en la base de datos vectorial. Al buscar contenido relevante, se encuentra el resumen y contenido relevante para formar un contexto, y se combina la capacidad de completado de texto de LLM/SLM para generar contenido.

### **Ajuste Fino**

El ajuste fino se basa en la mejora de un modelo determinado. No necesita comenzar con el algoritmo del modelo, pero los datos deben acumularse continuamente. Si deseas una terminología y expresión de lenguaje más precisas en aplicaciones industriales, el ajuste fino es tu mejor opción. Pero si tus datos cambian con frecuencia, el ajuste fino puede volverse complicado.

### **Cómo elegir**

1. Si nuestra respuesta requiere la introducción de datos externos, RAG es la mejor opción.

2. Si necesitas producir conocimientos industriales estables y precisos, el ajuste fino será una buena elección. RAG prioriza extraer contenido relevante, pero puede que no siempre capture los matices especializados.

3. El ajuste fino requiere un conjunto de datos de alta calidad, y si solo se trata de un pequeño rango de datos, no hará mucha diferencia. RAG es más flexible.

4. El ajuste fino es una caja negra, una metafísica, y es difícil entender el mecanismo interno. Pero RAG puede facilitar encontrar la fuente de los datos, ajustando eficazmente alucinaciones o errores de contenido y proporcionando mejor transparencia.

### **Escenarios**

1. Industrias verticales que requieren vocabulario y expresiones profesionales específicas, ***Ajuste Fino*** será la mejor opción.

2. Sistema de preguntas y respuestas, que involucra la síntesis de diferentes puntos de conocimiento, ***RAG*** será la mejor opción.

3. La combinación de flujo de negocios automatizado ***RAG + Ajuste Fino*** es la mejor opción.

## **Cómo usar RAG**

![rag](../../../../translated_images/RAG.099c3f3bc644ff2d8bb61d2fbc20a532958c6a1e4d1cb65a84edeb4ffe618bbb.es.png)

Una base de datos vectorial es una colección de datos almacenados en forma matemática. Las bases de datos vectoriales facilitan que los modelos de aprendizaje automático recuerden entradas anteriores, permitiendo que el aprendizaje automático se utilice para casos de uso como búsqueda, recomendaciones y generación de texto. Los datos pueden identificarse basándose en métricas de similitud en lugar de coincidencias exactas, permitiendo que los modelos informáticos comprendan el contexto de los datos.

La base de datos vectorial es la clave para realizar RAG. Podemos convertir datos en almacenamiento vectorial a través de modelos vectoriales como text-embedding-3, jina-ai-embedding, etc.

Aprende más sobre cómo crear una aplicación RAG [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Cómo usar el Ajuste Fino**

Los algoritmos comúnmente utilizados en el Ajuste Fino son Lora y QLora. ¿Cómo elegir?
- [Learn More with this sample notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora y QLora**

![lora](../../../../translated_images/qlora.ea4ce73918753819dc9e9cf1524ac40faa555d6b21168b667064be93c3913bbe.es.png)

LoRA (Adaptación de Bajo Rango) y QLoRA (Adaptación de Bajo Rango Cuantizada) son técnicas utilizadas para ajustar finamente grandes modelos de lenguaje (LLMs) utilizando Ajuste Fino Eficiente en Parámetros (PEFT). Las técnicas PEFT están diseñadas para entrenar modelos de manera más eficiente que los métodos tradicionales.
LoRA es una técnica de ajuste fino independiente que reduce la huella de memoria aplicando una aproximación de bajo rango a la matriz de actualización de pesos. Ofrece tiempos de entrenamiento rápidos y mantiene un rendimiento cercano a los métodos de ajuste fino tradicionales.

QLoRA es una versión extendida de LoRA que incorpora técnicas de cuantización para reducir aún más el uso de memoria. QLoRA cuantiza la precisión de los parámetros de peso en el LLM preentrenado a una precisión de 4 bits, lo cual es más eficiente en términos de memoria que LoRA. Sin embargo, el entrenamiento de QLoRA es aproximadamente un 30% más lento que el de LoRA debido a los pasos adicionales de cuantización y des-cuantización.

QLoRA utiliza LoRA como un accesorio para corregir los errores introducidos durante los errores de cuantización. QLoRA permite el ajuste fino de modelos masivos con miles de millones de parámetros en GPUs relativamente pequeñas y altamente disponibles. Por ejemplo, QLoRA puede ajustar finamente un modelo de 70B de parámetros que requiere 36 GPUs con solo 2.

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.