//    Copyright (c) 2024
//    Author      : Bruno Capuano
//    Change Log  :
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

#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052, SKEXP0070

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

var ollamaEndpoint = "http://localhost:11434";
var modelIdChat = "phi3.5";

// Create kernel with a custom http address
var kernel = Kernel.CreateBuilder()
    .AddOllamaChatCompletion(modelId: modelIdChat, endpoint: new Uri(ollamaEndpoint))
    .Build();

var settings = new OpenAIPromptExecutionSettings
{
    MaxTokens = 100,
    Temperature = 1
};
var kernelArguments = new KernelArguments(settings);

var prompt = "Write a short joke about kittens. Use Emojis";
var response = kernel.InvokePromptStreamingAsync(prompt, kernelArguments);

await foreach (var message in response)
{
    Console.Write(message.ToString());
}
