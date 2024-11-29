# Utiliser l'API Azure avec Phi-3

Ce notebook montre des exemples d'utilisation des API Phi-3 proposées par Microsoft Azure AI et Azure ML. Nous couvrirons :  
* L'utilisation de l'API de requêtes HTTP pour les modèles pré-entraînés et de chat Phi-3 en CLI
* L'utilisation de l'API de requêtes HTTP pour les modèles pré-entraînés et de chat Phi-3 en Python

Voici un aperçu de **l'utilisation de l'API de requêtes HTTP en CLI** :

## Utilisation de l'API de requêtes HTTP en CLI

### Notions de base

Pour utiliser l'API REST, vous aurez besoin d'une URL de point de terminaison et d'une clé d'authentification associée à ce point de terminaison. Ces éléments peuvent être acquis lors des étapes précédentes.

Dans cet exemple de complétion de chat, nous utilisons un simple appel `curl` pour illustration. Il y a trois composants principaux :

1. **L'`host-url`** : Il s'agit de votre URL de point de terminaison avec le schéma de complétion de chat `/v1/chat/completions`.
2. **L'`headers`** : Cela définit le type de contenu ainsi que votre clé API.
3. **L'`payload` ou `data`** : Cela inclut les détails de votre invite et les hyperparamètres du modèle.

### Exemple

Voici un exemple de requête de complétion de chat utilisant `curl` :

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "max_tokens": 50
}'
```

### Décomposition

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY` avec votre clé API réelle.
- **Payload** : Personnalisez le payload selon vos besoins, y compris différentes invites, modèles et paramètres.

Voir l'exemple [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

Consultez la [documentation](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) pour la famille de modèles Phi-3 sur AI Studio et ML Studio pour des détails sur la façon de provisionner des points de terminaison d'inférence, la disponibilité régionale, les prix et la référence de schéma d'inférence.

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.