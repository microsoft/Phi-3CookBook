# **Introduction de l'exemple E2E**

Cet exemple importe les données de [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) pour affiner le modèle Phi-3-mini. Voici l'architecture :

![arch](../../../../translated_images/arch.9993118a26f2f7367f8fbd75fa2c4ed75c503905d5662dc87818f7752be17716.fr.png)

## **Introduction**

Nous espérons utiliser l'ensemble de données de [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) pour que Phi-3-mini réponde à nos questions de manière plus professionnelle. C'est votre premier projet E2E utilisant Phi-3-mini.

### **Prérequis**

1. Python 3.10+
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **Connaissances**

1. [Apprenez à connaître Phi-3](../01.Introduce/Phi3Family.md)
2. [Apprenez à utiliser Microsoft Olive pour l'affinage](../04.Fine-tuning/FineTuning_MicrosoftOlive.md)
3. [Apprenez à utiliser ONNX Runtime pour l'IA générative](https://github.com/microsoft/onnxruntime-genai)

Avertissement : La traduction a été réalisée à partir de son original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.