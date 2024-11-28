### Scénario Exemple

Imaginez que vous avez une image (`demo.png`) et que vous souhaitez générer du code Python qui traite cette image et enregistre une nouvelle version de celle-ci (`phi-3-vision.jpg`).

Le code ci-dessus automatise ce processus en :

1. Configurant l'environnement et les configurations nécessaires.
2. Créant une invite qui demande au modèle de générer le code Python requis.
3. Envoyant l'invite au modèle et collectant le code généré.
4. Extrayant et exécutant le code généré.
5. Affichant les images originales et traitées.

Cette approche exploite la puissance de l'IA pour automatiser les tâches de traitement d'images, rendant ainsi plus facile et rapide l'atteinte de vos objectifs.

[Solution de Code Exemple](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Décomposons ce que fait l'ensemble du code étape par étape :

1. **Installer le package requis** :
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Cette commande installe le package `langchain_nvidia_ai_endpoints`, en s'assurant qu'il est à la dernière version.

2. **Importer les modules nécessaires** :
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ces imports amènent les modules nécessaires pour interagir avec les points de terminaison NVIDIA AI, gérer les mots de passe en toute sécurité, interagir avec le système d'exploitation, et encoder/décoder des données au format base64.

3. **Configurer la clé API** :
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ce code vérifie si la variable d'environnement `NVIDIA_API_KEY` est définie. Sinon, il demande à l'utilisateur de saisir sa clé API en toute sécurité.

4. **Définir le modèle et le chemin de l'image** :
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Cela définit le modèle à utiliser, crée une instance de `ChatNVIDIA` avec le modèle spécifié, et définit le chemin du fichier image.

5. **Créer l'invite de texte** :
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Cela définit une invite de texte demandant au modèle de générer du code Python pour traiter une image.

6. **Encoder l'image en Base64** :
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ce code lit le fichier image, l'encode en base64, et crée une balise HTML image avec les données encodées.

7. **Combiner le texte et l'image dans l'invite** :
    ```python
    prompt = f"{text} {image}"
    ```
    Cela combine l'invite de texte et la balise HTML image en une seule chaîne.

8. **Générer du code en utilisant ChatNVIDIA** :
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ce code envoie l'invite à `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extraire le code Python du contenu généré** :
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Cela extrait le code Python réel du contenu généré en supprimant le formatage markdown.

10. **Exécuter le code généré** :
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Cela exécute le code Python extrait en tant que sous-processus et capture sa sortie.

11. **Afficher les images** :
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ces lignes affichent les images en utilisant le module `IPython.display`.

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.