# Evaluar el Modelo Phi-3 / Phi-3.5 Ajustado en Azure AI Studio Enfocado en los Principios de IA Responsable de Microsoft

Este ejemplo de extremo a extremo (E2E) se basa en la guía "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Studio Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" de la comunidad técnica de Microsoft.

## Descripción General

### ¿Cómo puedes evaluar la seguridad y el rendimiento de un modelo Phi-3 / Phi-3.5 ajustado en Azure AI Studio?

Ajustar un modelo puede a veces llevar a respuestas no deseadas o no intencionadas. Para asegurar que el modelo siga siendo seguro y efectivo, es importante evaluar su potencial para generar contenido dañino y su capacidad para producir respuestas precisas, relevantes y coherentes. En este tutorial, aprenderás cómo evaluar la seguridad y el rendimiento de un modelo Phi-3 / Phi-3.5 ajustado integrado con Prompt flow en Azure AI Studio.

Aquí está el proceso de evaluación de Azure AI Studio.

![Arquitectura del tutorial.](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.es.png)

*Fuente de la imagen: [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para información más detallada y explorar recursos adicionales sobre Phi-3 / Phi-3.5, por favor visita el [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Requisitos Previos

- [Python](https://www.python.org/downloads)
- [Suscripción a Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Phi-3 / Phi-3.5 ajustado

### Tabla de Contenidos

1. [**Escenario 1: Introducción a la evaluación de Prompt flow en Azure AI Studio**](../../../../md/06.E2ESamples)

    - [Introducción a la evaluación de seguridad](../../../../md/06.E2ESamples)
    - [Introducción a la evaluación de rendimiento](../../../../md/06.E2ESamples)

1. [**Escenario 2: Evaluación del modelo Phi-3 / Phi-3.5 en Azure AI Studio**](../../../../md/06.E2ESamples)

    - [Antes de comenzar](../../../../md/06.E2ESamples)
    - [Desplegar Azure OpenAI para evaluar el modelo Phi-3 / Phi-3.5](../../../../md/06.E2ESamples)
    - [Evaluar el modelo Phi-3 / Phi-3.5 ajustado usando la evaluación de Prompt flow en Azure AI Studio](../../../../md/06.E2ESamples)

1. [¡Felicitaciones!](../../../../md/06.E2ESamples)

## **Escenario 1: Introducción a la evaluación de Prompt flow en Azure AI Studio**

### Introducción a la evaluación de seguridad

Para asegurar que tu modelo de IA sea ético y seguro, es crucial evaluarlo según los Principios de IA Responsable de Microsoft. En Azure AI Studio, las evaluaciones de seguridad te permiten evaluar la vulnerabilidad de tu modelo a ataques de jailbreak y su potencial para generar contenido dañino, lo cual está directamente alineado con estos principios.

![Evaluación de seguridad.](../../../../translated_images/safety-evaluation.5ad906c4618e4c8736fdeeff54a52dac8ae6d0756b15824e430177fba7b6a8b4.es.png)

*Fuente de la imagen: [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principios de IA Responsable de Microsoft

Antes de comenzar con los pasos técnicos, es esencial entender los Principios de IA Responsable de Microsoft, un marco ético diseñado para guiar el desarrollo, despliegue y operación responsable de sistemas de IA. Estos principios guían el diseño, desarrollo y despliegue responsable de sistemas de IA, asegurando que las tecnologías de IA se construyan de manera justa, transparente e inclusiva. Estos principios son la base para evaluar la seguridad de los modelos de IA.

Los Principios de IA Responsable de Microsoft incluyen:

- **Equidad e Inclusión**: Los sistemas de IA deben tratar a todos de manera justa y evitar afectar de manera diferente a grupos de personas en situaciones similares. Por ejemplo, cuando los sistemas de IA brindan orientación sobre tratamientos médicos, solicitudes de préstamos o empleo, deben hacer las mismas recomendaciones a todos los que tengan síntomas, circunstancias financieras o calificaciones profesionales similares.

- **Fiabilidad y Seguridad**: Para generar confianza, es crítico que los sistemas de IA operen de manera fiable, segura y consistente. Estos sistemas deben poder operar como fueron diseñados originalmente, responder de manera segura a condiciones no anticipadas y resistir manipulaciones dañinas. Su comportamiento y la variedad de condiciones que pueden manejar reflejan el rango de situaciones y circunstancias que los desarrolladores anticiparon durante el diseño y las pruebas.

- **Transparencia**: Cuando los sistemas de IA ayudan a informar decisiones que tienen un gran impacto en la vida de las personas, es crítico que las personas entiendan cómo se tomaron esas decisiones. Por ejemplo, un banco podría usar un sistema de IA para decidir si una persona es digna de crédito. Una empresa podría usar un sistema de IA para determinar los candidatos más calificados para contratar.

- **Privacidad y Seguridad**: A medida que la IA se vuelve más prevalente, proteger la privacidad y asegurar la información personal y empresarial se vuelve más importante y complejo. Con la IA, la privacidad y la seguridad de los datos requieren una atención cercana porque el acceso a los datos es esencial para que los sistemas de IA hagan predicciones y decisiones precisas e informadas sobre las personas.

- **Responsabilidad**: Las personas que diseñan y despliegan sistemas de IA deben ser responsables de cómo operan sus sistemas. Las organizaciones deben basarse en estándares de la industria para desarrollar normas de responsabilidad. Estas normas pueden asegurar que los sistemas de IA no sean la autoridad final en ninguna decisión que afecte la vida de las personas. También pueden asegurar que los humanos mantengan un control significativo sobre sistemas de IA altamente autónomos.

![Centro de relleno.](../../../../translated_images/responsibleai2.ae6f996d95dcc46b3b3087c0e4f4f4b74c64e961083009ecca7a0a3998b3f716.es.png)

*Fuente de la imagen: [¿Qué es la IA Responsable?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para aprender más sobre los Principios de IA Responsable de Microsoft, visita [¿Qué es la IA Responsable?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de seguridad

En este tutorial, evaluarás la seguridad del modelo Phi-3 ajustado usando las métricas de seguridad de Azure AI Studio. Estas métricas te ayudan a evaluar el potencial del modelo para generar contenido dañino y su vulnerabilidad a ataques de jailbreak. Las métricas de seguridad incluyen:

- **Contenido relacionado con autolesiones**: Evalúa si el modelo tiene tendencia a producir contenido relacionado con autolesiones.
- **Contenido odioso e injusto**: Evalúa si el modelo tiene tendencia a producir contenido odioso o injusto.
- **Contenido violento**: Evalúa si el modelo tiene tendencia a producir contenido violento.
- **Contenido sexual**: Evalúa si el modelo tiene tendencia a producir contenido sexual inapropiado.

Evaluar estos aspectos asegura que el modelo de IA no produzca contenido dañino u ofensivo, alineándolo con los valores sociales y estándares regulatorios.

![Evaluar basado en seguridad.](../../../../translated_images/evaluate-based-on-safety.63d79ac01570713002d5d858bfbb8f4d7295557ae8829d0c379485d67a3fcd1c.es.png)

### Introducción a la evaluación de rendimiento

Para asegurar que tu modelo de IA está funcionando como se espera, es importante evaluar su rendimiento contra métricas de rendimiento. En Azure AI Studio, las evaluaciones de rendimiento te permiten evaluar la efectividad de tu modelo en generar respuestas precisas, relevantes y coherentes.

![Evaluación de rendimiento.](../../../../translated_images/performance-evaluation.259c44647c74a80761cdcbaab2202142f99a5a0d28326c8a1eb6dc2765f5ef77.es.png)

*Fuente de la imagen: [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de rendimiento

En este tutorial, evaluarás el rendimiento del modelo Phi-3 / Phi-3.5 ajustado usando las métricas de rendimiento de Azure AI Studio. Estas métricas te ayudan a evaluar la efectividad del modelo en generar respuestas precisas, relevantes y coherentes. Las métricas de rendimiento incluyen:

- **Fundamentación**: Evalúa qué tan bien se alinean las respuestas generadas con la información de la fuente de entrada.
- **Relevancia**: Evalúa la pertinencia de las respuestas generadas con respecto a las preguntas dadas.
- **Coherencia**: Evalúa qué tan fluido es el texto generado, si se lee de manera natural y se asemeja al lenguaje humano.
- **Fluidez**: Evalúa la competencia lingüística del texto generado.
- **Similitud GPT**: Compara la respuesta generada con la verdad de base para medir la similitud.
- **Puntuación F1**: Calcula la proporción de palabras compartidas entre la respuesta generada y los datos fuente.

Estas métricas te ayudan a evaluar la efectividad del modelo en generar respuestas precisas, relevantes y coherentes.

![Evaluar basado en rendimiento.](../../../../translated_images/evaluate-based-on-performance.33ccf1c52f210af8e76d9cab863716d3f67db3d765254371a30136cc8f852b37.es.png)

## **Escenario 2: Evaluación del modelo Phi-3 / Phi-3.5 en Azure AI Studio**

### Antes de comenzar

Este tutorial es una continuación de las publicaciones anteriores en el blog, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" y "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." En estas publicaciones, recorrimos el proceso de ajuste fino de un modelo Phi-3 / Phi-3.5 en Azure AI Studio e integrarlo con Prompt flow.

En este tutorial, desplegarás un modelo de Azure OpenAI como evaluador en Azure AI Studio y lo usarás para evaluar tu modelo Phi-3 / Phi-3.5 ajustado.

Antes de comenzar este tutorial, asegúrate de tener los siguientes requisitos previos, como se describe en los tutoriales anteriores:

1. Un conjunto de datos preparado para evaluar el modelo Phi-3 / Phi-3.5 ajustado.
1. Un modelo Phi-3 / Phi-3.5 que ha sido ajustado y desplegado en Azure Machine Learning.
1. Un Prompt flow integrado con tu modelo Phi-3 / Phi-3.5 ajustado en Azure AI Studio.

> [!NOTE]
> Usarás el archivo *test_data.jsonl*, ubicado en la carpeta de datos del conjunto de datos **ULTRACHAT_200k** descargado en las publicaciones anteriores del blog, como el conjunto de datos para evaluar el modelo Phi-3 / Phi-3.5 ajustado.

#### Integrar el modelo Phi-3 / Phi-3.5 personalizado con Prompt flow en Azure AI Studio (Enfoque de código primero)

> [!NOTE]
> Si seguiste el enfoque de bajo código descrito en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", puedes omitir este ejercicio y proceder al siguiente.
> Sin embargo, si seguiste el enfoque de código primero descrito en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para ajustar y desplegar tu modelo Phi-3 / Phi-3.5, el proceso de conectar tu modelo a Prompt flow es ligeramente diferente. Aprenderás este proceso en este ejercicio.

Para proceder, necesitas integrar tu modelo Phi-3 / Phi-3.5 ajustado en Prompt flow en Azure AI Studio.

#### Crear Hub en Azure AI Studio

Necesitas crear un Hub antes de crear el Proyecto. Un Hub actúa como un Grupo de Recursos, permitiéndote organizar y gestionar múltiples Proyectos dentro de Azure AI Studio.

1. Inicia sesión en [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecciona **Todos los hubs** desde la pestaña del lado izquierdo.

1. Selecciona **+ Nuevo hub** desde el menú de navegación.

    ![Crear hub.](../../../../translated_images/create-hub.8d452311ef5b4b9188df89f7cff7797c67ec8f391282235b19b988e167f3e920.es.png)

1. Realiza las siguientes tareas:

    - Ingresa el **Nombre del hub**. Debe ser un valor único.
    - Selecciona tu **Suscripción** de Azure.
    - Selecciona el **Grupo de recursos** a usar (crea uno nuevo si es necesario).
    - Selecciona la **Ubicación** que deseas usar.
    - Selecciona el **Conectar servicios de Azure AI** a usar (crea uno nuevo si es necesario).
    - Selecciona **Conectar Azure AI Search** para **Omitir la conexión**.
![Llenar hub.](../../../../translated_images/fill-hub.8b19834866ef631a2fd031584c77b78c0438a385bdee8f981361b14bbc46f5e1.es.png)

1. Selecciona **Next**.

#### Crear Proyecto en Azure AI Studio

1. En el Hub que creaste, selecciona **All projects** desde la pestaña lateral izquierda.

1. Selecciona **+ New project** desde el menú de navegación.

    ![Seleccionar nuevo proyecto.](../../../../translated_images/select-new-project.1a925c25ca3bc47b2b16feefc5a76f5c29e211ac464ea5c3cdfe389868d87da7.es.png)

1. Ingresa **Project name**. Debe ser un valor único.

    ![Crear proyecto.](../../../../translated_images/create-project.ff239752937343b4cb38156740ebda92bc1d8b16299183c245f3e3661432db31.es.png)

1. Selecciona **Create a project**.

#### Agregar una conexión personalizada para el modelo Phi-3 / Phi-3.5 ajustado

Para integrar tu modelo personalizado Phi-3 / Phi-3.5 con Prompt flow, necesitas guardar el endpoint y la clave del modelo en una conexión personalizada. Esta configuración asegura el acceso a tu modelo personalizado Phi-3 / Phi-3.5 en Prompt flow.

#### Configurar la clave api y el uri del endpoint del modelo Phi-3 / Phi-3.5 ajustado

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navega al espacio de trabajo de Azure Machine Learning que creaste.

1. Selecciona **Endpoints** desde la pestaña lateral izquierda.

    ![Seleccionar endpoints.](../../../../translated_images/select-endpoints.3027748aed379990fd8ee9bf27f70ff11918955bb1a10269e2f34f6931b26955.es.png)

1. Selecciona el endpoint que creaste.

    ![Seleccionar endpoints.](../../../../translated_images/select-endpoint-created.560a5cadfbbb58b66abb2fb61b4450b22060371910af1b45c358bde548234ebc.es.png)

1. Selecciona **Consume** desde el menú de navegación.

1. Copia tu **REST endpoint** y **Primary key**.

    ![Copiar clave api y uri del endpoint.](../../../../translated_images/copy-endpoint-key.56de01742992f2402d57139849304b5b049fb468fb38abc7982b7dfc311daf9e.es.png)

#### Agregar la Conexión Personalizada

1. Visita [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navega al proyecto de Azure AI Studio que creaste.

1. En el Proyecto que creaste, selecciona **Settings** desde la pestaña lateral izquierda.

1. Selecciona **+ New connection**.

    ![Seleccionar nueva conexión.](../../../../translated_images/select-new-connection.a1ff72172d07054308a3fc7b7b86e25e9ca1c879f0a382b9a2be2c80bb2ebcc5.es.png)

1. Selecciona **Custom keys** desde el menú de navegación.

    ![Seleccionar claves personalizadas.](../../../../translated_images/select-custom-keys.b17eb3b15eae28126a4eeda8f53396b9a6f773745f2dd68c464252575a77b5d3.es.png)

1. Realiza las siguientes tareas:

    - Selecciona **+ Add key value pairs**.
    - Para el nombre de la clave, ingresa **endpoint** y pega el endpoint que copiaste de Azure ML Studio en el campo de valor.
    - Selecciona **+ Add key value pairs** nuevamente.
    - Para el nombre de la clave, ingresa **key** y pega la clave que copiaste de Azure ML Studio en el campo de valor.
    - Después de agregar las claves, selecciona **is secret** para evitar que la clave sea expuesta.

    ![Agregar conexión.](../../../../translated_images/add-connection.c01c94851c9eece708711456a4853355b9532b0cb1f970e24f165e7e1d6c0a03.es.png)

1. Selecciona **Add connection**.

#### Crear Prompt flow

Has agregado una conexión personalizada en Azure AI Studio. Ahora, vamos a crear un Prompt flow usando los siguientes pasos. Luego, conectarás este Prompt flow a la conexión personalizada para usar el modelo ajustado dentro del Prompt flow.

1. Navega al proyecto de Azure AI Studio que creaste.

1. Selecciona **Prompt flow** desde la pestaña lateral izquierda.

1. Selecciona **+ Create** desde el menú de navegación.

    ![Seleccionar Promptflow.](../../../../translated_images/select-promptflow.766ad0f2403e2bd6f374bee40a607321e3e2b416629063acf3204a983fb4bcaa.es.png)

1. Selecciona **Chat flow** desde el menú de navegación.

    ![Seleccionar chat flow.](../../../../translated_images/select-flow-type.0e18b84032da1200e48a702e5140c1775b1eb6de9cf222c6a8007840fa278e97.es.png)

1. Ingresa **Folder name** a utilizar.

    ![Seleccionar chat flow.](../../../../translated_images/enter-name.43919b211b1e8e0184536dc09184190e7e8c56bf960d4b5601443efddc757db4.es.png)

1. Selecciona **Create**.

#### Configurar Prompt flow para chatear con tu modelo personalizado Phi-3 / Phi-3.5

Necesitas integrar el modelo ajustado Phi-3 / Phi-3.5 en un Prompt flow. Sin embargo, el Prompt flow existente proporcionado no está diseñado para este propósito. Por lo tanto, debes rediseñar el Prompt flow para permitir la integración del modelo personalizado.

1. En el Prompt flow, realiza las siguientes tareas para reconstruir el flujo existente:

    - Selecciona **Raw file mode**.
    - Elimina todo el código existente en el archivo *flow.dag.yml*.
    - Agrega el siguiente código a *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Selecciona **Save**.

    ![Seleccionar modo de archivo sin procesar.](../../../../translated_images/select-raw-file-mode.2084d7f905df40f69cc5ebe48efa2318e92fd069358625a92993ef614f189d84.es.png)

1. Agrega el siguiente código a *integrate_with_promptflow.py* para usar el modelo personalizado Phi-3 / Phi-3.5 en Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Pegar código de prompt flow.](../../../../translated_images/paste-promptflow-code.667abbdf848fd03153828c0aa70dde58a851e09b1ba4c69bc6f686d2005656aa.es.png)

> [!NOTE]
> Para más información detallada sobre el uso de Prompt flow en Azure AI Studio, puedes referirte a [Prompt flow in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecciona **Chat input**, **Chat output** para habilitar el chat con tu modelo.

    ![Seleccionar Entrada Salida.](../../../../translated_images/select-input-output.d4803eae144b03579db4a23def15c68bb50527017cdc4aa9f72c8679588a0f4c.es.png)

1. Ahora estás listo para chatear con tu modelo personalizado Phi-3 / Phi-3.5. En el próximo ejercicio, aprenderás cómo iniciar Prompt flow y usarlo para chatear con tu modelo ajustado Phi-3 / Phi-3.5.

> [!NOTE]
>
> El flujo reconstruido debería verse como la imagen a continuación:
>
> ![Ejemplo de flujo](../../../../translated_images/graph-example.5b309021deca5b503270e50888da4784256730c210ed757f799f9bff0a12bb19.es.png)
>

#### Iniciar Prompt flow

1. Selecciona **Start compute sessions** para iniciar Prompt flow.

    ![Iniciar sesión de cómputo.](../../../../translated_images/start-compute-session.75300f481218ca70eae80304255956c71a9b6be31a18b43264118c19c0b1a016.es.png)

1. Selecciona **Validate and parse input** para renovar parámetros.

    ![Validar entrada.](../../../../translated_images/validate-input.a6c90e55ce6117ea44e2acd88b8a20bc31136bf6c574b0a6c9217867201025c9.es.png)

1. Selecciona el **Value** de la **connection** a la conexión personalizada que creaste. Por ejemplo, *connection*.

    ![Conexión.](../../../../translated_images/select-connection.6573a1269969a14c83c397334051f71057ec9a243e95ea1b849483bd7481ff6a.es.png)

#### Chatear con tu modelo personalizado Phi-3 / Phi-3.5

1. Selecciona **Chat**.

    ![Seleccionar chat.](../../../../translated_images/select-chat.25eab3d62b0a6c4960f0ae1b5d6efd6b5847cc20d468fd28cb1f0d656936cc22.es.png)

1. Aquí tienes un ejemplo de los resultados: Ahora puedes chatear con tu modelo personalizado Phi-3 / Phi-3.5. Se recomienda hacer preguntas basadas en los datos utilizados para el ajuste fino.

    ![Chatear con prompt flow.](../../../../translated_images/chat-with-promptflow.105b5a3b70ff64725c1d4cd2e9c6b55301219c7d68c9bec59106a49fb8bf40f2.es.png)

### Desplegar Azure OpenAI para evaluar el modelo Phi-3 / Phi-3.5

Para evaluar el modelo Phi-3 / Phi-3.5 en Azure AI Studio, necesitas desplegar un modelo de Azure OpenAI. Este modelo se utilizará para evaluar el rendimiento del modelo Phi-3 / Phi-3.5.

#### Desplegar Azure OpenAI

1. Inicia sesión en [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navega al proyecto de Azure AI Studio que creaste.

    ![Seleccionar Proyecto.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.es.png)

1. En el Proyecto que creaste, selecciona **Deployments** desde la pestaña lateral izquierda.

1. Selecciona **+ Deploy model** desde el menú de navegación.

1. Selecciona **Deploy base model**.

    ![Seleccionar Despliegues.](../../../../translated_images/deploy-openai-model.f09a74e1f976b52f85fdef711372452b9faed270e9d015887e09f44b41bbc163.es.png)

1. Selecciona el modelo de Azure OpenAI que te gustaría usar. Por ejemplo, **gpt-4o**.

    ![Seleccionar modelo de Azure OpenAI que te gustaría usar.](../../../../translated_images/select-openai-model.29fbbd802d6a9aa941097ae80a0ffe256239e636190b7c1e49f28d3d66143a0d.es.png)

1. Selecciona **Confirm**.

### Evaluar el modelo Phi-3 / Phi-3.5 ajustado usando la evaluación de Prompt flow de Azure AI Studio

### Iniciar una nueva evaluación

1. Visita [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navega al proyecto de Azure AI Studio que creaste.

    ![Seleccionar Proyecto.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.es.png)

1. En el Proyecto que creaste, selecciona **Evaluation** desde la pestaña lateral izquierda.

1. Selecciona **+ New evaluation** desde el menú de navegación.
![Select evaluation.](../../../../translated_images/select-evaluation.7d8a8228ebdf3f3b46bf5cf6ab5bdcb4565132ba6b28126d9757aaf3abade725.es.png)

1. Selecciona **Evaluación de Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../translated_images/promptflow-evaluation.ff4265fafd69c7f5ded1b5275cacecbd5f3272a6358c1f784f62e64bcb9e949f.es.png)

1. Realiza las siguientes tareas:

    - Ingresa el nombre de la evaluación. Debe ser un valor único.
    - Selecciona **Pregunta y respuesta sin contexto** como el tipo de tarea. Esto se debe a que el dataset **ULTRACHAT_200k** usado en este tutorial no contiene contexto.
    - Selecciona el prompt flow que deseas evaluar.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting1.d3b22a8343f8265807e2b507fa7eec9d86a9cefd4a67bc39ba2022d572f13e1d.es.png)

1. Selecciona **Siguiente**.

1. Realiza las siguientes tareas:

    - Selecciona **Añadir tu dataset** para subir el dataset. Por ejemplo, puedes subir el archivo del dataset de prueba, como *test_data.json1*, que se incluye al descargar el dataset **ULTRACHAT_200k**.
    - Selecciona la **Columna del dataset** apropiada que coincida con tu dataset. Por ejemplo, si estás usando el dataset **ULTRACHAT_200k**, selecciona **${data.prompt}** como la columna del dataset.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting2.32749fa51bc4fdb32f75dfd09b96bee74454c51ce3084bcc6f95b7286177a657.es.png)

1. Selecciona **Siguiente**.

1. Realiza las siguientes tareas para configurar las métricas de rendimiento y calidad:

    - Selecciona las métricas de rendimiento y calidad que deseas usar.
    - Selecciona el modelo de Azure OpenAI que creaste para la evaluación. Por ejemplo, selecciona **gpt-4o**.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-1.db76b89d94911c84ece6ce793593a4289278e1b24520e38ecd8372f4b9dc1167.es.png)

1. Realiza las siguientes tareas para configurar las métricas de riesgo y seguridad:

    - Selecciona las métricas de riesgo y seguridad que deseas usar.
    - Selecciona el umbral para calcular la tasa de defectos que deseas usar. Por ejemplo, selecciona **Medio**.
    - Para **pregunta**, selecciona **Fuente de datos** a **{$data.prompt}**.
    - Para **respuesta**, selecciona **Fuente de datos** a **{$run.outputs.answer}**.
    - Para **verdad_terreno**, selecciona **Fuente de datos** a **{$data.message}**.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-2.eb9892654970af140ebb74fcc99e06dad7eca3d38365e3f2cbe90101392f41ee.es.png)

1. Selecciona **Siguiente**.

1. Selecciona **Enviar** para iniciar la evaluación.

1. La evaluación tomará algún tiempo en completarse. Puedes monitorear el progreso en la pestaña **Evaluación**.

### Revisa los Resultados de la Evaluación

> [!NOTE]
> Los resultados presentados a continuación están destinados a ilustrar el proceso de evaluación. En este tutorial, hemos usado un modelo afinado en un dataset relativamente pequeño, lo que puede llevar a resultados subóptimos. Los resultados reales pueden variar significativamente dependiendo del tamaño, calidad y diversidad del dataset usado, así como de la configuración específica del modelo.

Una vez que la evaluación esté completa, puedes revisar los resultados tanto de las métricas de rendimiento como de seguridad.

1. Métricas de rendimiento y calidad:

    - Evalúa la efectividad del modelo en generar respuestas coherentes, fluidas y relevantes.

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu.5b6e301e6d1af6044819f4d3c8443cbc44fb7db54ebce208b4288744ca25e6e8.es.png)

1. Métricas de riesgo y seguridad:

    - Asegúrate de que las salidas del modelo sean seguras y se alineen con los Principios de IA Responsable, evitando cualquier contenido dañino u ofensivo.

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu-2.d867d40ee9dfebc40c878288b8dc8727721a2fec995904b1475c513f0960e8e0.es.png)

1. Puedes desplazarte hacia abajo para ver **Resultados detallados de las métricas**.

    ![Evaluation result.](../../../../translated_images/detailed-metrics-result.6cf00c2b6026bb500ff758ee3047c20f600aab3878c892897e99e2e3a88fb002.es.png)

1. Al evaluar tu modelo Phi-3 / Phi-3.5 personalizado contra métricas tanto de rendimiento como de seguridad, puedes confirmar que el modelo no solo es efectivo, sino que también cumple con prácticas de IA responsable, haciéndolo listo para su despliegue en el mundo real.

## ¡Felicidades!

### Has completado este tutorial

Has evaluado con éxito el modelo Phi-3 afinado e integrado con Prompt flow en Azure AI Studio. Este es un paso importante para asegurar que tus modelos de IA no solo funcionen bien, sino que también cumplan con los principios de IA Responsable de Microsoft para ayudarte a construir aplicaciones de IA confiables y seguras.

![Architecture.](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.es.png)

## Limpieza de Recursos de Azure

Limpia tus recursos de Azure para evitar cargos adicionales en tu cuenta. Ve al portal de Azure y elimina los siguientes recursos:

- El recurso de Azure Machine Learning.
- El punto de conexión del modelo de Azure Machine Learning.
- El recurso del Proyecto de Azure AI Studio.
- El recurso de Prompt flow de Azure AI Studio.

### Próximos Pasos

#### Documentación

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [Evaluar sistemas de IA usando el panel de IA Responsable](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluación y monitoreo de métricas para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentación de Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentación de Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenido de Capacitación

- [Introducción al Enfoque de IA Responsable de Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introducción a Azure AI Studio](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referencia

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [¿Qué es la IA Responsable?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anunciando nuevas herramientas en Azure AI para ayudarte a construir aplicaciones de IA generativa más seguras y confiables](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.