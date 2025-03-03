# Chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

## Aperçu

Le chatbot interactif Phi 3 Mini 4K Instruct est un outil permettant aux utilisateurs d'interagir avec la démo Microsoft Phi 3 Mini 4K instruct via une saisie textuelle ou audio. Ce chatbot peut être utilisé pour diverses tâches, telles que la traduction, les mises à jour météo et la recherche d'informations générales.

### Pour commencer

Pour utiliser ce chatbot, suivez simplement ces instructions :

1. Ouvrez un nouveau fichier [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Dans la fenêtre principale du notebook, vous verrez une interface de chat avec une boîte de saisie texte et un bouton "Envoyer".
3. Pour utiliser le chatbot textuel, tapez simplement votre message dans la boîte de saisie texte et cliquez sur le bouton "Envoyer". Le chatbot répondra avec un fichier audio qui peut être lu directement depuis le notebook.

**Remarque** : Cet outil nécessite un GPU et l'accès aux modèles Microsoft Phi-3 et OpenAI Whisper, utilisés pour la reconnaissance vocale et la traduction.

### Exigences GPU

Pour exécuter cette démo, vous avez besoin de 12 Go de mémoire GPU.

Les exigences en mémoire pour exécuter la démo **Microsoft-Phi-3-Mini-4K instruct** sur un GPU dépendront de plusieurs facteurs, tels que la taille des données d'entrée (audio ou texte), la langue utilisée pour la traduction, la vitesse du modèle et la mémoire disponible sur le GPU.

En général, le modèle Whisper est conçu pour fonctionner sur des GPU. La quantité minimale recommandée de mémoire GPU pour exécuter le modèle Whisper est de 8 Go, mais il peut gérer des quantités de mémoire plus importantes si nécessaire.

Il est important de noter que le traitement d'une grande quantité de données ou d'un volume élevé de requêtes peut nécessiter davantage de mémoire GPU et/ou entraîner des problèmes de performance. Il est recommandé de tester votre cas d'utilisation avec différentes configurations et de surveiller l'utilisation de la mémoire afin de déterminer les paramètres optimaux pour vos besoins spécifiques.

## Exemple E2E pour le chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

Le notebook Jupyter intitulé [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) montre comment utiliser la démo Microsoft Phi 3 Mini 4K instruct pour générer du texte à partir d'une saisie audio ou textuelle. Le notebook définit plusieurs fonctions :

1. `tts_file_name(text)` : Cette fonction génère un nom de fichier basé sur le texte d'entrée pour enregistrer le fichier audio généré.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)` : Cette fonction utilise l'API Edge TTS pour générer un fichier audio à partir d'une liste de segments de texte d'entrée. Les paramètres d'entrée incluent la liste des segments, la vitesse de parole, le nom de la voix et le chemin de sortie pour enregistrer le fichier audio généré.
1. `talk(input_text)` : Cette fonction génère un fichier audio en utilisant l'API Edge TTS et l'enregistre sous un nom de fichier aléatoire dans le répertoire /content/audio. Le paramètre d'entrée est le texte à convertir en parole.
1. `run_text_prompt(message, chat_history)` : Cette fonction utilise la démo Microsoft Phi 3 Mini 4K instruct pour générer un fichier audio à partir d'un message d'entrée et l'ajoute à l'historique du chat.
1. `run_audio_prompt(audio, chat_history)` : Cette fonction convertit un fichier audio en texte en utilisant l'API du modèle Whisper et le transmet à la fonction `run_text_prompt()`.
1. Le code lance une application Gradio permettant aux utilisateurs d'interagir avec la démo Phi 3 Mini 4K instruct en saisissant des messages ou en téléchargeant des fichiers audio. Le résultat est affiché sous forme de message texte dans l'application.

## Résolution des problèmes

Installation des pilotes GPU Cuda

1. Assurez-vous que vos applications Linux sont à jour.

    ```bash
    sudo apt update
    ```

1. Installez les pilotes Cuda.

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Enregistrez l'emplacement du pilote Cuda.

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Vérifiez la taille de la mémoire GPU Nvidia (12 Go de mémoire GPU requis).

    ```bash
    nvidia-smi
    ```

1. Videz le cache : Si vous utilisez PyTorch, vous pouvez appeler torch.cuda.empty_cache() pour libérer toute mémoire cache inutilisée afin qu'elle puisse être utilisée par d'autres applications GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Vérifiez Cuda Nvidia.

    ```bash
    nvcc --version
    ```

1. Effectuez les tâches suivantes pour créer un jeton Hugging Face.

    - Accédez à la [page des paramètres des jetons Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Sélectionnez **Nouveau jeton**.
    - Entrez le **Nom** du projet que vous souhaitez utiliser.
    - Sélectionnez **Type** sur **Écriture**.

> **Remarque**
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

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.