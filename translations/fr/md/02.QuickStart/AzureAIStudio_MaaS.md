# Déployer des modèles Phi-3 comme API sans serveur

Les modèles Phi-3 (Mini, Small et Medium) dans le [catalogue de modèles Azure](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo) peuvent être déployés comme une API sans serveur avec une facturation à l'utilisation. Ce type de déploiement permet de consommer des modèles en tant qu'API sans les héberger sur votre abonnement, tout en conservant la sécurité et la conformité d'entreprise nécessaires. Cette option de déploiement ne nécessite pas de quota de votre abonnement.

Les modèles MaaS [REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) prennent désormais en charge une API REST commune pour les complétions de chat en utilisant la route /chat/completions.

## Prérequis

1. Un abonnement Azure avec un moyen de paiement valide. Les abonnements Azure gratuits ou d'essai ne fonctionneront pas. Si vous n'avez pas d'abonnement Azure, créez un compte Azure payant pour commencer.
1. Un hub [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo). L'offre de déploiement de modèle API sans serveur pour Phi-3 est uniquement disponible avec des hubs créés dans ces régions :
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > Pour une liste des régions disponibles pour chacun des modèles prenant en charge les déploiements d'API sans serveur, voir Disponibilité régionale pour les modèles dans les points de terminaison API sans serveur.

1. Un projet [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Les contrôles d'accès basés sur les rôles Azure (Azure RBAC) sont utilisés pour accorder l'accès aux opérations dans Azure AI Studio. Pour effectuer les étapes de cet article, votre compte utilisateur doit se voir attribuer le rôle Azure AI Developer sur le groupe de ressources.

## Créer un nouveau déploiement

Effectuez les tâches suivantes pour créer un déploiement :

1. Connectez-vous à [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Sélectionnez Catalogue de modèles dans la barre latérale gauche.
1. Recherchez et sélectionnez le modèle que vous souhaitez déployer, par exemple Phi-3-mini-4k-Instruct, pour ouvrir sa page de détails.
1. Sélectionnez Déployer.
1. Choisissez l'option API sans serveur pour ouvrir une fenêtre de déploiement d'API sans serveur pour le modèle.

Alternativement, vous pouvez initier un déploiement en démarrant à partir de votre projet dans AI Studio.

1. Dans la barre latérale gauche de votre projet, sélectionnez Composants > Déploiements.
1. Sélectionnez + Créer un déploiement.
1. Recherchez et sélectionnez Phi-3-mini-4k-Instruct pour ouvrir la page de détails du modèle.
1. Sélectionnez Confirmer, et choisissez l'option API sans serveur pour ouvrir une fenêtre de déploiement d'API sans serveur pour le modèle.
1. Sélectionnez le projet dans lequel vous souhaitez déployer votre modèle. Pour déployer le modèle Phi-3, votre projet doit appartenir à l'une des régions listées dans la [section des prérequis](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo).
1. Sélectionnez l'onglet Tarification et conditions pour en savoir plus sur les tarifs du modèle sélectionné.
1. Donnez un nom au déploiement. Ce nom fait partie de l'URL de l'API de déploiement. Cette URL doit être unique dans chaque région Azure.
1. Sélectionnez Déployer. Attendez que le déploiement soit prêt et que vous soyez redirigé vers la page des Déploiements. Cette étape nécessite que votre compte dispose des autorisations de rôle Azure AI Developer sur le groupe de ressources, comme indiqué dans les prérequis.
1. Sélectionnez Ouvrir dans le playground pour commencer à interagir avec le modèle.

Retournez à la page des Déploiements, sélectionnez le déploiement et notez l'URL de cible de l'endpoint et la clé secrète, que vous pouvez utiliser pour appeler le déploiement et générer des complétions. Pour plus d'informations sur l'utilisation des APIs, voir [Référence : Complétions de Chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo).

Vous pouvez toujours trouver les détails de l'endpoint, l'URL et les clés d'accès en naviguant vers la page de vue d'ensemble de votre projet. Ensuite, dans la barre latérale gauche de votre projet, sélectionnez Composants > Déploiements.

## Consommer des modèles Phi-3 comme un service

Les modèles déployés en tant qu'APIs sans serveur peuvent être consommés en utilisant l'API de chat, selon le type de modèle que vous avez déployé.

1. Depuis la page de vue d'ensemble de votre projet, allez à la barre latérale gauche et sélectionnez Composants > Déploiements.
2. Trouvez et sélectionnez le déploiement que vous avez créé.
3. Copiez l'URL de cible et la valeur de la clé.
4. Faites une requête API en utilisant l'API chat/completions en utilisant <target_url>chat/completions. Pour plus d'informations sur l'utilisation des APIs, voir la [Référence : Complétions de Chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)

## Coût et quotas

Considérations de coût et de quota pour les modèles Phi-3 déployés comme APIs sans serveur

Vous pouvez trouver les informations sur les tarifs dans l'onglet Tarification et conditions de l'assistant de déploiement lors du déploiement du modèle.

Le quota est géré par déploiement. Chaque déploiement a une limite de taux de 200 000 tokens par minute et 1 000 requêtes API par minute. Cependant, nous limitons actuellement un déploiement par modèle et par projet. Contactez le support Microsoft Azure si les limites de taux actuelles ne sont pas suffisantes pour vos scénarios.

## Ressources supplémentaires

### Déployer des modèles comme APIs sans serveur

Modèles MaaS en tant que service Pour plus de détails sur [Déploiement MaaS](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)

### Comment déployer la famille de petits modèles linguistiques Phi-3 avec Azure Machine Learning studio ou Azure AI Studio

Modèles Maap en tant que plateforme pour plus de détails sur [Déploiement Maap](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.