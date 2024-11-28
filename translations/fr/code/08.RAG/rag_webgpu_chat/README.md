Phi-3-mini WebGPU RAG Chatbot

## Démo pour présenter WebGPU et le modèle RAG
Le modèle RAG avec le modèle hébergé Phi-3 Onnx utilise l'approche de génération augmentée par récupération, combinant la puissance des modèles Phi-3 avec l'hébergement ONNX pour des déploiements IA efficaces. Ce modèle est essentiel pour affiner les modèles pour des tâches spécifiques à un domaine, offrant un mélange de qualité, de rentabilité et de compréhension de contextes longs. Il fait partie de la suite Azure AI, offrant une large sélection de modèles faciles à trouver, essayer et utiliser, répondant aux besoins de personnalisation de diverses industries. Les modèles Phi-3, y compris Phi-3-mini, Phi-3-small et Phi-3-medium, sont disponibles sur le catalogue de modèles Azure AI et peuvent être affinés et déployés en autogestion ou via des plateformes comme HuggingFace et ONNX, montrant l'engagement de Microsoft pour des solutions IA accessibles et efficaces.

## Qu'est-ce que WebGPU
WebGPU est une API graphique web moderne conçue pour fournir un accès efficace au processeur graphique (GPU) d'un appareil directement depuis les navigateurs web. Elle est destinée à succéder à WebGL, offrant plusieurs améliorations clés :

1. **Compatibilité avec les GPU modernes** : WebGPU est conçu pour fonctionner de manière transparente avec les architectures GPU contemporaines, utilisant des API système comme Vulkan, Metal et Direct3D 12.
2. **Performances améliorées** : Elle prend en charge les calculs GPU à usage général et les opérations plus rapides, la rendant adaptée à la fois au rendu graphique et aux tâches d'apprentissage automatique.
3. **Fonctionnalités avancées** : WebGPU donne accès à des capacités GPU plus avancées, permettant des charges de travail graphiques et computationnelles plus complexes et dynamiques.
4. **Réduction de la charge de travail JavaScript** : En déléguant plus de tâches au GPU, WebGPU réduit considérablement la charge de travail sur JavaScript, conduisant à de meilleures performances et des expériences plus fluides.

WebGPU est actuellement pris en charge dans des navigateurs comme Google Chrome, avec des travaux en cours pour étendre le support à d'autres plateformes.

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

#### Ouvrez votre navigateur :
Lancez Google Chrome ou Microsoft Edge.

#### Accédez à la page des drapeaux :
Dans la barre d'adresse, tapez `chrome://flags` et appuyez sur Entrée.

#### Recherchez le drapeau :
Dans la boîte de recherche en haut de la page, tapez 'enable-unsafe-webgpu'

#### Activez le drapeau :
Trouvez le drapeau #enable-unsafe-webgpu dans la liste des résultats.

Cliquez sur le menu déroulant à côté et sélectionnez Activé.

#### Redémarrez votre navigateur :

Après avoir activé le drapeau, vous devrez redémarrer votre navigateur pour que les modifications prennent effet. Cliquez sur le bouton Relancer qui apparaît en bas de la page.

- Pour Linux, lancez le navigateur avec `--enable-features=Vulkan`.
- Safari 18 (macOS 15) a WebGPU activé par défaut.
- Dans Firefox Nightly, entrez about:config dans la barre d'adresse et `set dom.webgpu.enabled to true`.

### Configuration du GPU pour Microsoft Edge

Voici les étapes pour configurer un GPU haute performance pour Microsoft Edge sous Windows :

- **Ouvrir les paramètres** : Cliquez sur le menu Démarrer et sélectionnez Paramètres.
- **Paramètres système** : Allez dans Système puis Affichage.
- **Paramètres graphiques** : Faites défiler vers le bas et cliquez sur Paramètres graphiques.
- **Choisir l'application** : Sous “Choisir une application pour définir les préférences,” sélectionnez Application de bureau puis Parcourir.
- **Sélectionner Edge** : Naviguez jusqu'au dossier d'installation de Edge (généralement `C:\Program Files (x86)\Microsoft\Edge\Application`) et sélectionnez `msedge.exe`.
- **Définir les préférences** : Cliquez sur Options, choisissez Haute performance, puis cliquez sur Enregistrer.
Cela garantira que Microsoft Edge utilise votre GPU haute performance pour de meilleures performances.
- **Redémarrez** votre machine pour que ces paramètres prennent effet.

### Ouvrez votre Codespace :
Accédez à votre dépôt sur GitHub.
Cliquez sur le bouton Code et sélectionnez Ouvrir avec Codespaces.

Si vous n'avez pas encore de Codespace, vous pouvez en créer un en cliquant sur Nouveau codespace.

**Note** Installer l'environnement Node dans votre codespace
Exécuter une démo npm depuis un GitHub Codespace est un excellent moyen de tester et développer votre projet. Voici un guide étape par étape pour vous aider à démarrer :

### Configurez votre environnement :
Une fois votre Codespace ouvert, assurez-vous d'avoir Node.js et npm installés. Vous pouvez vérifier cela en exécutant :
```
node -v
```
```
npm -v
```

S'ils ne sont pas installés, vous pouvez les installer en utilisant :
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Naviguez vers votre répertoire de projet :
Utilisez le terminal pour naviguer vers le répertoire où se trouve votre projet npm :
```
cd path/to/your/project
```

### Installer les dépendances :
Exécutez la commande suivante pour installer toutes les dépendances nécessaires listées dans votre fichier package.json :

```
npm install
```

### Exécutez la démo :
Une fois les dépendances installées, vous pouvez exécuter votre script de démo. Cela est généralement spécifié dans la section scripts de votre package.json. Par exemple, si votre script de démo s'appelle start, vous pouvez l'exécuter avec :

```
npm run build
```
```
npm run dev
```

### Accédez à la démo :
Si votre démo implique un serveur web, Codespaces fournira une URL pour y accéder. Recherchez une notification ou consultez l'onglet Ports pour trouver l'URL.

**Note** Le modèle doit être mis en cache dans le navigateur, il peut donc prendre un certain temps pour se charger.

### Démo RAG
Téléchargez le fichier markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Sélectionnez votre fichier :
Cliquez sur le bouton "Choisir un fichier" pour sélectionner le document que vous souhaitez télécharger.

### Téléchargez le document :
Après avoir sélectionné votre fichier, cliquez sur le bouton "Télécharger" pour charger votre document pour RAG (Retrieval-Augmented Generation).

### Démarrez votre chat :
Une fois le document téléchargé, vous pouvez démarrer une session de chat utilisant RAG basé sur le contenu de votre document.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatisés par IA. Bien que nous nous efforcions d'atteindre une précision maximale, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.