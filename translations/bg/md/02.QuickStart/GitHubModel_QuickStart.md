## GitHub Модели - Ограничена публична бета

Добре дошли в [GitHub Модели](https://github.com/marketplace/models)! Всичко е готово, за да изследвате AI модели, хоствани на Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.bg.png)

За повече информация относно наличните модели в GitHub Модели, посетете [GitHub Model Marketplace](https://github.com/marketplace/models)

## Налични модели

Всеки модел разполага със специална среда за тестване и примерен код.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Модели в GitHub Model Catalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Първи стъпки

Има няколко основни примера, готови за изпълнение. Можете да ги намерите в директорията със sample файлове. Ако искате директно да преминете към любимия си език, можете да намерите примери на следните езици:

- Python
- JavaScript
- cURL

Има също специална среда Codespaces за изпълнение на примерите и моделите.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.bg.png)

## Примерен код

По-долу са дадени примери за код за няколко случая на използване. За допълнителна информация относно Azure AI Inference SDK, вижте пълната документация и примери.

## Настройка

1. Създайте личен достъпен токен  
Не е необходимо да давате разрешения на токена. Имайте предвид, че токенът ще бъде изпратен до услуга на Microsoft.

За да използвате примерите за код по-долу, създайте променлива на средата, за да зададете токена като ключ за клиентския код.

Ако използвате bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ако сте в PowerShell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ако използвате командния ред на Windows:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python Пример

### Инсталирайте зависимости  
Инсталирайте Azure AI Inference SDK с помощта на pip (Изисква: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Изпълнете основен пример за код  

Този пример демонстрира основно извикване на API за завършване на чат. Използва се крайна точка за GitHub AI модел и вашият GitHub токен. Извикването е синхронно.

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name 
model_name = "Phi-3-small-8k-instruct"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="What is the capital of France?"),
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)
```  

### Изпълнете многозавършващ разговор  

Този пример демонстрира многозавършващ разговор с API за завършване на чат. Когато използвате модела за чат приложение, ще трябва да управлявате историята на разговора и да изпращате последните съобщения към модела.

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    UserMessage(content="What is the capital of France?"),
    AssistantMessage(content="The capital of France is Paris."),
    UserMessage(content="What about Spain?"),
]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```  

### Стрийминг на изхода  

За по-добро потребителско изживяване ще искате да стриймвате отговора от модела, така че първият токен да се появи рано и да избегнете чакането на дълги отговори.

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Give me 5 good reasons why I should exercise every day."),
    ],
    model=model_name,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
```  

## JavaScript  

### Инсталирайте зависимости  

Инсталирайте Node.js.  

Копирайте следните редове текст и ги запазете като файл package.json във вашата папка.  

```
{
  "type": "module",
  "dependencies": {
    "@azure-rest/ai-inference": "latest",
    "@azure/core-auth": "latest",
    "@azure/core-sse": "latest"
  }
}
```  

Забележка: @azure/core-sse е необходим само когато стриймвате отговора от завършването на чат.  

Отворете терминал в тази папка и изпълнете npm install.  

За всеки от примерите за код по-долу копирайте съдържанието в файл sample.js и го изпълнете с node sample.js.  

### Изпълнете основен пример за код  

Този пример демонстрира основно извикване на API за завършване на чат. Използва се крайна точка за GitHub AI модел и вашият GitHub токен. Извикването е синхронно.

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role:"system", content: "You are a helpful assistant." },
        { role:"user", content: "What is the capital of France?" }
      ],
      model: modelName,
      temperature: 1.,
      max_tokens: 1000,
      top_p: 1.
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }
  console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```  

### Изпълнете многозавършващ разговор  

Този пример демонстрира многозавършващ разговор с API за завършване на чат. Когато използвате модела за чат приложение, ще трябва да управлявате историята на разговора и да изпращате последните съобщения към модела.

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of France?" },
        { role: "assistant", content: "The capital of France is Paris." },
        { role: "user", content: "What about Spain?" },
      ],
      model: modelName,
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }

  for (const choice of response.body.choices) {
    console.log(choice.message.content);
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```  

### Стрийминг на изхода  

За по-добро потребителско изживяване ще искате да стриймвате отговора от модела, така че първият токен да се появи рано и да избегнете чакането на дълги отговори.

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";
import { createSseStream } from "@azure/core-sse";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Give me 5 good reasons why I should exercise every day." },
      ],
      model: modelName,
      stream: true
    }
  }).asNodeStream();

  const stream = response.body;
  if (!stream) {
    throw new Error("The response stream is undefined");
  }

  if (response.status !== "200") {
    stream.destroy();
    throw new Error(`Failed to get chat completions, http operation failed with ${response.status} code`);
  }

  const sseStream = createSseStream(stream);

  for await (const event of sseStream) {
    if (event.data === "[DONE]") {
      return;
    }
    for (const choice of (JSON.parse(event.data)).choices) {
        process.stdout.write(choice.delta?.content ?? ``);
    }
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```  

## REST  

### Изпълнете основен пример за код  

Поставете следното в shell:  

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```  

### Изпълнете многозавършващ разговор  

Извикайте API за завършване на чат и предайте историята на чата:  

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            },
            {
                "role": "assistant",
                "content": "The capital of France is Paris."
            },
            {
                "role": "user",
                "content": "What about Spain?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```  

### Стрийминг на изхода  

Това е пример за извикване на крайна точка и стриймване на отговора.  

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Give me 5 good reasons why I should exercise every day."
            }
        ],
        "stream": true,
        "model": "Phi-3-small-8k-instruct"
    }'
```  

## БЕЗПЛАТНО използване и лимити за GitHub Модели  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.bg.png)  

[Лимитите за използване на средата за тестване и безплатния API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) са създадени, за да ви помогнат да експериментирате с модели и да прототипирате вашето AI приложение. За използване извън тези лимити и за мащабиране на вашето приложение, трябва да осигурите ресурси от акаунт в Azure и да се удостоверите оттам вместо чрез вашия GitHub личен достъпен токен. Не е необходимо да променяте нищо друго в кода си. Използвайте този линк, за да научите как да преминете отвъд лимитите на безплатния слой в Azure AI.

### Уточнения  

Помнете, че когато взаимодействате с модел, експериментирате с AI, така че са възможни грешки в съдържанието.  

Функцията е обект на различни ограничения (включително заявки на минута, заявки на ден, токени на заявка и едновременни заявки) и не е предназначена за производствени случаи на използване.  

GitHub Модели използва Azure AI Content Safety. Тези филтри не могат да бъдат изключени като част от преживяването с GitHub Модели. Ако решите да използвате модели чрез платена услуга, моля, конфигурирайте вашите филтри за съдържание, за да отговарят на вашите изисквания.  

Тази услуга е под Предварителните условия за ползване на GitHub.  

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.