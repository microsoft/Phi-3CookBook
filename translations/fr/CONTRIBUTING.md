# Contribuer

Ce projet accueille volontiers les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un
Contrat de Licence de Contributeur (CLA) déclarant que vous avez le droit de nous accorder les droits d'utiliser votre contribution. Pour plus de détails, visitez [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Lorsque vous soumettez une demande de tirage, un bot CLA déterminera automatiquement si vous devez fournir un CLA et décorera la PR en conséquence (par exemple, vérification de l'état, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de faire cela qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Code de Conduite

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/).
Pour plus d'informations, lisez la [FAQ du Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Précautions pour créer des issues

Veuillez ne pas ouvrir de issues GitHub pour des questions de support général car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs. De cette manière, nous pouvons plus facilement suivre les problèmes ou bugs réels du code et garder la discussion générale séparée du code réel.

## Comment Contribuer

### Directives pour les Demandes de Tirage

Lors de la soumission d'une demande de tirage (PR) au dépôt Phi-3 CookBook, veuillez suivre les directives suivantes :

- **Forker le Dépôt** : Forkez toujours le dépôt sur votre propre compte avant de faire vos modifications.

- **Séparer les demandes de tirage (PR)** :
  - Soumettez chaque type de changement dans sa propre demande de tirage. Par exemple, les corrections de bugs et les mises à jour de documentation doivent être soumises dans des PR séparées.
  - Les corrections de fautes de frappe et les mises à jour mineures de la documentation peuvent être combinées dans une seule PR si cela est approprié.

- **Gérer les conflits de fusion** : Si votre demande de tirage montre des conflits de fusion, mettez à jour votre branche locale `main` pour refléter le dépôt principal avant de faire vos modifications.

- **Soumissions de traductions** : Lors de la soumission d'une PR de traduction, assurez-vous que le dossier de traduction inclut les traductions de tous les fichiers du dossier original.

### Directives pour les Traductions

> [!IMPORTANT]
>
> Lors de la traduction de texte dans ce dépôt, n'utilisez pas de traduction automatique. Ne vous portez volontaire pour des traductions que dans des langues où vous êtes compétent.

Si vous êtes compétent dans une langue autre que l'anglais, vous pouvez aider à traduire le contenu. Suivez ces étapes pour vous assurer que vos contributions de traduction sont correctement intégrées, veuillez utiliser les directives suivantes :

- **Créer un dossier de traduction** : Naviguez vers le dossier de la section appropriée et créez un dossier de traduction pour la langue à laquelle vous contribuez. Par exemple :
  - Pour la section introduction : `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Pour la section démarrage rapide : `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Continuez ce schéma pour les autres sections (03.Inference, 04.Finetuning, etc.)

- **Mettre à jour les chemins relatifs** : Lors de la traduction, ajustez la structure des dossiers en ajoutant `../../` au début des chemins relatifs dans les fichiers markdown pour garantir que les liens fonctionnent correctement. Par exemple, changez comme suit :
  - Changez `(../../imgs/01/phi3aisafety.png)` en `(../../../../imgs/01/phi3aisafety.png)`

- **Organisez vos traductions** : Chaque fichier traduit doit être placé dans le dossier de traduction de la section correspondante. Par exemple, si vous traduisez la section introduction en espagnol, vous créeriez comme suit :
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Soumettre une PR complète** : Assurez-vous que tous les fichiers traduits pour une section sont inclus dans une seule PR. Nous n'acceptons pas les traductions partielles pour une section. Lors de la soumission d'une PR de traduction, assurez-vous que le dossier de traduction inclut les traductions de tous les fichiers du dossier original.

### Directives pour la Rédaction

Pour garantir la cohérence entre tous les documents, veuillez utiliser les directives suivantes :

- **Formatage des URL** : Enveloppez toutes les URL entre crochets suivis de parenthèses, sans espaces supplémentaires autour ou à l'intérieur. Par exemple : `[example](https://example.com)`.

- **Liens relatifs** : Utilisez `./` pour les liens relatifs pointant vers des fichiers ou des dossiers dans le répertoire courant, et `../` pour ceux dans un répertoire parent. Par exemple : `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales non spécifiques à un pays** : Assurez-vous que vos liens n'incluent pas de locales spécifiques à un pays. Par exemple, évitez `/en-us/` ou `/en/`.

- **Stockage des images** : Stockez toutes les images dans le dossier `./imgs`.

- **Noms d'images descriptifs** : Nommez les images de manière descriptive en utilisant des caractères anglais, des chiffres et des tirets. Par exemple : `example-image.jpg`.

## Workflows GitHub

Lorsque vous soumettez une demande de tirage, les workflows suivants seront déclenchés pour valider les modifications. Suivez les instructions ci-dessous pour vous assurer que votre demande de tirage passe les vérifications du workflow :

- [Vérifier les chemins relatifs cassés](../..)
- [Vérifier que les URLs n'ont pas de locale](../..)

### Vérifier les chemins relatifs cassés

Ce workflow garantit que tous les chemins relatifs dans vos fichiers sont corrects.

1. Pour vous assurer que vos liens fonctionnent correctement, effectuez les tâches suivantes en utilisant VS Code :
    - Survolez n'importe quel lien dans vos fichiers.
    - Appuyez sur **Ctrl + Clic** pour naviguer vers le lien.
    - Si vous cliquez sur un lien et qu'il ne fonctionne pas localement, cela déclenchera le workflow et ne fonctionnera pas sur GitHub.

1. Pour résoudre ce problème, effectuez les tâches suivantes en utilisant les suggestions de chemin fournies par VS Code :
    - Tapez `./` ou `../`.
    - VS Code vous invitera à choisir parmi les options disponibles en fonction de ce que vous avez tapé.
    - Suivez le chemin en cliquant sur le fichier ou dossier souhaité pour vous assurer que votre chemin est correct.

Une fois que vous avez ajouté le chemin relatif correct, enregistrez et poussez vos modifications.

### Vérifier que les URLs n'ont pas de locale

Ce workflow garantit que toute URL web n'inclut pas de locale spécifique à un pays. Comme ce dépôt est accessible globalement, il est important de s'assurer que les URLs ne contiennent pas la locale de votre pays.

1. Pour vérifier que vos URLs n'ont pas de locales de pays, effectuez les tâches suivantes :

    - Recherchez des textes comme `/en-us/`, `/en/`, ou toute autre locale de langue dans les URLs.
    - Si celles-ci ne sont pas présentes dans vos URLs, alors vous passerez cette vérification.

1. Pour résoudre ce problème, effectuez les tâches suivantes :
    - Ouvrez le chemin du fichier mis en évidence par le workflow.
    - Supprimez la locale de pays des URLs.

Une fois que vous avez supprimé la locale de pays, enregistrez et poussez vos modifications.

### Vérifier les URLs cassées

Ce workflow garantit que toute URL web dans vos fichiers fonctionne et renvoie un code de statut 200.

1. Pour vérifier que vos URLs fonctionnent correctement, effectuez les tâches suivantes :
    - Vérifiez le statut des URLs dans vos fichiers.

2. Pour corriger les URLs cassées, effectuez les tâches suivantes :
    - Ouvrez le fichier contenant l'URL cassée.
    - Mettez à jour l'URL avec la bonne.

Une fois que vous avez corrigé les URLs, enregistrez et poussez vos modifications.

> [!NOTE]
>
> Il peut y avoir des cas où la vérification des URLs échoue même si le lien est accessible. Cela peut arriver pour plusieurs raisons, notamment :
>
> - **Restrictions réseau** : Les serveurs d'actions GitHub peuvent avoir des restrictions réseau empêchant l'accès à certaines URLs.
> - **Problèmes de délai d'attente** : Les URLs qui prennent trop de temps à répondre peuvent déclencher une erreur de délai d'attente dans le workflow.
> - **Problèmes temporaires de serveur** : Les temps d'arrêt ou de maintenance occasionnels du serveur peuvent rendre une URL temporairement indisponible pendant la validation.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.