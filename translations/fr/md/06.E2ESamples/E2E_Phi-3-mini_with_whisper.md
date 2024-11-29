# Chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

## Vue d'ensemble

Le chatbot interactif Phi 3 Mini 4K Instruct est un outil qui permet aux utilisateurs d'interagir avec la démonstration Microsoft Phi 3 Mini 4K Instruct en utilisant des entrées textuelles ou audio. Le chatbot peut être utilisé pour diverses tâches, telles que la traduction, les mises à jour météorologiques et la collecte d'informations générales.

### Pour commencer

Pour utiliser ce chatbot, suivez simplement ces instructions :

1. Ouvrez un nouveau [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Dans la fenêtre principale du notebook, vous verrez une interface de chat avec une boîte de saisie de texte et un bouton "Envoyer".
3. Pour utiliser le chatbot basé sur du texte, tapez simplement votre message dans la boîte de saisie de texte et cliquez sur le bouton "Envoyer". Le chatbot répondra avec un fichier audio qui peut être lu directement depuis le notebook.

**Note**: Cet outil nécessite un GPU et un accès aux modèles Microsoft Phi-3 et OpenAI Whisper, utilisés pour la reconnaissance vocale et la traduction.

### Exigences GPU

Pour exécuter cette démonstration, vous avez besoin de 12 Go de mémoire GPU.

Les exigences en mémoire pour exécuter la démonstration **Microsoft-Phi-3-Mini-4K instruct** sur un GPU dépendent de plusieurs facteurs, tels que la taille des données d'entrée (audio ou texte), la langue utilisée pour la traduction, la vitesse du modèle et la mémoire disponible sur le GPU.

En général, le modèle Whisper est conçu pour fonctionner sur des GPU. La quantité minimale recommandée de mémoire GPU pour exécuter le modèle Whisper est de 8 Go, mais il peut gérer des quantités plus importantes de mémoire si nécessaire.

Il est important de noter que l'exécution d'une grande quantité de données ou d'un volume élevé de requêtes sur le modèle peut nécessiter plus de mémoire GPU et/ou causer des problèmes de performance. Il est recommandé de tester votre cas d'utilisation avec différentes configurations et de surveiller l'utilisation de la mémoire pour déterminer les paramètres optimaux pour vos besoins spécifiques.

## Exemple E2E pour le chatbot interactif Phi 3 Mini 4K Instruct avec Whisper

Le notebook jupyter intitulé [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) montre comment utiliser la démonstration Microsoft Phi 3 Mini 4K Instruct pour générer du texte à partir d'une entrée audio ou textuelle. Le notebook définit plusieurs fonctions :

1. `tts_file_name(text)` : Cette fonction génère un nom de fichier basé sur le texte d'entrée pour enregistrer le fichier audio généré.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)` : Cette fonction utilise l'API Edge TTS pour générer un fichier audio à partir d'une liste de morceaux de texte d'entrée. Les paramètres d'entrée sont la liste des morceaux, le taux de parole, le nom de la voix et le chemin de sortie pour enregistrer le fichier audio généré.
1. `talk(input_text)` : Cette fonction génère un fichier audio en utilisant l'API Edge TTS et en l'enregistrant sous un nom de fichier aléatoire dans le répertoire /content/audio. Le paramètre d'entrée est le texte d'entrée à convertir en parole.
1. `run_text_prompt(message, chat_history)` : Cette fonction utilise la démonstration Microsoft Phi 3 Mini 4K Instruct pour générer un fichier audio à partir d'un message d'entrée et l'ajoute à l'historique du chat.
1. `run_audio_prompt(audio, chat_history)` : Cette fonction convertit un fichier audio en texte en utilisant l'API du modèle Whisper et le passe à la fonction `run_text_prompt()`.
1. Le code lance une application Gradio qui permet aux utilisateurs d'interagir avec la démonstration Phi 3 Mini 4K Instruct en tapant des messages ou en téléchargeant des fichiers audio. La sortie est affichée sous forme de message texte dans l'application.

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

1. Vérifiez la taille de la mémoire GPU Nvidia (nécessite 12 Go de mémoire GPU)

    ```bash
    nvidia-smi
    ```

1. Vider le cache : Si vous utilisez PyTorch, vous pouvez appeler torch.cuda.empty_cache() pour libérer toute la mémoire mise en cache inutilisée afin qu'elle puisse être utilisée par d'autres applications GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Vérifiez Cuda Nvidia

    ```bash
    nvcc --version
    ```

1. Effectuez les tâches suivantes pour créer un jeton Hugging Face.

    - Accédez à la [page des paramètres de jeton Hugging Face](https://huggingface.co/settings/tokens).
    - Sélectionnez **Nouveau jeton**.
    - Entrez le **Nom** du projet que vous souhaitez utiliser.
    - Sélectionnez **Type** sur **Écriture**.

> **Note**
>
> Si vous rencontrez l'erreur suivante :
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pour résoudre cela, tapez la commande suivante dans votre terminal.
>
> ```bash
> sudo ldconfig
> ```

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.