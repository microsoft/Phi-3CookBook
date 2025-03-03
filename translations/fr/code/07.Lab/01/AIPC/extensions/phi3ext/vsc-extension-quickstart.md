# Bienvenue dans votre extension VS Code

## Contenu du dossier

* Ce dossier contient tous les fichiers nécessaires à votre extension.
* `package.json` - c'est le fichier manifeste dans lequel vous déclarez votre extension et votre commande.
  * Le plugin d'exemple enregistre une commande et définit son titre et son nom. Avec ces informations, VS Code peut afficher la commande dans la palette de commandes. Il n'est pas encore nécessaire de charger le plugin.
* `src/extension.ts` - c'est le fichier principal où vous fournirez l'implémentation de votre commande.
  * Le fichier exporte une fonction, `activate`, qui est appelée la toute première fois que votre extension est activée (dans ce cas, en exécutant la commande). À l'intérieur de la fonction `activate`, nous appelons `registerCommand`.
  * Nous passons la fonction contenant l'implémentation de la commande comme second paramètre à `registerCommand`.

## Configuration

* Installez les extensions recommandées (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, et dbaeumer.vscode-eslint).

## Lancez-vous immédiatement

* Appuyez sur `F5` pour ouvrir une nouvelle fenêtre avec votre extension chargée.
* Exécutez votre commande depuis la palette de commandes en appuyant sur (`Ctrl+Shift+P` ou `Cmd+Shift+P` sur Mac) et en tapant `Hello World`.
* Placez des points d'arrêt dans votre code à l'intérieur de `src/extension.ts` pour déboguer votre extension.
* Retrouvez la sortie de votre extension dans la console de débogage.

## Apportez des modifications

* Vous pouvez relancer l'extension depuis la barre d'outils de débogage après avoir modifié le code dans `src/extension.ts`.
* Vous pouvez également recharger (`Ctrl+R` ou `Cmd+R` sur Mac) la fenêtre VS Code avec votre extension pour appliquer vos modifications.

## Explorez l'API

* Vous pouvez ouvrir l'ensemble complet de notre API en ouvrant le fichier `node_modules/@types/vscode/index.d.ts`.

## Exécutez des tests

* Installez le [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Exécutez la tâche "watch" via la commande **Tâches : Exécuter une tâche**. Assurez-vous que celle-ci est en cours d'exécution, sinon les tests pourraient ne pas être détectés.
* Ouvrez la vue Test depuis la barre d'activité et cliquez sur le bouton "Exécuter le test", ou utilisez le raccourci `Ctrl/Cmd + ; A`.
* Consultez les résultats des tests dans la vue Résultats des tests.
* Apportez des modifications à `src/test/extension.test.ts` ou créez de nouveaux fichiers de test dans le dossier `test`.
  * Le runner de tests fourni ne prendra en compte que les fichiers correspondant au modèle de nommage `**.test.ts`.
  * Vous pouvez créer des dossiers dans le dossier `test` pour structurer vos tests comme vous le souhaitez.

## Allez plus loin

* Réduisez la taille de l'extension et améliorez le temps de démarrage en [regroupant votre extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publiez votre extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) sur la marketplace des extensions VS Code.
* Automatisez les builds en configurant [l'intégration continue](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.