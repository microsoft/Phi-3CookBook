### Exemple de Scénario

Imaginez que vous avez une image (`demo.png`) et que vous souhaitez générer du code Python qui traite cette image et en sauvegarde une nouvelle version (`phi-3-vision.jpg`).

Le code ci-dessus automatise ce processus en :

1. Configurant l'environnement et les paramètres nécessaires.
2. Créant une invite qui demande au modèle de générer le code Python requis.
3. Envoyant l'invite au modèle et collectant le code généré.
4. Extrayant et exécutant le code généré.
5. Affichant les images originale et traitée.

Cette approche exploite la puissance de l'IA pour automatiser les tâches de traitement d'images, rendant vos objectifs plus faciles et rapides à atteindre.

[Solution de Code Exemple](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Décomposons ce que fait le code dans son ensemble, étape par étape :

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
    Ces imports permettent d'utiliser les modules nécessaires pour interagir avec les points de terminaison NVIDIA AI, gérer les mots de passe de manière sécurisée, interagir avec le système d'exploitation et encoder/décoder des données au format base64.

3. **Configurer la Clé API** :
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ce code vérifie si la variable d'environnement `NVIDIA_API_KEY` est définie. Si ce n'est pas le cas, il invite l'utilisateur à entrer sa clé API de manière sécurisée.

4. **Définir le Modèle et le Chemin de l'Image** :
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Cela définit le modèle à utiliser, crée une instance de `ChatNVIDIA` avec le modèle spécifié, et définit le chemin du fichier image.

5. **Créer une Invite Texte** :
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Cette section définit une invite texte demandant au modèle de générer du code Python pour traiter une image.

6. **Encoder l'Image en Base64** :
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ce code lit le fichier image, l'encode en base64, et crée une balise HTML d'image avec les données encodées.

7. **Combiner Texte et Image dans l'Invite** :
    ```python
    prompt = f"{text} {image}"
    ```
    Cela combine l'invite texte et la balise HTML d'image en une seule chaîne.

8. **Générer du Code avec ChatNVIDIA** :
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ce code envoie l'invite à `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extraire le Code Python du Contenu Généré** :
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Cela extrait le code Python réel du contenu généré en supprimant le formatage markdown.

10. **Exécuter le Code Généré** :
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ce code exécute le code Python extrait en tant que sous-processus et capture sa sortie.

11. **Afficher les Images** :
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ces lignes affichent les images à l'aide du module `IPython.display`.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations découlant de l'utilisation de cette traduction.