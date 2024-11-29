# **Présentation de Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) est un outil visuel d'automatisation des flux de travail qui permet aux utilisateurs de créer des workflows automatisés en utilisant des modèles préconstruits et des connecteurs personnalisés. Il est conçu pour permettre aux développeurs et aux analystes commerciaux de créer rapidement des processus automatisés pour des tâches telles que la gestion des données, la collaboration et l'optimisation des processus. Avec Prompt Flow, les utilisateurs peuvent facilement connecter différents services, applications et systèmes, et automatiser des processus métier complexes.

Microsoft Prompt Flow est conçu pour rationaliser le cycle de développement complet des applications d'IA alimentées par des modèles de langage étendus (LLM). Que vous soyez en train de concevoir, prototyper, tester, évaluer ou déployer des applications basées sur les LLM, Prompt Flow simplifie le processus et vous permet de créer des applications LLM de qualité production.

## Voici les principales caractéristiques et avantages de l'utilisation de Microsoft Prompt Flow :

**Expérience de création interactive**

Prompt Flow offre une représentation visuelle de la structure de votre flux, ce qui facilite la compréhension et la navigation dans vos projets.
Il propose une expérience de codage similaire à celle des notebooks pour un développement et un débogage efficaces des flux.

**Variantes de prompts et ajustement**

Créez et comparez plusieurs variantes de prompts pour faciliter un processus de raffinement itératif. Évaluez la performance de différents prompts et choisissez les plus efficaces.

**Flux d'évaluation intégrés**
Évaluez la qualité et l'efficacité de vos prompts et flux en utilisant des outils d'évaluation intégrés.
Comprenez la performance de vos applications basées sur les LLM.

**Ressources complètes**

Prompt Flow inclut une bibliothèque d'outils intégrés, d'exemples et de modèles. Ces ressources servent de point de départ pour le développement, inspirent la créativité et accélèrent le processus.

**Collaboration et préparation à l'entreprise**

Soutenez la collaboration en équipe en permettant à plusieurs utilisateurs de travailler ensemble sur des projets d'ingénierie de prompts.
Maintenez le contrôle des versions et partagez les connaissances efficacement. Rationalisez l'ensemble du processus d'ingénierie de prompts, du développement et de l'évaluation au déploiement et à la surveillance.

## Évaluation dans Prompt Flow 

Dans Microsoft Prompt Flow, l'évaluation joue un rôle crucial dans l'évaluation des performances de vos modèles d'IA. Explorons comment vous pouvez personnaliser les flux d'évaluation et les métriques dans Prompt Flow :

![PFVizualise](../../../../translated_images/pfvisualize.e96398930e67b609687d11081caa625eb4313ff62e91998913a9df3cee641688.fr.png)

**Comprendre l'évaluation dans Prompt Flow**

Dans Prompt Flow, un flux représente une séquence de nœuds qui traitent l'entrée et génèrent une sortie. Les flux d'évaluation sont des types spéciaux de flux conçus pour évaluer la performance d'un exécution en fonction de critères et d'objectifs spécifiques.

**Caractéristiques clés des flux d'évaluation**

Ils s'exécutent généralement après le flux testé, en utilisant ses sorties. Ils calculent des scores ou des métriques pour mesurer la performance du flux testé. Les métriques peuvent inclure la précision, les scores de pertinence ou toute autre mesure pertinente.

### Personnalisation des flux d'évaluation

**Définition des entrées**

Les flux d'évaluation doivent prendre en compte les sorties de l'exécution testée. Définissez les entrées de manière similaire aux flux standard.
Par exemple, si vous évaluez un flux de questions-réponses, nommez une entrée "réponse". Si vous évaluez un flux de classification, nommez une entrée "catégorie". Des entrées de vérité terrain (par exemple, des étiquettes réelles) peuvent également être nécessaires.

**Sorties et métriques**

Les flux d'évaluation produisent des résultats qui mesurent la performance du flux testé. Les métriques peuvent être calculées en utilisant Python ou des LLM (modèles de langage étendus). Utilisez la fonction log_metric() pour enregistrer les métriques pertinentes.

**Utilisation des flux d'évaluation personnalisés**

Développez votre propre flux d'évaluation adapté à vos tâches et objectifs spécifiques. Personnalisez les métriques en fonction de vos objectifs d'évaluation.
Appliquez ce flux d'évaluation personnalisé à des exécutions par lot pour des tests à grande échelle.

## Méthodes d'évaluation intégrées

Prompt Flow propose également des méthodes d'évaluation intégrées.
Vous pouvez soumettre des exécutions par lot et utiliser ces méthodes pour évaluer la performance de votre flux avec de grands ensembles de données.
Consultez les résultats d'évaluation, comparez les métriques et itérez au besoin.
N'oubliez pas, l'évaluation est essentielle pour garantir que vos modèles d'IA répondent aux critères et objectifs souhaités. Consultez la documentation officielle pour des instructions détaillées sur le développement et l'utilisation des flux d'évaluation dans Microsoft Prompt Flow.

En résumé, Microsoft Prompt Flow permet aux développeurs de créer des applications LLM de haute qualité en simplifiant l'ingénierie des prompts et en fournissant un environnement de développement robuste. Si vous travaillez avec des LLM, Prompt Flow est un outil précieux à explorer. Consultez les [Documents d'évaluation de Prompt Flow](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) pour des instructions détaillées sur le développement et l'utilisation des flux d'évaluation dans Microsoft Prompt Flow.

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatisée par IA. Bien que nous nous efforcions d'atteindre une précision maximale, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.