# **Quantisierung von Phi-3.5 mit dem Apple MLX Framework**

MLX ist ein Array-Framework für maschinelles Lernen auf Apple Silicon, entwickelt von der Apple Machine Learning Forschung.

MLX wurde von Forschern für maschinelles Lernen entwickelt und richtet sich an andere Forschende in diesem Bereich. Das Framework ist benutzerfreundlich gestaltet, bleibt dabei aber effizient für das Training und den Einsatz von Modellen. Auch das Konzept hinter dem Framework ist bewusst einfach gehalten. Unser Ziel ist es, Forschenden zu ermöglichen, MLX leicht zu erweitern und zu verbessern, um neue Ideen schnell auszuprobieren.

LLMs können auf Apple-Silicon-Geräten mit MLX beschleunigt werden, und Modelle lassen sich lokal sehr bequem ausführen.

Das Apple MLX Framework unterstützt nun die Quantisierungskonvertierung von Phi-3.5-Instruct (**Apple MLX Framework-Unterstützung**), Phi-3.5-Vision (**MLX-VLM Framework-Unterstützung**) und Phi-3.5-MoE (**Apple MLX Framework-Unterstützung**). Probieren wir es aus:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Beispiele für Phi-3.5 mit Apple MLX**

| Labs    | Einführung | Gehe zu |
| -------- | ------- |  ------- |
| 🚀 Lab-Einführung Phi-3.5 Instruct  | Erfahre, wie man Phi-3.5 Instruct mit dem Apple MLX Framework verwendet   |  [Gehe zu](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Einführung Phi-3.5 Vision (Bild) | Erfahre, wie man Phi-3.5 Vision zur Bildanalyse mit dem Apple MLX Framework verwendet     |  [Gehe zu](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Einführung Phi-3.5 Vision (MoE)   | Erfahre, wie man Phi-3.5 MoE mit dem Apple MLX Framework verwendet  |  [Gehe zu](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressourcen**

1. Erfahre mehr über das Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.