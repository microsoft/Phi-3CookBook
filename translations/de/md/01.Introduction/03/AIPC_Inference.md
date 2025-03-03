# **Inference Phi-3 auf einem AI-PC**

Mit den Fortschritten in generativer KI und der Verbesserung der Hardwarefähigkeiten von Edge-Geräten können immer mehr generative KI-Modelle in die Bring-Your-Own-Device (BYOD)-Geräte der Nutzer integriert werden. AI-PCs gehören zu diesen Modellen. Ab 2024 arbeiten Intel, AMD und Qualcomm mit PC-Herstellern zusammen, um AI-PCs einzuführen, die durch Hardwaremodifikationen die Bereitstellung lokalisierter generativer KI-Modelle ermöglichen. In dieser Diskussion konzentrieren wir uns auf Intel AI-PCs und untersuchen, wie man Phi-3 auf einem Intel AI-PC einsetzen kann.

### Was ist eine NPU?

Eine NPU (Neural Processing Unit) ist ein spezieller Prozessor oder eine Verarbeitungseinheit auf einem größeren SoC, die speziell für die Beschleunigung von neuronalen Netzoperationen und KI-Aufgaben entwickelt wurde. Im Gegensatz zu universellen CPUs und GPUs sind NPUs für datengetriebenes paralleles Rechnen optimiert, was sie besonders effizient bei der Verarbeitung großer Multimedia-Datenmengen wie Videos und Bildern sowie bei der Verarbeitung von Daten für neuronale Netzwerke macht. Sie sind besonders geeignet für KI-bezogene Aufgaben wie Spracherkennung, Hintergrundunschärfe bei Videoanrufen und Foto- oder Videobearbeitungsprozesse wie Objekterkennung.

## NPU vs. GPU

Obwohl viele KI- und Machine-Learning-Workloads auf GPUs ausgeführt werden, gibt es einen entscheidenden Unterschied zwischen GPUs und NPUs.  
GPUs sind bekannt für ihre Fähigkeiten im parallelen Rechnen, aber nicht alle GPUs sind über die Grafikverarbeitung hinaus gleichermaßen effizient. NPUs hingegen sind speziell für die komplexen Berechnungen ausgelegt, die bei neuronalen Netzoperationen erforderlich sind, und sind daher besonders effektiv für KI-Aufgaben.

Zusammenfassend lässt sich sagen, dass NPUs die Mathe-Genies sind, die KI-Berechnungen beschleunigen, und sie spielen eine Schlüsselrolle in der aufkommenden Ära der AI-PCs!

***Dieses Beispiel basiert auf Intels neuestem Intel Core Ultra Prozessor.***

## **1. Verwendung der NPU zur Ausführung des Phi-3-Modells**

Das Intel® NPU-Gerät ist ein KI-Inferenzbeschleuniger, der in Intel-Client-CPUs integriert ist, beginnend mit der Intel® Core™ Ultra-Generation von CPUs (ehemals Meteor Lake). Es ermöglicht eine energieeffiziente Ausführung von Aufgaben neuronaler Netze.

![Latenz](../../../../../translated_images/aipcphitokenlatency.446d244d43a98a99f001e6eb55b421ab7ebc0b5d8f93fad8458da46cf263bfad.de.png)

![Latenz770](../../../../../translated_images/aipcphitokenlatency770.862269853961e495131e9465fdb06c2c7b94395b83729dc498cfc077e02caade.de.png)

**Intel NPU Acceleration Library**

Die Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) ist eine Python-Bibliothek, die entwickelt wurde, um die Effizienz Ihrer Anwendungen zu steigern, indem die Leistung der Intel Neural Processing Unit (NPU) genutzt wird, um Hochgeschwindigkeitsberechnungen auf kompatibler Hardware auszuführen.

Beispiel für Phi-3-mini auf einem AI-PC, der von Intel® Core™ Ultra-Prozessoren betrieben wird.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Installation der Python-Bibliothek mit pip

```bash

   pip install intel-npu-acceleration-library

```

***Hinweis*** Das Projekt befindet sich noch in der Entwicklung, aber das Referenzmodell ist bereits sehr vollständig.

### **Ausführung von Phi-3 mit der Intel NPU Acceleration Library**

Durch die Nutzung der Intel NPU-Beschleunigung wird der traditionelle Kodierungsprozess nicht beeinflusst. Sie müssen lediglich diese Bibliothek verwenden, um das ursprüngliche Phi-3-Modell zu quantisieren, z. B. FP16, INT8, INT4, wie 

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Nach erfolgreicher Quantisierung fahren Sie mit der Ausführung fort, um die NPU aufzurufen und das Phi-3-Modell auszuführen.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Beim Ausführen des Codes können wir den Betriebsstatus der NPU über den Task-Manager einsehen.

![NPU](../../../../../translated_images/aipc_NPU.f047860f84f5bb5b183756f23b4b8506485e862ea34c6a53c58988707c23bc80.de.png)

***Beispiele***: [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Verwendung von DirectML + ONNX Runtime zur Ausführung des Phi-3-Modells**

### **Was ist DirectML**

[DirectML](https://github.com/microsoft/DirectML) ist eine leistungsstarke, hardwarebeschleunigte DirectX 12-Bibliothek für maschinelles Lernen. DirectML bietet GPU-Beschleunigung für gängige Aufgaben des maschinellen Lernens auf einer breiten Palette unterstützter Hardware und Treiber, einschließlich aller DirectX 12-fähigen GPUs von Anbietern wie AMD, Intel, NVIDIA und Qualcomm.

Wenn es eigenständig verwendet wird, ist die DirectML-API eine Low-Level-DirectX-12-Bibliothek und eignet sich für leistungsstarke, latenzarme Anwendungen wie Frameworks, Spiele und andere Echtzeitanwendungen. Die nahtlose Interoperabilität von DirectML mit Direct3D 12 sowie der geringe Overhead und die Konformität über verschiedene Hardware machen DirectML ideal für die Beschleunigung von maschinellem Lernen, wenn sowohl hohe Leistung als auch Zuverlässigkeit und Vorhersehbarkeit der Ergebnisse über verschiedene Hardware hinweg entscheidend sind.

***Hinweis***: Die neueste Version von DirectML unterstützt bereits NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/).

### DirectML und CUDA in Bezug auf ihre Fähigkeiten und Leistung:

**DirectML** ist eine von Microsoft entwickelte Bibliothek für maschinelles Lernen. Sie wurde entwickelt, um Workloads für maschinelles Lernen auf Windows-Geräten zu beschleunigen, einschließlich Desktops, Laptops und Edge-Geräten.  
- DX12-basiert: DirectML basiert auf DirectX 12 (DX12), das eine breite Hardware-Unterstützung über GPUs hinweg bietet, einschließlich NVIDIA und AMD.  
- Breitere Unterstützung: Da es DX12 nutzt, kann DirectML mit jeder GPU arbeiten, die DX12 unterstützt, auch mit integrierten GPUs.  
- Bildverarbeitung: DirectML verarbeitet Bilder und andere Daten mithilfe von neuronalen Netzwerken und eignet sich daher für Aufgaben wie Bilderkennung, Objekterkennung und mehr.  
- Einfache Einrichtung: Die Einrichtung von DirectML ist unkompliziert und erfordert keine speziellen SDKs oder Bibliotheken von GPU-Herstellern.  
- Leistung: In einigen Fällen ist DirectML leistungsstark und kann für bestimmte Workloads schneller sein als CUDA.  
- Einschränkungen: Es gibt jedoch Fälle, in denen DirectML langsamer sein kann, insbesondere bei Float16 und großen Batch-Größen.

**CUDA** ist NVIDIAs Plattform und Programmiermodell für paralleles Rechnen. Es ermöglicht Entwicklern, die Leistung von NVIDIA-GPUs für allgemeine Berechnungen, einschließlich maschinellem Lernen und wissenschaftlichen Simulationen, zu nutzen.  
- NVIDIA-spezifisch: CUDA ist eng mit NVIDIA-GPUs integriert und speziell für diese entwickelt.  
- Hoch optimiert: Es bietet exzellente Leistung für GPU-beschleunigte Aufgaben, insbesondere bei der Verwendung von NVIDIA-GPUs.  
- Weit verbreitet: Viele Frameworks und Bibliotheken für maschinelles Lernen (wie TensorFlow und PyTorch) unterstützen CUDA.  
- Anpassung: Entwickler können CUDA-Einstellungen für spezifische Aufgaben feinabstimmen, was zu optimaler Leistung führen kann.  
- Einschränkungen: Die Abhängigkeit von NVIDIA-Hardware kann jedoch einschränkend sein, wenn eine breitere Kompatibilität über verschiedene GPUs hinweg gewünscht wird.

### Auswahl zwischen DirectML und CUDA

Die Wahl zwischen DirectML und CUDA hängt von Ihrem spezifischen Anwendungsfall, der verfügbaren Hardware und Ihren Präferenzen ab.  
Wenn Sie eine breitere Kompatibilität und eine einfache Einrichtung suchen, könnte DirectML eine gute Wahl sein. Wenn Sie jedoch NVIDIA-GPUs besitzen und eine hoch optimierte Leistung benötigen, bleibt CUDA eine starke Option. Zusammenfassend lässt sich sagen, dass sowohl DirectML als auch CUDA ihre Stärken und Schwächen haben. Berücksichtigen Sie daher Ihre Anforderungen und die verfügbare Hardware bei der Entscheidung.

### **Generative KI mit ONNX Runtime**

In der Ära der KI ist die Portabilität von KI-Modellen sehr wichtig. ONNX Runtime ermöglicht es, trainierte Modelle einfach auf verschiedene Geräte zu übertragen. Entwickler müssen sich nicht mit dem Inferenz-Framework beschäftigen und können mit einer einheitlichen API die Modellausführung abschließen. In der Ära der generativen KI hat ONNX Runtime auch Code-Optimierungen durchgeführt (https://onnxruntime.ai/docs/genai/). Mit der optimierten ONNX Runtime kann das quantisierte generative KI-Modell auf verschiedenen Endgeräten ausgeführt werden. In Generative KI mit ONNX Runtime können Sie KI-Modell-APIs über Python, C# oder C/C++ ausführen. Natürlich kann die Bereitstellung auf einem iPhone die Generative KI mit der ONNX Runtime API von C++ nutzen.

[Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Kompilieren der generativen KI mit der ONNX Runtime-Bibliothek***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Bibliothek installieren**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Dies ist das Ausführungsergebnis:

![DML](../../../../../translated_images/aipc_DML.dd810ee1f3882323c131b39065ed0cf41bbe0aaa8d346a0d6d290c20f5c0bf75.de.png)

***Beispiele***: [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Verwendung von Intel OpenVINO zur Ausführung des Phi-3-Modells**

### **Was ist OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) ist ein Open-Source-Toolkit zur Optimierung und Bereitstellung von Deep-Learning-Modellen. Es bietet gesteigerte Deep-Learning-Leistung für Vision-, Audio- und Sprachmodelle aus beliebten Frameworks wie TensorFlow, PyTorch und mehr. Mit OpenVINO können auch CPU und GPU kombiniert werden, um das Phi-3-Modell auszuführen.

***Hinweis***: OpenVINO unterstützt derzeit keine NPU.

### **OpenVINO-Bibliothek installieren**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Ausführung von Phi-3 mit OpenVINO**

Ähnlich wie bei der NPU führt OpenVINO die Aufrufe generativer KI-Modelle durch die Ausführung quantisierter Modelle aus. Zunächst müssen wir das Phi-3-Modell quantisieren und die Modellquantisierung über die Befehlszeile mit optimum-cli abschließen.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Das konvertierte Format sieht so aus:

![openvino_convert](../../../../../translated_images/aipc_OpenVINO_convert.bd70cf3d87e65a923d2d663f559a03d86227ab71071802355a6cfeaf80eb7042.de.png)

Laden Sie Modellpfade (model_dir), zugehörige Konfigurationen (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) und hardwarebeschleunigte Geräte (GPU.0) über OVModelForCausalLM.

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Beim Ausführen des Codes können wir den Betriebsstatus der GPU über den Task-Manager einsehen.

![openvino_gpu](../../../../../translated_images/aipc_OpenVINO_GPU.142b31f25c5ffcf8802077629d11fbae275e53aeeb0752e0cdccf826feca6875.de.png)

***Beispiele***: [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Hinweis***: Die oben genannten drei Methoden haben jeweils ihre eigenen Vorteile, aber es wird empfohlen, NPU-Beschleunigung für die KI-PC-Inferenz zu verwenden.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe maschineller KI-Übersetzungsdienste übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.