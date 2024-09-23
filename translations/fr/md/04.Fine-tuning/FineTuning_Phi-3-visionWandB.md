# Aperçu du Projet Phi-3-Vision-128K-Instruct

## Le Modèle

Le Phi-3-Vision-128K-Instruct, un modèle multimodal léger et à la pointe de la technologie, est au cœur de ce projet. Il fait partie de la famille de modèles Phi-3 et supporte une longueur de contexte allant jusqu'à 128 000 tokens. Le modèle a été entraîné sur un ensemble de données diversifié incluant des données synthétiques et des sites web publics soigneusement filtrés, mettant l'accent sur un contenu de haute qualité et intensif en raisonnement. Le processus de formation comprenait un ajustement supervisé et une optimisation directe des préférences pour assurer une adhésion précise aux instructions, ainsi que des mesures de sécurité robustes.

## La création de données d'échantillon est cruciale pour plusieurs raisons :

1. **Tests**: Les données d'échantillon permettent de tester votre application dans divers scénarios sans affecter les données réelles. Cela est particulièrement important dans les phases de développement et de mise en scène.

2. **Optimisation des performances**: Avec des données d'échantillon qui imitent l'échelle et la complexité des données réelles, vous pouvez identifier les goulots d'étranglement de performance et optimiser votre application en conséquence.

3. **Prototypage**: Les données d'échantillon peuvent être utilisées pour créer des prototypes et des maquettes, ce qui peut aider à comprendre les besoins des utilisateurs et à obtenir des retours.

4. **Analyse des données**: En science des données, les données d'échantillon sont souvent utilisées pour l'analyse exploratoire des données, l'entraînement de modèles et les tests d'algorithmes.

5. **Sécurité**: Utiliser des données d'échantillon dans les environnements de développement et de test peut aider à prévenir les fuites accidentelles de données sensibles réelles.

6. **Apprentissage**: Si vous apprenez une nouvelle technologie ou un nouvel outil, travailler avec des données d'échantillon peut fournir un moyen pratique d'appliquer ce que vous avez appris.

Rappelez-vous, la qualité de vos données d'échantillon peut avoir un impact significatif sur ces activités. Elles doivent être aussi proches que possible des données réelles en termes de structure et de variabilité.

### Création de Données d'Échantillon
[Script de Génération de Dataset](./CreatingSampleData.md)

## Ensemble de Données

Un bon exemple d'ensemble de données d'échantillon est [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponible sur Huggingface). 
L'ensemble de données d'échantillon des produits Burberry, accompagné de métadonnées sur la catégorie des produits, le prix et le titre, avec un total de 3 040 lignes, chacune représentant un produit unique. Cet ensemble de données nous permet de tester la capacité du modèle à comprendre et interpréter les données visuelles, en générant des textes descriptifs qui capturent des détails visuels complexes et des caractéristiques spécifiques à la marque.

**Note:** Vous pouvez utiliser n'importe quel ensemble de données incluant des images.

## Raisonnement Complexe

Le modèle doit raisonner sur les prix et les noms en se basant uniquement sur l'image. Cela nécessite que le modèle reconnaisse non seulement les caractéristiques visuelles, mais comprenne également leurs implications en termes de valeur et de marque du produit. En synthétisant des descriptions textuelles précises à partir d'images, le projet met en évidence le potentiel d'intégration des données visuelles pour améliorer la performance et la polyvalence des modèles dans des applications réelles.

## Architecture de Phi-3 Vision

L'architecture du modèle est une version multimodale d'un Phi-3. Elle traite à la fois les données textuelles et les images, intégrant ces entrées dans une séquence unifiée pour des tâches de compréhension et de génération complètes. Le modèle utilise des couches d'intégration séparées pour le texte et les images. Les tokens de texte sont convertis en vecteurs denses, tandis que les images sont traitées via un modèle de vision CLIP pour extraire des embeddings de caractéristiques. Ces embeddings d'images sont ensuite projetés pour correspondre aux dimensions des embeddings de texte, assurant une intégration transparente.

## Intégration des Embeddings de Texte et d'Image

Des tokens spéciaux dans la séquence de texte indiquent où les embeddings d'image doivent être insérés. Pendant le traitement, ces tokens spéciaux sont remplacés par les embeddings d'image correspondants, permettant au modèle de gérer le texte et les images comme une seule séquence. L'invite pour notre ensemble de données est formatée en utilisant le token spécial <|image|> comme suit :

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Exemple de Code
- [Script d'Entraînement Phi-3-Vision](../../../../code/04.Finetuning/Phi-3-vision-Trainingscript.py)
- [Exemple de Walkthrough Weights and Bias](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez vérifier le résultat et apporter les corrections nécessaires.