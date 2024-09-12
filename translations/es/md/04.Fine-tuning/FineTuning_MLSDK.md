

```markdown
# Importar los módulos necesarios del SDK de Azure AI ML
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# Verificar si la salida `trained_model` está disponible desde el trabajo de la pipeline
print("salidas del trabajo de pipeline: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# Construir una ruta al modelo entrenado formateando una cadena con el nombre del trabajo de la pipeline y el nombre de la salida ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# Definir un nombre para el modelo ajustado añadiendo "-ultrachat-200k" al nombre original del modelo y reemplazando cualquier barra con guiones
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("ruta para registrar el modelo: ", model_path_from_job)

# Preparar para registrar el modelo creando un objeto Model con varios parámetros
# Estos incluyen la ruta al modelo, el tipo de modelo (modelo MLflow), el nombre y la versión del modelo, y una descripción del modelo
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # Usar timestamp como versión para evitar conflictos de versión
    description=model_name + " modelo ajustado para ultrachat 200k chat-completion",
)

print("preparar para registrar el modelo: \n", prepare_to_register_model)

# Registrar el modelo llamando al método create_or_update del objeto models en el workspace_ml_client con el objeto Model como argumento
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# Imprimir el modelo registrado
print("modelo registrado: \n", registered_model)
```


Aviso legal: La traducción fue realizada por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.