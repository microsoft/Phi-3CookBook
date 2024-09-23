# **Présentation du Service Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) est un service cloud conçu pour accélérer et gérer le cycle de vie des projets de machine learning (ML).

Les professionnels du ML, les data scientists et les ingénieurs peuvent l'utiliser dans leurs flux de travail quotidiens pour :

- Entraîner et déployer des modèles.
- Gérer les opérations de machine learning (MLOps).
- Vous pouvez créer un modèle dans Azure Machine Learning ou utiliser un modèle construit à partir d'une plateforme open-source, telle que PyTorch, TensorFlow ou scikit-learn.
- Les outils MLOps vous aident à surveiller, réentraîner et redéployer les modèles.

## Pour qui est Azure Machine Learning ?

**Data Scientists et Ingénieurs ML**

Ils peuvent utiliser des outils pour accélérer et automatiser leurs flux de travail quotidiens.
Azure ML offre des fonctionnalités pour l'équité, l'explicabilité, le suivi et l'auditabilité.
Développeurs d'Applications :
Ils peuvent intégrer des modèles dans des applications ou des services de manière transparente.

**Développeurs de Plateformes**

Ils ont accès à un ensemble d'outils robustes soutenus par les API durables d'Azure Resource Manager.
Ces outils permettent de construire des outils ML avancés.

**Entreprises**

En travaillant dans le cloud Microsoft Azure, les entreprises bénéficient d'une sécurité familière et d'un contrôle d'accès basé sur les rôles.
Configurez des projets pour contrôler l'accès aux données protégées et aux opérations spécifiques.

## Productivité pour Tous les Membres de l'Équipe
Les projets ML nécessitent souvent une équipe avec un ensemble de compétences variées pour les construire et les maintenir.

Azure ML fournit des outils qui vous permettent de :
- Collaborer avec votre équipe via des notebooks partagés, des ressources de calcul, du calcul sans serveur, des données et des environnements.
- Développer des modèles avec équité, explicabilité, suivi et auditabilité pour répondre aux exigences de traçabilité et de conformité des audits.
- Déployer des modèles ML rapidement et facilement à grande échelle, et les gérer et les gouverner efficacement avec MLOps.
- Exécuter des charges de travail de machine learning n'importe où avec une gouvernance, une sécurité et une conformité intégrées.

## Outils de Plateforme Intercompatibles

Tous les membres d'une équipe ML peuvent utiliser leurs outils préférés pour accomplir leur travail.
Que vous exécutiez des expériences rapides, régliez des hyperparamètres, construisiez des pipelines ou gériez des inférences, vous pouvez utiliser des interfaces familières, notamment :
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

Au fur et à mesure que vous affinez les modèles et collaborez tout au long du cycle de développement, vous pouvez partager et trouver des ressources, des ressources et des métriques dans l'interface utilisateur d'Azure Machine Learning studio.

## **LLM/SLM dans Azure ML**

Azure ML a ajouté de nombreuses fonctions liées à LLM/SLM, combinant LLMOps et SLMOps pour créer une plateforme de technologie d'intelligence artificielle générative à l'échelle de l'entreprise.

### **Catalogue de Modèles**

Les utilisateurs d'entreprise peuvent déployer différents modèles en fonction de différents scénarios commerciaux via le Catalogue de Modèles, et fournir des services en tant que Model as Service pour que les développeurs ou utilisateurs d'entreprise puissent y accéder.

![models](../../../../translated_images/models.cb8d085cb832f2d0d8b24e4c091e223d3aa6a585f5ab53747e8d3db7ed3d2446.fr.png)

Le Catalogue de Modèles dans Azure Machine Learning studio est le centre pour découvrir et utiliser une large gamme de modèles qui vous permettent de construire des applications d'IA générative. Le catalogue de modèles propose des centaines de modèles provenant de fournisseurs de modèles tels que Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, y compris des modèles entraînés par Microsoft. Les modèles provenant de fournisseurs autres que Microsoft sont des Produits Non-Microsoft, tels que définis dans les Conditions des Produits de Microsoft, et soumis aux conditions fournies avec le modèle.

### **Pipeline de Tâches**

Le cœur d'un pipeline de machine learning consiste à diviser une tâche de machine learning complète en un flux de travail à plusieurs étapes. Chaque étape est un composant gérable qui peut être développé, optimisé, configuré et automatisé individuellement. Les étapes sont connectées par des interfaces bien définies. Le service de pipeline Azure Machine Learning orchestre automatiquement toutes les dépendances entre les étapes du pipeline.

Lors du fine-tuning SLM / LLM, nous pouvons gérer nos processus de données, d'entraînement et de génération via Pipeline.

![finetuning](../../../../translated_images/finetuning.45db682d7f536aeb2a5f38d7bd8a42e61d02b6729f6d39df7a97ff4fad4c42b6.fr.png)

### **Flux de Prompts**

Avantages de l'utilisation du flux de prompts Azure Machine Learning
Azure Machine Learning prompt flow offre une gamme d'avantages qui aident les utilisateurs à passer de l'idéation à l'expérimentation et, finalement, à des applications prêtes pour la production basées sur LLM :

**Agilité de l'ingénierie des prompts**

Expérience de création interactive : Azure Machine Learning prompt flow fournit une représentation visuelle de la structure du flux, permettant aux utilisateurs de comprendre et de naviguer facilement dans leurs projets. Il offre également une expérience de codage semblable à celle des notebooks pour un développement et un débogage efficaces des flux.
Variantes pour le réglage des prompts : Les utilisateurs peuvent créer et comparer plusieurs variantes de prompts, facilitant un processus de raffinement itératif.

Évaluation : Les flux d'évaluation intégrés permettent aux utilisateurs d'évaluer la qualité et l'efficacité de leurs prompts et flux.

Ressources complètes : Azure Machine Learning prompt flow comprend une bibliothèque d'outils, d'exemples et de modèles intégrés qui servent de point de départ pour le développement, inspirant la créativité et accélérant le processus.

**Prêt pour l'entreprise pour les applications basées sur LLM**

Collaboration : Azure Machine Learning prompt flow prend en charge la collaboration en équipe, permettant à plusieurs utilisateurs de travailler ensemble sur des projets d'ingénierie de prompts, de partager des connaissances et de maintenir le contrôle de version.

Plateforme tout-en-un : Azure Machine Learning prompt flow rationalise l'ensemble du processus d'ingénierie des prompts, du développement et de l'évaluation au déploiement et à la surveillance. Les utilisateurs peuvent déployer sans effort leurs flux en tant que points de terminaison Azure Machine Learning et surveiller leurs performances en temps réel, garantissant un fonctionnement optimal et une amélioration continue.

Solutions de Prêt pour l'Entreprise Azure Machine Learning : Prompt flow tire parti des solutions robustes de préparation pour l'entreprise d'Azure Machine Learning, offrant une base sécurisée, évolutive et fiable pour le développement, l'expérimentation et le déploiement des flux.

Avec Azure Machine Learning prompt flow, les utilisateurs peuvent libérer leur agilité en ingénierie des prompts, collaborer efficacement et tirer parti des solutions de qualité entreprise pour le développement et le déploiement réussis d'applications basées sur LLM.

En combinant la puissance de calcul, les données et les différents composants d'Azure ML, les développeurs d'entreprise peuvent facilement créer leurs propres applications d'intelligence artificielle.

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.