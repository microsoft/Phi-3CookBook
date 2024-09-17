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
