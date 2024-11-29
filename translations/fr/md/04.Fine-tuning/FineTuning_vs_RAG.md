## Affinage vs RAG

## Génération Augmentée par Récupération

RAG est la récupération de données + génération de texte. Les données structurées et non structurées de l'entreprise sont stockées dans la base de données vectorielle. Lors de la recherche de contenu pertinent, le résumé et le contenu pertinents sont trouvés pour former un contexte, et la capacité de complétion de texte de LLM/SLM est combinée pour générer du contenu.

## Processus RAG
![FinetuningvsRAG](../../../../translated_images/rag.20124d5657be35073dd1dbc93411c24ed912cbcc3bab5d37d28e648e6f175b7e.fr.png)

## Affinage
L'affinage est basé sur l'amélioration d'un certain modèle. Il n'est pas nécessaire de commencer avec l'algorithme du modèle, mais les données doivent être continuellement accumulées. Si vous souhaitez une terminologie et une expression linguistique plus précises dans les applications industrielles, l'affinage est votre meilleur choix. Mais si vos données changent fréquemment, l'affinage peut devenir compliqué.

## Comment choisir
Si notre réponse nécessite l'introduction de données externes, RAG est le meilleur choix.

Si vous avez besoin de produire des connaissances industrielles stables et précises, l'affinage sera un bon choix. RAG privilégie l'extraction de contenu pertinent mais peut ne pas toujours capter les nuances spécialisées.

L'affinage nécessite un ensemble de données de haute qualité, et si ce n'est qu'une petite gamme de données, cela ne fera pas beaucoup de différence. RAG est plus flexible.
L'affinage est une boîte noire, une métaphysique, et il est difficile de comprendre le mécanisme interne. Mais RAG peut rendre plus facile de trouver la source des données, permettant ainsi d'ajuster efficacement les hallucinations ou les erreurs de contenu et de fournir une meilleure transparence.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.