# Contribuyendo

Este proyecto da la bienvenida a contribuciones y sugerencias. La mayoría de las contribuciones requieren que aceptes un
Acuerdo de Licencia de Contribuyente (CLA) que declara que tienes el derecho de, y realmente, nos otorgas
los derechos para usar tu contribución. Para más detalles, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Cuando envíes una solicitud de extracción, un bot de CLA determinará automáticamente si necesitas proporcionar
un CLA y decorará el PR adecuadamente (por ejemplo, verificación de estado, comentario). Simplemente sigue las instrucciones
proporcionadas por el bot. Solo necesitarás hacer esto una vez en todos los repositorios que usan nuestro CLA.

## Código de Conducta

Este proyecto ha adoptado el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/).
Para más información, lee las [Preguntas Frecuentes sobre el Código de Conducta](https://opensource.microsoft.com/codeofconduct/faq/) o contacta a [opencode@microsoft.com](mailto:opencode@microsoft.com) con cualquier pregunta o comentario adicional.

## Precauciones para crear issues

Por favor, no abras issues en GitHub para preguntas generales de soporte, ya que la lista de GitHub debe usarse para solicitudes de características e informes de errores. De esta manera, podemos rastrear más fácilmente problemas o errores reales del código y mantener la discusión general separada del código real.

## Cómo Contribuir

### Pautas para Solicitudes de Extracción

Al enviar una solicitud de extracción (PR) al repositorio de Phi-3 CookBook, por favor usa las siguientes pautas:

- **Haz un Fork del Repositorio**: Siempre haz un fork del repositorio a tu propia cuenta antes de hacer tus modificaciones.

- **Solicitudes de extracción separadas (PR)**:
  - Envía cada tipo de cambio en su propia solicitud de extracción. Por ejemplo, las correcciones de errores y las actualizaciones de documentación deben enviarse en PRs separados.
  - Las correcciones de errores tipográficos y las actualizaciones menores de documentación pueden combinarse en un solo PR donde sea apropiado.

- **Maneja los conflictos de fusión**: Si tu solicitud de extracción muestra conflictos de fusión, actualiza tu rama `main` local para reflejar el repositorio principal antes de hacer tus modificaciones.

- **Envíos de traducción**: Al enviar un PR de traducción, asegúrate de que la carpeta de traducción incluya traducciones de todos los archivos en la carpeta original.

### Pautas de Traducción

> [!IMPORTANT]
>
> Al traducir texto en este repositorio, no uses traducción automática. Solo ofrece traducciones en idiomas en los que seas competente.

Si eres competente en un idioma que no sea inglés, puedes ayudar a traducir el contenido. Sigue estos pasos para asegurar que tus contribuciones de traducción se integren correctamente, por favor usa las siguientes pautas:

- **Crea una carpeta de traducción**: Navega a la carpeta de la sección correspondiente y crea una carpeta de traducción para el idioma al que estás contribuyendo. Por ejemplo:
  - Para la sección de introducción: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Para la sección de inicio rápido: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Continúa este patrón para otras secciones (03.Inference, 04.Finetuning, etc.)

- **Actualiza las rutas relativas**: Al traducir, ajusta la estructura de carpetas agregando `../../` al comienzo de las rutas relativas dentro de los archivos markdown para asegurar que los enlaces funcionen correctamente. Por ejemplo, cambia lo siguiente:
  - Cambia `(../../imgs/01/phi3aisafety.png)` a `(../../../../imgs/01/phi3aisafety.png)`

- **Organiza tus traducciones**: Cada archivo traducido debe colocarse en la carpeta de traducción correspondiente a la sección. Por ejemplo, si estás traduciendo la sección de introducción al español, crearías lo siguiente:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Envía un PR completo**: Asegúrate de que todos los archivos traducidos para una sección estén incluidos en un solo PR. No aceptamos traducciones parciales para una sección. Al enviar un PR de traducción, asegúrate de que la carpeta de traducción incluya traducciones de todos los archivos en la carpeta original.

### Pautas de Redacción

Para asegurar la consistencia en todos los documentos, por favor usa las siguientes pautas:

- **Formato de URL**: Envuelve todas las URLs entre corchetes seguidos de paréntesis, sin espacios extra alrededor o dentro de ellos. Por ejemplo: `[example](https://example.com)`.

- **Enlaces relativos**: Usa `./` para enlaces relativos que apunten a archivos o carpetas en el directorio actual, y `../` para aquellos en un directorio padre. Por ejemplo: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Locales no específicos de país**: Asegúrate de que tus enlaces no incluyan locales específicos de país. Por ejemplo, evita `/en-us/` o `/en/`.

- **Almacenamiento de imágenes**: Almacena todas las imágenes en la carpeta `./imgs`.

- **Nombres descriptivos de imágenes**: Nombra las imágenes de manera descriptiva usando caracteres en inglés, números y guiones. Por ejemplo: `example-image.jpg`.

## Flujos de Trabajo de GitHub

Cuando envíes una solicitud de extracción, se activarán los siguientes flujos de trabajo para validar los cambios. Sigue las instrucciones a continuación para asegurar que tu solicitud de extracción pase las verificaciones del flujo de trabajo:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este flujo de trabajo asegura que todas las rutas relativas en tus archivos sean correctas.

1. Para asegurarte de que tus enlaces funcionen correctamente, realiza las siguientes tareas usando VS Code:
    - Pasa el cursor sobre cualquier enlace en tus archivos.
    - Presiona **Ctrl + Click** para navegar al enlace.
    - Si haces clic en un enlace y no funciona localmente, activará el flujo de trabajo y no funcionará en GitHub.

1. Para solucionar este problema, realiza las siguientes tareas usando las sugerencias de ruta proporcionadas por VS Code:
    - Escribe `./` o `../`.
    - VS Code te pedirá que elijas entre las opciones disponibles basadas en lo que escribiste.
    - Sigue la ruta haciendo clic en el archivo o carpeta deseado para asegurar que tu ruta sea correcta.

Una vez que hayas agregado la ruta relativa correcta, guarda y envía tus cambios.

### Check URLs Don't Have Locale

Este flujo de trabajo asegura que cualquier URL web no incluya un local específico de país. Como este repositorio es accesible globalmente, es importante asegurar que las URLs no contengan el local de tu país.

1. Para verificar que tus URLs no tienen locales de país, realiza las siguientes tareas:

    - Revisa el texto como `/en-us/`, `/en/`, o cualquier otro local de idioma en las URLs.
    - Si estos no están presentes en tus URLs, entonces pasarás esta verificación.

1. Para solucionar este problema, realiza las siguientes tareas:
    - Abre la ruta del archivo destacada por el flujo de trabajo.
    - Elimina el local de país de las URLs.

Una vez que elimines el local de país, guarda y envía tus cambios.

### Check Broken Urls

Este flujo de trabajo asegura que cualquier URL web en tus archivos esté funcionando y devolviendo un código de estado 200.

1. Para verificar que tus URLs estén funcionando correctamente, realiza las siguientes tareas:
    - Revisa el estado de las URLs en tus archivos.

2. Para solucionar cualquier URL rota, realiza las siguientes tareas:
    - Abre el archivo que contiene la URL rota.
    - Actualiza la URL a la correcta.

Una vez que hayas corregido las URLs, guarda y envía tus cambios.

> [!NOTE]
>
> Puede haber casos en los que la verificación de URL falle aunque el enlace sea accesible. Esto puede suceder por varias razones, incluyendo:
>
> - **Restricciones de red:** Los servidores de GitHub actions pueden tener restricciones de red que impidan el acceso a ciertas URLs.
> - **Problemas de tiempo de espera:** Las URLs que tardan demasiado en responder pueden provocar un error de tiempo de espera en el flujo de trabajo.
> - **Problemas temporales del servidor:** Ocasionales tiempos de inactividad o mantenimiento del servidor pueden hacer que una URL no esté disponible temporalmente durante la validación.

Aviso legal: La traducción fue realizada por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.