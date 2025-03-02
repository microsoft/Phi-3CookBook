# **Quantifizierung der Phi-Familie**

Modellquantisierung bezieht sich auf den Prozess, die Parameter (wie Gewichte und Aktivierungswerte) in einem neuronalen Netzwerkmodell von einem großen Wertebereich (normalerweise ein kontinuierlicher Wertebereich) auf einen kleineren, endlichen Wertebereich abzubilden. Diese Technologie kann die Größe und die rechnerische Komplexität des Modells reduzieren und die Betriebseffizienz des Modells in ressourcenbeschränkten Umgebungen wie mobilen Geräten oder eingebetteten Systemen verbessern. Die Modellquantisierung erreicht eine Komprimierung, indem die Genauigkeit der Parameter reduziert wird, was jedoch auch einen gewissen Genauigkeitsverlust mit sich bringt. Daher ist es im Quantisierungsprozess notwendig, die Modellgröße, die rechnerische Komplexität und die Genauigkeit auszubalancieren. Zu den gängigen Quantisierungsmethoden gehören Festpunktquantisierung, Gleitpunktquantisierung usw. Sie können die geeignete Quantisierungsstrategie je nach spezifischem Szenario und Bedarf auswählen.

Wir möchten das GenAI-Modell auf Edge-Geräte bereitstellen und mehr Geräten den Zugang zu GenAI-Szenarien ermöglichen, wie z. B. mobile Geräte, AI-PCs/Copilot-PCs und traditionelle IoT-Geräte. Durch das quantisierte Modell können wir es je nach Gerät auf verschiedenen Edge-Geräten bereitstellen. In Kombination mit dem von Hardwareherstellern bereitgestellten Modellbeschleunigungsframework und dem quantisierten Modell können wir bessere SLM-Anwendungsszenarien erstellen.

Im Quantisierungsszenario haben wir unterschiedliche Genauigkeiten (INT4, INT8, FP16, FP32). Im Folgenden werden die häufig verwendeten Quantisierungsgenauigkeiten erläutert.

### **INT4**

INT4-Quantisierung ist eine radikale Quantisierungsmethode, bei der die Gewichte und Aktivierungswerte des Modells in 4-Bit-Ganzzahlen quantisiert werden. INT4-Quantisierung führt aufgrund des kleineren Darstellungsbereichs und der geringeren Genauigkeit in der Regel zu einem größeren Genauigkeitsverlust. Im Vergleich zur INT8-Quantisierung kann die INT4-Quantisierung jedoch die Speicheranforderungen und die rechnerische Komplexität des Modells weiter reduzieren. Es ist zu beachten, dass die INT4-Quantisierung in der Praxis relativ selten angewendet wird, da die zu geringe Genauigkeit zu einer erheblichen Verschlechterung der Modellleistung führen kann. Außerdem unterstützt nicht jede Hardware INT4-Operationen, sodass bei der Wahl der Quantisierungsmethode die Hardwarekompatibilität berücksichtigt werden muss.

### **INT8**

Die INT8-Quantisierung ist der Prozess, bei dem die Gewichte und Aktivierungen eines Modells von Gleitkommazahlen in 8-Bit-Ganzzahlen umgewandelt werden. Obwohl der durch INT8-Ganzzahlen dargestellte Wertebereich kleiner und weniger präzise ist, können die Speicher- und Berechnungsanforderungen erheblich reduziert werden. Bei der INT8-Quantisierung durchlaufen die Gewichte und Aktivierungswerte des Modells einen Quantisierungsprozess, der Skalierung und Offset umfasst, um die ursprünglichen Gleitkommainformationen so weit wie möglich zu bewahren. Während der Inferenz werden diese quantisierten Werte zurück in Gleitkommazahlen umgewandelt, um Berechnungen durchzuführen, und dann wieder in INT8 quantisiert, um den nächsten Schritt auszuführen. Diese Methode bietet in den meisten Anwendungen ausreichende Genauigkeit und gleichzeitig eine hohe Recheneffizienz.

### **FP16**

Das FP16-Format, also 16-Bit-Gleitkommazahlen (float16), reduziert den Speicherbedarf im Vergleich zu 32-Bit-Gleitkommazahlen (float32) um die Hälfte, was in groß angelegten Deep-Learning-Anwendungen erhebliche Vorteile bietet. Das FP16-Format ermöglicht das Laden größerer Modelle oder die Verarbeitung größerer Datenmengen innerhalb derselben GPU-Speichergrenzen. Da moderne GPU-Hardware zunehmend FP16-Operationen unterstützt, kann die Verwendung des FP16-Formats auch Verbesserungen bei der Rechengeschwindigkeit mit sich bringen. Das FP16-Format hat jedoch auch seine inhärenten Nachteile, nämlich eine geringere Genauigkeit, die in einigen Fällen zu numerischer Instabilität oder Genauigkeitsverlust führen kann.

### **FP32**

Das FP32-Format bietet eine höhere Genauigkeit und kann eine große Bandbreite von Werten präzise darstellen. In Szenarien, in denen komplexe mathematische Operationen durchgeführt werden oder hochpräzise Ergebnisse erforderlich sind, wird das FP32-Format bevorzugt. Hohe Genauigkeit bedeutet jedoch auch mehr Speicherverbrauch und längere Berechnungszeiten. Für groß angelegte Deep-Learning-Modelle, insbesondere wenn viele Modellparameter und eine riesige Datenmenge vorliegen, kann das FP32-Format zu unzureichendem GPU-Speicher oder einer Verringerung der Inferenzgeschwindigkeit führen.

Auf mobilen Geräten oder IoT-Geräten können wir Phi-3.x-Modelle in INT4 konvertieren, während AI-PCs/Copilot-PCs höhere Genauigkeiten wie INT8, FP16 oder FP32 verwenden können.

Derzeit haben verschiedene Hardwarehersteller unterschiedliche Frameworks zur Unterstützung generativer Modelle, wie Intels OpenVINO, Qualcomms QNN, Apples MLX und Nvidias CUDA usw., die in Kombination mit der Modellquantisierung eine lokale Bereitstellung ermöglichen.

Technisch gesehen haben wir nach der Quantisierung unterschiedliche Formatunterstützungen, wie PyTorch-/TensorFlow-Format, GGUF und ONNX. Ich habe einen Vergleich der Formate GGUF und ONNX sowie deren Anwendungsszenarien durchgeführt. Hier empfehle ich das ONNX-Quantisierungsformat, das eine gute Unterstützung vom Modellentwicklungsframework bis zur Hardware bietet. In diesem Kapitel werden wir uns auf ONNX Runtime für GenAI, OpenVINO und Apple MLX konzentrieren, um die Modellquantisierung durchzuführen (wenn Sie eine bessere Methode haben, können Sie uns diese gerne durch das Einreichen eines PR mitteilen).

**Dieses Kapitel umfasst**

1. [Quantisierung von Phi-3.5 / 4 mit llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantisierung von Phi-3.5 / 4 mit generativen AI-Erweiterungen für onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantisierung von Phi-3.5 / 4 mit Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantisierung von Phi-3.5 / 4 mit Apples MLX-Framework](./UsingAppleMLXQuantifyingPhi.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.