# Comienza con Phi-3 localmente

Esta guía te ayudará a configurar tu entorno local para ejecutar el modelo Phi-3 usando Ollama. Puedes ejecutar el modelo de varias maneras, incluyendo el uso de GitHub Codespaces, VS Code Dev Containers, o tu entorno local.

## Configuración del entorno

### GitHub Codespaces

Puedes ejecutar esta plantilla virtualmente usando GitHub Codespaces. El botón abrirá una instancia de VS Code basada en la web en tu navegador:

1. Abre la plantilla (esto puede tomar varios minutos):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. Abre una ventana de terminal

### VS Code Dev Containers

⚠️ Esta opción solo funcionará si tu Docker Desktop tiene al menos 16 GB de RAM asignados. Si tienes menos de 16 GB de RAM, puedes intentar la opción de [GitHub Codespaces](../../../../md/01.Introduce) o [configurarlo localmente](../../../../md/01.Introduce).

Una opción relacionada es VS Code Dev Containers, que abrirá el proyecto en tu VS Code local usando la [extensión Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Inicia Docker Desktop (instálalo si no está ya instalado)
2. Abre el proyecto:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. En la ventana de VS Code que se abre, una vez que los archivos del proyecto aparezcan (esto puede tomar varios minutos), abre una ventana de terminal.
4. Continúa con los [pasos de despliegue](../../../../md/01.Introduce)

### Entorno Local

1. Asegúrate de tener instaladas las siguientes herramientas:

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## Probar el modelo

1. Pídele a Ollama que descargue y ejecute el modelo phi3:mini:

    ```shell
    ollama run phi3:mini
    ```

    Eso tomará unos minutos para descargar el modelo.

2. Una vez que veas "success" en la salida, puedes enviar un mensaje a ese modelo desde el prompt.

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. Después de varios segundos, deberías ver una respuesta del modelo.

4. Para aprender sobre diferentes técnicas usadas con modelos de lenguaje, abre el cuaderno de Python [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb) y ejecuta cada celda. Si usaste un modelo diferente a 'phi3:mini', cambia el `MODEL_NAME` in the first cell.

5. To have a conversation with the phi3:mini model from Python, open the Python file [chat.py](../../../../code/01.Introduce/chat.py) and run it. You can change the `MODEL_NAME` en la parte superior del archivo según sea necesario, y también puedes modificar el mensaje del sistema o agregar ejemplos few-shot si lo deseas.

        **Descargo de responsabilidad**: 
        Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.