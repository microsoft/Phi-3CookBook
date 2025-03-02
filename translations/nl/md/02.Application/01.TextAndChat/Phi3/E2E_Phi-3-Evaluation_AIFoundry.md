# Evalueer het Fine-tuned Phi-3 / Phi-3.5 Model in Azure AI Foundry met Focus op de Responsible AI Principes van Microsoft

Dit end-to-end (E2E) voorbeeld is gebaseerd op de gids "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" van de Microsoft Tech Community.

## Overzicht

### Hoe kun je de veiligheid en prestaties van een fine-tuned Phi-3 / Phi-3.5 model in Azure AI Foundry evalueren?

Het fine-tunen van een model kan soms leiden tot onbedoelde of ongewenste reacties. Om ervoor te zorgen dat het model veilig en effectief blijft, is het belangrijk om het vermogen van het model om schadelijke inhoud te genereren te evalueren, evenals zijn vermogen om nauwkeurige, relevante en coherente reacties te produceren. In deze tutorial leer je hoe je de veiligheid en prestaties van een fine-tuned Phi-3 / Phi-3.5 model kunt evalueren dat is geïntegreerd met Prompt flow in Azure AI Foundry.

Hier is het evaluatieproces van Azure AI Foundry.

![Architectuur van de tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.nl.png)

*Afbeeldingsbron: [Evaluatie van generatieve AI-toepassingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Voor meer gedetailleerde informatie en om extra bronnen over Phi-3 / Phi-3.5 te verkennen, bezoek de [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Vereisten

- [Python](https://www.python.org/downloads)
- [Azure-abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 model

### Inhoudsopgave

1. [**Scenario 1: Introductie tot de Prompt flow evaluatie van Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introductie tot veiligheidsevaluatie](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introductie tot prestatie-evaluatie](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Het evalueren van het Phi-3 / Phi-3.5 model in Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Voordat je begint](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementeer Azure OpenAI om het Phi-3 / Phi-3.5 model te evalueren](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evalueer het fine-tuned Phi-3 / Phi-3.5 model met de Prompt flow evaluatie van Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gefeliciteerd!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introductie tot de Prompt flow evaluatie van Azure AI Foundry**

### Introductie tot veiligheidsevaluatie

Om ervoor te zorgen dat je AI-model ethisch en veilig is, is het cruciaal om het te evalueren aan de hand van de Responsible AI Principes van Microsoft. In Azure AI Foundry maken veiligheidsevaluaties het mogelijk om de kwetsbaarheid van je model voor jailbreak-aanvallen te beoordelen en het potentieel om schadelijke inhoud te genereren, wat direct in lijn is met deze principes.

![Veiligheidsevaluatie.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.nl.png)

*Afbeeldingsbron: [Evaluatie van generatieve AI-toepassingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Responsible AI Principes van Microsoft

Voordat je aan de technische stappen begint, is het belangrijk om de Responsible AI Principes van Microsoft te begrijpen, een ethisch kader dat is ontworpen om de verantwoorde ontwikkeling, implementatie en werking van AI-systemen te begeleiden. Deze principes sturen het verantwoord ontwerpen, ontwikkelen en implementeren van AI-systemen, zodat AI-technologieën eerlijk, transparant en inclusief worden gebouwd. Deze principes vormen de basis voor het evalueren van de veiligheid van AI-modellen.

De Responsible AI Principes van Microsoft omvatten:

- **Eerlijkheid en Inclusiviteit**: AI-systemen moeten iedereen eerlijk behandelen en voorkomen dat gelijksoortige groepen mensen verschillend worden behandeld. Bijvoorbeeld, wanneer AI-systemen advies geven over medische behandelingen, leningen of werkgelegenheid, moeten ze dezelfde aanbevelingen doen aan iedereen met vergelijkbare symptomen, financiële omstandigheden of professionele kwalificaties.

- **Betrouwbaarheid en Veiligheid**: Om vertrouwen op te bouwen, is het cruciaal dat AI-systemen betrouwbaar, veilig en consistent werken. Deze systemen moeten kunnen functioneren zoals oorspronkelijk ontworpen, veilig reageren op onverwachte omstandigheden en bestand zijn tegen schadelijke manipulatie. Hoe ze zich gedragen en de variëteit aan omstandigheden die ze aankunnen, weerspiegelen de situaties die ontwikkelaars tijdens ontwerp en testen hebben voorzien.

- **Transparantie**: Wanneer AI-systemen beslissingen ondersteunen die grote gevolgen hebben voor het leven van mensen, is het essentieel dat mensen begrijpen hoe die beslissingen zijn genomen. Bijvoorbeeld, een bank kan een AI-systeem gebruiken om te bepalen of iemand kredietwaardig is. Een bedrijf kan een AI-systeem gebruiken om de meest gekwalificeerde kandidaten te selecteren.

- **Privacy en Beveiliging**: Naarmate AI steeds meer voorkomt, wordt het beschermen van privacy en het beveiligen van persoonlijke en zakelijke informatie belangrijker en complexer. Bij AI vereisen privacy en gegevensbeveiliging extra aandacht, omdat toegang tot gegevens essentieel is voor AI-systemen om nauwkeurige en geïnformeerde voorspellingen en beslissingen te maken over mensen.

- **Verantwoordelijkheid**: De mensen die AI-systemen ontwerpen en implementeren, moeten verantwoordelijk zijn voor hoe hun systemen werken. Organisaties moeten gebruikmaken van industriestandaarden om normen voor verantwoordelijkheid te ontwikkelen. Deze normen kunnen ervoor zorgen dat AI-systemen niet de uiteindelijke autoriteit zijn bij beslissingen die het leven van mensen beïnvloeden. Ze kunnen ook garanderen dat mensen betekenisvolle controle behouden over anders zeer autonome AI-systemen.

![Vul hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.nl.png)

*Afbeeldingsbron: [Wat is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Voor meer informatie over de Responsible AI Principes van Microsoft, bezoek [Wat is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Veiligheidsmetingen

In deze tutorial evalueer je de veiligheid van het fine-tuned Phi-3 model met behulp van de veiligheidsmetingen van Azure AI Foundry. Deze metingen helpen je om het vermogen van het model om schadelijke inhoud te genereren en zijn kwetsbaarheid voor jailbreak-aanvallen te beoordelen. De veiligheidsmetingen omvatten:

- **Zelfbeschadigende inhoud**: Evalueert of het model de neiging heeft om inhoud te genereren die verband houdt met zelfbeschadiging.
- **Haatdragende en Oneerlijke Inhoud**: Evalueert of het model de neiging heeft om haatdragende of oneerlijke inhoud te genereren.
- **Gewelddadige Inhoud**: Evalueert of het model de neiging heeft om gewelddadige inhoud te genereren.
- **Seksuele Inhoud**: Evalueert of het model de neiging heeft om ongepaste seksuele inhoud te genereren.

Het evalueren van deze aspecten zorgt ervoor dat het AI-model geen schadelijke of aanstootgevende inhoud produceert, wat in lijn is met maatschappelijke waarden en wettelijke normen.

![Evalueren op basis van veiligheid.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.nl.png)

### Introductie tot prestatie-evaluatie

Om ervoor te zorgen dat je AI-model naar verwachting presteert, is het belangrijk om de prestaties ervan te evalueren aan de hand van prestatiestatistieken. In Azure AI Foundry maken prestatie-evaluaties het mogelijk om de effectiviteit van je model te beoordelen in het genereren van nauwkeurige, relevante en coherente reacties.

![Veiligheidsevaluatie.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.nl.png)

*Afbeeldingsbron: [Evaluatie van generatieve AI-toepassingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prestatiestatistieken

In deze tutorial evalueer je de prestaties van het fine-tuned Phi-3 / Phi-3.5 model met behulp van de prestatiestatistieken van Azure AI Foundry. Deze metingen helpen je om de effectiviteit van het model te beoordelen in het genereren van nauwkeurige, relevante en coherente reacties. De prestatiestatistieken omvatten:

- **Groundedness**: Evalueert hoe goed de gegenereerde antwoorden aansluiten bij de informatie uit de inputbron.
- **Relevantie**: Evalueert de relevantie van de gegenereerde reacties ten opzichte van de gestelde vragen.
- **Coherentie**: Evalueert hoe soepel de gegenereerde tekst leest, natuurlijk overkomt en mensachtige taal nabootst.
- **Vloeiendheid**: Evalueert de taalvaardigheid van de gegenereerde tekst.
- **GPT-gelijkenis**: Vergelijkt de gegenereerde reactie met de waarheid op gelijkenis.
- **F1 Score**: Berekent de verhouding van gedeelde woorden tussen de gegenereerde reactie en de brondata.

Deze metingen helpen je om de effectiviteit van het model te beoordelen in het genereren van nauwkeurige, relevante en coherente reacties.

![Evalueren op basis van prestaties.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.nl.png)

## **Scenario 2: Het evalueren van het Phi-3 / Phi-3.5 model in Azure AI Foundry**

### Voordat je begint

Deze tutorial is een vervolg op de eerdere blogposts, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In deze posts hebben we het proces doorlopen van het fine-tunen van een Phi-3 / Phi-3.5 model in Azure AI Foundry en het integreren ervan met Prompt flow.

In deze tutorial implementeer je een Azure OpenAI model als evaluator in Azure AI Foundry en gebruik je het om je fine-tuned Phi-3 / Phi-3.5 model te evalueren.

Voordat je aan deze tutorial begint, zorg ervoor dat je de volgende vereisten hebt, zoals beschreven in de eerdere tutorials:

1. Een voorbereid dataset om het fine-tuned Phi-3 / Phi-3.5 model te evalueren.
1. Een Phi-3 / Phi-3.5 model dat is fine-tuned en geïmplementeerd in Azure Machine Learning.
1. Een Prompt flow geïntegreerd met je fine-tuned Phi-3 / Phi-3.5 model in Azure AI Foundry.

> [!NOTE]
> Je gebruikt het *test_data.jsonl* bestand, dat zich bevindt in de datamap van de **ULTRACHAT_200k** dataset die in de vorige blogposts is gedownload, als dataset om het fine-tuned Phi-3 / Phi-3.5 model te evalueren.

#### Integreer het aangepaste Phi-3 / Phi-3.5 model met Prompt flow in Azure AI Foundry (Code-first aanpak)

> [!NOTE]
> Als je de low-code aanpak hebt gevolgd die wordt beschreven in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kun je deze oefening overslaan en doorgaan naar de volgende.
> Als je echter de code-first aanpak hebt gevolgd die wordt beschreven in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" om je Phi-3 / Phi-3.5 model te fine-tunen en implementeren, is het proces om je model te koppelen aan Prompt flow enigszins anders. Je leert dit proces in deze oefening.

Om verder te gaan, moet je je fine-tuned Phi-3 / Phi-3.5 model integreren in Prompt flow in Azure AI Foundry.

#### Maak Azure AI Foundry Hub

Je moet een Hub maken voordat je een Project aanmaakt. Een Hub fungeert als een Resource Group, waarmee je meerdere Projecten binnen Azure AI Foundry kunt organiseren en beheren.

1. Meld je aan bij [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecteer **Alle hubs** in het linker tabblad.

1. Selecteer **+ Nieuwe hub** in het navigatiemenu.

    ![Hub maken.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.nl.png)

1. Voer de volgende taken uit:

    - Voer **Hubnaam** in. Dit moet een unieke waarde zijn.
    - Selecteer je Azure **Abonnement**.
    - Selecteer de **Resourcegroep** die je wilt gebruiken (maak een nieuwe indien nodig).
    - Selecteer de **Locatie** die je wilt gebruiken.
    - Selecteer de **Verbind Azure AI Services** die je wilt gebruiken (maak een nieuwe indien nodig).
    - Selecteer **Verbind Azure AI Zoeken** om te **Overslaan met verbinden**.
![Vul hub in.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.nl.png)

1. Selecteer **Volgende**.

#### Maak een Azure AI Foundry-project aan

1. In de Hub die je hebt gemaakt, selecteer je **Alle projecten** in de linkerzijbalk.

1. Selecteer **+ Nieuw project** in het navigatiemenu.

    ![Selecteer nieuw project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.nl.png)

1. Voer **Projectnaam** in. Dit moet een unieke waarde zijn.

    ![Maak project aan.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.nl.png)

1. Selecteer **Maak een project**.

#### Voeg een aangepaste verbinding toe voor het fijn afgestemde Phi-3 / Phi-3.5-model

Om je aangepaste Phi-3 / Phi-3.5-model te integreren met Prompt flow, moet je de endpoint en sleutel van het model opslaan in een aangepaste verbinding. Deze configuratie zorgt ervoor dat je toegang hebt tot je aangepaste Phi-3 / Phi-3.5-model in Prompt flow.

#### Stel api-sleutel en endpoint-uri in van het fijn afgestemde Phi-3 / Phi-3.5-model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigeer naar de Azure Machine Learning-werkruimte die je hebt gemaakt.

1. Selecteer **Endpoints** in de linkerzijbalk.

    ![Selecteer endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.nl.png)

1. Selecteer de endpoint die je hebt gemaakt.

    ![Selecteer gemaakte endpoint.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.nl.png)

1. Selecteer **Verbruik** in het navigatiemenu.

1. Kopieer je **REST-endpoint** en **Primaire sleutel**.

    ![Kopieer api-sleutel en endpoint-uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.nl.png)

#### Voeg de aangepaste verbinding toe

1. Bezoek [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Azure AI Foundry-project dat je hebt gemaakt.

1. In het project dat je hebt gemaakt, selecteer je **Instellingen** in de linkerzijbalk.

1. Selecteer **+ Nieuwe verbinding**.

    ![Selecteer nieuwe verbinding.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.nl.png)

1. Selecteer **Aangepaste sleutels** in het navigatiemenu.

    ![Selecteer aangepaste sleutels.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.nl.png)

1. Voer de volgende taken uit:

    - Selecteer **+ Sleutel-waardeparen toevoegen**.
    - Voor de sleutelnaam voer je **endpoint** in en plak je de endpoint die je hebt gekopieerd uit Azure ML Studio in het waardeveld.
    - Selecteer **+ Sleutel-waardeparen toevoegen** opnieuw.
    - Voor de sleutelnaam voer je **sleutel** in en plak je de sleutel die je hebt gekopieerd uit Azure ML Studio in het waardeveld.
    - Nadat je de sleutels hebt toegevoegd, selecteer je **is geheim** om te voorkomen dat de sleutel zichtbaar wordt.

    ![Voeg verbinding toe.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.nl.png)

1. Selecteer **Voeg verbinding toe**.

#### Maak Prompt flow aan

Je hebt een aangepaste verbinding toegevoegd in Azure AI Foundry. Laten we nu een Prompt flow maken met de volgende stappen. Vervolgens koppel je deze Prompt flow aan de aangepaste verbinding om het fijn afgestemde model binnen de Prompt flow te gebruiken.

1. Navigeer naar het Azure AI Foundry-project dat je hebt gemaakt.

1. Selecteer **Prompt flow** in de linkerzijbalk.

1. Selecteer **+ Maken** in het navigatiemenu.

    ![Selecteer Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.nl.png)

1. Selecteer **Chat flow** in het navigatiemenu.

    ![Selecteer chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.nl.png)

1. Voer **Mapnaam** in die je wilt gebruiken.

    ![Selecteer chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.nl.png)

1. Selecteer **Maken**.

#### Stel Prompt flow in om te chatten met je aangepaste Phi-3 / Phi-3.5-model

Je moet het fijn afgestemde Phi-3 / Phi-3.5-model integreren in een Prompt flow. De bestaande Prompt flow is echter niet ontworpen voor dit doel. Daarom moet je de Prompt flow opnieuw ontwerpen om de integratie van het aangepaste model mogelijk te maken.

1. Voer in de Prompt flow de volgende taken uit om de bestaande flow opnieuw op te bouwen:

    - Selecteer **Raw file-modus**.
    - Verwijder alle bestaande code in het *flow.dag.yml*-bestand.
    - Voeg de volgende code toe aan *flow.dag.yml*.

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

    - Selecteer **Opslaan**.

    ![Selecteer raw file-modus.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.nl.png)

1. Voeg de volgende code toe aan *integrate_with_promptflow.py* om het aangepaste Phi-3 / Phi-3.5-model in Prompt flow te gebruiken.

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

    ![Plak prompt flow-code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.nl.png)

> [!NOTE]
> Voor meer gedetailleerde informatie over het gebruik van Prompt flow in Azure AI Foundry kun je [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) raadplegen.

1. Selecteer **Chat input**, **Chat output** om chatten met je model mogelijk te maken.

    ![Selecteer Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.nl.png)

1. Je bent nu klaar om te chatten met je aangepaste Phi-3 / Phi-3.5-model. In de volgende oefening leer je hoe je Prompt flow start en gebruikt om te chatten met je fijn afgestemde Phi-3 / Phi-3.5-model.

> [!NOTE]
>
> De opnieuw opgebouwde flow zou eruit moeten zien zoals in de onderstaande afbeelding:
>
> ![Flow voorbeeld](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.nl.png)
>

#### Start Prompt flow

1. Selecteer **Start compute-sessies** om Prompt flow te starten.

    ![Start compute-sessie.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.nl.png)

1. Selecteer **Valideer en parse invoer** om parameters te vernieuwen.

    ![Valideer invoer.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.nl.png)

1. Selecteer de **Waarde** van de **verbinding** naar de aangepaste verbinding die je hebt gemaakt. Bijvoorbeeld *verbinding*.

    ![Verbinding.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.nl.png)

#### Chat met je aangepaste Phi-3 / Phi-3.5-model

1. Selecteer **Chat**.

    ![Selecteer chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.nl.png)

1. Hier is een voorbeeld van de resultaten: Je kunt nu chatten met je aangepaste Phi-3 / Phi-3.5-model. Het wordt aanbevolen om vragen te stellen op basis van de gegevens die zijn gebruikt voor het fijn afstemmen.

    ![Chat met prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.nl.png)

### Azure OpenAI implementeren om het Phi-3 / Phi-3.5-model te evalueren

Om het Phi-3 / Phi-3.5-model te evalueren in Azure AI Foundry, moet je een Azure OpenAI-model implementeren. Dit model wordt gebruikt om de prestaties van het Phi-3 / Phi-3.5-model te evalueren.

#### Azure OpenAI implementeren

1. Meld je aan bij [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Azure AI Foundry-project dat je hebt gemaakt.

    ![Selecteer Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.nl.png)

1. In het project dat je hebt gemaakt, selecteer je **Implementaties** in de linkerzijbalk.

1. Selecteer **+ Model implementeren** in het navigatiemenu.

1. Selecteer **Basis model implementeren**.

    ![Selecteer Implementaties.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.nl.png)

1. Selecteer het Azure OpenAI-model dat je wilt gebruiken. Bijvoorbeeld **gpt-4o**.

    ![Selecteer Azure OpenAI-model dat je wilt gebruiken.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.nl.png)

1. Selecteer **Bevestigen**.

### Evalueer het fijn afgestemde Phi-3 / Phi-3.5-model met behulp van Azure AI Foundry's Prompt flow-evaluatie

### Start een nieuwe evaluatie

1. Bezoek [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Azure AI Foundry-project dat je hebt gemaakt.

    ![Selecteer Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.nl.png)

1. In het project dat je hebt gemaakt, selecteer je **Evaluatie** in de linkerzijbalk.

1. Selecteer **+ Nieuwe evaluatie** in het navigatiemenu.
![Select evaluatie.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.nl.png)

1. Selecteer **Prompt flow** evaluatie.

    ![Selecteer Prompt flow evaluatie.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.nl.png)

1. Voer de volgende taken uit:

    - Voer de evaluatienaam in. Dit moet een unieke waarde zijn.
    - Selecteer **Vraag en antwoord zonder context** als het taaktype. Dit komt omdat de **UlTRACHAT_200k** dataset die in deze tutorial wordt gebruikt geen context bevat.
    - Selecteer de prompt flow die je wilt evalueren.

    ![Prompt flow evaluatie.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.nl.png)

1. Selecteer **Volgende**.

1. Voer de volgende taken uit:

    - Selecteer **Voeg je dataset toe** om de dataset te uploaden. Je kunt bijvoorbeeld het testdatasetbestand uploaden, zoals *test_data.json1*, dat wordt meegeleverd bij het downloaden van de **ULTRACHAT_200k** dataset.
    - Selecteer de juiste **Datasetkolom** die overeenkomt met je dataset. Als je bijvoorbeeld de **ULTRACHAT_200k** dataset gebruikt, selecteer dan **${data.prompt}** als datasetkolom.

    ![Prompt flow evaluatie.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.nl.png)

1. Selecteer **Volgende**.

1. Voer de volgende taken uit om de prestatie- en kwaliteitsstatistieken te configureren:

    - Selecteer de prestatie- en kwaliteitsstatistieken die je wilt gebruiken.
    - Selecteer het Azure OpenAI-model dat je hebt gemaakt voor evaluatie. Selecteer bijvoorbeeld **gpt-4o**.

    ![Prompt flow evaluatie.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.nl.png)

1. Voer de volgende taken uit om de risico- en veiligheidsstatistieken te configureren:

    - Selecteer de risico- en veiligheidsstatistieken die je wilt gebruiken.
    - Selecteer de drempelwaarde om het defectpercentage te berekenen dat je wilt gebruiken. Selecteer bijvoorbeeld **Gemiddeld**.
    - Voor **vraag**, selecteer **Gegevensbron** naar **{$data.prompt}**.
    - Voor **antwoord**, selecteer **Gegevensbron** naar **{$run.outputs.answer}**.
    - Voor **ground_truth**, selecteer **Gegevensbron** naar **{$data.message}**.

    ![Prompt flow evaluatie.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.nl.png)

1. Selecteer **Volgende**.

1. Selecteer **Verzenden** om de evaluatie te starten.

1. De evaluatie zal enige tijd duren om te voltooien. Je kunt de voortgang volgen in het tabblad **Evaluatie**.

### Resultaten van de evaluatie bekijken

> [!NOTE]
> De onderstaande resultaten zijn bedoeld om het evaluatieproces te illustreren. In deze tutorial hebben we een model gebruikt dat is getraind op een relatief kleine dataset, wat kan leiden tot suboptimale resultaten. De werkelijke resultaten kunnen aanzienlijk variëren, afhankelijk van de grootte, kwaliteit en diversiteit van de gebruikte dataset, evenals de specifieke configuratie van het model.

Zodra de evaluatie is voltooid, kun je de resultaten bekijken voor zowel prestatie- als veiligheidsstatistieken.

1. Prestatie- en kwaliteitsstatistieken:

    - Beoordeel de effectiviteit van het model bij het genereren van coherente, vloeiende en relevante antwoorden.

    ![Evaluatieresultaat.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.nl.png)

1. Risico- en veiligheidsstatistieken:

    - Zorg ervoor dat de outputs van het model veilig zijn en in lijn met de Principes van Verantwoordelijke AI, waarbij schadelijke of beledigende inhoud wordt vermeden.

    ![Evaluatieresultaat.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.nl.png)

1. Je kunt naar beneden scrollen om **Gedetailleerde statistiekenresultaten** te bekijken.

    ![Evaluatieresultaat.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.nl.png)

1. Door je aangepaste Phi-3 / Phi-3.5 model te evalueren op zowel prestatie- als veiligheidsstatistieken, kun je bevestigen dat het model niet alleen effectief is, maar ook voldoet aan de principes van Verantwoordelijke AI, waardoor het klaar is voor implementatie in de praktijk.

## Gefeliciteerd!

### Je hebt deze tutorial voltooid

Je hebt met succes het getrainde Phi-3 model geëvalueerd dat is geïntegreerd met Prompt flow in Azure AI Foundry. Dit is een belangrijke stap om ervoor te zorgen dat je AI-modellen niet alleen goed presteren, maar ook voldoen aan de principes van Verantwoordelijke AI van Microsoft, zodat je betrouwbare en vertrouwde AI-toepassingen kunt bouwen.

![Architectuur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.nl.png)

## Azure-resources opruimen

Ruim je Azure-resources op om extra kosten voor je account te voorkomen. Ga naar de Azure-portal en verwijder de volgende resources:

- De Azure Machine Learning-resource.
- Het Azure Machine Learning-modelendpoint.
- De Azure AI Foundry Project-resource.
- De Azure AI Foundry Prompt flow-resource.

### Volgende stappen

#### Documentatie

- [AI-systemen beoordelen met het Responsible AI-dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluatie- en monitoringstatistieken voor generatieve AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry-documentatie](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-documentatie](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Trainingsmateriaal

- [Inleiding tot Microsofts Responsible AI-aanpak](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Inleiding tot Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referentie

- [Wat is Verantwoordelijke AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Nieuwe tools in Azure AI om veiligere en betrouwbaardere generatieve AI-toepassingen te bouwen](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluatie van generatieve AI-toepassingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Disclaimer**:  
Dit document is vertaald met behulp van machinegebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.