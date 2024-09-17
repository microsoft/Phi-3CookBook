# Escenario Completo de RAG Local Usando Phi-3, SemanticKernel, y TextMemory

## Introducción

Bienvenido al repositorio para el escenario completo de RAG local usando Phi-3, SemanticKernel, y TextMemory. Este proyecto demuestra el poder de Phi-3, un modelo de lenguaje pequeño (SLM) innovador que está redefiniendo las capacidades de IA para desarrolladores y empresas.

## Descripción del Escenario

El escenario de demostración está diseñado para responder a la pregunta, "¿Cuál es el superhéroe favorito de Bruno?" usando dos enfoques diferentes:

1. Preguntando directamente al modelo Phi-3.
2. Añadiendo un objeto de memoria semántica con datos de fan cargados y luego haciendo la pregunta.

## Importancia del Escenario Completo

Phi-3 representa un salto significativo en los modelos de lenguaje pequeños, ofreciendo una combinación única de rendimiento y eficiencia. Es capaz de manejar escenarios completos de manera independiente, lo que simplifica el proceso de desarrollo y reduce las complejidades de integración.

## Explicación del Código

La aplicación de consola demuestra el uso de un modelo local alojado en Ollama y memoria semántica para búsqueda. El programa utiliza varias bibliotecas externas para la inyección de dependencias, configuración y funcionalidades de kernel y memoria semántica.

## Cómo Probar

1. Abre una terminal y navega al proyecto actual.

    ```bash
    cd .\src\Sample03\
    ```

1. Ejecuta el proyecto con el comando

    ```bash
    dotnet run
    ```

1. El proyecto `Sample03`, responde a la siguiente pregunta:

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. Primero, la pregunta se hace directamente al Modelo Phi-3. Luego, el programa carga la siguiente información en una Memoria de Texto y hace la pregunta nuevamente.

    ```csharp

    // obtener el servicio generador de embeddings
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // añadir datos a la colección
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "El superhéroe favorito de Gisela es Batman");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "La última película de superhéroes que vio Gisela fue Guardianes de la Galaxia Vol 3");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "El superhéroe favorito de Bruno es Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "La última película de superhéroes que vio Bruno fue Aquaman II");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "A Bruno no le gustó la película de superhéroes: Eternals");    
    ```

1. Una vez que la memoria de texto está lista, se carga en el kernel como un plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Importar el plugin de memoria de texto en el Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Aquí está la aplicación de consola de demostración ejecutándose en un Codespace:

    ![Aplicación de consola de demostración ejecutándose en un Codespace](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## Referencias

- [Blog de Microsoft sobre Phi-3](https://aka.ms/phi3blog-april)
- [Informe Técnico de Phi-3](https://aka.ms/phi3-tech-report)
- [Cookbook de Phi-3](https://aka.ms/Phi-3CookBook)
- [IA Generativa para principiantes](https://github.com/microsoft/generative-ai-for-beginners)
- [Repositorio principal de Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Componentes Inteligentes - Embeddings Locales](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.