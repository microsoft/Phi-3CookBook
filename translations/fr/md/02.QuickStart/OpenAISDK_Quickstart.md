# Utiliser le SDK OpenAI avec Phi-3 dans Azure AI et Azure ML

Utilisez le SDK `openai` pour consommer les déploiements Phi-3 dans Azure AI et Azure ML. La famille de modèles Phi-3 dans Azure AI et Azure ML offre une API compatible avec l'API OpenAI Chat Completion. Cela permet aux clients et utilisateurs de passer sans difficulté des modèles OpenAI aux LLMs Phi-3.

L'API peut être directement utilisée avec les bibliothèques clientes d'OpenAI ou des outils tiers, comme LangChain ou LlamaIndex.

L'exemple ci-dessous montre comment effectuer cette transition en utilisant la bibliothèque Python d'OpenAI. Notez que Phi-3 ne prend en charge que l'API de complétion de chat.

Pour utiliser le modèle Phi-3 avec le SDK OpenAI, vous devrez suivre quelques étapes pour configurer votre environnement et effectuer des appels API. Voici un guide pour vous aider à démarrer :

1. **Installer le SDK OpenAI** : Tout d'abord, vous devrez installer le package Python OpenAI si ce n'est déjà fait.
   ```bash
   pip install openai
   ```

2. **Configurer votre clé API** : Assurez-vous d'avoir votre clé API OpenAI. Vous pouvez la configurer dans vos variables d'environnement ou directement dans votre code.
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **Effectuer des appels API** : Utilisez le SDK OpenAI pour interagir avec le modèle Phi-3. Voici un exemple de demande de complétion :
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **Gérer les réponses** : Traitez les réponses du modèle selon les besoins de votre application.

Voici un exemple plus détaillé :
```python
import openai

# Set your API key
openai.api_key = "your-api-key"

# Define the prompt
prompt = "Write a short story about a brave knight."

# Make the API call
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Print the response
print(response.choices[0].text.strip())
```

Cela générera une courte histoire basée sur l'invite fournie. Vous pouvez ajuster le paramètre `max_tokens` pour contrôler la longueur de la sortie.

[Voir un exemple complet de Notebook pour les modèles Phi-3](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

Consultez la [documentation](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) pour la famille de modèles Phi-3 dans AI Studio et ML Studio pour des détails sur comment provisionner des points de terminaison d'inférence, la disponibilité régionale, les prix et la référence de schéma d'inférence.

**Avertissement** :
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.