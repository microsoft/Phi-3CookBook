# Phi-3.5-Instruct WebGPU RAG Chatbot

## Démonstration pour présenter WebGPU et le modèle RAG

Le modèle RAG avec Phi-3.5 Onnx Hosted utilise l'approche de génération augmentée par récupération, combinant la puissance des modèles Phi-3.5 avec l'hébergement ONNX pour des déploiements d'IA efficaces. Ce modèle est essentiel pour affiner les modèles pour des tâches spécifiques à un domaine, offrant un mélange de qualité, de rentabilité et de compréhension sur de longs contextes. Il fait partie de la suite Azure AI, proposant une large sélection de modèles faciles à trouver, tester et utiliser, répondant aux besoins de personnalisation de diverses industries.

## Qu'est-ce que WebGPU
WebGPU est une API graphique web moderne conçue pour offrir un accès efficace au processeur graphique (GPU) d’un appareil directement depuis les navigateurs web. Elle est destinée à succéder à WebGL, offrant plusieurs améliorations clés :

1. **Compatibilité avec les GPU modernes** : WebGPU est conçu pour fonctionner de manière fluide avec les architectures GPU contemporaines, en s’appuyant sur des API système comme Vulkan, Metal et Direct3D 12.
2. **Performances améliorées** : Elle prend en charge les calculs GPU à usage général et des opérations plus rapides, ce qui la rend adaptée tant au rendu graphique qu’aux tâches d’apprentissage automatique.
3. **Fonctionnalités avancées** : WebGPU donne accès à des capacités GPU plus avancées, permettant des charges de travail graphiques et computationnelles plus complexes et dynamiques.
4. **Réduction de la charge de travail JavaScript** : En déléguant davantage de tâches au GPU, WebGPU réduit considérablement la charge de travail sur JavaScript, offrant de meilleures performances et une expérience plus fluide.

WebGPU est actuellement pris en charge dans des navigateurs comme Google Chrome, avec des travaux en cours pour étendre cette prise en charge à d'autres plateformes.

### 03.WebGPU
Environnement requis :

**Navigateurs pris en charge :**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Activer WebGPU :

- Dans Chrome/Microsoft Edge  

Activez le drapeau `chrome://flags/#enable-unsafe-webgpu`.

#### Ouvrir votre navigateur :
Lancez Google Chrome ou Microsoft Edge.

#### Accéder à la page des drapeaux :
Dans la barre d'adresse, tapez `chrome://flags` et appuyez sur Entrée.

#### Rechercher le drapeau :
Dans la boîte de recherche en haut de la page, tapez 'enable-unsafe-webgpu'.

#### Activer le drapeau :
Trouvez le drapeau #enable-unsafe-webgpu dans la liste des résultats.

Cliquez sur le menu déroulant à côté et sélectionnez Enabled.

#### Redémarrer votre navigateur :

Après avoir activé le drapeau, vous devrez redémarrer votre navigateur pour que les modifications prennent effet. Cliquez sur le bouton Relancer qui apparaît en bas de la page.

- Pour Linux, lancez le navigateur avec `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) a WebGPU activé par défaut.  
- Dans Firefox Nightly, entrez about:config dans la barre d'adresse et `set dom.webgpu.enabled to true`.

### Configuration du GPU pour Microsoft Edge 

Voici les étapes pour configurer un GPU haute performance pour Microsoft Edge sous Windows :

- **Ouvrir les paramètres :** Cliquez sur le menu Démarrer et sélectionnez Paramètres.  
- **Paramètres système :** Allez dans Système, puis Affichage.  
- **Paramètres graphiques :** Faites défiler vers le bas et cliquez sur Paramètres graphiques.  
- **Choisir l'application :** Sous « Choisir une application pour définir les préférences », sélectionnez Application de bureau, puis Parcourir.  
- **Sélectionner Edge :** Accédez au dossier d'installation de Edge (généralement `C:\Program Files (x86)\Microsoft\Edge\Application`) et sélectionnez `msedge.exe`.  
- **Définir la préférence :** Cliquez sur Options, choisissez Haute performance, puis cliquez sur Enregistrer.  
Cela garantira que Microsoft Edge utilise votre GPU haute performance pour de meilleures performances.  
- **Redémarrez** votre machine pour que ces paramètres prennent effet.

### Exemples : Veuillez [cliquer sur ce lien](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.