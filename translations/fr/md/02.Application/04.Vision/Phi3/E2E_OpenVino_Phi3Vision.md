Cette démonstration montre comment utiliser un modèle préentraîné pour générer du code Python à partir d'une image et d'une invite textuelle.

[Exemple de Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Voici une explication étape par étape :

1. **Importations et Configuration** :
   - Les bibliothèques et modules nécessaires sont importés, y compris `requests`, `PIL` pour le traitement d'images, et `transformers` pour gérer le modèle et le traitement.

2. **Chargement et Affichage de l'Image** :
   - Un fichier image (`demo.png`) est ouvert en utilisant la bibliothèque `PIL` et affiché.

3. **Définir l'Invite** :
   - Un message est créé, incluant l'image et une demande pour générer du code Python afin de traiter l'image et de l'enregistrer en utilisant `plt` (matplotlib).

4. **Chargement du Processeur** :
   - Le `AutoProcessor` est chargé à partir d'un modèle préentraîné spécifié dans le répertoire `out_dir`. Ce processeur gérera les entrées textuelles et d'images.

5. **Création de l'Invite** :
   - La méthode `apply_chat_template` est utilisée pour formater le message en une invite adaptée au modèle.

6. **Traitement des Entrées** :
   - L'invite et l'image sont transformées en tenseurs compréhensibles par le modèle.

7. **Définir les Paramètres de Génération** :
   - Les paramètres du processus de génération du modèle sont définis, y compris le nombre maximal de nouveaux tokens à générer et si la sortie doit être échantillonnée.

8. **Génération du Code** :
   - Le modèle génère le code Python en fonction des entrées et des paramètres de génération. Le `TextStreamer` est utilisé pour gérer la sortie, en ignorant l'invite et les tokens spéciaux.

9. **Résultat** :
   - Le code généré est affiché, incluant le code Python pour traiter l'image et l'enregistrer comme spécifié dans l'invite.

Cette démonstration illustre comment exploiter un modèle préentraîné avec OpenVino pour générer dynamiquement du code en fonction des entrées utilisateur et des images.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisés basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.