Phi-3-mini WebGPU RAG Chatbot

## Demostración para mostrar WebGPU y el patrón RAG
El patrón RAG con el modelo Phi-3 Onnx Hosted aprovecha el enfoque de Generación Aumentada por Recuperación (Retrieval-Augmented Generation), combinando el poder de los modelos Phi-3 con el alojamiento en ONNX para implementaciones de IA eficientes. Este patrón es fundamental para ajustar modelos a tareas específicas de dominio, ofreciendo una mezcla de calidad, rentabilidad y comprensión de contextos largos. Forma parte de la suite de Azure AI, proporcionando una amplia selección de modelos fáciles de encontrar, probar y usar, adaptándose a las necesidades de personalización de diversas industrias. Los modelos Phi-3, incluidos Phi-3-mini, Phi-3-small y Phi-3-medium, están disponibles en el Catálogo de Modelos de Azure AI y pueden ajustarse y desplegarse de manera autónoma o a través de plataformas como HuggingFace y ONNX, demostrando el compromiso de Microsoft con soluciones de IA accesibles y eficientes.

## ¿Qué es WebGPU?
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde los navegadores web. Está pensada como la sucesora de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs modernas**: WebGPU está diseñada para funcionar perfectamente con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento mejorado**: Soporta cálculos generales en la GPU y operaciones más rápidas, haciéndola adecuada tanto para renderizado gráfico como para tareas de aprendizaje automático.
3. **Funciones avanzadas**: WebGPU proporciona acceso a capacidades más avanzadas de la GPU, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Menor carga de trabajo en JavaScript**: Al delegar más tareas a la GPU, WebGPU reduce significativamente la carga de trabajo en JavaScript, lo que se traduce en un mejor rendimiento y experiencias más fluidas.

Actualmente, WebGPU es compatible con navegadores como Google Chrome, y se está trabajando para ampliar su soporte a otras plataformas.

### 03.WebGPU
Entorno necesario:

**Navegadores compatibles:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Habilitar WebGPU:

- En Chrome/Microsoft Edge 

Habilita el flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abre tu navegador:
Inicia Google Chrome o Microsoft Edge.

#### Accede a la página de Flags:
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca el Flag:
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'.

#### Habilita el Flag:
Encuentra el flag #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a él y selecciona Enabled.

#### Reinicia tu navegador:
Después de habilitar el flag, deberás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- Para Linux, inicia el navegador con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tiene WebGPU habilitado por defecto.
- En Firefox Nightly, ingresa about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configuración de GPU para Microsoft Edge

Aquí están los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abrir Configuración:** Haz clic en el menú Inicio y selecciona Configuración.
- **Configuración del Sistema:** Ve a Sistema y luego a Pantalla.
- **Configuración de Gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.
- **Seleccionar Aplicación:** En “Elegir una aplicación para establecer preferencia,” selecciona Aplicación de escritorio y luego Examinar.
- **Seleccionar Edge:** Navega a la carpeta de instalación de Edge (generalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.
- **Establecer Preferencia:** Haz clic en Opciones, elige Alto rendimiento y luego haz clic en Guardar.
Esto asegurará que Microsoft Edge utilice tu GPU de alto rendimiento para un mejor rendimiento.
- **Reinicia** tu máquina para que estos ajustes surtan efecto.

### Abre tu Codespace:
Navega a tu repositorio en GitHub.
Haz clic en el botón Code y selecciona Open with Codespaces.

Si aún no tienes un Codespace, puedes crear uno haciendo clic en New codespace.

**Nota** Instalando el entorno Node en tu Codespace
Ejecutar un demo de npm desde un Codespace de GitHub es una excelente manera de probar y desarrollar tu proyecto. Aquí tienes una guía paso a paso para comenzar:

### Configura tu entorno:
Una vez que tu Codespace esté abierto, asegúrate de tener Node.js y npm instalados. Puedes verificarlo ejecutando:
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

### Instala las dependencias:
Ejecuta el siguiente comando para instalar todas las dependencias necesarias listadas en tu archivo package.json:

```
npm install
```

### Ejecuta el demo:
Una vez instaladas las dependencias, puedes ejecutar tu script de demostración. Esto generalmente está especificado en la sección de scripts de tu archivo package.json. Por ejemplo, si tu script de demostración se llama start, puedes ejecutar:

```
npm run build
```
```
npm run dev
```

### Accede al demo:
Si tu demostración implica un servidor web, Codespaces proporcionará una URL para acceder a él. Busca una notificación o revisa la pestaña Ports para encontrar la URL.

**Nota:** El modelo necesita ser almacenado en caché en el navegador, por lo que puede tardar un poco en cargarse.

### Demostración RAG
Sube el archivo markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecciona tu archivo:
Haz clic en el botón que dice “Elegir archivo” para seleccionar el documento que deseas subir.

### Sube el documento:
Después de seleccionar tu archivo, haz clic en el botón “Subir” para cargar tu documento para RAG (Generación Aumentada por Recuperación).

### Inicia tu chat:
Una vez que el documento esté subido, puedes iniciar una sesión de chat usando RAG basado en el contenido de tu documento.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.