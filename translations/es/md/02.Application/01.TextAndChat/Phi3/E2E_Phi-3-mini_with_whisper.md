# Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

## Descripción General

El Chatbot Interactivo Phi 3 Mini 4K Instruct es una herramienta que permite a los usuarios interactuar con la demostración Phi 3 Mini 4K Instruct de Microsoft utilizando entrada de texto o audio. El chatbot puede ser utilizado para una variedad de tareas, como traducción, actualizaciones del clima y recopilación de información general.

### Primeros Pasos

Para usar este chatbot, simplemente sigue estas instrucciones:

1. Abre un nuevo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. En la ventana principal del notebook, verás una interfaz de chat con un cuadro de entrada de texto y un botón "Send".
3. Para usar el chatbot basado en texto, simplemente escribe tu mensaje en el cuadro de entrada de texto y haz clic en el botón "Send". El chatbot responderá con un archivo de audio que puede reproducirse directamente desde el notebook.

**Nota**: Esta herramienta requiere una GPU y acceso a los modelos Microsoft Phi-3 y OpenAI Whisper, utilizados para reconocimiento de voz y traducción.

### Requisitos de GPU

Para ejecutar esta demostración necesitas 12 GB de memoria GPU.

Los requisitos de memoria para ejecutar la demostración **Microsoft-Phi-3-Mini-4K Instruct** en una GPU dependerán de varios factores, como el tamaño de los datos de entrada (audio o texto), el idioma usado para la traducción, la velocidad del modelo y la memoria disponible en la GPU.

En general, el modelo Whisper está diseñado para ejecutarse en GPUs. La cantidad mínima recomendada de memoria GPU para ejecutar el modelo Whisper es de 8 GB, aunque puede manejar mayores cantidades de memoria si es necesario.

Es importante tener en cuenta que ejecutar una gran cantidad de datos o un alto volumen de solicitudes en el modelo puede requerir más memoria GPU y/o causar problemas de rendimiento. Se recomienda probar tu caso de uso con diferentes configuraciones y monitorear el uso de memoria para determinar la configuración óptima para tus necesidades específicas.

## Ejemplo E2E para el Chatbot Interactivo Phi 3 Mini 4K Instruct con Whisper

El notebook Jupyter titulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demuestra cómo usar la demostración Microsoft Phi 3 Mini 4K Instruct para generar texto a partir de entrada de audio o texto escrito. El notebook define varias funciones:

1. `tts_file_name(text)`: Esta función genera un nombre de archivo basado en el texto de entrada para guardar el archivo de audio generado.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta función utiliza la API de Edge TTS para generar un archivo de audio a partir de una lista de fragmentos de texto de entrada. Los parámetros de entrada son la lista de fragmentos, la velocidad del habla, el nombre de la voz y la ruta de salida para guardar el archivo de audio generado.
3. `talk(input_text)`: Esta función genera un archivo de audio utilizando la API de Edge TTS y lo guarda con un nombre de archivo aleatorio en el directorio /content/audio. El parámetro de entrada es el texto de entrada a convertir en habla.
4. `run_text_prompt(message, chat_history)`: Esta función utiliza la demostración Microsoft Phi 3 Mini 4K Instruct para generar un archivo de audio a partir de un mensaje de entrada y lo agrega al historial de chat.
5. `run_audio_prompt(audio, chat_history)`: Esta función convierte un archivo de audio en texto utilizando la API del modelo Whisper y lo pasa a la función `run_text_prompt()`.
6. El código lanza una aplicación Gradio que permite a los usuarios interactuar con la demostración Phi 3 Mini 4K Instruct ya sea escribiendo mensajes o cargando archivos de audio. La salida se muestra como un mensaje de texto dentro de la aplicación.

## Solución de Problemas

Instalación de controladores GPU Cuda

1. Asegúrate de que tus aplicaciones de Linux estén actualizadas

    ```bash
    sudo apt update
    ```

2. Instala los controladores Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Registra la ubicación del controlador Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Comprobación del tamaño de la memoria GPU Nvidia (Se requieren 12 GB de memoria GPU)

    ```bash
    nvidia-smi
    ```

5. Vaciar la Caché: Si estás usando PyTorch, puedes llamar a torch.cuda.empty_cache() para liberar toda la memoria en caché no utilizada, de modo que pueda ser utilizada por otras aplicaciones de GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Comprobación de Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. Realiza las siguientes tareas para crear un token de Hugging Face.

    - Navega a la [página de configuración de tokens de Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecciona **New token**.
    - Ingresa el **Nombre** del proyecto que deseas usar.
    - Selecciona el **Tipo** como **Write**.

> **Nota**
>
> Si encuentras el siguiente error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolverlo, escribe el siguiente comando dentro de tu terminal.
>
> ```bash
> sudo ldconfig
> ```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.