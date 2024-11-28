# Déployer des modèles Phi-3 en tant qu'API sans serveur

Les modèles Phi-3 (Mini, Small et Medium) dans le [catalogue de modèles Azure](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo) peuvent être déployés en tant qu'API sans serveur avec une facturation à l'utilisation. Ce type de déploiement permet de consommer des modèles en tant qu'API sans les héberger sur votre abonnement, tout en conservant la sécurité et la conformité dont les organisations ont besoin. Cette option de déploiement ne nécessite pas de quota de votre abonnement.

Les modèles MaaS [REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) supportent maintenant une API REST commune pour les complétions de chat en utilisant la route /chat/completions.

## Prérequis

1. Un abonnement Azure avec un moyen de paiement valide. Les abonnements Azure gratuits ou d'essai ne fonctionneront pas. Si vous n'avez pas d'abonnement Azure, créez un compte Azure payant pour commencer.
1. Un hub [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo). L'offre de déploiement de modèle sans serveur pour Phi-3 n'est disponible qu'avec des hubs créés dans ces régions :
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > Pour une liste des régions disponibles pour chacun des modèles supportant les déploiements d'API sans serveur, consultez la disponibilité des régions pour les modèles dans les points de terminaison d'API sans serveur.

1. Un projet [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Les contrôles d'accès basés sur les rôles Azure (Azure RBAC) sont utilisés pour accorder l'accès aux opérations dans Azure AI Foundry. Pour effectuer les étapes de cet article, votre compte utilisateur doit être assigné au rôle Azure AI Developer sur le groupe de ressources.

## Créer un nouveau déploiement

Effectuez les tâches suivantes pour créer un déploiement :

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Sélectionnez Catalogue de modèles dans la barre latérale gauche.
1. Recherchez et sélectionnez le modèle que vous souhaitez déployer, par exemple Phi-3-mini-4k-Instruct, pour ouvrir sa page Détails.
1. Sélectionnez Déployer.
1. Choisissez l'option API sans serveur pour ouvrir une fenêtre de déploiement d'API sans serveur pour le modèle.

Alternativement, vous pouvez initier un déploiement en commençant par votre projet dans AI Foundry.

1. Dans la barre latérale gauche de votre projet, sélectionnez Composants > Déploiements.
1. Sélectionnez + Créer un déploiement.
1. Recherchez et sélectionnez Phi-3-mini-4k-Instruct pour ouvrir la page Détails du modèle.
1. Sélectionnez Confirmer, et choisissez l'option API sans serveur pour ouvrir une fenêtre de déploiement d'API sans serveur pour le modèle.
1. Sélectionnez le projet dans lequel vous souhaitez déployer votre modèle. Pour déployer le modèle Phi-3, votre projet doit appartenir à l'une des régions listées dans la [section des prérequis](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo).
1. Sélectionnez l'onglet Tarification et conditions pour en savoir plus sur la tarification du modèle sélectionné.
1. Donnez un nom au déploiement. Ce nom devient une partie de l'URL de l'API de déploiement. Cette URL doit être unique dans chaque région Azure.
1. Sélectionnez Déployer. Attendez que le déploiement soit prêt et que vous soyez redirigé vers la page Déploiements. Cette étape nécessite que votre compte ait les permissions du rôle Azure AI Developer sur le groupe de ressources, comme indiqué dans les prérequis.
1. Sélectionnez Ouvrir dans le playground pour commencer à interagir avec le modèle.

Retournez à la page Déploiements, sélectionnez le déploiement, et notez l'URL cible du point de terminaison et la clé secrète, que vous pouvez utiliser pour appeler le déploiement et générer des complétions. Pour plus d'informations sur l'utilisation des API, consultez [Référence : Complétions de chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo).

Vous pouvez toujours trouver les détails du point de terminaison, l'URL, et les clés d'accès en naviguant vers la page d'aperçu de votre projet. Ensuite, dans la barre latérale gauche de votre projet, sélectionnez Composants > Déploiements.

## Consommer les modèles Phi-3 en tant que service

Les modèles déployés en tant qu'API sans serveur peuvent être consommés en utilisant l'API de chat, selon le type de modèle que vous avez déployé.

1. Depuis la page d'aperçu de votre projet, allez à la barre latérale gauche et sélectionnez Composants > Déploiements.
2. Trouvez et sélectionnez le déploiement que vous avez créé.
3. Copiez l'URL cible et la valeur de la clé.
4. Faites une requête API en utilisant l'API chat/completions en utilisant <target_url>chat/completions. Pour plus d'informations sur l'utilisation des API, consultez la [Référence : Complétions de chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)

## Coût et quotas

Considérations de coût et de quota pour les modèles Phi-3 déployés en tant qu'API sans serveur

Vous pouvez trouver les informations de tarification sur l'onglet Tarification et conditions de l'assistant de déploiement lors du déploiement du modèle.

Le quota est géré par déploiement. Chaque déploiement a une limite de taux de 200 000 tokens par minute et 1 000 requêtes API par minute. Cependant, nous limitons actuellement un déploiement par modèle par projet. Contactez le support Microsoft Azure si les limites actuelles ne suffisent pas pour vos scénarios.

## Ressources supplémentaires 

### Déployer des modèles en tant qu'API sans serveur

Modèles MaaS en tant que service Pour plus de détails sur le [déploiement MaaS](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)

### Comment déployer la famille de petits modèles linguistiques Phi-3 avec Azure Machine Learning studio ou Azure AI Foundry

Modèles Maap en tant que plateforme pour plus de détails sur le [déploiement Maap](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.