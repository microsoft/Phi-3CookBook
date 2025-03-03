Dans le contexte de Phi-3-mini, l'inférence fait référence au processus d'utilisation du modèle pour effectuer des prédictions ou générer des résultats à partir de données d'entrée. Permettez-moi de vous fournir plus de détails sur Phi-3-mini et ses capacités d'inférence.

Phi-3-mini fait partie de la série de modèles Phi-3 publiée par Microsoft. Ces modèles sont conçus pour redéfinir ce qui est possible avec les modèles de langage de petite taille (SLM).

Voici quelques points clés sur Phi-3-mini et ses capacités d'inférence :

## **Aperçu de Phi-3-mini :**
- Phi-3-mini dispose d'une taille de paramètre de 3,8 milliards.
- Il peut fonctionner non seulement sur des appareils informatiques traditionnels, mais aussi sur des appareils en périphérie, tels que les appareils mobiles et les appareils IoT.
- La sortie de Phi-3-mini permet aux particuliers et aux entreprises de déployer des SLM sur différents appareils matériels, en particulier dans des environnements à ressources limitées.
- Il prend en charge divers formats de modèle, y compris le format PyTorch traditionnel, la version quantifiée du format gguf et la version quantifiée basée sur ONNX.

## **Accéder à Phi-3-mini :**
Pour accéder à Phi-3-mini, vous pouvez utiliser [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dans une application Copilot. Semantic Kernel est généralement compatible avec Azure OpenAI Service, les modèles open source sur Hugging Face et les modèles locaux.  
Vous pouvez également utiliser [Ollama](https://ollama.com) ou [LlamaEdge](https://llamaedge.com) pour appeler des modèles quantifiés. Ollama permet aux utilisateurs individuels d'appeler différents modèles quantifiés, tandis que LlamaEdge offre une disponibilité multiplateforme pour les modèles GGUF.

## **Modèles quantifiés :**
De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour l'inférence locale. Par exemple, vous pouvez exécuter directement Ollama run Phi-3 ou le configurer hors ligne à l'aide d'un Modelfile. Le Modelfile spécifie le chemin du fichier GGUF et le format du prompt.

## **Possibilités d'IA générative :**
La combinaison de SLM comme Phi-3-mini ouvre de nouvelles possibilités pour l'IA générative. L'inférence n'est que la première étape ; ces modèles peuvent être utilisés pour diverses tâches dans des scénarios contraints en ressources, en latence et en coûts.

## **Libérer le potentiel de l'IA générative avec Phi-3-mini : Un guide pour l'inférence et le déploiement**  
Apprenez à utiliser Semantic Kernel, Ollama/LlamaEdge et ONNX Runtime pour accéder aux modèles Phi-3-mini et les inférer, et explorez les possibilités de l'IA générative dans divers scénarios d'application.

**Fonctionnalités**  
Effectuer une inférence avec le modèle Phi-3-mini dans :

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

En résumé, Phi-3-mini permet aux développeurs d'explorer différents formats de modèles et de tirer parti de l'IA générative dans divers scénarios d'application.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.