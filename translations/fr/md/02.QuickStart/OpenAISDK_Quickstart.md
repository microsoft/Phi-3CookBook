# Utiliser le SDK OpenAI avec Phi-3 dans Azure AI et Azure ML

Utilisez le SDK `openai` pour consommer les déploiements Phi-3 dans Azure AI et Azure ML. La famille de modèles Phi-3 dans Azure AI et Azure ML offre une API compatible avec l'API OpenAI Chat Completion. Elle permet aux clients et aux utilisateurs de passer sans problème des modèles OpenAI aux LLMs Phi-3.

L'API peut être utilisée directement avec les bibliothèques clientes d'OpenAI ou des outils tiers, comme LangChain ou LlamaIndex.

L'exemple ci-dessous montre comment effectuer cette transition en utilisant la bibliothèque Python OpenAI. Notez que Phi-3 ne supporte que l'API de complétions de chat.

Pour utiliser le modèle Phi-3 avec le SDK OpenAI, vous devrez suivre quelques étapes pour configurer votre environnement et effectuer des appels API. Voici un guide pour vous aider à démarrer :

1. **Installer le SDK OpenAI** : Tout d'abord, vous devez installer le package Python OpenAI si ce n'est pas déjà fait.
   ```bash
   pip install openai
   ```

2. **Configurer votre clé API** : Assurez-vous d'avoir votre clé API OpenAI. Vous pouvez la configurer dans vos variables d'environnement ou directement dans votre code.
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **Effectuer des appels API** : Utilisez le SDK OpenAI pour interagir avec le modèle Phi-3. Voici un exemple de requête de complétion :
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

# Configurez votre clé API
openai.api_key = "your-api-key"

# Définissez l'invite
prompt = "Write a short story about a brave knight."

# Effectuez l'appel API
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Affichez la réponse
print(response.choices[0].text.strip())
```

Cela générera une courte histoire basée sur l'invite fournie. Vous pouvez ajuster le paramètre `max_tokens` pour contrôler la longueur de la sortie.

[Voir un exemple complet de Notebook pour les modèles Phi-3](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

Consultez la [documentation](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) pour la famille de modèles Phi-3 dans AI Studio et ML Studio pour des détails sur la provision des points de terminaison d'inférence, la disponibilité régionale, les prix et la référence de schéma d'inférence.

Avertissement : La traduction a été réalisée à partir de son original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.