# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demostración para mostrar WebGPU y el patrón RAG

El patrón RAG con el modelo Phi-3.5 Onnx Hosted utiliza el enfoque de Generación Aumentada por Recuperación, combinando la potencia de los modelos Phi-3.5 con la infraestructura de ONNX para implementaciones de IA eficientes. Este patrón es fundamental para ajustar modelos a tareas específicas de un dominio, ofreciendo una combinación de calidad, rentabilidad y comprensión de contextos largos. Forma parte de la suite de Azure AI, que proporciona una amplia selección de modelos fáciles de encontrar, probar y usar, adaptándose a las necesidades de personalización de diversas industrias.

## ¿Qué es WebGPU? 
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está pensada como la sucesora de WebGL y ofrece varias mejoras clave:

1. **Compatibilidad con GPUs modernas**: WebGPU está diseñada para funcionar sin problemas con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento mejorado**: Soporta cálculos de propósito general en la GPU y operaciones más rápidas, lo que la hace adecuada tanto para renderizado gráfico como para tareas de aprendizaje automático.
3. **Características avanzadas**: WebGPU proporciona acceso a capacidades más avanzadas de las GPUs, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Carga reducida en JavaScript**: Al delegar más tareas a la GPU, WebGPU reduce significativamente la carga en JavaScript, lo que resulta en un mejor rendimiento y experiencias más fluidas.

WebGPU es compatible actualmente con navegadores como Google Chrome, y se está trabajando para expandir el soporte a otras plataformas.

### 03.WebGPU
Entorno requerido:

**Navegadores compatibles:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Activar WebGPU:

- En Chrome/Microsoft Edge 

Habilita el flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu navegador:
Inicia Google Chrome o Microsoft Edge.

#### Accede a la página de flags:
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca el flag:
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'.

#### Habilita el flag:
Encuentra el flag #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a él y selecciona Enabled.

#### Reinicia tu navegador:

Después de habilitar el flag, necesitarás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- Para Linux, inicia el navegador con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tiene WebGPU habilitado de forma predeterminada.
- En Firefox Nightly, escribe about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configuración de la GPU para Microsoft Edge 

A continuación, los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abre Configuración:** Haz clic en el menú Inicio y selecciona Configuración.
- **Configuración del sistema:** Ve a Sistema y luego a Pantalla.
- **Configuración de gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.
- **Elige una aplicación:** En “Elegir una aplicación para establecer preferencia”, selecciona Aplicación de escritorio y luego Explorar.
- **Selecciona Edge:** Navega a la carpeta de instalación de Edge (generalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.
- **Establece la preferencia:** Haz clic en Opciones, elige Alto rendimiento y luego haz clic en Guardar.
Esto garantizará que Microsoft Edge utilice tu GPU de alto rendimiento para un mejor rendimiento.
- **Reinicia** tu equipo para que estos ajustes surtan efecto.

### Ejemplos: Por favor [haz clic en este enlace](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.