# **Usando Phi-3 en Hugging Face**

[Hugging Face](https://huggingface.co/) es una comunidad de IA muy popular con datos ricos y recursos de modelos de código abierto. Diferentes fabricantes lanzan LLM y SLM de código abierto a través de Hugging Face, como Microsoft, Meta, Mistral, Apple, Google, etc.

![Phi3](../../../../translated_images/Hg_Phi3.dc94956455e775c886b69f7430a05b7a42aab729a81fa4083c906812edb475f8.es.png)

Microsoft Phi-3 ha sido lanzado en Hugging Face. Los desarrolladores pueden descargar el modelo Phi-3 correspondiente basado en escenarios y negocios. Además de desplegar modelos Pytorch de Phi-3 en Hugging Face, también hemos lanzado modelos cuantificados, utilizando formatos GGUF y ONNX para ofrecer opciones a los usuarios finales.


## **1. Descargar Phi-3 desde Hugging Face**

```bash

git lfs install 

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

```

## **2. Conocer la Plantilla de Prompt de Phi-3**

Existe una plantilla de datos específica al entrenar Phi-3, por lo que al usar Phi-3, el envío de Prompt necesita configurarse a través de la Plantilla. Durante el ajuste fino, los datos también deben expandirse según la plantilla.

La plantilla tiene tres roles, incluyendo sistema, usuario y asistente.

```txt

<|system|>
Your Role<|end|>
<|user|>
Your Question?<|end|>
<|assistant|>

```

por ejemplo

```txt

<|system|>
Eres un desarrollador de Python.<|end|>
<|user|>
Ayúdame a generar un algoritmo de burbuja<|end|>
<|assistant|>

```

## **3. Inferencias con Phi-3 usando Python**

Las inferencias con Phi-3 se refieren al proceso de usar los modelos Phi-3 para generar predicciones o salidas basadas en datos de entrada. Los modelos Phi-3 son una familia de pequeños modelos de lenguaje (SLMs) que incluyen variantes como Phi-3-Mini, Phi-3-Small y Phi-3-Medium, cada uno diseñado para diferentes escenarios de aplicación y con tamaños de parámetros variados. Estos modelos han sido entrenados con datos de alta calidad y están afinados para capacidades de chat, alineación, robustez y seguridad. Pueden ser desplegados tanto en plataformas de borde como en la nube usando ONNX y TensorFlow Lite, y se desarrollan de acuerdo con los principios de IA Responsable de Microsoft.

Por ejemplo, el Phi-3-Mini es un modelo ligero y de última generación con 3.8 mil millones de parámetros, adecuado para prompts en formato de chat y soportando una longitud de contexto de hasta 128K tokens. Es el primer modelo en su clase de peso en soportar un contexto tan largo.

Los modelos Phi-3 están disponibles en plataformas como Azure AI MaaS, HuggingFace, NVIDIA, Ollama, ONNX, y pueden ser usados para una variedad de aplicaciones, incluyendo interacciones en tiempo real, sistemas autónomos y aplicaciones que requieren baja latencia.

Hay muchas maneras de referenciar Phi-3. Puedes usar diferentes lenguajes de programación para referenciar el modelo.

Aquí hay un ejemplo en Python.

```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

messages = [
    {"role": "system", "content": "Eres un desarrollador de Python."},
    {"role": "user", "content": "Ayúdame a generar un algoritmo de burbuja"},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 600,
    "return_full_text": False,
    "temperature": 0.3,
    "do_sample": False,
}

output = pipe(messages, **generation_args)
print(output[0]['generated_text'])


```

> [!NOTE]
> Puedes ver si este resultado es consistente con el resultado en tu mente

## **4. Inferencias con Phi-3 usando C#**

Aquí hay un ejemplo en una aplicación de consola .NET.

El proyecto de C# debe agregar los siguientes paquetes:

```bash
dotnet add package Microsoft.ML.OnnxRuntime --version 1.18.0
dotnet add package Microsoft.ML.OnnxRuntimeGenAI --version 0.3.0-rc2
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda --version 0.3.0-rc2
```

Aquí está el código en C#.

```csharp
using System;
using Microsoft.ML.OnnxRuntimeGenAI;


// ubicación de la carpeta del archivo de modelo ONNX
var modelPath = @"..\models\Phi-3-mini-4k-instruct-onnx";
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);

var systemPrompt = "Eres un asistente de IA que ayuda a las personas a encontrar información. Responde preguntas usando un estilo directo. No compartas más información de la solicitada por los usuarios.";

// inicio del chat
Console.WriteLine(@"Haz tu pregunta. Escribe una cadena vacía para salir.");


// bucle de chat
while (true)
{
    // Obtener pregunta del usuario
    Console.WriteLine();
    Console.Write(@"Q: ");
    var userQ = Console.ReadLine();    
    if (string.IsNullOrEmpty(userQ))
    {
        break;
    }

    // mostrar respuesta de phi3
    Console.Write("Phi3: ");
    var fullPrompt = $"<|system|>{systemPrompt}<|end|><|user|>{userQ}<|end|><|assistant|>";
    var tokens = tokenizer.Encode(fullPrompt);

    var generatorParams = new GeneratorParams(model);
    generatorParams.SetSearchOption("max_length", 2048);
    generatorParams.SetSearchOption("past_present_share_buffer", false);
    generatorParams.SetInputSequences(tokens);

    var generator = new Generator(model, generatorParams);
    while (!generator.IsDone())
    {
        generator.ComputeLogits();
        generator.GenerateNextToken();
        var outputTokens = generator.GetSequence(0);
        var newToken = outputTokens.Slice(outputTokens.Length - 1, 1);
        var output = tokenizer.Decode(newToken);
        Console.Write(output);
    }
    Console.WriteLine();
}
```

La demostración en ejecución es similar a esta:

![Chat running demo](../../../../imgs/02/csharp/20SampleConsole.gif)

***Nota:** hay un error tipográfico en la primera pregunta, ¡Phi-3 es lo suficientemente genial para compartir la respuesta correcta!*

## **5. Usando Phi-3 en el Chat de Hugging Face**

El chat de Hugging Face proporciona una experiencia relacionada. Ingresa [aquí para probar el chat de Phi-3](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct) en tu navegador para experimentarlo.

![Hg_Chat](../../../../translated_images/Hg_Chat.6ca1ac61a91bc770f0fb8043586eaf117397de78a5f3c77dac81a6f115c5347c.es.png)

        Descargo de responsabilidad: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
        Por favor, revise el resultado y haga las correcciones necesarias.