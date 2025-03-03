# Bienvenue dans votre extension VS Code

## Contenu du dossier

* Ce dossier contient tous les fichiers nécessaires pour votre extension.
* `package.json` - c'est le fichier manifeste dans lequel vous déclarez votre extension et votre commande.
  * Le plugin d'exemple enregistre une commande et définit son titre ainsi que son nom. Avec ces informations, VS Code peut afficher la commande dans la palette de commandes. Il n'est pas encore nécessaire de charger le plugin.
* `src/extension.ts` - c'est le fichier principal où vous fournirez l'implémentation de votre commande.
  * Le fichier exporte une fonction, `activate`, qui est appelée la toute première fois que votre extension est activée (dans ce cas, en exécutant la commande). À l'intérieur de la fonction `activate`, nous appelons `registerCommand`.
  * Nous passons la fonction contenant l'implémentation de la commande comme second paramètre à `registerCommand`.

## Configuration

* Installez les extensions recommandées (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, et dbaeumer.vscode-eslint).

## Démarrez rapidement

* Appuyez sur `F5` pour ouvrir une nouvelle fenêtre avec votre extension chargée.
* Exécutez votre commande depuis la palette de commandes en appuyant sur (`Ctrl+Shift+P` ou `Cmd+Shift+P` sur Mac) et en tapant `Hello World`.
* Placez des points d'arrêt dans votre code à l'intérieur de `src/extension.ts` pour déboguer votre extension.
* Retrouvez la sortie de votre extension dans la console de débogage.

## Apportez des modifications

* Vous pouvez relancer l'extension depuis la barre d'outils de débogage après avoir modifié le code dans `src/extension.ts`.
* Vous pouvez également recharger (`Ctrl+R` ou `Cmd+R` sur Mac) la fenêtre VS Code avec votre extension pour appliquer vos modifications.

## Explorez l'API

* Vous pouvez accéder à l'ensemble complet de notre API en ouvrant le fichier `node_modules/@types/vscode/index.d.ts`.

## Exécuter des tests

* Installez le [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Exécutez la tâche "watch" via la commande **Tasks: Run Task**. Assurez-vous que cette tâche est en cours d'exécution, sinon les tests pourraient ne pas être détectés.
* Ouvrez la vue Testing depuis la barre d'activité et cliquez sur le bouton "Run Test", ou utilisez le raccourci `Ctrl/Cmd + ; A`.
* Consultez les résultats des tests dans la vue des résultats de tests.
* Apportez des modifications à `src/test/extension.test.ts` ou créez de nouveaux fichiers de test dans le dossier `test`.
  * Le test runner fourni ne prendra en compte que les fichiers correspondant au modèle de nommage `**.test.ts`.
  * Vous pouvez créer des dossiers à l'intérieur du dossier `test` pour organiser vos tests comme vous le souhaitez.

## Aller plus loin

* Réduisez la taille de l'extension et améliorez le temps de démarrage en [regroupant votre extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiez votre extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) sur le marketplace des extensions VS Code.
* Automatisez les builds en configurant [l'intégration continue](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.