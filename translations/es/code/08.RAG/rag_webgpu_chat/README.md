Phi-3-mini WebGPU RAG Chatbot

## Demo para mostrar WebGPU y el Patrón RAG
El Patrón RAG con el modelo Phi-3 Onnx Hosted aprovecha el enfoque de Generación Aumentada por Recuperación, combinando la potencia de los modelos Phi-3 con el alojamiento ONNX para despliegues de IA eficientes. Este patrón es instrumental en la afinación de modelos para tareas específicas de dominio, ofreciendo una mezcla de calidad, rentabilidad y comprensión de contextos largos. Es parte de la suite de Azure AI, proporcionando una amplia selección de modelos que son fáciles de encontrar, probar y usar, atendiendo a las necesidades de personalización de diversas industrias. Los modelos Phi-3, incluyendo Phi-3-mini, Phi-3-small y Phi-3-medium, están disponibles en el Catálogo de Modelos de Azure AI y pueden ser afinados y desplegados de manera autogestionada o a través de plataformas como HuggingFace y ONNX, demostrando el compromiso de Microsoft con soluciones de IA accesibles y eficientes.

## ¿Qué es WebGPU?
WebGPU es una API moderna de gráficos web diseñada para proporcionar acceso eficiente a la unidad de procesamiento gráfico (GPU) de un dispositivo directamente desde navegadores web. Está destinada a ser la sucesora de WebGL, ofreciendo varias mejoras clave:

1. **Compatibilidad con GPUs Modernas**: WebGPU está diseñada para trabajar sin problemas con arquitecturas de GPU contemporáneas, aprovechando APIs del sistema como Vulkan, Metal y Direct3D 12.
2. **Rendimiento Mejorado**: Soporta cálculos de propósito general en GPU y operaciones más rápidas, haciéndolo adecuado tanto para renderizado gráfico como para tareas de aprendizaje automático.
3. **Características Avanzadas**: WebGPU proporciona acceso a capacidades de GPU más avanzadas, permitiendo cargas de trabajo gráficas y computacionales más complejas y dinámicas.
4. **Carga de Trabajo Reducida en JavaScript**: Al descargar más tareas a la GPU, WebGPU reduce significativamente la carga de trabajo en JavaScript, llevando a un mejor rendimiento y experiencias más fluidas.

WebGPU es actualmente compatible con navegadores como Google Chrome, con trabajo en curso para expandir el soporte a otras plataformas.

### 03.WebGPU
Entorno Requerido:

**Navegadores compatibles:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Habilitar WebGPU:

- En Chrome/Microsoft Edge 

Habilita la bandera `chrome://flags/#enable-unsafe-webgpu`.

#### Abre Tu Navegador:
Lanza Google Chrome o Microsoft Edge.

#### Accede a la Página de Flags:
En la barra de direcciones, escribe `chrome://flags` y presiona Enter.

#### Busca la Bandera:
En el cuadro de búsqueda en la parte superior de la página, escribe 'enable-unsafe-webgpu'

#### Habilita la Bandera:
Encuentra la bandera #enable-unsafe-webgpu en la lista de resultados.

Haz clic en el menú desplegable junto a ella y selecciona Enabled.

#### Reinicia Tu Navegador:

Después de habilitar la bandera, necesitarás reiniciar tu navegador para que los cambios surtan efecto. Haz clic en el botón Relaunch que aparece en la parte inferior de la página.

- Para Linux, lanza el navegador con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tiene WebGPU habilitado por defecto.
- En Firefox Nightly, ingresa about:config en la barra de direcciones y `set dom.webgpu.enabled to true`.

### Configuración de GPU para Microsoft Edge 

Aquí están los pasos para configurar una GPU de alto rendimiento para Microsoft Edge en Windows:

- **Abre Configuración:** Haz clic en el menú Inicio y selecciona Configuración.
- **Configuración del Sistema:** Ve a Sistema y luego Pantalla.
- **Configuración de Gráficos:** Desplázate hacia abajo y haz clic en Configuración de gráficos.
- **Elige Aplicación:** Bajo “Elige una aplicación para establecer preferencia,” selecciona Aplicación de escritorio y luego Examinar.
- **Selecciona Edge:** Navega a la carpeta de instalación de Edge (usualmente `C:\Program Files (x86)\Microsoft\Edge\Application`) y selecciona `msedge.exe`.
- **Establece Preferencia:** Haz clic en Opciones, elige Alto rendimiento, y luego haz clic en Guardar.
Esto asegurará que Microsoft Edge use tu GPU de alto rendimiento para un mejor rendimiento.
- **Reinicia** tu máquina para que estos ajustes surtan efecto.

### Abre Tu Codespace:
Navega a tu repositorio en GitHub.
Haz clic en el botón Code y selecciona Open with Codespaces.

Si aún no tienes un Codespace, puedes crear uno haciendo clic en New codespace.

**Nota** Instalando el Entorno de Node en tu codespace
Ejecutar una demo de npm desde un GitHub Codespace es una excelente manera de probar y desarrollar tu proyecto. Aquí hay una guía paso a paso para ayudarte a comenzar:

### Configura Tu Entorno:
Una vez que tu Codespace esté abierto, asegúrate de tener Node.js y npm instalados. Puedes verificar esto ejecutando:
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

### Navega a Tu Directorio de Proyecto:
Usa la terminal para navegar al directorio donde se encuentra tu proyecto npm:
```
cd path/to/your/project
```

### Instala Dependencias:
Ejecuta el siguiente comando para instalar todas las dependencias necesarias listadas en tu archivo package.json:

```
npm install
```

### Ejecuta la Demo:
Una vez que las dependencias estén instaladas, puedes ejecutar tu script de demo. Esto usualmente se especifica en la sección scripts de tu package.json. Por ejemplo, si tu script de demo se llama start, puedes ejecutar:

```
npm run build
```
```
npm run dev
```

### Accede a la Demo:
Si tu demo involucra un servidor web, Codespaces proporcionará una URL para acceder a él. Busca una notificación o revisa la pestaña de Puertos para encontrar la URL.

**Nota:** El modelo necesita ser almacenado en caché en el navegador, por lo que puede tardar un tiempo en cargar.

### Demo de RAG
Sube el archivo markdown `intro_rag.md` para completar la solución RAG. Si usas codespaces puedes descargar el archivo ubicado en `01.InferencePhi3/docs/`

### Selecciona Tu Archivo:
Haz clic en el botón que dice “Choose File” para elegir el documento que quieres subir.

### Sube el Documento:
Después de seleccionar tu archivo, haz clic en el botón “Upload” para cargar tu documento para RAG (Generación Aumentada por Recuperación).

### Inicia Tu Chat:
Una vez que el documento esté subido, puedes iniciar una sesión de chat usando RAG basado en el contenido de tu documento.

Aviso legal: La traducción fue realizada por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.