# Terrain de jeu Ollama C#

Ce laboratoire est conçu pour tester Phi-3 avec des exemples en C# directement dans GitHub Codespaces, offrant ainsi une manière simple pour tout le monde d'essayer les SLMs (petits modèles de langage) entièrement dans le navigateur.

## Comment créer le Codespace C# + Ollama + Phi-3

1. Créez un nouveau Codespace en utilisant le bouton `Code` en haut du dépôt. Sélectionnez [+ New with options ...]
![Créer un Codespace avec options](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.fr.png)

1. Depuis la page des options, sélectionnez la configuration nommée `Ollama with Phi-3 for C#`

![Sélectionner l'option Ollama with Phi-3 for C#, pour créer le Codespace](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.fr.png)

1. Une fois le Codespace chargé, il devrait avoir [ollama](https://ollama.com/) pré-installé, le dernier modèle Phi-3 téléchargé, et [.NET 8](https://dotnet.microsoft.com/download) installé.

1. (Optionnel) Utilisez le terminal du Codespace pour demander à Ollama d'exécuter le modèle [phi3](https://ollama.com/library/phi3) :

    ```shell
    ollama run phi3
    ```

4. Vous pouvez envoyer un message à ce modèle depuis l'invite.

    ```shell
    >>> Write a joke about kittens
    ```

5. Après plusieurs secondes, vous devriez voir une réponse en provenance du modèle.

    ![exécuter ollama et demander une blague](../../../../../md/07.Labs/CsharpOllamaCodeSpaces/20ollamarunphi.gif)

1. Pour en savoir plus sur les différentes techniques utilisées avec les modèles de langage, consultez les projets d'exemples dans le dossier `.\src` :

| Projet | Description |
|--------|-------------|
| Sample01  | C'est un projet exemple qui utilise le modèle Phi-3 hébergé dans Ollama pour répondre à une question.  |
| Sample02  | C'est un projet exemple qui implémente un chat de console utilisant Semantic Kernel. |
| [Sample03](./src/Sample03/readme.md)  | C'est un projet exemple qui implémente un RAG en utilisant des embeddings locaux et Semantic Kernel. Consultez les détails du RAG local [ici](./src/Sample03/readme.md) |

## Comment exécuter un exemple

1. Ouvrez un terminal et naviguez vers le projet souhaité. Par exemple, exécutons `Sample02`, le chat de console.

    ```bash
    cd .\src\Sample02\
    ```

1. Exécutez le projet avec la commande

    ```bash
    dotnet run
    ```

1. Le projet `Sample02` définit un message système personnalisé :

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

    ```

1. Ainsi, lorsque l'utilisateur pose une question, comme `What is the capital of Italy?`, le chat répond en utilisant le mode local.
   
    La sortie est similaire à celle-ci :

    ![Démo de chat en cours d'exécution](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.fr.png)

## Tutoriels vidéo

Si vous souhaitez en savoir plus sur l'utilisation de Codespaces avec Ollama dans un dépôt GitHub, consultez la vidéo de 3 minutes suivante :

[![Regarder la vidéo](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.fr.jpg)](https://youtu.be/HmKpHErUEHM)

