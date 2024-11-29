# Escenario Completo de RAG Local Usando Phi-3, SemanticKernel y TextMemory

## Introducción

Bienvenido al repositorio para el escenario completo de RAG local usando Phi-3, SemanticKernel y TextMemory. Este proyecto demuestra el poder de Phi-3, un innovador Modelo de Lenguaje Pequeño (SLM) que está redefiniendo las capacidades de la IA para desarrolladores y negocios.

## Descripción del Escenario

El escenario de demostración está diseñado para responder a la pregunta, "¿Cuál es el superhéroe favorito de Bruno?" usando dos enfoques diferentes:

1. Preguntando directamente al modelo Phi-3.
2. Añadiendo un objeto de memoria semántica con datos de fanáticos cargados y luego haciendo la pregunta.

## Importancia del Escenario Completo

Phi-3 representa un avance significativo en los Modelos de Lenguaje Pequeño, ofreciendo una combinación única de rendimiento y eficiencia. Es capaz de manejar escenarios completos de manera independiente, lo que simplifica el proceso de desarrollo y reduce las complejidades de integración.

## Explicación del Código

La aplicación de consola demuestra el uso de un modelo local alojado en Ollama y memoria semántica para búsqueda. El programa utiliza varias bibliotecas externas para inyección de dependencias, configuración y funcionalidades de kernel y memoria semántica.

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

1. Primero, la pregunta se hace directamente al Modelo Phi-3. Luego, el programa carga la siguiente información en una Memoria de Texto, y vuelve a hacer la pregunta.

    ```csharp

    // get the embeddings generator service
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // add facts to the collection
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Gisela's favourite super hero is Batman");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "The last super hero movie watched by Gisela was Guardians of the Galaxy Vol 3");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Bruno's favourite super hero is Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "The last super hero movie watched by Bruno was Aquaman II");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno don't like the super hero movie: Eternals");    
    ```

1. Una vez que la memoria de texto está lista, se carga en el kernel como un plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Aquí está la aplicación de consola de demostración ejecutándose en un Codespace:

    ![Aplicación de consola de demostración ejecutándose en un Codespace](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## Referencias

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automatizada por IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No nos hacemos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.