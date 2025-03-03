# **Kreirajte sopstvenog Visual Studio Code Chat Copilot Agenta sa Phi-3.5 pomoću GitHub Modela**

Da li koristite Visual Studio Code Copilot? Posebno u okviru Chat-a, možete koristiti različite agente kako biste unapredili sposobnosti kreiranja, pisanja i održavanja projekata u Visual Studio Code-u. Visual Studio Code pruža API koji omogućava kompanijama i pojedincima da kreiraju različite agente bazirane na svojim poslovnim potrebama, čime proširuju mogućnosti u različitim specifičnim oblastima. U ovom članku ćemo se fokusirati na **Phi-3.5-mini-instruct (128k)** i **Phi-3.5-vision-instruct (128k)** GitHub Modela kako bismo kreirali sopstvenog Visual Studio Code Agenta.

## **O Phi-3.5 u okviru GitHub Modela**

Znamo da Phi-3/3.5-mini-instruct iz porodice Phi-3/3.5 ima snažne sposobnosti razumevanja i generisanja koda, te prednosti u odnosu na Gemma-2-9b i Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.sr.png)

Najnoviji GitHub Modeli već omogućavaju pristup modelima Phi-3.5-mini-instruct (128k) i Phi-3.5-vision-instruct (128k). Programeri im mogu pristupiti putem OpenAI SDK-a, Azure AI Inference SDK-a i REST API-ja.

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.sr.png)

***Napomena:*** Preporučuje se korišćenje Azure AI Inference SDK-a, jer omogućava lakšu integraciju sa Azure Model Catalog-om u produkcionom okruženju.

U nastavku su prikazani rezultati **Phi-3.5-mini-instruct (128k)** i **Phi-3.5-vision-instruct (128k)** u scenarijima generisanja koda nakon povezivanja sa GitHub Modelima, kao i priprema za sledeće primere.

**Demo: GitHub Modeli Phi-3.5-mini-instruct (128k) generišu kod iz Prompt-a** ([kliknite ovde](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Modeli Phi-3.5-vision-instruct (128k) generišu kod iz slike** ([kliknite ovde](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **O GitHub Copilot Chat Agent-u**

GitHub Copilot Chat Agent može izvršavati različite zadatke u različitim projektima na osnovu koda. Sistem ima četiri agenta: workspace, github, terminal, vscode.

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.sr.png)

Dodavanjem imena agenta sa ‘@’, brzo možete završiti odgovarajući posao. Za preduzeća, ako dodate sopstvene poslovno specifične sadržaje kao što su zahtevi, kodiranje, specifikacije testiranja i objavljivanje, možete dobiti moćnije privatne funkcije zasnovane na GitHub Copilot-u.

Visual Studio Code Chat Agent je sada zvanično objavio svoj API, omogućavajući preduzećima ili programerima da razvijaju agente zasnovane na različitim poslovnim ekosistemima softvera. Na osnovu metode razvoja Visual Studio Code Extension-a, lako možete pristupiti interfejsu Visual Studio Code Chat Agent API-ja. Razvoj se može zasnivati na ovom procesu.

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.sr.png)

Scenariji razvoja podržavaju pristup API-jima trećih modela (kao što su GitHub Modeli, Azure Model Catalog i usluge zasnovane na otvorenim modelima) i takođe omogućavaju korišćenje modela gpt-35-turbo, gpt-4 i gpt-4o koje pruža GitHub Copilot.

## **Dodavanje Agenta @phicoding zasnovanog na Phi-3.5**

Pokušavamo da integrišemo programerske sposobnosti Phi-3.5 za izvršavanje zadataka poput pisanja koda, generisanja koda iz slika i drugih zadataka. Kreiraćemo Agenta zasnovanog na Phi-3.5 - @PHI, sa sledećim funkcijama:

1. Generisanje samoupoznavanja pomoću GPT-4o koji pruža GitHub Copilot preko komande **@phicoding /help**.

2. Generisanje koda za različite programske jezike pomoću **Phi-3.5-mini-instruct (128k)** preko komande **@phicoding /gen**.

3. Generisanje koda i dopunjavanje slika pomoću **Phi-3.5-vision-instruct (128k)** preko komande **@phicoding /image**.

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.sr.png)

## **Povezani koraci**

1. Instalirajte podršku za razvoj Visual Studio Code Extension-a koristeći npm.

```bash

npm install --global yo generator-code 

```
2. Kreirajte Visual Studio Code Extension plugin (koristeći Typescript razvojni režim, nazvan phiext).

```bash

yo code 

```

3. Otvorite kreirani projekat i modifikujte package.json. Ovde se nalaze uputstva i konfiguracije, kao i konfiguracija za GitHub Model-e. Napomena: potrebno je dodati svoj GitHub Models token.

```json

{
  "name": "phiext",
  "displayName": "phiext",
  "description": "",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.93.0"
  },
  "categories": [
    "AI",
    "Chat"
  ],
  "activationEvents": [],
  "enabledApiProposals": [
      "chatVariableResolver"
  ],
  "main": "./dist/extension.js",
  "contributes": {
    "chatParticipants": [
        {
            "id": "chat.phicoding",
            "name": "phicoding",
            "description": "Hey! I am Microsoft Phi-3.5, She can help me with coding problems, such as generation code with your natural language, or even generation code about chart from images. Just ask me anything!",
            "isSticky": true,
            "commands": [
                {
                    "name": "help",
                    "description": "Introduce myself to you"
                },
                {
                    "name": "gen",
                    "description": "Generate code for you with Microsoft Phi-3.5-mini-instruct"
                },
                {
                    "name": "image",
                    "description": "Generate code for chart from image(png or jpg) with Microsoft Phi-3.5-vision-instruct, please add image url like this : https://ajaytech.co/wp-content/uploads/2019/09/index.png"
                }
            ]
        }
    ],
    "commands": [
        {
            "command": "phicoding.namesInEditor",
            "title": "Use Microsoft Phi 3.5 in Editor"
        }
    ],
    "configuration": {
      "type": "object",
      "title": "githubmodels",
      "properties": {
        "githubmodels.endpoint": {
          "type": "string",
          "default": "https://models.inference.ai.azure.com",
          "description": "Your GitHub Models Endpoint",
          "order": 0
        },
        "githubmodels.api_key": {
          "type": "string",
          "default": "Your GitHub Models Token",
          "description": "Your GitHub Models Token",
          "order": 1
        },
        "githubmodels.phi35instruct": {
          "type": "string",
          "default": "Phi-3.5-mini-instruct",
          "description": "Your Phi-35-Instruct Model",
          "order": 2
        },
        "githubmodels.phi35vision": {
          "type": "string",
          "default": "Phi-3.5-vision-instruct",
          "description": "Your Phi-35-Vision Model",
          "order": 3
        }
      }
    }
  },
  "scripts": {
    "vscode:prepublish": "npm run package",
    "compile": "webpack",
    "watch": "webpack --watch",
    "package": "webpack --mode production --devtool hidden-source-map",
    "compile-tests": "tsc -p . --outDir out",
    "watch-tests": "tsc -p . -w --outDir out",
    "pretest": "npm run compile-tests && npm run compile && npm run lint",
    "lint": "eslint src",
    "test": "vscode-test"
  },
  "devDependencies": {
    "@types/vscode": "^1.93.0",
    "@types/mocha": "^10.0.7",
    "@types/node": "20.x",
    "@typescript-eslint/eslint-plugin": "^8.3.0",
    "@typescript-eslint/parser": "^8.3.0",
    "eslint": "^9.9.1",
    "typescript": "^5.5.4",
    "ts-loader": "^9.5.1",
    "webpack": "^5.94.0",
    "webpack-cli": "^5.1.4",
    "@vscode/test-cli": "^0.0.10",
    "@vscode/test-electron": "^2.4.1"
  },
  "dependencies": {
    "@types/node-fetch": "^2.6.11",
    "node-fetch": "^3.3.2",
    "@azure-rest/ai-inference": "latest",
    "@azure/core-auth": "latest",
    "@azure/core-sse": "latest"
  }
}


```

4. Modifikujte src/extension.ts.

```typescript

// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";


interface IPhiChatResult extends vscode.ChatResult {
    metadata: {
        command: string;
    };
}


const MODEL_SELECTOR: vscode.LanguageModelChatSelector = { vendor: 'copilot', family: 'gpt-4o' };

function isValidImageUrl(url: string): boolean {
    const regex = /^(https?:\/\/.*\.(?:png|jpg))$/i;
    return regex.test(url);
}
  

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

    const codinghandler: vscode.ChatRequestHandler = async (request: vscode.ChatRequest, context: vscode.ChatContext, stream: vscode.ChatResponseStream, token: vscode.CancellationToken): Promise<IPhiChatResult> => {


        const config : any = vscode.workspace.getConfiguration('githubmodels');
        const endPoint: string = config.get('endpoint');
        const apiKey: string = config.get('api_key');
        const phi35instruct: string = config.get('phi35instruct');
        const phi35vision: string = config.get('phi35vision');
        
        if (request.command === 'help') {

            const content = "Welcome to Coding assistant with Microsoft Phi-3.5"; 
            stream.progress(content);


            try {
                const [model] = await vscode.lm.selectChatModels(MODEL_SELECTOR);
                if (model) {
                    const messages = [
                        vscode.LanguageModelChatMessage.User("Please help me express this content in a humorous way: I am a programming assistant who can help you convert natural language into code and generate code based on the charts in the images. output format like this : Hey I am Phi ......")
                    ];
                    const chatResponse = await model.sendRequest(messages, {}, token);
                    for await (const fragment of chatResponse.text) {
                        stream.markdown(fragment);
                    }
                }
            } catch(err) {
                console.log(err);
            }


            return { metadata: { command: 'help' } };

        }

        
        if (request.command === 'gen') {

            const content = "Welcome to use phi-3.5 to generate code";

            stream.progress(content);

            const client = new ModelClient(endPoint, new AzureKeyCredential(apiKey));

            const response = await client.path("/chat/completions").post({
              body: {
                messages: [
                  { role:"system", content: "You are a coding assistant.Help answer all code generation questions." },
                  { role:"user", content: request.prompt }
                ],
                model: phi35instruct,
                temperature: 0.4,
                max_tokens: 1000,
                top_p: 1.
              }
            });

            stream.markdown(response.body.choices[0].message.content);

            return { metadata: { command: 'gen' } };

        }



        
        if (request.command === 'image') {


            const content = "Welcome to use phi-3.5 to generate code from image(png or jpg),image url like this:https://ajaytech.co/wp-content/uploads/2019/09/index.png";

            stream.progress(content);

            if (!isValidImageUrl(request.prompt)) {
                stream.markdown('Please provide a valid image URL');
                return { metadata: { command: 'image' } };
            }
            else
            {

                const client = new ModelClient(endPoint, new AzureKeyCredential(apiKey));
    
                const response = await client.path("/chat/completions").post({
                    body: {
                      messages: [
                        { role: "system", content: "You are a helpful assistant that describes images in details." },
                        { role: "user", content: [
                            { type: "text", text: "Please generate code according to the chart in the picture according to the following requirements\n1. Keep all information in the chart, including data and text\n2. Do not generate additional information that is not included in the chart\n3. Please extract data from the picture, do not generate it from csv\n4. Please save the regenerated chart as a chart and save it to ./output/demo.png"},
                            { type: "image_url", image_url: {url: request.prompt}
                            }
                          ]
                        }
                      ],
                      model: phi35vision,
                      temperature: 0.4,
                      max_tokens: 2048,
                      top_p: 1.
                    }
                  });
    
                
                stream.markdown(response.body.choices[0].message.content);
    
                return { metadata: { command: 'image' } };
            }



        }


        return { metadata: { command: '' } };
    };


    const phi_ext = vscode.chat.createChatParticipant("chat.phicoding", codinghandler);

    phi_ext.iconPath = new vscode.ThemeIcon('sparkle');


    phi_ext.followupProvider = {
        provideFollowups(result: IPhiChatResult, context: vscode.ChatContext, token: vscode.CancellationToken) {
            return [{
                prompt: 'Let us coding with Phi-3.5 😋😋😋😋',
                label: vscode.l10n.t('Enjoy coding with Phi-3.5'),
                command: 'help'
            } satisfies vscode.ChatFollowup];
        }
    };

    context.subscriptions.push(phi_ext);
}

// This method is called when your extension is deactivated
export function deactivate() {}


```

6. Pokretanje.

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.sr.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.sr.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.sr.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.sr.png)

Možete preuzeti uzorak koda: [kliknite ovde](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Resursi**

1. Prijavite se na GitHub Model-e [https://gh.io/models](https://gh.io/models)

2. Naučite razvoj Visual Studio Code Extension-a [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Naučite o Visual Studio Code Copilot Chat API-ju [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских услуга превођења заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, имајте на уму да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неразумевања која могу произаћи из коришћења овог превода.