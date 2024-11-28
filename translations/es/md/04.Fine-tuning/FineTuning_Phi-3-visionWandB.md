# Resumen del Proyecto Phi-3-Vision-128K-Instruct

## El Modelo

El Phi-3-Vision-128K-Instruct, un modelo multimodal ligero y de última generación, es el núcleo de este proyecto. Es parte de la familia de modelos Phi-3 y soporta una longitud de contexto de hasta 128,000 tokens. El modelo fue entrenado en un conjunto de datos diverso que incluye datos sintéticos y sitios web públicos cuidadosamente filtrados, enfatizando contenido de alta calidad y con un enfoque intensivo en el razonamiento. El proceso de entrenamiento incluyó ajuste fino supervisado y optimización directa de preferencias para asegurar una adherencia precisa a las instrucciones, así como robustas medidas de seguridad.

## Crear datos de muestra es crucial por varias razones:

1. **Pruebas**: Los datos de muestra te permiten probar tu aplicación en diversos escenarios sin afectar los datos reales. Esto es especialmente importante en las fases de desarrollo y pruebas.

2. **Optimización de Rendimiento**: Con datos de muestra que imitan la escala y complejidad de los datos reales, puedes identificar cuellos de botella en el rendimiento y optimizar tu aplicación en consecuencia.

3. **Prototipado**: Los datos de muestra pueden usarse para crear prototipos y maquetas, lo cual puede ayudar a entender los requisitos del usuario y obtener retroalimentación.

4. **Análisis de Datos**: En ciencia de datos, los datos de muestra se usan a menudo para análisis exploratorio de datos, entrenamiento de modelos y pruebas de algoritmos.

5. **Seguridad**: Usar datos de muestra en entornos de desarrollo y pruebas puede ayudar a prevenir filtraciones accidentales de datos sensibles reales.

6. **Aprendizaje**: Si estás aprendiendo una nueva tecnología o herramienta, trabajar con datos de muestra puede proporcionar una manera práctica de aplicar lo que has aprendido.

Recuerda, la calidad de tus datos de muestra puede impactar significativamente estas actividades. Deberían ser lo más cercanos posible a los datos reales en términos de estructura y variabilidad.

### Creación de Datos de Muestra
[Generar Script de Conjunto de Datos](./CreatingSampleData.md)

## Conjunto de Datos

Un buen ejemplo de conjunto de datos de muestra es [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible en Huggingface). 
El conjunto de datos de muestra de productos Burberry junto con metadatos sobre la categoría del producto, precio y título con un total de 3,040 filas, cada una representando un producto único. Este conjunto de datos nos permite probar la capacidad del modelo para entender e interpretar datos visuales, generando textos descriptivos que capturen detalles visuales intrincados y características específicas de la marca.

**Nota:** Puedes usar cualquier conjunto de datos que incluya imágenes.

## Razonamiento Complejo

El modelo necesita razonar sobre los precios y nombres dados solo la imagen. Esto requiere que el modelo no solo reconozca características visuales sino también entienda sus implicaciones en términos de valor del producto y marca. Al sintetizar descripciones textuales precisas a partir de imágenes, el proyecto destaca el potencial de integrar datos visuales para mejorar el rendimiento y la versatilidad de los modelos en aplicaciones del mundo real.

## Arquitectura de Phi-3 Vision

La arquitectura del modelo es una versión multimodal de un Phi-3. Procesa tanto datos de texto como de imagen, integrando estas entradas en una secuencia unificada para tareas de comprensión y generación completas. El modelo utiliza capas de incrustación separadas para texto e imágenes. Los tokens de texto se convierten en vectores densos, mientras que las imágenes se procesan a través de un modelo de visión CLIP para extraer incrustaciones de características. Estas incrustaciones de imagen se proyectan luego para coincidir con las dimensiones de las incrustaciones de texto, asegurando que puedan integrarse sin problemas.

## Integración de Incrustaciones de Texto e Imagen

Tokens especiales dentro de la secuencia de texto indican dónde deben insertarse las incrustaciones de imagen. Durante el procesamiento, estos tokens especiales se reemplazan con las correspondientes incrustaciones de imagen, permitiendo al modelo manejar texto e imágenes como una única secuencia. El prompt para nuestro conjunto de datos se formatea usando el token especial <|image|> de la siguiente manera:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Código de Ejemplo
- [Script de Entrenamiento de Phi-3-Vision](../../../../code/04.Finetuning/Phi-3-vision-Trainingscript.py)
- [Ejemplo de Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.