# Bienvenido a tu Extensión de VS Code

## Qué hay en la carpeta

* Esta carpeta contiene todos los archivos necesarios para tu extensión.
* `package.json` - este es el archivo de manifiesto en el cual declaras tu extensión y comando.
  * El plugin de ejemplo registra un comando y define su título y nombre de comando. Con esta información, VS Code puede mostrar el comando en la paleta de comandos. Aún no necesita cargar el plugin.
* `src/extension.ts` - este es el archivo principal donde proporcionarás la implementación de tu comando.
  * El archivo exporta una función, `activate`, que se llama la primera vez que se activa tu extensión (en este caso al ejecutar el comando). Dentro de la función `activate` llamamos a `registerCommand`.
  * Pasamos la función que contiene la implementación del comando como segundo parámetro a `registerCommand`.

## Configuración

* instala las extensiones recomendadas (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner y dbaeumer.vscode-eslint)

## Poner en marcha de inmediato

* Presiona `F5` para abrir una nueva ventana con tu extensión cargada.
* Ejecuta tu comando desde la paleta de comandos presionando (`Ctrl+Shift+P` o `Cmd+Shift+P` en Mac) y escribiendo `Hello World`.
* Coloca puntos de interrupción en tu código dentro de `src/extension.ts` para depurar tu extensión.
* Encuentra la salida de tu extensión en la consola de depuración.

## Realizar cambios

* Puedes relanzar la extensión desde la barra de herramientas de depuración después de cambiar el código en `src/extension.ts`.
* También puedes recargar (`Ctrl+R` o `Cmd+R` en Mac) la ventana de VS Code con tu extensión para cargar tus cambios.

## Explorar la API

* Puedes abrir el conjunto completo de nuestra API cuando abras el archivo `node_modules/@types/vscode/index.d.ts`.

## Ejecutar pruebas

* Instala el [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Ejecuta la tarea "watch" a través del comando **Tasks: Run Task**. Asegúrate de que esto esté ejecutándose, o las pruebas podrían no ser descubiertas.
* Abre la vista de Testing desde la barra de actividades y haz clic en el botón "Run Test", o usa la tecla de acceso rápido `Ctrl/Cmd + ; A`
* Ve la salida del resultado de la prueba en la vista de Resultados de Pruebas.
* Realiza cambios en `src/test/extension.test.ts` o crea nuevos archivos de prueba dentro de la carpeta `test`.
  * El runner de pruebas proporcionado solo considerará archivos que coincidan con el patrón de nombre `**.test.ts`.
  * Puedes crear carpetas dentro de la carpeta `test` para estructurar tus pruebas como quieras.

## Ir más allá

* Reduce el tamaño de la extensión y mejora el tiempo de inicio [empaquetando tu extensión](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publica tu extensión](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) en el mercado de extensiones de VS Code.
* Automatiza las compilaciones configurando [Integración Continua](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automatizada por inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.