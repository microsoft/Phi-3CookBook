# Evaluér den Finjusterede Phi-3 / Phi-3.5 Model i Azure AI Foundry med Fokus på Microsofts Principper for Ansvarlig AI

Denne end-to-end (E2E) vejledning er baseret på guiden "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community.

## Oversigt

### Hvordan kan du evaluere sikkerheden og ydeevnen af en finjusteret Phi-3 / Phi-3.5 model i Azure AI Foundry?

Finjustering af en model kan til tider føre til utilsigtede eller uønskede svar. For at sikre, at modellen forbliver sikker og effektiv, er det vigtigt at evaluere modellens potentiale til at generere skadelig indhold og dens evne til at producere nøjagtige, relevante og sammenhængende svar. I denne vejledning lærer du, hvordan du evaluerer sikkerheden og ydeevnen af en finjusteret Phi-3 / Phi-3.5 model integreret med Prompt flow i Azure AI Foundry.

Her er en oversigt over Azure AI Foundry's evalueringsproces.

![Arkitektur for vejledning.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.da.png)

*Billedkilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For mere detaljeret information og yderligere ressourcer om Phi-3 / Phi-3.5, besøg venligst [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Forudsætninger

- [Python](https://www.python.org/downloads)
- [Azure abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finjusteret Phi-3 / Phi-3.5 model

### Indholdsfortegnelse

1. [**Scenario 1: Introduktion til Azure AI Foundry's Prompt flow evaluering**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduktion til sikkerhedsevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduktion til ydeevneevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluering af Phi-3 / Phi-3.5 modellen i Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Før du begynder](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Udrul Azure OpenAI for at evaluere Phi-3 / Phi-3.5 modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluer den finjusterede Phi-3 / Phi-3.5 model ved hjælp af Azure AI Foundry's Prompt flow evaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Tillykke!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduktion til Azure AI Foundry's Prompt flow evaluering**

### Introduktion til sikkerhedsevaluering

For at sikre, at din AI-model er etisk og sikker, er det afgørende at evaluere den i forhold til Microsofts Principper for Ansvarlig AI. I Azure AI Foundry gør sikkerhedsevalueringer det muligt at vurdere modellens sårbarhed over for jailbreak-angreb og dens potentiale til at generere skadeligt indhold, hvilket er direkte i overensstemmelse med disse principper.

![Sikkerhedsevaluering.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.da.png)

*Billedkilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts Principper for Ansvarlig AI

Før du starter de tekniske trin, er det vigtigt at forstå Microsofts Principper for Ansvarlig AI, en etisk ramme designet til at vejlede den ansvarlige udvikling, udrulning og drift af AI-systemer. Disse principper sikrer, at AI-teknologier bygges på en måde, der er retfærdig, gennemsigtig og inkluderende. Principperne danner grundlaget for evaluering af AI-modellers sikkerhed.

Microsofts Principper for Ansvarlig AI inkluderer:

- **Retfærdighed og Inklusion**: AI-systemer bør behandle alle retfærdigt og undgå at påvirke lignende grupper af mennesker på forskellige måder. For eksempel, når AI-systemer giver vejledning om medicinsk behandling, lån eller ansættelse, bør de give samme anbefalinger til alle med lignende symptomer, økonomiske forhold eller faglige kvalifikationer.

- **Pålidelighed og Sikkerhed**: For at opbygge tillid er det afgørende, at AI-systemer fungerer pålideligt, sikkert og konsekvent. Disse systemer bør kunne fungere som oprindeligt designet, reagere sikkert på uforudsete forhold og modstå skadelig manipulation. Deres adfærd og evne til at håndtere forskellige forhold afspejler de situationer og omstændigheder, udviklerne forudså under design og test.

- **Gennemsigtighed**: Når AI-systemer hjælper med at træffe beslutninger, der har stor indflydelse på folks liv, er det afgørende, at folk forstår, hvordan disse beslutninger blev truffet. For eksempel kan en bank bruge et AI-system til at beslutte, om en person er kreditværdig. En virksomhed kan bruge et AI-system til at finde de mest kvalificerede kandidater til ansættelse.

- **Privatliv og Sikkerhed**: Efterhånden som AI bliver mere udbredt, bliver det stadig vigtigere og mere komplekst at beskytte privatliv og sikre personlige og forretningsmæssige oplysninger. Med AI kræver privatliv og datasikkerhed tæt opmærksomhed, da adgang til data er afgørende for, at AI-systemer kan lave præcise og informerede forudsigelser og beslutninger om mennesker.

- **Ansvarlighed**: Personerne, der designer og udruller AI-systemer, skal være ansvarlige for, hvordan deres systemer fungerer. Organisationer bør trække på industristandarder for at udvikle normer for ansvarlighed. Disse normer kan sikre, at AI-systemer ikke er den endelige myndighed i beslutninger, der påvirker menneskers liv. De kan også sikre, at mennesker bevarer meningsfuld kontrol over ellers meget autonome AI-systemer.

![Ansvarlig AI hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.da.png)

*Billedkilde: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> For at lære mere om Microsofts Principper for Ansvarlig AI, besøg [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sikkerhedsmetrikker

I denne vejledning vil du evaluere sikkerheden af den finjusterede Phi-3 model ved hjælp af Azure AI Foundry's sikkerhedsmetrikker. Disse metrikker hjælper dig med at vurdere modellens potentiale til at generere skadeligt indhold og dens sårbarhed over for jailbreak-angreb. Sikkerhedsmetrikkerne inkluderer:

- **Indhold relateret til selvskade**: Evaluerer, om modellen har en tendens til at producere indhold relateret til selvskade.
- **Hadefuldt og Uretfærdigt Indhold**: Evaluerer, om modellen har en tendens til at producere hadefuldt eller uretfærdigt indhold.
- **Voldeligt Indhold**: Evaluerer, om modellen har en tendens til at producere voldeligt indhold.
- **Seksuelt Indhold**: Evaluerer, om modellen har en tendens til at producere upassende seksuelt indhold.

Ved at evaluere disse aspekter sikrer du, at AI-modellen ikke producerer skadeligt eller stødende indhold, hvilket stemmer overens med samfundsværdier og lovgivningsmæssige standarder.

![Evaluér baseret på sikkerhed.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.da.png)

### Introduktion til ydeevneevaluering

For at sikre, at din AI-model fungerer som forventet, er det vigtigt at evaluere dens ydeevne i forhold til ydeevnemetrikker. I Azure AI Foundry gør ydeevneevalueringer det muligt at vurdere modellens effektivitet i at generere nøjagtige, relevante og sammenhængende svar.

![Sikkerhedsevaluering.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.da.png)

*Billedkilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Ydeevnemetrikker

I denne vejledning vil du evaluere ydeevnen af den finjusterede Phi-3 / Phi-3.5 model ved hjælp af Azure AI Foundry's ydeevnemetrikker. Disse metrikker hjælper dig med at vurdere modellens effektivitet i at generere nøjagtige, relevante og sammenhængende svar. Ydeevnemetrikkerne inkluderer:

- **Groundedness**: Evaluerer, hvor godt de genererede svar stemmer overens med informationen fra inputkilden.
- **Relevans**: Evaluerer, hvor relevante de genererede svar er i forhold til de stillede spørgsmål.
- **Sammenhæng**: Evaluerer, hvor naturligt og flydende den genererede tekst læses, og om den minder om menneskelig sprogbrug.
- **Fluency**: Evaluerer sprogfærdigheden i den genererede tekst.
- **GPT Similarity**: Sammenligner det genererede svar med det korrekte svar for lighed.
- **F1 Score**: Beregner forholdet mellem fælles ord i det genererede svar og kildedataene.

Disse metrikker hjælper dig med at evaluere modellens effektivitet i at generere nøjagtige, relevante og sammenhængende svar.

![Evaluér baseret på ydeevne.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.da.png)

## **Scenario 2: Evaluering af Phi-3 / Phi-3.5 modellen i Azure AI Foundry**

### Før du begynder

Denne vejledning er en opfølgning på de tidligere blogindlæg, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" og "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I disse indlæg gennemgik vi processen med at finjustere en Phi-3 / Phi-3.5 model i Azure AI Foundry og integrere den med Prompt flow.

I denne vejledning vil du udrulle en Azure OpenAI model som evaluator i Azure AI Foundry og bruge den til at evaluere din finjusterede Phi-3 / Phi-3.5 model.

Før du begynder denne vejledning, skal du sikre dig, at du har følgende forudsætninger, som beskrevet i de tidligere vejledninger:

1. Et forberedt datasæt til evaluering af den finjusterede Phi-3 / Phi-3.5 model.
1. En Phi-3 / Phi-3.5 model, der er finjusteret og udrullet til Azure Machine Learning.
1. En Prompt flow integreret med din finjusterede Phi-3 / Phi-3.5 model i Azure AI Foundry.

> [!NOTE]
> Du vil bruge filen *test_data.jsonl*, som findes i data-mappen fra **ULTRACHAT_200k** datasættet downloadet i de tidligere blogindlæg, som datasæt til at evaluere den finjusterede Phi-3 / Phi-3.5 model.

#### Integrer den brugerdefinerede Phi-3 / Phi-3.5 model med Prompt flow i Azure AI Foundry (Kode-først tilgang)

> [!NOTE]
> Hvis du fulgte den low-code tilgang, der blev beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kan du springe denne øvelse over og gå videre til den næste.
> Men hvis du fulgte kode-først tilgangen, der blev beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" for at finjustere og udrulle din Phi-3 / Phi-3.5 model, er processen med at forbinde din model til Prompt flow lidt anderledes. Du vil lære denne proces i denne øvelse.

For at fortsætte skal du integrere din finjusterede Phi-3 / Phi-3.5 model i Prompt flow i Azure AI Foundry.

#### Opret Azure AI Foundry Hub

Du skal oprette en Hub, før du opretter Projektet. En Hub fungerer som en Ressourcegruppe og giver dig mulighed for at organisere og administrere flere Projekter inden for Azure AI Foundry.

1. Log ind på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Vælg **Alle hubs** i venstre fane.

1. Vælg **+ Ny hub** fra navigationsmenuen.

    ![Opret hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.da.png)

1. Udfør følgende opgaver:

    - Indtast **Hub-navn**. Det skal være en unik værdi.
    - Vælg dit Azure **Abonnement**.
    - Vælg den **Ressourcegruppe**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg den **Placering**, du ønsker at bruge.
    - Vælg **Forbind Azure AI Services**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg **Forbind Azure AI Search** til **Spring over forbindelse**.
![Fyld hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.da.png)

1. Vælg **Næste**.

#### Opret Azure AI Foundry-projekt

1. I den hub, du oprettede, vælg **Alle projekter** fra fanen i venstre side.

1. Vælg **+ Nyt projekt** fra navigationsmenuen.

    ![Vælg nyt projekt.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.da.png)

1. Indtast **Projektnavn**. Det skal være en unik værdi.

    ![Opret projekt.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.da.png)

1. Vælg **Opret et projekt**.

#### Tilføj en brugerdefineret forbindelse til den finjusterede Phi-3 / Phi-3.5-model

For at integrere din brugerdefinerede Phi-3 / Phi-3.5-model med Prompt flow skal du gemme modellens endpoint og nøgle i en brugerdefineret forbindelse. Denne opsætning sikrer adgang til din brugerdefinerede Phi-3 / Phi-3.5-model i Prompt flow.

#### Indstil API-nøgle og endpoint-URI for den finjusterede Phi-3 / Phi-3.5-model

1. Besøg [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviger til det Azure Machine Learning-arbejdsområde, du oprettede.

1. Vælg **Endpoints** fra fanen i venstre side.

    ![Vælg endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.da.png)

1. Vælg det endpoint, du oprettede.

    ![Vælg oprettet endpoint.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.da.png)

1. Vælg **Forbrug** fra navigationsmenuen.

1. Kopiér din **REST endpoint** og **Primær nøgle**.

    ![Kopiér API-nøgle og endpoint-URI.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.da.png)

#### Tilføj den brugerdefinerede forbindelse

1. Besøg [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til det Azure AI Foundry-projekt, du oprettede.

1. I det projekt, du oprettede, vælg **Indstillinger** fra fanen i venstre side.

1. Vælg **+ Ny forbindelse**.

    ![Vælg ny forbindelse.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.da.png)

1. Vælg **Brugerdefinerede nøgler** fra navigationsmenuen.

    ![Vælg brugerdefinerede nøgler.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.da.png)

1. Udfør følgende opgaver:

    - Vælg **+ Tilføj nøgle-værdi-par**.
    - For nøgle-navn, indtast **endpoint** og indsæt det endpoint, du kopierede fra Azure ML Studio, i værdifeltet.
    - Vælg **+ Tilføj nøgle-værdi-par** igen.
    - For nøgle-navn, indtast **key** og indsæt den nøgle, du kopierede fra Azure ML Studio, i værdifeltet.
    - Efter tilføjelse af nøglerne, vælg **er hemmelig** for at forhindre, at nøglen bliver synlig.

    ![Tilføj forbindelse.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.da.png)

1. Vælg **Tilføj forbindelse**.

#### Opret Prompt flow

Du har tilføjet en brugerdefineret forbindelse i Azure AI Foundry. Nu skal vi oprette et Prompt flow ved hjælp af følgende trin. Derefter vil du forbinde dette Prompt flow til den brugerdefinerede forbindelse for at bruge den finjusterede model i Prompt flow.

1. Naviger til det Azure AI Foundry-projekt, du oprettede.

1. Vælg **Prompt flow** fra fanen i venstre side.

1. Vælg **+ Opret** fra navigationsmenuen.

    ![Vælg Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.da.png)

1. Vælg **Chat flow** fra navigationsmenuen.

    ![Vælg chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.da.png)

1. Indtast **Mappenavn**, der skal bruges.

    ![Vælg chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.da.png)

1. Vælg **Opret**.

#### Opsæt Prompt flow til at chatte med din brugerdefinerede Phi-3 / Phi-3.5-model

Du skal integrere den finjusterede Phi-3 / Phi-3.5-model i et Prompt flow. Dog er det eksisterende Prompt flow ikke designet til dette formål. Derfor skal du redesigne Prompt flow for at muliggøre integration af den brugerdefinerede model.

1. I Prompt flow, udfør følgende opgaver for at genopbygge den eksisterende flow:

    - Vælg **Rå filtilstand**.
    - Slet al eksisterende kode i *flow.dag.yml*-filen.
    - Tilføj følgende kode til *flow.dag.yml*.

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

    - Vælg **Gem**.

    ![Vælg rå filtilstand.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.da.png)

1. Tilføj følgende kode til *integrate_with_promptflow.py* for at bruge den brugerdefinerede Phi-3 / Phi-3.5-model i Prompt flow.

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

    ![Indsæt Prompt flow-kode.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.da.png)

> [!NOTE]
> For mere detaljeret information om brug af Prompt flow i Azure AI Foundry, kan du se [Prompt flow i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vælg **Chat input**, **Chat output** for at aktivere chat med din model.

    ![Vælg Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.da.png)

1. Nu er du klar til at chatte med din brugerdefinerede Phi-3 / Phi-3.5-model. I den næste øvelse lærer du, hvordan du starter Prompt flow og bruger det til at chatte med din finjusterede Phi-3 / Phi-3.5-model.

> [!NOTE]
>
> Det genopbyggede flow skal se ud som billedet nedenfor:
>
> ![Flow eksempel](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.da.png)
>

#### Start Prompt flow

1. Vælg **Start beregningssessioner** for at starte Prompt flow.

    ![Start beregningssession.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.da.png)

1. Vælg **Validér og parse input** for at opdatere parametre.

    ![Validér input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.da.png)

1. Vælg værdien af **connection** til den brugerdefinerede forbindelse, du oprettede. For eksempel *connection*.

    ![Forbindelse.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.da.png)

#### Chat med din brugerdefinerede Phi-3 / Phi-3.5-model

1. Vælg **Chat**.

    ![Vælg chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.da.png)

1. Her er et eksempel på resultaterne: Nu kan du chatte med din brugerdefinerede Phi-3 / Phi-3.5-model. Det anbefales at stille spørgsmål baseret på de data, der blev brugt til finjustering.

    ![Chat med Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.da.png)

### Udrul Azure OpenAI for at evaluere Phi-3 / Phi-3.5-modellen

For at evaluere Phi-3 / Phi-3.5-modellen i Azure AI Foundry skal du udrulle en Azure OpenAI-model. Denne model vil blive brugt til at evaluere ydeevnen af Phi-3 / Phi-3.5-modellen.

#### Udrul Azure OpenAI

1. Log ind på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til det Azure AI Foundry-projekt, du oprettede.

    ![Vælg projekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.da.png)

1. I det projekt, du oprettede, vælg **Udrulninger** fra fanen i venstre side.

1. Vælg **+ Udrul model** fra navigationsmenuen.

1. Vælg **Udrul basismodel**.

    ![Vælg udrulninger.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.da.png)

1. Vælg den Azure OpenAI-model, du ønsker at bruge. For eksempel **gpt-4o**.

    ![Vælg Azure OpenAI-model, du ønsker at bruge.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.da.png)

1. Vælg **Bekræft**.

### Evaluer den finjusterede Phi-3 / Phi-3.5-model ved hjælp af Azure AI Foundrys Prompt flow-evaluering

### Start en ny evaluering

1. Besøg [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til det Azure AI Foundry-projekt, du oprettede.

    ![Vælg projekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.da.png)

1. I det projekt, du oprettede, vælg **Evaluering** fra fanen i venstre side.

1. Vælg **+ Ny evaluering** fra navigationsmenuen.
![Vælg evaluering.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.da.png)

1. Vælg **Prompt flow** evaluering.

   ![Vælg Prompt flow evaluering.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.da.png)

1. Udfør følgende opgaver:

   - Indtast evalueringsnavnet. Det skal være en unik værdi.
   - Vælg **Spørgsmål og svar uden kontekst** som opgavetypen. Dette skyldes, at **ULTRACHAT_200k** datasættet, der bruges i denne vejledning, ikke indeholder kontekst.
   - Vælg den prompt flow, du ønsker at evaluere.

   ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.da.png)

1. Vælg **Næste**.

1. Udfør følgende opgaver:

   - Vælg **Tilføj dit datasæt** for at uploade datasættet. For eksempel kan du uploade testdatasættet, som *test_data.json1*, der følger med, når du downloader **ULTRACHAT_200k** datasættet.
   - Vælg den relevante **Datasætkolonne**, der matcher dit datasæt. For eksempel, hvis du bruger **ULTRACHAT_200k** datasættet, vælg **${data.prompt}** som datasætkolonne.

   ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.da.png)

1. Vælg **Næste**.

1. Udfør følgende opgaver for at konfigurere præstations- og kvalitetsmålinger:

   - Vælg de præstations- og kvalitetsmålinger, du ønsker at bruge.
   - Vælg den Azure OpenAI-model, du har oprettet til evaluering. For eksempel, vælg **gpt-4o**.

   ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.da.png)

1. Udfør følgende opgaver for at konfigurere risiko- og sikkerhedsmålinger:

   - Vælg de risiko- og sikkerhedsmålinger, du ønsker at bruge.
   - Vælg tærsklen for at beregne den defektrate, du ønsker at bruge. For eksempel, vælg **Medium**.
   - For **spørgsmål**, vælg **Datakilde** til **{$data.prompt}**.
   - For **svar**, vælg **Datakilde** til **{$run.outputs.answer}**.
   - For **ground_truth**, vælg **Datakilde** til **{$data.message}**.

   ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.da.png)

1. Vælg **Næste**.

1. Vælg **Indsend** for at starte evalueringen.

1. Evalueringen vil tage noget tid at fuldføre. Du kan overvåge fremskridtet i **Evaluering** fanen.

### Gennemgå evalueringsresultaterne

> [!NOTE]
> Resultaterne præsenteret nedenfor er kun til illustration af evalueringsprocessen. I denne vejledning har vi brugt en model, der er finjusteret på et relativt lille datasæt, hvilket kan føre til suboptimale resultater. Faktiske resultater kan variere betydeligt afhængigt af datasættets størrelse, kvalitet og diversitet samt den specifikke konfiguration af modellen.

Når evalueringen er fuldført, kan du gennemgå resultaterne for både præstations- og sikkerhedsmålinger.

1. Præstations- og kvalitetsmålinger:

   - Evaluer modellens effektivitet i at generere sammenhængende, flydende og relevante svar.

   ![Evalueringsresultat.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.da.png)

1. Risiko- og sikkerhedsmålinger:

   - Sikr, at modellens output er sikre og i overensstemmelse med principperne for ansvarlig AI, og undgå skadeligt eller stødende indhold.

   ![Evalueringsresultat.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.da.png)

1. Du kan rulle ned for at se **Detaljerede måleresultater**.

   ![Evalueringsresultat.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.da.png)

1. Ved at evaluere din tilpassede Phi-3 / Phi-3.5 model mod både præstations- og sikkerhedsmålinger kan du bekræfte, at modellen ikke kun er effektiv, men også overholder ansvarlige AI-principper, hvilket gør den klar til implementering i virkelige scenarier.

## Tillykke!

### Du har gennemført denne vejledning

Du har med succes evalueret den finjusterede Phi-3 model integreret med Prompt flow i Azure AI Foundry. Dette er et vigtigt skridt for at sikre, at dine AI-modeller ikke kun præsterer godt, men også overholder Microsofts principper for ansvarlig AI, hvilket hjælper dig med at bygge pålidelige og troværdige AI-applikationer.

![Arkitektur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.da.png)

## Ryd op i Azure-ressourcer

Ryd op i dine Azure-ressourcer for at undgå ekstra omkostninger på din konto. Gå til Azure-portalen og slet følgende ressourcer:

- Azure Machine learning ressource.
- Azure Machine learning model endpoint.
- Azure AI Foundry Project ressource.
- Azure AI Foundry Prompt flow ressource.

### Næste trin

#### Dokumentation

- [Vurder AI-systemer ved hjælp af Responsible AI-dashboardet](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluering og overvågningsmålinger for generativ AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry dokumentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow dokumentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Træningsindhold

- [Introduktion til Microsofts tilgang til ansvarlig AI](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduktion til Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [Hvad er ansvarlig AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Nye værktøjer i Azure AI til at bygge mere sikre og troværdige generative AI-applikationer](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluering af generative AI-applikationer](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.