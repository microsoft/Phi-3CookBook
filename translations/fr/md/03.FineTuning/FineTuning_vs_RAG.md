## Ajustement fin vs RAG

## Génération augmentée par récupération

RAG combine la récupération de données et la génération de texte. Les données structurées et non structurées de l'entreprise sont stockées dans une base de données vectorielle. Lors de la recherche de contenu pertinent, un résumé et un contenu associés sont identifiés pour former un contexte, et la capacité de complétion de texte de LLM/SLM est utilisée pour générer du contenu.

## Processus RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.fr.png)

## Ajustement fin
L'ajustement fin repose sur l'amélioration d'un modèle existant. Il n'est pas nécessaire de repartir de l'algorithme du modèle, mais il faut accumuler des données en continu. Si vous recherchez une terminologie précise et une expression linguistique adaptée aux applications industrielles, l'ajustement fin est une meilleure option. Cependant, si vos données évoluent fréquemment, l'ajustement fin peut devenir complexe.

## Comment choisir
Si notre réponse nécessite l'intégration de données externes, RAG est le meilleur choix.

Si vous devez produire des connaissances industrielles stables et précises, l'ajustement fin sera une bonne option. RAG privilégie la récupération de contenu pertinent mais peut parfois manquer de nuances spécialisées.

L'ajustement fin nécessite un jeu de données de haute qualité, et si les données concernent un domaine restreint, cela n'apportera pas de grande différence. RAG est plus flexible.  
L'ajustement fin est une "boîte noire", une sorte de métaphysique, et il est difficile d'en comprendre le mécanisme interne. En revanche, RAG permet de mieux identifier la source des données, ce qui facilite la correction des hallucinations ou des erreurs de contenu et offre une meilleure transparence.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.