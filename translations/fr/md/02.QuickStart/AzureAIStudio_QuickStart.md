# **Utilisation de Phi-3 dans Azure AI Studio**

Avec le développement de l'IA générative, nous espérons utiliser une plateforme unifiée pour gérer différents LLM et SLM, intégrer les données d'entreprise, effectuer des opérations de fine-tuning/RAG, et évaluer les différentes activités d'entreprise après intégration des LLM et SLM, etc., afin que les applications intelligentes de l'IA générative soient mieux mises en œuvre. [Azure AI Studio](https://ai.azure.com) est une plateforme d'application d'IA générative de niveau entreprise.

![aistudo](../../../../translated_images/ai-studio-home.e25e21a22af0a57c0cb02815f4c7554c8816afe8bc3c3008ac74e2eedd9fbaa9.fr.png)

Avec Azure AI Studio, vous pouvez évaluer les réponses des grands modèles de langage (LLM) et orchestrer les composants d'application de prompt avec le flux de prompt pour de meilleures performances. La plateforme facilite l'évolutivité pour transformer les preuves de concept en production complète avec facilité. La surveillance continue et le raffinement soutiennent le succès à long terme.

Nous pouvons déployer rapidement le modèle Phi-3 sur Azure AI Studio en quelques étapes simples, puis utiliser Azure AI Studio pour effectuer des travaux liés à Phi-3 tels que Playground/Chat, Fine-tuning, évaluation, etc.

## **1. Préparation**

## [AZD AI Studio Starter Template](https://azure.github.io/awesome-azd/?name=AI+Studio)

### Azure AI Studio Starter

Ceci est un template Bicep qui déploie tout ce dont vous avez besoin pour commencer avec Azure AI Studio. Comprend AI Hub avec des ressources dépendantes, un projet AI, des services AI et un endpoint en ligne.

### Utilisation Rapide

Si vous avez déjà installé le [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) sur votre machine, utiliser ce template est aussi simple que de lancer cette commande dans un nouveau répertoire.

### Commande Terminal

```bash
azd init -t azd-aistudio-starter
```

Ou
Si vous utilisez l'extension azd pour VS Code, vous pouvez coller cette URL dans le terminal de commande de VS Code.

### URL Terminal

```bash
azd-aistudio-starter
```

## Création Manuelle

Créez Azure AI Studio sur [Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo)

![portal](../../../../translated_images/ai-studio-portal.8ae13fc10a0fe53104d7fe8d1c8c59b53f5ff7f4d74e52d81bcd63b5de6baf13.fr.png)

Après avoir complété le nommage du studio et réglé la région, vous pouvez le créer.

![settings](../../../../translated_images/ai-studio-settings.ac28832948da45fd844232ae8e743f3e657a4b88e8a02ce80ae6bfad8ba4733a.fr.png)

Après une création réussie, vous pouvez accéder au studio que vous avez créé via [ai.azure.com](https://ai.azure.com/)

![page](../../../../translated_images/ai-studio-page.9bfba68b0b3662a5323008dab8d9b24d4fc580be93777203bb64ad78283df469.fr.png)

Il peut y avoir plusieurs projets sur un AI Studio. Créez un projet dans AI Studio pour vous préparer.

![proj](../../../../translated_images/ai-studio-proj.62b5b49ee77bd4e382a82c1c28c247c1204c11ea212a4d95b39e467c6a24998f.fr.png)

## **2. Déployer le modèle Phi-3 dans Azure AI Studio**

Cliquez sur l'option Explorer du projet pour entrer dans le Catalogue de Modèles et sélectionnez Phi-3.

![model](../../../../translated_images/ai-studio-model.d90f85e0b4ce4bbdde6e460304f2e6676502e86ec0aae8f39dd56b7f0538afb9.fr.png)

Sélectionnez Phi-3-mini-4k-instruct.

![phi3](../../../../translated_images/ai-studio-phi3.9320ffe396abdbf9d1026637016462406090df88e0883e411b1984be34ed5710.fr.png)

Cliquez sur 'Déployer' pour déployer le modèle Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Vous pouvez sélectionner la puissance de calcul lors du déploiement.

## **3. Playground Chat Phi-3 dans Azure AI Studio**

Accédez à la page de déploiement, sélectionnez Playground, et discutez avec Phi-3 d'Azure AI Studio.

![chat](../../../../translated_images/ai-studio-chat.ba2c631ac2279f2deb4e87998895b0688e33d2f79475da6a3851e3fb3a0495c5.fr.png)

## **4. Déploiement du Modèle depuis Azure AI Studio**

Pour déployer un modèle depuis le Catalogue de Modèles Azure, vous pouvez suivre ces étapes :

- Connectez-vous à Azure AI Studio.
- Choisissez le modèle que vous souhaitez déployer depuis le catalogue de modèles Azure AI Studio.
- Sur la page de détails du modèle, sélectionnez Déployer puis sélectionnez API sans serveur avec Azure AI Content Safety.
- Sélectionnez le projet dans lequel vous souhaitez déployer vos modèles. Pour utiliser l'offre API sans serveur, votre workspace doit appartenir à la région East US 2 ou Sweden Central. Vous pouvez personnaliser le nom du déploiement.
- Sur l'assistant de déploiement, sélectionnez les Tarifs et conditions pour en savoir plus sur les tarifs et les conditions d'utilisation.
- Sélectionnez Déployer. Attendez que le déploiement soit prêt et que vous soyez redirigé vers la page Déploiements.
- Sélectionnez Ouvrir dans le playground pour commencer à interagir avec le modèle.
- Vous pouvez retourner à la page Déploiements, sélectionner le déploiement, et noter l'URL cible du endpoint et la clé secrète, que vous pouvez utiliser pour appeler le déploiement et générer des complétions.
- Vous pouvez toujours trouver les détails du endpoint, l'URL et les clés d'accès en naviguant vers l'onglet Build et en sélectionnant Déploiements dans la section Composants.

> [!NOTE]
> Veuillez noter que votre compte doit avoir les permissions du rôle Développeur Azure AI sur le groupe de ressources pour effectuer ces étapes.

## **5. Utilisation de l'API Phi-3 dans Azure AI Studio**

Vous pouvez accéder à https://{Votre nom de projet}.region.inference.ml.azure.com/swagger.json via Postman GET et le combiner avec la clé pour en savoir plus sur les interfaces fournies.

![swagger](../../../../translated_images/ai-studio-swagger.ae9e8fff8aba78ec18dc94b0ef251f0efe4ba90e77618ff0df13e1636e196abf.fr.png)

comme accéder à l'API de score

![score](../../../../translated_images/ai-studio-score.0d5c8ce86241111633e946acf3413d3073957beb81cd37382cfd084ae310678f.fr.png)

Vous pouvez obtenir très facilement les paramètres de requête, ainsi que les paramètres de réponse. Voici le résultat de Postman.

![result](../../../../translated_images/ai-studio-result.8563455b3a437110aa1d99bfc21cd8c624510b100f20b8907653cba5eef36226.fr.png)

