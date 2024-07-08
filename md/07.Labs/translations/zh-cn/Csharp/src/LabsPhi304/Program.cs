//    Copyright (c) 2024
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

using LabsPhi304;
using Microsoft.ML.OnnxRuntimeGenAI;
using Spectre.Console;
using System.Text;

// path for model and images
var modelPath = @"d:\phi3\models\Phi-3-vision-128k-instruct-onnx-cpu\cpu-int4-rtn-block-32-acc-level-4";

// write title
SpectreConsoleOutput.DisplayTitle($".NET - Phi3v");

// load model and create processor
using Model model = new Model(modelPath);
using MultiModalProcessor processor = new MultiModalProcessor(model);
using var tokenizerStream = processor.CreateStream();
var tokenizer = new Tokenizer(model);

// define prompts
var systemPrompt = "You are an AI assistant that helps people find information. Answer questions using a direct style. Do not share more information that the requested by the users.";

// user choice scenarios
var scenarios = SpectreConsoleOutput.SelectScenarios();
var scenario = scenarios[0];

// switch between the options for the selected scenario
// options can be file names with extension equal to ".png" or ".jpg"
// or the values "Type the image path to be analyzed" or "Type a question"
switch (scenario)
{
    case "foggyday.png":
    case "foggydaysmall.png":
    case "petsmusic.png":
    case "ultrarunningmug.png":
        var imagePath = Path.Combine(Directory.GetCurrentDirectory(), "imgs", scenario);
        AnalizeImage(imagePath);
        break;
    case "Type the image path to be analyzed":
        scenario = SpectreConsoleOutput.AskForString("Type the image path to be analyzed");
        AnalizeImage(scenario);
        break;
    case "Type a question":
        AnswerQuestion();
        break;
}
SpectreConsoleOutput.DisplayTitleH3("Done !");

void AnswerQuestion()
{
    var question = SpectreConsoleOutput.AskForString("Type a question");
    SpectreConsoleOutput.DisplayQuestion(question);
    SpectreConsoleOutput.DisplayAnswerStart("Phi-3");

    var fullPrompt = $"<|system|>{systemPrompt}<|end|><|user|>{question}<|end|><|assistant|>";
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

void AnalizeImage(string imagePath)
{
    // display text with the image path
    SpectreConsoleOutput.DisplayFilePath("Analizing image", imagePath);

    // Display the image thumbnail
    var image = new CanvasImage(imagePath);
    image.MaxWidth(16);
    AnsiConsole.Write(image);

    StringBuilder phiResponse = new StringBuilder();

    AnsiConsole.Status()
    .Start("Analyzing image ...", ctx =>
    {
         var img = Images.Load(imagePath);
        string userPrompt = "Describe the image, and return the string 'STOP' at the end.";
        var fullPrompt = $"<|system|>{systemPrompt}<|end|><|user|><|image_1|>{userPrompt}<|end|><|assistant|>";

        // create the input tensor with the prompt and image
        SpectreConsoleOutput.DisplaySubtitle("Full Prompt", fullPrompt);

        // Update the status and spinner
        ctx.Status("ONNX image processing ...");
        ctx.Spinner(Spinner.Known.Star);
        ctx.SpinnerStyle(Style.Parse("green"));


        var inputTensors = processor.ProcessImages(fullPrompt, img);
        using GeneratorParams generatorParams = new GeneratorParams(model);
        generatorParams.SetSearchOption("max_length", 3072);
        generatorParams.SetInputs(inputTensors);

        var isProcessingTokenStarted = false;

        // generate response        
        using var generator = new Generator(model, generatorParams);
        while (!generator.IsDone())
        {
            generator.ComputeLogits();
            generator.GenerateNextToken();

            if (!isProcessingTokenStarted)
            {
                ctx.Status("Processing response tokens ...");
                ctx.Spinner(Spinner.Known.Dots12);
                ctx.SpinnerStyle(Style.Parse("blue"));
                isProcessingTokenStarted = true;
            }

            var seq = generator.GetSequence(0)[^1];
            var tokenString = tokenizerStream.Decode(seq);
            AnsiConsole.Markup($"[bold][blue]>> Token:[/][/] {tokenString}");
            phiResponse.Append(tokenString);
        }
    });

    // display the response
    SpectreConsoleOutput.DisplaySubtitle("Phi-3 Response", phiResponse.ToString());
}