# Évaluer le modèle Phi-3 / Phi-3.5 ajusté dans Azure AI Foundry en se concentrant sur les principes d'IA responsable de Microsoft

Cet exemple de bout en bout (E2E) est basé sur le guide "[Évaluer les modèles Phi-3 / 3.5 ajustés dans Azure AI Foundry en se concentrant sur l'IA responsable de Microsoft](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" de la communauté technique de Microsoft.

## Vue d'ensemble

### Comment évaluer la sécurité et les performances d'un modèle Phi-3 / Phi-3.5 ajusté dans Azure AI Foundry ?

L'ajustement d'un modèle peut parfois entraîner des réponses involontaires ou indésirables. Pour garantir que le modèle reste sûr et efficace, il est essentiel d'évaluer son potentiel à générer un contenu nuisible ainsi que sa capacité à produire des réponses précises, pertinentes et cohérentes. Dans ce tutoriel, vous apprendrez à évaluer la sécurité et les performances d'un modèle Phi-3 / Phi-3.5 ajusté et intégré à Prompt flow dans Azure AI Foundry.

Voici le processus d'évaluation d'Azure AI Foundry.

![Architecture du tutoriel.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.fr.png)

*Source de l'image : [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pour plus d'informations détaillées et pour explorer des ressources supplémentaires sur Phi-3 / Phi-3.5, veuillez visiter le [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prérequis

- [Python](https://www.python.org/downloads)
- [Abonnement Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modèle Phi-3 / Phi-3.5 ajusté

### Table des matières

1. [**Scénario 1 : Introduction à l'évaluation de Prompt flow dans Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduction à l'évaluation de la sécurité](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduction à l'évaluation des performances](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scénario 2 : Évaluation du modèle Phi-3 / Phi-3.5 dans Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Avant de commencer](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Déployer Azure OpenAI pour évaluer le modèle Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Évaluer le modèle Phi-3 / Phi-3.5 ajusté à l'aide de Prompt flow dans Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Félicitations !](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scénario 1 : Introduction à l'évaluation de Prompt flow dans Azure AI Foundry**

### Introduction à l'évaluation de la sécurité

Pour garantir que votre modèle d'IA est éthique et sûr, il est crucial de l'évaluer selon les principes d'IA responsable de Microsoft. Dans Azure AI Foundry, les évaluations de sécurité permettent d'analyser la vulnérabilité de votre modèle face aux attaques de contournement (jailbreak) et son potentiel à générer du contenu nuisible, en conformité avec ces principes.

![Évaluation de la sécurité.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.fr.png)

*Source de l'image : [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principes d'IA responsable de Microsoft

Avant de commencer les étapes techniques, il est essentiel de comprendre les principes d'IA responsable de Microsoft, un cadre éthique conçu pour guider le développement, le déploiement et l'exploitation responsables des systèmes d'IA. Ces principes garantissent que les technologies d'IA sont conçues de manière équitable, transparente et inclusive. Ils servent de base pour évaluer la sécurité des modèles d'IA.

Les principes d'IA responsable de Microsoft incluent :

- **Équité et inclusivité** : Les systèmes d'IA doivent traiter tout le monde équitablement et éviter d'avoir des impacts différents sur des groupes de personnes similaires. Par exemple, lorsqu'un système d'IA fournit des conseils sur des traitements médicaux, des demandes de prêt ou des emplois, il doit faire les mêmes recommandations pour des personnes ayant des symptômes, des situations financières ou des qualifications professionnelles similaires.

- **Fiabilité et sécurité** : Pour instaurer la confiance, il est essentiel que les systèmes d'IA fonctionnent de manière fiable, sûre et cohérente. Ces systèmes doivent être capables de fonctionner comme initialement prévu, de répondre en toute sécurité à des conditions imprévues et de résister à des manipulations nuisibles. Leur comportement doit refléter la variété des situations anticipées lors de leur conception et de leur test.

- **Transparence** : Lorsque les systèmes d'IA aident à prendre des décisions ayant un impact significatif sur la vie des gens, il est crucial que ces derniers comprennent comment ces décisions ont été prises. Par exemple, une banque pourrait utiliser un système d'IA pour évaluer la solvabilité d'une personne. Une entreprise pourrait utiliser un système d'IA pour identifier les candidats les plus qualifiés à embaucher.

- **Confidentialité et sécurité** : À mesure que l'IA devient plus répandue, la protection de la vie privée et la sécurisation des informations personnelles et professionnelles deviennent plus importantes et complexes. Avec l'IA, la confidentialité et la sécurité des données nécessitent une attention particulière, car l'accès aux données est essentiel pour permettre aux systèmes d'IA de faire des prédictions et des décisions précises et éclairées.

- **Responsabilité** : Les personnes qui conçoivent et déploient les systèmes d'IA doivent être responsables de leur fonctionnement. Les organisations doivent s'appuyer sur des normes industrielles pour développer des normes de responsabilité. Ces normes peuvent garantir que les systèmes d'IA ne sont pas l'autorité finale sur toute décision affectant la vie des gens. Elles peuvent également garantir que les humains conservent un contrôle significatif sur les systèmes d'IA hautement autonomes.

![Hub d'IA responsable.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.fr.png)

*Source de l'image : [Qu'est-ce que l'IA responsable ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pour en savoir plus sur les principes d'IA responsable de Microsoft, visitez la page [Qu'est-ce que l'IA responsable ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Mesures de sécurité

Dans ce tutoriel, vous évaluerez la sécurité du modèle Phi-3 ajusté à l'aide des mesures de sécurité d'Azure AI Foundry. Ces mesures vous aident à évaluer le potentiel du modèle à générer du contenu nuisible et sa vulnérabilité aux attaques de contournement. Les mesures de sécurité incluent :

- **Contenu lié à l'automutilation** : Évalue si le modèle a tendance à produire du contenu lié à l'automutilation.
- **Contenu haineux et injuste** : Évalue si le modèle a tendance à produire du contenu haineux ou injuste.
- **Contenu violent** : Évalue si le modèle a tendance à produire du contenu violent.
- **Contenu sexuel** : Évalue si le modèle a tendance à produire du contenu sexuel inapproprié.

Évaluer ces aspects garantit que le modèle d'IA ne produit pas de contenu nuisible ou offensant, en accord avec les valeurs sociétales et les normes réglementaires.

![Évaluer en fonction de la sécurité.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.fr.png)

### Introduction à l'évaluation des performances

Pour garantir que votre modèle d'IA fonctionne comme prévu, il est important d'évaluer ses performances selon des mesures spécifiques. Dans Azure AI Foundry, les évaluations des performances permettent d'analyser l'efficacité de votre modèle à générer des réponses précises, pertinentes et cohérentes.

![Évaluation des performances.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.fr.png)

*Source de l'image : [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Mesures de performance

Dans ce tutoriel, vous évaluerez les performances du modèle Phi-3 / Phi-3.5 ajusté à l'aide des mesures de performance d'Azure AI Foundry. Ces mesures vous aident à analyser l'efficacité du modèle à générer des réponses précises, pertinentes et cohérentes. Les mesures de performance incluent :

- **Ancrage** : Évalue dans quelle mesure les réponses générées s'alignent sur les informations de la source d'entrée.
- **Pertinence** : Évalue la pertinence des réponses générées par rapport aux questions posées.
- **Cohérence** : Évalue la fluidité du texte généré, sa lecture naturelle et sa ressemblance avec un langage humain.
- **Fluidité** : Évalue la maîtrise linguistique du texte généré.
- **Similarité GPT** : Compare la réponse générée avec la vérité terrain pour la similarité.
- **Score F1** : Calcule le ratio de mots communs entre la réponse générée et les données sources.

Ces mesures vous aident à évaluer l'efficacité du modèle à générer des réponses précises, pertinentes et cohérentes.

![Évaluer en fonction des performances.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.fr.png)

## **Scénario 2 : Évaluation du modèle Phi-3 / Phi-3.5 dans Azure AI Foundry**

### Avant de commencer

Ce tutoriel fait suite aux articles de blog précédents, "[Ajuster et intégrer des modèles Phi-3 personnalisés avec Prompt Flow : Guide étape par étape](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" et "[Ajuster et intégrer des modèles Phi-3 personnalisés avec Prompt Flow dans Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Dans ces articles, nous avons décrit le processus d'ajustement d'un modèle Phi-3 / Phi-3.5 dans Azure AI Foundry et son intégration avec Prompt flow.

Dans ce tutoriel, vous déploierez un modèle Azure OpenAI en tant qu'évaluateur dans Azure AI Foundry et l'utiliserez pour évaluer votre modèle Phi-3 / Phi-3.5 ajusté.

Avant de commencer ce tutoriel, assurez-vous de disposer des prérequis suivants, comme décrit dans les tutoriels précédents :

1. Un jeu de données préparé pour évaluer le modèle Phi-3 / Phi-3.5 ajusté.
1. Un modèle Phi-3 / Phi-3.5 ajusté et déployé dans Azure Machine Learning.
1. Un Prompt flow intégré à votre modèle Phi-3 / Phi-3.5 ajusté dans Azure AI Foundry.

> [!NOTE]
> Vous utiliserez le fichier *test_data.jsonl*, situé dans le dossier des données du jeu de données **ULTRACHAT_200k** téléchargé dans les articles de blog précédents, comme jeu de données pour évaluer le modèle Phi-3 / Phi-3.5 ajusté.

#### Intégrer le modèle personnalisé Phi-3 / Phi-3.5 avec Prompt flow dans Azure AI Foundry (approche "code first")

> [!NOTE]
> Si vous avez suivi l'approche "low-code" décrite dans "[Ajuster et intégrer des modèles Phi-3 personnalisés avec Prompt Flow dans Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", vous pouvez passer cet exercice et passer au suivant.
> Cependant, si vous avez suivi l'approche "code-first" décrite dans "[Ajuster et intégrer des modèles Phi-3 personnalisés avec Prompt Flow : Guide étape par étape](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" pour ajuster et déployer votre modèle Phi-3 / Phi-3.5, le processus de connexion de votre modèle à Prompt flow est légèrement différent. Vous apprendrez ce processus dans cet exercice.

Pour continuer, vous devez intégrer votre modèle Phi-3 / Phi-3.5 ajusté à Prompt flow dans Azure AI Foundry.

#### Créer un Hub Azure AI Foundry

Vous devez créer un Hub avant de créer un Projet. Un Hub agit comme un groupe de ressources, vous permettant d'organiser et de gérer plusieurs Projets au sein d'Azure AI Foundry.

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Sélectionnez **Tous les hubs** dans l'onglet latéral gauche.

1. Sélectionnez **+ Nouveau hub** dans le menu de navigation.

    ![Créer un hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.fr.png)

1. Effectuez les tâches suivantes :

    - Entrez un **Nom de hub** unique.
    - Sélectionnez votre **Abonnement Azure**.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Région** souhaitée.
    - Sélectionnez le **Service Azure AI connecté** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Ignorer la connexion** pour **Connecter Azure AI Search**.
![Remplir le hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.fr.png)

1. Sélectionnez **Suivant**.

#### Créer un projet Azure AI Foundry

1. Dans le Hub que vous avez créé, sélectionnez **Tous les projets** dans l'onglet de gauche.

1. Sélectionnez **+ Nouveau projet** dans le menu de navigation.

    ![Sélectionner un nouveau projet.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.fr.png)

1. Entrez **Nom du projet**. Il doit s'agir d'une valeur unique.

    ![Créer un projet.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.fr.png)

1. Sélectionnez **Créer un projet**.

#### Ajouter une connexion personnalisée pour le modèle Phi-3 / Phi-3.5 ajusté

Pour intégrer votre modèle Phi-3 / Phi-3.5 personnalisé avec Prompt flow, vous devez enregistrer l'endpoint et la clé du modèle dans une connexion personnalisée. Cette configuration garantit l'accès à votre modèle personnalisé dans Prompt flow.

#### Définir la clé API et l'URI de l'endpoint du modèle Phi-3 / Phi-3.5 ajusté

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Accédez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l'onglet de gauche.

    ![Sélectionner endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.fr.png)

1. Sélectionnez l'endpoint que vous avez créé.

    ![Sélectionner l'endpoint créé.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.fr.png)

1. Sélectionnez **Consommer** dans le menu de navigation.

1. Copiez votre **Endpoint REST** et **Clé primaire**.

    ![Copier la clé API et l'URI de l'endpoint.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.fr.png)

#### Ajouter la connexion personnalisée

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Dans le projet que vous avez créé, sélectionnez **Paramètres** dans l'onglet de gauche.

1. Sélectionnez **+ Nouvelle connexion**.

    ![Sélectionner une nouvelle connexion.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.fr.png)

1. Sélectionnez **Clés personnalisées** dans le menu de navigation.

    ![Sélectionner clés personnalisées.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez **+ Ajouter des paires clé-valeur**.
    - Pour le nom de la clé, entrez **endpoint** et collez l'endpoint que vous avez copié depuis Azure ML Studio dans le champ de valeur.
    - Sélectionnez **+ Ajouter des paires clé-valeur** à nouveau.
    - Pour le nom de la clé, entrez **key** et collez la clé que vous avez copiée depuis Azure ML Studio dans le champ de valeur.
    - Après avoir ajouté les clés, sélectionnez **est secret** pour éviter que la clé ne soit exposée.

    ![Ajouter une connexion.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.fr.png)

1. Sélectionnez **Ajouter une connexion**.

#### Créer un Prompt flow

Vous avez ajouté une connexion personnalisée dans Azure AI Foundry. Maintenant, créons un Prompt flow en suivant les étapes ci-dessous. Ensuite, vous connecterez ce Prompt flow à la connexion personnalisée pour utiliser le modèle ajusté dans le Prompt flow.

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Sélectionnez **Prompt flow** dans l'onglet de gauche.

1. Sélectionnez **+ Créer** dans le menu de navigation.

    ![Sélectionner Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.fr.png)

1. Sélectionnez **Chat flow** dans le menu de navigation.

    ![Sélectionner chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.fr.png)

1. Entrez **Nom du dossier** à utiliser.

    ![Sélectionner chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.fr.png)

1. Sélectionnez **Créer**.

#### Configurer le Prompt flow pour discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé

Vous devez intégrer le modèle ajusté Phi-3 / Phi-3.5 dans un Prompt flow. Cependant, le Prompt flow existant fourni n'est pas conçu à cet effet. Par conséquent, vous devez repenser le Prompt flow pour permettre l'intégration du modèle personnalisé.

1. Dans le Prompt flow, effectuez les tâches suivantes pour reconstruire le flux existant :

    - Sélectionnez **Mode fichier brut**.
    - Supprimez tout le code existant dans le fichier *flow.dag.yml*.
    - Ajoutez le code suivant dans *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

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

    ![Sélectionner mode fichier brut.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.fr.png)

1. Ajoutez le code suivant dans *integrate_with_promptflow.py* pour utiliser le modèle Phi-3 / Phi-3.5 personnalisé dans Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Coller le code du prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.fr.png)

> [!NOTE]
> Pour des informations plus détaillées sur l'utilisation de Prompt flow dans Azure AI Foundry, vous pouvez consulter [Prompt flow dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Sélectionnez **Entrée chat**, **Sortie chat** pour activer la discussion avec votre modèle.

    ![Sélectionner Entrée Sortie.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.fr.png)

1. Vous êtes maintenant prêt à discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé. Dans le prochain exercice, vous apprendrez à démarrer Prompt flow et à l'utiliser pour discuter avec votre modèle ajusté Phi-3 / Phi-3.5.

> [!NOTE]
>
> Le flux reconstruit devrait ressembler à l'image ci-dessous :
>
> ![Exemple de flux.](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.fr.png)
>

#### Démarrer Prompt flow

1. Sélectionnez **Démarrer les sessions de calcul** pour démarrer Prompt flow.

    ![Démarrer une session de calcul.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.fr.png)

1. Sélectionnez **Valider et analyser l'entrée** pour renouveler les paramètres.

    ![Valider l'entrée.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.fr.png)

1. Sélectionnez la **Valeur** de la **connexion** vers la connexion personnalisée que vous avez créée. Par exemple, *connexion*.

    ![Connexion.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.fr.png)

#### Discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé

1. Sélectionnez **Chat**.

    ![Sélectionner chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.fr.png)

1. Voici un exemple des résultats : vous pouvez désormais discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé. Il est recommandé de poser des questions basées sur les données utilisées pour l'ajustement.

    ![Discuter avec Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.fr.png)

### Déployer Azure OpenAI pour évaluer le modèle Phi-3 / Phi-3.5

Pour évaluer le modèle Phi-3 / Phi-3.5 dans Azure AI Foundry, vous devez déployer un modèle Azure OpenAI. Ce modèle sera utilisé pour évaluer les performances du modèle Phi-3 / Phi-3.5.

#### Déployer Azure OpenAI

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Foundry que vous avez créé.

    ![Sélectionner le projet.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.fr.png)

1. Dans le projet que vous avez créé, sélectionnez **Déploiements** dans l'onglet de gauche.

1. Sélectionnez **+ Déployer un modèle** dans le menu de navigation.

1. Sélectionnez **Déployer un modèle de base**.

    ![Sélectionner Déploiements.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.fr.png)

1. Sélectionnez le modèle Azure OpenAI que vous souhaitez utiliser. Par exemple, **gpt-4o**.

    ![Sélectionner le modèle Azure OpenAI à utiliser.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.fr.png)

1. Sélectionnez **Confirmer**.

### Évaluer le modèle Phi-3 / Phi-3.5 ajusté à l'aide de l'évaluation Prompt flow d'Azure AI Foundry

### Lancer une nouvelle évaluation

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Foundry que vous avez créé.

    ![Sélectionner le projet.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.fr.png)

1. Dans le projet que vous avez créé, sélectionnez **Évaluation** dans l'onglet de gauche.

1. Sélectionnez **+ Nouvelle évaluation** dans le menu de navigation.
![Sélectionnez l'évaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.fr.png)

1. Sélectionnez l'évaluation **Prompt flow**.

    ![Sélectionnez l'évaluation Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.fr.png)

1. Effectuez les tâches suivantes :

    - Entrez le nom de l'évaluation. Il doit être une valeur unique.
    - Sélectionnez **Question et réponse sans contexte** comme type de tâche. En effet, le jeu de données **UlTRACHAT_200k** utilisé dans ce tutoriel ne contient pas de contexte.
    - Sélectionnez le flux d'invite que vous souhaitez évaluer.

    ![Évaluation du flux d'invite.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.fr.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes :

    - Sélectionnez **Ajouter votre jeu de données** pour télécharger le jeu de données. Par exemple, vous pouvez télécharger le fichier de test, tel que *test_data.json1*, qui est inclus lorsque vous téléchargez le jeu de données **ULTRACHAT_200k**.
    - Sélectionnez la **Colonne du jeu de données** appropriée correspondant à votre jeu de données. Par exemple, si vous utilisez le jeu de données **ULTRACHAT_200k**, sélectionnez **${data.prompt}** comme colonne du jeu de données.

    ![Évaluation du flux d'invite.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.fr.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes pour configurer les métriques de performance et de qualité :

    - Sélectionnez les métriques de performance et de qualité que vous souhaitez utiliser.
    - Sélectionnez le modèle Azure OpenAI que vous avez créé pour l'évaluation. Par exemple, sélectionnez **gpt-4o**.

    ![Évaluation du flux d'invite.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.fr.png)

1. Effectuez les tâches suivantes pour configurer les métriques de risque et de sécurité :

    - Sélectionnez les métriques de risque et de sécurité que vous souhaitez utiliser.
    - Sélectionnez le seuil pour calculer le taux de défaut que vous souhaitez utiliser. Par exemple, sélectionnez **Moyen**.
    - Pour **question**, sélectionnez **Source de données** sur **{$data.prompt}**.
    - Pour **réponse**, sélectionnez **Source de données** sur **{$run.outputs.answer}**.
    - Pour **vérité terrain**, sélectionnez **Source de données** sur **{$data.message}**.

    ![Évaluation du flux d'invite.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.fr.png)

1. Sélectionnez **Suivant**.

1. Sélectionnez **Soumettre** pour démarrer l'évaluation.

1. L'évaluation prendra un certain temps pour se terminer. Vous pouvez surveiller la progression dans l'onglet **Évaluation**.

### Examiner les résultats de l'évaluation

> [!NOTE]
> Les résultats présentés ci-dessous sont destinés à illustrer le processus d'évaluation. Dans ce tutoriel, nous avons utilisé un modèle affiné sur un jeu de données relativement petit, ce qui peut entraîner des résultats sous-optimaux. Les résultats réels peuvent varier considérablement en fonction de la taille, de la qualité et de la diversité du jeu de données utilisé, ainsi que de la configuration spécifique du modèle.

Une fois l'évaluation terminée, vous pouvez examiner les résultats pour les métriques de performance et de sécurité.

1. Métriques de performance et de qualité :

    - Évaluez l'efficacité du modèle dans la génération de réponses cohérentes, fluides et pertinentes.

    ![Résultat de l'évaluation.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.fr.png)

1. Métriques de risque et de sécurité :

    - Assurez-vous que les sorties du modèle sont sûres et alignées avec les Principes d'IA Responsable, évitant tout contenu nuisible ou offensant.

    ![Résultat de l'évaluation.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.fr.png)

1. Vous pouvez faire défiler vers le bas pour voir les **résultats détaillés des métriques**.

    ![Résultat de l'évaluation.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.fr.png)

1. En évaluant votre modèle personnalisé Phi-3 / Phi-3.5 sur les métriques de performance et de sécurité, vous pouvez confirmer que le modèle est non seulement efficace, mais également conforme aux pratiques d'IA Responsable, le rendant prêt pour un déploiement dans le monde réel.

## Félicitations !

### Vous avez terminé ce tutoriel

Vous avez évalué avec succès le modèle Phi-3 affiné intégré avec Prompt flow dans Azure AI Foundry. Il s'agit d'une étape importante pour garantir que vos modèles d'IA non seulement performent bien, mais respectent également les principes d'IA Responsable de Microsoft, vous aidant à créer des applications d'IA fiables et dignes de confiance.

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.fr.png)

## Nettoyer les ressources Azure

Nettoyez vos ressources Azure pour éviter des frais supplémentaires sur votre compte. Accédez au portail Azure et supprimez les ressources suivantes :

- La ressource Azure Machine Learning.
- Le point de terminaison du modèle Azure Machine Learning.
- La ressource de projet Azure AI Foundry.
- La ressource Prompt flow d'Azure AI Foundry.

### Étapes Suivantes

#### Documentation

- [Évaluer les systèmes d'IA à l'aide du tableau de bord IA Responsable](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métriques d'évaluation et de surveillance pour l'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentation Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentation Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenu de Formation

- [Introduction à l'approche d'IA Responsable de Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction à Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Références

- [Qu'est-ce que l'IA Responsable ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Annonce de nouveaux outils dans Azure AI pour vous aider à créer des applications d'IA générative plus sûres et fiables](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.