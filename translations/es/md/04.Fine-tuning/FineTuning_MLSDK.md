
Importa el módulo os, que proporciona una manera portátil de usar funcionalidades dependientes del sistema operativo. Utiliza la función os.system para ejecutar el script download-dataset.py en la terminal con argumentos específicos de línea de comando. Los argumentos especifican el conjunto de datos a descargar (HuggingFaceH4/ultrachat_200k), el directorio donde descargarlo (ultrachat_200k_dataset), y el porcentaje del conjunto de datos a dividir (5). La función os.system devuelve el estado de salida del comando que ejecutó; este estado se almacena en la variable exit_status. Verifica si exit_status no es 0. En sistemas operativos tipo Unix, un estado de salida de 0 generalmente indica que un comando ha tenido éxito, mientras que cualquier otro número indica un error. Si exit_status no es 0, lanza una Excepción con un mensaje que indica que hubo un error al descargar el conjunto de datos. En resumen, este script está ejecutando un comando para descargar un conjunto de datos usando un script auxiliar, y lanza una excepción si el comando falla. ```
# Importa el módulo os, que proporciona una manera de usar funcionalidades dependientes del sistema operativo
import os

# Usa la función os.system para ejecutar el script download-dataset.py en la terminal con argumentos específicos de línea de comando
# Los argumentos especifican el conjunto de datos a descargar (HuggingFaceH4/ultrachat_200k), el directorio donde descargarlo (ultrachat_200k_dataset), y el porcentaje del conjunto de datos a dividir (5)
# La función os.system devuelve el estado de salida del comando que ejecutó; este estado se almacena en la variable exit_status
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# Verifica si exit_status no es 0
# En sistemas operativos tipo Unix, un estado de salida de 0 generalmente indica que un comando ha tenido éxito, mientras que cualquier otro número indica un error
# Si exit_status no es 0, lanza una Excepción con un mensaje que indica que hubo un error al descargar el conjunto de datos
if exit_status != 0:
    raise Exception("Error downloading dataset")
```
### Cargando Datos en un DataFrame
Este script de Python está cargando un archivo JSON Lines en un DataFrame de pandas y mostrando las primeras 5 filas. Aquí tienes un desglose de lo que hace:

Importa la biblioteca pandas, que es una poderosa herramienta para la manipulación y análisis de datos.

Establece el ancho máximo de columna para las opciones de visualización de pandas en 0. Esto significa que el texto completo de cada columna se mostrará sin truncar cuando se imprima el DataFrame.

Utiliza la función pd.read_json para cargar el archivo train_sft.jsonl desde el directorio ultrachat_200k_dataset en un DataFrame. El argumento lines=True indica que el archivo está en formato JSON Lines, donde cada línea es un objeto JSON separado.

Utiliza el método head para mostrar las primeras 5 filas del DataFrame. Si el DataFrame tiene menos de 5 filas, mostrará todas ellas.

En resumen, este script está cargando un archivo JSON Lines en un DataFrame y mostrando las primeras 5 filas con el texto completo de las columnas.

```
# Importa la biblioteca pandas, que es una poderosa herramienta para la manipulación y análisis de datos
import pandas as pd

# Establece el ancho máximo de columna para las opciones de visualización de pandas en 0
# Esto significa que el texto completo de cada columna se mostrará sin truncar cuando se imprima el DataFrame
pd.set_option("display.max_colwidth", 0)

# Usa la función pd.read_json para cargar el archivo train_sft.jsonl desde el directorio ultrachat_200k_dataset en un DataFrame
# El argumento lines=True indica que el archivo está en formato JSON Lines, donde cada línea es un objeto JSON separado
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# Usa el método head para mostrar las primeras 5 filas del DataFrame
# Si el DataFrame tiene menos de 5 filas, mostrará todas ellas
df.head()
```
## 5. Enviar el trabajo de ajuste fino usando el modelo y los datos como entradas
Crea el trabajo que utiliza el componente del pipeline chat-completion. Aprende más sobre todos los parámetros que se soportan para el ajuste fino.

### Definir parámetros de ajuste fino

Los parámetros de ajuste fino se pueden agrupar en 2 categorías: parámetros de entrenamiento y parámetros de optimización.

Los parámetros de entrenamiento definen los aspectos del entrenamiento como:

- El optimizador, el planificador a usar
- La métrica para optimizar el ajuste fino
- Número de pasos de entrenamiento y el tamaño del lote, entre otros
- Los parámetros de optimización ayudan a optimizar la memoria GPU y a usar eficazmente los recursos de cómputo.

A continuación se muestran algunos de los parámetros que pertenecen a esta categoría. Los parámetros de optimización difieren para cada modelo y se empaquetan con el modelo para manejar estas variaciones.

- Habilitar deepspeed y LoRA
- Habilitar entrenamiento de precisión mixta
- Habilitar entrenamiento multi-nodo

**Nota:** El ajuste fino supervisado puede resultar en la pérdida de alineación o en el olvido catastrófico. Recomendamos revisar este problema y ejecutar una etapa de alineación después de realizar el ajuste fino.

### Parámetros de Ajuste Fino

Este script de Python está configurando parámetros para el ajuste fino de un modelo de aprendizaje automático. Aquí tienes un desglose de lo que hace:

Configura parámetros de entrenamiento predeterminados como el número de épocas de entrenamiento, tamaños de lote para entrenamiento y evaluación, tasa de aprendizaje y tipo de planificador de tasa de aprendizaje.

Configura parámetros de optimización predeterminados como si aplicar Propagación de Relevancia por Capas (LoRa) y DeepSpeed, y la etapa de DeepSpeed.

Combina los parámetros de entrenamiento y optimización en un único diccionario llamado finetune_parameters.

Verifica si el foundation_model tiene parámetros predeterminados específicos del modelo. Si es así, imprime un mensaje de advertencia y actualiza el diccionario finetune_parameters con estos valores predeterminados específicos del modelo. La función ast.literal_eval se utiliza para convertir los valores predeterminados específicos del modelo de una cadena a un diccionario de Python.

Imprime el conjunto final de parámetros de ajuste fino que se utilizarán para la ejecución.

En resumen, este script está configurando y mostrando los parámetros para el ajuste fino de un modelo de aprendizaje automático, con la capacidad de sobrescribir los parámetros predeterminados con los específicos del modelo.

```
# Configura parámetros de entrenamiento predeterminados como el número de épocas de entrenamiento, tamaños de lote para entrenamiento y evaluación, tasa de aprendizaje, y tipo de planificador de tasa de aprendizaje
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# Configura parámetros de optimización predeterminados como si aplicar Propagación de Relevancia por Capas (LoRa) y DeepSpeed, y la etapa de DeepSpeed
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# Combina los parámetros de entrenamiento y optimización en un único diccionario llamado finetune_parameters
finetune_parameters = {**training_parameters, **optimization_parameters}

# Verifica si el foundation_model tiene parámetros predeterminados específicos del modelo
# Si es así, imprime un mensaje de advertencia y actualiza el diccionario finetune_parameters con estos valores predeterminados específicos del modelo
# La función ast.literal_eval se utiliza para convertir los valores predeterminados específicos del modelo de una cadena a un diccionario de Python
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # convert string to python dict
            foundation_model.tags["model_specific_defaults"]
        )
    )

# Imprime el conjunto final de parámetros de ajuste fino que se utilizarán para la ejecución
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### Pipeline de Entrenamiento
Este script de Python está definiendo una función para generar un nombre de visualización para un pipeline de entrenamiento de aprendizaje automático, y luego llama a esta función para generar e imprimir el nombre de visualización. Aquí tienes un desglose de lo que hace:

Se define la función get_pipeline_display_name. Esta función genera un nombre de visualización basado en varios parámetros relacionados con el pipeline de entrenamiento.

Dentro de la función, calcula el tamaño total del lote multiplicando el tamaño del lote por dispositivo, el número de pasos de acumulación de gradientes, el número de GPUs por nodo y el número de nodos utilizados para el ajuste fino.

Recupera varios otros parámetros como el tipo de planificador de tasa de aprendizaje, si se aplica DeepSpeed, la etapa de DeepSpeed, si se aplica Propagación de Relevancia por Capas (LoRa), el límite en el número de puntos de control del modelo a mantener, y la longitud máxima de secuencia.

Construye una cadena que incluye todos estos parámetros, separados por guiones. Si se aplica DeepSpeed o LoRa, la cadena incluye "ds" seguido de la etapa de DeepSpeed, o "lora", respectivamente. Si no, incluye "nods" o "nolora", respectivamente.

La función devuelve esta cadena, que sirve como nombre de visualización para el pipeline de entrenamiento.

Después de definir la función, se llama para generar el nombre de visualización, que luego se imprime.

En resumen, este script está generando un nombre de visualización para un pipeline de entrenamiento de aprendizaje automático basado en varios parámetros, y luego imprime este nombre de visualización.

```
# Define una función para generar un nombre de visualización para el pipeline de entrenamiento
def get_pipeline_display_name():
    # Calcula el tamaño total del lote multiplicando el tamaño del lote por dispositivo, el número de pasos de acumulación de gradientes, el número de GPUs por nodo y el número de nodos utilizados para el ajuste fino
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # Recupera el tipo de planificador de tasa de aprendizaje
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # Recupera si se aplica DeepSpeed
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # Recupera la etapa de DeepSpeed
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # Si se aplica DeepSpeed, incluye "ds" seguido de la etapa de DeepSpeed en el nombre de visualización; si no, incluye "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # Recupera si se aplica Propagación de Relevancia por Capas (LoRa)
    lora = finetune_parameters.get("apply_lora", "false")
    # Si se aplica LoRa, incluye "lora" en el nombre de visualización; si no, incluye "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # Recupera el límite en el número de puntos de control del modelo a mantener
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # Recupera la longitud máxima de secuencia
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # Construye el nombre de visualización concatenando todos estos parámetros, separados por guiones
    return (
        model_name
        + "-"
        + "ultrachat"
        + "-"
        + f"bs{batch_size}"
        + "-"
        + f"{scheduler}"
        + "-"
        + ds_string
        + "-"
        + lora_string
        + f"-save_limit{save_limit}"
        + f"-seqlen{seq_len}"
    )

# Llama a la función para generar el nombre de visualización
pipeline_display_name = get_pipeline_display_name()
# Imprime el nombre de visualización
print(f"Display name used for the run: {pipeline_display_name}")
```
### Configurando el Pipeline

Este script de Python está definiendo y configurando un pipeline de aprendizaje automático usando el SDK de Azure Machine Learning. Aquí tienes un desglose de lo que hace:

1. Importa los módulos necesarios del SDK de Azure AI ML.

2. Obtiene un componente de pipeline llamado "chat_completion_pipeline" del registro.

3. Define un trabajo de pipeline usando el decorador `@pipeline` y la función `create_pipeline`. El nombre del pipeline se establece en `pipeline_display_name`.

4. Dentro de la función `create_pipeline`, inicializa el componente de pipeline obtenido con varios parámetros, incluyendo la ruta del modelo, los clústeres de cómputo para diferentes etapas, divisiones de conjuntos de datos para entrenamiento y prueba, el número de GPUs a usar para el ajuste fino, y otros parámetros de ajuste fino.

5. Mapea la salida del trabajo de ajuste fino a la salida del trabajo de pipeline. Esto se hace para que el modelo ajustado se pueda registrar fácilmente, lo cual es necesario para desplegar el modelo en un endpoint en línea o por lotes.

6. Crea una instancia del pipeline llamando a la función `create_pipeline`.

7. Establece la configuración `force_rerun` del pipeline en `True`, lo que significa que no se usarán resultados en caché de trabajos anteriores.

8. Establece la configuración `continue_on_step_failure` del pipeline en `False`, lo que significa que el pipeline se detendrá si alguna etapa falla.

En resumen, este script está definiendo y configurando un pipeline de aprendizaje automático para una tarea de completación de chat usando el SDK de Azure Machine Learning.

```
# Importa los módulos necesarios del SDK de Azure AI ML
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# Obtiene el componente de pipeline llamado "chat_completion_pipeline" del registro
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# Define el trabajo de pipeline usando el decorador @pipeline y la función create_pipeline
# El nombre del pipeline se establece en pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # Inicializa el componente de pipeline obtenido con varios parámetros
    # Estos incluyen la ruta del modelo, clústeres de cómputo para diferentes etapas, divisiones de conjuntos de datos para entrenamiento y prueba, el número de GPUs a usar para el ajuste fino, y otros parámetros de ajuste fino
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # Mapea las divisiones de conjuntos de datos a parámetros
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # Configuración de entrenamiento
        number_of_gpu_to_use_finetuning=gpus_per_node,  # Establecer al número de GPUs disponibles en el cómputo
        **finetune_parameters
    )
    return {
        # Mapea la salida del trabajo de ajuste fino a la salida del trabajo de pipeline
        # Esto se hace para que podamos registrar fácilmente el modelo ajustado
        # Registrar el modelo es necesario para desplegar el modelo en un endpoint en línea o por lotes
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# Crea una instancia del pipeline llamando a la función create_pipeline
pipeline_object = create_pipeline()

# No usar resultados en caché de trabajos anteriores
pipeline_object.settings.force_rerun = True

# Establecer continuar en caso de fallo de etapa en False
# Esto significa que el pipeline se detendrá si alguna etapa falla
pipeline_object.settings.continue_on_step_failure = False
```
### Enviar el Trabajo

Este script de Python está enviando un trabajo de pipeline de aprendizaje automático a un espacio de trabajo de Azure Machine Learning y luego espera a que el trabajo se complete. Aquí tienes un desglose de lo que hace:

Llama al método create_or_update del objeto jobs en el workspace_ml_client para enviar el trabajo de pipeline. El pipeline a ejecutar se especifica mediante pipeline_object, y el experimento bajo el cual se ejecuta el trabajo se especifica mediante experiment_name.

Luego llama al método stream del objeto jobs en el workspace_ml_client para esperar a que el trabajo de pipeline se complete. El trabajo a esperar se especifica mediante el atributo name del objeto pipeline_job.

En resumen, este script está enviando un trabajo de pipeline de aprendizaje automático a un espacio de trabajo de Azure Machine Learning, y luego espera a que el trabajo se complete.

```
# Enviar el trabajo de pipeline al espacio de trabajo de Azure Machine Learning
# El pipeline a ejecutar se especifica mediante pipeline_object
# El experimento bajo el cual se ejecuta el trabajo se especifica mediante experiment_name
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# Esperar a que el trabajo de pipeline se complete
# El trabajo a esperar se especifica mediante el atributo name del objeto pipeline_job
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. Registrar el modelo ajustado con el espacio de trabajo
Registraremos el modelo desde la salida del trabajo de ajuste fino. Esto rastreará la línea de tiempo entre el modelo ajustado y el trabajo de ajuste fino. El trabajo de ajuste fino, además, rastrea la línea de tiempo hacia el modelo base, los datos y el código de entrenamiento.

### Registrando el Modelo de ML
Este script de Python está registrando un modelo de aprendizaje automático que fue entrenado en un pipeline de Azure Machine Learning. Aquí tienes un desglose de lo que hace:

Importa los módulos necesarios del SDK de Azure AI ML.

Verifica si la salida trained_model está disponible desde el trabajo de pipeline llamando al método get del objeto jobs en el workspace_ml_client y accediendo a su atributo outputs.

Construye una ruta al modelo entrenado formateando una cadena con el nombre del trabajo de pipeline y el nombre de la salida ("trained_model").

Define un nombre para el modelo ajustado
```
# Importar los módulos necesarios del SDK de Azure AI ML
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# Verificar si la salida `trained_model` está disponible en el trabajo del pipeline
print("salidas del trabajo del pipeline: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# Construir una ruta al modelo entrenado formateando una cadena con el nombre del trabajo del pipeline y el nombre de la salida ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# Definir un nombre para el modelo ajustado agregando "-ultrachat-200k" al nombre original del modelo y reemplazando cualquier barra con guiones
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("ruta para registrar el modelo: ", model_path_from_job)

# Preparar para registrar el modelo creando un objeto Model con varios parámetros
# Estos incluyen la ruta al modelo, el tipo de modelo (modelo MLflow), el nombre y la versión del modelo, y una descripción del modelo
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # Usar timestamp como versión para evitar conflicto de versiones
    description=model_name + " modelo ajustado para ultrachat 200k chat-completion",
)

print("preparar para registrar el modelo: \n", prepare_to_register_model)

# Registrar el modelo llamando al método create_or_update del objeto models en workspace_ml_client con el objeto Model como argumento
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# Imprimir el modelo registrado
print("modelo registrado: \n", registered_model)
```
## 7. Desplegar el modelo ajustado a un endpoint en línea
Los endpoints en línea proporcionan una API REST duradera que se puede usar para integrarse con aplicaciones que necesiten utilizar el modelo.

### Administrar Endpoint
Este script de Python está creando un endpoint en línea gestionado en Azure Machine Learning para un modelo registrado. Aquí tienes un desglose de lo que hace:

Importa los módulos necesarios del SDK de Azure AI ML.

Define un nombre único para el endpoint en línea añadiendo una marca de tiempo a la cadena "ultrachat-completion-".

Prepara la creación del endpoint en línea creando un objeto ManagedOnlineEndpoint con varios parámetros, incluyendo el nombre del endpoint, una descripción del endpoint y el modo de autenticación ("key").

Crea el endpoint en línea llamando al método begin_create_or_update del workspace_ml_client con el objeto ManagedOnlineEndpoint como argumento. Luego espera a que la operación de creación se complete llamando al método wait.

En resumen, este script está creando un endpoint en línea gestionado en Azure Machine Learning para un modelo registrado.

```
# Importar los módulos necesarios del SDK de Azure AI ML
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# Definir un nombre único para el endpoint en línea añadiendo una marca de tiempo a la cadena "ultrachat-completion-"
online_endpoint_name = "ultrachat-completion-" + timestamp

# Preparar la creación del endpoint en línea creando un objeto ManagedOnlineEndpoint con varios parámetros
# Estos incluyen el nombre del endpoint, una descripción del endpoint y el modo de autenticación ("key")
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# Crear el endpoint en línea llamando al método begin_create_or_update del workspace_ml_client con el objeto ManagedOnlineEndpoint como argumento
# Luego esperar a que la operación de creación se complete llamando al método wait
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
Puedes encontrar aquí la lista de SKU's soportados para el despliegue - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Desplegar el Modelo de ML

Este script de Python está desplegando un modelo de aprendizaje automático registrado en un endpoint en línea gestionado en Azure Machine Learning. Aquí tienes un desglose de lo que hace:

Importa el módulo ast, que proporciona funciones para procesar árboles de la gramática de sintaxis abstracta de Python.

Establece el tipo de instancia para el despliegue en "Standard_NC6s_v3".

Verifica si la etiqueta inference_compute_allow_list está presente en el modelo base. Si lo está, convierte el valor de la etiqueta de una cadena a una lista de Python y lo asigna a inference_computes_allow_list. Si no lo está, establece inference_computes_allow_list en None.

Verifica si el tipo de instancia especificado está en la lista permitida. Si no lo está, imprime un mensaje pidiendo al usuario que seleccione un tipo de instancia de la lista permitida.

Prepara la creación del despliegue creando un objeto ManagedOnlineDeployment con varios parámetros, incluyendo el nombre del despliegue, el nombre del endpoint, el ID del modelo, el tipo y la cantidad de instancias, las configuraciones de la sonda de vitalidad y las configuraciones de la solicitud.

Crea el despliegue llamando al método begin_create_or_update del workspace_ml_client con el objeto ManagedOnlineDeployment como argumento. Luego espera a que la operación de creación se complete llamando al método wait.

Establece el tráfico del endpoint para dirigir el 100% del tráfico al despliegue "demo".

Actualiza el endpoint llamando al método begin_create_or_update del workspace_ml_client con el objeto endpoint como argumento. Luego espera a que la operación de actualización se complete llamando al método result.

En resumen, este script está desplegando un modelo de aprendizaje automático registrado en un endpoint en línea gestionado en Azure Machine Learning.

```
# Importar el módulo ast, que proporciona funciones para procesar árboles de la gramática de sintaxis abstracta de Python
import ast

# Establecer el tipo de instancia para el despliegue
instance_type = "Standard_NC6s_v3"

# Verificar si la etiqueta `inference_compute_allow_list` está presente en el modelo base
if "inference_compute_allow_list" in foundation_model.tags:
    # Si lo está, convertir el valor de la etiqueta de una cadena a una lista de Python y asignarlo a `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # Si no lo está, establecer `inference_computes_allow_list` en `None`
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# Verificar si el tipo de instancia especificado está en la lista permitida
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# Preparar la creación del despliegue creando un objeto `ManagedOnlineDeployment` con varios parámetros
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# Crear el despliegue llamando al método `begin_create_or_update` del `workspace_ml_client` con el objeto `ManagedOnlineDeployment` como argumento
# Luego esperar a que la operación de creación se complete llamando al método `wait`
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# Establecer el tráfico del endpoint para dirigir el 100% del tráfico al despliegue "demo"
endpoint.traffic = {"demo": 100}

# Actualizar el endpoint llamando al método `begin_create_or_update` del `workspace_ml_client` con el objeto `endpoint` como argumento
# Luego esperar a que la operación de actualización se complete llamando al método `result`
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. Probar el endpoint con datos de muestra
Vamos a obtener algunos datos de muestra del conjunto de datos de prueba y enviarlos al endpoint en línea para inferencia. Luego mostraremos las etiquetas puntuadas junto a las etiquetas de verdad del terreno.

### Leyendo los resultados
Este script de Python está leyendo un archivo JSON Lines en un DataFrame de pandas, tomando una muestra aleatoria y restableciendo el índice. Aquí tienes un desglose de lo que hace:

Lee el archivo ./ultrachat_200k_dataset/test_gen.jsonl en un DataFrame de pandas. La función read_json se usa con el argumento lines=True porque el archivo está en formato JSON Lines, donde cada línea es un objeto JSON separado.

Toma una muestra aleatoria de 1 fila del DataFrame. La función sample se usa con el argumento n=1 para especificar el número de filas aleatorias a seleccionar.

Restablece el índice del DataFrame. La función reset_index se usa con el argumento drop=True para eliminar el índice original y reemplazarlo con un nuevo índice de valores enteros por defecto.

Muestra las primeras 2 filas del DataFrame usando la función head con el argumento 2. Sin embargo, dado que el DataFrame solo contiene una fila después del muestreo, esto solo mostrará esa fila.

En resumen, este script está leyendo un archivo JSON Lines en un DataFrame de pandas, tomando una muestra aleatoria de 1 fila, restableciendo el índice y mostrando la primera fila.

```
# Importar la biblioteca pandas
import pandas as pd

# Leer el archivo JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' en un DataFrame de pandas
# El argumento 'lines=True' indica que el archivo está en formato JSON Lines, donde cada línea es un objeto JSON separado
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# Tomar una muestra aleatoria de 1 fila del DataFrame
# El argumento 'n=1' especifica el número de filas aleatorias a seleccionar
test_df = test_df.sample(n=1)

# Restablecer el índice del DataFrame
# El argumento 'drop=True' indica que el índice original debe eliminarse y reemplazarse con un nuevo índice de valores enteros por defecto
# El argumento 'inplace=True' indica que el DataFrame debe modificarse en su lugar (sin crear un nuevo objeto)
test_df.reset_index(drop=True, inplace=True)

# Mostrar las primeras 2 filas del DataFrame
# Sin embargo, dado que el DataFrame solo contiene una fila después del muestreo, esto solo mostrará esa fila
test_df.head(2)
```
### Crear Objeto JSON

Este script de Python está creando un objeto JSON con parámetros específicos y guardándolo en un archivo. Aquí tienes un desglose de lo que hace:

Importa el módulo json, que proporciona funciones para trabajar con datos JSON.

Crea un diccionario parameters con claves y valores que representan parámetros para un modelo de aprendizaje automático. Las claves son "temperature", "top_p", "do_sample" y "max_new_tokens", y sus valores correspondientes son 0.6, 0.9, True y 200 respectivamente.

Crea otro diccionario test_json con dos claves: "input_data" y "params". El valor de "input_data" es otro diccionario con claves "input_string" y "parameters". El valor de "input_string" es una lista que contiene el primer mensaje del DataFrame test_df. El valor de "parameters" es el diccionario parameters creado anteriormente. El valor de "params" es un diccionario vacío.

Abre un archivo llamado sample_score.json en el directorio ./ultrachat_200k_dataset en modo escritura.

```
# Importar el módulo json, que proporciona funciones para trabajar con datos JSON
import json

# Crear un diccionario `parameters` con claves y valores que representan parámetros para un modelo de aprendizaje automático
# Las claves son "temperature", "top_p", "do_sample" y "max_new_tokens", y sus valores correspondientes son 0.6, 0.9, True y 200 respectivamente
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# Crear otro diccionario `test_json` con dos claves: "input_data" y "params"
# El valor de "input_data" es otro diccionario con claves "input_string" y "parameters"
# El valor de "input_string" es una lista que contiene el primer mensaje del DataFrame `test_df`
# El valor de "parameters" es el diccionario `parameters` creado anteriormente
# El valor de "params" es un diccionario vacío
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# Abrir un archivo llamado `sample_score.json` en el directorio `./ultrachat_200k_dataset` en modo escritura
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # Escribir el diccionario `test_json` en el archivo en formato JSON usando la función `json.dump`
    json.dump(test_json, f)
```
### Invocando el Endpoint

Este script de Python está invocando un endpoint en línea en Azure Machine Learning para puntuar un archivo JSON. Aquí tienes un desglose de lo que hace:

Llama al método invoke de la propiedad online_endpoints del objeto workspace_ml_client. Este método se usa para enviar una solicitud a un endpoint en línea y obtener una respuesta.

Especifica el nombre del endpoint y el despliegue con los argumentos endpoint_name y deployment_name. En este caso, el nombre del endpoint se almacena en la variable online_endpoint_name y el nombre del despliegue es "demo".

Especifica la ruta al archivo JSON a puntuar con el argumento request_file. En este caso, el archivo es ./ultrachat_200k_dataset/sample_score.json.

Almacena la respuesta del endpoint en la variable response.

Imprime la respuesta en bruto.

En resumen, este script está invocando un endpoint en línea en Azure Machine Learning para puntuar un archivo JSON e imprimiendo la respuesta.

```
# Invocar el endpoint en línea en Azure Machine Learning para puntuar el archivo `sample_score.json`
# El método `invoke` de la propiedad `online_endpoints` del objeto `workspace_ml_client` se usa para enviar una solicitud a un endpoint en línea y obtener una respuesta
# El argumento `endpoint_name` especifica el nombre del endpoint, que se almacena en la variable `online_endpoint_name`
# El argumento `deployment_name` especifica el nombre del despliegue, que es "demo"
# El argumento `request_file` especifica la ruta al archivo JSON a puntuar, que es `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# Imprimir la respuesta en bruto del endpoint
print("raw response: \n", response, "\n")
```
## 9. Eliminar el endpoint en línea
No olvides eliminar el endpoint en línea, de lo contrario, dejarás el contador de facturación en funcionamiento para el cómputo utilizado por el endpoint. Esta línea de código en Python está eliminando un endpoint en línea en Azure Machine Learning. Aquí tienes un desglose de lo que hace:

Llama al método begin_delete de la propiedad online_endpoints del objeto workspace_ml_client. Este método se usa para iniciar la eliminación de un endpoint en línea.

Especifica el nombre del endpoint a eliminar con el argumento name. En este caso, el nombre del endpoint se almacena en la variable online_endpoint_name.

Llama al método wait para esperar a que la operación de eliminación se complete. Esta es una operación de bloqueo, lo que significa que evitará que el script continúe hasta que la eliminación haya finalizado.

En resumen, esta línea de código está iniciando la eliminación de un endpoint en línea en Azure Machine Learning y esperando a que la operación se complete.

```
# Eliminar el endpoint en línea en Azure Machine Learning
# El método `begin_delete` de la propiedad `online_endpoints` del objeto `workspace_ml_client` se usa para iniciar la eliminación de un endpoint en línea
# El argumento `name` especifica el nombre del endpoint a eliminar, que se almacena en la variable `online_endpoint_name`
# Se llama al método `wait` para esperar a que la operación de eliminación se complete. Esta es una operación de bloqueo, lo que significa que evitará que el script continúe hasta que la eliminación haya finalizado
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.