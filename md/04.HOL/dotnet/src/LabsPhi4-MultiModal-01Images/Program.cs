//    Copyright (c) 2025
//    Author      : Bruno Capuano
//    Change Log  :
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

using Microsoft.ML.OnnxRuntimeGenAI;

// Phi4
var modelPath = @"d:\phi\models\Phi-4-multimodal-instruct-onnx\gpu\gpu-int4-rtn-block-32\";

var foggyDayImagePath = Path.Combine(Directory.GetCurrentDirectory(), "imgs", "foggyday.png");
var img = Images.Load([foggyDayImagePath]);


var systemPrompt = "You are an AI assistant that helps people find information. Answer questions using a direct style. Do not share more information that the requested by the users.";
string userPrompt = "Describe the image, and return the string 'STOP' at the end.";
var fullPrompt = $"<|system|>{systemPrompt}<|end|><|user|><|image_1|>{userPrompt}<|end|><|assistant|>";

// initialize model
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);


using MultiModalProcessor processor = new MultiModalProcessor(model);
using var tokenizerStream = processor.CreateStream();

// create the input tensor with the prompt and image
Console.WriteLine($"Full Prompt: \n{fullPrompt}\n");
Console.WriteLine("Start processing image and prompt ...");
var inputTensors = processor.ProcessImages(fullPrompt, img);
using GeneratorParams generatorParams = new GeneratorParams(model);
generatorParams.SetSearchOption("max_length", 3072);
generatorParams.SetInputs(inputTensors);

// generate response
Console.WriteLine("Generating response ...");
Console.WriteLine("");
using var generator = new Generator(model, generatorParams);
while (!generator.IsDone())
{
    //generator.ComputeLogits();
    generator.GenerateNextToken();
    var seq = generator.GetSequence(0)[^1];
    Console.Write(tokenizerStream.Decode(seq));
}

tokenizerStream.Dispose();
processor.Dispose();
tokenizer.Dispose();
model.Dispose();

Console.WriteLine("");
Console.WriteLine("Done!");