### Guidance-AI et les modèles Phi en tant que service (MaaS)
Nous apportons [Guidance](https://github.com/guidance-ai/guidance) à l'offre de point de terminaison sans serveur Phi-3.5-mini dans Azure AI Foundry pour rendre les sorties plus prévisibles en définissant la structure adaptée à une application. Avec Guidance, vous pouvez éliminer les réessais coûteux et, par exemple, contraindre le modèle à sélectionner à partir de listes prédéfinies (par exemple, des codes médicaux), restreindre les sorties à des citations directes du contexte fourni, ou suivre n'importe quel regex. Guidance dirige le modèle token par token dans la pile d'inférence, réduisant les coûts et la latence de 30 à 50 %, ce qui en fait un complément unique et précieux au [point de terminaison sans serveur Phi-3-mini](https://aka.ms/try-phi3.5mini).

## [**Guidance-AI**](https://github.com/guidance-ai/guidance) est un framework conçu pour aider les développeurs à créer et déployer des modèles d'IA de manière efficace. Il se concentre sur la fourniture d'outils et de meilleures pratiques pour construire des applications d'IA robustes.

Lorsqu'il est combiné avec **Phi Models as a Service (MaaS)**, il offre une solution puissante pour déployer des petits modèles de langage (SLM) à la fois rentables et performants.

**Guidance-AI** est un framework de programmation conçu pour aider les développeurs à contrôler et orienter les grands modèles de langage (LLM) plus efficacement. Il permet une structuration précise des sorties, réduisant la latence et les coûts par rapport aux méthodes traditionnelles de prompting ou de fine-tuning.

### Principales caractéristiques de Guidance-AI :
- **Contrôle efficace** : Permet aux développeurs de contrôler la génération de texte par le modèle de langage, garantissant des sorties de haute qualité et pertinentes.
- **Réduction des coûts et de la latence** : Optimise le processus de génération pour être plus rentable et rapide.
- **Intégration flexible** : Fonctionne avec divers backends, y compris Transformers, llama.cpp, AzureAI, VertexAI et OpenAI.
- **Structures de sortie riches** : Prend en charge des structures de sortie complexes comme des conditionnels, des boucles et l'utilisation d'outils, facilitant la génération de résultats clairs et analysables.
- **Compatibilité** : Permet à un seul programme Guidance d'être exécuté sur plusieurs backends, améliorant ainsi la flexibilité et la facilité d'utilisation.

### Exemples d'utilisation :
- **Génération contrainte** : Utilisation d'expressions régulières et de grammaires sans contexte pour guider la sortie du modèle.
- **Intégration d'outils** : Intercalation automatique de contrôle et de génération, comme l'utilisation d'une calculatrice dans une tâche de génération de texte.

Pour plus d'informations détaillées et des exemples, vous pouvez consulter le [dépôt GitHub de Guidance-AI](https://github.com/guidance-ai/guidance).

[Consultez l'exemple de Phi-3.5](../../../../code/01.Introduce/guidance.ipynb)

### Principales caractéristiques des modèles Phi :
1. **Rentable** : Conçu pour être abordable tout en maintenant des performances élevées.
2. **Faible latence** : Idéal pour les applications en temps réel nécessitant des réponses rapides.
3. **Flexibilité** : Peut être déployé dans divers environnements, y compris le cloud, l'edge et les scénarios hors ligne.
4. **Personnalisation** : Les modèles peuvent être ajustés avec des données spécifiques au domaine pour améliorer les performances.
5. **Sécurité et conformité** : Construit avec les principes d'IA de Microsoft, garantissant responsabilité, transparence, équité, fiabilité, sécurité, confidentialité et inclusivité.

### Modèles Phi en tant que service (MaaS) :
Les modèles Phi sont disponibles via un système de facturation à l'utilisation via des API d'inférence, ce qui facilite leur intégration dans vos applications sans coûts initiaux significatifs.

### Commencer avec Phi-3 :
Pour commencer à utiliser les modèles Phi, vous pouvez explorer le [catalogue de modèles Azure AI](https://ai.azure.com/explore/models) ou le [GitHub Marketplace Models](https://github.com/marketplace/models) qui propose des modèles préconstruits et personnalisables. De plus, vous pouvez utiliser des outils comme [Azure AI Foundry](https://ai.azure.com) pour développer et déployer vos applications d'IA.

### Ressources
[Exemple de notebook pour commencer avec Guidance](../../../../code/01.Introduce/guidance.ipynb)

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatisée par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.