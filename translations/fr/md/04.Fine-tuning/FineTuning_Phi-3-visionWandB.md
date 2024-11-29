# Aperçu du projet Phi-3-Vision-128K-Instruct

## Le modèle

Le Phi-3-Vision-128K-Instruct, un modèle multimodal léger et à la pointe de la technologie, est au cœur de ce projet. Il fait partie de la famille de modèles Phi-3 et supporte une longueur de contexte allant jusqu'à 128 000 tokens. Le modèle a été entraîné sur un ensemble de données diversifié qui inclut des données synthétiques et des sites web publics soigneusement filtrés, en mettant l'accent sur du contenu de haute qualité et nécessitant une réflexion approfondie. Le processus d'entraînement a inclus un ajustement supervisé et une optimisation directe des préférences pour garantir une adhésion précise aux instructions, ainsi que des mesures de sécurité robustes.

## Créer des données d'exemple est crucial pour plusieurs raisons :

1. **Tests** : Les données d'exemple vous permettent de tester votre application dans divers scénarios sans affecter les données réelles. Cela est particulièrement important dans les phases de développement et de mise en scène.

2. **Optimisation des performances** : Avec des données d'exemple qui imitent l'échelle et la complexité des données réelles, vous pouvez identifier les goulots d'étranglement en termes de performances et optimiser votre application en conséquence.

3. **Prototypage** : Les données d'exemple peuvent être utilisées pour créer des prototypes et des maquettes, ce qui peut aider à comprendre les exigences des utilisateurs et obtenir des retours.

4. **Analyse des données** : En science des données, les données d'exemple sont souvent utilisées pour l'analyse exploratoire des données, l'entraînement de modèles et les tests d'algorithmes.

5. **Sécurité** : Utiliser des données d'exemple dans les environnements de développement et de test peut aider à prévenir les fuites accidentelles de données sensibles réelles.

6. **Apprentissage** : Si vous apprenez une nouvelle technologie ou un nouvel outil, travailler avec des données d'exemple peut offrir un moyen pratique d'appliquer ce que vous avez appris.

Rappelez-vous, la qualité de vos données d'exemple peut avoir un impact significatif sur ces activités. Elles doivent être aussi proches que possible des données réelles en termes de structure et de variabilité.

### Création de données d'exemple
[Generate DataSet Script](./CreatingSampleData.md)

## Ensemble de données

Un bon exemple d'ensemble de données d'exemple est [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible sur Huggingface). 
L'ensemble de données d'exemple des produits Burberry, avec des métadonnées sur la catégorie du produit, le prix et le titre, comprend un total de 3 040 lignes, chacune représentant un produit unique. Cet ensemble de données nous permet de tester la capacité du modèle à comprendre et interpréter les données visuelles, en générant des textes descriptifs qui capturent des détails visuels complexes et des caractéristiques spécifiques à la marque.

**Note:** Vous pouvez utiliser n'importe quel ensemble de données incluant des images.

## Raisonnement complexe

Le modèle doit raisonner sur les prix et les noms en se basant uniquement sur l'image. Cela nécessite que le modèle non seulement reconnaisse les caractéristiques visuelles, mais comprenne également leurs implications en termes de valeur du produit et de marque. En synthétisant des descriptions textuelles précises à partir d'images, le projet met en lumière le potentiel de l'intégration des données visuelles pour améliorer les performances et la polyvalence des modèles dans des applications du monde réel.

## Architecture de Phi-3 Vision

L'architecture du modèle est une version multimodale d'un Phi-3. Il traite à la fois les données textuelles et visuelles, intégrant ces entrées dans une séquence unifiée pour des tâches de compréhension et de génération complètes. Le modèle utilise des couches d'embedding séparées pour le texte et les images. Les tokens de texte sont convertis en vecteurs denses, tandis que les images sont traitées via un modèle de vision CLIP pour extraire des embeddings de caractéristiques. Ces embeddings d'images sont ensuite projetés pour correspondre aux dimensions des embeddings de texte, garantissant ainsi qu'ils peuvent être intégrés de manière transparente.

## Intégration des embeddings de texte et d'image

Des tokens spéciaux au sein de la séquence de texte indiquent où les embeddings d'image doivent être insérés. Pendant le traitement, ces tokens spéciaux sont remplacés par les embeddings d'image correspondants, permettant au modèle de traiter le texte et les images comme une seule séquence. L'invite pour notre ensemble de données est formatée en utilisant le token spécial <|image|> comme suit :

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exemple de code
- [Script d'entraînement Phi-3-Vision](../../../../code/04.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemple de walkthrough Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.