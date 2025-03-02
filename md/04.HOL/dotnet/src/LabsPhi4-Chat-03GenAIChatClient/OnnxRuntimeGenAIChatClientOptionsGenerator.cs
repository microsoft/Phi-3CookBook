using Microsoft.Extensions.AI;
using Microsoft.ML.OnnxRuntimeGenAI;
using System.Text;

public static class OnnxRuntimeGenAIChatClientOptionsGenerator
{
    public static OnnxRuntimeGenAIChatClientOptions GetDefault()
    {
        return new OnnxRuntimeGenAIChatClientOptions()
        {
            StopSequences = ["<|system|>", "<|user|>", "<|assistant|>", "<|end|>"],
            PromptFormatter = static (messages, options) =>
            {
                StringBuilder prompt = new();

                foreach (var message in messages)
                    foreach (var content in message.Contents.OfType<TextContent>())
                        prompt.Append("<|").Append(message.Role.Value).Append("|>\n").Append(content.Text).Append("<|end|>\n");

                return prompt.Append("<|assistant|>\n").ToString();
            },
        };
    }
}
