# Affiner et Intégrer des modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Studio

Cet exemple de bout en bout (E2E) est basé sur le guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" de la communauté technique de Microsoft. Il introduit les processus d'affinement, de déploiement et d'intégration de modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Studio.
Contrairement à l'exemple E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", qui impliquait d'exécuter du code localement, ce tutoriel se concentre entièrement sur l'affinement et l'intégration de votre modèle au sein d'Azure AI / ML Studio.

## Aperçu

Dans cet exemple E2E, vous apprendrez à affiner le modèle Phi-3 et à l'intégrer avec Prompt flow dans Azure AI Studio. En tirant parti d'Azure AI / ML Studio, vous établirez un flux de travail pour déployer et utiliser des modèles d'IA personnalisés. Cet exemple E2E est divisé en trois scénarios :

**Scénario 1 : Configurer les ressources Azure et préparer l'affinement**

**Scénario 2 : Affiner le modèle Phi-3 et le déployer dans Azure Machine Learning Studio**

**Scénario 3 : Intégrer avec Prompt flow et discuter avec votre modèle personnalisé dans Azure AI Studio**

Voici un aperçu de cet exemple E2E.

![Aperçu de l'intégration Phi-3-FineTuning_PromptFlow.](../../../../translated_images/00-01-architecture.fa40b38b29f795863378026c4dcc3007b0938b0b43afaf8c331906d03742b2e6.fr.png)

### Table des Matières

1. **[Scénario 1 : Configurer les ressources Azure et préparer l'affinement](../../../../md/06.E2ESamples)**
    - [Créer un espace de travail Azure Machine Learning](../../../../md/06.E2ESamples)
    - [Demander des quotas GPU dans l'abonnement Azure](../../../../md/06.E2ESamples)
    - [Ajouter une attribution de rôle](../../../../md/06.E2ESamples)
    - [Configurer le projet](../../../../md/06.E2ESamples)
    - [Préparer le jeu de données pour l'affinement](../../../../md/06.E2ESamples)

1. **[Scénario 2 : Affiner le modèle Phi-3 et le déployer dans Azure Machine Learning Studio](../../../../md/06.E2ESamples)**
    - [Affiner le modèle Phi-3](../../../../md/06.E2ESamples)
    - [Déployer le modèle Phi-3 affiné](../../../../md/06.E2ESamples)

1. **[Scénario 3 : Intégrer avec Prompt flow et discuter avec votre modèle personnalisé dans Azure AI Studio](../../../../md/06.E2ESamples)**
    - [Intégrer le modèle Phi-3 personnalisé avec Prompt flow](../../../../md/06.E2ESamples)
    - [Discuter avec votre modèle Phi-3 personnalisé](../../../../md/06.E2ESamples)

## Scénario 1 : Configurer les ressources Azure et préparer l'affinement

### Créer un espace de travail Azure Machine Learning

1. Tapez *azure machine learning* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Azure Machine Learning** parmi les options qui apparaissent.

    ![Tapez azure machine learning.](../../../../translated_images/01-01-type-azml.98b3003c07da4dbb6885400f66988b3ae05767edb5e8b8ef480e584abe379ca7.fr.png)

2. Sélectionnez **+ Créer** dans le menu de navigation.

3. Sélectionnez **Nouvel espace de travail** dans le menu de navigation.

    ![Sélectionnez nouvel espace de travail.](../../../../translated_images/01-02-select-new-workspace.7648b384cbd786565740c0e5ea203d4710889d5ef23a2abf08428444f6d1a2a6.fr.png)

4. Effectuez les tâches suivantes :

    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Entrez le **Nom de l'espace de travail**. Il doit être une valeur unique.
    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Sélectionnez le **Compte de stockage** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez le **Key vault** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez les **Insights de l'application** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez le **Registre de conteneurs** à utiliser (créez-en un nouveau si nécessaire).

    ![Remplir azure machine learning.](../../../../translated_images/01-03-fill-AZML.a3f644231a76859c7d92134b7dea1dd0d4df1c11cc615351c95be5a2c7056b03.fr.png)

5. Sélectionnez **Vérifier + Créer**.

6. Sélectionnez **Créer**.

### Demander des quotas GPU dans l'abonnement Azure

Dans ce tutoriel, vous apprendrez à affiner et déployer un modèle Phi-3 en utilisant des GPU. Pour l'affinement, vous utiliserez le GPU *Standard_NC24ads_A100_v4*, qui nécessite une demande de quota. Pour le déploiement, vous utiliserez le GPU *Standard_NC6s_v3*, qui nécessite également une demande de quota.

> [!NOTE]
>
> Seuls les abonnements Pay-As-You-Go (le type d'abonnement standard) sont éligibles à l'allocation GPU ; les abonnements avec avantages ne sont pas actuellement pris en charge.
>

1. Visitez [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Effectuez les tâches suivantes pour demander un quota *Standard NCADSA100v4 Family* :

    - Sélectionnez **Quota** dans l'onglet de gauche.
    - Sélectionnez la **Famille de machines virtuelles** à utiliser. Par exemple, sélectionnez **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC24ads_A100_v4*.
    - Sélectionnez **Demander un quota** dans le menu de navigation.

        ![Demander un quota.](../../../../translated_images/02-02-request-quota.55f797113d95ad20ca91943eed637488d0aa51d61f3bbe7f080ec466b2ae0666.fr.png)

    - À l'intérieur de la page de demande de quota, entrez la **Nouvelle limite de cœurs** que vous souhaitez utiliser. Par exemple, 24.
    - À l'intérieur de la page de demande de quota, sélectionnez **Soumettre** pour demander le quota GPU.

1. Effectuez les tâches suivantes pour demander un quota *Standard NCSv3 Family* :

    - Sélectionnez **Quota** dans l'onglet de gauche.
    - Sélectionnez la **Famille de machines virtuelles** à utiliser. Par exemple, sélectionnez **Standard NCSv3 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC6s_v3*.
    - Sélectionnez **Demander un quota** dans le menu de navigation.
    - À l'intérieur de la page de demande de quota, entrez la **Nouvelle limite de cœurs** que vous souhaitez utiliser. Par exemple, 24.
    - À l'intérieur de la page de demande de quota, sélectionnez **Soumettre** pour demander le quota GPU.

### Ajouter une attribution de rôle

Pour affiner et déployer vos modèles, vous devez d'abord créer une identité managée assignée par l'utilisateur (UAI) et lui attribuer les autorisations appropriées. Cette UAI sera utilisée pour l'authentification pendant le déploiement.

#### Créer une identité managée assignée par l'utilisateur (UAI)

1. Tapez *managed identities* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Managed Identities** parmi les options qui apparaissent.

    ![Tapez managed identities.](../../../../translated_images/03-01-type-managed-identities.2f7b07daa34dc15303b6a3f8c364bc0b7e892dd18aaff361440a030621b540b8.fr.png)

1. Sélectionnez **+ Créer**.

    ![Sélectionnez créer.](../../../../translated_images/03-02-select-create.0bde775b318f4adba24a7637b31f00f9b685214ed225c5123845a215a260ac71.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Entrez le **Nom**. Il doit être une valeur unique.

    ![Sélectionnez créer.](../../../../translated_images/03-03-fill-managed-identities-1.688009e629c1e6952853b94022d3fe97c659c34e29908db17218a5cab6d6add1.fr.png)

1. Sélectionnez **Vérifier + créer**.

1. Sélectionnez **+ Créer**.

#### Ajouter une attribution de rôle de contributeur à l'identité managée

1. Accédez à la ressource d'identité managée que vous avez créée.

1. Sélectionnez **Attributions de rôles Azure** dans l'onglet de gauche.

1. Sélectionnez **+Ajouter une attribution de rôle** dans le menu de navigation.

1. À l'intérieur de la page d'ajout d'attribution de rôle, effectuez les tâches suivantes :
    - Sélectionnez la **Portée** sur **Groupe de ressources**.
    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser.
    - Sélectionnez le **Rôle** sur **Contributeur**.

    ![Remplir le rôle de contributeur.](../../../../translated_images/03-04-fill-contributor-role.8bc54b3ac8f64842c82b3379f3c3e9f8d778abf28c00e5b7b471935a86d3ae64.fr.png)

1. Sélectionnez **Enregistrer**.

#### Ajouter une attribution de rôle de lecteur de données Blob de stockage à l'identité managée

1. Tapez *storage accounts* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Storage accounts** parmi les options qui apparaissent.

    ![Tapez storage accounts.](../../../../translated_images/03-05-type-storage-accounts.236987db35ba863124c6de8dd16533fe35b96ee4e2dcb9d67e6b279a285f0e6d.fr.png)

1. Sélectionnez le compte de stockage associé à l'espace de travail Azure Machine Learning que vous avez créé. Par exemple, *finetunephistorage*.

1. Effectuez les tâches suivantes pour accéder à la page d'ajout d'attribution de rôle :

    - Accédez au compte de stockage Azure que vous avez créé.
    - Sélectionnez **Contrôle d'accès (IAM)** dans l'onglet de gauche.
    - Sélectionnez **+ Ajouter** dans le menu de navigation.
    - Sélectionnez **Ajouter une attribution de rôle** dans le menu de navigation.

    ![Ajouter un rôle.](../../../../translated_images/03-06-add-role.dde49177fe7ce1cd1604f620ca5c8ac6442fc516effb057e9f74645f35f9d038.fr.png)

1. À l'intérieur de la page d'ajout d'attribution de rôle, effectuez les tâches suivantes :

    - À l'intérieur de la page de rôle, tapez *Storage Blob Data Reader* dans la **barre de recherche** et sélectionnez **Storage Blob Data Reader** parmi les options qui apparaissent.
    - À l'intérieur de la page de rôle, sélectionnez **Suivant**.
    - À l'intérieur de la page Membres, sélectionnez **Attribuer l'accès à** **Managed identity**.
    - À l'intérieur de la page Membres, sélectionnez **+ Sélectionner des membres**.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez votre **Abonnement** Azure.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez l'**Identité managée** pour **Manage Identity**.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez l'identité managée que vous avez créée. Par exemple, *finetunephi-managedidentity*.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez **Sélectionner**.

    ![Sélectionnez l'identité managée.](../../../../translated_images/03-08-select-managed-identity.f9a44699bf247a4583e2d377e304de8c3d8a602b7d3fed52b9ae790e64e94fe9.fr.png)

1. Sélectionnez **Vérifier + attribuer**.

#### Ajouter une attribution de rôle AcrPull à l'identité managée

1. Tapez *container registries* dans la **barre de recherche** en haut de la page du portail et sélectionnez **Container registries** parmi les options qui apparaissent.

    ![Tapez container registries.](../../../../translated_images/03-09-type-container-registries.b5519f1fbf49bff0c0d4c95deecd2ef0c61b4870119886c3661014435e2b7095.fr.png)

1. Sélectionnez le registre de conteneurs associé à l'espace de travail Azure Machine Learning. Par exemple, *finetunephicontainerregistry*

1. Effectuez les tâches suivantes pour accéder à la page d'ajout d'attribution de rôle :

    - Sélectionnez **Contrôle d'accès (IAM)** dans l'onglet de gauche.
    - Sélectionnez **+ Ajouter** dans le menu de navigation.
    - Sélectionnez **Ajouter une attribution de rôle** dans le menu de navigation.

1. À l'intérieur de la page d'ajout d'attribution de rôle, effectuez les tâches suivantes :

    - À l'intérieur de la page de rôle, tapez *AcrPull* dans la **barre de recherche** et sélectionnez **AcrPull** parmi les options qui apparaissent.
    - À l'intérieur de la page de rôle, sélectionnez **Suivant**.
    - À l'intérieur de la page Membres, sélectionnez **Attribuer l'accès à** **Managed identity**.
    - À l'intérieur de la page Membres, sélectionnez **+ Sélectionner des membres**.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez votre **Abonnement** Azure.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez l'**Identité managée** pour **Manage Identity**.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez l'identité managée que vous avez créée. Par exemple, *finetunephi-managedidentity*.
    - À l'intérieur de la page Sélectionner les identités managées, sélectionnez **Sélectionner**.
    - Sélectionnez **Vérifier + attribuer**.

### Configurer le projet

Pour télécharger les jeux de données nécessaires à l'affinement, vous allez configurer un environnement local.

Dans cet exercice, vous allez

- Créer un dossier pour travailler à l'intérieur.
- Créer un environnement virtuel.
- Installer les packages requis.
- Créer un fichier *download_dataset.py* pour télécharger le jeu de données.

#### Créer un dossier pour travailler à l'intérieur

1. Ouvrez une fenêtre de terminal et tapez la commande suivante pour créer un dossier nommé *finetune-phi* dans le chemin par défaut.

    ```console
    mkdir finetune-phi
    ```

2. Tapez la commande suivante dans votre terminal pour naviguer jusqu'au dossier *finetune-phi* que vous avez créé.

    ```console
    cd finetune-phi
    ```

#### Créer un environnement virtuel

1. Tapez la commande suivante dans votre terminal pour créer un environnement virtuel nommé *.venv*.

    ```console
    python -m venv .venv
    ```

2. Tapez la commande suivante dans votre terminal pour activer l'environnement virtuel.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Si cela a fonctionné, vous devriez voir *(.venv)* avant l'invite de commande.

#### Installer les packages requis

1. Tapez les commandes suivantes dans votre terminal pour installer les packages requis.

    ```console
    pip install datasets==2.19.1
    ```

#### Créer `download_dataset.py`

> [!NOTE]
> Structure complète du dossier :
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Ouvrez **Visual Studio Code**.

1. Sélectionnez **Fichier** dans la barre de menu.

1. Sélectionnez **Ouvrir le dossier**.

1. Sélectionnez le dossier *finetune-phi* que vous avez créé, situé à *C:\Users\yourUserName\finetune-phi*.

    ![Sélectionnez le dossier que vous avez créé.](../../../../translated_images/04-01-open-project-folder.f5e2b4ce1cb596eae857303b12909dc0174fd99129d6944c41079f24ee17eed2.fr.png)

1. Dans le volet gauche de Visual Studio Code, cliquez avec le bouton droit de la souris et sélectionnez **Nouveau fichier** pour créer un nouveau fichier nommé *download_dataset.py*.

    ![Créez un nouveau fichier.](../../../../translated_images/04-02-create-new-file.7c51fabe5e84788e34e43f951164471eb07df8363993ce69badc8908f1033613.fr.png)

### Préparer le jeu de données pour l'affinement

Dans cet exercice, vous allez exécuter le fichier *download_dataset.py* pour télécharger les jeux de données *ultrachat_200k* dans votre environnement local. Vous utiliserez ensuite ces jeux de données pour affiner le modèle Phi-3 dans Azure Machine Learning.

Dans cet exercice, vous allez :

- Ajouter du code au fichier *download_dataset.py* pour télécharger les jeux de données.
- Exécuter le fichier *download_dataset.py* pour télécharger les jeux de données dans votre environnement local.

#### Télécharger votre jeu de données en utilisant *download_dataset.py*

1. Ouvrez le fichier *download_dataset.py* dans Visual Studio Code.

1. Ajoutez le code suivant dans le fichier *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Charger et diviser un jeu de données.
        """
        # Charger le jeu de données avec le nom, la configuration et le ratio de division spécifiés
        dataset = load_dataset(dataset_name, config_name, split
1. Visitez [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez **Compute** dans l'onglet de gauche.

1. Sélectionnez **Compute clusters** dans le menu de navigation.

1. Sélectionnez **+ New**.

    ![Sélectionnez compute.](../../../../translated_images/06-01-select-compute.69422609cf19921fb16f550b2566e00870f63ba0caf66b0d26b34e6b0ed21a68.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Choisissez le **Niveau de machine virtuelle** sur **Dedicated**.
    - Sélectionnez le **Type de machine virtuelle** sur **GPU**.
    - Appliquez le filtre **Taille de machine virtuelle** sur **Select from all options**.
    - Choisissez la **Taille de machine virtuelle** sur **Standard_NC24ads_A100_v4**.

    ![Créer un cluster.](../../../../translated_images/06-02-create-cluster.ad68bcb0914b62972408da8f925632977c54248ff99d2c45761f7e3d33f40fe1.fr.png)

1. Sélectionnez **Next**.

1. Effectuez les tâches suivantes :

    - Entrez le **Nom du compute**. Il doit être unique.
    - Réglez le **Nombre minimum de nœuds** sur **0**.
    - Réglez le **Nombre maximum de nœuds** sur **1**.
    - Réglez les **Secondes d'inactivité avant réduction d'échelle** sur **120**.

    ![Créer un cluster.](../../../../translated_images/06-03-create-cluster.f36399780462ff69f62b9bdf22180d6824b00cdc913fe2a639dde3e4b9eaa43e.fr.png)

1. Sélectionnez **Create**.

#### Affiner le modèle Phi-3

1. Visitez [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez l'espace de travail Azure Machine Learning que vous avez créé.

    ![Sélectionnez l'espace de travail que vous avez créé.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez **Model catalog** dans l'onglet de gauche.
    - Tapez *phi-3-mini-4k* dans la **barre de recherche** et sélectionnez **Phi-3-mini-4k-instruct** parmi les options qui apparaissent.

    ![Tapez phi-3-mini-4k.](../../../../translated_images/06-05-type-phi-3-mini-4k.7461addd95ede137f6f018a29681762f85e063477ded6043aafbdf6d742a54e8.fr.png)

1. Sélectionnez **Fine-tune** dans le menu de navigation.

    ![Sélectionnez fine tune.](../../../../translated_images/06-06-select-fine-tune.2c678a7f33294c16ae3ad30ce5d4a78600013dc3a0227e8d341a1962f3aff84d.fr.png)

1. Effectuez les tâches suivantes :

    - Réglez **Select task type** sur **Chat completion**.
    - Sélectionnez **+ Select data** pour télécharger les **Données d'entraînement**.
    - Choisissez le type de téléchargement des données de validation sur **Provide different validation data**.
    - Sélectionnez **+ Select data** pour télécharger les **Données de validation**.

    ![Remplissez la page de fine-tuning.](../../../../translated_images/06-07-fill-finetuning.c76431cc247b6398fb9d33da62841adf87d5eebaa92cd79e80bd7bcbed49f1d3.fr.png)

    > [!TIP]
    >
    > Vous pouvez sélectionner **Advanced settings** pour personnaliser des configurations comme **learning_rate** et **lr_scheduler_type** pour optimiser le processus de fine-tuning selon vos besoins spécifiques.

1. Sélectionnez **Finish**.

1. Dans cet exercice, vous avez réussi à affiner le modèle Phi-3 en utilisant Azure Machine Learning. Notez que le processus de fine-tuning peut prendre un certain temps. Après avoir lancé le job de fine-tuning, vous devez attendre qu'il se termine. Vous pouvez surveiller le statut du job de fine-tuning en naviguant vers l'onglet Jobs sur le côté gauche de votre espace de travail Azure Machine Learning. Dans la prochaine série, vous déploierez le modèle affiné et l'intégrerez avec Prompt flow.

    ![Voir le job de fine-tuning.](../../../../translated_images/06-08-output.9f9cf6f9e9e83533b793a5ff3066b09475e299999fead6f98dfb102f48db0061.fr.png)

### Déployer le modèle Phi-3 affiné

Pour intégrer le modèle Phi-3 affiné avec Prompt flow, vous devez déployer le modèle pour le rendre accessible pour des inférences en temps réel. Ce processus implique l'enregistrement du modèle, la création d'un endpoint en ligne et le déploiement du modèle.

Dans cet exercice, vous allez :

- Enregistrer le modèle affiné dans l'espace de travail Azure Machine Learning.
- Créer un endpoint en ligne.
- Déployer le modèle Phi-3 affiné enregistré.

#### Enregistrer le modèle affiné

1. Visitez [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Sélectionnez l'espace de travail Azure Machine Learning que vous avez créé.

    ![Sélectionnez l'espace de travail que vous avez créé.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.fr.png)

1. Sélectionnez **Models** dans l'onglet de gauche.
1. Sélectionnez **+ Register**.
1. Sélectionnez **From a job output**.

    ![Enregistrer le modèle.](../../../../translated_images/07-01-register-model.9b64d29736e0be32343b36a503d7e38c47c22d9edfa554aae179352982fdf96b.fr.png)

1. Sélectionnez le job que vous avez créé.

    ![Sélectionnez le job.](../../../../translated_images/07-02-select-job.712abf18cdae5256776907df3ed30df53d297ff8d475fb64d5c03e92304db6ef.fr.png)

1. Sélectionnez **Next**.

1. Réglez **Model type** sur **MLflow**.

1. Assurez-vous que **Job output** est sélectionné ; cela devrait être sélectionné automatiquement.

    ![Sélectionnez output.](../../../../translated_images/07-03-select-output.45098161b7ddfda4b8d4d62676da0488a32a16e838ff03f37bfd71b9886da798.fr.png)

1. Sélectionnez **Next**.

1. Sélectionnez **Register**.

    ![Sélectionnez register.](../../../../translated_images/07-04-register.3403ed7976f07fbfc27210550cf2f793d9cf778032ea276ecb287bd9df88f188.fr.png)

1. Vous pouvez visualiser votre modèle enregistré en naviguant dans le menu **Models** depuis l'onglet de gauche.

    ![Modèle enregistré.](../../../../translated_images/07-05-registered-model.90693749513e55231e8904304e4ea1f9e29ab659bc1926ea69dffd25e77ffb2d.fr.png)

#### Déployer le modèle affiné

1. Allez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l'onglet de gauche.

1. Sélectionnez **Real-time endpoints** dans le menu de navigation.

    ![Créer un endpoint.](../../../../translated_images/07-06-create-endpoint.28687e4d01bffed741bf461bbb36ceef441ed5d049ca5d091aab511ced67a804.fr.png)

1. Sélectionnez **Create**.

1. Sélectionnez le modèle enregistré que vous avez créé.

    ![Sélectionnez le modèle enregistré.](../../../../translated_images/07-07-select-registered-model.5190ae13400cc09a6410f891a62e6b2ccc2c2bd7f419b0df4ea964731e72407f.fr.png)

1. Sélectionnez **Select**.

1. Effectuez les tâches suivantes :

    - Réglez la **Machine virtuelle** sur *Standard_NC6s_v3*.
    - Choisissez le **Nombre d'instances** que vous souhaitez utiliser. Par exemple, *1*.
    - Réglez l'**Endpoint** sur **New** pour créer un endpoint.
    - Entrez le **Nom de l'endpoint**. Il doit être unique.
    - Entrez le **Nom du déploiement**. Il doit être unique.

    ![Remplissez les paramètres de déploiement.](../../../../translated_images/07-08-deployment-setting.5449edf53b27f5457cc68d2285d355a7d364b01423a51e5af63e7c52374a3a79.fr.png)

1. Sélectionnez **Deploy**.

> [!WARNING]
> Pour éviter des frais supplémentaires sur votre compte, assurez-vous de supprimer l'endpoint créé dans l'espace de travail Azure Machine Learning.
>

#### Vérifiez le statut du déploiement dans l'espace de travail Azure Machine Learning

1. Allez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l'onglet de gauche.

1. Sélectionnez l'endpoint que vous avez créé.

    ![Sélectionnez endpoints](../../../../translated_images/07-09-check-deployment.8e4465a7585b3c22db5fc9d5757269a919b5104fdeb5f736fa573ca9b3e16abe.fr.png)

1. Sur cette page, vous pouvez gérer les endpoints pendant le processus de déploiement.

> [!NOTE]
> Une fois le déploiement terminé, assurez-vous que **Live traffic** est réglé sur **100%**. Si ce n'est pas le cas, sélectionnez **Update traffic** pour ajuster les paramètres de trafic. Notez que vous ne pouvez pas tester le modèle si le trafic est réglé sur 0%.
>
> ![Régler le trafic.](../../../../translated_images/07-10-set-traffic.1d1b24b39c7ec80451c99fe05298fac636f0cd449e7be282736f6c06a1a70875.fr.png)
>

## Scénario 3 : Intégrer avec Prompt flow et discuter avec votre modèle personnalisé dans Azure AI Studio

### Intégrer le modèle Phi-3 personnalisé avec Prompt flow

Après avoir déployé votre modèle affiné, vous pouvez maintenant l'intégrer avec Prompt Flow pour utiliser votre modèle dans des applications en temps réel, permettant une variété de tâches interactives avec votre modèle Phi-3 personnalisé.

Dans cet exercice, vous allez :

- Créer un Hub Azure AI Studio.
- Créer un Projet Azure AI Studio.
- Créer un Prompt flow.
- Ajouter une connexion personnalisée pour le modèle Phi-3 affiné.
- Configurer Prompt flow pour discuter avec votre modèle Phi-3 personnalisé

> [!NOTE]
> Vous pouvez également intégrer avec Promptflow en utilisant Azure ML Studio. Le même processus d'intégration peut être appliqué à Azure ML Studio.

#### Créer un Hub Azure AI Studio

Vous devez créer un Hub avant de créer le Projet. Un Hub agit comme un groupe de ressources, vous permettant d'organiser et de gérer plusieurs Projets au sein d'Azure AI Studio.

1. Visitez [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Sélectionnez **All hubs** dans l'onglet de gauche.

1. Sélectionnez **+ New hub** dans le menu de navigation.

    ![Créer un hub.](../../../../translated_images/08-01-create-hub.1df80696bf3376f0e56ffa90de1fc35962acf2fc3c1a3a6b254015b8b993e55e.fr.png)

1. Effectuez les tâches suivantes :

    - Entrez le **Nom du hub**. Il doit être unique.
    - Sélectionnez votre **Subscription** Azure.
    - Choisissez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Localisation** que vous souhaitez utiliser.
    - Choisissez **Connect Azure AI Services** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Connect Azure AI Search** sur **Skip connecting**.

    ![Remplissez le hub.](../../../../translated_images/08-02-fill-hub.fc194526614a5811e7b57e699911be39babdc95aa425b6c4a72f064948865ce3.fr.png)

1. Sélectionnez **Next**.

#### Créer un Projet Azure AI Studio

1. Dans le Hub que vous avez créé, sélectionnez **All projects** dans l'onglet de gauche.

1. Sélectionnez **+ New project** dans le menu de navigation.

    ![Sélectionnez nouveau projet.](../../../../translated_images/08-04-select-new-project.dc11f26658c3c3f9d0fcf3232a954abfc115de5eb74da21d5be229c9c1be2875.fr.png)

1. Entrez le **Nom du projet**. Il doit être unique.

    ![Créer un projet.](../../../../translated_images/08-05-create-project.61caaa28c1b9b696bf29de6b002bbb2040dbaeb764adab161dcb3472fe789aea.fr.png)

1. Sélectionnez **Create a project**.

#### Ajouter une connexion personnalisée pour le modèle Phi-3 affiné

Pour intégrer votre modèle Phi-3 personnalisé avec Prompt flow, vous devez enregistrer l'endpoint et la clé du modèle dans une connexion personnalisée. Cette configuration assure l'accès à votre modèle Phi-3 personnalisé dans Prompt flow.

#### Définir la clé API et l'URI de l'endpoint du modèle Phi-3 affiné

1. Visitez [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Naviguez vers l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l'onglet de gauche.

    ![Sélectionnez endpoints.](../../../../translated_images/08-06-select-endpoints.75d3bdd7f0b17da0367370d1293f7e7f7b2a65fb7e17390997be0460e8f0b82b.fr.png)

1. Sélectionnez l'endpoint que vous avez créé.

    ![Sélectionnez endpoints.](../../../../translated_images/08-07-select-endpoint-created.851b32efc6058e5863aa62ae8d576a6c20792e24f1862dc6857b9f24a2949f96.fr.png)

1. Sélectionnez **Consume** dans le menu de navigation.

1. Copiez votre **REST endpoint** et **Primary key**.
![Copier la clé API et l'URI de l'endpoint.](../../../../translated_images/08-08-copy-endpoint-key.947512a4c95b5dd9fc5a606bad4244bf9b136929c1fab06570c463311ef29df1.fr.png)

#### Ajouter la Connexion Personnalisée

1. Visitez [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Accédez au projet Azure AI Studio que vous avez créé.

1. Dans le projet que vous avez créé, sélectionnez **Paramètres** dans l'onglet de gauche.

1. Sélectionnez **+ Nouvelle connexion**.

    ![Sélectionner nouvelle connexion.](../../../../translated_images/08-09-select-new-connection.b5e93c85028739875916f34a1821b0b086f0e993b8d7d7388c100e3a38b70bbd.fr.png)

1. Sélectionnez **Clés personnalisées** dans le menu de navigation.

    ![Sélectionner clés personnalisées.](../../../../translated_images/08-10-select-custom-keys.077f17a1a49b8f76e446453b6a68c09c2aa08291818d98edcf39e3013c5b45ac.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez **+ Ajouter des paires clé-valeur**.
    - Pour le nom de la clé, entrez **endpoint** et collez l'endpoint que vous avez copié depuis Azure ML Studio dans le champ valeur.
    - Sélectionnez **+ Ajouter des paires clé-valeur** à nouveau.
    - Pour le nom de la clé, entrez **key** et collez la clé que vous avez copiée depuis Azure ML Studio dans le champ valeur.
    - Après avoir ajouté les clés, sélectionnez **est secret** pour éviter que la clé ne soit exposée.

    ![Ajouter connexion.](../../../../translated_images/08-11-add-connection.01279deb77ede4d195b17ecabae70979976834892e9dbb3354f504bb6edaa6e1.fr.png)

1. Sélectionnez **Ajouter connexion**.

#### Créer un Flux de Prompts

Vous avez ajouté une connexion personnalisée dans Azure AI Studio. Maintenant, créons un flux de prompts en suivant les étapes ci-dessous. Ensuite, vous connecterez ce flux de prompts à la connexion personnalisée afin de pouvoir utiliser le modèle ajusté dans le flux de prompts.

1. Accédez au projet Azure AI Studio que vous avez créé.

1. Sélectionnez **Flux de prompts** dans l'onglet de gauche.

1. Sélectionnez **+ Créer** dans le menu de navigation.

    ![Sélectionner Flux de prompts.](../../../../translated_images/08-12-select-promptflow.5e0527f1e5102c604e0e8a34f2321e28f8c815ec2908ae7038f012a088ff2bbc.fr.png)

1. Sélectionnez **Flux de chat** dans le menu de navigation.

    ![Sélectionner flux de chat.](../../../../translated_images/08-13-select-flow-type.e3fb41375041faa4d058304c319329d5f45f87139143b384f056bb500076ca73.fr.png)

1. Entrez le **Nom du dossier** à utiliser.

    ![Entrer nom.](../../../../translated_images/08-14-enter-name.90db481f18468cfd78b281825cb5484ab7236cfa29d59d287b7b0f423516e6ea.fr.png)

1. Sélectionnez **Créer**.

#### Configurer le Flux de Prompts pour discuter avec votre modèle Phi-3 personnalisé

Vous devez intégrer le modèle Phi-3 ajusté dans un flux de prompts. Cependant, le flux de prompts existant fourni n'est pas conçu pour cet objectif. Vous devez donc repenser le flux de prompts pour permettre l'intégration du modèle personnalisé.

1. Dans le flux de prompts, effectuez les tâches suivantes pour reconstruire le flux existant :

    - Sélectionnez **Mode fichier brut**.
    - Supprimez tout le code existant dans le fichier *flow.dag.yml*.
    - Ajoutez le code suivant au fichier *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Qui a fondé Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Sélectionnez **Enregistrer**.

    ![Sélectionner mode fichier brut.](../../../../translated_images/08-15-select-raw-file-mode.28d80142df9d540c66c37d17825cec921bb1f7b54e386223bb4ad38df10e5e2d.fr.png)

1. Ajoutez le code suivant au fichier *integrate_with_promptflow.py* pour utiliser le modèle Phi-3 personnalisé dans le flux de prompts.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configuration du journal
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Envoyer une requête à l'endpoint du modèle Phi-3 avec les données d'entrée fournies en utilisant la Connexion Personnalisée.
        """

        # "connection" est le nom de la Connexion Personnalisée, "endpoint", "key" sont les clés dans la Connexion Personnalisée
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Enregistrer la réponse JSON complète
            logger.debug(f"Réponse JSON complète : {response.json()}")

            result = response.json()["output"]
            logger.info("Réponse reçue avec succès de l'endpoint Azure ML.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Erreur lors de la requête à l'endpoint Azure ML : {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Fonction outil pour traiter les données d'entrée et interroger le modèle Phi-3.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Coller le code du flux de prompts.](../../../../translated_images/08-16-paste-promptflow-code.c27a93ed6134adbe7ce618ffad7300923f3c02defedef0b5598eab5a6ee2afc2.fr.png)

> [!NOTE]
> Pour plus d'informations détaillées sur l'utilisation de Flux de prompts dans Azure AI Studio, vous pouvez vous référer à [Flux de prompts dans Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Sélectionnez **Entrée de chat**, **Sortie de chat** pour activer la discussion avec votre modèle.

    ![Entrée Sortie.](../../../../translated_images/08-17-select-input-output.d188ea79fc21d29e615b6cc50d638214a2dcbc3b3ccb16009aa67698227d2765.fr.png)

1. Vous êtes maintenant prêt à discuter avec votre modèle Phi-3 personnalisé. Dans le prochain exercice, vous apprendrez à démarrer le Flux de prompts et à l'utiliser pour discuter avec votre modèle Phi-3 ajusté.

> [!NOTE]
>
> Le flux reconstruit devrait ressembler à l'image ci-dessous :
>
> ![Exemple de flux.](../../../../translated_images/08-18-graph-example.48c427864370ac7dd02e500bc3a0ff49785d4480e489b4dfe25e529da99f193f.fr.png)
>

### Discuter avec votre modèle Phi-3 personnalisé

Maintenant que vous avez ajusté et intégré votre modèle Phi-3 personnalisé avec le Flux de prompts, vous êtes prêt à commencer à interagir avec lui. Cet exercice vous guidera à travers le processus de configuration et d'initiation d'une discussion avec votre modèle en utilisant le Flux de prompts. En suivant ces étapes, vous serez en mesure de tirer pleinement parti des capacités de votre modèle Phi-3 ajusté pour diverses tâches et conversations.

- Discutez avec votre modèle Phi-3 personnalisé en utilisant le Flux de prompts.

#### Démarrer le Flux de prompts

1. Sélectionnez **Démarrer les sessions de calcul** pour démarrer le Flux de prompts.

    ![Démarrer la session de calcul.](../../../../translated_images/09-01-start-compute-session.9d080c30a6fc78a8b23ac54e7c8b11aeecc005d3da03cb0f9bd8afc298151ffa.fr.png)

1. Sélectionnez **Valider et analyser l'entrée** pour renouveler les paramètres.

    ![Valider l'entrée.](../../../../translated_images/09-02-validate-input.db05a40e29a21b333848b7c03542b0ec521ce9c6fbe12fba51c2addcb1c07c68.fr.png)

1. Sélectionnez la **Valeur** de la **connexion** à la connexion personnalisée que vous avez créée. Par exemple, *connection*.

    ![Connexion.](../../../../translated_images/09-03-select-connection.de0137da33c86e581425cef4a25957d86140d1605968f6f7c98207b8e715cca8.fr.png)

#### Discuter avec votre modèle personnalisé

1. Sélectionnez **Chat**.

    ![Sélectionner chat.](../../../../translated_images/09-04-select-chat.87b90a2f41e38714f40dedde608d349bfaca00a75f08166816dddb92de711e32.fr.png)

1. Voici un exemple des résultats : Maintenant, vous pouvez discuter avec votre modèle Phi-3 personnalisé. Il est recommandé de poser des questions basées sur les données utilisées pour l'ajustement.

    ![Discuter avec flux de prompts.](../../../../translated_images/09-05-chat-with-promptflow.46c9fdf0e6de0e15e9618f654830e52bd8ead4aec0de57bb960206321d2bd0bd.fr.png)

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.