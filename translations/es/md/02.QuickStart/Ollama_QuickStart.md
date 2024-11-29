# **Usando Phi-3 en Ollama**

[Ollama](https://ollama.com) permite que más personas desplieguen directamente LLM o SLM de código abierto a través de scripts simples, y también puede construir APIs para ayudar en escenarios de aplicaciones locales de Copilot.

## **1. Instalación**

Ollama es compatible con Windows, macOS y Linux. Puedes instalar Ollama a través de este enlace ([https://ollama.com/download](https://ollama.com/download)). Después de una instalación exitosa, puedes usar directamente el script de Ollama para llamar a Phi-3 a través de una ventana de terminal. Puedes ver todas las [bibliotecas disponibles en Ollama](https://ollama.com/library). Si abres este repositorio en un Codespace, ya tendrá Ollama instalado.

```bash

ollama run phi3

```

> [!NOTE]
> El modelo se descargará primero cuando lo ejecutes por primera vez. Por supuesto, también puedes especificar directamente el modelo Phi-3 descargado. Tomamos WSL como ejemplo para ejecutar el comando. Después de que el modelo se descargue con éxito, puedes interactuar directamente en el terminal.

![run](../../../../translated_images/ollama_run.302aa6484e50a7f8f09b40c787dc22eea10525cac6287c92825c8fc80c012c48.es.png)

## **2. Llamar a la API de phi-3 desde Ollama**

Si deseas llamar a la API de Phi-3 generada por Ollama, puedes usar este comando en el terminal para iniciar el servidor Ollama.

```bash

ollama serve

```

> [!NOTE]
> Si estás ejecutando MacOS o Linux, ten en cuenta que puedes encontrarte con el siguiente error **"Error: listen tcp 127.0.0.1:11434: bind: address already in use"** Puedes obtener este error al ejecutar el comando. Puedes ignorar ese error, ya que típicamente indica que el servidor ya está en funcionamiento, o puedes detener y reiniciar Ollama:

**macOS**

```bash

brew services restart ollama

```

**Linux**

```bash

sudo systemctl stop ollama

```

Ollama soporta dos API: generate y chat. Puedes llamar a la API del modelo proporcionada por Ollama según tus necesidades, enviando solicitudes al servicio local que se ejecuta en el puerto 11434.

**Chat**

```bash

curl http://127.0.0.1:11434/api/chat -d '{
  "model": "phi3",
  "messages": [
    {
      "role": "system",
      "content": "Your are a python developer."
    },
    {
      "role": "user",
      "content": "Help me generate a bubble algorithm"
    }
  ],
  "stream": false
  
}'


```

Este es el resultado en Postman

![Captura de pantalla de los resultados JSON para la solicitud de chat](../../../../translated_images/ollama_chat.25d29e9741e1daa8efd30ca36e60008b6f2841edb544ca8167645e0ec750c72a.es.png)

```bash

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "<|system|>Your are my AI assistant.<|end|><|user|>tell me how to learn AI<|end|><|assistant|>",
  "stream": false
}'


```

Este es el resultado en Postman

![Captura de pantalla de los resultados JSON para la solicitud de generate](../../../../translated_images/ollama_gen.523df35c3c34f0ada4770f77c9bb68f55442958adffe73ba5ae03e417ff9a781.es.png)

## Recursos adicionales

Consulta la lista de modelos disponibles en Ollama en [su biblioteca](https://ollama.com/library).

Descarga tu modelo desde el servidor de Ollama usando este comando

```bash
ollama pull phi3
```

Ejecuta el modelo usando este comando

```bash
ollama run phi3
```

***Nota:*** Visita este enlace [https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md) para aprender más

## Llamando a Ollama desde Python

Puedes usar `requests` or `urllib3` para hacer solicitudes a los endpoints del servidor local usados anteriormente. Sin embargo, una forma popular de usar Ollama en Python es a través del SDK de [openai](https://pypi.org/project/openai/), ya que Ollama proporciona endpoints del servidor compatibles con OpenAI.

Aquí hay un ejemplo para phi3-mini:

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

response = client.chat.completions.create(
    model="phi3",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about a hungry cat"},
    ],
)

print("Response:")
print(response.choices[0].message.content)
```

## Llamando a Ollama desde JavaScript 

```javascript
// Example of Summarize a file with Phi-3
script({
    model: "ollama:phi3",
    title: "Summarize with Phi-3",
    system: ["system"],
})

// Example of summarize
const file = def("FILE", env.files)
$`Summarize ${file} in a single paragraph.`
```

## Llamando a Ollama desde C#

Crea una nueva aplicación de consola en C# y añade el siguiente paquete NuGet:

```bash
dotnet add package Microsoft.SemanticKernel --version 1.13.0
```

Luego reemplaza este código en el archivo `Program.cs`

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

// add chat completion service using the local ollama server endpoint
#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri("http://localhost:11434/"),
    apiKey: "non required");

// invoke a simple prompt to the chat service
string prompt = "Write a joke about kittens";
var response = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(response.GetValue<string>());
```

Ejecuta la aplicación con el comando:

```bash
dotnet run
```

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.