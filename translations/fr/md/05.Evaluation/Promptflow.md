# **Présentation de Promptflow**

 [Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) est un outil d'automatisation de flux de travail visuel qui permet aux utilisateurs de créer des flux de travail automatisés en utilisant des modèles préconstruits et des connecteurs personnalisés. Il est conçu pour permettre aux développeurs et aux analystes commerciaux de créer rapidement des processus automatisés pour des tâches telles que la gestion des données, la collaboration et l'optimisation des processus. Avec Prompt Flow, les utilisateurs peuvent facilement connecter différents services, applications et systèmes, et automatiser des processus métier complexes.

 Microsoft Prompt Flow est conçu pour rationaliser le cycle de développement de bout en bout des applications d'IA alimentées par des modèles de langage de grande taille (LLM). Que vous soyez en phase d'idéation, de prototypage, de test, d'évaluation ou de déploiement d'applications basées sur LLM, Prompt Flow simplifie le processus et vous permet de créer des applications LLM de qualité production.

## Voici les principales fonctionnalités et avantages de l'utilisation de Microsoft Prompt Flow :

**Expérience de création interactive**

Prompt Flow fournit une représentation visuelle de la structure de votre flux, facilitant ainsi la compréhension et la navigation dans vos projets.
Il offre une expérience de codage similaire à un carnet de notes pour un développement et un débogage de flux efficaces.

**Variantes de prompt et ajustement**

Créez et comparez plusieurs variantes de prompt pour faciliter un processus de raffinement itératif. Évaluez les performances des différents prompts et choisissez les plus efficaces.

**Flux d'évaluation intégrés**
Évaluez la qualité et l'efficacité de vos prompts et flux à l'aide d'outils d'évaluation intégrés.
Comprenez à quel point vos applications basées sur LLM performent.

**Ressources complètes**

Prompt Flow inclut une bibliothèque d'outils intégrés, d'exemples et de modèles. Ces ressources servent de point de départ pour le développement, inspirent la créativité et accélèrent le processus.

**Collaboration et préparation à l'entreprise**

Soutenez la collaboration en équipe en permettant à plusieurs utilisateurs de travailler ensemble sur des projets d'ingénierie de prompt.
Maintenez le contrôle des versions et partagez les connaissances de manière efficace. Rationalisez l'ensemble du processus d'ingénierie de prompt, du développement et de l'évaluation au déploiement et à la surveillance.

## Évaluation dans Prompt Flow 

Dans Microsoft Prompt Flow, l'évaluation joue un rôle crucial dans l'évaluation des performances de vos modèles d'IA. Explorons comment vous pouvez personnaliser les flux et les métriques d'évaluation dans Prompt Flow :

![PFVizualise](../../../../translated_images/pfvisualize.e96398930e67b609687d11081caa625eb4313ff62e91998913a9df3cee641688.fr.png)

**Comprendre l'évaluation dans Prompt Flow**

Dans Prompt Flow, un flux représente une séquence de nœuds qui traitent les entrées et génèrent des sorties. Les flux d'évaluation sont des types spéciaux de flux conçus pour évaluer les performances d'une exécution en fonction de critères et d'objectifs spécifiques.

**Caractéristiques clés des flux d'évaluation**

Ils fonctionnent généralement après le flux testé, en utilisant ses sorties. Ils calculent des scores ou des métriques pour mesurer les performances du flux testé. Les métriques peuvent inclure la précision, les scores de pertinence ou toute autre mesure pertinente.

### Personnalisation des flux d'évaluation

**Définir les entrées**

Les flux d'évaluation doivent prendre en compte les sorties de l'exécution testée. Définissez les entrées de manière similaire aux flux standard.
Par exemple, si vous évaluez un flux de questions-réponses, nommez une entrée "answer". Si vous évaluez un flux de classification, nommez une entrée "category". Des entrées de vérité terrain (par exemple, des étiquettes réelles) peuvent également être nécessaires.

**Sorties et métriques**

Les flux d'évaluation produisent des résultats qui mesurent les performances du flux testé. Les métriques peuvent être calculées en utilisant Python ou LLM (Large Language Models). Utilisez la fonction log_metric() pour enregistrer les métriques pertinentes.

**Utilisation des flux d'évaluation personnalisés**

Développez votre propre flux d'évaluation adapté à vos tâches et objectifs spécifiques. Personnalisez les métriques en fonction de vos objectifs d'évaluation.
Appliquez ce flux d'évaluation personnalisé aux exécutions par lot pour des tests à grande échelle.

## Méthodes d'évaluation intégrées

Prompt Flow propose également des méthodes d'évaluation intégrées.
Vous pouvez soumettre des exécutions par lot et utiliser ces méthodes pour évaluer les performances de votre flux avec de grands ensembles de données.
Consultez les résultats de l'évaluation, comparez les métriques et itérez selon les besoins.
N'oubliez pas que l'évaluation est essentielle pour garantir que vos modèles d'IA répondent aux critères et objectifs souhaités. Explorez la documentation officielle pour des instructions détaillées sur le développement et l'utilisation des flux d'évaluation dans Microsoft Prompt Flow.

En résumé, Microsoft Prompt Flow permet aux développeurs de créer des applications LLM de haute qualité en simplifiant l'ingénierie des prompts et en fournissant un environnement de développement robuste. Si vous travaillez avec des LLM, Prompt Flow est un outil précieux à explorer. Consultez les [Documents d'évaluation de Prompt Flow](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) pour des instructions détaillées sur le développement et l'utilisation des flux d'évaluation dans Microsoft Prompt Flow.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.