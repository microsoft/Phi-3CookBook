# Contribuer

Ce projet accueille avec plaisir les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA), déclarant que vous avez le droit de nous accorder les droits d'utiliser votre contribution. Pour plus de détails, visitez [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir un CLA et annotera la PR en conséquence (par exemple, vérification de statut, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de faire cela qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Code de Conduite

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Pour plus d'informations, consultez la [FAQ du Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Précautions pour créer des issues

Veuillez ne pas ouvrir d'issues GitHub pour des questions générales de support, car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs. Cela nous permet de suivre plus facilement les problèmes ou bugs réels liés au code et de séparer les discussions générales du code lui-même.

## Comment contribuer

### Directives pour les Pull Requests

Lorsque vous soumettez une pull request (PR) au dépôt Phi-3 CookBook, veuillez suivre les directives suivantes :

- **Forker le dépôt** : Forkez toujours le dépôt dans votre propre compte avant de faire vos modifications.

- **Séparer les pull requests (PR)** :
  - Soumettez chaque type de modification dans une PR distincte. Par exemple, les corrections de bugs et les mises à jour de documentation doivent être soumises dans des PR séparées.
  - Les corrections de fautes de frappe et les mises à jour mineures de documentation peuvent être combinées dans une seule PR si nécessaire.

- **Gérer les conflits de fusion** : Si votre pull request présente des conflits de fusion, mettez à jour votre branche locale `main` pour refléter le dépôt principal avant de faire vos modifications.

- **Soumissions de traductions** : Lorsque vous soumettez une PR de traduction, assurez-vous que le dossier de traduction contient les traductions pour tous les fichiers du dossier original.

### Directives pour les traductions

> [!IMPORTANT]
>
> Lors de la traduction de texte dans ce dépôt, n'utilisez pas de traduction automatique. Ne contribuez qu'aux traductions dans les langues que vous maîtrisez.

Si vous maîtrisez une langue autre que l'anglais, vous pouvez aider à traduire le contenu. Pour que vos contributions de traduction soient correctement intégrées, veuillez suivre les étapes suivantes :

- **Créer un dossier de traduction** : Accédez au dossier de la section appropriée et créez un dossier de traduction pour la langue à laquelle vous contribuez. Par exemple :
  - Pour la section introduction : `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Pour la section démarrage rapide : `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Continuez ce modèle pour les autres sections (03.Inference, 04.Finetuning, etc.)

- **Mettre à jour les chemins relatifs** : Lors de la traduction, ajustez la structure des dossiers en ajoutant `../../` au début des chemins relatifs dans les fichiers markdown pour garantir le bon fonctionnement des liens. Par exemple, modifiez comme suit :
  - Changez `(../../imgs/01/phi3aisafety.png)` en `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser vos traductions** : Chaque fichier traduit doit être placé dans le dossier de traduction correspondant à la section. Par exemple, si vous traduisez la section introduction en espagnol, vous devez créer ce qui suit :
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Soumettre une PR complète** : Assurez-vous que tous les fichiers traduits pour une section sont inclus dans une seule PR. Nous n'acceptons pas les traductions partielles pour une section. Lors de la soumission d'une PR de traduction, assurez-vous que le dossier de traduction contient les traductions pour tous les fichiers du dossier original.

### Directives de rédaction

Pour garantir la cohérence dans tous les documents, veuillez suivre les directives suivantes :

- **Formatage des URL** : Encadrez toutes les URL entre crochets carrés suivis de parenthèses, sans espaces supplémentaires autour ou à l'intérieur. Par exemple : `[example](https://example.com)`.

- **Liens relatifs** : Utilisez `./` pour les liens relatifs pointant vers des fichiers ou dossiers dans le répertoire actuel, et `../` pour ceux dans un répertoire parent. Par exemple : `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales non spécifiques à un pays** : Assurez-vous que vos liens n'incluent pas de locales spécifiques à un pays. Par exemple, évitez `/en-us/` ou `/en/`.

- **Stockage des images** : Stockez toutes les images dans le dossier `./imgs`.

- **Noms d'images descriptifs** : Nommez les images de manière descriptive en utilisant des caractères anglais, des chiffres et des tirets. Par exemple : `example-image.jpg`.

## Workflows GitHub

Lorsque vous soumettez une pull request, les workflows suivants seront déclenchés pour valider les modifications. Suivez les instructions ci-dessous pour vous assurer que votre pull request passe les vérifications des workflows :

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Vérification des chemins relatifs incorrects

Ce workflow vérifie que tous les chemins relatifs dans vos fichiers sont corrects.

1. Pour vous assurer que vos liens fonctionnent correctement, effectuez les tâches suivantes avec VS Code :
    - Survolez n'importe quel lien dans vos fichiers.
    - Appuyez sur **Ctrl + Clic** pour naviguer vers le lien.
    - Si vous cliquez sur un lien et qu'il ne fonctionne pas localement, cela déclenchera le workflow et ne fonctionnera pas sur GitHub.

1. Pour corriger ce problème, effectuez les tâches suivantes en utilisant les suggestions de chemin fournies par VS Code :
    - Tapez `./` ou `../`.
    - VS Code vous proposera des options disponibles basées sur ce que vous avez tapé.
    - Suivez le chemin en cliquant sur le fichier ou dossier souhaité pour vous assurer que votre chemin est correct.

Une fois que vous avez ajouté le chemin relatif correct, enregistrez et poussez vos modifications.

### Vérification des URLs sans locale

Ce workflow vérifie que toute URL web n'inclut pas de locale spécifique à un pays. Étant donné que ce dépôt est accessible globalement, il est important de s'assurer que les URLs ne contiennent pas la locale de votre pays.

1. Pour vérifier que vos URLs n'ont pas de locales de pays, effectuez les tâches suivantes :

    - Recherchez des textes comme `/en-us/`, `/en/`, ou toute autre locale linguistique dans les URLs.
    - Si ces éléments ne sont pas présents dans vos URLs, alors vous passerez cette vérification.

1. Pour corriger ce problème, effectuez les tâches suivantes :
    - Ouvrez le chemin de fichier mis en évidence par le workflow.
    - Supprimez la locale de pays des URLs.

Une fois que vous avez supprimé la locale de pays, enregistrez et poussez vos modifications.

### Vérification des URLs incorrectes

Ce workflow vérifie que toute URL web dans vos fichiers fonctionne et retourne un code de statut 200.

1. Pour vérifier que vos URLs fonctionnent correctement, effectuez les tâches suivantes :
    - Vérifiez le statut des URLs dans vos fichiers.

2. Pour corriger les URLs incorrectes, effectuez les tâches suivantes :
    - Ouvrez le fichier contenant l'URL incorrecte.
    - Mettez à jour l'URL avec la bonne.

Une fois que vous avez corrigé les URLs, enregistrez et poussez vos modifications.

> [!NOTE]
>
> Il peut y avoir des cas où la vérification des URLs échoue même si le lien est accessible. Cela peut se produire pour plusieurs raisons, notamment :
>
> - **Restrictions réseau** : Les serveurs d'actions GitHub peuvent avoir des restrictions réseau empêchant l'accès à certaines URLs.
> - **Problèmes de délai d'attente** : Les URLs qui mettent trop de temps à répondre peuvent déclencher une erreur de délai d'attente dans le workflow.
> - **Problèmes temporaires de serveur** : Des pannes de serveur ou des maintenances occasionnelles peuvent rendre une URL temporairement indisponible lors de la validation.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.