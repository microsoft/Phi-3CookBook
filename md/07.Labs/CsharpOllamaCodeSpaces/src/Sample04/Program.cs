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

#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;

using OpenTelemetry;
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using System.Text;

// Define endpoints for telemetry and Phi-3
var otlpEndPoint = "http://localhost:4317";
var phi3EndPoint = "http://localhost:11434";

// Create kernel with a custom http address
var builder = Kernel.CreateBuilder();
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri(phi3EndPoint),
    apiKey: "apikey");
ConfigureOpenTelemetry(builder, otlpEndPoint);
var kernel = builder.Build();

var chat = kernel.GetRequiredService<IChatCompletionService>();
var history = new ChatHistory();
history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

while (true)
{
    Console.Write("Q: ");
    var userQ = Console.ReadLine();
    if (string.IsNullOrEmpty(userQ))
    {
        break;
    }
    history.AddUserMessage(userQ);
    kernel.Services.GetRequiredService<ILogger<Program>>().LogInformation($"User Question: {userQ}");

    Console.Write($"Phi-3: ");
    StringBuilder sb = new();
    var result = chat.GetStreamingChatMessageContentsAsync(history);
    await foreach (var item in result)
    {
        sb.Append(item);
        Console.Write(item);
    }
    Console.WriteLine("");
    history.AddAssistantMessage(sb.ToString());

    // logging message
    kernel.Services.GetRequiredService<ILogger<Program>>().LogInformation($"Phi-3 Response: {sb.ToString()}");
}

static IKernelBuilder ConfigureOpenTelemetry(IKernelBuilder builder, string otlpEndPoint)
{
    builder.Services.AddLogging(logging =>
    {
        //logging.AddSimpleConsole(options => options.TimestampFormat = "hh:mm:ss ");
        logging.SetMinimumLevel(LogLevel.Debug);

        //logging.AddConsole();
        logging.Configure(options =>
        {
            options.ActivityTrackingOptions = ActivityTrackingOptions.SpanId;
        });
    });

    builder.Services.AddOpenTelemetry()
        .ConfigureResource(c => c.AddService("Sample04"))
        .WithMetrics(metrics =>
        {
            metrics.AddHttpClientInstrumentation()
                   .AddRuntimeInstrumentation();
        })
        .WithTracing(tracing =>
        {
            tracing.AddHttpClientInstrumentation();
        });


    var useOtlpExporter = !string.IsNullOrWhiteSpace(otlpEndPoint);
    if (useOtlpExporter)
    {
        builder.Services.AddOpenTelemetry().UseOtlpExporter();
    }

    return builder;
}
