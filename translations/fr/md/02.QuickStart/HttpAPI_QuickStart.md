# Utiliser l'API Azure avec Phi-3

Ce notebook montre des exemples d'utilisation des API Phi-3 proposées par Microsoft Azure AI et Azure ML. Nous couvrirons :  
* Utilisation de l'API de requêtes HTTP pour les modèles pré-entraînés et de chat Phi-3 en CLI
* Utilisation de l'API de requêtes HTTP pour les modèles pré-entraînés et de chat Phi-3 en Python

Voici un aperçu de **l'utilisation de l'API de requêtes HTTP en CLI** :

## Utilisation de l'API de requêtes HTTP en CLI

### Bases

Pour utiliser l'API REST, vous aurez besoin d'une URL de point de terminaison et d'une clé d'authentification associée à ce point de terminaison. Ceux-ci peuvent être acquis à partir des étapes précédentes.

Dans cet exemple de complétion de chat, nous utilisons un simple appel `curl` pour illustration. Il y a trois composants principaux :

1. **L'`host-url`** : C'est votre URL de point de terminaison avec le schéma de complétion de chat `/v1/chat/completions`.
2. **Les `headers`** : Cela définit le type de contenu ainsi que votre clé API.
3. **Le `payload` ou `data`** : Cela inclut les détails de votre prompt et les hyperparamètres du modèle.

### Exemple

Voici un exemple de requête de complétion de chat utilisant `curl` :

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Bonjour, comment ça va?"}],
  "max_tokens": 50
}'
```

### Décomposition

- **`-X POST`** : Spécifie la méthode HTTP à utiliser, qui est POST dans ce cas.
- **`https://api.example.com/v1/chat/completions`** : L'URL du point de terminaison.
- **`-H "Content-Type: application/json"`** : Définit le type de contenu sur JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`** : Ajoute l'en-tête d'autorisation avec votre clé API.
- **`-d '{...}'`** : La charge utile des données, qui inclut le modèle, les messages et d'autres paramètres.

### Conseils

- **URL du point de terminaison** : Assurez-vous de remplacer `https://api.example.com` par votre URL de point de terminaison réelle.
- **Clé API** : Remplacez `YOUR_API_KEY` par votre clé API réelle.
- **Charge utile** : Personnalisez la charge utile selon vos besoins, en incluant différents prompts, modèles et paramètres.

Voir l'exemple [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

Consultez la [documentation](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) pour la famille de modèles Phi-3 sur AI Studio et ML Studio pour des détails sur la façon de provisionner des points de terminaison d'inférence, la disponibilité régionale, les tarifs et la référence de schéma d'inférence.

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez vérifier le résultat et apporter les corrections nécessaires.