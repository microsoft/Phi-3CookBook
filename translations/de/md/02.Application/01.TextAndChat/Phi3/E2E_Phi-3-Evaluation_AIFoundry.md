# Evaluieren des Feinabgestimmten Phi-3 / Phi-3.5 Modells in Azure AI Foundry im Fokus auf Microsofts Prinzipien für Verantwortungsvolle KI

Dieses End-to-End (E2E) Beispiel basiert auf der Anleitung "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" aus der Microsoft Tech Community.

## Überblick

### Wie können Sie die Sicherheit und Leistung eines feinabgestimmten Phi-3 / Phi-3.5 Modells in Azure AI Foundry bewerten?

Das Feinabstimmen eines Modells kann manchmal zu unbeabsichtigten oder unerwünschten Antworten führen. Um sicherzustellen, dass das Modell sicher und effektiv bleibt, ist es wichtig, das Potenzial des Modells zur Erzeugung schädlicher Inhalte sowie seine Fähigkeit zur Erstellung genauer, relevanter und kohärenter Antworten zu bewerten. In diesem Tutorial lernen Sie, wie Sie die Sicherheit und Leistung eines feinabgestimmten Phi-3 / Phi-3.5 Modells bewerten, das in Azure AI Foundry mit Prompt flow integriert ist.

Hier ist der Bewertungsprozess von Azure AI Foundry.

![Architektur des Tutorials.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.de.png)

*Bildquelle: [Bewertung generativer KI-Anwendungen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Für detailliertere Informationen und zusätzliche Ressourcen zu Phi-3 / Phi-3.5 besuchen Sie bitte das [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Voraussetzungen

- [Python](https://www.python.org/downloads)
- [Azure-Abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Feinabgestimmtes Phi-3 / Phi-3.5 Modell

### Inhaltsverzeichnis

1. [**Szenario 1: Einführung in die Bewertung mit Azure AI Foundry's Prompt flow**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Einführung in die Sicherheitsbewertung](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Einführung in die Leistungsbewertung](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Szenario 2: Bewertung des Phi-3 / Phi-3.5 Modells in Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Vorbereitungen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Bereitstellen von Azure OpenAI zur Bewertung des Phi-3 / Phi-3.5 Modells](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells mit Azure AI Foundry's Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Glückwunsch!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Szenario 1: Einführung in die Bewertung mit Azure AI Foundry's Prompt flow**

### Einführung in die Sicherheitsbewertung

Um sicherzustellen, dass Ihr KI-Modell ethisch und sicher ist, ist es entscheidend, es anhand von Microsofts Prinzipien für Verantwortungsvolle KI zu bewerten. In Azure AI Foundry ermöglichen Sicherheitsbewertungen die Überprüfung der Anfälligkeit Ihres Modells gegenüber Jailbreak-Angriffen und seines Potenzials zur Erzeugung schädlicher Inhalte, was direkt mit diesen Prinzipien übereinstimmt.

![Sicherheitsbewertung.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.de.png)

*Bildquelle: [Bewertung generativer KI-Anwendungen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts Prinzipien für Verantwortungsvolle KI

Bevor Sie mit den technischen Schritten beginnen, ist es wichtig, die Prinzipien für Verantwortungsvolle KI von Microsoft zu verstehen – ein ethisches Rahmenwerk, das die verantwortungsvolle Entwicklung, Bereitstellung und den Betrieb von KI-Systemen leitet. Diese Prinzipien gewährleisten, dass KI-Technologien fair, transparent und inklusiv gestaltet werden. Sie bilden die Grundlage für die Bewertung der Sicherheit von KI-Modellen.

Microsofts Prinzipien für Verantwortungsvolle KI umfassen:

- **Fairness und Inklusivität**: KI-Systeme sollten alle fair behandeln und vermeiden, ähnlich situierte Gruppen unterschiedlich zu behandeln. Beispielsweise sollten KI-Systeme bei medizinischen Behandlungsanweisungen, Kreditanträgen oder Bewerbungen die gleichen Empfehlungen für Personen mit ähnlichen Symptomen, finanziellen Verhältnissen oder beruflichen Qualifikationen geben.

- **Zuverlässigkeit und Sicherheit**: Um Vertrauen aufzubauen, ist es entscheidend, dass KI-Systeme zuverlässig, sicher und konsistent arbeiten. Diese Systeme sollten so funktionieren, wie sie ursprünglich entworfen wurden, sicher auf unvorhergesehene Bedingungen reagieren und schädlicher Manipulation widerstehen können. Ihr Verhalten und die Vielzahl der Bedingungen, die sie bewältigen können, spiegeln die Situationen wider, die Entwickler während Design und Tests erwartet haben.

- **Transparenz**: Wenn KI-Systeme Entscheidungen beeinflussen, die erhebliche Auswirkungen auf das Leben von Menschen haben, ist es entscheidend, dass Menschen verstehen, wie diese Entscheidungen getroffen wurden. Zum Beispiel könnte eine Bank ein KI-System verwenden, um die Kreditwürdigkeit einer Person zu beurteilen. Ein Unternehmen könnte ein KI-System einsetzen, um die am besten qualifizierten Bewerber auszuwählen.

- **Datenschutz und Sicherheit**: Mit der zunehmenden Verbreitung von KI wird der Schutz der Privatsphäre und die Sicherung persönlicher und geschäftlicher Informationen immer wichtiger und komplexer. Datenschutz und Datensicherheit erfordern besondere Aufmerksamkeit, da der Zugang zu Daten essenziell ist, damit KI-Systeme genaue und fundierte Vorhersagen und Entscheidungen über Menschen treffen können.

- **Verantwortlichkeit**: Die Personen, die KI-Systeme entwerfen und bereitstellen, müssen für deren Funktionsweise verantwortlich sein. Organisationen sollten auf Branchenstandards zurückgreifen, um Verantwortungsnormen zu entwickeln. Diese Normen können sicherstellen, dass KI-Systeme keine endgültige Autorität bei Entscheidungen haben, die das Leben von Menschen betreffen. Sie können auch sicherstellen, dass Menschen die Kontrolle über hochautonome KI-Systeme behalten.

![Füll-Hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.de.png)

*Bildquelle: [Was ist Verantwortungsvolle KI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Um mehr über Microsofts Prinzipien für Verantwortungsvolle KI zu erfahren, besuchen Sie [Was ist Verantwortungsvolle KI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sicherheitsmetriken

In diesem Tutorial bewerten Sie die Sicherheit des feinabgestimmten Phi-3 Modells mit den Sicherheitsmetriken von Azure AI Foundry. Diese Metriken helfen Ihnen, das Potenzial des Modells zur Erzeugung schädlicher Inhalte und seine Anfälligkeit gegenüber Jailbreak-Angriffen zu bewerten. Die Sicherheitsmetriken umfassen:

- **Inhalte zu Selbstverletzung**: Bewertet, ob das Modell eine Tendenz hat, Inhalte zu Selbstverletzung zu erzeugen.
- **Hasserfüllte und unfaire Inhalte**: Bewertet, ob das Modell eine Tendenz hat, hasserfüllte oder unfaire Inhalte zu erzeugen.
- **Gewalttätige Inhalte**: Bewertet, ob das Modell eine Tendenz hat, gewalttätige Inhalte zu erzeugen.
- **Sexuelle Inhalte**: Bewertet, ob das Modell eine Tendenz hat, unangemessene sexuelle Inhalte zu erzeugen.

Die Bewertung dieser Aspekte stellt sicher, dass das KI-Modell keine schädlichen oder anstößigen Inhalte erzeugt und mit gesellschaftlichen Werten sowie regulatorischen Standards übereinstimmt.

![Bewertung basierend auf Sicherheit.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.de.png)

### Einführung in die Leistungsbewertung

Um sicherzustellen, dass Ihr KI-Modell wie erwartet funktioniert, ist es wichtig, seine Leistung anhand von Leistungsmetriken zu bewerten. In Azure AI Foundry ermöglichen Leistungsbewertungen die Überprüfung der Effektivität Ihres Modells bei der Generierung genauer, relevanter und kohärenter Antworten.

![Sicherheitsbewertung.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.de.png)

*Bildquelle: [Bewertung generativer KI-Anwendungen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Leistungsmetriken

In diesem Tutorial bewerten Sie die Leistung des feinabgestimmten Phi-3 / Phi-3.5 Modells mit den Leistungsmetriken von Azure AI Foundry. Diese Metriken helfen Ihnen, die Effektivität des Modells bei der Generierung genauer, relevanter und kohärenter Antworten zu bewerten. Die Leistungsmetriken umfassen:

- **Fundierung**: Bewertet, wie gut die generierten Antworten mit den Informationen aus der Eingabequelle übereinstimmen.
- **Relevanz**: Bewertet die Relevanz der generierten Antworten zu den gestellten Fragen.
- **Kohärenz**: Bewertet, wie flüssig der generierte Text ist, ob er natürlich klingt und menschenähnlicher Sprache ähnelt.
- **Flüssigkeit**: Bewertet die sprachliche Kompetenz des generierten Textes.
- **GPT-Ähnlichkeit**: Vergleicht die generierte Antwort mit der Grundwahrheit auf Ähnlichkeit.
- **F1-Wert**: Berechnet das Verhältnis der gemeinsamen Wörter zwischen der generierten Antwort und den Quelldaten.

Diese Metriken helfen Ihnen, die Effektivität des Modells bei der Generierung genauer, relevanter und kohärenter Antworten zu bewerten.

![Bewertung basierend auf Leistung.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.de.png)

## **Szenario 2: Bewertung des Phi-3 / Phi-3.5 Modells in Azure AI Foundry**

### Vorbereitungen

Dieses Tutorial baut auf den vorherigen Blogbeiträgen auf, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" und "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In diesen Beiträgen haben wir den Prozess der Feinabstimmung eines Phi-3 / Phi-3.5 Modells in Azure AI Foundry und der Integration in Prompt flow durchlaufen.

In diesem Tutorial werden Sie ein Azure OpenAI Modell als Evaluator in Azure AI Foundry bereitstellen und es zur Bewertung Ihres feinabgestimmten Phi-3 / Phi-3.5 Modells verwenden.

Bevor Sie mit diesem Tutorial beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen aus den vorherigen Tutorials erfüllt haben:

1. Einen vorbereiteten Datensatz zur Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells.
1. Ein Phi-3 / Phi-3.5 Modell, das feinabgestimmt und in Azure Machine Learning bereitgestellt wurde.
1. Einen Prompt flow, der mit Ihrem feinabgestimmten Phi-3 / Phi-3.5 Modell in Azure AI Foundry integriert ist.

> [!NOTE]
> Sie verwenden die Datei *test_data.jsonl*, die sich im Datenordner des **ULTRACHAT_200k** Datensatzes befindet, der in den vorherigen Blogbeiträgen heruntergeladen wurde, als Datensatz zur Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells.

#### Integration des benutzerdefinierten Phi-3 / Phi-3.5 Modells mit Prompt flow in Azure AI Foundry (Code-First-Ansatz)

> [!NOTE]
> Wenn Sie dem Low-Code-Ansatz gefolgt sind, der in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" beschrieben ist, können Sie diese Übung überspringen und zur nächsten übergehen.
> Wenn Sie jedoch dem Code-First-Ansatz gefolgt sind, der in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" beschrieben ist, um Ihr Phi-3 / Phi-3.5 Modell feinabzustimmen und bereitzustellen, ist der Prozess zur Verbindung Ihres Modells mit Prompt flow leicht unterschiedlich. Sie lernen diesen Prozess in dieser Übung kennen.

Um fortzufahren, müssen Sie Ihr feinabgestimmtes Phi-3 / Phi-3.5 Modell in Prompt flow in Azure AI Foundry integrieren.

#### Erstellen eines Azure AI Foundry Hubs

Sie müssen einen Hub erstellen, bevor Sie ein Projekt erstellen können. Ein Hub funktioniert wie eine Ressourcengruppe, mit der Sie mehrere Projekte in Azure AI Foundry organisieren und verwalten können.

1. Melden Sie sich bei [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) an.

1. Wählen Sie **Alle Hubs** aus der linken Seitenleiste.

1. Wählen Sie **+ Neuer Hub** aus dem Navigationsmenü.

    ![Hub erstellen.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Geben Sie **Hub-Name** ein. Es muss ein eindeutiger Wert sein.
    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe**, die Sie verwenden möchten (erstellen Sie eine neue, falls erforderlich).
    - Wählen Sie den **Standort**, den Sie verwenden möchten.
    - Wählen Sie **Azure AI Services verbinden** aus (erstellen Sie einen neuen, falls erforderlich).
    - Wählen Sie **Azure AI Search verbinden** und **Überspringen** aus.
![Hub ausfüllen.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.de.png)

1. Wählen Sie **Weiter**.

#### Erstellen eines Azure AI Foundry-Projekts

1. Wählen Sie im erstellten Hub **Alle Projekte** aus der linken Seitenleiste.

1. Wählen Sie **+ Neues Projekt** aus dem Navigationsmenü.

    ![Neues Projekt auswählen.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.de.png)

1. Geben Sie **Projektname** ein. Dieser muss einzigartig sein.

    ![Projekt erstellen.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.de.png)

1. Wählen Sie **Projekt erstellen**.

#### Hinzufügen einer benutzerdefinierten Verbindung für das feinabgestimmte Phi-3 / Phi-3.5-Modell

Um Ihr benutzerdefiniertes Phi-3 / Phi-3.5-Modell mit Prompt Flow zu integrieren, müssen Sie den Endpunkt und den Schlüssel des Modells in einer benutzerdefinierten Verbindung speichern. Diese Einrichtung ermöglicht den Zugriff auf Ihr benutzerdefiniertes Phi-3 / Phi-3.5-Modell in Prompt Flow.

#### Festlegen des API-Schlüssels und der Endpunkt-URI des feinabgestimmten Phi-3 / Phi-3.5-Modells

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigieren Sie zum erstellten Azure Machine Learning-Arbeitsbereich.

1. Wählen Sie **Endpunkte** aus der linken Seitenleiste.

    ![Endpunkte auswählen.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.de.png)

1. Wählen Sie den erstellten Endpunkt aus.

    ![Erstellten Endpunkt auswählen.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.de.png)

1. Wählen Sie **Verbrauchen** aus dem Navigationsmenü.

1. Kopieren Sie Ihren **REST-Endpunkt** und den **Primärschlüssel**.

    ![API-Schlüssel und Endpunkt-URI kopieren.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.de.png)

#### Benutzerdefinierte Verbindung hinzufügen

1. Besuchen Sie [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigieren Sie zum erstellten Azure AI Foundry-Projekt.

1. Wählen Sie im erstellten Projekt **Einstellungen** aus der linken Seitenleiste.

1. Wählen Sie **+ Neue Verbindung**.

    ![Neue Verbindung auswählen.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.de.png)

1. Wählen Sie **Benutzerdefinierte Schlüssel** aus dem Navigationsmenü.

    ![Benutzerdefinierte Schlüssel auswählen.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie **+ Schlüssel-Wert-Paare hinzufügen**.
    - Geben Sie für den Schlüsselname **endpoint** ein und fügen Sie den aus Azure ML Studio kopierten Endpunkt in das Wertfeld ein.
    - Wählen Sie erneut **+ Schlüssel-Wert-Paare hinzufügen**.
    - Geben Sie für den Schlüsselname **key** ein und fügen Sie den aus Azure ML Studio kopierten Schlüssel in das Wertfeld ein.
    - Nachdem Sie die Schlüssel hinzugefügt haben, wählen Sie **ist geheim**, um den Schlüssel vor einer Offenlegung zu schützen.

    ![Verbindung hinzufügen.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.de.png)

1. Wählen Sie **Verbindung hinzufügen**.

#### Prompt Flow erstellen

Sie haben eine benutzerdefinierte Verbindung in Azure AI Foundry hinzugefügt. Nun erstellen wir einen Prompt Flow anhand der folgenden Schritte. Anschließend verbinden Sie diesen Prompt Flow mit der benutzerdefinierten Verbindung, um das feinabgestimmte Modell im Prompt Flow zu verwenden.

1. Navigieren Sie zum erstellten Azure AI Foundry-Projekt.

1. Wählen Sie **Prompt Flow** aus der linken Seitenleiste.

1. Wählen Sie **+ Erstellen** aus dem Navigationsmenü.

    ![Prompt Flow auswählen.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.de.png)

1. Wählen Sie **Chat Flow** aus dem Navigationsmenü.

    ![Chat Flow auswählen.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.de.png)

1. Geben Sie **Ordnername** ein.

    ![Chat Flow auswählen.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.de.png)

1. Wählen Sie **Erstellen**.

#### Prompt Flow einrichten, um mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5-Modell zu chatten

Sie müssen das feinabgestimmte Phi-3 / Phi-3.5-Modell in einen Prompt Flow integrieren. Der bestehende Prompt Flow ist jedoch nicht für diesen Zweck ausgelegt. Daher müssen Sie den Prompt Flow neu entwerfen, um die Integration des benutzerdefinierten Modells zu ermöglichen.

1. Führen Sie im Prompt Flow die folgenden Schritte aus, um den bestehenden Flow neu zu erstellen:

    - Wählen Sie **Rohdateimodus**.
    - Löschen Sie den gesamten vorhandenen Code in der Datei *flow.dag.yml*.
    - Fügen Sie den folgenden Code in *flow.dag.yml* ein.

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

    - Wählen Sie **Speichern**.

    ![Rohdateimodus auswählen.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.de.png)

1. Fügen Sie den folgenden Code in *integrate_with_promptflow.py* ein, um das benutzerdefinierte Phi-3 / Phi-3.5-Modell im Prompt Flow zu verwenden.

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

    ![Prompt Flow Code einfügen.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.de.png)

> [!NOTE]
> Weitere Informationen zur Verwendung von Prompt Flow in Azure AI Foundry finden Sie unter [Prompt Flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Wählen Sie **Chat-Eingabe**, **Chat-Ausgabe**, um den Chat mit Ihrem Modell zu aktivieren.

    ![Eingabe und Ausgabe auswählen.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.de.png)

1. Nun können Sie mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5-Modell chatten. Im nächsten Abschnitt lernen Sie, wie Sie Prompt Flow starten und es zum Chatten mit Ihrem feinabgestimmten Phi-3 / Phi-3.5-Modell verwenden.

> [!NOTE]
>
> Der neu gestaltete Flow sollte wie das folgende Bild aussehen:
>
> ![Flow-Beispiel](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.de.png)
>

#### Prompt Flow starten

1. Wählen Sie **Compute-Sitzungen starten**, um Prompt Flow zu starten.

    ![Compute-Sitzung starten.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.de.png)

1. Wählen Sie **Eingabe validieren und analysieren**, um die Parameter zu erneuern.

    ![Eingabe validieren.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.de.png)

1. Wählen Sie den **Wert** der **Verbindung**, die Sie erstellt haben. Zum Beispiel *connection*.

    ![Verbindung auswählen.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.de.png)

#### Chat mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5-Modell

1. Wählen Sie **Chat**.

    ![Chat auswählen.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.de.png)

1. Hier ist ein Beispiel für die Ergebnisse: Jetzt können Sie mit Ihrem benutzerdefinierten Phi-3 / Phi-3.5-Modell chatten. Es wird empfohlen, Fragen basierend auf den Daten zu stellen, die für das Fein-Tuning verwendet wurden.

    ![Chat mit Prompt Flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.de.png)

### Azure OpenAI bereitstellen, um das Phi-3 / Phi-3.5-Modell zu evaluieren

Um das Phi-3 / Phi-3.5-Modell in Azure AI Foundry zu evaluieren, müssen Sie ein Azure OpenAI-Modell bereitstellen. Dieses Modell wird verwendet, um die Leistung des Phi-3 / Phi-3.5-Modells zu bewerten.

#### Azure OpenAI bereitstellen

1. Melden Sie sich bei [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) an.

1. Navigieren Sie zum erstellten Azure AI Foundry-Projekt.

    ![Projekt auswählen.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.de.png)

1. Wählen Sie im erstellten Projekt **Bereitstellungen** aus der linken Seitenleiste.

1. Wählen Sie **+ Modell bereitstellen** aus dem Navigationsmenü.

1. Wählen Sie **Basis-Modell bereitstellen**.

    ![Bereitstellungen auswählen.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.de.png)

1. Wählen Sie das Azure OpenAI-Modell, das Sie verwenden möchten. Zum Beispiel **gpt-4o**.

    ![Azure OpenAI-Modell auswählen.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.de.png)

1. Wählen Sie **Bestätigen**.

### Das feinabgestimmte Phi-3 / Phi-3.5-Modell mit Azure AI Foundry's Prompt Flow Evaluation bewerten

### Neue Evaluation starten

1. Besuchen Sie [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigieren Sie zum erstellten Azure AI Foundry-Projekt.

    ![Projekt auswählen.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.de.png)

1. Wählen Sie im erstellten Projekt **Evaluation** aus der linken Seitenleiste.

1. Wählen Sie **+ Neue Evaluation** aus dem Navigationsmenü.
![Bewertung auswählen.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.de.png)

1. Wählen Sie die Bewertung **Prompt flow** aus.

    ![Prompt flow Bewertung auswählen.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Geben Sie den Namen der Bewertung ein. Dieser muss eindeutig sein.
    - Wählen Sie **Frage und Antwort ohne Kontext** als Aufgabentyp aus, da das in diesem Tutorial verwendete **ULTRACHAT_200k**-Datenset keinen Kontext enthält.
    - Wählen Sie den Prompt flow aus, den Sie bewerten möchten.

    ![Prompt flow Bewertung.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.de.png)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie **Ihr Dataset hinzufügen**, um das Dataset hochzuladen. Zum Beispiel können Sie die Test-Datensatzdatei wie *test_data.json1* hochladen, die im **ULTRACHAT_200k**-Datenset enthalten ist.
    - Wählen Sie die passende **Dataset-Spalte**, die zu Ihrem Dataset passt. Zum Beispiel, wenn Sie das **ULTRACHAT_200k**-Datenset verwenden, wählen Sie **${data.prompt}** als Dataset-Spalte.

    ![Prompt flow Bewertung.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.de.png)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Schritte aus, um die Leistungs- und Qualitätsmetriken zu konfigurieren:

    - Wählen Sie die Leistungs- und Qualitätsmetriken aus, die Sie verwenden möchten.
    - Wählen Sie das Azure OpenAI-Modell aus, das Sie für die Bewertung erstellt haben. Zum Beispiel **gpt-4o**.

    ![Prompt flow Bewertung.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.de.png)

1. Führen Sie die folgenden Schritte aus, um die Risiko- und Sicherheitsmetriken zu konfigurieren:

    - Wählen Sie die Risiko- und Sicherheitsmetriken aus, die Sie verwenden möchten.
    - Wählen Sie den Schwellenwert aus, um die Defektrate zu berechnen, die Sie verwenden möchten. Zum Beispiel **Mittel**.
    - Für **Frage** wählen Sie **Datenquelle** zu **{$data.prompt}**.
    - Für **Antwort** wählen Sie **Datenquelle** zu **{$run.outputs.answer}**.
    - Für **ground_truth** wählen Sie **Datenquelle** zu **{$data.message}**.

    ![Prompt flow Bewertung.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.de.png)

1. Wählen Sie **Weiter**.

1. Wählen Sie **Absenden**, um die Bewertung zu starten.

1. Die Bewertung wird einige Zeit in Anspruch nehmen. Sie können den Fortschritt auf der Registerkarte **Bewertung** überwachen.

### Bewertungsergebnisse überprüfen

> [!NOTE]
> Die unten dargestellten Ergebnisse dienen zur Veranschaulichung des Bewertungsprozesses. In diesem Tutorial haben wir ein Modell verwendet, das mit einem relativ kleinen Datensatz feinabgestimmt wurde, was möglicherweise zu suboptimalen Ergebnissen führt. Die tatsächlichen Ergebnisse können erheblich variieren, abhängig von der Größe, Qualität und Vielfalt des verwendeten Datensatzes sowie der spezifischen Konfiguration des Modells.

Nach Abschluss der Bewertung können Sie die Ergebnisse sowohl für die Leistungs- als auch für die Sicherheitsmetriken überprüfen.

1. Leistungs- und Qualitätsmetriken:

    - Bewerten Sie die Effektivität des Modells bei der Erstellung kohärenter, flüssiger und relevanter Antworten.

    ![Bewertungsergebnis.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.de.png)

1. Risiko- und Sicherheitsmetriken:

    - Stellen Sie sicher, dass die Ausgaben des Modells sicher sind und mit den Prinzipien für verantwortungsvolle KI übereinstimmen, um schädliche oder anstößige Inhalte zu vermeiden.

    ![Bewertungsergebnis.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.de.png)

1. Sie können nach unten scrollen, um **Detaillierte Metrikergebnisse** anzuzeigen.

    ![Bewertungsergebnis.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.de.png)

1. Durch die Bewertung Ihres benutzerdefinierten Phi-3 / Phi-3.5-Modells anhand von Leistungs- und Sicherheitsmetriken können Sie sicherstellen, dass das Modell nicht nur effektiv, sondern auch mit den Prinzipien für verantwortungsvolle KI übereinstimmt und somit für den Einsatz in der realen Welt bereit ist.

## Glückwunsch!

### Sie haben dieses Tutorial abgeschlossen

Sie haben erfolgreich das feinabgestimmte Phi-3-Modell in Kombination mit Prompt flow in Azure AI Foundry bewertet. Dies ist ein wichtiger Schritt, um sicherzustellen, dass Ihre KI-Modelle nicht nur gut funktionieren, sondern auch den Prinzipien für verantwortungsvolle KI von Microsoft entsprechen, damit Sie vertrauenswürdige und zuverlässige KI-Anwendungen entwickeln können.

![Architektur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.de.png)

## Azure-Ressourcen bereinigen

Bereinigen Sie Ihre Azure-Ressourcen, um zusätzliche Kosten für Ihr Konto zu vermeiden. Gehen Sie dazu zum Azure-Portal und löschen Sie die folgenden Ressourcen:

- Die Azure Machine Learning-Ressource.
- Den Azure Machine Learning-Modell-Endpunkt.
- Die Azure AI Foundry Projektressource.
- Die Azure AI Foundry Prompt flow-Ressource.

### Nächste Schritte

#### Dokumentation

- [Bewertung von KI-Systemen mit dem Dashboard für verantwortungsvolle KI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Bewertungs- und Überwachungsmetriken für generative KI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry-Dokumentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-Dokumentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Schulungsinhalte

- [Einführung in Microsofts Ansatz für verantwortungsvolle KI](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Einführung in Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referenzen

- [Was ist verantwortungsvolle KI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Ankündigung neuer Tools in Azure AI zur Unterstützung beim Aufbau sicherer und vertrauenswürdiger generativer KI-Anwendungen](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Bewertung generativer KI-Anwendungen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.