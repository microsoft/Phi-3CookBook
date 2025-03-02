# Lab. Optimieren von KI-Modellen für die Ausführung auf Geräten

## Einführung

> [!IMPORTANT]
> Dieses Lab erfordert eine **Nvidia A10 oder A100 GPU** mit den zugehörigen Treibern und installiertem CUDA Toolkit (Version 12+).

> [!NOTE]
> Dieses Lab dauert **35 Minuten** und bietet Ihnen eine praktische Einführung in die Kernkonzepte der Optimierung von Modellen für die Ausführung auf Geräten mithilfe von OLIVE.

## Lernziele

Am Ende dieses Labs können Sie OLIVE verwenden, um:

- Ein KI-Modell mithilfe der AWQ-Quantisierungsmethode zu quantisieren.
- Ein KI-Modell für eine spezifische Aufgabe zu optimieren.
- LoRA-Adapter (feinabgestimmte Modelle) zu generieren, um eine effiziente Ausführung auf Geräten mit ONNX Runtime zu ermöglichen.

### Was ist Olive?

Olive (*O*NNX *live*) ist ein Toolkit zur Modelloptimierung mit einer zugehörigen CLI, das Ihnen ermöglicht, Modelle für die ONNX Runtime bereitzustellen +++https://onnxruntime.ai+++ mit hoher Qualität und Performance.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.de.png)

Der Input für Olive ist typischerweise ein PyTorch- oder Hugging Face-Modell, und der Output ist ein optimiertes ONNX-Modell, das auf einem Gerät (Bereitstellungsziel) mit ONNX Runtime ausgeführt wird. Olive optimiert das Modell für den KI-Beschleuniger (NPU, GPU, CPU) des Bereitstellungsziels, der von einem Hardwareanbieter wie Qualcomm, AMD, Nvidia oder Intel bereitgestellt wird.

Olive führt einen *Workflow* aus, der eine geordnete Abfolge von einzelnen Modelloptimierungsaufgaben namens *Passes* darstellt – Beispiele für Passes sind: Modellkomprimierung, Graph-Capture, Quantisierung, Graph-Optimierung. Jeder Pass hat eine Reihe von Parametern, die angepasst werden können, um die besten Metriken wie Genauigkeit und Latenz zu erreichen, die vom jeweiligen Evaluator bewertet werden. Olive verwendet eine Suchstrategie, die einen Suchalgorithmus einsetzt, um jeden Pass einzeln oder mehrere Passes gemeinsam automatisch zu optimieren.

#### Vorteile von Olive

- **Reduziert Frustration und Zeit** durch manuelles Ausprobieren verschiedener Techniken zur Graph-Optimierung, Komprimierung und Quantisierung. Definieren Sie Ihre Qualitäts- und Leistungsanforderungen, und Olive findet automatisch das beste Modell für Sie.
- **Über 40 eingebaute Modelloptimierungskomponenten**, die modernste Techniken in den Bereichen Quantisierung, Komprimierung, Graph-Optimierung und Feinabstimmung abdecken.
- **Einfache CLI** für häufige Modelloptimierungsaufgaben, z. B. `olive quantize`, `olive auto-opt`, `olive finetune`.
- Integrierte Modellverpackung und -bereitstellung.
- Unterstützung für die Generierung von Modellen für **Multi-LoRA-Serving**.
- Workflows können mit YAML/JSON erstellt werden, um Modelloptimierungs- und Bereitstellungsaufgaben zu orchestrieren.
- Integration mit **Hugging Face** und **Azure AI**.
- Eingebauter **Caching-Mechanismus**, um **Kosten zu sparen**.

## Lab-Anleitung

> [!NOTE]
> Stellen Sie sicher, dass Sie Ihren Azure AI Hub und Ihr Projekt bereitgestellt und Ihre A100-Computing-Umgebung gemäß Lab 1 eingerichtet haben.

### Schritt 0: Verbindung zu Ihrer Azure AI Compute herstellen

Sie verbinden sich mit der Azure AI Compute-Umgebung über die Remote-Funktion in **VS Code**.

1. Öffnen Sie Ihre **VS Code**-Desktopanwendung:
1. Öffnen Sie die **Befehlsübersicht** mit **Shift+Ctrl+P**.
1. Suchen Sie in der Befehlsübersicht nach **AzureML - remote: Connect to compute instance in New Window**.
1. Befolgen Sie die Anweisungen auf dem Bildschirm, um eine Verbindung zur Compute-Umgebung herzustellen. Dies umfasst die Auswahl Ihres Azure-Abonnements, der Ressourcengruppe, des Projekts und des Computernamens, die Sie in Lab 1 eingerichtet haben.
1. Sobald Sie mit Ihrer Azure ML Compute-Instanz verbunden sind, wird dies in der **unteren linken Ecke von Visual Code** angezeigt `><Azure ML: Compute Name`.

### Schritt 1: Dieses Repository klonen

In VS Code können Sie ein neues Terminal mit **Ctrl+J** öffnen und dieses Repository klonen:

Im Terminal sollte die Eingabeaufforderung angezeigt werden:

```
azureuser@computername:~/cloudfiles/code$ 
```  
Klonen Sie die Lösung:

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```  

### Schritt 2: Ordner in VS Code öffnen

Um VS Code im relevanten Ordner zu öffnen, führen Sie den folgenden Befehl im Terminal aus. Dadurch wird ein neues Fenster geöffnet:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```  

Alternativ können Sie den Ordner öffnen, indem Sie **Datei** > **Ordner öffnen** auswählen.

### Schritt 3: Abhängigkeiten installieren

Öffnen Sie ein Terminalfenster in VS Code in Ihrer Azure AI Compute-Instanz (Tipp: **Ctrl+J**) und führen Sie die folgenden Befehle aus, um die Abhängigkeiten zu installieren:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```  

> [!NOTE]
> Die Installation aller Abhängigkeiten dauert ca. **5 Minuten**.

In diesem Lab laden Sie Modelle herunter und hoch, um sie im Azure AI Model Catalog zu verwenden. Damit Sie auf den Model Catalog zugreifen können, müssen Sie sich bei Azure anmelden:

```bash
az login
```  

> [!NOTE]
> Während der Anmeldung werden Sie aufgefordert, Ihr Abonnement auszuwählen. Stellen Sie sicher, dass Sie das für dieses Lab bereitgestellte Abonnement auswählen.

### Schritt 4: Olive-Befehle ausführen

Öffnen Sie ein Terminalfenster in VS Code in Ihrer Azure AI Compute-Instanz (Tipp: **Ctrl+J**) und stellen Sie sicher, dass die `olive-ai`-Conda-Umgebung aktiviert ist:

```bash
conda activate olive-ai
```  

Führen Sie anschließend die folgenden Olive-Befehle in der Befehlszeile aus:

1. **Daten inspizieren:** In diesem Beispiel werden Sie das Modell Phi-3.5-Mini so feinabstimmen, dass es auf reiserelevante Fragen spezialisiert ist. Der folgende Code zeigt die ersten Einträge des Datensatzes an, der im JSON-Lines-Format vorliegt:

    ```bash
    head data/data_sample_travel.jsonl
    ```  
   
1. **Modell quantisieren:** Bevor Sie das Modell trainieren, quantisieren Sie es mit dem folgenden Befehl, der eine Technik namens Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ verwendet. AWQ quantisiert die Gewichte eines Modells, indem die während der Inferenz erzeugten Aktivierungen berücksichtigt werden. Dadurch wird die Genauigkeit des Modells besser erhalten als bei herkömmlichen Methoden der Gewichtquantisierung.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```  

    Die AWQ-Quantisierung dauert **ca. 8 Minuten** und reduziert die Modellgröße von **~7,5 GB auf ~2,5 GB**.

    In diesem Lab zeigen wir Ihnen, wie Sie Modelle von Hugging Face importieren können (z. B.: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune`-Befehl das quantisierte Modell. Die Quantisierung des Modells *vor* der Feinabstimmung führt zu einer besseren Genauigkeit, da der Feinabstimmungsprozess einige Verluste durch die Quantisierung kompensiert.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```  

    Die Feinabstimmung dauert **ca. 6 Minuten** (mit 100 Schritten).

1. **Optimieren:** Nachdem das Modell trainiert wurde, optimieren Sie es nun mit dem `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider`-Argument von Olive – für die Zwecke dieses Labs verwenden wir jedoch die CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```  

    Die Optimierung dauert **ca. 5 Minuten**.

### Schritt 5: Schneller Test der Modellinferenz

Um das Modell zu testen, erstellen Sie in Ihrem Ordner eine Python-Datei mit dem Namen **app.py** und kopieren Sie den folgenden Code hinein:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```  

Führen Sie den Code mit folgendem Befehl aus:

```bash
python app.py
```  

### Schritt 6: Modell in Azure AI hochladen

Das Hochladen des Modells in ein Azure AI Model Repository ermöglicht es, das Modell mit anderen Mitgliedern Ihres Entwicklungsteams zu teilen und die Versionskontrolle des Modells zu verwalten. Führen Sie zum Hochladen des Modells den folgenden Befehl aus:

> [!NOTE]
> Aktualisieren Sie die Platzhalter `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `` für die `resourceGroup` und den Azure AI-Projektnamen und führen Sie den folgenden Befehl aus:

```
az ml workspace show
```  

Oder gehen Sie zu +++ai.azure.com+++ und wählen Sie **Management Center** > **Projekt** > **Übersicht**.

Aktualisieren Sie die `{}`-Platzhalter mit dem Namen Ihrer Ressourcengruppe und des Azure AI-Projektnamens.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Sie können Ihr hochgeladenes Modell anzeigen und es unter https://ml.azure.com/model/list bereitstellen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.