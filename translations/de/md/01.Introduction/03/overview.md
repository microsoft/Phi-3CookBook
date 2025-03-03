Im Kontext von Phi-3-mini bezieht sich Inferenz auf den Prozess, das Modell zu nutzen, um Vorhersagen zu treffen oder Ausgaben basierend auf Eingabedaten zu generieren. Lassen Sie mich Ihnen mehr Details zu Phi-3-mini und seinen Inferenzfähigkeiten geben.

Phi-3-mini ist Teil der Phi-3-Modellreihe, die von Microsoft veröffentlicht wurde. Diese Modelle sind darauf ausgelegt, die Möglichkeiten von Small Language Models (SLMs) neu zu definieren.

Hier sind einige wichtige Punkte zu Phi-3-mini und seinen Inferenzfähigkeiten:

## **Übersicht über Phi-3-mini:**
- Phi-3-mini hat eine Parametergröße von 3,8 Milliarden.
- Es kann nicht nur auf herkömmlichen Rechengeräten, sondern auch auf Edge-Geräten wie Mobilgeräten und IoT-Geräten ausgeführt werden.
- Die Veröffentlichung von Phi-3-mini ermöglicht es Einzelpersonen und Unternehmen, SLMs auf verschiedenen Hardwaregeräten einzusetzen, insbesondere in ressourcenbeschränkten Umgebungen.
- Es unterstützt verschiedene Modellformate, darunter das traditionelle PyTorch-Format, die quantisierte Version des gguf-Formats und die auf ONNX basierende quantisierte Version.

## **Zugriff auf Phi-3-mini:**
Um auf Phi-3-mini zuzugreifen, können Sie [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) in einer Copilot-Anwendung verwenden. Semantic Kernel ist im Allgemeinen kompatibel mit dem Azure OpenAI Service, Open-Source-Modellen auf Hugging Face und lokalen Modellen.
Sie können auch [Ollama](https://ollama.com) oder [LlamaEdge](https://llamaedge.com) nutzen, um quantisierte Modelle aufzurufen. Ollama ermöglicht es Einzelpersonen, verschiedene quantisierte Modelle zu verwenden, während LlamaEdge plattformübergreifende Verfügbarkeit für GGUF-Modelle bietet.

## **Quantisierte Modelle:**
Viele Nutzer bevorzugen die Verwendung von quantisierten Modellen für lokale Inferenz. Zum Beispiel können Sie direkt Ollama run Phi-3 ausführen oder es offline mit einer Modelfile konfigurieren. Die Modelfile gibt den GGUF-Dateipfad und das Prompt-Format an.

## **Möglichkeiten der generativen KI:**
Die Kombination von SLMs wie Phi-3-mini eröffnet neue Möglichkeiten für generative KI. Inferenz ist nur der erste Schritt; diese Modelle können für verschiedene Aufgaben in ressourcenbeschränkten, latenzabhängigen und kostenoptimierten Szenarien eingesetzt werden.

## **Generative KI mit Phi-3-mini freischalten: Ein Leitfaden für Inferenz und Bereitstellung**
Erfahren Sie, wie Sie Semantic Kernel, Ollama/LlamaEdge und ONNX Runtime nutzen können, um Phi-3-mini-Modelle zu verwenden und die Möglichkeiten der generativen KI in verschiedenen Anwendungsszenarien zu erkunden.

**Funktionen**
Inference des phi3-mini-Modells in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Zusammenfassend ermöglicht Phi-3-mini Entwicklern, verschiedene Modellformate zu erkunden und generative KI in verschiedenen Anwendungsszenarien zu nutzen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.