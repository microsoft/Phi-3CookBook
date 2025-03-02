# Welcome to your VS Code Extension

## What's in the folder

* This folder contains all the files needed for your extension.
* `package.json` - this is the manifest file where you declare your extension and command.
  * The sample extension registers a command and defines its title and command name. With this information, VS Code can display the command in the command palette. It doesn't need to load the extension yet.
* `src/extension.ts` - this is the main file where you implement your command.
  * The file exports a function, `activate`, which is called the first time your extension is activated (in this case, when the command is executed). Inside the `activate` function, we call `registerCommand`.
  * We pass the function containing the command implementation as the second parameter to `registerCommand`.

## Setup

* Install the recommended extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, and dbaeumer.vscode-eslint).

## Get up and running straight away

* Press `F5` to open a new window with your extension loaded.
* Run your command from the command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `Hello World`.
* Set breakpoints in your code inside `src/extension.ts` to debug your extension.
* Find your extension's output in the debug console.

## Make changes

* You can relaunch the extension from the debug toolbar after making changes to `src/extension.ts`.
* You can also reload (`Ctrl+R` or `Cmd+R` on Mac) the VS Code window with your extension to apply your changes.

## Explore the API

* You can access the complete API documentation by opening the file `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Install the [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Run the "watch" task using the **Tasks: Run Task** command. Ensure this is running; otherwise, tests may not be detected.
* Open the Testing view from the activity bar and click the "Run Test" button, or use the hotkey `Ctrl/Cmd + ; A`.
* View the test results in the Test Results view.
* Modify `src/test/extension.test.ts` or create new test files in the `test` folder.
  * The test runner only considers files that match the pattern `**.test.ts`.
  * You can create subfolders within the `test` folder to organize your tests however you like.

## Go further

* Reduce the size of your extension and improve its startup time by [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) to the VS Code extension marketplace.
* Automate builds by setting up [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.