# Utvärdera den finjusterade Phi-3 / Phi-3.5-modellen i Azure AI Foundry med fokus på Microsofts principer för ansvarsfull AI

Detta end-to-end (E2E) exempel är baserat på guiden "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" från Microsoft Tech Community.

## Översikt

### Hur kan du utvärdera säkerheten och prestandan hos en finjusterad Phi-3 / Phi-3.5-modell i Azure AI Foundry?

Finjustering av en modell kan ibland leda till oavsiktliga eller oönskade svar. För att säkerställa att modellen förblir säker och effektiv är det viktigt att utvärdera modellens potential att generera skadligt innehåll och dess förmåga att producera korrekta, relevanta och sammanhängande svar. I den här handledningen lär du dig hur du utvärderar säkerheten och prestandan hos en finjusterad Phi-3 / Phi-3.5-modell som integrerats med Prompt flow i Azure AI Foundry.

Här är en översikt av Azure AI Foundrys utvärderingsprocess.

![Arkitektur av handledningen.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.sv.png)

*Bildkälla: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> För mer detaljerad information och ytterligare resurser om Phi-3 / Phi-3.5, besök [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Förutsättningar

- [Python](https://www.python.org/downloads)
- [Azure-prenumeration](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finjusterad Phi-3 / Phi-3.5-modell

### Innehållsförteckning

1. [**Scenario 1: Introduktion till Azure AI Foundrys Prompt flow-utvärdering**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduktion till säkerhetsutvärdering](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduktion till prestandautvärdering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Utvärdera Phi-3 / Phi-3.5-modellen i Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Innan du börjar](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuera Azure OpenAI för att utvärdera Phi-3 / Phi-3.5-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Utvärdera den finjusterade Phi-3 / Phi-3.5-modellen med Azure AI Foundrys Prompt flow-utvärdering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Grattis!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduktion till Azure AI Foundrys Prompt flow-utvärdering**

### Introduktion till säkerhetsutvärdering

För att säkerställa att din AI-modell är etisk och säker är det avgörande att utvärdera den mot Microsofts principer för ansvarsfull AI. I Azure AI Foundry gör säkerhetsutvärderingar det möjligt att bedöma modellens sårbarhet för "jailbreak"-attacker och dess potential att generera skadligt innehåll, vilket är direkt i linje med dessa principer.

![Säkerhetsutvärdering.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.sv.png)

*Bildkälla: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts principer för ansvarsfull AI

Innan du börjar med de tekniska stegen är det viktigt att förstå Microsofts principer för ansvarsfull AI, ett etiskt ramverk som är utformat för att vägleda ansvarsfull utveckling, distribution och drift av AI-system. Dessa principer säkerställer att AI-teknologier utvecklas på ett rättvist, transparent och inkluderande sätt. De utgör grunden för att utvärdera säkerheten hos AI-modeller.

Microsofts principer för ansvarsfull AI inkluderar:

- **Rättvisa och inkludering**: AI-system ska behandla alla rättvist och undvika att påverka liknande grupper av människor på olika sätt. Till exempel ska AI-system som ger vägledning om medicinsk behandling, låneansökningar eller anställningar ge samma rekommendationer till alla med liknande symptom, ekonomiska förhållanden eller yrkeskvalifikationer.

- **Tillförlitlighet och säkerhet**: För att bygga förtroende är det avgörande att AI-system fungerar tillförlitligt, säkert och konsekvent. Dessa system ska kunna fungera som de ursprungligen var utformade, reagera säkert på oväntade förhållanden och motstå skadlig manipulation.

- **Transparens**: När AI-system bidrar till beslut som har stora konsekvenser för människors liv är det avgörande att människor förstår hur dessa beslut fattades.

- **Sekretess och säkerhet**: När AI blir allt vanligare blir skyddet av integritet och säkerhet för personliga och affärsmässiga uppgifter allt viktigare och mer komplext.

- **Ansvarsskyldighet**: De som utformar och distribuerar AI-system måste vara ansvariga för hur deras system fungerar. Organisationer bör använda industristandarder för att utveckla normer för ansvarsskyldighet.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.sv.png)

*Bildkälla: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> För att lära dig mer om Microsofts principer för ansvarsfull AI, besök [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Säkerhetsmått

I denna handledning kommer du att utvärdera säkerheten hos den finjusterade Phi-3-modellen med hjälp av Azure AI Foundrys säkerhetsmått. Dessa mått hjälper dig att bedöma modellens potential att generera skadligt innehåll och dess sårbarhet för "jailbreak"-attacker. Säkerhetsmåtten inkluderar:

- **Självskaderelaterat innehåll**: Utvärderar om modellen tenderar att producera innehåll relaterat till självskada.
- **Hatiskt och orättvist innehåll**: Utvärderar om modellen tenderar att producera hatiskt eller orättvist innehåll.
- **Våldsamt innehåll**: Utvärderar om modellen tenderar att producera våldsamt innehåll.
- **Sexuellt innehåll**: Utvärderar om modellen tenderar att producera olämpligt sexuellt innehåll.

Genom att utvärdera dessa aspekter säkerställer du att AI-modellen inte producerar skadligt eller stötande innehåll, i linje med samhälleliga värderingar och regulatoriska standarder.

![Utvärdera baserat på säkerhet.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.sv.png)

### Introduktion till prestandautvärdering

För att säkerställa att din AI-modell presterar som förväntat är det viktigt att utvärdera dess prestanda mot specifika prestandamått. I Azure AI Foundry gör prestandautvärderingar det möjligt att bedöma modellens effektivitet i att generera korrekta, relevanta och sammanhängande svar.

![Prestandautvärdering.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.sv.png)

*Bildkälla: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prestandamått

I denna handledning kommer du att utvärdera prestandan hos den finjusterade Phi-3 / Phi-3.5-modellen med hjälp av Azure AI Foundrys prestandamått. Dessa mått hjälper dig att bedöma modellens effektivitet i att generera korrekta, relevanta och sammanhängande svar. Prestandamåtten inkluderar:

- **Grundadhet**: Utvärderar hur väl de genererade svaren överensstämmer med informationen från indata.
- **Relevans**: Utvärderar hur relevant de genererade svaren är för de givna frågorna.
- **Sammanhang**: Utvärderar hur smidigt den genererade texten flyter, hur naturlig den känns och hur lik den är mänskligt språk.
- **Språklig flyt**: Utvärderar språkkunskapen i den genererade texten.
- **GPT-likhet**: Jämför det genererade svaret med den faktiska sanningen för likhet.
- **F1-poäng**: Beräknar förhållandet mellan delade ord mellan det genererade svaret och källdata.

Dessa mått hjälper dig att utvärdera modellens effektivitet i att generera korrekta, relevanta och sammanhängande svar.

![Utvärdera baserat på prestanda.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.sv.png)

## **Scenario 2: Utvärdera Phi-3 / Phi-3.5-modellen i Azure AI Foundry**

### Innan du börjar

Denna handledning är en uppföljning av tidigare blogginlägg, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" och "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I dessa inlägg gick vi igenom processen att finjustera en Phi-3 / Phi-3.5-modell i Azure AI Foundry och integrera den med Prompt flow.

I denna handledning kommer du att distribuera en Azure OpenAI-modell som en utvärderare i Azure AI Foundry och använda den för att utvärdera din finjusterade Phi-3 / Phi-3.5-modell.

Innan du börjar denna handledning, se till att du har följande förutsättningar, som beskrivs i de tidigare handledningarna:

1. Ett förberett dataset för att utvärdera den finjusterade Phi-3 / Phi-3.5-modellen.
1. En Phi-3 / Phi-3.5-modell som har finjusterats och distribuerats till Azure Machine Learning.
1. En Prompt flow integrerad med din finjusterade Phi-3 / Phi-3.5-modell i Azure AI Foundry.

> [!NOTE]
> Du kommer att använda filen *test_data.jsonl*, som finns i datamappen från **ULTRACHAT_200k**-datasetet som laddades ner i de tidigare blogginläggen, som dataset för att utvärdera den finjusterade Phi-3 / Phi-3.5-modellen.

#### Integrera den anpassade Phi-3 / Phi-3.5-modellen med Prompt flow i Azure AI Foundry (Kodbaserat tillvägagångssätt)

> [!NOTE]
> Om du följde det lågnivåkodade tillvägagångssättet som beskrivs i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" kan du hoppa över denna övning och gå vidare till nästa.
> Om du däremot följde det kodbaserade tillvägagångssättet som beskrivs i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" för att finjustera och distribuera din Phi-3 / Phi-3.5-modell, är processen för att koppla din modell till Prompt flow något annorlunda. Du kommer att lära dig denna process i denna övning.

För att fortsätta behöver du integrera din finjusterade Phi-3 / Phi-3.5-modell i Prompt flow i Azure AI Foundry.

#### Skapa Azure AI Foundry Hub

Du behöver skapa en Hub innan du skapar Projektet. En Hub fungerar som en Resursgrupp och gör det möjligt att organisera och hantera flera Projekt inom Azure AI Foundry.

1. Logga in på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Välj **All hubs** från den vänstra panelen.

1. Välj **+ New hub** från navigeringsmenyn.

    ![Skapa hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.sv.png)

1. Utför följande uppgifter:

    - Ange **Hub name**. Det måste vara ett unikt värde.
    - Välj din Azure **Subscription**.
    - Välj den **Resource group** du vill använda (skapa en ny om det behövs).
    - Välj den **Location** du vill använda.
    - Välj **Connect Azure AI Services** att använda (skapa en ny om det behövs).
    - Välj **Connect Azure AI Search** och **Skip connecting**.
![Fyll hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.sv.png)

1. Välj **Nästa**.

#### Skapa Azure AI Foundry-projekt

1. I hubben som du skapade, välj **Alla projekt** från fliken till vänster.

1. Välj **+ Nytt projekt** från navigeringsmenyn.

    ![Välj nytt projekt.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.sv.png)

1. Ange **Projektnamn**. Det måste vara ett unikt värde.

    ![Skapa projekt.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.sv.png)

1. Välj **Skapa ett projekt**.

#### Lägg till en anpassad anslutning för den finjusterade Phi-3 / Phi-3.5-modellen

För att integrera din anpassade Phi-3 / Phi-3.5-modell med Prompt flow behöver du spara modellens slutpunkt och nyckel i en anpassad anslutning. Denna konfiguration säkerställer åtkomst till din anpassade Phi-3 / Phi-3.5-modell i Prompt flow.

#### Ange API-nyckel och slutpunkts-URI för den finjusterade Phi-3 / Phi-3.5-modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigera till det Azure Machine Learning-arbetsutrymme som du skapade.

1. Välj **Slutpunkter** från fliken till vänster.

    ![Välj slutpunkter.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.sv.png)

1. Välj slutpunkten som du skapade.

    ![Välj skapad slutpunkt.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.sv.png)

1. Välj **Konsumera** från navigeringsmenyn.

1. Kopiera din **REST-slutpunkt** och **Primär nyckel**.

    ![Kopiera API-nyckel och slutpunkts-URI.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.sv.png)

#### Lägg till den anpassade anslutningen

1. Besök [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigera till det Azure AI Foundry-projekt som du skapade.

1. I projektet som du skapade, välj **Inställningar** från fliken till vänster.

1. Välj **+ Ny anslutning**.

    ![Välj ny anslutning.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.sv.png)

1. Välj **Anpassade nycklar** från navigeringsmenyn.

    ![Välj anpassade nycklar.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.sv.png)

1. Utför följande uppgifter:

    - Välj **+ Lägg till nyckel-värde-par**.
    - För nyckelns namn, ange **slutpunkt** och klistra in slutpunkten du kopierade från Azure ML Studio i värdefältet.
    - Välj **+ Lägg till nyckel-värde-par** igen.
    - För nyckelns namn, ange **nyckel** och klistra in nyckeln du kopierade från Azure ML Studio i värdefältet.
    - Efter att ha lagt till nycklarna, välj **är hemlig** för att förhindra att nyckeln exponeras.

    ![Lägg till anslutning.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.sv.png)

1. Välj **Lägg till anslutning**.

#### Skapa Prompt flow

Du har lagt till en anpassad anslutning i Azure AI Foundry. Nu ska vi skapa en Prompt flow med följande steg. Därefter kopplar du denna Prompt flow till den anpassade anslutningen för att använda den finjusterade modellen i Prompt flow.

1. Navigera till det Azure AI Foundry-projekt som du skapade.

1. Välj **Prompt flow** från fliken till vänster.

1. Välj **+ Skapa** från navigeringsmenyn.

    ![Välj Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.sv.png)

1. Välj **Chatflöde** från navigeringsmenyn.

    ![Välj chatflöde.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.sv.png)

1. Ange **Mappnamn** att använda.

    ![Välj chatflöde.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.sv.png)

1. Välj **Skapa**.

#### Konfigurera Prompt flow för att chatta med din anpassade Phi-3 / Phi-3.5-modell

Du behöver integrera den finjusterade Phi-3 / Phi-3.5-modellen i ett Prompt flow. Det befintliga Prompt flow som tillhandahålls är dock inte utformat för detta ändamål. Därför måste du omdesigna Prompt flow för att möjliggöra integration av den anpassade modellen.

1. I Prompt flow, utför följande uppgifter för att bygga om det befintliga flödet:

    - Välj **Rå fil-läge**.
    - Radera all befintlig kod i filen *flow.dag.yml*.
    - Lägg till följande kod i *flow.dag.yml*.

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

    - Välj **Spara**.

    ![Välj rå fil-läge.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.sv.png)

1. Lägg till följande kod i *integrate_with_promptflow.py* för att använda den anpassade Phi-3 / Phi-3.5-modellen i Prompt flow.

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

    ![Klistra in prompt flow-kod.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.sv.png)

> [!NOTE]
> För mer detaljerad information om hur man använder Prompt flow i Azure AI Foundry, kan du hänvisa till [Prompt flow i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Välj **Chatinmatning**, **Chatutmatning** för att aktivera chatt med din modell.

    ![Välj Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.sv.png)

1. Nu är du redo att chatta med din anpassade Phi-3 / Phi-3.5-modell. I nästa övning kommer du att lära dig hur du startar Prompt flow och använder det för att chatta med din finjusterade Phi-3 / Phi-3.5-modell.

> [!NOTE]
>
> Det ombyggda flödet ska se ut som bilden nedan:
>
> ![Flödesexempel](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.sv.png)
>

#### Starta Prompt flow

1. Välj **Starta beräkningssessioner** för att starta Prompt flow.

    ![Starta beräkningssession.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.sv.png)

1. Välj **Validera och analysera inmatning** för att uppdatera parametrar.

    ![Validera inmatning.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.sv.png)

1. Välj **Värde** för **anslutning** till den anpassade anslutningen du skapade. Till exempel *connection*.

    ![Anslutning.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.sv.png)

#### Chatta med din anpassade Phi-3 / Phi-3.5-modell

1. Välj **Chatta**.

    ![Välj chatt.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.sv.png)

1. Här är ett exempel på resultaten: Nu kan du chatta med din anpassade Phi-3 / Phi-3.5-modell. Det rekommenderas att ställa frågor baserade på data som användes för finjusteringen.

    ![Chatta med prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.sv.png)

### Distribuera Azure OpenAI för att utvärdera Phi-3 / Phi-3.5-modellen

För att utvärdera Phi-3 / Phi-3.5-modellen i Azure AI Foundry behöver du distribuera en Azure OpenAI-modell. Denna modell kommer att användas för att utvärdera prestandan hos Phi-3 / Phi-3.5-modellen.

#### Distribuera Azure OpenAI

1. Logga in på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigera till det Azure AI Foundry-projekt som du skapade.

    ![Välj Projekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.sv.png)

1. I projektet som du skapade, välj **Distributioner** från fliken till vänster.

1. Välj **+ Distribuera modell** från navigeringsmenyn.

1. Välj **Distribuera basmodell**.

    ![Välj Distributioner.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.sv.png)

1. Välj den Azure OpenAI-modell du vill använda. Till exempel **gpt-4o**.

    ![Välj Azure OpenAI-modell du vill använda.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.sv.png)

1. Välj **Bekräfta**.

### Utvärdera den finjusterade Phi-3 / Phi-3.5-modellen med Azure AI Foundry's Prompt flow-utvärdering

### Starta en ny utvärdering

1. Besök [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigera till det Azure AI Foundry-projekt som du skapade.

    ![Välj Projekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.sv.png)

1. I projektet som du skapade, välj **Utvärdering** från fliken till vänster.

1. Välj **+ Ny utvärdering** från navigeringsmenyn.
![Välj utvärdering.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.sv.png)

1. Välj **Prompt flow**-utvärdering.

    ![Välj Prompt flow-utvärdering.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.sv.png)

1. Utför följande uppgifter:

    - Ange ett namn för utvärderingen. Det måste vara unikt.
    - Välj **Fråga och svar utan kontext** som uppgiftstyp. Detta eftersom datasetet **ULTRACHAT_200k** som används i denna handledning inte innehåller någon kontext.
    - Välj det prompt flow du vill utvärdera.

    ![Prompt flow-utvärdering.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.sv.png)

1. Välj **Nästa**.

1. Utför följande uppgifter:

    - Välj **Lägg till ditt dataset** för att ladda upp datasetet. Till exempel kan du ladda upp testdatafilen, som *test_data.json1*, som ingår när du laddar ner datasetet **ULTRACHAT_200k**.
    - Välj rätt **Datasetskolumn** som matchar ditt dataset. Till exempel, om du använder datasetet **ULTRACHAT_200k**, välj **${data.prompt}** som datasetskolumn.

    ![Prompt flow-utvärdering.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.sv.png)

1. Välj **Nästa**.

1. Utför följande uppgifter för att konfigurera prestations- och kvalitetsmått:

    - Välj de prestations- och kvalitetsmått du vill använda.
    - Välj den Azure OpenAI-modell du skapade för utvärdering. Till exempel, välj **gpt-4o**.

    ![Prompt flow-utvärdering.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.sv.png)

1. Utför följande uppgifter för att konfigurera risk- och säkerhetsmått:

    - Välj de risk- och säkerhetsmått du vill använda.
    - Välj den tröskel du vill använda för att beräkna defektsatsen. Till exempel, välj **Medium**.
    - För **fråga**, välj **Datakälla** till **{$data.prompt}**.
    - För **svar**, välj **Datakälla** till **{$run.outputs.answer}**.
    - För **ground_truth**, välj **Datakälla** till **{$data.message}**.

    ![Prompt flow-utvärdering.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.sv.png)

1. Välj **Nästa**.

1. Välj **Skicka** för att starta utvärderingen.

1. Utvärderingen kommer att ta en stund att slutföra. Du kan övervaka framstegen i fliken **Utvärdering**.

### Granska utvärderingsresultaten

> [!NOTE]
> Resultaten som presenteras nedan är avsedda att illustrera utvärderingsprocessen. I denna handledning har vi använt en modell som är finjusterad på ett relativt litet dataset, vilket kan leda till mindre optimala resultat. Faktiska resultat kan variera avsevärt beroende på storlek, kvalitet och mångfald av det dataset som används, samt den specifika konfigurationen av modellen.

När utvärderingen är klar kan du granska resultaten för både prestations- och säkerhetsmått.

1. Prestations- och kvalitetsmått:

    - Utvärdera modellens effektivitet i att generera sammanhängande, flytande och relevanta svar.

    ![Utvärderingsresultat.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.sv.png)

1. Risk- och säkerhetsmått:

    - Säkerställ att modellens resultat är säkra och följer principerna för Ansvarsfull AI, och undviker skadligt eller stötande innehåll.

    ![Utvärderingsresultat.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.sv.png)

1. Du kan rulla ned för att visa **Detaljerade måttresultat**.

    ![Utvärderingsresultat.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.sv.png)

1. Genom att utvärdera din anpassade Phi-3 / Phi-3.5-modell mot både prestations- och säkerhetsmått kan du bekräfta att modellen inte bara är effektiv, utan också följer principerna för ansvarsfull AI, vilket gör den redo för användning i verkliga tillämpningar.

## Grattis!

### Du har slutfört denna handledning

Du har framgångsrikt utvärderat den finjusterade Phi-3-modellen integrerad med Prompt flow i Azure AI Foundry. Detta är ett viktigt steg för att säkerställa att dina AI-modeller inte bara presterar väl, utan också följer Microsofts principer för Ansvarsfull AI för att hjälpa dig bygga pålitliga och trovärdiga AI-applikationer.

![Arkitektur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.sv.png)

## Rensa upp Azure-resurser

Rensa upp dina Azure-resurser för att undvika extra kostnader på ditt konto. Gå till Azure-portalen och ta bort följande resurser:

- Azure Machine Learning-resursen.
- Azure Machine Learning-modellens slutpunkt.
- Azure AI Foundry-projektresursen.
- Azure AI Foundry Prompt flow-resursen.

### Nästa steg

#### Dokumentation

- [Utvärdera AI-system med hjälp av Ansvarsfull AI-instrumentpanelen](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Utvärderings- och övervakningsmått för generativ AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry-dokumentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-dokumentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Utbildningsinnehåll

- [Introduktion till Microsofts Ansvarsfull AI-strategi](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduktion till Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referens

- [Vad är Ansvarsfull AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Lansering av nya verktyg i Azure AI för att hjälpa dig bygga säkrare och mer pålitliga generativa AI-applikationer](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Utvärdering av generativa AI-applikationer](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.