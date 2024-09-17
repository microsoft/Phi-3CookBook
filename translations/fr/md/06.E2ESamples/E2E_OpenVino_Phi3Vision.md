Cette démonstration montre comment utiliser un modèle pré-entraîné pour générer du code Python à partir d'une image et d'une invite textuelle.

[Code Exemple](../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Voici une explication étape par étape :

1. **Imports et Configuration** :
   - Les bibliothèques et modules nécessaires sont importés, y compris `requests`, `PIL` pour le traitement des images, et `transformers` pour gérer le modèle et le traitement.

2. **Chargement et Affichage de l'Image** :
   - Un fichier image (`demo.png`) est ouvert en utilisant la bibliothèque `PIL` et affiché.

3. **Définition de l'Invite** :
   - Un message est créé qui inclut l'image et une demande de génération de code Python pour traiter l'image et la sauvegarder en utilisant `plt` (matplotlib).

4. **Chargement du Processeur** :
   - Le `AutoProcessor` est chargé à partir d'un modèle pré-entraîné spécifié par le répertoire `out_dir`. Ce processeur gérera les entrées textuelles et d'image.

5. **Création de l'Invite** :
   - La méthode `apply_chat_template` est utilisée pour formater le message en une invite appropriée pour le modèle.

6. **Traitement des Entrées** :
   - L'invite et l'image sont traitées en tenseurs que le modèle peut comprendre.

7. **Définition des Arguments de Génération** :
   - Les arguments pour le processus de génération du modèle sont définis, y compris le nombre maximum de nouveaux tokens à générer et si la sortie doit être échantillonnée.

8. **Génération du Code** :
   - Le modèle génère le code Python basé sur les entrées et les arguments de génération. Le `TextStreamer` est utilisé pour gérer la sortie, en sautant l'invite et les tokens spéciaux.

9. **Sortie** :
   - Le code généré est imprimé, qui devrait inclure du code Python pour traiter l'image et la sauvegarder comme spécifié dans l'invite.

Cette démonstration illustre comment exploiter un modèle pré-entraîné en utilisant OpenVino pour générer du code de manière dynamique en fonction des entrées de l'utilisateur et des images.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez vérifier le résultat et apporter les corrections nécessaires.