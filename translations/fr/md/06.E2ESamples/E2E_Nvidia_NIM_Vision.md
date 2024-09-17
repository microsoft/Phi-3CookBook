### Scénario Exemple

Imaginez que vous avez une image (`demo.png`) et que vous souhaitez générer du code Python pour traiter cette image et enregistrer une nouvelle version de celle-ci (`phi-3-vision.jpg`). 

Le code ci-dessus automatise ce processus en :

1. Configurant l'environnement et les configurations nécessaires.
2. Créant une invite qui demande au modèle de générer le code Python requis.
3. Envoyant l'invite au modèle et collectant le code généré.
4. Extrayant et exécutant le code généré.
5. Affichant les images originale et traitée.

Cette approche tire parti de la puissance de l'IA pour automatiser les tâches de traitement d'images, rendant plus facile et rapide l'atteinte de vos objectifs.

[Solution de Code Exemple](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Analysons ce que fait le code pas à pas :

1. **Installer le Package Requis** :
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Cette commande installe le package `langchain_nvidia_ai_endpoints`, en s'assurant qu'il s'agit de la dernière version.

2. **Importer les Modules Nécessaires** :
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ces imports amènent les modules nécessaires pour interagir avec les points de terminaison AI de NVIDIA, gérer les mots de passe de manière sécurisée, interagir avec le système d'exploitation et encoder/décoder des données en format base64.

3. **Configurer la Clé API** :
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ce code vérifie si la variable d'environnement `NVIDIA_API_KEY` est définie. Sinon, il invite l'utilisateur à entrer sa clé API de manière sécurisée.

4. **Définir le Modèle et le Chemin de l'Image** :
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Cela définit le modèle à utiliser, crée une instance de `ChatNVIDIA` avec le modèle spécifié, et définit le chemin vers le fichier image.

5. **Créer l'Invite de Texte** :
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Cela définit une invite de texte demandant au modèle de générer du code Python pour traiter une image.

6. **Encoder l'Image en Base64** :
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'
    ```
    Ce code lit le fichier image, l'encode en base64, et crée une balise HTML d'image avec les données encodées.

7. **Combiner le Texte et l'Image dans l'Invite** :
    ```python
    prompt = f"{text} {image}"
    ```
    Cela combine l'invite de texte et la balise HTML d'image en une seule chaîne.

8. **Générer le Code en Utilisant ChatNVIDIA** :
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ce code envoie l'invite au modèle `ChatNVIDIA` et collecte le code généré en morceaux, imprimant et ajoutant chaque morceau à la chaîne `code`.

9. **Extraire le Code Python du Contenu Généré** :
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Cela extrait le code Python réel du contenu généré en supprimant la mise en forme markdown.

10. **Exécuter le Code Généré** :
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Cela exécute le code Python extrait en tant que sous-processus et capture sa sortie.

11. **Afficher les Images** :
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ces lignes affichent les images en utilisant le module `IPython.display`.

Avertissement : La traduction a été effectuée à partir de son original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez revoir le résultat et apporter les corrections nécessaires.