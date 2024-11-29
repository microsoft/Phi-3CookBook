Phi-3-mini WebGPU RAG Chatbot

## Demo para mostrar WebGPU y el patrón RAG
El patrón RAG con el modelo Phi-3 Onnx Hosted aprovecha el enfoque de Generación Aumentada por Recuperación, combinando el poder de los modelos Phi-3 con el alojamiento ONNX para implementaciones eficientes de IA. Este patrón es fundamental para ajustar modelos para tareas específicas de dominio, ofreciendo una mezcla de calidad, rentabilidad y comprensión de contextos largos. Es parte del conjunto de Azure AI, que proporciona una amplia selección de modelos fáciles de encontrar, probar y usar, satisfaciendo las necesidades de personalización de diversas industrias. Los modelos Phi-3, incluidos Phi-3-mini, Phi-3-small y Phi-3-medium, están disponibles en el Catálogo de Modelos de Azure AI y se pueden ajustar y desplegar de manera autogestionada o a través de plataformas como HuggingFace y ONNX, mostrando el compromiso de Microsoft con soluciones de IA accesibles y eficientes.

## ¿Qué es WebGPU?
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está destinada a ser la sucesora de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs Modernas**: WebGPU está construida para funcionar sin problemas con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento Mejorado**: Soporta cálculos de propósito general en la GPU y operaciones más rápidas, haciéndola adecuada tanto para renderizado de gráficos como para tareas de aprendizaje automático.
3. **Características Avanzadas**: WebGPU proporciona acceso a capacidades de GPU más avanzadas, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Reducción de la Carga de Trabajo de JavaScript**: Al descargar más tareas a la GPU, WebGPU reduce significativamente la carga de trabajo en JavaScript, llevando a un mejor rendimiento y experiencias más fluidas.

WebGPU es actualmente compatible con navegadores como Google Chrome, con trabajo en curso para expandir el soporte a otras plataformas.

### 03.WebGPU
Entorno requerido:

**Navegadores compatibles:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Habilitar WebGPU:

- En Chrome/Microsoft Edge 

Habilita la bandera `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu navegador:
Inicia Google Chrome o Microsoft Edge.

#### Accede a la página de banderas:
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca la bandera:
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'

#### Habilita la bandera:
Encuentra la bandera #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a ella y selecciona Enabled.

#### Reinicia tu navegador:

Después de habilitar la bandera, necesitarás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- Para Linux, inicia el navegador con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tiene WebGPU habilitado por defecto.
- En Firefox Nightly, ingresa about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configurando GPU para Microsoft Edge 

Aquí están los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abre Configuración:** Haz clic en el menú de Inicio y selecciona Configuración.
- **Configuración del Sistema:** Ve a Sistema y luego a Pantalla.
- **Configuración de Gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.
- **Elegir Aplicación:** En "Elegir una aplicación para establecer preferencia," selecciona Aplicación de escritorio y luego Examinar.
- **Selecciona Edge:** Navega a la carpeta de instalación de Edge (usualmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.
- **Establecer Preferencia:** Haz clic en Opciones, elige Alto rendimiento, y luego haz clic en Guardar.
Esto asegurará que Microsoft Edge use tu GPU de alto rendimiento para un mejor rendimiento.
- **Reinicia** tu máquina para que estos ajustes surtan efecto.

### Abre tu Codespace:
Navega a tu repositorio en GitHub.
Haz clic en el botón Code y selecciona Open with Codespaces.

Si aún no tienes un Codespace, puedes crear uno haciendo clic en New codespace.

**Nota** Instalando el entorno Node en tu Codespace
Ejecutar una demostración de npm desde un GitHub Codespace es una excelente manera de probar y desarrollar tu proyecto. Aquí tienes una guía paso a paso para ayudarte a comenzar:

### Configura tu entorno:
Una vez que tu Codespace esté abierto, asegúrate de tener Node.js y npm instalados. Puedes comprobarlo ejecutando:
```
node -v
```
```
npm -v
```

Si no están instalados, puedes instalarlos usando:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navega a tu directorio de proyecto:
Usa la terminal para navegar al directorio donde se encuentra tu proyecto npm:
```
cd path/to/your/project
```

### Instala dependencias:
Ejecuta el siguiente comando para instalar todas las dependencias necesarias listadas en tu archivo package.json:

```
npm install
```

### Ejecuta la demo:
Una vez que las dependencias estén instaladas, puedes ejecutar tu script de demostración. Esto generalmente se especifica en la sección de scripts de tu package.json. Por ejemplo, si tu script de demostración se llama start, puedes ejecutar:

```
npm run build
```
```
npm run dev
```

### Accede a la demo:
Si tu demo implica un servidor web, Codespaces proporcionará una URL para acceder a ella. Busca una notificación o revisa la pestaña Ports para encontrar la URL.

**Nota:** El modelo necesita ser almacenado en caché en el navegador, por lo que puede tardar un tiempo en cargarse.

### Demo RAG
Sube el archivo markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecciona tu archivo:
Haz clic en el botón que dice “Choose File” para elegir el documento que deseas subir.

### Sube el documento:
Después de seleccionar tu archivo, haz clic en el botón “Upload” para cargar tu documento para RAG (Generación Aumentada por Recuperación).

### Comienza tu chat:
Una vez que el documento esté subido, puedes comenzar una sesión de chat usando RAG basada en el contenido de tu documento.

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automatizada por IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.