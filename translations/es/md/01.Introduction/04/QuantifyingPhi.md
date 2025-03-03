# **Cuantificación de la Familia Phi**

La cuantificación de modelos se refiere al proceso de mapear los parámetros (como pesos y valores de activación) en un modelo de red neuronal desde un rango de valores amplio (generalmente un rango continuo) a un rango de valores finito más pequeño. Esta tecnología puede reducir el tamaño y la complejidad computacional del modelo, además de mejorar la eficiencia operativa del modelo en entornos con recursos limitados, como dispositivos móviles o sistemas embebidos. La cuantificación de modelos logra la compresión al reducir la precisión de los parámetros, pero también introduce una cierta pérdida de precisión. Por lo tanto, en el proceso de cuantificación, es necesario equilibrar el tamaño del modelo, la complejidad computacional y la precisión. Los métodos de cuantificación más comunes incluyen cuantificación de punto fijo, cuantificación de punto flotante, etc. Puedes elegir la estrategia de cuantificación adecuada según el escenario y las necesidades específicas.

Esperamos desplegar el modelo GenAI en dispositivos de borde y permitir que más dispositivos participen en escenarios de GenAI, como dispositivos móviles, PC con IA/PC Copilot y dispositivos IoT tradicionales. A través del modelo cuantificado, podemos desplegarlo en diferentes dispositivos de borde según las características de cada uno. Combinado con el marco de aceleración del modelo y el modelo cuantificado proporcionado por los fabricantes de hardware, podemos construir mejores escenarios de aplicación SLM.

En el escenario de cuantificación, tenemos diferentes precisiones (INT4, INT8, FP16, FP32). A continuación, se presenta una explicación de las precisiones de cuantificación más comunes:

### **INT4**

La cuantificación INT4 es un método radical que cuantifica los pesos y valores de activación del modelo en enteros de 4 bits. La cuantificación INT4 generalmente resulta en una mayor pérdida de precisión debido al rango de representación más pequeño y a la menor precisión. Sin embargo, en comparación con la cuantificación INT8, la cuantificación INT4 puede reducir aún más los requisitos de almacenamiento y la complejidad computacional del modelo. Cabe señalar que la cuantificación INT4 es relativamente rara en aplicaciones prácticas, ya que una precisión demasiado baja puede causar una degradación significativa en el rendimiento del modelo. Además, no todo el hardware admite operaciones INT4, por lo que es necesario considerar la compatibilidad del hardware al elegir un método de cuantificación.

### **INT8**

La cuantificación INT8 es el proceso de convertir los pesos y activaciones de un modelo de números de punto flotante a enteros de 8 bits. Aunque el rango numérico representado por los enteros INT8 es más pequeño y menos preciso, puede reducir significativamente los requisitos de almacenamiento y cálculo. En la cuantificación INT8, los pesos y valores de activación del modelo pasan por un proceso de cuantificación, que incluye escalado y desplazamiento, para preservar la mayor cantidad posible de información original de punto flotante. Durante la inferencia, estos valores cuantificados se des-cuantifican de nuevo a números de punto flotante para el cálculo y luego se vuelven a cuantificar a INT8 para el siguiente paso. Este método puede proporcionar suficiente precisión en la mayoría de las aplicaciones mientras mantiene una alta eficiencia computacional.

### **FP16**

El formato FP16, es decir, números de punto flotante de 16 bits (float16), reduce el uso de memoria a la mitad en comparación con números de punto flotante de 32 bits (float32), lo que tiene ventajas significativas en aplicaciones de aprendizaje profundo a gran escala. El formato FP16 permite cargar modelos más grandes o procesar más datos dentro de las mismas limitaciones de memoria de la GPU. A medida que el hardware moderno de GPU continúa soportando operaciones FP16, usar el formato FP16 también puede traer mejoras en la velocidad de cálculo. Sin embargo, el formato FP16 también tiene sus desventajas inherentes, como una menor precisión, lo que puede llevar a inestabilidad numérica o pérdida de precisión en algunos casos.

### **FP32**

El formato FP32 proporciona una mayor precisión y puede representar con exactitud un amplio rango de valores. En escenarios donde se realizan operaciones matemáticas complejas o se requieren resultados de alta precisión, se prefiere el formato FP32. Sin embargo, una alta precisión también implica un mayor uso de memoria y un tiempo de cálculo más largo. Para modelos de aprendizaje profundo a gran escala, especialmente cuando hay muchos parámetros del modelo y una enorme cantidad de datos, el formato FP32 puede causar insuficiencia de memoria en la GPU o una disminución en la velocidad de inferencia.

En dispositivos móviles o dispositivos IoT, podemos convertir modelos Phi-3.x a INT4, mientras que las PC con IA / PC Copilot pueden usar precisiones más altas como INT8, FP16, FP32.

Actualmente, diferentes fabricantes de hardware tienen distintos marcos para soportar modelos generativos, como OpenVINO de Intel, QNN de Qualcomm, MLX de Apple y CUDA de Nvidia, entre otros, que se combinan con la cuantificación de modelos para completar el despliegue local.

En términos de tecnología, tenemos diferentes formatos compatibles después de la cuantificación, como los formatos PyTorch / Tensorflow, GGUF y ONNX. He realizado una comparación de formatos y escenarios de aplicación entre GGUF y ONNX. Aquí recomiendo el formato de cuantificación ONNX, que tiene un buen soporte desde el marco del modelo hasta el hardware. En este capítulo, nos centraremos en ONNX Runtime para GenAI, OpenVINO y Apple MLX para realizar la cuantificación de modelos (si tienes una mejor manera, también puedes compartirla con nosotros enviando un PR).

**Este capítulo incluye**

1. [Cuantificación de Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificación de Phi-3.5 / 4 usando extensiones de IA generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificación de Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificación de Phi-3.5 / 4 usando el marco Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.