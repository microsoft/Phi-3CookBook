# Inferencia Remota con el modelo afinado

Después de que los adaptadores se entrenan en el entorno remoto, utiliza una aplicación simple de Gradio para interactuar con el modelo.

![Fine-tune complete](../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.es.png)

### Aprovisionar Recursos de Azure
Necesitas configurar los Recursos de Azure para la inferencia remota ejecutando `AI Toolkit: Provision Azure Container Apps for inference` desde el paleta de comandos. Durante esta configuración, se te pedirá que selecciones tu Suscripción de Azure y el grupo de recursos.  
![Provision Inference Resource](../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.es.png)
   
Por defecto, la suscripción y el grupo de recursos para la inferencia deben coincidir con los utilizados para la afinación. La inferencia utilizará el mismo entorno de Azure Container App y accederá al modelo y al adaptador del modelo almacenados en Azure Files, que se generaron durante el paso de afinación.

## Usando AI Toolkit 

### Despliegue para Inferencia  
Si deseas revisar el código de inferencia o recargar el modelo de inferencia, por favor ejecuta el comando `AI Toolkit: Deploy for inference`. Esto sincronizará tu último código con ACA y reiniciará la réplica.  

![Deploy for inference](../../../../translated_images/command-deploy.a2c9346bd1b7ac9b9fd49fc5e95871a974fbfd647f6c50331f8daa6e45121225.es.png)

Después de completar exitosamente el despliegue, el modelo estará listo para evaluación usando este endpoint.

### Acceso a la API de Inferencia

Puedes acceder a la API de inferencia haciendo clic en el botón "*Go to Inference Endpoint*" mostrado en la notificación de VSCode. Alternativamente, el endpoint de la web API se puede encontrar bajo `ACA_APP_ENDPOINT` en `./infra/inference.config.json` y en el panel de salida.

![App Endpoint](../../../../translated_images/notification-deploy.79f6704239f7d016da3bf72b5c661961c8ddd17147fad195f6282df94d489a86.es.png)

> **Note:** El endpoint de inferencia puede requerir unos minutos para estar completamente operativo.

## Componentes de Inferencia Incluidos en la Plantilla
 
| Carpeta | Contenido |
| ------ |--------- |
| `infra` | Contiene todas las configuraciones necesarias para operaciones remotas. |
| `infra/provision/inference.parameters.json` | Contiene parámetros para las plantillas bicep, usadas para aprovisionar recursos de Azure para inferencia. |
| `infra/provision/inference.bicep` | Contiene plantillas para aprovisionar recursos de Azure para inferencia. |
| `infra/inference.config.json` | El archivo de configuración, generado por el comando `AI Toolkit: Provision Azure Container Apps for inference`. Se utiliza como entrada para otros paletas de comandos remotos. |

### Usando AI Toolkit para configurar el Aprovisionamiento de Recursos de Azure
Configura el [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Comando `Provision Azure Container Apps for inference`.

Puedes encontrar los parámetros de configuración en el archivo `./infra/provision/inference.parameters.json`. Aquí están los detalles:
| Parámetro | Descripción |
| --------- |------------ |
| `defaultCommands` | Estos son los comandos para iniciar una web API. |
| `maximumInstanceCount` | Este parámetro establece la capacidad máxima de instancias GPU. |
| `location` | Esta es la ubicación donde se aprovisionan los recursos de Azure. El valor por defecto es el mismo que la ubicación del grupo de recursos elegido. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | Estos parámetros se utilizan para nombrar los recursos de Azure para aprovisionamiento. Por defecto, serán los mismos que los nombres de recursos de afinación. Puedes ingresar un nuevo nombre de recurso no utilizado para crear tus propios recursos personalizados, o puedes ingresar el nombre de un recurso de Azure ya existente si prefieres usar ese. Para más detalles, consulta la sección [Using existing Azure Resources](#using-existing-azure-resources). |

### Usando Recursos de Azure Existentes

Por defecto, el aprovisionamiento de inferencia utiliza el mismo entorno de Azure Container App, Cuenta de Almacenamiento, Azure File Share, y Azure Log Analytics que se usaron para la afinación. Se crea una Azure Container App separada únicamente para la API de inferencia. 

Si has personalizado los recursos de Azure durante el paso de afinación o deseas usar tus propios recursos de Azure existentes para la inferencia, especifica sus nombres en el archivo `./infra/inference.parameters.json`. Luego, ejecuta el comando `AI Toolkit: Provision Azure Container Apps for inference` desde el paleta de comandos. Esto actualizará cualquier recurso especificado y creará cualquier recurso que falte.

Por ejemplo, si tienes un entorno de contenedor de Azure existente, tu `./infra/finetuning.parameters.json` debería verse así:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### Aprovisionamiento Manual  
Si prefieres configurar manualmente los recursos de Azure, puedes usar los archivos bicep proporcionados en las carpetas `./infra/provision`. Si ya has configurado todos los recursos de Azure sin usar el paleta de comandos de AI Toolkit, simplemente ingresa los nombres de los recursos en el archivo `inference.config.json`.

Por ejemplo:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

        Descargo de responsabilidad: La traducción fue realizada por un modelo de IA y puede no ser perfecta. 
        Por favor, revise el resultado y haga las correcciones necesarias.