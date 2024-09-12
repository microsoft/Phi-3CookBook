# Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

## Resumen

El Chatbot Interactivo Phi 3 Mini 4K Instruct es una herramienta que permite a los usuarios interactuar con la demo de Microsoft Phi 3 Mini 4K instruct utilizando entrada de texto o audio. El chatbot se puede usar para una variedad de tareas, como traducción, actualizaciones del clima y recopilación de información general.

### Primeros Pasos

Para usar este chatbot, simplemente sigue estas instrucciones:

1. Abre un nuevo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. En la ventana principal del notebook, verás una interfaz de chat con un cuadro de entrada de texto y un botón de "Enviar".
3. Para usar el chatbot basado en texto, simplemente escribe tu mensaje en el cuadro de entrada de texto y haz clic en el botón "Enviar". El chatbot responderá con un archivo de audio que se puede reproducir directamente desde el notebook.

**Nota**: Esta herramienta requiere una GPU y acceso a los modelos Microsoft Phi-3 y OpenAI Whisper, que se utilizan para el reconocimiento y traducción de voz.

### Requisitos de GPU

Para ejecutar esta demo necesitas 12Gb de memoria GPU.

Los requisitos de memoria para ejecutar la demo **Microsoft-Phi-3-Mini-4K instruct** en una GPU dependerán de varios factores, como el tamaño de los datos de entrada (audio o texto), el idioma utilizado para la traducción, la velocidad del modelo y la memoria disponible en la GPU.

En general, el modelo Whisper está diseñado para ejecutarse en GPUs. La cantidad mínima recomendada de memoria GPU para ejecutar el modelo Whisper es de 8 GB, pero puede manejar cantidades mayores de memoria si es necesario.

Es importante notar que ejecutar una gran cantidad de datos o un alto volumen de solicitudes en el modelo puede requerir más memoria GPU y/o puede causar problemas de rendimiento. Se recomienda probar tu caso de uso con diferentes configuraciones y monitorear el uso de la memoria para determinar la configuración óptima para tus necesidades específicas.

## Ejemplo E2E para el Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

El notebook jupyter titulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demuestra cómo usar la Demo de Microsoft Phi 3 Mini 4K instruct para generar texto a partir de entrada de audio o texto escrito. El notebook define varias funciones:

1. `tts_file_name(text)`: Esta función genera un nombre de archivo basado en el texto de entrada para guardar el archivo de audio generado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta función utiliza la API de Edge TTS para generar un archivo de audio a partir de una lista de fragmentos de texto de entrada. Los parámetros de entrada son la lista de fragmentos, la velocidad del habla, el nombre de la voz y la ruta de salida para guardar el archivo de audio generado.
1. `talk(input_text)`: Esta función genera un archivo de audio usando la API de Edge TTS y lo guarda con un nombre de archivo aleatorio en el directorio /content/audio. El parámetro de entrada es el texto de entrada que se convertirá a voz.
1. `run_text_prompt(message, chat_history)`: Esta función utiliza la demo de Microsoft Phi 3 Mini 4K instruct para generar un archivo de audio a partir de un mensaje de entrada y lo añade al historial de chat.
1. `run_audio_prompt(audio, chat_history)`: Esta función convierte un archivo de audio en texto usando la API del modelo Whisper y lo pasa a la función `run_text_prompt()`.
1. El código lanza una app de Gradio que permite a los usuarios interactuar con la demo Phi 3 Mini 4K instruct escribiendo mensajes o subiendo archivos de audio. La salida se muestra como un mensaje de texto dentro de la app.

## Solución de Problemas

Instalando controladores GPU de Cuda

1. Asegúrate de que tu aplicación de Linux esté actualizada

    ```bash
    sudo apt update
    ```

1. Instala los controladores de Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registra la ubicación del controlador de cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Comprobando el tamaño de la memoria de la GPU Nvidia (Requiere 12GB de Memoria GPU)

    ```bash
    nvidia-smi
    ```

1. Vaciar la Caché: Si estás usando PyTorch, puedes llamar a torch.cuda.empty_cache() para liberar toda la memoria en caché no utilizada para que pueda ser utilizada por otras aplicaciones de GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Comprobando Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Realiza las siguientes tareas para crear un token de Hugging Face.

    - Navega a la [página de configuración de tokens de Hugging Face](https://huggingface.co/settings/tokens).
    - Selecciona **Nuevo token**.
    - Introduce el **Nombre** del proyecto que deseas utilizar.
    - Selecciona **Tipo** a **Escribir**.

> **Note**
>
> Si encuentras el siguiente error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolver esto, escribe el siguiente comando en tu terminal.
>
> ```bash
> sudo ldconfig
> ```

