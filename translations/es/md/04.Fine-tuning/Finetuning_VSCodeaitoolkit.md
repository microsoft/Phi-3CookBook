## Bienvenido al AI Toolkit para VS Code

[AI Toolkit para VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) reúne varios modelos del Catálogo de Azure AI Studio y otros catálogos como Hugging Face. El toolkit simplifica las tareas comunes de desarrollo para construir aplicaciones de IA con herramientas y modelos de IA generativa a través de:
- Comenzar con el descubrimiento de modelos y el playground.
- Ajuste y inferencia de modelos usando recursos de computación locales.
- Ajuste y inferencia remotos usando recursos de Azure.

[Instalar AI Toolkit para VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.e66b56f619fdbb43d80893a20ec56678138f438ae58bfd34b6726ae4d96a1cc4.es.png)

**[Private Preview]** Aprovisionamiento con un clic para Azure Container Apps para ejecutar ajuste de modelos e inferencia en la nube.

Ahora vamos a empezar con el desarrollo de tu aplicación de IA:

- [Desarrollo Local](#local-development)
    - [Preparativos](#preparations)
    - [Activar Conda](#activate-conda)
    - [Solo ajuste del modelo base](#base-model-fine-tuning-only)
    - [Ajuste del modelo e inferencia](#model-fine-tuning-and-inferencing)
- [**[Private Preview]** Desarrollo Remoto](#private-preview-remote-development)
    - [Requisitos Previos](#prerequisites)
    - [Configurar un Proyecto de Desarrollo Remoto](#setting-up-a-remote-development-project)
    - [Aprovisionar Recursos de Azure](#provision-azure-resources)
    - [[Opcional] Agregar Token de Huggingface al Secreto de Azure Container App](#optional-add-huggingface-token-to-the-azure-container-app-secret)
    - [Ejecutar el Ajuste](#run-fine-tuning)
    - [Aprovisionar el Endpoint de Inferencia](#provision-inference-endpoint)
    - [Desplegar el Endpoint de Inferencia](#deploy-the-inference-endpoint)
    - [Uso avanzado](#advanced-usage)

## Desarrollo Local
### Preparativos

1. Asegúrate de que el controlador NVIDIA esté instalado en el host.
2. Ejecuta `huggingface-cli login`, si estás usando HF para la utilización del conjunto de datos.
3. Explicaciones de configuraciones clave de `Olive` para cualquier cosa que modifique el uso de memoria.

### Activar Conda
Dado que estamos usando un entorno WSL y es compartido, necesitas activar manualmente el entorno conda. Después de este paso, puedes ejecutar ajuste o inferencia.

```bash
conda activate [conda-env-name]
```

### Solo ajuste del modelo base
Para probar solo el modelo base sin ajuste, puedes ejecutar este comando después de activar conda.

```bash
cd inference

# La interfaz del navegador web permite ajustar algunos parámetros como la longitud máxima del nuevo token, la temperatura, etc.
# El usuario debe abrir manualmente el enlace (por ejemplo, http://0.0.0.0:7860) en un navegador después de que gradio inicie las conexiones.
python gradio_chat.py --baseonly
```

### Ajuste del modelo e inferencia

Una vez que el espacio de trabajo esté abierto en un contenedor de desarrollo, abre una terminal (la ruta predeterminada es la raíz del proyecto), luego ejecuta el comando a continuación para ajustar un LLM en el conjunto de datos seleccionado.

```bash
python finetuning/invoke_olive.py
```

Los puntos de control y el modelo final se guardarán en la carpeta `models`.

Luego, ejecuta la inferencia con el modelo ajustado a través de chats en una `consola`, `navegador web` o `prompt flow`.

```bash
cd inference

# Interfaz de consola.
python console_chat.py

# La interfaz del navegador web permite ajustar algunos parámetros como la longitud máxima del nuevo token, la temperatura, etc.
# El usuario debe abrir manualmente el enlace (por ejemplo, http://127.0.0.1:7860) en un navegador después de que gradio inicie las conexiones.
python gradio_chat.py
```

Para usar `prompt flow` en VS Code, consulta este [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Ajuste del Modelo

A continuación, descarga el siguiente modelo dependiendo de la disponibilidad de una GPU en tu dispositivo.

Para iniciar la sesión de ajuste local usando QLoRA, selecciona un modelo que quieras ajustar de nuestro catálogo.
| Plataforma(s) | GPU disponible | Nombre del modelo | Tamaño (GB) |
|---------|---------|--------|--------|
| Windows | Sí | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Sí | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | No | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Nota_** No necesitas una cuenta de Azure para descargar los modelos.

El modelo Phi3-mini (int4) tiene aproximadamente un tamaño de 2GB-3GB. Dependiendo de la velocidad de tu red, podría tomar unos minutos descargarlo.

Empieza seleccionando un nombre y una ubicación para el proyecto.
A continuación, selecciona un modelo del catálogo de modelos. Se te pedirá que descargues la plantilla del proyecto. Luego, puedes hacer clic en "Configurar Proyecto" para ajustar varias configuraciones.

### Microsoft Olive

Usamos [Olive](https://microsoft.github.io/Olive/overview/olive.html) para ejecutar el ajuste QLoRA en un modelo PyTorch de nuestro catálogo. Todas las configuraciones están preestablecidas con los valores predeterminados para optimizar el proceso de ajuste local con uso optimizado de memoria, pero se puede ajustar para tu escenario.

### Ejemplos y Recursos de Ajuste

- [Guía de Inicio Rápido para el Ajuste](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Ajuste con un Conjunto de Datos de HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-hf-dataset.md)
- [Ajuste con un Conjunto de Datos Simple](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-simple-dataset.md)

## **[Private Preview]** Desarrollo Remoto
### Requisitos Previos
1. Para ejecutar el ajuste del modelo en tu entorno remoto de Azure Container App, asegúrate de que tu suscripción tenga suficiente capacidad de GPU. Envía un [ticket de soporte](https://azure.microsoft.com/support/create-ticket/) para solicitar la capacidad requerida para tu aplicación. [Obtener más información sobre la capacidad de GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Si estás usando un conjunto de datos privado en HuggingFace, asegúrate de tener una [cuenta de HuggingFace](https://huggingface.co/) y [generar un token de acceso](https://huggingface.co/docs/hub/security-tokens).
3. Habilita la bandera de característica de Ajuste Remoto e Inferencia en el AI Toolkit para VS Code.
   1. Abre la Configuración de VS Code seleccionando *Archivo -> Preferencias -> Configuración*.
   2. Navega a *Extensiones* y selecciona *AI Toolkit*.
   3. Selecciona la opción *"Habilitar Ajuste Remoto e Inferencia"*.
   4. Recarga VS Code para que surta efecto.

- [Ajuste Remoto](https://github.com/microsoft/vscode-ai-toolkit/blob/main/remote-finetuning.md)

### Configurar un Proyecto de Desarrollo Remoto
1. Ejecuta el comando del paleta `AI Toolkit: Focus on Resource View`.
2. Navega a *Model Fine-tuning* para acceder al catálogo de modelos. Asigna un nombre a tu proyecto y selecciona su ubicación en tu máquina. Luego, haz clic en el botón *"Configurar Proyecto"*.
3. Configuración del Proyecto
    1. Evita habilitar la opción *"Ajustar localmente"*.
    2. Las configuraciones de Olive aparecerán con valores predeterminados preestablecidos. Ajusta y completa estas configuraciones según sea necesario.
    3. Continúa con *Generar Proyecto*. Esta etapa aprovecha WSL e implica configurar un nuevo entorno Conda, preparándose para futuras actualizaciones que incluyen Dev Containers.
4. Haz clic en *"Reiniciar Ventana en el Espacio de Trabajo"* para abrir tu proyecto de desarrollo remoto.

> **Nota:** El proyecto actualmente funciona ya sea localmente o remotamente dentro del AI Toolkit para VS Code. Si eliges *"Ajustar localmente"* durante la creación del proyecto, operará exclusivamente en WSL sin capacidades de desarrollo remoto. Por otro lado, si decides no habilitar *"Ajustar localmente"*, el proyecto se restringirá al entorno remoto de Azure Container App.

### Aprovisionar Recursos de Azure
Para empezar, necesitas aprovisionar el Recurso de Azure para el ajuste remoto. Haz esto ejecutando `AI Toolkit: Provision Azure Container Apps job for fine-tuning` desde la paleta de comandos.

Monitorea el progreso del aprovisionamiento a través del enlace mostrado en el canal de salida.

### [Opcional] Agregar Token de Huggingface al Secreto de Azure Container App
Si estás usando un conjunto de datos privado de HuggingFace, configura tu token de HuggingFace como una variable de entorno para evitar la necesidad de iniciar sesión manualmente en el Hugging Face Hub.
Puedes hacer esto usando el comando `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Con este comando, puedes configurar el nombre del secreto como [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) y usar tu token de Hugging Face como el valor del secreto.

### Ejecutar el Ajuste
Para iniciar el trabajo de ajuste remoto, ejecuta el comando `AI Toolkit: Run fine-tuning`.

Para ver los registros del sistema y la consola, puedes visitar el portal de Azure usando el enlace en el panel de salida (más pasos en [Ver y Consultar Registros en Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). O bien, puedes ver los registros de la consola directamente en el panel de salida de VSCode ejecutando el comando `AI Toolkit: Show the running fine-tuning job streaming logs`.
> **Nota:** El trabajo podría estar en cola debido a recursos insuficientes. Si el registro no se muestra, ejecuta el comando `AI Toolkit: Show the running fine-tuning job streaming logs`, espera un momento y luego ejecuta el comando nuevamente para reconectarte al registro en streaming.

Durante este proceso, se usará QLoRA para el ajuste y se crearán adaptadores LoRA para que el modelo los use durante la inferencia.
Los resultados del ajuste se almacenarán en los Archivos de Azure.

### Aprovisionar el Endpoint de Inferencia
Después de que los adaptadores estén entrenados en el entorno remoto, usa una aplicación simple de Gradio para interactuar con el modelo.
Similar al proceso de ajuste, necesitas configurar los Recursos de Azure para la inferencia remota ejecutando `AI Toolkit: Provision Azure Container Apps for inference` desde la paleta de comandos.

Por defecto, la suscripción y el grupo de recursos para la inferencia deben coincidir con los utilizados para el ajuste. La inferencia usará el mismo entorno de Azure Container App y accederá al modelo y al adaptador del modelo almacenado en los Archivos de Azure, que se generaron durante el paso de ajuste.

### Desplegar el Endpoint de Inferencia
Si deseas revisar el código de inferencia o recargar el modelo de inferencia, ejecuta el comando `AI Toolkit: Deploy for inference`. Esto sincronizará tu último código con Azure Container App y reiniciará la réplica.

Una vez que el despliegue se complete con éxito, puedes acceder a la API de inferencia haciendo clic en el botón "*Ir al Endpoint de Inferencia*" mostrado en la notificación de VSCode. O bien, el endpoint de la API web se puede encontrar bajo `ACA_APP_ENDPOINT` en `./infra/inference.config.json` y en el panel de salida. Ahora estás listo para evaluar el modelo usando este endpoint.

### Uso avanzado
Para más información sobre el desarrollo remoto con AI Toolkit, consulta la documentación de [Ajuste de modelos remotamente](https://aka.ms/ai-toolkit/remote-provision) y [Inferencia con el modelo ajustado](https://aka.ms/ai-toolkit/remote-inference).

