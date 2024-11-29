# **Laissez Phi-3 devenir un expert de l'industrie**

Pour intégrer le modèle Phi-3 dans une industrie, vous devez ajouter des données commerciales spécifiques à l'industrie au modèle Phi-3. Nous avons deux options différentes, la première est RAG (Retrieval Augmented Generation) et la seconde est le Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG est la récupération de données + génération de texte. Les données structurées et non structurées de l'entreprise sont stockées dans la base de données vectorielle. Lors de la recherche de contenu pertinent, le résumé et le contenu pertinents sont trouvés pour former un contexte, et la capacité de complétion de texte de LLM/SLM est combinée pour générer du contenu.

### **Fine-tuning**

Le Fine-tuning est basé sur l'amélioration d'un certain modèle. Il n'est pas nécessaire de commencer par l'algorithme du modèle, mais les données doivent être continuellement accumulées. Si vous souhaitez des terminologies et des expressions linguistiques plus précises dans les applications industrielles, le Fine-tuning est votre meilleur choix. Mais si vos données changent fréquemment, le Fine-tuning peut devenir compliqué.

### **Comment choisir**

1. Si notre réponse nécessite l'introduction de données externes, RAG est le meilleur choix

2. Si vous avez besoin de produire des connaissances industrielles stables et précises, le Fine-tuning sera un bon choix. RAG privilégie la récupération de contenu pertinent mais peut ne pas toujours capter les nuances spécialisées.

3. Le Fine-tuning nécessite un ensemble de données de haute qualité, et si ce n'est qu'une petite gamme de données, cela ne fera pas beaucoup de différence. RAG est plus flexible

4. Le Fine-tuning est une boîte noire, une métaphysique, et il est difficile de comprendre le mécanisme interne. Mais RAG peut rendre plus facile de trouver la source des données, permettant ainsi d'ajuster efficacement les hallucinations ou les erreurs de contenu et d'offrir une meilleure transparence.

### **Scénarios**

1. Les industries verticales nécessitent un vocabulaire et des expressions professionnels spécifiques, ***Fine-tuning*** sera le meilleur choix

2. Système de questions-réponses, impliquant la synthèse de différents points de connaissance, ***RAG*** sera le meilleur choix

3. La combinaison du flux de travail automatisé ***RAG + Fine-tuning*** est le meilleur choix

## **Comment utiliser RAG**

![rag](../../../../translated_images/RAG.099c3f3bc644ff2d8bb61d2fbc20a532958c6a1e4d1cb65a84edeb4ffe618bbb.fr.png)

Une base de données vectorielle est une collection de données stockées sous forme mathématique. Les bases de données vectorielles facilitent la mémorisation des entrées précédentes par les modèles d'apprentissage automatique, permettant d'utiliser l'apprentissage automatique pour prendre en charge des cas d'utilisation tels que la recherche, les recommandations et la génération de texte. Les données peuvent être identifiées en fonction de métriques de similarité plutôt que de correspondances exactes, permettant aux modèles informatiques de comprendre le contexte des données.

La base de données vectorielle est la clé pour réaliser RAG. Nous pouvons convertir les données en stockage vectoriel grâce à des modèles vectoriels tels que text-embedding-3, jina-ai-embedding, etc.

En savoir plus sur la création d'application RAG [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Comment utiliser le Fine-tuning**

Les algorithmes couramment utilisés dans le Fine-tuning sont Lora et QLora. Comment choisir ?
- [En savoir plus avec cet exemple de notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script de FineTuning en Python](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora et QLora**

![lora](../../../../translated_images/qlora.ea4ce73918753819dc9e9cf1524ac40faa555d6b21168b667064be93c3913bbe.fr.png)

LoRA (Low-Rank Adaptation) et QLoRA (Quantized Low-Rank Adaptation) sont deux techniques utilisées pour affiner les grands modèles de langage (LLMs) en utilisant le Fine Tuning efficace en paramètres (PEFT). Les techniques PEFT sont conçues pour entraîner les modèles plus efficacement que les méthodes traditionnelles. 
LoRA est une technique de Fine Tuning autonome qui réduit l'empreinte mémoire en appliquant une approximation de faible rang à la matrice de mise à jour des poids. Elle offre des temps d'entraînement rapides et maintient des performances proches des méthodes de Fine Tuning traditionnelles.

QLoRA est une version étendue de LoRA qui intègre des techniques de quantification pour réduire encore plus l'utilisation de la mémoire. QLoRA quantifie la précision des paramètres de poids dans le LLM pré-entraîné à une précision de 4 bits, ce qui est plus efficace en mémoire que LoRA. Cependant, l'entraînement de QLoRA est environ 30 % plus lent que celui de LoRA en raison des étapes supplémentaires de quantification et de déquantification.

QLoRA utilise LoRA comme accessoire pour corriger les erreurs introduites lors des erreurs de quantification. QLoRA permet d'affiner des modèles massifs avec des milliards de paramètres sur des GPU relativement petits et très disponibles. Par exemple, QLoRA peut affiner un modèle de 70B paramètres qui nécessite 36 GPU avec seulement 2.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.