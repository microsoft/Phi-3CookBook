# **Quantisierung der Phi-Familie mit llama.cpp**

## **Was ist llama.cpp**

llama.cpp ist eine Open-Source-Softwarebibliothek, die hauptsächlich in C++ geschrieben ist und Inferenz für verschiedene Large Language Models (LLMs) wie Llama durchführt. Ihr Hauptziel ist es, erstklassige Leistung für LLM-Inferenz auf einer Vielzahl von Hardware mit minimalem Setup zu bieten. Zusätzlich gibt es Python-Bindings für diese Bibliothek, die eine High-Level-API für Textvervollständigung und einen OpenAI-kompatiblen Webserver bereitstellen.

Das Hauptziel von llama.cpp ist es, LLM-Inferenz mit minimalem Setup und erstklassiger Leistung auf einer breiten Palette von Hardware zu ermöglichen – sowohl lokal als auch in der Cloud.

- Reine C/C++-Implementierung ohne Abhängigkeiten
- Apple Silicon wird erstklassig unterstützt – optimiert durch ARM NEON, Accelerate und Metal-Frameworks
- Unterstützung für AVX, AVX2 und AVX512 auf x86-Architekturen
- 1,5-Bit-, 2-Bit-, 3-Bit-, 4-Bit-, 5-Bit-, 6-Bit- und 8-Bit-Ganzzahlquantisierung für schnellere Inferenz und geringeren Speicherbedarf
- Benutzerdefinierte CUDA-Kernels für das Ausführen von LLMs auf NVIDIA-GPUs (Unterstützung für AMD-GPUs über HIP)
- Vulkan- und SYCL-Backend-Unterstützung
- Hybrid-Inferenz CPU+GPU, um Modelle zu beschleunigen, die größer sind als die gesamte VRAM-Kapazität

## **Quantisierung von Phi-3.5 mit llama.cpp**

Das Phi-3.5-Instruct-Modell kann mit llama.cpp quantisiert werden, aber Phi-3.5-Vision und Phi-3.5-MoE werden derzeit noch nicht unterstützt. Das von llama.cpp konvertierte Format ist GGUF, welches auch das am weitesten verbreitete Quantisierungsformat ist.

Es gibt eine große Anzahl von quantisierten Modellen im GGUF-Format auf Hugging Face. AI Foundry, Ollama und LlamaEdge basieren auf llama.cpp, weshalb GGUF-Modelle ebenfalls häufig verwendet werden.

### **Was ist GGUF**

GGUF ist ein binäres Format, das für schnelles Laden und Speichern von Modellen optimiert ist und somit hoch effizient für Inferenzzwecke ist. GGUF wurde für die Nutzung mit GGML und anderen Ausführungsengines entwickelt. GGUF wurde von @ggerganov entwickelt, der auch der Entwickler von llama.cpp ist, einem beliebten C/C++-Framework für LLM-Inferenz. Modelle, die ursprünglich in Frameworks wie PyTorch entwickelt wurden, können in das GGUF-Format konvertiert werden, um mit diesen Engines genutzt zu werden.

### **ONNX vs GGUF**

ONNX ist ein traditionelles Format für maschinelles Lernen/Tiefenlernen, das in verschiedenen KI-Frameworks gut unterstützt wird und sich für Edge-Geräte eignet. GGUF hingegen basiert auf llama.cpp und stammt aus der GenAI-Ära. Beide Formate haben ähnliche Einsatzbereiche. Wenn Sie bessere Leistung auf eingebetteter Hardware und Anwendungsebenen wünschen, könnte ONNX die bessere Wahl sein. Wenn Sie jedoch das Framework und die Technologien von llama.cpp nutzen, ist GGUF möglicherweise besser geeignet.

### **Quantisierung von Phi-3.5-Instruct mit llama.cpp**

**1. Umgebung konfigurieren**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. Quantisierung**

Mit llama.cpp Phi-3.5-Instruct zu FP16 GGUF konvertieren

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantisierung von Phi-3.5 zu INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. Testen**

llama-cpp-python installieren

```bash

pip install llama-cpp-python -U

```

***Hinweis***

Wenn Sie Apple Silicon verwenden, installieren Sie llama-cpp-python folgendermaßen:

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testen

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **Ressourcen**

1. Mehr über llama.cpp erfahren [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Mehr über GGUF erfahren [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.