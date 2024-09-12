# Ollama C# Playground

Este laboratorio está diseñado para probar Phi-3 con ejemplos de C# directamente en GitHub Codespaces, como una forma sencilla para que cualquiera pueda probar SLMs (modelos de lenguaje pequeño) completamente en el navegador.

## Cómo crear el Codespace de C# + Ollama + Phi-3

1. Crea un nuevo Codespace usando el botón `Code` en la parte superior del repositorio. Selecciona la opción [+ New with options ...]
![Create Codespace with options](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.es.png)

1. En la página de opciones, selecciona la configuración llamada `Ollama with Phi-3 for C#`

![Select the option Ollama with Phi-3 for C#, to create the CodeSpace](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.es.png)

1. Una vez que el Codespace esté cargado, debería tener [ollama](https://ollama.com/) preinstalado, el último modelo Phi-3 descargado y [.NET 8](https://dotnet.microsoft.com/download) instalado.

1. (Opcional) Usando la terminal del Codespace, pide a Ollama que ejecute el modelo [phi3](https://ollama.com/library/phi3):

    ```shell
    ollama run phi3
    ```

4. Puedes enviar un mensaje a ese modelo desde el prompt.

    ```shell
    >>> Write a joke about kittens
    ```

5. Después de varios segundos, deberías ver una respuesta del modelo.

    ![run ollama and ask for a joke](./20ollamarunphi.gif)

1. Para aprender sobre diferentes técnicas utilizadas con modelos de lenguaje, revisa los proyectos de muestra en la carpeta `.\src`:

| Proyecto | Descripción |
|---------|-------------|
| Sample01  | Este es un proyecto de muestra que utiliza el modelo Phi-3 alojado en ollama para responder una pregunta.  |
| Sample02  | Este es un proyecto de muestra que implementa un chat de consola usando Semantic Kernel. |
| [Sample03](./src/Sample03/readme.md)  | Este es un proyecto de muestra que implementa un RAG usando embeddings locales y Semantic Kernel. Revisa los detalles del RAG local [aquí](./src/Sample03/readme.md) |

## Cómo ejecutar un ejemplo

1. Abre una terminal y navega al proyecto deseado. Por ejemplo, ejecutemos `Sample02`, el chat de consola.

    ```bash
    cd .\src\Sample02\
    ```

1. Ejecuta el proyecto con el comando

    ```bash
    dotnet run
    ```

1. El proyecto `Sample02` define un mensaje de sistema personalizado:

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

    ```

1. Así que cuando el usuario hace una pregunta, como `What is the capital of Italy?`, el chat responde usando el modelo local.
   
    La salida es similar a esta:

    ![Chat running demo](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.es.png)

## Tutoriales en Video

Si deseas aprender más sobre cómo usar Codespaces con Ollama en un repositorio de GitHub, revisa el siguiente video de 3 minutos:

[![Watch the video](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.es.jpg)](https://youtu.be/HmKpHErUEHM)

        Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
        Por favor, revise el resultado y haga las correcciones necesarias.