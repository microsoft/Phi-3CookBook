Cette démonstration montre comment utiliser un modèle préentraîné pour générer du code Python basé sur une image et une invite textuelle.

[Code d'exemple](../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Voici une explication étape par étape :

1. **Importations et Configuration** :
   - Les bibliothèques et modules nécessaires sont importés, y compris `requests`, `PIL` pour le traitement d'image, et `transformers` pour la gestion du modèle et le traitement.

2. **Chargement et Affichage de l'Image** :
   - Un fichier image (`demo.png`) est ouvert en utilisant la bibliothèque `PIL` et affiché.

3. **Définition de l'Invite** :
   - Un message est créé qui inclut l'image et une demande pour générer du code Python pour traiter l'image et la sauvegarder en utilisant `plt` (matplotlib).

4. **Chargement du Processeur** :
   - Le `AutoProcessor` est chargé à partir d'un modèle préentraîné spécifié par le répertoire `out_dir`. Ce processeur gérera les entrées textuelles et d'image.

5. **Création de l'Invite** :
   - La méthode `apply_chat_template` est utilisée pour formater le message en une invite appropriée pour le modèle.

6. **Traitement des Entrées** :
   - L'invite et l'image sont transformées en tenseurs que le modèle peut comprendre.

7. **Définition des Arguments de Génération** :
   - Les arguments pour le processus de génération du modèle sont définis, y compris le nombre maximum de nouveaux tokens à générer et si la sortie doit être échantillonnée.

8. **Génération du Code** :
   - Le modèle génère le code Python basé sur les entrées et les arguments de génération. Le `TextStreamer` est utilisé pour gérer la sortie, en sautant l'invite et les tokens spéciaux.

9. **Sortie** :
   - Le code généré est imprimé, qui devrait inclure du code Python pour traiter l'image et la sauvegarder comme spécifié dans l'invite.

Cette démonstration illustre comment tirer parti d'un modèle préentraîné en utilisant OpenVino pour générer du code dynamiquement basé sur les entrées utilisateur et les images.

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.