# **Inference Phi-3 sur Serveur Local**

Nous pouvons déployer Phi-3 sur un serveur local. Les utilisateurs peuvent choisir les solutions [Ollama](https://ollama.com) ou [LM Studio](https://llamaedge.com), ou ils peuvent écrire leur propre code. Vous pouvez connecter les services locaux de Phi-3 via [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) ou [Langchain](https://www.langchain.com/) pour créer des applications Copilot.

## **Utiliser Semantic Kernel pour accéder à Phi-3-mini**

Dans l'application Copilot, nous créons des applications via Semantic Kernel / LangChain. Ce type de framework d'application est généralement compatible avec Azure OpenAI Service / modèles OpenAI, et peut également prendre en charge les modèles open source sur Hugging Face et les modèles locaux. Que devons-nous faire si nous voulons utiliser Semantic Kernel pour accéder à Phi-3-mini ? En utilisant .NET comme exemple, nous pouvons le combiner avec le Hugging Face Connector dans Semantic Kernel. Par défaut, il peut correspondre à l'id du modèle sur Hugging Face (la première fois que vous l'utilisez, le modèle sera téléchargé depuis Hugging Face, ce qui prend beaucoup de temps). Vous pouvez également vous connecter au service local construit. Comparé aux deux, nous recommandons d'utiliser ce dernier car il offre un degré d'autonomie plus élevé, en particulier dans les applications d'entreprise.

![sk](../../../../translated_images/sk.fc8f38bb6ac491315099aa29a2704de109fc0b052448c9bc3d7c02586c196ca4.fr.png)

D'après la figure, accéder aux services locaux via Semantic Kernel peut facilement se connecter au serveur de modèle Phi-3-mini auto-construit. Voici le résultat de l'exécution.

![skrun](../../../../translated_images/skrun.f579fcb28592ba4644af8b578e66fb01923bf032b670cef44874c6550e85876d.fr.png)

***Code Exemple*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction automatisée par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.