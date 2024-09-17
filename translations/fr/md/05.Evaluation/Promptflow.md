# **Introduction à Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) est un outil visuel d'automatisation de flux de travail qui permet aux utilisateurs de créer des flux automatisés en utilisant des modèles préconstruits et des connecteurs personnalisés. Il est conçu pour permettre aux développeurs et aux analystes métiers de créer rapidement des processus automatisés pour des tâches telles que la gestion des données, la collaboration et l'optimisation des processus. Avec Prompt Flow, les utilisateurs peuvent facilement connecter différents services, applications et systèmes, et automatiser des processus métiers complexes.

Microsoft Prompt Flow est conçu pour rationaliser le cycle de développement de bout en bout des applications d'IA alimentées par des modèles de langage de grande taille (LLM). Que vous soyez en train d'idéation, de prototypage, de test, d'évaluation ou de déploiement d'applications basées sur les LLM, Prompt Flow simplifie le processus et vous permet de créer des applications LLM de qualité production.

## Voici les principales fonctionnalités et avantages de l'utilisation de Microsoft Prompt Flow :

**Expérience d'Auteur Interactive**

Prompt Flow offre une représentation visuelle de la structure de votre flux, facilitant la compréhension et la navigation dans vos projets.
Il propose une expérience de codage semblable à un notebook pour un développement et un débogage de flux efficaces.

**Variantes de Prompt et Ajustement**

Créez et comparez plusieurs variantes de prompt pour faciliter un processus de raffinement itératif. Évaluez la performance des différents prompts et choisissez les plus efficaces.

**Flux d'Évaluation Intégrés**

Évaluez la qualité et l'efficacité de vos prompts et flux à l'aide des outils d'évaluation intégrés.
Comprenez comment vos applications basées sur les LLM se comportent.

**Ressources Complètes**

Prompt Flow inclut une bibliothèque d'outils, d'exemples et de modèles intégrés. Ces ressources servent de point de départ pour le développement, inspirent la créativité et accélèrent le processus.

**Collaboration et Préparation à l'Entreprise**

Soutenez la collaboration d'équipe en permettant à plusieurs utilisateurs de travailler ensemble sur des projets d'ingénierie de prompt.
Maintenez le contrôle des versions et partagez les connaissances efficacement. Rationalisez l'ensemble du processus d'ingénierie de prompt, du développement et de l'évaluation au déploiement et à la surveillance.

## Évaluation dans Prompt Flow

Dans Microsoft Prompt Flow, l'évaluation joue un rôle crucial dans l'évaluation des performances de vos modèles d'IA. Explorons comment vous pouvez personnaliser les flux et les métriques d'évaluation dans Prompt Flow :

![PFVizualise](../../../../translated_images/pfvisualize.e96398930e67b609687d11081caa625eb4313ff62e91998913a9df3cee641688.fr.png)

**Comprendre l'Évaluation dans Prompt Flow**

Dans Prompt Flow, un flux représente une séquence de nœuds qui traitent des entrées et génèrent des sorties. Les flux d'évaluation sont des types spéciaux de flux conçus pour évaluer les performances d'une exécution en fonction de critères et d'objectifs spécifiques.

**Principales caractéristiques des flux d'évaluation**

Ils fonctionnent généralement après le flux testé, en utilisant ses sorties. Ils calculent des scores ou des métriques pour mesurer les performances du flux testé. Les métriques peuvent inclure la précision, les scores de pertinence ou toute autre mesure pertinente.

### Personnalisation des Flux d'Évaluation

**Définition des Entrées**

Les flux d'évaluation doivent prendre en compte les sorties de l'exécution testée. Définissez les entrées de manière similaire aux flux standard.
Par exemple, si vous évaluez un flux de QnA, nommez une entrée "answer". Si vous évaluez un flux de classification, nommez une entrée "category". Des entrées de vérité terrain (par exemple, des étiquettes réelles) peuvent également être nécessaires.

**Sorties et Métriques**

Les flux d'évaluation produisent des résultats qui mesurent les performances du flux testé. Les métriques peuvent être calculées en utilisant Python ou LLM (Large Language Models). Utilisez la fonction log_metric() pour enregistrer les métriques pertinentes.

**Utilisation des Flux d'Évaluation Personnalisés**

Développez votre propre flux d'évaluation adapté à vos tâches et objectifs spécifiques. Personnalisez les métriques en fonction de vos objectifs d'évaluation.
Appliquez ce flux d'évaluation personnalisé aux exécutions en lot pour des tests à grande échelle.

## Méthodes d'Évaluation Intégrées

Prompt Flow propose également des méthodes d'évaluation intégrées.
Vous pouvez soumettre des exécutions en lot et utiliser ces méthodes pour évaluer les performances de votre flux avec de grands ensembles de données.
Consultez les résultats de l'évaluation, comparez les métriques et itérez selon les besoins.
N'oubliez pas, l'évaluation est essentielle pour garantir que vos modèles d'IA répondent aux critères et objectifs souhaités. Consultez la documentation officielle pour des instructions détaillées sur le développement et l'utilisation des flux d'évaluation dans Microsoft Prompt Flow.

En résumé, Microsoft Prompt Flow permet aux développeurs de créer des applications LLM de haute qualité en simplifiant l'ingénierie des prompts et en fournissant un environnement de développement robuste. Si vous travaillez avec des LLM, Prompt Flow est un outil précieux à explorer. Consultez les [Documents d'Évaluation de Prompt Flow](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) pour des instructions détaillées sur le développement et l'utilisation des flux d'évaluation dans Microsoft Prompt Flow.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.