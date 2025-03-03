# Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryssa keskittyen Microsoftin vastuullisen tekoälyn periaatteisiin

Tämä end-to-end (E2E) esimerkki perustuu oppaaseen "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" Microsoft Tech Community -sivustolta.

## Yleiskatsaus

### Kuinka voit arvioida hienosäädetyn Phi-3 / Phi-3.5 -mallin turvallisuutta ja suorituskykyä Azure AI Foundryssa?

Mallin hienosäätö voi joskus johtaa odottamattomiin tai ei-toivottuihin vastauksiin. Jotta malli pysyy turvallisena ja tehokkaana, on tärkeää arvioida sen kykyä tuottaa haitallista sisältöä sekä sen tarkkuutta, osuvuutta ja johdonmukaisuutta. Tässä opetusohjelmassa opit arvioimaan hienosäädetyn Phi-3 / Phi-3.5 -mallin turvallisuutta ja suorituskykyä, kun se on integroitu Prompt flow'n kanssa Azure AI Foundryssa.

Tässä on Azure AI Foundryn arviointiprosessi.

![Opetusohjelman arkkitehtuuri.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.fi.png)

*Kuvan lähde: [Generatiivisen tekoälyn sovellusten arviointi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Saat lisätietoa ja pääset tutustumaan muihin Phi-3 / Phi-3.5 -mallia käsitteleviin resursseihin vierailemalla [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) -sivustolla.

### Esivaatimukset

- [Python](https://www.python.org/downloads)
- [Azure-tilaus](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Hienosäädetty Phi-3 / Phi-3.5 -malli

### Sisällysluettelo

1. [**Skenaario 1: Johdatus Azure AI Foundryn Prompt flow'n arviointiin**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Turvallisuusarvioinnin johdanto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Suorituskyvyn arvioinnin johdanto](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Skenaario 2: Phi-3 / Phi-3.5 -mallin arviointi Azure AI Foundryssa**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Ennen kuin aloitat](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ota käyttöön Azure OpenAI Phi-3 / Phi-3.5 -mallin arvioimiseksi](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryn Prompt flow'n avulla](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Onnittelut!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Skenaario 1: Johdatus Azure AI Foundryn Prompt flow'n arviointiin**

### Turvallisuusarvioinnin johdanto

Jotta tekoälymallisi olisi eettinen ja turvallinen, on tärkeää arvioida se Microsoftin vastuullisen tekoälyn periaatteiden mukaisesti. Azure AI Foundryssa turvallisuusarvioinnit mahdollistavat mallisi haavoittuvuuden jailbreak-hyökkäyksille ja sen kyvyn tuottaa haitallista sisältöä, mikä on linjassa näiden periaatteiden kanssa.

![Turvallisuusarviointi.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.fi.png)

*Kuvan lähde: [Generatiivisen tekoälyn sovellusten arviointi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftin vastuullisen tekoälyn periaatteet

Ennen teknisten vaiheiden aloittamista on tärkeää ymmärtää Microsoftin vastuullisen tekoälyn periaatteet. Tämä eettinen viitekehys on suunniteltu ohjaamaan tekoälyjärjestelmien vastuullista kehittämistä, käyttöönottoa ja käyttöä. Periaatteet varmistavat, että tekoälyteknologiat rakennetaan oikeudenmukaisella, läpinäkyvällä ja osallistavalla tavalla. Ne muodostavat perustan tekoälymallien turvallisuuden arvioinnille.

Microsoftin vastuullisen tekoälyn periaatteet sisältävät:

- **Oikeudenmukaisuus ja osallistavuus**: Tekoälyjärjestelmien tulee kohdella kaikkia oikeudenmukaisesti ja välttää erilaista kohtelua samankaltaisissa tilanteissa oleville ryhmille. Esimerkiksi, kun tekoälyjärjestelmät antavat ohjeita lääketieteelliseen hoitoon, lainahakemuksiin tai työllistymiseen, niiden tulisi antaa samat suositukset kaikille, joilla on samankaltaiset oireet, taloudellinen tilanne tai ammatilliset pätevyydet.

- **Luotettavuus ja turvallisuus**: Luottamuksen rakentamiseksi on tärkeää, että tekoälyjärjestelmät toimivat luotettavasti, turvallisesti ja johdonmukaisesti. Järjestelmien tulisi toimia suunnitellulla tavalla, reagoida turvallisesti odottamattomiin olosuhteisiin ja vastustaa haitallista manipulointia.

- **Läpinäkyvyys**: Kun tekoälyjärjestelmät vaikuttavat merkittäviin päätöksiin ihmisten elämässä, on tärkeää, että ihmiset ymmärtävät, miten päätökset on tehty. Esimerkiksi pankki voi käyttää tekoälyjärjestelmää arvioidakseen henkilön luottokelpoisuuden.

- **Yksityisyys ja turvallisuus**: Kun tekoäly yleistyy, yksityisyyden suojaaminen ja henkilökohtaisten sekä yritystietojen turvallisuus korostuvat. Tekoälyjärjestelmien tarkkuus ja päätöksenteon laatu edellyttävät pääsyä tietoihin, mutta samalla tietosuojaan on kiinnitettävä erityistä huomiota.

- **Vastuullisuus**: Tekoälyjärjestelmien suunnittelijoiden ja käyttäjien on oltava vastuussa siitä, miten järjestelmät toimivat. Organisaatioiden tulisi noudattaa alan standardeja vastuullisuuden varmistamiseksi.

![Täytä hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.fi.png)

*Kuvan lähde: [Mitä on vastuullinen tekoäly?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Lisätietoja Microsoftin vastuullisen tekoälyn periaatteista löytyy [Mitä on vastuullinen tekoäly?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) -sivulta.

#### Turvallisuusmittarit

Tässä opetusohjelmassa arvioit hienosäädetyn Phi-3-mallin turvallisuutta Azure AI Foundryn turvallisuusmittareiden avulla. Näiden mittareiden avulla voit arvioida mallin kykyä tuottaa haitallista sisältöä ja sen haavoittuvuutta jailbreak-hyökkäyksille. Turvallisuusmittarit sisältävät:

- **Itsetuhoinen sisältö**: Arvioi, onko mallilla taipumus tuottaa itsetuhoista sisältöä.
- **Vihamielinen ja epäoikeudenmukainen sisältö**: Arvioi, onko mallilla taipumus tuottaa vihamielistä tai epäoikeudenmukaista sisältöä.
- **Väkivaltainen sisältö**: Arvioi, onko mallilla taipumus tuottaa väkivaltaista sisältöä.
- **Seksuaalinen sisältö**: Arvioi, onko mallilla taipumus tuottaa sopimatonta seksuaalista sisältöä.

Näiden osa-alueiden arviointi varmistaa, ettei tekoälymalli tuota haitallista tai loukkaavaa sisältöä ja että se on linjassa yhteiskunnallisten arvojen ja sääntelystandardien kanssa.

![Arvioi turvallisuuden perusteella.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.fi.png)

### Suorituskyvyn arvioinnin johdanto

Jotta tekoälymallisi toimii odotetusti, on tärkeää arvioida sen suorituskyky suorituskykymittareiden perusteella. Azure AI Foundryssa suorituskyvyn arvioinnit mahdollistavat mallin tehokkuuden arvioinnin tarkkojen, osuvien ja johdonmukaisten vastausten tuottamisessa.

![Turvallisuusarviointi.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.fi.png)

*Kuvan lähde: [Generatiivisen tekoälyn sovellusten arviointi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Suorituskykymittarit

Tässä opetusohjelmassa arvioit hienosäädetyn Phi-3 / Phi-3.5 -mallin suorituskykyä Azure AI Foundryn suorituskykymittareiden avulla. Näiden mittareiden avulla voit arvioida mallin tehokkuutta tarkkojen, osuvien ja johdonmukaisten vastausten tuottamisessa. Suorituskykymittarit sisältävät:

- **Perusteltavuus**: Arvioi, kuinka hyvin tuotetut vastaukset vastaavat syötelähteen tietoja.
- **Osuvuus**: Arvioi tuotettujen vastausten osuvuutta annettuihin kysymyksiin.
- **Johdonmukaisuus**: Arvioi, kuinka sujuvasti tuotettu teksti etenee ja muistuttaa luonnollista kieltä.
- **Sujuvuus**: Arvioi tuotetun tekstin kielenkäytön tasoa.
- **GPT-yhtäläisyys**: Vertaa tuotettua vastausta ja oikeaa vastausta yhtäläisyyden perusteella.
- **F1-pisteet**: Laskee jaettujen sanojen osuuden tuotetun vastauksen ja lähdetietojen välillä.

Nämä mittarit auttavat arvioimaan mallin tehokkuutta tarkkojen, osuvien ja johdonmukaisten vastausten tuottamisessa.

![Arvioi suorituskyvyn perusteella.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.fi.png)

## **Skenaario 2: Phi-3 / Phi-3.5 -mallin arviointi Azure AI Foundryssa**

### Ennen kuin aloitat

Tämä opetusohjelma on jatkoa aiemmille blogipostauksille "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ja "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Näissä postauksissa käytiin läpi Phi-3 / Phi-3.5 -mallin hienosäätö Azure AI Foundryssa ja sen integrointi Prompt flow'n kanssa.

Tässä opetusohjelmassa otat käyttöön Azure OpenAI -mallin arvioijana Azure AI Foundryssa ja käytät sitä hienosäädetyn Phi-3 / Phi-3.5 -mallisi arvioimiseen.

Ennen tämän opetusohjelman aloittamista varmista, että sinulla on seuraavat esivaatimukset, kuten aiemmissa opetusohjelmissa kuvattiin:

1. Valmisteltu datasetti hienosäädetyn Phi-3 / Phi-3.5 -mallin arviointiin.
1. Hienosäädetty ja Azure Machine Learningiin käyttöön otettu Phi-3 / Phi-3.5 -malli.
1. Prompt flow, joka on integroitu hienosäädettyyn Phi-3 / Phi-3.5 -malliisi Azure AI Foundryssa.

> [!NOTE]
> Käytät *test_data.jsonl*-tiedostoa, joka sijaitsee **ULTRACHAT_200k**-datasetin data-kansiossa, aiemmissa blogipostauksissa ladattuna datasetinä hienosäädetyn Phi-3 / Phi-3.5 -mallin arviointiin.

#### Integroi mukautettu Phi-3 / Phi-3.5 -malli Prompt flow'n kanssa Azure AI Foundryssa (Code first -lähestymistapa)

> [!NOTE]
> Jos seurasit vähäkoodista lähestymistapaa, joka kuvattiin "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" -oppaassa, voit ohittaa tämän harjoituksen ja siirtyä seuraavaan.
> Jos kuitenkin seurasit koodipohjaista lähestymistapaa, joka kuvattiin "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" -oppaassa, hienosäädetyn Phi-3 / Phi-3.5 -mallisi yhdistämisprosessi Prompt flow'hun on hieman erilainen. Opit tämän prosessin tässä harjoituksessa.

Jatkaaksesi sinun täytyy integroida hienosäädetty Phi-3 / Phi-3.5 -mallisi Prompt flow'hun Azure AI Foundryssa.

#### Luo Azure AI Foundry Hub

Sinun täytyy luoda Hub ennen Projektin luomista. Hub toimii resurssiryhmän tavoin, jolloin voit organisoida ja hallita useita projekteja Azure AI Foundryssa.

1. Kirjaudu sisään [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Valitse **All hubs** vasemman puolen välilehdestä.

1. Valitse **+ New hub** navigointivalikosta.

    ![Luo hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.fi.png)

1. Suorita seuraavat tehtävät:

    - Syötä **Hub name**. Nimen tulee olla yksilöllinen.
    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Valitse **Location**, jota haluat käyttää.
    - Valitse **Connect Azure AI Services** (luo uusi tarvittaessa).
    - Valitse **Connect Azure AI Search** ja valitse **Skip connecting**.
![Täytä hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.fi.png)

1. Valitse **Seuraava**.

#### Luo Azure AI Foundry -projekti

1. Valitse luomassasi hubissa vasemman reunan välilehdestä **Kaikki projektit**.

1. Valitse navigointivalikosta **+ Uusi projekti**.

    ![Valitse uusi projekti.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.fi.png)

1. Anna **Projektin nimi**. Sen täytyy olla yksilöllinen arvo.

    ![Luo projekti.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.fi.png)

1. Valitse **Luo projekti**.

#### Lisää mukautettu yhteys hienosäädetylle Phi-3 / Phi-3.5 -mallille

Jotta voit integroida mukautetun Phi-3 / Phi-3.5 -mallisi Prompt flow -työkaluun, sinun täytyy tallentaa mallin päätepiste ja avain mukautettuun yhteyteen. Tämä asetus varmistaa pääsyn mukautettuun Phi-3 / Phi-3.5 -malliin Prompt flow -työkalussa.

#### Aseta hienosäädetyn Phi-3 / Phi-3.5 -mallin API-avain ja päätepisteen URI

1. Siirry [Azure ML Studioon](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure Machine Learning -työtilaan.

1. Valitse vasemman reunan välilehdestä **Päätepisteet**.

    ![Valitse päätepisteet.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.fi.png)

1. Valitse luomasi päätepiste.

    ![Valitse luotu päätepiste.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.fi.png)

1. Valitse navigointivalikosta **Kulutus**.

1. Kopioi **REST-päätepiste** ja **Ensisijainen avain**.

    ![Kopioi API-avain ja päätepisteen URI.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.fi.png)

#### Lisää mukautettu yhteys

1. Siirry [Azure AI Foundryyn](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure AI Foundry -projektiin.

1. Valitse luomassasi projektissa vasemman reunan välilehdestä **Asetukset**.

1. Valitse **+ Uusi yhteys**.

    ![Valitse uusi yhteys.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.fi.png)

1. Valitse navigointivalikosta **Mukautetut avaimet**.

    ![Valitse mukautetut avaimet.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.fi.png)

1. Suorita seuraavat toimenpiteet:

    - Valitse **+ Lisää avain-arvopareja**.
    - Anna avaimen nimeksi **endpoint** ja liitä Azure ML Studiosta kopioimasi päätepiste arvokenttään.
    - Valitse uudelleen **+ Lisää avain-arvopareja**.
    - Anna avaimen nimeksi **key** ja liitä Azure ML Studiosta kopioimasi avain arvokenttään.
    - Valitse **on salainen** varmistaaksesi, ettei avain tule näkyviin.

    ![Lisää yhteys.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.fi.png)

1. Valitse **Lisää yhteys**.

#### Luo Prompt flow

Olet lisännyt mukautetun yhteyden Azure AI Foundryyn. Nyt luodaan Prompt flow seuraavien vaiheiden avulla. Tämän jälkeen yhdistät Prompt flow -työkalun mukautettuun yhteyteen käyttääksesi hienosäädettyä mallia Prompt flow -työkalussa.

1. Siirry luomaasi Azure AI Foundry -projektiin.

1. Valitse vasemman reunan välilehdestä **Prompt flow**.

1. Valitse navigointivalikosta **+ Luo**.

    ![Valitse Prompt flow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.fi.png)

1. Valitse navigointivalikosta **Chat flow**.

    ![Valitse chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.fi.png)

1. Anna **Kansion nimi**, jota haluat käyttää.

    ![Valitse chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.fi.png)

1. Valitse **Luo**.

#### Määritä Prompt flow keskustelemaan mukautetun Phi-3 / Phi-3.5 -mallisi kanssa

Sinun täytyy integroida hienosäädetty Phi-3 / Phi-3.5 -malli Prompt flow -työkaluun. Olemassa oleva Prompt flow ei kuitenkaan ole suunniteltu tähän tarkoitukseen. Siksi sinun täytyy suunnitella Prompt flow uudelleen, jotta voit integroida mukautetun mallin.

1. Prompt flow -työkalussa suorita seuraavat toimenpiteet rakentaaksesi olemassa olevan flown uudelleen:

    - Valitse **Raakatiedostotila**.
    - Poista kaikki olemassa oleva koodi *flow.dag.yml*-tiedostosta.
    - Lisää seuraava koodi *flow.dag.yml*-tiedostoon:

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

    - Valitse **Tallenna**.

    ![Valitse raakatiedostotila.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.fi.png)

1. Lisää seuraava koodi *integrate_with_promptflow.py*-tiedostoon käyttääksesi mukautettua Phi-3 / Phi-3.5 -mallia Prompt flow -työkalussa.

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

    ![Liitä Prompt flow -koodi.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.fi.png)

> [!NOTE]
> Lisätietoja Prompt flow -työkalun käytöstä Azure AI Foundryssä löydät [Prompt flow Azure AI Foundryssä](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valitse **Chat-tulo**, **Chat-tulos** ottaaksesi keskustelun käyttöön mallisi kanssa.

    ![Valitse tulo ja tulos.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.fi.png)

1. Nyt olet valmis keskustelemaan mukautetun Phi-3 / Phi-3.5 -mallisi kanssa. Seuraavassa harjoituksessa opit, kuinka Prompt flow käynnistetään ja miten sitä käytetään keskusteluun hienosäädetyn Phi-3 / Phi-3.5 -mallin kanssa.

> [!NOTE]
>
> Uudelleenrakennetun flown tulisi näyttää seuraavalta kuvalta:
>
> ![Flow-esimerkki](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.fi.png)
>

#### Käynnistä Prompt flow

1. Valitse **Käynnistä laskentakokoukset** käynnistääksesi Prompt flow.

    ![Käynnistä laskentakokous.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.fi.png)

1. Valitse **Vahvista ja jäsennä syöte** päivittääksesi parametrit.

    ![Vahvista syöte.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.fi.png)

1. Valitse **Yhteyden** **Arvo** mukautetulle yhteydelle, jonka loit. Esimerkiksi *connection*.

    ![Yhteys.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.fi.png)

#### Keskustele mukautetun Phi-3 / Phi-3.5 -mallisi kanssa

1. Valitse **Chat**.

    ![Valitse chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.fi.png)

1. Tässä on esimerkki tuloksista: Nyt voit keskustella mukautetun Phi-3 / Phi-3.5 -mallisi kanssa. Suositeltavaa on esittää kysymyksiä, jotka perustuvat hienosäätöön käytettyihin tietoihin.

    ![Keskustele Prompt flow -työkalulla.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.fi.png)

### Ota käyttöön Azure OpenAI arvioidaksesi Phi-3 / Phi-3.5 -mallia

Jotta voit arvioida Phi-3 / Phi-3.5 -mallia Azure AI Foundryssä, sinun täytyy ottaa käyttöön Azure OpenAI -malli. Tätä mallia käytetään Phi-3 / Phi-3.5 -mallin suorituskyvyn arviointiin.

#### Ota käyttöön Azure OpenAI

1. Kirjaudu sisään [Azure AI Foundryyn](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure AI Foundry -projektiin.

    ![Valitse projekti.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.fi.png)

1. Valitse luomassasi projektissa vasemman reunan välilehdestä **Käyttöönotot**.

1. Valitse navigointivalikosta **+ Ota malli käyttöön**.

1. Valitse **Ota perusmalli käyttöön**.

    ![Valitse käyttöönotot.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.fi.png)

1. Valitse Azure OpenAI -malli, jota haluat käyttää. Esimerkiksi **gpt-4o**.

    ![Valitse Azure OpenAI -malli.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.fi.png)

1. Valitse **Vahvista**.

### Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryn Prompt flow -arvioinnin avulla

### Aloita uusi arviointi

1. Siirry [Azure AI Foundryyn](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure AI Foundry -projektiin.

    ![Valitse projekti.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.fi.png)

1. Valitse luomassasi projektissa vasemman reunan välilehdestä **Arviointi**.

1. Valitse navigointivalikosta **+ Uusi arviointi**.
![Valitse arviointi.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.fi.png)

1. Valitse **Prompt flow** -arviointi.

    ![Valitse Prompt flow -arviointi.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.fi.png)

1. Suorita seuraavat tehtävät:

    - Syötä arvioinnin nimi. Sen täytyy olla yksilöllinen arvo.
    - Valitse **Kysymys ja vastaus ilman kontekstia** tehtävätyypiksi. Tämä johtuu siitä, että tässä opetusohjelmassa käytetty **ULTRACHAT_200k**-aineisto ei sisällä kontekstia.
    - Valitse arvioitava Prompt flow.

    ![Prompt flow -arviointi.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.fi.png)

1. Valitse **Seuraava**.

1. Suorita seuraavat tehtävät:

    - Valitse **Lisää aineistosi** ladataksesi aineiston. Voit esimerkiksi ladata testiaineistotiedoston, kuten *test_data.json1*, joka sisältyy ladattavaan **ULTRACHAT_200k**-aineistoon.
    - Valitse aineistoosi sopiva **Dataset column**. Esimerkiksi, jos käytät **ULTRACHAT_200k**-aineistoa, valitse **${data.prompt}** aineistosarakkeeksi.

    ![Prompt flow -arviointi.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.fi.png)

1. Valitse **Seuraava**.

1. Suorita seuraavat tehtävät suorituskyvyn ja laadun mittareiden määrittämiseksi:

    - Valitse suorituskyvyn ja laadun mittarit, joita haluat käyttää.
    - Valitse Azure OpenAI -malli, jonka loit arviointia varten. Esimerkiksi valitse **gpt-4o**.

    ![Prompt flow -arviointi.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.fi.png)

1. Suorita seuraavat tehtävät riskien ja turvallisuuden mittareiden määrittämiseksi:

    - Valitse riskien ja turvallisuuden mittarit, joita haluat käyttää.
    - Valitse kynnysarvo virheprosentin laskentaa varten. Esimerkiksi valitse **Keskitaso**.
    - **Kysymys**: valitse **Tietolähde** kohtaan **{$data.prompt}**.
    - **Vastaus**: valitse **Tietolähde** kohtaan **{$run.outputs.answer}**.
    - **ground_truth**: valitse **Tietolähde** kohtaan **{$data.message}**.

    ![Prompt flow -arviointi.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.fi.png)

1. Valitse **Seuraava**.

1. Valitse **Lähetä** aloittaaksesi arvioinnin.

1. Arvioinnin suorittaminen kestää hetken. Voit seurata edistymistä **Arviointi**-välilehdellä.

### Tarkastele arvioinnin tuloksia

> [!NOTE]
> Alla esitetyt tulokset on tarkoitettu havainnollistamaan arviointiprosessia. Tässä opetusohjelmassa käytetty malli on hienosäädetty suhteellisen pienellä aineistolla, mikä voi johtaa suboptimaalisiin tuloksiin. Todelliset tulokset voivat vaihdella merkittävästi aineiston koon, laadun ja monimuotoisuuden sekä mallin konfiguraation mukaan.

Kun arviointi on valmis, voit tarkastella sekä suorituskyvyn että turvallisuuden mittareiden tuloksia.

1. Suorituskyvyn ja laadun mittarit:

    - Arvioi mallin tehokkuutta tuottaa johdonmukaisia, sujuvia ja relevantteja vastauksia.

    ![Arvioinnin tulos.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.fi.png)

1. Riskien ja turvallisuuden mittarit:

    - Varmista, että mallin tuotokset ovat turvallisia ja noudattavat vastuullisen tekoälyn periaatteita, välttäen haitallista tai loukkaavaa sisältöä.

    ![Arvioinnin tulos.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.fi.png)

1. Voit selata alaspäin nähdäksesi **Yksityiskohtaiset mittaritulokset**.

    ![Arvioinnin tulos.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.fi.png)

1. Arvioimalla mukautetun Phi-3 / Phi-3.5 -mallisi sekä suorituskyvyn että turvallisuuden mittareilla voit varmistaa, että malli ei ole ainoastaan tehokas, vaan myös noudattaa vastuullisen tekoälyn käytäntöjä, mikä tekee siitä valmiin todelliseen käyttöönottoon.

## Onnittelut!

### Olet suorittanut tämän opetusohjelman

Olet onnistuneesti arvioinut hienosäädetyn Phi-3-mallin, joka on integroitu Prompt flow'hun Azure AI Foundryssa. Tämä on tärkeä askel varmistettaessa, että tekoälymallisi eivät ainoastaan suoriudu hyvin, vaan myös noudattavat Microsoftin vastuullisen tekoälyn periaatteita, auttaen sinua rakentamaan luotettavia ja vastuullisia tekoälysovelluksia.

![Arkkitehtuuri.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.fi.png)

## Poista Azure-resurssit

Poista Azure-resurssisi välttääksesi lisäkustannuksia tilillesi. Siirry Azure-portaaliin ja poista seuraavat resurssit:

- Azure Machine Learning -resurssi.
- Azure Machine Learning -mallin päätepiste.
- Azure AI Foundry -projektiresurssi.
- Azure AI Foundry Prompt flow -resurssi.

### Seuraavat vaiheet

#### Dokumentaatio

- [Tekoälyjärjestelmien arviointi vastuullisen tekoälyn hallintapaneelilla](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Generatiivisen tekoälyn arviointi- ja valvontamittarit](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry -dokumentaatio](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow -dokumentaatio](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Koulutussisältö

- [Johdatus Microsoftin vastuullisen tekoälyn lähestymistapaan](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Johdatus Azure AI Foundryyn](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Viite

- [Mitä on vastuullinen tekoäly?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Uudet työkalut Azure AI:ssa turvallisten ja luotettavien generatiivisten tekoälysovellusten rakentamiseen](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Generatiivisten tekoälysovellusten arviointi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.