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

var audioFilePath = Path.Combine(Directory.GetCurrentDirectory(), "audio", "audio_weather_alaw.wav");
var audioFiles = Audios.Load([audioFilePath]);
Images imageFiles = null;

var prompt = @"<|user|>
<|audio_1|>
generate a comprehensive text transcription of the spoken content in the audio, return the text transcription<|end|>
<|assistant|>";

// initialize model

// initialize model
Config config = new Config(modelPath);
config.ClearProviders();
#if DEBUG_CUDA
config.SetProviderOption("cuda", "enable_cuda_graph", "0");
#endif

var model = new Model(config);
var tokenizer = new Tokenizer(model);

//var model = new Model(modelPath);
//var tokenizer = new Tokenizer(model);

using MultiModalProcessor processor = new MultiModalProcessor(model);
using var tokenizerStream = processor.CreateStream();

// create the input tensor with the prompt and image
Console.WriteLine($"Full Prompt: \n{prompt}\n");
Console.WriteLine("Start processing audio and prompt ...");

var inputTensors = processor.ProcessImagesAndAudios(prompt, images: imageFiles, audios: audioFiles);
using GeneratorParams generatorParams = new GeneratorParams(model);
generatorParams.SetSearchOption("max_length", 7680);
generatorParams.SetInputs(inputTensors);

// generate response
Console.WriteLine("Generating response ...");
Console.WriteLine("");
using var generator = new Generator(model, generatorParams);
while (!generator.IsDone())
{
    generator.GenerateNextToken();
    var seq = generator.GetSequence(0)[^1];
    Console.Write(tokenizerStream.Decode(seq));
}

audioFiles.Dispose();
tokenizerStream.Dispose();
processor.Dispose();
tokenizer.Dispose();
model.Dispose();

Console.WriteLine("");
Console.WriteLine("Done!");