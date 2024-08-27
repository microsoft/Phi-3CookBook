# **在 Ollama 中使用 Phi-3**

[Ollama](https://ollama.com) 使更多人能够通过简单的脚本直接部署开源LLM或SLM，并且还可以构建API来帮助本地Copilot应用场景。

## **1. 安装**

Ollama支持在Windows、macOS和Linux上运行。您可以通过此链接 ([https://ollama.com/download](https://ollama.com/download)) 安装Ollama。 安装成功后，您可以直接使用Ollama脚本通过终端窗口调用Phi-3。您可以在Ollama中查看所有可用的库 [available libaries in Ollama](https://ollama.com/library)。 如果您在Codespace中可以打开此存储库，意味着已经成功安装了Ollama。


```bash

ollama run phi3

```

***注意:*** 当您第一次运行时，模型将先被下载。当然，您也可以直接指定已下载的Phi-3模型。此处以WSL为例，运行命令。模型成功下载后，您可以直接在终端上进行交互。如下图所示。

![run](../../../../imgs/02/Ollama/ollama_run.png)

## **2.在 Ollama 中调用 Phi-3 API**

如果您想调用由ollama生成的Phi-3 API，您可以在终端中使用此命令启动Ollama服务器。

```bash

ollama serve

```
***注意:***  如果运行MacOS或Linux，您可能会遇到以下错误 <b>"Error: listen tcp 127.0.0.1:11434: bind: address already in use"</b> 在运行命令时，您可能会遇到这个错误。您可以忽略该错误，因为它通常表示服务器已经在运行，或者您可以停止并重新启动Ollama:

**macOS**


```bash

brew services restart ollama

```

**Linux**


```bash

sudo systemctl stop ollama

```

Ollama支持两个API：generate和chat。您可以根据需要调用Ollama提供的模型API，通过向运行在11434端口的本地服务发送请求。

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

以下是Postman调试工具返回的结果：


![Screenshot of JSON results for chat request](../../../../imgs/02/Ollama/ollama_chat.png)


```bash

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "<|system|>Your are my AI assistant.<|end|><|user|>tell me how to learn AI<|end|><|assistant|>",
  "stream": false
}'


```


以下是Postman调试工具返回的结果：


![Screenshot of JSON results for generate request](../../../../imgs/02/Ollama/ollama_gen.png)

# 其他资源

请查看Ollama库中可用模型的列表 [their library](https://ollama.com/library).

使用此命令从Ollama服务器获取您的模型：

```bash
ollama pull phi3
```

使用此命令来运行模型：

```bash
ollama run phi3
```

***注意:*** 可以访问此链接来获取更多信息 [https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md)


## 使用 Python 调用 Ollama

您可以使用 `requests` 或者 `urllib3` 向上述本地服务器端点发出请求。然而，在Python中使用Ollama的一种流行方法是通过 [openai](https://pypi.org/project/openai/) SDK, 因为Ollama同样也提供了与OpenAI兼容的服务器端点。

下面是利用openai SDK来访问 phi3-mini 的例子:

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

## 使用 JavaScript 调用 Ollama

下面是使用JavaScript来进行文件内容总结的例子：

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

## 使用 C# 调用 Ollama

创建一个新的C# Console应用程序，添加以下NuGet包：

```bash
dotnet add package Microsoft.SemanticKernel --version 1.13.0
```

在 `Program.cs` 文件中，添加以下代码：

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

用以下命令运行应用:

```bash
dotnet run
```
