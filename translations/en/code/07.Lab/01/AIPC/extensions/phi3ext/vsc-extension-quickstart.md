# Welcome to your VS Code Extension

## What's in the folder

* This folder contains all the files you need for your extension.
* `package.json` - this is the manifest file where you declare your extension and command.
  * The sample plugin registers a command and specifies its title and command name. With this information, VS Code can display the command in the command palette. At this stage, the plugin doesn’t need to be loaded yet.
* `src/extension.ts` - this is the main file where the implementation of your command is defined.
  * The file exports a function, `activate`, which gets called the first time your extension is activated (in this case, when the command is executed). Inside the `activate` function, we call `registerCommand`.
  * The function containing the command's implementation is passed as the second parameter to `registerCommand`.

## Setup

* Install the recommended extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, and dbaeumer.vscode-eslint).

## Get up and running straight away

* Press `F5` to open a new window with your extension loaded.
* Run your command from the command palette by pressing (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and typing `Hello World`.
* Set breakpoints in your code inside `src/extension.ts` to debug your extension.
* View the output from your extension in the debug console.

## Make changes

* After making changes to the code in `src/extension.ts`, you can relaunch the extension from the debug toolbar.
* Alternatively, you can reload the VS Code window (`Ctrl+R` or `Cmd+R` on Mac) to apply your changes.

## Explore the API

* You can access the complete API documentation by opening the file `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Install the [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Use the **Tasks: Run Task** command to start the "watch" task. Ensure this is running; otherwise, tests may not be detected.
* Open the Testing view from the activity bar and click the "Run Test" button, or use the shortcut `Ctrl/Cmd + ; A`.
* Check the test results in the Test Results view.
* Modify `src/test/extension.test.ts` or add new test files in the `test` folder.
  * The test runner only recognizes files matching the pattern `**.test.ts`.
  * You can organize your tests by creating subfolders within the `test` folder.

## Go further

* Optimize your extension's size and startup time by [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) to the VS Code extension marketplace.
* Set up [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) to automate builds.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.