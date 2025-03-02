**Ajustement fin de Phi-3 avec QLoRA**

Ajustement fin du modèle de langage Phi-3 Mini de Microsoft à l’aide de [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA permettra d’améliorer la compréhension des conversations et la génération de réponses.

Pour charger des modèles en 4 bits avec transformers et bitsandbytes, vous devez installer accelerate et transformers depuis la source, et vous assurer d’avoir la dernière version de la bibliothèque bitsandbytes.

**Exemples**
- [En savoir plus avec cet exemple de notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script d’ajustement fin en Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemple d’ajustement fin sur Hugging Face Hub avec LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemple d’ajustement fin sur Hugging Face Hub avec QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.