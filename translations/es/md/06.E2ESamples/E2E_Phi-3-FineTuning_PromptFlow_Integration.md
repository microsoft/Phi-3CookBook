# Ajusta y Integra modelos personalizados Phi-3 con Prompt flow

Este ejemplo de extremo a extremo (E2E) se basa en la guía "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" de la comunidad técnica de Microsoft. Introduce los procesos de ajuste fino, despliegue e integración de modelos Phi-3 personalizados con Prompt flow.

## Descripción General

En este ejemplo E2E, aprenderás cómo ajustar el modelo Phi-3 e integrarlo con Prompt flow. Aprovechando Azure Machine Learning y Prompt flow, establecerás un flujo de trabajo para desplegar y utilizar modelos de IA personalizados. Este ejemplo E2E se divide en tres escenarios:

**Escenario 1: Configura los recursos de Azure y prepárate para el ajuste fino**

**Escenario 2: Ajusta el modelo Phi-3 y despliega en Azure Machine Learning Studio**

**Escenario 3: Integra con Prompt flow y chatea con tu modelo personalizado**

Aquí tienes una visión general de este ejemplo E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../translated_images/00-01-architecture.8105090d271b94fffec713da4c928ae31366b3521c18eec086cd4d2a3bddb3c4.es.png)

### Tabla de Contenidos

1. **[Escenario 1: Configura los recursos de Azure y prepárate para el ajuste fino](../../../../md/06.E2ESamples)**
    - [Crear un Azure Machine Learning Workspace](../../../../md/06.E2ESamples)
    - [Solicitar cuotas de GPU en la suscripción de Azure](../../../../md/06.E2ESamples)
    - [Agregar asignación de roles](../../../../md/06.E2ESamples)
    - [Configurar el proyecto](../../../../md/06.E2ESamples)
    - [Preparar el conjunto de datos para el ajuste fino](../../../../md/06.E2ESamples)

1. **[Escenario 2: Ajustar el modelo Phi-3 y desplegar en Azure Machine Learning Studio](../../../../md/06.E2ESamples)**
    - [Configurar Azure CLI](../../../../md/06.E2ESamples)
    - [Ajustar el modelo Phi-3](../../../../md/06.E2ESamples)
    - [Desplegar el modelo ajustado](../../../../md/06.E2ESamples)

1. **[Escenario 3: Integra con Prompt flow y chatea con tu modelo personalizado](../../../../md/06.E2ESamples)**
    - [Integrar el modelo Phi-3 personalizado con Prompt flow](../../../../md/06.E2ESamples)
    - [Chatear con tu modelo personalizado](../../../../md/06.E2ESamples)

## Escenario 1: Configura los recursos de Azure y prepárate para el ajuste fino

### Crear un Azure Machine Learning Workspace

1. Escribe *azure machine learning* en la **barra de búsqueda** en la parte superior de la página del portal y selecciona **Azure Machine Learning** de las opciones que aparecen.

    ![Type azure machine learning](../../../../translated_images/01-01-type-azml.30fc3af530e71efb5187e52631f92a1377a4ab54b8d985f588b35c06019ccc9f.es.png)

1. Selecciona **+ Create** del menú de navegación.

1. Selecciona **New workspace** del menú de navegación.

    ![Select new workspace](../../../../translated_images/01-02-select-new-workspace.e57f445179f0c022dcc899843751864d2638d13e91e521ab9b60828b516852c0.es.png)

1. Realiza las siguientes tareas:

    - Selecciona tu **Suscripción** de Azure.
    - Selecciona el **Grupo de recursos** a utilizar (crea uno nuevo si es necesario).
    - Introduce el **Nombre del espacio de trabajo**. Debe ser un valor único.
    - Selecciona la **Región** que deseas usar.
    - Selecciona la **Cuenta de almacenamiento** a utilizar (crea una nueva si es necesario).
    - Selecciona el **Key vault** a utilizar (crea uno nuevo si es necesario).
    - Selecciona **Application insights** a utilizar (crea uno nuevo si es necesario).
    - Selecciona el **Registro de contenedores** a utilizar (crea uno nuevo si es necesario).

    ![Fill AZML.](../../../../translated_images/01-03-fill-AZML.3bdb688242c6de17de9add70865278d88a60efb58686b351cec608ab5152d6d6.es.png)

1. Selecciona **Review + Create**.

1. Selecciona **Create**.

### Solicitar cuotas de GPU en la suscripción de Azure

En este ejemplo E2E, utilizarás la *GPU Standard_NC24ads_A100_v4* para el ajuste fino, que requiere una solicitud de cuota, y la CPU *Standard_E4s_v3* para el despliegue, que no requiere una solicitud de cuota.

> [!NOTE]
>
> Solo las suscripciones Pay-As-You-Go (el tipo estándar de suscripción) son elegibles para la asignación de GPU; las suscripciones de beneficios no son actualmente compatibles.
>
> Para aquellos que usan suscripciones de beneficios (como Visual Studio Enterprise Subscription) o aquellos que buscan probar rápidamente el proceso de ajuste fino y despliegue, este tutorial también proporciona orientación para el ajuste fino con un conjunto de datos mínimo usando una CPU. Sin embargo, es importante notar que los resultados del ajuste fino son significativamente mejores cuando se usa una GPU con conjuntos de datos más grandes.

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Realiza las siguientes tareas para solicitar la cuota de *Standard NCADSA100v4 Family*:

    - Selecciona **Quota** del menú lateral.
    - Selecciona la **Familia de máquinas virtuales** a utilizar. Por ejemplo, selecciona **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, que incluye la GPU *Standard_NC24ads_A100_v4*.
    - Selecciona **Request quota** del menú de navegación.

        ![Request quota.](../../../../translated_images/01-04-request-quota.7995c4c08ea51cd4952d34415bd7b7ea3c2d7dc219c7493afe436c75d5b891b1.es.png)

    - Dentro de la página de solicitud de cuota, introduce el **Nuevo límite de núcleos** que deseas usar. Por ejemplo, 24.
    - Dentro de la página de solicitud de cuota, selecciona **Submit** para solicitar la cuota de GPU.

> [!NOTE]
> Puedes seleccionar la GPU o CPU adecuada para tus necesidades consultando el documento [Tamaños de Máquinas Virtuales en Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Agregar asignación de roles

Para ajustar y desplegar tus modelos, primero debes crear una Identidad Administrada Asignada por el Usuario (UAI) y asignarle los permisos adecuados. Esta UAI se utilizará para la autenticación durante el despliegue.

#### Crear Identidad Administrada Asignada por el Usuario (UAI)

1. Escribe *managed identities* en la **barra de búsqueda** en la parte superior de la página del portal y selecciona **Managed Identities** de las opciones que aparecen.

    ![Type managed identities.](../../../../translated_images/01-05-type-managed-identities.02acd91a0a275a38cdc0c7be56a8db9a96b8f453764accb878e3e8707d6d8cfb.es.png)

1. Selecciona **+ Create**.

    ![Select create.](../../../../translated_images/01-06-select-create.5a0b10765271f872fb078968e8f3b5f6027136653d27e73e78cc4ced0687fa86.es.png)

1. Realiza las siguientes tareas:

    - Selecciona tu **Suscripción** de Azure.
    - Selecciona el **Grupo de recursos** a utilizar (crea uno nuevo si es necesario).
    - Selecciona la **Región** que deseas usar.
    - Introduce el **Nombre**. Debe ser un valor único.

1. Selecciona **Review + create**.

1. Selecciona **+ Create**.

#### Agregar asignación de rol de Colaborador a la Identidad Administrada

1. Navega al recurso de Identidad Administrada que creaste.

1. Selecciona **Azure role assignments** del menú lateral.

1. Selecciona **+Add role assignment** del menú de navegación.

1. Dentro de la página de asignación de roles, realiza las siguientes tareas:
    - Selecciona el **Ámbito** a **Resource group**.
    - Selecciona tu **Suscripción** de Azure.
    - Selecciona el **Grupo de recursos** a utilizar.
    - Selecciona el **Rol** a **Contributor**.

    ![Fill contributor role.](../../../../translated_images/01-07-fill-contributor-role.20a2b4f31e7495a9f8bc97a8e338ff2e7c2dcd6589d355ce4898f22f871f3d25.es.png)

1. Selecciona **Save**.

#### Agregar asignación de rol de Lector de Datos de Blob de Almacenamiento a la Identidad Administrada

1. Escribe *storage accounts* en la **barra de búsqueda** en la parte superior de la página del portal y selecciona **Storage accounts** de las opciones que aparecen.

    ![Type storage accounts.](../../../../translated_images/01-08-type-storage-accounts.5dc1776356053848154e9c73faacd69c96224626395cafd0d22c9f42ed523c55.es.png)

1. Selecciona la cuenta de almacenamiento asociada con el espacio de trabajo de Azure Machine Learning que creaste. Por ejemplo, *finetunephistorage*.

1. Realiza las siguientes tareas para navegar a la página de asignación de roles:

    - Navega a la cuenta de almacenamiento de Azure que creaste.
    - Selecciona **Access Control (IAM)** del menú lateral.
    - Selecciona **+ Add** del menú de navegación.
    - Selecciona **Add role assignment** del menú de navegación.

    ![Add role.](../../../../translated_images/01-09-add-role.0fcf57f69c109448b6ae259356c5ec5d1a3fd5d751a1d6a994f1c16db923dae0.es.png)

1. Dentro de la página de asignación de roles, realiza las siguientes tareas:

    - Dentro de la página de Rol, escribe *Storage Blob Data Reader* en la **barra de búsqueda** y selecciona **Storage Blob Data Reader** de las opciones que aparecen.
    - Dentro de la página de Rol, selecciona **Next**.
    - Dentro de la página de Miembros, selecciona **Assign access to** **Managed identity**.
    - Dentro de la página de Miembros, selecciona **+ Select members**.
    - Dentro de la página de selección de identidades administradas, selecciona tu **Suscripción** de Azure.
    - Dentro de la página de selección de identidades administradas, selecciona la **Identidad administrada** a **Manage Identity**.
    - Dentro de la página de selección de identidades administradas, selecciona la Identidad Administrada que creaste. Por ejemplo, *finetunephi-managedidentity*.
    - Dentro de la página de selección de identidades administradas, selecciona **Select**.

    ![Select managed identity.](../../../../translated_images/01-10-select-managed-identity.980c5177907f18065d2e28097b3629e3d66530902a39899aa4dd1214493a65d0.es.png)

1. Selecciona **Review + assign**.

#### Agregar asignación de rol AcrPull a la Identidad Administrada

1. Escribe *container registries* en la **barra de búsqueda** en la parte superior de la página del portal y selecciona **Container registries** de las opciones que aparecen.

    ![Type container registries.](../../../../translated_images/01-11-type-container-registries.2b96aa253440c5322c55865732a1b15e1b5e71d1d98a701012eaee389e4ee08c.es.png)

1. Selecciona el registro de contenedores asociado con el espacio de trabajo de Azure Machine Learning. Por ejemplo, *finetunephicontainerregistries*

1. Realiza las siguientes tareas para navegar a la página de asignación de roles:

    - Selecciona **Access Control (IAM)** del menú lateral.
    - Selecciona **+ Add** del menú de navegación.
    - Selecciona **Add role assignment** del menú de navegación.

1. Dentro de la página de asignación de roles, realiza las siguientes tareas:

    - Dentro de la página de Rol, escribe *AcrPull* en la **barra de búsqueda** y selecciona **AcrPull** de las opciones que aparecen.
    - Dentro de la página de Rol, selecciona **Next**.
    - Dentro de la página de Miembros, selecciona **Assign access to** **Managed identity**.
    - Dentro de la página de Miembros, selecciona **+ Select members**.
    - Dentro de la página de selección de identidades administradas, selecciona tu **Suscripción** de Azure.
    - Dentro de la página de selección de identidades administradas, selecciona la **Identidad administrada** a **Manage Identity**.
    - Dentro de la página de selección de identidades administradas, selecciona la Identidad Administrada que creaste. Por ejemplo, *finetunephi-managedidentity*.
    - Dentro de la página de selección de identidades administradas, selecciona **Select**.
    - Selecciona **Review + assign**.

### Configurar el proyecto

Ahora, crearás una carpeta para trabajar y configurarás un entorno virtual para desarrollar un programa que interactúe con los usuarios y utilice el historial de chat almacenado en Azure Cosmos DB para informar sus respuestas.

#### Crear una carpeta para trabajar dentro de ella

1. Abre una ventana de terminal y escribe el siguiente comando para crear una carpeta llamada *finetune-phi* en la ruta predeterminada.

    ```console
    mkdir finetune-phi
    ```

1. Escribe el siguiente comando en tu terminal para navegar a la carpeta *finetune-phi* que creaste.

    ```console
    cd finetune-phi
    ```

#### Crear un entorno virtual

1. Escribe el siguiente comando en tu terminal para crear un entorno virtual llamado *.venv*.

    ```console
    python -m venv .venv
    ```

1. Escribe el siguiente comando en tu terminal para activar el entorno virtual.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Si funcionó, deberías ver *(.venv)* antes del símbolo del sistema.

#### Instalar los paquetes requeridos

1. Escribe los siguientes comandos en tu terminal para instalar los paquetes requeridos.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Crear archivos de proyecto

En este ejercicio, crearás los archivos esenciales para nuestro proyecto. Estos archivos incluyen scripts para descargar el conjunto de datos, configurar el entorno de Azure Machine Learning, ajustar el modelo Phi-3 y desplegar el modelo ajustado. También crearás un archivo *conda.yml* para configurar el entorno de ajuste fino.

En este ejercicio, harás:

- Crear un archivo *download_dataset.py* para descargar el conjunto de datos.
- Crear un archivo *setup_ml.py* para configurar el entorno de Azure Machine Learning.
- Crear un archivo *fine_tune.py* en la carpeta *finetuning_dir* para ajustar el modelo Phi-3 usando el conjunto de datos.
- Crear un archivo *conda.yml* para configurar el entorno de ajuste fino.
- Crear un archivo *deploy_model.py* para desplegar el modelo ajustado.
- Crear un archivo *integrate_with_promptflow.py* para integrar el modelo ajustado y ejecutar el modelo usando Prompt flow.
- Crear un archivo flow.dag.yml para configurar la estructura del flujo de trabajo para Prompt flow.
- Crear un archivo *config.py* para ingresar la información de Azure.

> [!NOTE]
>
> Estructura completa de la carpeta:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Abre **Visual Studio Code**.

1. Selecciona **File** del menú.

1. Selecciona **Open Folder**.

1. Selecciona la carpeta *finetune-phi* que creaste, ubicada en *C:\Users\yourUserName\finetune-phi*.

    ![Open project folder.](../../../../translated_images/01-12-open-project-folder.f41fede45e248ad8a028f4db6f18a04eb4a2ebc4643e7f66e00f7239d539fdf9.es.png)

1. En el panel izquierdo de Visual Studio Code, haz clic derecho y selecciona **New File** para crear un nuevo archivo llamado *download_dataset.py*.

1. En el panel izquierdo de Visual Studio Code, haz clic derecho y selecciona **New File** para crear un nuevo archivo llamado *setup_ml.py*.

1. En el panel izquierdo de Visual Studio Code, haz clic derecho y selecciona **New File** para crear un nuevo archivo llamado *deploy_model.py*.

    ![Create new file.](../../../../translated_images/01-13-create-new-file.d684d1125b452778b5f8df8e1f3202e0a6d1c9ced6f6e8e4ce65da40df49c32c.es.png)

1. En el panel izquierdo de Visual Studio Code, haz clic derecho y selecciona **New Folder** para crear una nueva carpeta llamada *finetuning_dir*.

1. En la carpeta *finetuning_dir*, crea un nuevo archivo llamado *fine_tune.py*.

#### Crear y Configurar archivo *conda.yml*

1. En el panel izquierdo de Visual Studio Code, haz clic derecho y selecciona **New File** para crear un nuevo archivo llamado *conda.yml*.

1. Agrega el siguiente código al archivo *conda.yml* para configurar el entorno de ajuste fino para el modelo Phi-3.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure


Aviso legal: La traducción fue realizada a partir del original por un modelo de inteligencia artificial y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.