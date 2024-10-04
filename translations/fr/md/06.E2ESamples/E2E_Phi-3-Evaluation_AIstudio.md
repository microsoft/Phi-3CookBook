# Évaluer le modèle Phi-3 / Phi-3.5 affiné dans Azure AI Studio en se concentrant sur les principes d'IA responsable de Microsoft

Cet exemple de bout en bout (E2E) est basé sur le guide "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Studio Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" de la communauté technique de Microsoft.

## Aperçu

### Comment évaluer la sécurité et les performances d'un modèle Phi-3 / Phi-3.5 affiné dans Azure AI Studio ?

Affiner un modèle peut parfois conduire à des réponses non intentionnelles ou indésirables. Pour garantir que le modèle reste sûr et efficace, il est important d'évaluer son potentiel à générer du contenu nuisible et sa capacité à produire des réponses précises, pertinentes et cohérentes. Dans ce tutoriel, vous apprendrez comment évaluer la sécurité et les performances d'un modèle Phi-3 / Phi-3.5 affiné intégré avec Prompt flow dans Azure AI Studio.

Voici le processus d'évaluation d'Azure AI Studio.

![Architecture du tutoriel.](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.fr.png)

*Source de l'image : [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pour plus d'informations détaillées et pour explorer des ressources supplémentaires sur Phi-3 / Phi-3.5, veuillez visiter le [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prérequis

- [Python](https://www.python.org/downloads)
- [Abonnement Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modèle Phi-3 / Phi-3.5 affiné

### Table des matières

1. [**Scénario 1 : Introduction à l'évaluation du flux de prompts d'Azure AI Studio**](../../../../md/06.E2ESamples)

    - [Introduction à l'évaluation de la sécurité](../../../../md/06.E2ESamples)
    - [Introduction à l'évaluation des performances](../../../../md/06.E2ESamples)

1. [**Scénario 2 : Évaluation du modèle Phi-3 / Phi-3.5 dans Azure AI Studio**](../../../../md/06.E2ESamples)

    - [Avant de commencer](../../../../md/06.E2ESamples)
    - [Déployer Azure OpenAI pour évaluer le modèle Phi-3 / Phi-3.5](../../../../md/06.E2ESamples)
    - [Évaluer le modèle Phi-3 / Phi-3.5 affiné en utilisant l'évaluation du flux de prompts d'Azure AI Studio](../../../../md/06.E2ESamples)

1. [Félicitations !](../../../../md/06.E2ESamples)

## **Scénario 1 : Introduction à l'évaluation du flux de prompts d'Azure AI Studio**

### Introduction à l'évaluation de la sécurité

Pour garantir que votre modèle d'IA est éthique et sûr, il est crucial de l'évaluer par rapport aux principes d'IA responsable de Microsoft. Dans Azure AI Studio, les évaluations de sécurité vous permettent d'évaluer la vulnérabilité de votre modèle aux attaques de type jailbreak et son potentiel à générer du contenu nuisible, ce qui est directement aligné avec ces principes.

![Évaluation de la sécurité.](../../../../translated_images/safety-evaluation.5ad906c4618e4c8736fdeeff54a52dac8ae6d0756b15824e430177fba7b6a8b4.fr.png)

*Source de l'image : [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principes d'IA responsable de Microsoft

Avant de commencer les étapes techniques, il est essentiel de comprendre les principes d'IA responsable de Microsoft, un cadre éthique conçu pour guider le développement, le déploiement et l'exploitation responsables des systèmes d'IA. Ces principes guident la conception, le développement et le déploiement responsables des systèmes d'IA, garantissant que les technologies d'IA sont construites de manière équitable, transparente et inclusive. Ces principes sont la base pour évaluer la sécurité des modèles d'IA.

Les principes d'IA responsable de Microsoft incluent :

- **Équité et inclusivité** : Les systèmes d'IA doivent traiter tout le monde équitablement et éviter de traiter différemment des groupes de personnes similaires. Par exemple, lorsque les systèmes d'IA fournissent des conseils sur le traitement médical, les demandes de prêt ou l'emploi, ils doivent faire les mêmes recommandations à tous ceux qui ont des symptômes, des circonstances financières ou des qualifications professionnelles similaires.

- **Fiabilité et sécurité** : Pour instaurer la confiance, il est essentiel que les systèmes d'IA fonctionnent de manière fiable, sûre et cohérente. Ces systèmes doivent pouvoir fonctionner comme ils ont été conçus à l'origine, répondre en toute sécurité à des conditions imprévues et résister à toute manipulation nuisible. Leur comportement et la variété des conditions qu'ils peuvent gérer reflètent la gamme de situations et de circonstances anticipées par les développeurs lors de la conception et des tests.

- **Transparence** : Lorsque les systèmes d'IA aident à prendre des décisions ayant un impact considérable sur la vie des gens, il est crucial que les gens comprennent comment ces décisions ont été prises. Par exemple, une banque pourrait utiliser un système d'IA pour décider si une personne est solvable. Une entreprise pourrait utiliser un système d'IA pour déterminer les candidats les plus qualifiés à embaucher.

- **Confidentialité et sécurité** : À mesure que l'IA devient plus répandue, la protection de la vie privée et la sécurisation des informations personnelles et professionnelles deviennent de plus en plus importantes et complexes. Avec l'IA, la confidentialité et la sécurité des données nécessitent une attention particulière car l'accès aux données est essentiel pour que les systèmes d'IA fassent des prédictions et des décisions précises et éclairées sur les personnes.

- **Responsabilité** : Les personnes qui conçoivent et déploient les systèmes d'IA doivent être responsables de leur fonctionnement. Les organisations devraient s'appuyer sur les normes de l'industrie pour développer des normes de responsabilité. Ces normes peuvent garantir que les systèmes d'IA ne sont pas l'autorité finale sur toute décision affectant la vie des gens. Elles peuvent également garantir que les humains maintiennent un contrôle significatif sur des systèmes d'IA autrement très autonomes.

![Hub de remplissage.](../../../../translated_images/responsibleai2.ae6f996d95dcc46b3b3087c0e4f4f4b74c64e961083009ecca7a0a3998b3f716.fr.png)

*Source de l'image : [Qu'est-ce que l'IA responsable ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pour en savoir plus sur les principes d'IA responsable de Microsoft, visitez la page [Qu'est-ce que l'IA responsable ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Indicateurs de sécurité

Dans ce tutoriel, vous évaluerez la sécurité du modèle Phi-3 affiné en utilisant les indicateurs de sécurité d'Azure AI Studio. Ces indicateurs vous aident à évaluer le potentiel du modèle à générer du contenu nuisible et sa vulnérabilité aux attaques de type jailbreak. Les indicateurs de sécurité incluent :

- **Contenu lié à l'automutilation** : Évalue si le modèle a tendance à produire du contenu lié à l'automutilation.
- **Contenu haineux et injuste** : Évalue si le modèle a tendance à produire du contenu haineux ou injuste.
- **Contenu violent** : Évalue si le modèle a tendance à produire du contenu violent.
- **Contenu sexuel** : Évalue si le modèle a tendance à produire du contenu sexuel inapproprié.

Évaluer ces aspects garantit que le modèle d'IA ne produit pas de contenu nuisible ou offensant, l'alignant ainsi avec les valeurs sociétales et les normes réglementaires.

![Évaluer en fonction de la sécurité.](../../../../translated_images/evaluate-based-on-safety.63d79ac01570713002d5d858bfbb8f4d7295557ae8829d0c379485d67a3fcd1c.fr.png)

### Introduction à l'évaluation des performances

Pour garantir que votre modèle d'IA fonctionne comme prévu, il est important d'évaluer ses performances par rapport à des indicateurs de performance. Dans Azure AI Studio, les évaluations de performance vous permettent d'évaluer l'efficacité de votre modèle à générer des réponses précises, pertinentes et cohérentes.

![Évaluation des performances.](../../../../translated_images/performance-evaluation.259c44647c74a80761cdcbaab2202142f99a5a0d28326c8a1eb6dc2765f5ef77.fr.png)

*Source de l'image : [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Indicateurs de performance

Dans ce tutoriel, vous évaluerez les performances du modèle Phi-3 / Phi-3.5 affiné en utilisant les indicateurs de performance d'Azure AI Studio. Ces indicateurs vous aident à évaluer l'efficacité du modèle à générer des réponses précises, pertinentes et cohérentes. Les indicateurs de performance incluent :

- **Ancrage** : Évalue la mesure dans laquelle les réponses générées s'alignent sur les informations de la source d'entrée.
- **Pertinence** : Évalue la pertinence des réponses générées par rapport aux questions posées.
- **Cohérence** : Évalue la fluidité du texte généré, sa lisibilité naturelle et sa ressemblance avec le langage humain.
- **Fluidité** : Évalue la maîtrise linguistique du texte généré.
- **Similarité GPT** : Compare la réponse générée avec la vérité terrain pour la similarité.
- **Score F1** : Calcule le ratio des mots partagés entre la réponse générée et les données sources.

Ces indicateurs vous aident à évaluer l'efficacité du modèle à générer des réponses précises, pertinentes et cohérentes.

![Évaluer en fonction des performances.](../../../../translated_images/evaluate-based-on-performance.33ccf1c52f210af8e76d9cab863716d3f67db3d765254371a30136cc8f852b37.fr.png)

## **Scénario 2 : Évaluation du modèle Phi-3 / Phi-3.5 dans Azure AI Studio**

### Avant de commencer

Ce tutoriel fait suite aux articles de blog précédents, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" et "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Dans ces articles, nous avons parcouru le processus d'affinage d'un modèle Phi-3 / Phi-3.5 dans Azure AI Studio et son intégration avec Prompt flow.

Dans ce tutoriel, vous déploierez un modèle Azure OpenAI en tant qu'évaluateur dans Azure AI Studio et l'utiliserez pour évaluer votre modèle Phi-3 / Phi-3.5 affiné.

Avant de commencer ce tutoriel, assurez-vous d'avoir les prérequis suivants, comme décrit dans les tutoriels précédents :

1. Un jeu de données préparé pour évaluer le modèle Phi-3 / Phi-3.5 affiné.
1. Un modèle Phi-3 / Phi-3.5 qui a été affiné et déployé dans Azure Machine Learning.
1. Un flux de prompts intégré à votre modèle Phi-3 / Phi-3.5 affiné dans Azure AI Studio.

> [!NOTE]
> Vous utiliserez le fichier *test_data.jsonl*, situé dans le dossier de données du jeu de données **ULTRACHAT_200k** téléchargé dans les articles de blog précédents, comme jeu de données pour évaluer le modèle Phi-3 / Phi-3.5 affiné.

#### Intégrer le modèle Phi-3 / Phi-3.5 personnalisé avec Prompt flow dans Azure AI Studio (Approche code-first)

> [!NOTE]
> Si vous avez suivi l'approche low-code décrite dans "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", vous pouvez passer cet exercice et passer au suivant.
> Cependant, si vous avez suivi l'approche code-first décrite dans "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" pour affiner et déployer votre modèle Phi-3 / Phi-3.5, le processus de connexion de votre modèle à Prompt flow est légèrement différent. Vous apprendrez ce processus dans cet exercice.

Pour continuer, vous devez intégrer votre modèle Phi-3 / Phi-3.5 affiné dans Prompt flow dans Azure AI Studio.

#### Créer un hub Azure AI Studio

Vous devez créer un hub avant de créer le projet. Un hub agit comme un groupe de ressources, vous permettant d'organiser et de gérer plusieurs projets dans Azure AI Studio.

1. Connectez-vous à [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Sélectionnez **Tous les hubs** dans l'onglet de gauche.

1. Sélectionnez **+ Nouveau hub** dans le menu de navigation.

    ![Créer un hub.](../../../../translated_images/create-hub.8d452311ef5b4b9188df89f7cff7797c67ec8f391282235b19b988e167f3e920.fr.png)

1. Effectuez les tâches suivantes :

    - Entrez **Nom du hub**. Il doit s'agir d'une valeur unique.
    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez l'**Emplacement** que vous souhaitez utiliser.
    - Sélectionnez les **Services Azure AI** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Connecter Azure AI Search** pour **Passer la connexion**.
![Remplir le hub.](../../../../translated_images/fill-hub.8b19834866ef631a2fd031584c77b78c0438a385bdee8f981361b14bbc46f5e1.fr.png)

1. Sélectionnez **Suivant**.

#### Créer un projet Azure AI Studio

1. Dans le hub que vous avez créé, sélectionnez **Tous les projets** dans l'onglet de gauche.

1. Sélectionnez **+ Nouveau projet** dans le menu de navigation.

    ![Sélectionner nouveau projet.](../../../../translated_images/select-new-project.1a925c25ca3bc47b2b16feefc5a76f5c29e211ac464ea5c3cdfe389868d87da7.fr.png)

1. Entrez **Nom du projet**. Il doit être unique.

    ![Créer un projet.](../../../../translated_images/create-project.ff239752937343b4cb38156740ebda92bc1d8b16299183c245f3e3661432db31.fr.png)

1. Sélectionnez **Créer un projet**.

#### Ajouter une connexion personnalisée pour le modèle Phi-3 / Phi-3.5 ajusté

Pour intégrer votre modèle Phi-3 / Phi-3.5 ajusté avec Prompt flow, vous devez enregistrer l'endpoint et la clé du modèle dans une connexion personnalisée. Cette configuration garantit l'accès à votre modèle personnalisé dans Prompt flow.

#### Définir la clé API et l'uri de l'endpoint du modèle Phi-3 / Phi-3.5 ajusté

1. Visitez [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Accédez à l'espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l'onglet de gauche.

    ![Sélectionner endpoints.](../../../../translated_images/select-endpoints.3027748aed379990fd8ee9bf27f70ff11918955bb1a10269e2f34f6931b26955.fr.png)

1. Sélectionnez l'endpoint que vous avez créé.

    ![Sélectionner endpoints.](../../../../translated_images/select-endpoint-created.560a5cadfbbb58b66abb2fb61b4450b22060371910af1b45c358bde548234ebc.fr.png)

1. Sélectionnez **Consommer** dans le menu de navigation.

1. Copiez votre **endpoint REST** et **clé principale**.

    ![Copier la clé API et l'uri de l'endpoint.](../../../../translated_images/copy-endpoint-key.56de01742992f2402d57139849304b5b049fb468fb38abc7982b7dfc311daf9e.fr.png)

#### Ajouter la connexion personnalisée

1. Visitez [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Studio que vous avez créé.

1. Dans le projet que vous avez créé, sélectionnez **Paramètres** dans l'onglet de gauche.

1. Sélectionnez **+ Nouvelle connexion**.

    ![Sélectionner nouvelle connexion.](../../../../translated_images/select-new-connection.a1ff72172d07054308a3fc7b7b86e25e9ca1c879f0a382b9a2be2c80bb2ebcc5.fr.png)

1. Sélectionnez **Clés personnalisées** dans le menu de navigation.

    ![Sélectionner clés personnalisées.](../../../../translated_images/select-custom-keys.b17eb3b15eae28126a4eeda8f53396b9a6f773745f2dd68c464252575a77b5d3.fr.png)

1. Effectuez les tâches suivantes :

    - Sélectionnez **+ Ajouter des paires clé-valeur**.
    - Pour le nom de la clé, entrez **endpoint** et collez l'endpoint que vous avez copié depuis Azure ML Studio dans le champ de valeur.
    - Sélectionnez **+ Ajouter des paires clé-valeur** à nouveau.
    - Pour le nom de la clé, entrez **key** et collez la clé que vous avez copiée depuis Azure ML Studio dans le champ de valeur.
    - Après avoir ajouté les clés, sélectionnez **est secret** pour éviter que la clé ne soit exposée.

    ![Ajouter la connexion.](../../../../translated_images/add-connection.c01c94851c9eece708711456a4853355b9532b0cb1f970e24f165e7e1d6c0a03.fr.png)

1. Sélectionnez **Ajouter la connexion**.

#### Créer un Prompt flow

Vous avez ajouté une connexion personnalisée dans Azure AI Studio. Maintenant, créons un Prompt flow en suivant les étapes suivantes. Ensuite, vous connecterez ce Prompt flow à la connexion personnalisée pour utiliser le modèle ajusté dans le Prompt flow.

1. Accédez au projet Azure AI Studio que vous avez créé.

1. Sélectionnez **Prompt flow** dans l'onglet de gauche.

1. Sélectionnez **+ Créer** dans le menu de navigation.

    ![Sélectionner Promptflow.](../../../../translated_images/select-promptflow.766ad0f2403e2bd6f374bee40a607321e3e2b416629063acf3204a983fb4bcaa.fr.png)

1. Sélectionnez **Chat flow** dans le menu de navigation.

    ![Sélectionner chat flow.](../../../../translated_images/select-flow-type.0e18b84032da1200e48a702e5140c1775b1eb6de9cf222c6a8007840fa278e97.fr.png)

1. Entrez **Nom du dossier** à utiliser.

    ![Sélectionner chat flow.](../../../../translated_images/enter-name.43919b211b1e8e0184536dc09184190e7e8c56bf960d4b5601443efddc757db4.fr.png)

1. Sélectionnez **Créer**.

#### Configurer Prompt flow pour discuter avec votre modèle Phi-3 / Phi-3.5 ajusté

Vous devez intégrer le modèle Phi-3 / Phi-3.5 ajusté dans un Prompt flow. Cependant, le Prompt flow existant fourni n'est pas conçu pour cela. Par conséquent, vous devez redessiner le Prompt flow pour permettre l'intégration du modèle personnalisé.

1. Dans le Prompt flow, effectuez les tâches suivantes pour reconstruire le flux existant :

    - Sélectionnez **Mode fichier brut**.
    - Supprimez tout le code existant dans le fichier *flow.dag.yml*.
    - Ajoutez le code suivant à *flow.dag.yml*.

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

    ![Sélectionner mode fichier brut.](../../../../translated_images/select-raw-file-mode.2084d7f905df40f69cc5ebe48efa2318e92fd069358625a92993ef614f189d84.fr.png)

1. Ajoutez le code suivant à *integrate_with_promptflow.py* pour utiliser le modèle Phi-3 / Phi-3.5 personnalisé dans Prompt flow.

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

    ![Coller le code prompt flow.](../../../../translated_images/paste-promptflow-code.667abbdf848fd03153828c0aa70dde58a851e09b1ba4c69bc6f686d2005656aa.fr.png)

> [!NOTE]
> Pour plus d'informations sur l'utilisation de Prompt flow dans Azure AI Studio, vous pouvez consulter [Prompt flow in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Sélectionnez **Entrée de chat**, **Sortie de chat** pour activer le chat avec votre modèle.

    ![Sélectionner Entrée Sortie.](../../../../translated_images/select-input-output.d4803eae144b03579db4a23def15c68bb50527017cdc4aa9f72c8679588a0f4c.fr.png)

1. Vous êtes maintenant prêt à discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé. Dans le prochain exercice, vous apprendrez comment démarrer Prompt flow et l'utiliser pour discuter avec votre modèle Phi-3 / Phi-3.5 ajusté.

> [!NOTE]
>
> Le flux reconstruit devrait ressembler à l'image ci-dessous :
>
> ![Exemple de flux](../../../../translated_images/graph-example.5b309021deca5b503270e50888da4784256730c210ed757f799f9bff0a12bb19.fr.png)
>

#### Démarrer Prompt flow

1. Sélectionnez **Démarrer les sessions de calcul** pour démarrer Prompt flow.

    ![Démarrer la session de calcul.](../../../../translated_images/start-compute-session.75300f481218ca70eae80304255956c71a9b6be31a18b43264118c19c0b1a016.fr.png)

1. Sélectionnez **Valider et analyser l'entrée** pour renouveler les paramètres.

    ![Valider l'entrée.](../../../../translated_images/validate-input.a6c90e55ce6117ea44e2acd88b8a20bc31136bf6c574b0a6c9217867201025c9.fr.png)

1. Sélectionnez la **Valeur** de la **connexion** à la connexion personnalisée que vous avez créée. Par exemple, *connexion*.

    ![Connexion.](../../../../translated_images/select-connection.6573a1269969a14c83c397334051f71057ec9a243e95ea1b849483bd7481ff6a.fr.png)

#### Discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé

1. Sélectionnez **Chat**.

    ![Sélectionner chat.](../../../../translated_images/select-chat.25eab3d62b0a6c4960f0ae1b5d6efd6b5847cc20d468fd28cb1f0d656936cc22.fr.png)

1. Voici un exemple de résultats : Vous pouvez maintenant discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé. Il est recommandé de poser des questions basées sur les données utilisées pour l'ajustement.

    ![Discuter avec prompt flow.](../../../../translated_images/chat-with-promptflow.105b5a3b70ff64725c1d4cd2e9c6b55301219c7d68c9bec59106a49fb8bf40f2.fr.png)

### Déployer Azure OpenAI pour évaluer le modèle Phi-3 / Phi-3.5

Pour évaluer le modèle Phi-3 / Phi-3.5 dans Azure AI Studio, vous devez déployer un modèle Azure OpenAI. Ce modèle sera utilisé pour évaluer les performances du modèle Phi-3 / Phi-3.5.

#### Déployer Azure OpenAI

1. Connectez-vous à [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Studio que vous avez créé.

    ![Sélectionner Projet.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.fr.png)

1. Dans le projet que vous avez créé, sélectionnez **Déploiements** dans l'onglet de gauche.

1. Sélectionnez **+ Déployer un modèle** dans le menu de navigation.

1. Sélectionnez **Déployer le modèle de base**.

    ![Sélectionner Déploiements.](../../../../translated_images/deploy-openai-model.f09a74e1f976b52f85fdef711372452b9faed270e9d015887e09f44b41bbc163.fr.png)

1. Sélectionnez le modèle Azure OpenAI que vous souhaitez utiliser. Par exemple, **gpt-4o**.

    ![Sélectionner le modèle Azure OpenAI que vous souhaitez utiliser.](../../../../translated_images/select-openai-model.29fbbd802d6a9aa941097ae80a0ffe256239e636190b7c1e49f28d3d66143a0d.fr.png)

1. Sélectionnez **Confirmer**.

### Évaluer le modèle Phi-3 / Phi-3.5 ajusté en utilisant l'évaluation Prompt flow d'Azure AI Studio

### Démarrer une nouvelle évaluation

1. Visitez [Azure AI Studio](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Studio que vous avez créé.

    ![Sélectionner Projet.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.fr.png)

1. Dans le projet que vous avez créé, sélectionnez **Évaluation** dans l'onglet de gauche.

1. Sélectionnez **+ Nouvelle évaluation** dans le menu de navigation.
![Select evaluation.](../../../../translated_images/select-evaluation.7d8a8228ebdf3f3b46bf5cf6ab5bdcb4565132ba6b28126d9757aaf3abade725.fr.png)

1. Sélectionnez l'évaluation **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../translated_images/promptflow-evaluation.ff4265fafd69c7f5ded1b5275cacecbd5f3272a6358c1f784f62e64bcb9e949f.fr.png)

1. Effectuez les tâches suivantes :

    - Entrez le nom de l'évaluation. Il doit être unique.
    - Sélectionnez **Question et réponse sans contexte** comme type de tâche. En effet, le jeu de données **UlTRACHAT_200k** utilisé dans ce tutoriel ne contient pas de contexte.
    - Sélectionnez le flux de prompts que vous souhaitez évaluer.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting1.d3b22a8343f8265807e2b507fa7eec9d86a9cefd4a67bc39ba2022d572f13e1d.fr.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes :

    - Sélectionnez **Ajouter votre jeu de données** pour télécharger le jeu de données. Par exemple, vous pouvez télécharger le fichier de test du jeu de données, tel que *test_data.json1*, inclus lorsque vous téléchargez le jeu de données **ULTRACHAT_200k**.
    - Sélectionnez la **Colonne du jeu de données** appropriée qui correspond à votre jeu de données. Par exemple, si vous utilisez le jeu de données **ULTRACHAT_200k**, sélectionnez **${data.prompt}** comme colonne du jeu de données.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting2.32749fa51bc4fdb32f75dfd09b96bee74454c51ce3084bcc6f95b7286177a657.fr.png)

1. Sélectionnez **Suivant**.

1. Effectuez les tâches suivantes pour configurer les métriques de performance et de qualité :

    - Sélectionnez les métriques de performance et de qualité que vous souhaitez utiliser.
    - Sélectionnez le modèle Azure OpenAI que vous avez créé pour l'évaluation. Par exemple, sélectionnez **gpt-4o**.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-1.db76b89d94911c84ece6ce793593a4289278e1b24520e38ecd8372f4b9dc1167.fr.png)

1. Effectuez les tâches suivantes pour configurer les métriques de risque et de sécurité :

    - Sélectionnez les métriques de risque et de sécurité que vous souhaitez utiliser.
    - Sélectionnez le seuil pour calculer le taux de défaut que vous souhaitez utiliser. Par exemple, sélectionnez **Moyen**.
    - Pour **question**, sélectionnez **Source de données** sur **{$data.prompt}**.
    - Pour **answer**, sélectionnez **Source de données** sur **{$run.outputs.answer}**.
    - Pour **ground_truth**, sélectionnez **Source de données** sur **{$data.message}**.

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-2.eb9892654970af140ebb74fcc99e06dad7eca3d38365e3f2cbe90101392f41ee.fr.png)

1. Sélectionnez **Suivant**.

1. Sélectionnez **Soumettre** pour démarrer l'évaluation.

1. L'évaluation prendra un certain temps pour se terminer. Vous pouvez suivre la progression dans l'onglet **Évaluation**.

### Examiner les résultats de l'évaluation

> [!NOTE]
> Les résultats présentés ci-dessous sont destinés à illustrer le processus d'évaluation. Dans ce tutoriel, nous avons utilisé un modèle affiné sur un jeu de données relativement petit, ce qui peut entraîner des résultats sous-optimaux. Les résultats réels peuvent varier considérablement en fonction de la taille, de la qualité et de la diversité du jeu de données utilisé, ainsi que de la configuration spécifique du modèle.

Une fois l'évaluation terminée, vous pouvez examiner les résultats pour les métriques de performance et de sécurité.

1. Métriques de performance et de qualité :

    - évaluez l'efficacité du modèle à générer des réponses cohérentes, fluides et pertinentes.

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu.5b6e301e6d1af6044819f4d3c8443cbc44fb7db54ebce208b4288744ca25e6e8.fr.png)

1. Métriques de risque et de sécurité :

    - Assurez-vous que les sorties du modèle sont sûres et alignées avec les Principes de l'IA Responsable, évitant tout contenu nuisible ou offensant.

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu-2.d867d40ee9dfebc40c878288b8dc8727721a2fec995904b1475c513f0960e8e0.fr.png)

1. Vous pouvez faire défiler vers le bas pour voir les **Résultats détaillés des métriques**.

    ![Evaluation result.](../../../../translated_images/detailed-metrics-result.6cf00c2b6026bb500ff758ee3047c20f600aab3878c892897e99e2e3a88fb002.fr.png)

1. En évaluant votre modèle personnalisé Phi-3 / Phi-3.5 par rapport aux métriques de performance et de sécurité, vous pouvez confirmer que le modèle est non seulement efficace, mais qu'il adhère également aux pratiques d'IA responsable, le rendant prêt pour une utilisation dans le monde réel.

## Félicitations !

### Vous avez terminé ce tutoriel

Vous avez réussi à évaluer le modèle affiné Phi-3 intégré avec Prompt flow dans Azure AI Studio. C'est une étape importante pour s'assurer que vos modèles d'IA non seulement fonctionnent bien, mais adhèrent également aux principes d'IA Responsable de Microsoft pour vous aider à créer des applications d'IA fiables et dignes de confiance.

![Architecture.](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.fr.png)

## Nettoyer les ressources Azure

Nettoyez vos ressources Azure pour éviter des frais supplémentaires sur votre compte. Allez sur le portail Azure et supprimez les ressources suivantes :

- La ressource Azure Machine Learning.
- Le point de terminaison du modèle Azure Machine Learning.
- La ressource du projet Azure AI Studio.
- La ressource Prompt flow d'Azure AI Studio.

### Étapes suivantes

#### Documentation

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [Évaluer les systèmes d'IA en utilisant le tableau de bord de l'IA Responsable](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métriques d'évaluation et de surveillance pour l'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentation Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentation Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenu de formation

- [Introduction à l'approche d'IA Responsable de Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction à Azure AI Studio](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Référence

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [Qu'est-ce que l'IA Responsable ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Annonce de nouveaux outils dans Azure AI pour vous aider à créer des applications d'IA générative plus sécurisées et fiables](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Évaluation des applications d'IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.