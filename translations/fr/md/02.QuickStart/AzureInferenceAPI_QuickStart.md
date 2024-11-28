## Exécuter le modèle de la famille Phi en Python Pour d'autres exemples, voir https://github.com/marketplace/models

Ci-dessous, des extraits de code pour quelques cas d'utilisation. Pour plus d'informations sur le SDK Azure AI Inference, consultez la [documentation complète](https://aka.ms/azsdk/azure-ai-inference/python/reference) et les [exemples](https://aka.ms/azsdk/azure-ai-inference/python/samples).

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# Pour s'authentifier avec le modèle, vous devrez générer un jeton d'accès personnel (PAT) dans vos paramètres GitHub si vous utilisez les modèles du GitHub Marketplace (https://github.com/marketplace/models). 
# Créez votre jeton PAT en suivant les instructions ici : https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# Créez un fichier .env avec GitHub_token pour votre jeton personnel GitHub ou clé Azure

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="Pouvez-vous expliquer les bases de l'apprentissage automatique ?"),
    ],
    # Changez simplement le nom du modèle pour le modèle approprié "Phi-3.5-mini-instruct" ou "Phi-3.5-vision-instruct"
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
```

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations cruciales, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.