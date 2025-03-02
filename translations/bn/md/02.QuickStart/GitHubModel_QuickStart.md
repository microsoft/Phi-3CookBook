## গিটহাব মডেলস - সীমিত পাবলিক বিটা

[গিটহাব মডেলস](https://github.com/marketplace/models)-এ আপনাকে স্বাগতম! আমরা সবকিছু প্রস্তুত রেখেছি যাতে আপনি Azure AI-তে হোস্ট করা AI মডেলগুলো সহজেই এক্সপ্লোর করতে পারেন।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.bn.png)

গিটহাব মডেলসে উপলব্ধ মডেল সম্পর্কে আরও তথ্য পেতে, দেখুন [গিটহাব মডেল মার্কেটপ্লেস](https://github.com/marketplace/models)।

## উপলব্ধ মডেল

প্রতিটি মডেলের জন্য একটি নির্দিষ্ট প্লেগ্রাউন্ড এবং নমুনা কোড রয়েছে।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### গিটহাব মডেল ক্যাটালগে Phi-3 মডেলস

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## শুরু করা

কিছু বেসিক উদাহরণ প্রস্তুত রয়েছে যা আপনি চালাতে পারেন। এগুলো নমুনা ডিরেক্টরিতে পাওয়া যাবে। যদি আপনি সরাসরি আপনার প্রিয় ভাষায় যেতে চান, তাহলে নিম্নলিখিত ভাষাগুলোতে উদাহরণ পাবেন:

- পাইথন  
- জাভাস্ক্রিপ্ট  
- cURL  

নমুনা এবং মডেল চালানোর জন্য একটি নির্দিষ্ট Codespaces পরিবেশও রয়েছে।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.bn.png)

## নমুনা কোড

নিচে কিছু ব্যবহার ক্ষেত্রে উদাহরণ কোড স্নিপেট দেওয়া হলো। Azure AI Inference SDK সম্পর্কিত অতিরিক্ত তথ্যের জন্য সম্পূর্ণ ডকুমেন্টেশন এবং নমুনাগুলো দেখুন।

## সেটআপ

1. একটি ব্যক্তিগত অ্যাক্সেস টোকেন তৈরি করুন  
এই টোকেনের জন্য কোনো অনুমতি দেওয়ার প্রয়োজন নেই। টোকেনটি একটি মাইক্রোসফট সার্ভিসে পাঠানো হবে।  

নিচের কোড স্নিপেটগুলো ব্যবহার করতে, একটি এনভায়রনমেন্ট ভেরিয়েবল তৈরি করুন এবং টোকেনটি ক্লায়েন্ট কোডের জন্য কী হিসেবে সেট করুন।  

যদি আপনি bash ব্যবহার করেন:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
যদি আপনি powershell-এ থাকেন:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

যদি আপনি Windows কমান্ড প্রম্পট ব্যবহার করেন:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## পাইথন নমুনা

### ডিপেনডেন্সি ইনস্টল করুন  
pip ব্যবহার করে Azure AI Inference SDK ইনস্টল করুন (প্রয়োজন: Python >=3.8):  

```
pip install azure-ai-inference
```  

### একটি বেসিক কোড উদাহরণ চালান  

এই উদাহরণটি chat completion API-তে একটি বেসিক কল ডেমোনস্ট্রেট করে। এটি GitHub AI মডেল ইনফারেন্স এন্ডপয়েন্ট এবং আপনার GitHub টোকেন ব্যবহার করছে। এই কলটি সিঙ্ক্রোনাস।  

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

### একটি মাল্টি-টার্ন কথোপকথন চালান  

এই উদাহরণটি chat completion API-এর সঙ্গে একটি মাল্টি-টার্ন কথোপকথন ডেমোনস্ট্রেট করে। চ্যাট অ্যাপ্লিকেশনের জন্য মডেল ব্যবহার করার সময়, আপনাকে সেই কথোপকথনের ইতিহাস পরিচালনা করতে হবে এবং সর্বশেষ বার্তাগুলো মডেলে পাঠাতে হবে।  

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

### আউটপুট স্ট্রিম করুন  

ভাল ব্যবহারকারীর অভিজ্ঞতার জন্য, আপনি মডেলের প্রতিক্রিয়া স্ট্রিম করতে চাইবেন যাতে প্রথম টোকেনটি তাড়াতাড়ি দেখা যায় এবং দীর্ঘ প্রতিক্রিয়ার জন্য অপেক্ষা করতে না হয়।  

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

## জাভাস্ক্রিপ্ট  

### ডিপেনডেন্সি ইনস্টল করুন  

Node.js ইনস্টল করুন।  

নিচের টেক্সটগুলো কপি করে আপনার ফোল্ডারে package.json নামে একটি ফাইল হিসেবে সংরক্ষণ করুন।  

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

দ্রষ্টব্য: @azure/core-sse শুধুমাত্র তখন প্রয়োজন যখন আপনি চ্যাট কমপ্লিশনের প্রতিক্রিয়া স্ট্রিম করেন।  

এই ফোল্ডারে একটি টার্মিনাল উইন্ডো খুলুন এবং npm install চালান।  

নিচের কোড স্নিপেটগুলোর প্রতিটির জন্য, কনটেন্ট কপি করে sample.js নামে একটি ফাইলে সংরক্ষণ করুন এবং node sample.js দিয়ে চালান।  

### একটি বেসিক কোড উদাহরণ চালান  

এই উদাহরণটি chat completion API-তে একটি বেসিক কল ডেমোনস্ট্রেট করে। এটি GitHub AI মডেল ইনফারেন্স এন্ডপয়েন্ট এবং আপনার GitHub টোকেন ব্যবহার করছে। এই কলটি সিঙ্ক্রোনাস।  

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

### একটি মাল্টি-টার্ন কথোপকথন চালান  

এই উদাহরণটি chat completion API-এর সঙ্গে একটি মাল্টি-টার্ন কথোপকথন ডেমোনস্ট্রেট করে। চ্যাট অ্যাপ্লিকেশনের জন্য মডেল ব্যবহার করার সময়, আপনাকে সেই কথোপকথনের ইতিহাস পরিচালনা করতে হবে এবং সর্বশেষ বার্তাগুলো মডেলে পাঠাতে হবে।  

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

### আউটপুট স্ট্রিম করুন  
ভাল ব্যবহারকারীর অভিজ্ঞতার জন্য, আপনি মডেলের প্রতিক্রিয়া স্ট্রিম করতে চাইবেন যাতে প্রথম টোকেনটি তাড়াতাড়ি দেখা যায় এবং দীর্ঘ প্রতিক্রিয়ার জন্য অপেক্ষা করতে না হয়।  

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

### একটি বেসিক কোড উদাহরণ চালান  

একটি শেলে নিচেরটি পেস্ট করুন:  

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

### একটি মাল্টি-টার্ন কথোপকথন চালান  

chat completion API-তে কল করুন এবং চ্যাট ইতিহাস পাঠান:  

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

### আউটপুট স্ট্রিম করুন  

এটি এন্ডপয়েন্টে কল করার এবং প্রতিক্রিয়া স্ট্রিম করার একটি উদাহরণ।  

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

## গিটহাব মডেলের জন্য ফ্রি ব্যবহার এবং রেট সীমা  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.bn.png)  

[প্লেগ্রাউন্ড এবং ফ্রি API ব্যবহারের জন্য রেট সীমা](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) আপনাকে মডেলগুলো পরীক্ষা করার এবং আপনার AI অ্যাপ্লিকেশন প্রোটোটাইপ করার জন্য সাহায্য করার উদ্দেশ্যে প্রণীত। এই সীমার বাইরে ব্যবহারের জন্য এবং আপনার অ্যাপ্লিকেশনকে স্কেলে নিয়ে যেতে, আপনাকে একটি Azure অ্যাকাউন্ট থেকে রিসোর্স প্রভিশন করতে হবে এবং সেখান থেকে অথেন্টিকেট করতে হবে, আপনার গিটহাব ব্যক্তিগত অ্যাক্সেস টোকেনের পরিবর্তে। আপনার কোডে অন্য কিছু পরিবর্তন করার প্রয়োজন নেই। Azure AI-তে ফ্রি টিয়ার সীমার বাইরে যেতে কীভাবে করবেন তা জানতে এই লিংকটি ব্যবহার করুন।  

### প্রকাশ  

মডেলের সঙ্গে ইন্টারঅ্যাক্ট করার সময় মনে রাখবেন যে আপনি AI নিয়ে পরীক্ষা করছেন, তাই কনটেন্টে ভুল থাকতে পারে।  

এই ফিচারটি বিভিন্ন সীমার (যেমন প্রতি মিনিটে অনুরোধ, প্রতি দিনে অনুরোধ, প্রতি অনুরোধে টোকেন এবং কনকারেন্ট অনুরোধ) অধীন এবং এটি প্রোডাকশন ব্যবহারের জন্য ডিজাইন করা হয়নি।  

গিটহাব মডেলস Azure AI কনটেন্ট সেফটি ব্যবহার করে। গিটহাব মডেলস অভিজ্ঞতার অংশ হিসেবে এই ফিল্টারগুলো বন্ধ করা যাবে না। যদি আপনি পেইড সার্ভিসের মাধ্যমে মডেল ব্যবহার করার সিদ্ধান্ত নেন, তাহলে আপনার প্রয়োজন অনুযায়ী কনটেন্ট ফিল্টারগুলো কনফিগার করুন।  

এই সার্ভিসটি গিটহাবের প্রি-রিলিজ টার্মসের অধীন।  

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবাগুলির মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহার থেকে উদ্ভূত যেকোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।