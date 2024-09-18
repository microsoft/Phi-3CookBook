# Chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

## Aperçu

Le Chatbot interactif Phi 3 Mini 4K Instruct est un outil qui permet aux utilisateurs d'interagir avec la démo Microsoft Phi 3 Mini 4K instruct en utilisant une entrée texte ou audio. Le chatbot peut être utilisé pour diverses tâches, telles que la traduction, les mises à jour météo et la collecte d'informations générales.

### Pour commencer

Pour utiliser ce chatbot, suivez simplement ces instructions :

1. Ouvrez un nouveau [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Dans la fenêtre principale du notebook, vous verrez une interface de chat avec une boîte de saisie de texte et un bouton "Send".
3. Pour utiliser le chatbot basé sur le texte, tapez simplement votre message dans la boîte de saisie de texte et cliquez sur le bouton "Send". Le chatbot répondra avec un fichier audio qui peut être lu directement depuis le notebook.

**Note** : Cet outil nécessite un GPU et un accès aux modèles Microsoft Phi-3 et OpenAI Whisper, utilisés pour la reconnaissance vocale et la traduction.

### Exigences GPU

Pour exécuter cette démo, vous avez besoin de 12 Go de mémoire GPU.

Les exigences en mémoire pour exécuter la démo **Microsoft-Phi-3-Mini-4K instruct** sur un GPU dépendront de plusieurs facteurs, tels que la taille des données d'entrée (audio ou texte), la langue utilisée pour la traduction, la vitesse du modèle et la mémoire disponible sur le GPU.

En général, le modèle Whisper est conçu pour fonctionner sur des GPU. La quantité minimale recommandée de mémoire GPU pour exécuter le modèle Whisper est de 8 Go, mais il peut gérer des quantités de mémoire plus importantes si nécessaire.

Il est important de noter que l'exécution d'une grande quantité de données ou d'un volume élevé de requêtes sur le modèle peut nécessiter plus de mémoire GPU et/ou provoquer des problèmes de performance. Il est recommandé de tester votre cas d'utilisation avec différentes configurations et de surveiller l'utilisation de la mémoire pour déterminer les paramètres optimaux pour vos besoins spécifiques.

## Exemple E2E pour le Chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

Le notebook jupyter intitulé [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](../../../../md/06.E2ESamples/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) montre comment utiliser la démo Microsoft Phi 3 Mini 4K instruct pour générer du texte à partir d'une entrée audio ou texte. Le notebook définit plusieurs fonctions :

1. `tts_file_name(text)`: Cette fonction génère un nom de fichier basé sur le texte d'entrée pour enregistrer le fichier audio généré.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Cette fonction utilise l'API Edge TTS pour générer un fichier audio à partir d'une liste de morceaux de texte d'entrée. Les paramètres d'entrée sont la liste des morceaux, la vitesse de parole, le nom de la voix et le chemin de sortie pour enregistrer le fichier audio généré.
1. `talk(input_text)`: Cette fonction génère un fichier audio en utilisant l'API Edge TTS et l'enregistre sous un nom de fichier aléatoire dans le répertoire /content/audio. Le paramètre d'entrée est le texte d'entrée à convertir en parole.
1. `run_text_prompt(message, chat_history)`: Cette fonction utilise la démo Microsoft Phi 3 Mini 4K instruct pour générer un fichier audio à partir d'un message d'entrée et l'ajoute à l'historique du chat.
1. `run_audio_prompt(audio, chat_history)`: Cette fonction convertit un fichier audio en texte en utilisant l'API du modèle Whisper et le passe à la fonction `run_text_prompt()`.
1. Le code lance une application Gradio qui permet aux utilisateurs d'interagir avec la démo Phi 3 Mini 4K instruct en tapant des messages ou en téléchargeant des fichiers audio. Le résultat est affiché sous forme de message texte dans l'application.

## Dépannage

Installation des pilotes GPU Cuda

1. Assurez-vous que vos applications Linux sont à jour

    ```bash
    sudo apt update
    ```

1. Installez les pilotes Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Enregistrez l'emplacement du pilote cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Vérifiez la taille de la mémoire GPU Nvidia (12 Go de mémoire GPU requis)

    ```bash
    nvidia-smi
    ```

1. Videz le cache : Si vous utilisez PyTorch, vous pouvez appeler torch.cuda.empty_cache() pour libérer toute la mémoire mise en cache inutilisée afin qu'elle puisse être utilisée par d'autres applications GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Vérifiez Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Effectuez les tâches suivantes pour créer un jeton Hugging Face.

    - Accédez à la [page des paramètres des jetons Hugging Face](https://huggingface.co/settings/tokens).
    - Sélectionnez **New token**.
    - Entrez le **Nom** du projet que vous souhaitez utiliser.
    - Sélectionnez **Type** sur **Write**.

> **Note**
>
> Si vous rencontrez l'erreur suivante :
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pour résoudre ce problème, tapez la commande suivante dans votre terminal.
>
> ```bash
> sudo ldconfig
> ```

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.