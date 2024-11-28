## Ejecutar el modelo de la familia Phi en Python Para otros ejemplos, consulta https://github.com/marketplace/models

A continuación se muestran fragmentos de código de ejemplo para algunos casos de uso. Para obtener información adicional sobre Azure AI Inference SDK, consulta la [documentación completa](https://aka.ms/azsdk/azure-ai-inference/python/reference) y los [ejemplos](https://aka.ms/azsdk/azure-ai-inference/python/samples).

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# Para autenticarte con el modelo, necesitarás generar un token de acceso personal (PAT) en la configuración de tu GitHub si estás utilizando modelos del GitHub Marketplace (https://github.com/marketplace/models).
# Crea tu token PAT siguiendo las instrucciones aquí: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# Crea un archivo .env con GitHub_token para tu Token Personal de GitHub o Azure Key

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="¿Puedes explicar los conceptos básicos del aprendizaje automático?"),
    ],
    # Simplemente cambia el nombre del modelo por el modelo apropiado "Phi-3.5-mini-instruct" o "Phi-3.5-vision-instruct"
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
```

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.