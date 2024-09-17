### Guidance-AI et Phi Models en tant que Service (MaaS)

Nous apportons [Guidance](https://github.com/guidance-ai/guidance) à l'offre de point de terminaison sans serveur Phi-3.5-mini dans Azure AI Studio pour rendre les sorties plus prévisibles en définissant la structure adaptée à une application. Avec Guidance, vous pouvez éliminer les réessais coûteux et, par exemple, contraindre le modèle à sélectionner parmi des listes prédéfinies (par exemple, des codes médicaux), restreindre les sorties à des citations directes du contexte fourni, ou suivre un regex quelconque. Guidance dirige le modèle token par token dans la pile d'inférence, réduisant les coûts et la latence de 30 à 50 %, ce qui en fait un ajout unique et précieux au [point de terminaison sans serveur Phi-3-mini](https://aka.ms/try-phi3.5mini).

## [**Guidance-AI**](https://github.com/guidance-ai/guidance) est un cadre conçu pour aider les développeurs à créer et déployer des modèles d'IA de manière efficace. Il se concentre sur la fourniture d'outils et de meilleures pratiques pour construire des applications d'IA robustes.

Lorsqu'il est combiné avec **Phi Models en tant que Service (MaaS)**, il offre une solution puissante pour déployer des petits modèles de langage (SLM) à la fois rentables et performants.

**Guidance-AI** est un cadre de programmation conçu pour aider les développeurs à contrôler et diriger les grands modèles de langage (LLM) de manière plus efficace. Il permet une structuration précise des sorties, réduisant la latence et le coût par rapport aux méthodes traditionnelles de prompting ou de fine-tuning.

### Caractéristiques Clés de Guidance-AI :
- **Contrôle Efficace** : Permet aux développeurs de contrôler comment le modèle de langage génère du texte, assurant des sorties de haute qualité et pertinentes.
- **Réduction des Coûts et de la Latence** : Optimise le processus de génération pour être plus rentable et rapide.
- **Intégration Flexible** : Fonctionne avec divers backends, y compris Transformers, llama.cpp, AzureAI, VertexAI, et OpenAI.
- **Structures de Sortie Riches** : Supporte des structures de sortie complexes comme des conditionnels, des boucles et l'utilisation d'outils, facilitant la génération de résultats clairs et analysables.
- **Compatibilité** : Permet à un seul programme Guidance d'être exécuté sur plusieurs backends, améliorant ainsi la flexibilité et la facilité d'utilisation.

### Exemples d'Utilisation :
- **Génération Contrainte** : Utilisation de regex et de grammaires sans contexte pour guider la sortie du modèle.
- **Intégration d'Outils** : Entrelacement automatique du contrôle et de la génération, comme l'utilisation d'une calculatrice dans une tâche de génération de texte.

Pour plus d'informations détaillées et des exemples, vous pouvez consulter le [répertoire GitHub de Guidance-AI](https://github.com/guidance-ai/guidance).

[Consultez l'exemple Phi-3.5](../../../../code/01.Introduce/guidance.ipynb)

### Caractéristiques Clés des Modèles Phi :
1. **Rentable** : Conçu pour être abordable tout en maintenant une haute performance.
2. **Faible Latence** : Idéal pour les applications en temps réel nécessitant des réponses rapides.
3. **Flexibilité** : Peut être déployé dans divers environnements, y compris le cloud, l'edge, et les scénarios hors ligne.
4. **Personnalisation** : Les modèles peuvent être ajustés avec des données spécifiques au domaine pour améliorer les performances.
5. **Sécurité et Conformité** : Construit avec les principes d'IA de Microsoft, assurant responsabilité, transparence, équité, fiabilité, sécurité, confidentialité, et inclusivité.

### Phi Models en tant que Service (MaaS) :
Les modèles Phi sont disponibles via un système de facturation à l'utilisation via des API d'inférence, facilitant leur intégration dans vos applications sans coûts initiaux significatifs.

### Commencer avec Phi-3 :
Pour commencer à utiliser les modèles Phi, vous pouvez explorer le [catalogue de modèles Azure AI](https://ai.azure.com/explore/models) ou les [modèles du GitHub Marketplace](https://github.com/marketplace/models) qui offrent des modèles préconstruits et personnalisables. De plus, vous pouvez utiliser des outils comme [Azure AI Studio](https://ai.azure.com) pour développer et déployer vos applications d'IA.

### Ressources
[Exemple de Notebook pour commencer avec Guidance](../../../../code/01.Introduce/guidance.ipynb)

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.