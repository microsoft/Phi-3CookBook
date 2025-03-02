**Feinabstimmung von Phi-3 mit QLoRA**

Feinabstimmung von Microsofts Phi-3 Mini-Sprachmodell mithilfe von [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora). 

QLoRA hilft dabei, das Verständnis in Gesprächen und die Generierung von Antworten zu verbessern.

Um Modelle in 4-Bit mit transformers und bitsandbytes zu laden, müssen Sie accelerate und transformers aus dem Quellcode installieren und sicherstellen, dass Sie die neueste Version der bitsandbytes-Bibliothek verwenden.

**Beispiele**
- [Erfahren Sie mehr mit diesem Beispiel-Notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Beispiel eines Python-Feinabstimmungs-Skripts](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Beispiel für Feinabstimmung mit Hugging Face Hub und LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Beispiel für Feinabstimmung mit Hugging Face Hub und QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.