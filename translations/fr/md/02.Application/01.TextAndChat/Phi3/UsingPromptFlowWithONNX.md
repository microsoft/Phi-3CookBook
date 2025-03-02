# Utiliser le GPU Windows pour créer une solution Prompt Flow avec Phi-3.5-Instruct ONNX 

Le document suivant est un exemple d'utilisation de PromptFlow avec ONNX (Open Neural Network Exchange) pour développer des applications d'IA basées sur les modèles Phi-3.

PromptFlow est une suite d'outils de développement conçue pour simplifier le cycle de développement complet des applications d'IA basées sur des modèles de langage de grande taille (LLM), depuis l'idéation et le prototypage jusqu'aux phases de test et d'évaluation.

En intégrant PromptFlow avec ONNX, les développeurs peuvent :

- **Optimiser les performances du modèle** : Exploitez ONNX pour une inférence et un déploiement efficaces des modèles.
- **Simplifier le développement** : Utilisez PromptFlow pour gérer les flux de travail et automatiser les tâches répétitives.
- **Améliorer la collaboration** : Facilitez la collaboration entre les membres de l'équipe grâce à un environnement de développement unifié.

**Prompt Flow** est une suite d'outils de développement conçue pour simplifier le cycle de développement complet des applications d'IA basées sur des LLM, depuis l'idéation, le prototypage, les tests, l'évaluation, jusqu'au déploiement en production et au suivi. Il facilite l'ingénierie des prompts et permet de créer des applications LLM de qualité production.

Prompt Flow peut se connecter à OpenAI, Azure OpenAI Service et à des modèles personnalisables (Huggingface, LLM/SLM locaux). Nous espérons déployer le modèle ONNX quantifié de Phi-3.5 dans des applications locales. Prompt Flow peut nous aider à mieux planifier nos activités et à réaliser des solutions locales basées sur Phi-3.5. Dans cet exemple, nous combinerons la bibliothèque ONNX Runtime GenAI pour compléter la solution Prompt Flow sur un GPU Windows.

## **Installation**

### **ONNX Runtime GenAI pour GPU Windows**

Lisez ce guide pour configurer ONNX Runtime GenAI pour GPU Windows [cliquez ici](./ORTWindowGPUGuideline.md)

### **Configurer Prompt Flow dans VSCode**

1. Installez l'extension VS Code Prompt Flow.

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.fr.png)

2. Après avoir installé l'extension VS Code Prompt Flow, cliquez sur l'extension et choisissez **Installation dependencies**. Suivez ce guide pour installer le SDK Prompt Flow dans votre environnement.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.fr.png)

3. Téléchargez [le code exemple](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) et utilisez VS Code pour ouvrir cet exemple.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.fr.png)

4. Ouvrez **flow.dag.yaml** pour choisir votre environnement Python.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.fr.png)

   Ouvrez **chat_phi3_ort.py** pour modifier l'emplacement de votre modèle Phi-3.5-Instruct ONNX.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.fr.png)

5. Exécutez votre Prompt Flow pour effectuer des tests.

Ouvrez **flow.dag.yaml** et cliquez sur l'éditeur visuel.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.fr.png)

Après avoir cliqué, exécutez-le pour tester.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.fr.png)

1. Vous pouvez exécuter un lot dans le terminal pour vérifier plus de résultats.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Vous pouvez consulter les résultats dans votre navigateur par défaut.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.fr.png)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.