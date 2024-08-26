//    Copyright (c) 2024
//    Author      : Bruno Capuano
//    Change Log  :
//    - Sample console application to use a local model hosted in ollama and semantic memory for search
//
//    The MIT License (MIT)
//
//    Permission is hereby granted, free of charge, to any person obtaining a copy
//    of this software and associated documentation files (the "Software"), to deal
//    in the Software without restriction, including without limitation the rights
//    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
//    copies of the Software, and to permit persons to whom the Software is
//    furnished to do so, subject to the following conditions:
//
//    The above copyright notice and this permission notice shall be included in
//    all copies or substantial portions of the Software.
//
//    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
//    THE SOFTWARE.

#pragma warning disable SKEXP0001
#pragma warning disable SKEXP0003
#pragma warning disable SKEXP0010
#pragma warning disable SKEXP0011
#pragma warning disable SKEXP0050
#pragma warning disable SKEXP0052

using Microsoft.Extensions.DependencyInjection;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using Microsoft.SemanticKernel.Embeddings;
using Microsoft.SemanticKernel.Memory;
using Microsoft.SemanticKernel.Plugins.Memory;

var question = "What is Bruno's favourite super hero?";
Console.WriteLine($"This program will answer the following question: {question}");
Console.WriteLine("1st approach will be to ask the question directly to the Phi-3 model.");
Console.WriteLine("2nd approach will be to add facts to a semantic memory and ask the question again");
Console.WriteLine("");

// Create a chat completion service
var builder = Kernel.CreateBuilder();
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri("http://localhost:11434"),
    apiKey: "apikey");
builder.AddLocalTextEmbeddingGeneration();
Kernel kernel = builder.Build();

Console.WriteLine($"Phi-3 response (no memory).");
var response = kernel.InvokePromptStreamingAsync(question);
await foreach (var result in response)
{
    Console.Write(result);
}

// separator
Console.WriteLine("");
Console.WriteLine("==============");
Console.WriteLine("");

// get the embeddings generator service
var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);

// add facts to the collection
const string MemoryCollectionName = "fanFacts";

await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", text: "Gisela's favourite super hero is Batman");
await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", text: "The last super hero movie watched by Gisela was Guardians of the Galaxy Vol 3");
await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", text: "Bruno's favourite super hero is Invincible");
await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", text: "The last super hero movie watched by Bruno was Aquaman II");
await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", text: "Bruno don't like the super hero movie: Eternals");

TextMemoryPlugin memoryPlugin = new(memory);

// Import the text memory plugin into the Kernel.
kernel.ImportPluginFromObject(memoryPlugin);

OpenAIPromptExecutionSettings settings = new()
{
    ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions,
};


var prompt = @"
    Question: {{$input}}
    Answer the question using the memory content: {{Recall}}";

var arguments = new KernelArguments(settings)
{
    { "input", question },
    { "collection", MemoryCollectionName }
};

Console.WriteLine($"Phi-3 response (using semantic memory).");

response = kernel.InvokePromptStreamingAsync(prompt, arguments);
await foreach (var result in response)
{
    Console.Write(result);
}

Console.WriteLine($"");