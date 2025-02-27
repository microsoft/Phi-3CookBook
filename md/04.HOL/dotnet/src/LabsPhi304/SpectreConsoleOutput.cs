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

#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
using Spectre.Console;

namespace LabsPhi304;

public static class SpectreConsoleOutput
{
    public static void DisplayTitle(string title = ".NET - Phi-3 Vision Sample")
    {
        AnsiConsole.Write(new FigletText(title).Centered().Color(Color.Purple));
    }

    public static void DisplayTitleH2(string subtitle)
    {
        AnsiConsole.MarkupLine($"[bold][blue]=== {subtitle} ===[/][/]");
        AnsiConsole.MarkupLine($"");
    }

    public static void DisplayTitleH3(string subtitle)
    {
        AnsiConsole.MarkupLine($"[bold]>> {subtitle}[/]");
        AnsiConsole.MarkupLine($"");
    }

    public static void DisplayQuestion(string question)
    {
        AnsiConsole.MarkupLine($"[bold][blue]>>Q: {question}[/][/]");
        AnsiConsole.MarkupLine($"");
    }
    public static void DisplayAnswerStart(string answerPrefix)
    {
        AnsiConsole.Markup($"[bold][blue]>> {answerPrefix}:[/][/]");
    }

    public static void DisplayFilePath(string prefix, string filePath)
    {
        var path = new TextPath(filePath);

        AnsiConsole.Markup($"[bold][blue]>> {prefix}: [/][/]");
        AnsiConsole.Write(path);
        AnsiConsole.MarkupLine($"");
    }

    public static void DisplaySubtitle(string prefix, string content)
    {
        AnsiConsole.Markup($"[bold][blue]>> {prefix}: [/][/]");
        AnsiConsole.WriteLine(content);
        AnsiConsole.MarkupLine($"");
    }



    public static int AskForNumber(string question)
    {
        var number = AnsiConsole.Ask<int>(@$"[green]{question}[/]");
        return number;
    }

    public static string AskForString(string question)
    {
        var response = AnsiConsole.Ask<string>(@$"[green]{question}[/]");
        return response;
    }

    public static List<string> SelectScenarios()
    {
        // Ask for the user's favorite fruits
        var scenarios = AnsiConsole.Prompt(
            new MultiSelectionPrompt<string>()
                .Title("Select the [green]Phi 3 Vision scenarios[/] to run?")
                .PageSize(10)
                .Required(true)
                .MoreChoicesText("[grey](Move up and down to reveal more scenarios)[/]")
                .InstructionsText(
                    "[grey](Press [blue]<space>[/] to toggle a scenario, " +
                    "[green]<enter>[/] to accept)[/]")
                .AddChoiceGroup("Select an image to be analuyzed", new[]
                    {"foggyday.png","foggydaysmall.png","petsmusic.png","ultrarunningmug.png",
                    })
                .AddChoices( new[] { 
                    "Type the image path to be analyzed",
                    "Type a question"
                    })
                );
        return scenarios;
    }
}