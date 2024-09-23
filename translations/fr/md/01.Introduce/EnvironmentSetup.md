# Commencer avec Phi-3 en local

Ce guide vous aidera à configurer votre environnement local pour exécuter le modèle Phi-3 en utilisant Ollama. Vous pouvez exécuter le modèle de différentes manières, y compris en utilisant GitHub Codespaces, les conteneurs de développement VS Code, ou votre environnement local.

## Configuration de l'environnement

### GitHub Codespaces

Vous pouvez exécuter ce modèle virtuellement en utilisant GitHub Codespaces. Le bouton ouvrira une instance de VS Code basée sur le web dans votre navigateur :

1. Ouvrez le modèle (cela peut prendre plusieurs minutes) :

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. Ouvrez une fenêtre de terminal

### Conteneurs de développement VS Code

⚠️ Cette option ne fonctionnera que si votre Docker Desktop dispose d'au moins 16 Go de RAM. Si vous avez moins de 16 Go de RAM, vous pouvez essayer l'[option GitHub Codespaces](../../../../md/01.Introduce) ou [le configurer localement](../../../../md/01.Introduce).

Une option similaire est les conteneurs de développement VS Code, qui ouvriront le projet dans votre VS Code local en utilisant l'[extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) :

1. Démarrez Docker Desktop (installez-le s'il n'est pas déjà installé)
2. Ouvrez le projet :

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. Dans la fenêtre VS Code qui s'ouvre, une fois que les fichiers du projet apparaissent (cela peut prendre plusieurs minutes), ouvrez une fenêtre de terminal.
4. Continuez avec les [étapes de déploiement](../../../../md/01.Introduce)

### Environnement local

1. Assurez-vous que les outils suivants sont installés :

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## Tester le modèle

1. Demandez à Ollama de télécharger et d'exécuter le modèle phi3:mini :

    ```shell
    ollama run phi3:mini
    ```

    Cela prendra quelques minutes pour télécharger le modèle.

2. Une fois que vous voyez "success" dans la sortie, vous pouvez envoyer un message à ce modèle depuis l'invite.

    ```shell
    >>> Écris un haïku sur les hippopotames affamés
    ```

3. Après plusieurs secondes, vous devriez voir une réponse du modèle.

4. Pour en savoir plus sur les différentes techniques utilisées avec les modèles de langage, ouvrez le notebook Python [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb) et exécutez chaque cellule. Si vous avez utilisé un modèle autre que 'phi3:mini', changez le `MODEL_NAME` dans la première cellule.

5. Pour avoir une conversation avec le modèle phi3:mini depuis Python, ouvrez le fichier Python [chat.py](../../../../code/01.Introduce/chat.py) et exécutez-le. Vous pouvez changer le `MODEL_NAME` en haut du fichier si nécessaire, et vous pouvez également modifier le message système ou ajouter des exemples few-shot si vous le souhaitez.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.