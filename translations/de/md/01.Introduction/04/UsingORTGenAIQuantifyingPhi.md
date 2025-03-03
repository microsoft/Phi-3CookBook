# **Quantisierung der Phi-Familie mit Generative AI-Erweiterungen für onnxruntime**

## **Was sind Generative AI-Erweiterungen für onnxruntime**

Diese Erweiterungen helfen Ihnen, generative KI mit ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) auszuführen. Sie bieten die generative KI-Schleife für ONNX-Modelle, einschließlich Inferenz mit ONNX Runtime, Logits-Verarbeitung, Suche und Sampling sowie Verwaltung des KV-Caches. Entwickler können entweder eine hochrangige generate()-Methode aufrufen oder jede Iteration des Modells in einer Schleife ausführen, wobei ein Token nach dem anderen generiert wird. Dabei können sie optional die Generierungsparameter innerhalb der Schleife aktualisieren. Die Erweiterungen unterstützen Greedy-/Beam-Suche sowie TopP- und TopK-Sampling zur Generierung von Token-Sequenzen und bieten eingebaute Logits-Verarbeitung wie Wiederholungsstrafen. Außerdem können Sie problemlos benutzerdefinierte Bewertungen hinzufügen.

Auf Anwendungsebene können Sie Generative AI-Erweiterungen für onnxruntime verwenden, um Anwendungen mit C++/C#/Python zu erstellen. Auf Modellebene können Sie sie nutzen, um feinabgestimmte Modelle zu kombinieren und damit verbundene quantitative Deployment-Arbeiten durchzuführen.

## **Quantisierung von Phi-3.5 mit Generative AI-Erweiterungen für onnxruntime**

### **Unterstützte Modelle**

Die Generative AI-Erweiterungen für onnxruntime unterstützen die Quantisierungskonvertierung von Microsoft Phi, Google Gemma, Mistral und Meta LLaMA.

### **Model Builder in Generative AI-Erweiterungen für onnxruntime**

Der Model Builder beschleunigt erheblich die Erstellung optimierter und quantisierter ONNX-Modelle, die mit der ONNX Runtime generate()-API ausgeführt werden.

Mit dem Model Builder können Sie das Modell auf INT4, INT8, FP16, FP32 quantisieren und verschiedene Hardwarebeschleunigungsmethoden wie CPU, CUDA, DirectML, Mobile usw. kombinieren.

Um den Model Builder zu verwenden, müssen Sie Folgendes installieren:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Nach der Installation können Sie das Model Builder-Skript aus dem Terminal ausführen, um die Konvertierung des Modellformats und der Quantisierung durchzuführen.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Verstehen Sie die relevanten Parameter:

1. **model_name** Dies ist das Modell auf Hugging Face, wie z. B. microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct usw. Es kann auch der Pfad sein, in dem Sie das Modell speichern.

2. **path_to_output_folder** Speicherpfad für die quantisierte Konvertierung.

3. **execution_provider** Unterstützung für verschiedene Hardwarebeschleunigungen, wie CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Wir laden das Modell von Hugging Face herunter und cachen es lokal.

***Hinweis:*** 

## **Wie man den Model Builder zur Quantisierung von Phi-3.5 verwendet**

Der Model Builder unterstützt jetzt die ONNX-Modellquantisierung für Phi-3.5 Instruct und Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-beschleunigte Konvertierung auf quantisiertes INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-beschleunigte Konvertierung auf quantisiertes INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Umgebung im Terminal einrichten:

```bash

mkdir models

cd models 

```

2. Laden Sie microsoft/Phi-3.5-vision-instruct im Ordner "models" herunter:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Laden Sie diese Dateien in Ihren Phi-3.5-vision-instruct-Ordner herunter:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Laden Sie diese Datei in den Ordner "models" herunter:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gehen Sie ins Terminal:

   Konvertieren Sie ONNX-Unterstützung mit FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Hinweis:**

1. Der Model Builder unterstützt derzeit die Konvertierung von Phi-3.5-Instruct und Phi-3.5-Vision, jedoch nicht Phi-3.5-MoE.

2. Um das quantisierte Modell von ONNX zu verwenden, können Sie es über das Generative AI-Erweiterungen für onnxruntime SDK nutzen.

3. Wir müssen mehr auf verantwortungsvolle KI achten. Daher wird empfohlen, nach der Modellquantisierung effektivere Ergebnistests durchzuführen.

4. Durch die Quantisierung des CPU-INT4-Modells können wir es auf Edge-Geräten bereitstellen, was bessere Anwendungsszenarien bietet. Aus diesem Grund haben wir Phi-3.5-Instruct für INT4 abgeschlossen.

## **Ressourcen**

1. Mehr über Generative AI-Erweiterungen für onnxruntime erfahren:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-Erweiterungen für onnxruntime GitHub-Repo:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.