# **Crie seu próprio Agente Visual Studio Code Chat Copilot com Phi-3.5 dos Modelos GitHub**

Você utiliza o Visual Studio Code Copilot? Especialmente no Chat, você pode usar diferentes agentes para melhorar a capacidade de criar, escrever e manter projetos no Visual Studio Code. O Visual Studio Code oferece uma API que permite a empresas e indivíduos criarem diferentes agentes com base em seus negócios, expandindo suas capacidades em áreas proprietárias específicas. Neste artigo, focaremos nos modelos **Phi-3.5-mini-instruct (128k)** e **Phi-3.5-vision-instruct (128k)** dos Modelos GitHub para criar seu próprio Agente Visual Studio Code.

## **Sobre o Phi-3.5 nos Modelos GitHub**

Sabemos que o Phi-3/3.5-mini-instruct da Família Phi-3/3.5 possui fortes capacidades de entendimento e geração de código, com vantagens em relação ao Gemma-2-9b e Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.pt.png)

Os Modelos GitHub mais recentes já oferecem acesso aos modelos Phi-3.5-mini-instruct (128k) e Phi-3.5-vision-instruct (128k). Os desenvolvedores podem acessá-los por meio do OpenAI SDK, Azure AI Inference SDK e REST API.

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.pt.png)

***Nota:*** Recomenda-se o uso do Azure AI Inference SDK aqui, pois ele permite uma melhor integração com o Azure Model Catalog em ambientes de produção.

A seguir estão os resultados do **Phi-3.5-mini-instruct (128k)** e do **Phi-3.5-vision-instruct (128k)** no cenário de geração de código após a integração com os Modelos GitHub, preparando o terreno para os exemplos a seguir.

**Demo: Modelos GitHub Phi-3.5-mini-instruct (128k) gerando código a partir de um Prompt** ([clique neste link](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: Modelos GitHub Phi-3.5-vision-instruct (128k) gerando código a partir de uma Imagem** ([clique neste link](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **Sobre o GitHub Copilot Chat Agent**

O GitHub Copilot Chat Agent pode realizar diferentes tarefas em diversos cenários de projeto com base no código. O sistema possui quatro agentes: workspace, github, terminal, vscode.

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.pt.png)

Adicionando o nome do agente com ‘@’, você pode rapidamente completar a tarefa correspondente. Para empresas, se você adicionar conteúdos relacionados ao seu negócio, como requisitos, codificação, especificações de teste e lançamento, é possível obter funções privadas empresariais mais poderosas com base no GitHub Copilot.

O Visual Studio Code Chat Agent já lançou oficialmente sua API, permitindo que empresas ou desenvolvedores corporativos criem agentes baseados em diferentes ecossistemas de software. Com base no método de desenvolvimento de Extensões do Visual Studio Code, você pode acessar facilmente a interface da API do Visual Studio Code Chat Agent. Podemos desenvolver seguindo este processo:

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.pt.png)

O cenário de desenvolvimento pode suportar o acesso a APIs de modelos de terceiros (como os Modelos GitHub, Azure Model Catalog e serviços próprios baseados em modelos de código aberto) e também utilizar os modelos gpt-35-turbo, gpt-4 e gpt-4o fornecidos pelo GitHub Copilot.

## **Adicionar um Agente @phicoding baseado no Phi-3.5**

Tentamos integrar as capacidades de programação do Phi-3.5 para realizar tarefas como escrita de código, geração de código a partir de imagens, entre outras. Criamos um Agente baseado no Phi-3.5 - @PHI. A seguir estão algumas de suas funções:

1. Gerar uma autoapresentação com base no GPT-4o fornecido pelo GitHub Copilot por meio do comando **@phicoding /help**.

2. Gerar código para diferentes linguagens de programação com base no **Phi-3.5-mini-instruct (128k)** por meio do comando **@phicoding /gen**.

3. Gerar código com base no **Phi-3.5-vision-instruct (128k)** e completar imagens por meio do comando **@phicoding /image**.

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.pt.png)

## **Passos Relacionados**

1. Instale o suporte para desenvolvimento de Extensões do Visual Studio Code usando npm.

```bash

npm install --global yo generator-code 

```

2. Crie um plugin de Extensão para o Visual Studio Code (usando o modo de desenvolvimento em Typescript, nomeado como phiext).

```bash

yo code 

```

3. Abra o projeto criado e modifique o arquivo package.json. Aqui estão as instruções e configurações relacionadas, além da configuração dos Modelos GitHub. Observe que você precisará adicionar o token dos Modelos GitHub.

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

4. Modifique o arquivo src/extension.ts.

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

6. Executando

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.pt.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.pt.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.pt.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.pt.png)

Você pode baixar o código de exemplo: [clique aqui](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Recursos**

1. Cadastre-se nos Modelos GitHub [https://gh.io/models](https://gh.io/models)

2. Aprenda sobre Desenvolvimento de Extensões no Visual Studio Code [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Saiba mais sobre a API do Visual Studio Code Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Aviso Legal**:  
Este documento foi traduzido usando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.