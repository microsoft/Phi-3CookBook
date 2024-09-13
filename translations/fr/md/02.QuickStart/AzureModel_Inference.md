# Inférence du modèle Azure AI

L'[inférence du modèle Azure AI est une API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo) qui expose un ensemble commun de capacités pour les modèles fondamentaux et qui peut être utilisée par les développeurs pour consommer des prédictions à partir d'un ensemble diversifié de modèles de manière uniforme et cohérente. Les développeurs peuvent interagir avec différents modèles déployés dans Azure AI Studio sans modifier le code sous-jacent qu'ils utilisent.

Microsoft dispose désormais de son propre SDK pour l'inférence des modèles AI, pour différents modèles hébergés sur [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo).

Les versions Python et JS sont disponibles. C# sera la prochaine à être publiée.

Pour [Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) [Exemples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

Pour [JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [Exemples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

Le SDK utilise la [REST API documentée ici](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo).

## Disponibilité

L'API d'inférence du modèle Azure AI est disponible dans les modèles Phi-3 suivants :

- Modèles déployés sur des points de terminaison API sans serveur :
- Modèles déployés pour l'inférence gérée :

L'API est compatible avec les déploiements de modèles Azure OpenAI.

> [!NOTE]
> L'API d'inférence du modèle Azure AI est disponible dans l'inférence gérée (Managed Online Endpoints) pour les modèles déployés après le 24 juin 2024. Pour profiter de l'API, redéployez votre point de terminaison si le modèle a été déployé avant cette date.

## Capacités

La section suivante décrit certaines des capacités exposées par l'API. Pour une spécification complète de l'API, consultez la section de référence.

### Modalités

L'API indique comment les développeurs peuvent consommer des prédictions pour les modalités suivantes :

- Obtenir des infos : Retourne les informations sur le modèle déployé sous le point de terminaison.
- Text embeddings : Crée un vecteur d'embedding représentant le texte d'entrée.
- Complétions de texte : Crée une complétion pour le prompt et les paramètres fournis.
- Complétions de chat : Crée une réponse du modèle pour la conversation de chat donnée.
- Image embeddings : Crée un vecteur d'embedding représentant le texte et l'image d'entrée.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.