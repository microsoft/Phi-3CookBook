# Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

## Descripción General

El Chatbot Interactivo Phi 3 Mini 4K Instruct es una herramienta que permite a los usuarios interactuar con la demo de instrucciones de Microsoft Phi 3 Mini 4K utilizando entrada de texto o audio. El chatbot puede usarse para diversas tareas, como traducción, actualizaciones del clima y recopilación de información general.

### Primeros Pasos

Para usar este chatbot, simplemente sigue estas instrucciones:

1. Abre un nuevo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. En la ventana principal del notebook, verás una interfaz de chat con una caja de entrada de texto y un botón de "Enviar".
3. Para usar el chatbot basado en texto, simplemente escribe tu mensaje en la caja de entrada de texto y haz clic en el botón de "Enviar". El chatbot responderá con un archivo de audio que se puede reproducir directamente desde el notebook.

**Nota**: Esta herramienta requiere una GPU y acceso a los modelos Microsoft Phi-3 y OpenAI Whisper, que se utilizan para el reconocimiento y la traducción de voz.

### Requisitos de GPU

Para ejecutar esta demo necesitas 12 GB de memoria GPU.

Los requisitos de memoria para ejecutar la demo **Microsoft-Phi-3-Mini-4K instruct** en una GPU dependerán de varios factores, como el tamaño de los datos de entrada (audio o texto), el idioma utilizado para la traducción, la velocidad del modelo y la memoria disponible en la GPU.

En general, el modelo Whisper está diseñado para ejecutarse en GPUs. La cantidad mínima recomendada de memoria GPU para ejecutar el modelo Whisper es de 8 GB, pero puede manejar cantidades mayores de memoria si es necesario.

Es importante tener en cuenta que ejecutar una gran cantidad de datos o un alto volumen de solicitudes en el modelo puede requerir más memoria GPU y/o causar problemas de rendimiento. Se recomienda probar tu caso de uso con diferentes configuraciones y monitorear el uso de memoria para determinar la configuración óptima para tus necesidades específicas.

## Ejemplo E2E para el Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

El notebook jupyter titulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](../../../../md/06.E2ESamples/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demuestra cómo usar la Demo de Instrucciones de Microsoft Phi 3 Mini 4K para generar texto a partir de entrada de audio o texto escrito. El notebook define varias funciones:

1. `tts_file_name(text)`: Esta función genera un nombre de archivo basado en el texto de entrada para guardar el archivo de audio generado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta función utiliza la API de Edge TTS para generar un archivo de audio a partir de una lista de fragmentos de texto de entrada. Los parámetros de entrada son la lista de fragmentos, la velocidad del habla, el nombre de la voz y la ruta de salida para guardar el archivo de audio generado.
1. `talk(input_text)`: Esta función genera un archivo de audio utilizando la API de Edge TTS y lo guarda con un nombre de archivo aleatorio en el directorio /content/audio. El parámetro de entrada es el texto de entrada que se convertirá en voz.
1. `run_text_prompt(message, chat_history)`: Esta función utiliza la demo de instrucciones de Microsoft Phi 3 Mini 4K para generar un archivo de audio a partir de un mensaje de entrada y lo añade al historial de chat.
1. `run_audio_prompt(audio, chat_history)`: Esta función convierte un archivo de audio en texto utilizando la API del modelo Whisper y lo pasa a la función `run_text_prompt()`.
1. El código lanza una aplicación Gradio que permite a los usuarios interactuar con la demo de instrucciones Phi 3 Mini 4K escribiendo mensajes o subiendo archivos de audio. La salida se muestra como un mensaje de texto dentro de la aplicación.

## Solución de Problemas

Instalación de drivers Cuda GPU

1. Asegúrate de que tu aplicación Linux esté actualizada

    ```bash
    sudo apt update
    ```

1. Instala los drivers de Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registra la ubicación del driver de cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Comprobación del tamaño de la memoria GPU de Nvidia (Requiere 12GB de Memoria GPU)

    ```bash
    nvidia-smi
    ```

1. Vaciar Caché: Si estás usando PyTorch, puedes llamar a torch.cuda.empty_cache() para liberar toda la memoria caché no utilizada para que pueda ser usada por otras aplicaciones GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Comprobación de Cuda de Nvidia

    ```bash
    nvcc --version
    ```

1. Realiza las siguientes tareas para crear un token de Hugging Face.

    - Navega a la [página de Configuración de Tokens de Hugging Face](https://huggingface.co/settings/tokens).
    - Selecciona **Nuevo token**.
    - Ingresa el **Nombre** del proyecto que deseas usar.
    - Selecciona **Tipo** a **Escribir**.

> **Note**
>
> Si encuentras el siguiente error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolver esto, escribe el siguiente comando dentro de tu terminal.
>
> ```bash
> sudo ldconfig
> ```

Aviso legal: La traducción fue realizada por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.