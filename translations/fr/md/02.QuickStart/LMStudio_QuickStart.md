# **Utilisation de Phi-3 dans LM Studio**

[LM Studio](https://lmstudio.ai) est une application pour appeler SLM et LLM dans une application de bureau locale. Elle permet aux utilisateurs d'utiliser facilement différents modèles et prend en charge le calcul accéléré avec GPU NVIDIA/AMD/Apple Silicon. Grâce à LM Studio, les utilisateurs peuvent télécharger, installer et exécuter divers LLM et SLM open source basés sur Hugging Face pour tester les performances des modèles localement sans coder.

## **1. Installation**

![LMStudio](../../../../translated_images/LMStudio.87422bdb03d330dc05137ba237dd0cb43f7964245b848a466ab1730de93bc4db.fr.png)

Vous pouvez choisir d'installer sous Windows, Linux, macOS via le site web de LM Studio [https://lmstudio.ai/](https://lmstudio.ai/)

## **2. Télécharger Phi-3 dans LM Studio**

LM Studio appelle des modèles open source au format gguf quantifié. Vous pouvez le télécharger directement depuis la plateforme fournie par l'interface de recherche de LM Studio, ou vous pouvez le télécharger vous-même et le spécifier pour être appelé dans le répertoire concerné.

***Nous recherchons Phi3 dans la recherche de LM Studio et téléchargeons le modèle gguf Phi-3***

![LMStudioSearch](../../../../translated_images/LMStudio_Search.1e577e0f69f336fc26e56653eeec2a20b90c3895cc4aa2ff05b6ec51059f12fd.fr.png)

***Gérer les modèles téléchargés via LM Studio***

![LMStudioLocal](../../../../translated_images/LMStudio_Local.55f9d6f61eb27f0f37fc4833599aa43fa45a66dfc20444ba1419a922b60b5005.fr.png)

## **3. Discuter avec Phi-3 dans LM Studio**

Nous sélectionnons Phi-3 dans LM Studio Chat et configurons le modèle de discussion (Preset - Phi3) pour commencer une discussion locale avec Phi-3

![LMStudioChat](../../../../translated_images/LMStudio_Chat.1bdc3a8f804f12d9548b386448c1642b741c10816576973155a90ef55f8a9c8d.fr.png)

***Remarque*** :

a. Vous pouvez définir des paramètres via la Configuration Avancée dans le panneau de contrôle de LM Studio

b. Comme Phi-3 a des exigences spécifiques en matière de modèle de discussion, Phi-3 doit être sélectionné dans Preset

c. Vous pouvez également définir différents paramètres, tels que l'utilisation du GPU, etc.

## **4. Appeler l'API Phi-3 depuis LM Studio**

LM Studio prend en charge le déploiement rapide de services locaux, et vous pouvez créer des services de modèles sans coder.

![LMStudioServer](../../../../translated_images/LMStudio_Server.917c115e12599e7698ce323085ce4f8bdb020665656bbe90edca2d45a7de932d.fr.png)

Voici le résultat dans Postman

![LMStudioPostman](../../../../translated_images/LMStudio_Postman.4481aa4873ecaae0e05032f539090897002fc9aca9da5d1336fb28776f4c45a7.fr.png)

