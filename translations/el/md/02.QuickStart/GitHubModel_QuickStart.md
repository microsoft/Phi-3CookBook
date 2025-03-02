## Μοντέλα GitHub - Περιορισμένη Δημόσια Δοκιμαστική Έκδοση

Καλώς ήρθατε στα [GitHub Models](https://github.com/marketplace/models)! Όλα είναι έτοιμα για να εξερευνήσετε τα Μοντέλα AI που φιλοξενούνται στο Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.el.png)

Για περισσότερες πληροφορίες σχετικά με τα διαθέσιμα Μοντέλα στα GitHub Models, επισκεφθείτε το [GitHub Model Marketplace](https://github.com/marketplace/models)

## Διαθέσιμα Μοντέλα

Κάθε μοντέλο διαθέτει ξεχωριστό playground και δείγματα κώδικα.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Μοντέλα Phi-3 στον Κατάλογο Μοντέλων GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Ξεκινώντας

Υπάρχουν μερικά βασικά παραδείγματα έτοιμα για να τα εκτελέσετε. Μπορείτε να τα βρείτε στον φάκελο samples. Αν θέλετε να ξεκινήσετε κατευθείαν με την αγαπημένη σας γλώσσα, μπορείτε να βρείτε τα παραδείγματα στις παρακάτω γλώσσες:

- Python
- JavaScript
- cURL

Υπάρχει επίσης ένα ειδικό περιβάλλον Codespaces για την εκτέλεση των δειγμάτων και των μοντέλων.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.el.png)

## Δείγματα Κώδικα

Παρακάτω θα βρείτε παραδείγματα κώδικα για μερικές περιπτώσεις χρήσης. Για περισσότερες πληροφορίες σχετικά με το Azure AI Inference SDK, δείτε την πλήρη τεκμηρίωση και τα δείγματα.

## Ρύθμιση

1. Δημιουργήστε ένα προσωπικό διακριτικό πρόσβασης
Δεν χρειάζεται να δώσετε καμία άδεια στο διακριτικό. Σημειώστε ότι το διακριτικό θα σταλεί σε μια υπηρεσία της Microsoft.

Για να χρησιμοποιήσετε τα παρακάτω αποσπάσματα κώδικα, δημιουργήστε μια μεταβλητή περιβάλλοντος για να ορίσετε το διακριτικό σας ως το κλειδί για τον κώδικα του πελάτη.

Αν χρησιμοποιείτε bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
Αν χρησιμοποιείτε powershell:

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

Αν χρησιμοποιείτε την εντολή prompt των Windows:

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Παράδειγμα Python

### Εγκατάσταση εξαρτήσεων
Εγκαταστήστε το Azure AI Inference SDK χρησιμοποιώντας pip (Απαιτείται: Python >=3.8):

```
pip install azure-ai-inference
```
### Εκτέλεση βασικού παραδείγματος κώδικα

Αυτό το παράδειγμα δείχνει μια βασική κλήση στο API ολοκλήρωσης συνομιλίας. Χρησιμοποιεί το GitHub AI model inference endpoint και το προσωπικό σας διακριτικό GitHub. Η κλήση είναι συγχρονισμένη.

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

### Εκτέλεση συνομιλίας πολλαπλών γύρων

Αυτό το παράδειγμα δείχνει μια συνομιλία πολλαπλών γύρων με το API ολοκλήρωσης συνομιλίας. Όταν χρησιμοποιείτε το μοντέλο για μια εφαρμογή συνομιλίας, θα χρειαστεί να διαχειριστείτε το ιστορικό της συνομιλίας και να στείλετε τα πιο πρόσφατα μηνύματα στο μοντέλο.

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

### Ροή εξόδου

Για καλύτερη εμπειρία χρήστη, μπορείτε να ρυθμίσετε τη ροή της απόκρισης του μοντέλου ώστε το πρώτο αποτέλεσμα να εμφανίζεται νωρίς και να αποφεύγετε την αναμονή για μεγάλες αποκρίσεις.

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

### Εγκατάσταση εξαρτήσεων

Εγκαταστήστε το Node.js.

Αντιγράψτε τις παρακάτω γραμμές κειμένου και αποθηκεύστε τις ως αρχείο package.json στον φάκελό σας.

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

Σημείωση: Το @azure/core-sse χρειάζεται μόνο όταν κάνετε ροή της απόκρισης των ολοκληρώσεων συνομιλίας.

Ανοίξτε ένα παράθυρο τερματικού σε αυτόν τον φάκελο και εκτελέστε npm install.

Για κάθε ένα από τα παρακάτω αποσπάσματα κώδικα, αντιγράψτε το περιεχόμενο σε ένα αρχείο sample.js και εκτελέστε το με την εντολή node sample.js.

### Εκτέλεση βασικού παραδείγματος κώδικα

Αυτό το παράδειγμα δείχνει μια βασική κλήση στο API ολοκλήρωσης συνομιλίας. Χρησιμοποιεί το GitHub AI model inference endpoint και το προσωπικό σας διακριτικό GitHub. Η κλήση είναι συγχρονισμένη.

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

### Εκτέλεση συνομιλίας πολλαπλών γύρων

Αυτό το παράδειγμα δείχνει μια συνομιλία πολλαπλών γύρων με το API ολοκλήρωσης συνομιλίας. Όταν χρησιμοποιείτε το μοντέλο για μια εφαρμογή συνομιλίας, θα χρειαστεί να διαχειριστείτε το ιστορικό της συνομιλίας και να στείλετε τα πιο πρόσφατα μηνύματα στο μοντέλο.

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

### Ροή εξόδου
Για καλύτερη εμπειρία χρήστη, μπορείτε να ρυθμίσετε τη ροή της απόκρισης του μοντέλου ώστε το πρώτο αποτέλεσμα να εμφανίζεται νωρίς και να αποφεύγετε την αναμονή για μεγάλες αποκρίσεις.

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

### Εκτέλεση βασικού παραδείγματος κώδικα

Επικολλήστε τα παρακάτω σε ένα shell:

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
### Εκτέλεση συνομιλίας πολλαπλών γύρων

Καλέστε το API ολοκλήρωσης συνομιλίας και περάστε το ιστορικό συνομιλίας:

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
### Ροή εξόδου

Αυτό είναι ένα παράδειγμα κλήσης του endpoint και ροής της απόκρισης.

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

## ΔΩΡΕΑΝ Χρήση και Όρια για τα GitHub Models

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.el.png)

Τα [όρια χρήσης για το playground και το δωρεάν API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) έχουν σχεδιαστεί για να σας βοηθήσουν να πειραματιστείτε με τα μοντέλα και να δημιουργήσετε πρωτότυπες εφαρμογές AI. Για χρήση πέρα από αυτά τα όρια, και για να κλιμακώσετε την εφαρμογή σας, πρέπει να προμηθευτείτε πόρους από έναν λογαριασμό Azure και να αυθεντικοποιηθείτε από εκεί αντί να χρησιμοποιείτε το προσωπικό σας διακριτικό GitHub. Δεν χρειάζεται να αλλάξετε τίποτα άλλο στον κώδικά σας. Χρησιμοποιήστε αυτόν τον σύνδεσμο για να μάθετε πώς να ξεπεράσετε τα όρια του δωρεάν επιπέδου στο Azure AI.

### Αποποιήσεις

Να θυμάστε ότι όταν αλληλεπιδράτε με ένα μοντέλο, πειραματίζεστε με την τεχνητή νοημοσύνη, επομένως είναι πιθανό να υπάρχουν λάθη στο περιεχόμενο.

Η δυνατότητα υπόκειται σε διάφορα όρια (συμπεριλαμβανομένων αιτημάτων ανά λεπτό, αιτημάτων ανά ημέρα, tokens ανά αίτημα και ταυτόχρονων αιτημάτων) και δεν είναι σχεδιασμένη για περιπτώσεις παραγωγικής χρήσης.

Τα GitHub Models χρησιμοποιούν το Azure AI Content Safety. Αυτά τα φίλτρα δεν μπορούν να απενεργοποιηθούν ως μέρος της εμπειρίας των GitHub Models. Αν αποφασίσετε να χρησιμοποιήσετε μοντέλα μέσω μιας επί πληρωμή υπηρεσίας, παρακαλούμε να ρυθμίσετε τα φίλτρα περιεχομένου σας ώστε να πληρούν τις απαιτήσεις σας.

Αυτή η υπηρεσία διέπεται από τους Όρους Προέκδοσης του GitHub.

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης βασισμένες σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.