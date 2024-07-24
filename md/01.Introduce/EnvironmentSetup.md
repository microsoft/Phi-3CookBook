# Opening the project

We have provided a Ollama Python Playground

This project is designed to be opened in GitHub Codespaces as an easy way for anyone to try out SLMs (small language models) entirely in the browser.

1. Open the Codespace in the browser using the `Code` button at the top of the repository.
2. Once the Codespace is loaded, it should have [ollama](https://ollama.com/).
3. Ask Ollama to run the SLM of your choice. For example, to run the [phi3](https://ollama.com/library/phi3) model:

    ```shell
    ollama run phi3:mini
    ```

    That will take a few minutes to download the model into the Codespace.
4. Once you see "success" in the output, you can send a message to that model from the prompt.

    ```shell
    >>> Write a haiku about hungry hippos
    ```

5. After several seconds, you should see a response stream in from the model.
6. To learn about different techniques used with language models, open the Python notebook `ollama.ipynb` and run each cell . If you used a model other than 'phi3:mini', change the `MODEL_NAME` in the first cell.
7. To have a conversation with a model from Python, open the Python file `chat.py` and run it. You can change the `MODEL_NAME` at the top of the file as needed, and you can also modify the system message or add few-shot examples if desired.

You have a few options for getting started with this template.
The quickest way to get started is GitHub Codespaces, since it will setup all the tools for you, but you can also [set it up locally](#local-environment).

## GitHub Codespaces

You can run this template virtually by using GitHub Codespaces. The button will open a web-based VS Code instance in your browser:

1. Open the template (this may take several minutes):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. Open a terminal window
3. Continue with the [deployment steps](#deployment)

## VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. In the VS Code window that opens, once the project files show up (this may take several minutes), open a terminal window.
4. Continue with the [deployment steps](#deployment)

## Local Environment

1. Make sure the following tools are installed:

    * [Python 3.10+](https://www.python.org/downloads/)
    * [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    * [Git](https://git-scm.com/downloads)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

2. Open the project folder

3. Install OpenAI Python Library:

    ```shell
    pip install openai
    ```
