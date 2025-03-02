# Feinabstimmung von Phi3 mit Olive

In diesem Beispiel verwenden Sie Olive, um:

1. Einen LoRA-Adapter zu trainieren, der Phrasen in die Kategorien Traurigkeit, Freude, Angst und Überraschung einordnet.
2. Die Adapter-Gewichte in das Basismodell zu integrieren.
3. Das Modell zu optimieren und in `int4` zu quantisieren.

Wir zeigen Ihnen außerdem, wie Sie das feinabgestimmte Modell mithilfe der ONNX Runtime (ORT) Generate API zur Inferenz nutzen können.

> **⚠️ Für das Fein-Tuning benötigen Sie eine geeignete GPU - zum Beispiel eine A10, V100, A100.**

## 💾 Installation

Erstellen Sie eine neue Python-Umgebung (zum Beispiel mit `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installieren Sie anschließend Olive und die Abhängigkeiten für den Fein-Tuning-Workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Feinabstimmung von Phi3 mit Olive
Die [Olive-Konfigurationsdatei](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) enthält einen *Workflow* mit den folgenden *Passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Auf hoher Ebene führt dieser Workflow die folgenden Schritte aus:

1. Feinabstimmung von Phi3 (für 150 Schritte, dies können Sie anpassen) mit den Daten aus [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Zusammenführen der LoRA-Adapter-Gewichte mit dem Basismodell. Dadurch erhalten Sie ein einzelnes Modellartefakt im ONNX-Format.
3. Der Model Builder optimiert das Modell für die ONNX Runtime *und* quantisiert es in `int4`.

Um den Workflow auszuführen, verwenden Sie:

```bash
olive run --config phrase-classification.json
```

Nach Abschluss durch Olive steht Ihr optimiertes `int4` feinabgestimmtes Phi3-Modell unter folgendem Pfad bereit: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Feinabgestimmtes Phi3 in Ihre Anwendung integrieren

Um die Anwendung auszuführen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Die Antwort sollte eine einzelne Wortklassifikation der Phrase sein (Traurigkeit/Freude/Angst/Überraschung).

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe KI-gestützter maschineller Übersetzungsdienste übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.