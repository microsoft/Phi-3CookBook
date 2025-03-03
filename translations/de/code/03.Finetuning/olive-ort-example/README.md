# Feinabstimmung von Phi3 mit Olive

In diesem Beispiel verwenden Sie Olive, um:

1. Einen LoRA-Adapter zu trainieren, der Phrasen in die Kategorien Traurig, Freude, Angst und Überraschung klassifiziert.
1. Die Adaptergewichte mit dem Basismodell zu verschmelzen.
1. Das Modell zu optimieren und in `int4` zu quantisieren.

Wir zeigen Ihnen außerdem, wie Sie das feinabgestimmte Modell mithilfe der ONNX Runtime (ORT) Generate API für Inferenz verwenden können.

> **⚠️ Für das Fein-Tuning benötigen Sie eine geeignete GPU, z. B. eine A10, V100 oder A100.**

## 💾 Installation

Erstellen Sie eine neue Python-Umgebung (zum Beispiel mit `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installieren Sie anschließend Olive und die Abhängigkeiten für einen Fein-Tuning-Workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Feinabstimmung von Phi3 mit Olive

Die [Olive-Konfigurationsdatei](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) enthält einen *Workflow* mit den folgenden *Passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Auf hoher Ebene führt dieser Workflow Folgendes aus:

1. Feinabstimmung von Phi3 (für 150 Schritte, die Sie anpassen können) mit den Daten aus [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Zusammenführung der LoRA-Adaptergewichte mit dem Basismodell. Dies ergibt ein einzelnes Modellartefakt im ONNX-Format.
1. Der Model Builder optimiert das Modell für die ONNX Runtime *und* quantisiert das Modell in `int4`.

Um den Workflow auszuführen, verwenden Sie:

```bash
olive run --config phrase-classification.json
```

Sobald Olive abgeschlossen ist, steht Ihr optimiertes `int4` feinabgestimmtes Phi3-Modell hier zur Verfügung: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integration des feinabgestimmten Phi3 in Ihre Anwendung

Um die Anwendung auszuführen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Die Antwort sollte eine Ein-Wort-Klassifikation der Phrase sein (Traurig/Freude/Angst/Überraschung).

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.