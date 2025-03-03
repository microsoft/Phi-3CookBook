# Evaluering av finjustert Phi-3 / Phi-3.5-modell i Azure AI Foundry med fokus på Microsofts prinsipper for ansvarlig AI

Denne ende-til-ende (E2E) veiledningen er basert på artikkelen "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community.

## Oversikt

### Hvordan kan du evaluere sikkerheten og ytelsen til en finjustert Phi-3 / Phi-3.5-modell i Azure AI Foundry?

Finjustering av en modell kan noen ganger føre til utilsiktede eller uønskede responser. For å sikre at modellen forblir trygg og effektiv, er det viktig å evaluere modellens potensial til å generere skadelig innhold og dens evne til å produsere nøyaktige, relevante og sammenhengende svar. I denne veiledningen vil du lære hvordan du evaluerer sikkerheten og ytelsen til en finjustert Phi-3 / Phi-3.5-modell integrert med Prompt flow i Azure AI Foundry.

Her er evalueringsprosessen i Azure AI Foundry.

![Arkitektur for veiledning.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.no.png)

*Bildekilde: [Evaluering av generative AI-applikasjoner](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For mer detaljert informasjon og for å utforske ytterligere ressurser om Phi-3 / Phi-3.5, vennligst besøk [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Forutsetninger

- [Python](https://www.python.org/downloads)
- [Azure-abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finjustert Phi-3 / Phi-3.5-modell

### Innholdsfortegnelse

1. [**Scenario 1: Introduksjon til Azure AI Foundrys Prompt flow-evaluering**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduksjon til sikkerhetsevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduksjon til ytelsesevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluering av Phi-3 / Phi-3.5-modellen i Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Før du begynner](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuer Azure OpenAI for å evaluere Phi-3 / Phi-3.5-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluer den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av Azure AI Foundrys Prompt flow-evaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gratulerer!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduksjon til Azure AI Foundrys Prompt flow-evaluering**

### Introduksjon til sikkerhetsevaluering

For å sikre at AI-modellen din er etisk og trygg, er det avgjørende å evaluere den mot Microsofts prinsipper for ansvarlig AI. I Azure AI Foundry lar sikkerhetsevalueringer deg vurdere modellens sårbarhet for jailbreak-angrep og dens potensial til å generere skadelig innhold, noe som er i tråd med disse prinsippene.

![Sikkerhetsevaluering.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.no.png)

*Bildekilde: [Evaluering av generative AI-applikasjoner](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts prinsipper for ansvarlig AI

Før du starter de tekniske stegene, er det viktig å forstå Microsofts prinsipper for ansvarlig AI, et etisk rammeverk designet for å veilede ansvarlig utvikling, distribusjon og drift av AI-systemer. Disse prinsippene sikrer at AI-teknologier utvikles på en måte som er rettferdig, transparent og inkluderende. De er grunnlaget for evalueringen av AI-modellenes sikkerhet.

Microsofts prinsipper for ansvarlig AI inkluderer:

- **Rettferdighet og inkludering**: AI-systemer bør behandle alle rettferdig og unngå å påvirke lignende grupper av mennesker på forskjellige måter. For eksempel, når AI-systemer gir veiledning om medisinsk behandling, lånesøknader eller ansettelse, bør de gi samme anbefalinger til alle med lignende symptomer, økonomiske forhold eller faglige kvalifikasjoner.

- **Pålitelighet og sikkerhet**: For å bygge tillit er det kritisk at AI-systemer fungerer pålitelig, trygt og konsistent. Disse systemene bør fungere som de opprinnelig ble designet, reagere trygt på uforutsette situasjoner og motstå skadelig manipulering.

- **Åpenhet**: Når AI-systemer hjelper til med å informere beslutninger som har stor innvirkning på folks liv, er det avgjørende at folk forstår hvordan disse beslutningene ble tatt. For eksempel kan en bank bruke et AI-system for å avgjøre om en person er kredittverdig.

- **Personvern og sikkerhet**: Etter hvert som AI blir mer utbredt, blir det stadig viktigere og mer komplekst å beskytte personvern og sikre personlig og forretningsmessig informasjon.

- **Ansvarlighet**: Personene som designer og distribuerer AI-systemer må være ansvarlige for hvordan systemene fungerer. Organisasjoner bør følge industristandarder for å utvikle normer for ansvarlighet.

![Fyll hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.no.png)

*Bildekilde: [Hva er ansvarlig AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> For å lære mer om Microsofts prinsipper for ansvarlig AI, besøk [Hva er ansvarlig AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sikkerhetsmålinger

I denne veiledningen vil du evaluere sikkerheten til den finjusterte Phi-3-modellen ved hjelp av sikkerhetsmålinger i Azure AI Foundry. Disse målingene hjelper deg med å vurdere modellens potensial til å generere skadelig innhold og dens sårbarhet for jailbreak-angrep. Sikkerhetsmålingene inkluderer:

- **Innhold relatert til selvskading**: Evaluerer om modellen har en tendens til å produsere innhold relatert til selvskading.
- **Hatefult og urettferdig innhold**: Evaluerer om modellen har en tendens til å produsere hatefullt eller urettferdig innhold.
- **Voldelig innhold**: Evaluerer om modellen har en tendens til å produsere voldelig innhold.
- **Seksuelt innhold**: Evaluerer om modellen har en tendens til å produsere upassende seksuelt innhold.

Ved å evaluere disse aspektene sikrer du at AI-modellen ikke produserer skadelig eller støtende innhold, i tråd med samfunnsverdier og regulatoriske standarder.

![Evaluer basert på sikkerhet.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.no.png)

### Introduksjon til ytelsesevaluering

For å sikre at AI-modellen din fungerer som forventet, er det viktig å evaluere ytelsen mot ytelsesmålinger. I Azure AI Foundry lar ytelsesevalueringer deg vurdere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar.

![Sikkerhetsevaluering.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.no.png)

*Bildekilde: [Evaluering av generative AI-applikasjoner](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Ytelsesmålinger

I denne veiledningen vil du evaluere ytelsen til den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av ytelsesmålinger i Azure AI Foundry. Disse målingene hjelper deg med å vurdere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar. Ytelsesmålingene inkluderer:

- **Grunnlag**: Evaluer hvor godt de genererte svarene samsvarer med informasjonen fra inngangskilden.
- **Relevans**: Evaluer hvor relevante de genererte svarene er for de gitte spørsmålene.
- **Sammenheng**: Evaluer hvor jevnt teksten flyter, leser naturlig og ligner menneskelig språk.
- **Flyt**: Evaluer språkferdigheten til den genererte teksten.
- **GPT-likhet**: Sammenligner det genererte svaret med den faktiske sannheten for likhet.
- **F1-score**: Beregner forholdet mellom delte ord mellom det genererte svaret og kildedataene.

Disse målingene hjelper deg med å evaluere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar.

![Evaluer basert på ytelse.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.no.png)

## **Scenario 2: Evaluering av Phi-3 / Phi-3.5-modellen i Azure AI Foundry**

### Før du begynner

Denne veiledningen er en oppfølging av de tidligere blogginnleggene, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" og "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I disse innleggene gikk vi gjennom prosessen med å finjustere en Phi-3 / Phi-3.5-modell i Azure AI Foundry og integrere den med Prompt flow.

I denne veiledningen vil du distribuere en Azure OpenAI-modell som en evaluator i Azure AI Foundry og bruke den til å evaluere din finjusterte Phi-3 / Phi-3.5-modell.

Før du begynner denne veiledningen, sørg for at du har følgende forutsetninger, som beskrevet i de tidligere veiledningene:

1. Et forberedt datasett for å evaluere den finjusterte Phi-3 / Phi-3.5-modellen.
1. En Phi-3 / Phi-3.5-modell som er finjustert og distribuert til Azure Machine Learning.
1. En Prompt flow integrert med din finjusterte Phi-3 / Phi-3.5-modell i Azure AI Foundry.

> [!NOTE]
> Du vil bruke filen *test_data.jsonl*, som ligger i data-mappen fra **ULTRACHAT_200k**-datasettet som ble lastet ned i de forrige blogginnleggene, som datasettet for å evaluere den finjusterte Phi-3 / Phi-3.5-modellen.

#### Integrer den tilpassede Phi-3 / Phi-3.5-modellen med Prompt flow i Azure AI Foundry (Kode-først-tilnærming)

> [!NOTE]
> Hvis du fulgte lavkode-tilnærmingen beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kan du hoppe over denne øvelsen og gå videre til neste.
> Hvis du derimot fulgte kode-først-tilnærmingen beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" for å finjustere og distribuere din Phi-3 / Phi-3.5-modell, er prosessen med å koble modellen din til Prompt flow litt annerledes. Du vil lære denne prosessen i denne øvelsen.

For å fortsette må du integrere din finjusterte Phi-3 / Phi-3.5-modell i Prompt flow i Azure AI Foundry.

#### Opprett Azure AI Foundry Hub

Du må opprette en Hub før du oppretter et prosjekt. En Hub fungerer som en Ressursgruppe, som lar deg organisere og administrere flere prosjekter i Azure AI Foundry.

1. Logg inn på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Velg **Alle hubs** fra venstre sidefane.

1. Velg **+ Ny hub** fra navigasjonsmenyen.

    ![Opprett hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.no.png)

1. Utfør følgende oppgaver:

    - Skriv inn **Hub-navn**. Det må være en unik verdi.
    - Velg ditt Azure **Abonnement**.
    - Velg **Ressursgruppe** som skal brukes (opprett en ny hvis nødvendig).
    - Velg **Plassering** du vil bruke.
    - Velg **Koble til Azure AI-tjenester** som skal brukes (opprett en ny hvis nødvendig).
    - Velg **Koble til Azure AI Search** for å **Hopp over tilkobling**.
![Fyll hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.no.png)

1. Velg **Neste**.

#### Opprett Azure AI Foundry-prosjekt

1. I huben du opprettet, velg **Alle prosjekter** fra fanen på venstre side.

1. Velg **+ Nytt prosjekt** fra navigasjonsmenyen.

    ![Velg nytt prosjekt.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.no.png)

1. Skriv inn **Prosjektnavn**. Det må være en unik verdi.

    ![Opprett prosjekt.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.no.png)

1. Velg **Opprett et prosjekt**.

#### Legg til en tilpasset tilkobling for den finjusterte Phi-3 / Phi-3.5-modellen

For å integrere din tilpassede Phi-3 / Phi-3.5-modell med Prompt flow, må du lagre modellens endepunkt og nøkkel i en tilpasset tilkobling. Dette oppsettet sikrer tilgang til din tilpassede Phi-3 / Phi-3.5-modell i Prompt flow.

#### Angi API-nøkkel og endepunkt-URI for den finjusterte Phi-3 / Phi-3.5-modellen

1. Gå til [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviger til Azure Machine Learning-arbeidsområdet du opprettet.

1. Velg **Endepunkter** fra fanen på venstre side.

    ![Velg endepunkter.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.no.png)

1. Velg endepunktet du opprettet.

    ![Velg opprettet endepunkt.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.no.png)

1. Velg **Forbruk** fra navigasjonsmenyen.

1. Kopier ditt **REST-endepunkt** og **Primærnøkkel**.

    ![Kopier API-nøkkel og endepunkt-URI.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.no.png)

#### Legg til den tilpassede tilkoblingen

1. Gå til [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. I prosjektet du opprettet, velg **Innstillinger** fra fanen på venstre side.

1. Velg **+ Ny tilkobling**.

    ![Velg ny tilkobling.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.no.png)

1. Velg **Tilpassede nøkler** fra navigasjonsmenyen.

    ![Velg tilpassede nøkler.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.no.png)

1. Utfør følgende oppgaver:

    - Velg **+ Legg til nøkkel-verdi-par**.
    - For nøkkelnavnet, skriv inn **endpoint** og lim inn endepunktet du kopierte fra Azure ML Studio i verdifeltet.
    - Velg **+ Legg til nøkkel-verdi-par** igjen.
    - For nøkkelnavnet, skriv inn **key** og lim inn nøkkelen du kopierte fra Azure ML Studio i verdifeltet.
    - Etter å ha lagt til nøklene, velg **er hemmelig** for å forhindre at nøkkelen blir eksponert.

    ![Legg til tilkobling.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.no.png)

1. Velg **Legg til tilkobling**.

#### Opprett Prompt flow

Du har lagt til en tilpasset tilkobling i Azure AI Foundry. Nå skal vi opprette en Prompt flow ved hjelp av følgende trinn. Deretter kobler du denne Prompt flow til den tilpassede tilkoblingen for å bruke den finjusterte modellen i Prompt flow.

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. Velg **Prompt flow** fra fanen på venstre side.

1. Velg **+ Opprett** fra navigasjonsmenyen.

    ![Velg Prompt flow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.no.png)

1. Velg **Chat flow** fra navigasjonsmenyen.

    ![Velg chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.no.png)

1. Skriv inn **Mappenavn** som skal brukes.

    ![Velg chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.no.png)

1. Velg **Opprett**.

#### Konfigurer Prompt flow for å chatte med din tilpassede Phi-3 / Phi-3.5-modell

Du må integrere den finjusterte Phi-3 / Phi-3.5-modellen i en Prompt flow. Den eksisterende Prompt flow som tilbys, er imidlertid ikke designet for dette formålet. Derfor må du redesigne Prompt flow for å muliggjøre integrasjon av den tilpassede modellen.

1. I Prompt flow, utfør følgende oppgaver for å bygge om den eksisterende flyten:

    - Velg **Råfil-modus**.
    - Slett all eksisterende kode i *flow.dag.yml*-filen.
    - Legg til følgende kode i *flow.dag.yml*.

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

    - Velg **Lagre**.

    ![Velg råfil-modus.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.no.png)

1. Legg til følgende kode i *integrate_with_promptflow.py* for å bruke den tilpassede Phi-3 / Phi-3.5-modellen i Prompt flow.

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

    ![Lim inn Prompt flow-kode.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.no.png)

> [!NOTE]
> For mer detaljert informasjon om hvordan du bruker Prompt flow i Azure AI Foundry, kan du se [Prompt flow i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Velg **Chat input**, **Chat output** for å aktivere chat med modellen din.

    ![Velg Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.no.png)

1. Nå er du klar til å chatte med din tilpassede Phi-3 / Phi-3.5-modell. I neste øvelse vil du lære hvordan du starter Prompt flow og bruker den til å chatte med din finjusterte Phi-3 / Phi-3.5-modell.

> [!NOTE]
>
> Den ombygde flyten skal se ut som bildet nedenfor:
>
> ![Flyteksempel](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.no.png)
>

#### Start Prompt flow

1. Velg **Start beregningsøkter** for å starte Prompt flow.

    ![Start beregningsøkt.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.no.png)

1. Velg **Valider og analyser input** for å fornye parametere.

    ![Valider input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.no.png)

1. Velg **Verdien** til **tilkoblingen** til den tilpassede tilkoblingen du opprettet. For eksempel *connection*.

    ![Tilkobling.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.no.png)

#### Chat med din tilpassede Phi-3 / Phi-3.5-modell

1. Velg **Chat**.

    ![Velg chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.no.png)

1. Her er et eksempel på resultatene: Nå kan du chatte med din tilpassede Phi-3 / Phi-3.5-modell. Det anbefales å stille spørsmål basert på dataene som ble brukt til finjustering.

    ![Chat med Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.no.png)

### Distribuer Azure OpenAI for å evaluere Phi-3 / Phi-3.5-modellen

For å evaluere Phi-3 / Phi-3.5-modellen i Azure AI Foundry, må du distribuere en Azure OpenAI-modell. Denne modellen vil bli brukt til å evaluere ytelsen til Phi-3 / Phi-3.5-modellen.

#### Distribuer Azure OpenAI

1. Logg inn på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

    ![Velg prosjekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.no.png)

1. I prosjektet du opprettet, velg **Distribusjoner** fra fanen på venstre side.

1. Velg **+ Distribuer modell** fra navigasjonsmenyen.

1. Velg **Distribuer grunnmodell**.

    ![Velg distribusjoner.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.no.png)

1. Velg Azure OpenAI-modellen du ønsker å bruke. For eksempel **gpt-4o**.

    ![Velg Azure OpenAI-modellen du ønsker å bruke.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.no.png)

1. Velg **Bekreft**.

### Evaluer den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av Azure AI Foundrys Prompt flow-evaluering

### Start en ny evaluering

1. Gå til [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

    ![Velg prosjekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.no.png)

1. I prosjektet du opprettet, velg **Evaluering** fra fanen på venstre side.

1. Velg **+ Ny evaluering** fra navigasjonsmenyen.
![Velg evaluering.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.no.png)

1. Velg **Prompt flow**-evaluering.

    ![Velg Prompt flow-evaluering.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.no.png)

1. Utfør følgende oppgaver:

    - Skriv inn evalueringsnavnet. Det må være en unik verdi.
    - Velg **Spørsmål og svar uten kontekst** som oppgavetypen. Dette fordi **ULTRACHAT_200k**-datasettet som brukes i denne opplæringen ikke inneholder kontekst.
    - Velg prompt flow-en du ønsker å evaluere.

    ![Prompt flow-evaluering.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.no.png)

1. Velg **Neste**.

1. Utfør følgende oppgaver:

    - Velg **Legg til datasettet ditt** for å laste opp datasettet. For eksempel kan du laste opp testdatasett-filen, som *test_data.json1*, som er inkludert når du laster ned **ULTRACHAT_200k**-datasettet.
    - Velg riktig **Datasettkolonne** som samsvarer med datasettet ditt. For eksempel, hvis du bruker **ULTRACHAT_200k**-datasettet, velg **${data.prompt}** som datasettkolonne.

    ![Prompt flow-evaluering.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.no.png)

1. Velg **Neste**.

1. Utfør følgende oppgaver for å konfigurere ytelses- og kvalitetsmålinger:

    - Velg ytelses- og kvalitetsmålingene du ønsker å bruke.
    - Velg Azure OpenAI-modellen du opprettet for evaluering. For eksempel, velg **gpt-4o**.

    ![Prompt flow-evaluering.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.no.png)

1. Utfør følgende oppgaver for å konfigurere risiko- og sikkerhetsmålinger:

    - Velg risiko- og sikkerhetsmålingene du ønsker å bruke.
    - Velg terskelen for å beregne feilraten du ønsker å bruke. For eksempel, velg **Medium**.
    - For **spørsmål**, velg **Datakilde** til **{$data.prompt}**.
    - For **svar**, velg **Datakilde** til **{$run.outputs.answer}**.
    - For **ground_truth**, velg **Datakilde** til **{$data.message}**.

    ![Prompt flow-evaluering.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.no.png)

1. Velg **Neste**.

1. Velg **Send inn** for å starte evalueringen.

1. Evalueringen vil ta litt tid å fullføre. Du kan overvåke fremdriften i **Evaluering**-fanen.

### Gjennomgå evalueringsresultatene

> [!NOTE]
> Resultatene som presenteres nedenfor er ment å illustrere evalueringsprosessen. I denne opplæringen har vi brukt en modell som er finjustert på et relativt lite datasett, noe som kan føre til suboptimale resultater. Faktiske resultater kan variere betydelig avhengig av størrelsen, kvaliteten og mangfoldet på datasettet som brukes, samt den spesifikke konfigurasjonen av modellen.

Når evalueringen er fullført, kan du gjennomgå resultatene for både ytelses- og sikkerhetsmålinger.

1. Ytelses- og kvalitetsmålinger:

    - Vurder modellens effektivitet i å generere sammenhengende, flytende og relevante svar.

    ![Evalueringsresultat.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.no.png)

1. Risiko- og sikkerhetsmålinger:

    - Sørg for at modellens utdata er sikre og i tråd med prinsippene for ansvarlig AI, og unngå skadelig eller støtende innhold.

    ![Evalueringsresultat.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.no.png)

1. Du kan bla ned for å se **Detaljerte måleresultater**.

    ![Evalueringsresultat.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.no.png)

1. Ved å evaluere din tilpassede Phi-3 / Phi-3.5-modell mot både ytelses- og sikkerhetsmålinger, kan du bekrefte at modellen ikke bare er effektiv, men også følger ansvarlige AI-praksiser, og dermed er klar for implementering i virkelige scenarier.

## Gratulerer!

### Du har fullført denne opplæringen

Du har med hell evaluert den finjusterte Phi-3-modellen integrert med Prompt flow i Azure AI Foundry. Dette er et viktig steg for å sikre at AI-modellene dine ikke bare presterer godt, men også følger Microsofts prinsipper for ansvarlig AI, slik at du kan bygge pålitelige og pålitelige AI-applikasjoner.

![Arkitektur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.no.png)

## Rydd opp Azure-ressurser

Rydd opp i Azure-ressursene dine for å unngå ekstra kostnader på kontoen din. Gå til Azure-portalen og slett følgende ressurser:

- Azure Machine Learning-ressursen.
- Endepunktet for Azure Machine Learning-modellen.
- Azure AI Foundry-prosjektressursen.
- Azure AI Foundry Prompt flow-ressursen.

### Neste steg

#### Dokumentasjon

- [Vurder AI-systemer ved hjelp av instrumentbordet for ansvarlig AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluering og overvåking av målinger for generativ AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry-dokumentasjon](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-dokumentasjon](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Opplæringsinnhold

- [Introduksjon til Microsofts tilnærming til ansvarlig AI](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduksjon til Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referanse

- [Hva er ansvarlig AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Kunngjøring av nye verktøy i Azure AI for å hjelpe deg med å bygge sikrere og mer pålitelige generative AI-applikasjoner](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluering av generative AI-applikasjoner](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.