# Vyhodnocení doladěného modelu Phi-3 / Phi-3.5 v Azure AI Foundry s důrazem na principy zodpovědné AI od Microsoftu

Tento komplexní příklad vychází z průvodce "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community.

## Přehled

### Jak můžete vyhodnotit bezpečnost a výkon doladěného modelu Phi-3 / Phi-3.5 v Azure AI Foundry?

Doladění modelu může někdy vést k neúmyslným nebo nežádoucím reakcím. Aby byl model bezpečný a efektivní, je důležité vyhodnotit jeho potenciál generovat škodlivý obsah a jeho schopnost vytvářet přesné, relevantní a srozumitelné odpovědi. V tomto návodu se naučíte, jak vyhodnotit bezpečnost a výkon doladěného modelu Phi-3 / Phi-3.5 integrovaného s Prompt flow v Azure AI Foundry.

Zde je proces vyhodnocení v Azure AI Foundry.

![Architektura tutoriálu.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.cs.png)

*Zdroj obrázku: [Vyhodnocení generativních AI aplikací](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pro více podrobností a další zdroje o Phi-3 / Phi-3.5 navštivte [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Požadavky

- [Python](https://www.python.org/downloads)
- [Azure předplatné](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Doladěný model Phi-3 / Phi-3.5

### Obsah

1. [**Scénář 1: Úvod do vyhodnocení Prompt flow v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Úvod do vyhodnocení bezpečnosti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Úvod do vyhodnocení výkonu](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scénář 2: Vyhodnocení modelu Phi-3 / Phi-3.5 v Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Než začnete](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasazení Azure OpenAI k vyhodnocení modelu Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Vyhodnocení doladěného modelu Phi-3 / Phi-3.5 pomocí Prompt flow v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gratulujeme!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scénář 1: Úvod do vyhodnocení Prompt flow v Azure AI Foundry**

### Úvod do vyhodnocení bezpečnosti

Aby byl váš AI model etický a bezpečný, je klíčové jej vyhodnotit podle principů zodpovědné AI od Microsoftu. V Azure AI Foundry umožňuje vyhodnocení bezpečnosti posoudit zranitelnost modelu vůči útokům typu jailbreak a jeho potenciál generovat škodlivý obsah, což přímo odpovídá těmto principům.

![Vyhodnocení bezpečnosti.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.cs.png)

*Zdroj obrázku: [Vyhodnocení generativních AI aplikací](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principy zodpovědné AI od Microsoftu

Než začnete s technickými kroky, je důležité pochopit principy zodpovědné AI od Microsoftu, což je etický rámec navržený k vedení zodpovědného vývoje, nasazení a provozu AI systémů. Tyto principy zajišťují, že AI technologie jsou navrženy tak, aby byly spravedlivé, transparentní a inkluzivní. Jsou základem pro vyhodnocení bezpečnosti AI modelů.

Principy zodpovědné AI od Microsoftu zahrnují:

- **Spravedlnost a inkluzivita**: AI systémy by měly zacházet se všemi spravedlivě a vyhnout se tomu, aby různé skupiny lidí byly ovlivněny odlišně. Například při poskytování doporučení ohledně léčby, půjček nebo zaměstnání by měly AI systémy poskytovat stejné rady lidem s podobnými symptomy, finanční situací nebo profesní kvalifikací.

- **Spolehlivost a bezpečnost**: Pro budování důvěry je zásadní, aby AI systémy fungovaly spolehlivě, bezpečně a konzistentně. Tyto systémy by měly být schopné fungovat podle původního návrhu, bezpečně reagovat na neočekávané podmínky a odolávat škodlivé manipulaci.

- **Transparentnost**: Když AI systémy pomáhají při rozhodování, které má velký dopad na životy lidí, je zásadní, aby lidé rozuměli, jak byla tato rozhodnutí učiněna.

- **Ochrana soukromí a bezpečnost**: S rostoucím využitím AI je ochrana soukromí a zabezpečení osobních a firemních informací stále důležitější a složitější.

- **Odpovědnost**: Lidé, kteří navrhují a nasazují AI systémy, musí nést odpovědnost za jejich fungování.

![Plnění zásad.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.cs.png)

*Zdroj obrázku: [Co je zodpovědná AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Další informace o principech zodpovědné AI od Microsoftu naleznete na [Co je zodpovědná AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriky bezpečnosti

V tomto návodu budete vyhodnocovat bezpečnost doladěného modelu Phi-3 pomocí metrik bezpečnosti v Azure AI Foundry. Tyto metriky pomáhají posoudit potenciál modelu generovat škodlivý obsah a jeho zranitelnost vůči útokům typu jailbreak. Metriky bezpečnosti zahrnují:

- **Obsah související s sebepoškozováním**: Posuzuje, zda má model tendenci generovat obsah související se sebepoškozováním.
- **Nenávistný a nespravedlivý obsah**: Posuzuje, zda má model tendenci generovat nenávistný nebo nespravedlivý obsah.
- **Násilný obsah**: Posuzuje, zda má model tendenci generovat násilný obsah.
- **Sexuální obsah**: Posuzuje, zda má model tendenci generovat nevhodný sexuální obsah.

Vyhodnocení těchto aspektů zajišťuje, že AI model nevytváří škodlivý nebo urážlivý obsah, což odpovídá společenským hodnotám a regulačním standardům.

![Vyhodnocení na základě bezpečnosti.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.cs.png)

### Úvod do vyhodnocení výkonu

Aby váš AI model fungoval podle očekávání, je důležité posoudit jeho výkon podle metrik výkonu. V Azure AI Foundry umožňuje vyhodnocení výkonu posoudit efektivitu modelu při generování přesných, relevantních a srozumitelných odpovědí.

![Vyhodnocení výkonu.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.cs.png)

*Zdroj obrázku: [Vyhodnocení generativních AI aplikací](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriky výkonu

V tomto návodu budete vyhodnocovat výkon doladěného modelu Phi-3 / Phi-3.5 pomocí metrik výkonu v Azure AI Foundry. Tyto metriky pomáhají posoudit efektivitu modelu při generování přesných, relevantních a srozumitelných odpovědí. Metriky výkonu zahrnují:

- **Opodstatněnost**: Posuzuje, jak dobře odpovědi odpovídají informacím ze vstupního zdroje.
- **Relevance**: Posuzuje, jak relevantní jsou generované odpovědi k daným otázkám.
- **Koherence**: Posuzuje, jak plynule generovaný text plyne, čte se přirozeně a připomíná lidský jazyk.
- **Plynulost**: Posuzuje jazykovou úroveň generovaného textu.
- **Podobnost s GPT**: Porovnává generovanou odpověď se správnou odpovědí pro podobnost.
- **F1 skóre**: Vypočítává poměr sdílených slov mezi generovanou odpovědí a zdrojovými daty.

Tyto metriky pomáhají posoudit efektivitu modelu při generování přesných, relevantních a srozumitelných odpovědí.

![Vyhodnocení na základě výkonu.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.cs.png)

## **Scénář 2: Vyhodnocení modelu Phi-3 / Phi-3.5 v Azure AI Foundry**

### Než začnete

Tento návod navazuje na předchozí příspěvky na blogu, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" a "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." V těchto příspěvcích jsme prošli procesem doladění modelu Phi-3 / Phi-3.5 v Azure AI Foundry a jeho integrací s Prompt flow.

V tomto návodu nasadíte model Azure OpenAI jako hodnotitele v Azure AI Foundry a použijete jej k vyhodnocení vašeho doladěného modelu Phi-3 / Phi-3.5.

Než začnete s tímto návodem, ujistěte se, že máte následující požadavky, jak je popsáno v předchozích návodech:

1. Připravenou datovou sadu pro vyhodnocení doladěného modelu Phi-3 / Phi-3.5.
1. Doladěný model Phi-3 / Phi-3.5, který byl nasazen do Azure Machine Learning.
1. Prompt flow integrovaný s vaším doladěným modelem Phi-3 / Phi-3.5 v Azure AI Foundry.

> [!NOTE]
> Použijete soubor *test_data.jsonl*, který se nachází ve složce data z datové sady **ULTRACHAT_200k** stažené v předchozích příspěvcích na blogu, jako datovou sadu pro vyhodnocení doladěného modelu Phi-3 / Phi-3.5.

#### Integrace vlastního modelu Phi-3 / Phi-3.5 s Prompt flow v Azure AI Foundry (přístup založený na kódu)

> [!NOTE]
> Pokud jste postupovali podle přístupu s nízkým kódem popsaného v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", můžete tuto část přeskočit a pokračovat k další.
> Pokud jste však postupovali podle přístupu založeného na kódu popsaného v "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", proces připojení vašeho modelu k Prompt flow se mírně liší. Tento proces se naučíte v této části.

Chcete-li pokračovat, musíte integrovat svůj doladěný model Phi-3 / Phi-3.5 do Prompt flow v Azure AI Foundry.

#### Vytvoření hubu v Azure AI Foundry

Než vytvoříte projekt, musíte vytvořit hub. Hub funguje jako skupina prostředků, která vám umožňuje organizovat a spravovat více projektů v Azure AI Foundry.

1. Přihlaste se do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Zvolte **Všechny huby** v levém panelu.

1. Klikněte na **+ Nový hub** v navigačním menu.

    ![Vytvoření hubu.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.cs.png)

1. Proveďte následující úkoly:

    - Zadejte **Název hubu**. Musí být unikátní.
    - Vyberte své Azure **Předplatné**.
    - Zvolte **Skupinu prostředků**, kterou chcete použít (vytvořte novou, pokud je potřeba).
    - Vyberte **Umístění**, které chcete použít.
    - Zvolte **Připojit Azure AI Services**, které chcete použít (vytvořte nové, pokud je potřeba).
    - Vyberte **Připojit Azure AI Search** a zvolte **Přeskočit připojení**.
![Vyplňte hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.cs.png)

1. Vyberte **Next**.

#### Vytvoření projektu Azure AI Foundry

1. V Hubu, který jste vytvořili, vyberte **All projects** z levého postranního panelu.

1. Vyberte **+ New project** z navigačního menu.

    ![Vyberte nový projekt.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.cs.png)

1. Zadejte **Project name**. Musí se jednat o jedinečnou hodnotu.

    ![Vytvoření projektu.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.cs.png)

1. Vyberte **Create a project**.

#### Přidání vlastního připojení pro jemně doladěný model Phi-3 / Phi-3.5

Pro integraci vlastního modelu Phi-3 / Phi-3.5 s Prompt flow je nutné uložit endpoint modelu a klíč do vlastního připojení. Tato konfigurace zajišťuje přístup k vašemu vlastnímu modelu Phi-3 / Phi-3.5 v Prompt flow.

#### Nastavení api klíče a endpoint uri pro jemně doladěný model Phi-3 / Phi-3.5

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Přejděte do prostoru Azure Machine Learning, který jste vytvořili.

1. Vyberte **Endpoints** z levého postranního panelu.

    ![Vyberte endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.cs.png)

1. Vyberte endpoint, který jste vytvořili.

    ![Vyberte vytvořený endpoint.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.cs.png)

1. Vyberte **Consume** z navigačního menu.

1. Zkopírujte váš **REST endpoint** a **Primary key**.

    ![Zkopírujte api klíč a endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.cs.png)

#### Přidání vlastního připojení

1. Navštivte [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do projektu Azure AI Foundry, který jste vytvořili.

1. V projektu, který jste vytvořili, vyberte **Settings** z levého postranního panelu.

1. Vyberte **+ New connection**.

    ![Vyberte nové připojení.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.cs.png)

1. Vyberte **Custom keys** z navigačního menu.

    ![Vyberte vlastní klíče.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.cs.png)

1. Proveďte následující kroky:

    - Vyberte **+ Add key value pairs**.
    - Pro název klíče zadejte **endpoint** a vložte endpoint, který jste zkopírovali z Azure ML Studio, do pole pro hodnotu.
    - Znovu vyberte **+ Add key value pairs**.
    - Pro název klíče zadejte **key** a vložte klíč, který jste zkopírovali z Azure ML Studio, do pole pro hodnotu.
    - Po přidání klíčů vyberte **is secret**, aby byl klíč chráněn před zobrazením.

    ![Přidání připojení.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.cs.png)

1. Vyberte **Add connection**.

#### Vytvoření Prompt flow

Přidali jste vlastní připojení v Azure AI Foundry. Nyní vytvoříme Prompt flow pomocí následujících kroků. Poté toto Prompt flow připojíte k vlastnímu připojení, abyste mohli používat jemně doladěný model v Prompt flow.

1. Přejděte do projektu Azure AI Foundry, který jste vytvořili.

1. Vyberte **Prompt flow** z levého postranního panelu.

1. Vyberte **+ Create** z navigačního menu.

    ![Vyberte Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.cs.png)

1. Vyberte **Chat flow** z navigačního menu.

    ![Vyberte chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.cs.png)

1. Zadejte **Folder name**, který chcete použít.

    ![Zadejte název složky.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.cs.png)

1. Vyberte **Create**.

#### Nastavení Prompt flow pro chat s vlastním modelem Phi-3 / Phi-3.5

Musíte integrovat jemně doladěný model Phi-3 / Phi-3.5 do Prompt flow. Stávající Prompt flow však není pro tento účel navržen. Proto musíte Prompt flow přepracovat, aby umožňoval integraci vlastního modelu.

1. V Prompt flow proveďte následující kroky pro přestavbu stávajícího flow:

    - Vyberte **Raw file mode**.
    - Smažte veškerý stávající kód v souboru *flow.dag.yml*.
    - Přidejte následující kód do *flow.dag.yml*.

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

    - Vyberte **Save**.

    ![Vyberte režim raw souboru.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.cs.png)

1. Přidejte následující kód do *integrate_with_promptflow.py* pro použití vlastního modelu Phi-3 / Phi-3.5 v Prompt flow.

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

    ![Vložte kód Prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.cs.png)

> [!NOTE]
> Pro podrobnější informace o použití Prompt flow v Azure AI Foundry můžete navštívit [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output**, abyste mohli chatovat se svým modelem.

    ![Vyberte Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.cs.png)

1. Nyní jste připraveni chatovat se svým vlastním modelem Phi-3 / Phi-3.5. V dalším cvičení se naučíte, jak spustit Prompt flow a používat ho k chatu s jemně doladěným modelem Phi-3 / Phi-3.5.

> [!NOTE]
>
> Přepracované flow by mělo vypadat jako na obrázku níže:
>
> ![Příklad flow](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.cs.png)
>

#### Spuštění Prompt flow

1. Vyberte **Start compute sessions** pro spuštění Prompt flow.

    ![Spusťte výpočetní relaci.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.cs.png)

1. Vyberte **Validate and parse input** pro obnovení parametrů.

    ![Validujte vstup.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.cs.png)

1. Vyberte **Value** připojení k vlastnímu připojení, které jste vytvořili. Například *connection*.

    ![Připojení.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.cs.png)

#### Chat s vlastním modelem Phi-3 / Phi-3.5

1. Vyberte **Chat**.

    ![Vyberte chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.cs.png)

1. Zde je příklad výsledků: Nyní můžete chatovat se svým vlastním modelem Phi-3 / Phi-3.5. Doporučuje se klást otázky založené na datech použitých pro jemné doladění.

    ![Chat s Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.cs.png)

### Nasazení Azure OpenAI pro hodnocení modelu Phi-3 / Phi-3.5

Pro hodnocení modelu Phi-3 / Phi-3.5 v Azure AI Foundry je nutné nasadit model Azure OpenAI. Tento model bude použit k hodnocení výkonu modelu Phi-3 / Phi-3.5.

#### Nasazení Azure OpenAI

1. Přihlaste se do [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do projektu Azure AI Foundry, který jste vytvořili.

    ![Vyberte projekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.cs.png)

1. V projektu, který jste vytvořili, vyberte **Deployments** z levého postranního panelu.

1. Vyberte **+ Deploy model** z navigačního menu.

1. Vyberte **Deploy base model**.

    ![Vyberte nasazení.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.cs.png)

1. Vyberte model Azure OpenAI, který chcete použít. Například **gpt-4o**.

    ![Vyberte model Azure OpenAI.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.cs.png)

1. Vyberte **Confirm**.

### Hodnocení jemně doladěného modelu Phi-3 / Phi-3.5 pomocí evaluace Prompt flow v Azure AI Foundry

### Spuštění nové evaluace

1. Navštivte [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Přejděte do projektu Azure AI Foundry, který jste vytvořili.

    ![Vyberte projekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.cs.png)

1. V projektu, který jste vytvořili, vyberte **Evaluation** z levého postranního panelu.

1. Vyberte **+ New evaluation** z navigačního menu.
![Vyberte hodnocení.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.cs.png)

1. Vyberte hodnocení **Prompt flow**.

    ![Vyberte hodnocení Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.cs.png)

1. Proveďte následující kroky:

    - Zadejte název hodnocení. Musí být unikátní.
    - Vyberte **Otázka a odpověď bez kontextu** jako typ úlohy. Důvodem je, že dataset **ULTRACHAT_200k** použitý v tomto tutoriálu neobsahuje kontext.
    - Vyberte Prompt flow, který chcete hodnotit.

    ![Hodnocení Prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.cs.png)

1. Vyberte **Next**.

1. Proveďte následující kroky:

    - Vyberte **Add your dataset** pro nahrání datasetu. Například můžete nahrát testovací soubor datasetu, jako je *test_data.json1*, který je součástí staženého datasetu **ULTRACHAT_200k**.
    - Vyberte odpovídající **Sloupec datasetu**, který odpovídá vašemu datasetu. Například, pokud používáte dataset **ULTRACHAT_200k**, vyberte **${data.prompt}** jako sloupec datasetu.

    ![Hodnocení Prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.cs.png)

1. Vyberte **Next**.

1. Proveďte následující kroky pro nastavení metrik výkonu a kvality:

    - Vyberte metriky výkonu a kvality, které chcete použít.
    - Vyberte model Azure OpenAI, který jste vytvořili pro hodnocení. Například vyberte **gpt-4o**.

    ![Hodnocení Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.cs.png)

1. Proveďte následující kroky pro nastavení metrik rizik a bezpečnosti:

    - Vyberte metriky rizik a bezpečnosti, které chcete použít.
    - Vyberte práh pro výpočet míry defektů, který chcete použít. Například vyberte **Střední**.
    - Pro **question** vyberte **Zdroj dat** jako **{$data.prompt}**.
    - Pro **answer** vyberte **Zdroj dat** jako **{$run.outputs.answer}**.
    - Pro **ground_truth** vyberte **Zdroj dat** jako **{$data.message}**.

    ![Hodnocení Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.cs.png)

1. Vyberte **Next**.

1. Vyberte **Submit** pro spuštění hodnocení.

1. Hodnocení bude chvíli trvat. Pokrok můžete sledovat na záložce **Evaluation**.

### Prohlédněte si výsledky hodnocení

> [!NOTE]
> Výsledky uvedené níže slouží k ilustraci procesu hodnocení. V tomto tutoriálu jsme použili model doladěný na relativně malém datasetu, což může vést k suboptimálním výsledkům. Skutečné výsledky se mohou výrazně lišit v závislosti na velikosti, kvalitě a rozmanitosti použitého datasetu, stejně jako na konkrétní konfiguraci modelu.

Po dokončení hodnocení si můžete prohlédnout výsledky jak pro metriky výkonu, tak pro metriky bezpečnosti.

1. Metriky výkonu a kvality:

    - Vyhodnoťte efektivitu modelu při generování koherentních, plynulých a relevantních odpovědí.

    ![Výsledek hodnocení.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.cs.png)

1. Metriky rizik a bezpečnosti:

    - Ujistěte se, že výstupy modelu jsou bezpečné a odpovídají principům odpovědné AI, přičemž se vyhýbají jakémukoliv škodlivému nebo urážlivému obsahu.

    ![Výsledek hodnocení.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.cs.png)

1. Můžete sjet dolů a zobrazit **Podrobné výsledky metrik**.

    ![Výsledek hodnocení.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.cs.png)

1. Hodnocením vašeho vlastního modelu Phi-3 / Phi-3.5 podle metrik výkonu i bezpečnosti můžete potvrdit, že model je nejen efektivní, ale také splňuje zásady odpovědné AI, což jej činí připraveným pro nasazení v reálném světě.

## Gratulujeme!

### Dokončili jste tento tutoriál

Úspěšně jste zhodnotili doladěný model Phi-3 integrovaný s Prompt flow v Azure AI Foundry. Toto je důležitý krok k zajištění toho, že vaše AI modely nejen dobře fungují, ale také splňují principy odpovědné AI společnosti Microsoft, což vám pomůže vytvářet důvěryhodné a spolehlivé AI aplikace.

![Architektura.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.cs.png)

## Vyčištění Azure prostředků

Vyčistěte své Azure prostředky, abyste předešli dalším poplatkům na vašem účtu. Přejděte do Azure portálu a smažte následující prostředky:

- Prostředek Azure Machine Learning.
- Koncový bod modelu Azure Machine Learning.
- Prostředek projektu Azure AI Foundry.
- Prostředek Prompt flow v Azure AI Foundry.

### Další kroky

#### Dokumentace

- [Hodnocení AI systémů pomocí panelu odpovědné AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Hodnocení a monitorovací metriky pro generativní AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentace Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentace Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Výukový obsah

- [Úvod k odpovědnému AI přístupu společnosti Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Úvod do Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [Co je odpovědná AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Oznámení nových nástrojů v Azure AI pro vytváření bezpečnějších a důvěryhodnějších generativních AI aplikací](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Hodnocení generativních AI aplikací](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese zodpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.