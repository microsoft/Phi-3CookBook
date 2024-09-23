### Escenario de Ejemplo

Imagina que tienes una imagen (`demo.png`) y quieres generar código en Python que procese esta imagen y guarde una nueva versión de ella (`phi-3-vision.jpg`). 

El código anterior automatiza este proceso mediante:

1. La configuración del entorno y las configuraciones necesarias.
2. La creación de un prompt que instruye al modelo para generar el código Python requerido.
3. El envío del prompt al modelo y la recolección del código generado.
4. La extracción y ejecución del código generado.
5. La visualización de las imágenes original y procesada.

Este enfoque aprovecha el poder de la IA para automatizar tareas de procesamiento de imágenes, haciendo que sea más fácil y rápido alcanzar tus objetivos.

[Solución de Código de Ejemplo](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Desglosemos lo que hace todo el código paso a paso:

1. **Instalar el Paquete Requerido**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Este comando instala el paquete `langchain_nvidia_ai_endpoints`, asegurándose de que sea la última versión.

2. **Importar Módulos Necesarios**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Estas importaciones traen los módulos necesarios para interactuar con los endpoints de NVIDIA AI, manejar contraseñas de manera segura, interactuar con el sistema operativo y codificar/decodificar datos en formato base64.

3. **Configurar la Clave API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Introduce tu clave API de NVIDIA: ")
    ```
    Este código verifica si la variable de entorno `NVIDIA_API_KEY` está configurada. Si no, solicita al usuario que introduzca su clave API de manera segura.

4. **Definir Modelo y Ruta de la Imagen**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Esto establece el modelo a utilizar, crea una instancia de `ChatNVIDIA` con el modelo especificado y define la ruta al archivo de imagen.

5. **Crear el Prompt de Texto**:
    ```python
    text = "Por favor, crea código Python para la imagen, y usa plt para guardar la nueva imagen en imgs/ y nombrarla phi-3-vision.jpg."
    ```
    Esto define un prompt de texto que instruye al modelo a generar código Python para procesar una imagen.

6. **Codificar la Imagen en Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'
    ```
    Este código lee el archivo de imagen, lo codifica en base64 y crea una etiqueta HTML de imagen con los datos codificados.

7. **Combinar Texto e Imagen en el Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Esto combina el prompt de texto y la etiqueta HTML de imagen en una sola cadena.

8. **Generar Código Usando ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Este código envía el prompt al modelo `ChatNVIDIA` y recopila el código generado en fragmentos, imprimiendo y añadiendo cada fragmento a la cadena `code`.

9. **Extraer Código Python del Contenido Generado**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Esto extrae el código Python real del contenido generado eliminando el formato markdown.

10. **Ejecutar el Código Generado**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Esto ejecuta el código Python extraído como un subproceso y captura su salida.

11. **Mostrar Imágenes**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Estas líneas muestran las imágenes usando el módulo `IPython.display`.

        Descargo de responsabilidad: La traducción fue realizada por un modelo de IA y puede no ser perfecta.
        Por favor, revise el resultado y haga las correcciones necesarias.