Phi-3-mini WebGPU RAG Chatbot

## Démo pour présenter WebGPU et le modèle RAG
Le modèle RAG avec le modèle hébergé Phi-3 Onnx exploite l'approche de la génération augmentée par la récupération, combinant la puissance des modèles Phi-3 avec l'hébergement ONNX pour des déploiements d'IA efficaces. Ce modèle est essentiel pour affiner les modèles pour des tâches spécifiques à un domaine, offrant un mélange de qualité, de rentabilité et de compréhension de contextes longs. Il fait partie de la suite Azure AI, offrant une large sélection de modèles faciles à trouver, essayer et utiliser, répondant aux besoins de personnalisation de diverses industries. Les modèles Phi-3, y compris Phi-3-mini, Phi-3-small et Phi-3-medium, sont disponibles sur le catalogue de modèles Azure AI et peuvent être affinés et déployés de manière autonome ou via des plateformes comme HuggingFace et ONNX, démontrant l'engagement de Microsoft envers des solutions d'IA accessibles et efficaces.

## Qu'est-ce que WebGPU
WebGPU est une API graphique web moderne conçue pour fournir un accès efficace au processeur graphique (GPU) d'un appareil directement depuis les navigateurs web. Elle est destinée à succéder à WebGL, offrant plusieurs améliorations clés :

1. **Compatibilité avec les GPU modernes** : WebGPU est conçu pour fonctionner parfaitement avec les architectures GPU contemporaines, en utilisant des API système comme Vulkan, Metal et Direct3D 12.
2. **Performance améliorée** : Elle prend en charge les calculs GPU à usage général et les opérations plus rapides, ce qui la rend adaptée à la fois au rendu graphique et aux tâches d'apprentissage automatique.
3. **Fonctionnalités avancées** : WebGPU donne accès à des capacités GPU plus avancées, permettant des charges de travail graphiques et computationnelles plus complexes et dynamiques.
4. **Réduction de la charge de travail JavaScript** : En déchargeant plus de tâches sur le GPU, WebGPU réduit considérablement la charge de travail sur JavaScript, conduisant à de meilleures performances et des expériences plus fluides.

WebGPU est actuellement pris en charge dans des navigateurs comme Google Chrome, avec des travaux en cours pour étendre la prise en charge à d'autres plateformes.

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

Cliquez sur le menu déroulant à côté et sélectionnez Enabled.

#### Redémarrez votre navigateur :

Après avoir activé le drapeau, vous devrez redémarrer votre navigateur pour que les modifications prennent effet. Cliquez sur le bouton Relancer qui apparaît en bas de la page.

- Pour Linux, lancez le navigateur avec `--enable-features=Vulkan`.
- Safari 18 (macOS 15) a WebGPU activé par défaut.
- Dans Firefox Nightly, entrez about:config dans la barre d'adresse et `set dom.webgpu.enabled to true`.

### Configurer le GPU pour Microsoft Edge 

Voici les étapes pour configurer un GPU haute performance pour Microsoft Edge sur Windows :

- **Ouvrez les paramètres :** Cliquez sur le menu Démarrer et sélectionnez Paramètres.
- **Paramètres système :** Allez dans Système puis Affichage.
- **Paramètres graphiques :** Faites défiler vers le bas et cliquez sur Paramètres graphiques.
- **Choisir une application :** Sous "Choisir une application à définir la préférence", sélectionnez Application de bureau puis Parcourir.
- **Sélectionnez Edge :** Naviguez jusqu'au dossier d'installation de Edge (généralement `C:\Program Files (x86)\Microsoft\Edge\Application`) et sélectionnez `msedge.exe`.
- **Définir la préférence :** Cliquez sur Options, choisissez Haute performance, puis cliquez sur Enregistrer.
Cela garantira que Microsoft Edge utilise votre GPU haute performance pour de meilleures performances.
- **Redémarrez** votre machine pour que ces paramètres prennent effet.

### Ouvrez votre Codespace :
Naviguez jusqu'à votre dépôt sur GitHub.
Cliquez sur le bouton Code et sélectionnez Ouvrir avec Codespaces.

Si vous n'avez pas encore de Codespace, vous pouvez en créer un en cliquant sur Nouveau codespace.

**Note** Installer l'environnement Node dans votre codespace
Exécuter une démo npm depuis un GitHub Codespace est un excellent moyen de tester et développer votre projet. Voici un guide étape par étape pour vous aider à démarrer :

### Configurez votre environnement :
Une fois votre Codespace ouvert, assurez-vous que Node.js et npm sont installés. Vous pouvez vérifier cela en exécutant :
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
Utilisez le terminal pour naviguer jusqu'au répertoire où se trouve votre projet npm :
```
cd path/to/your/project
```

### Installer les dépendances :
Exécutez la commande suivante pour installer toutes les dépendances nécessaires répertoriées dans votre fichier package.json :

```
npm install
```

### Exécuter la démo :
Une fois les dépendances installées, vous pouvez exécuter votre script de démo. Cela est généralement spécifié dans la section scripts de votre package.json. Par exemple, si votre script de démo s'appelle start, vous pouvez exécuter :

```
npm run build
```
```
npm run dev
```

### Accéder à la démo :
Si votre démo implique un serveur web, Codespaces fournira une URL pour y accéder. Cherchez une notification ou vérifiez l'onglet Ports pour trouver l'URL.

**Note:** Le modèle doit être mis en cache dans le navigateur, donc cela peut prendre un certain temps pour se charger.

### Démo RAG
Téléchargez le fichier markdown `intro_rag.md` pour compléter la solution RAG. Si vous utilisez Codespaces, vous pouvez télécharger le fichier situé dans `01.InferencePhi3/docs/`

### Sélectionnez votre fichier :
Cliquez sur le bouton qui dit "Choisir un fichier" pour sélectionner le document que vous souhaitez télécharger.

### Téléchargez le document :
Après avoir sélectionné votre fichier, cliquez sur le bouton "Télécharger" pour charger votre document pour RAG (Génération augmentée par la récupération).

### Commencez votre chat :
Une fois le document téléchargé, vous pouvez démarrer une session de chat en utilisant RAG basé sur le contenu de votre document.

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.