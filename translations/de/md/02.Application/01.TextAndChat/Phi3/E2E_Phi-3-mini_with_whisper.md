# Interaktiver Phi 3 Mini 4K Instruct Chatbot mit Whisper

## Überblick

Der interaktive Phi 3 Mini 4K Instruct Chatbot ist ein Tool, mit dem Benutzer über Text- oder Audioeingaben mit der Microsoft Phi 3 Mini 4K Instruct Demo interagieren können. Der Chatbot kann für eine Vielzahl von Aufgaben verwendet werden, wie z. B. Übersetzungen, Wetteraktualisierungen und allgemeine Informationsbeschaffung.

### Erste Schritte

Um diesen Chatbot zu verwenden, folgen Sie einfach diesen Anweisungen:

1. Öffnen Sie ein neues [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Im Hauptfenster des Notebooks sehen Sie eine Chatbox-Oberfläche mit einem Texteingabefeld und einer Schaltfläche „Senden“.
3. Um den textbasierten Chatbot zu verwenden, geben Sie Ihre Nachricht einfach in das Texteingabefeld ein und klicken Sie auf die Schaltfläche „Senden“. Der Chatbot antwortet mit einer Audiodatei, die direkt im Notebook abgespielt werden kann.

**Hinweis**: Dieses Tool erfordert eine GPU und Zugriff auf die Microsoft Phi-3- und OpenAI-Whisper-Modelle, die für Spracherkennung und Übersetzung verwendet werden.

### GPU-Anforderungen

Um diese Demo auszuführen, benötigen Sie 12 GB GPU-Speicher.

Die Speicheranforderungen für die Ausführung der **Microsoft-Phi-3-Mini-4K Instruct**-Demo auf einer GPU hängen von mehreren Faktoren ab, wie z. B. der Größe der Eingabedaten (Audio oder Text), der Sprache für die Übersetzung, der Geschwindigkeit des Modells und dem verfügbaren GPU-Speicher.

Im Allgemeinen ist das Whisper-Modell für die Ausführung auf GPUs konzipiert. Der empfohlene minimale GPU-Speicher für die Ausführung des Whisper-Modells beträgt 8 GB, es kann jedoch auch größere Speichermengen verarbeiten, falls erforderlich.

Es ist wichtig zu beachten, dass das Verarbeiten großer Datenmengen oder eines hohen Anfragevolumens mehr GPU-Speicher erfordern und/oder zu Leistungsproblemen führen kann. Es wird empfohlen, Ihren Anwendungsfall mit verschiedenen Konfigurationen zu testen und die Speichernutzung zu überwachen, um die optimalen Einstellungen für Ihre spezifischen Anforderungen zu ermitteln.

## E2E-Beispiel für den interaktiven Phi 3 Mini 4K Instruct Chatbot mit Whisper

Das Jupyter-Notebook mit dem Titel [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) zeigt, wie die Microsoft Phi 3 Mini 4K Instruct Demo verwendet wird, um Text aus Audio- oder Texteingaben zu generieren. Das Notebook definiert mehrere Funktionen:

1. `tts_file_name(text)`: Diese Funktion generiert basierend auf dem Eingabetext einen Dateinamen, um die erstellte Audiodatei zu speichern.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Diese Funktion verwendet die Edge TTS API, um aus einer Liste von Textabschnitten eine Audiodatei zu generieren. Die Eingabeparameter sind die Liste der Abschnitte, die Sprachgeschwindigkeit, der Name der Stimme und der Ausgabepfad zum Speichern der generierten Audiodatei.
1. `talk(input_text)`: Diese Funktion erstellt eine Audiodatei, indem sie die Edge TTS API verwendet und sie unter einem zufälligen Dateinamen im Verzeichnis /content/audio speichert. Der Eingabeparameter ist der Text, der in Sprache umgewandelt werden soll.
1. `run_text_prompt(message, chat_history)`: Diese Funktion verwendet die Microsoft Phi 3 Mini 4K Instruct Demo, um aus einer Nachrichten-Eingabe eine Audiodatei zu generieren, und fügt diese dem Chatverlauf hinzu.
1. `run_audio_prompt(audio, chat_history)`: Diese Funktion wandelt eine Audiodatei mithilfe der Whisper-Model-API in Text um und übergibt diesen an die `run_text_prompt()`-Funktion.
1. Der Code startet eine Gradio-App, die es Benutzern ermöglicht, mit der Phi 3 Mini 4K Instruct Demo zu interagieren, indem sie entweder Nachrichten eingeben oder Audiodateien hochladen. Die Ausgabe wird als Textnachricht innerhalb der App angezeigt.

## Fehlerbehebung

Installation von Cuda GPU-Treibern

1. Stellen Sie sicher, dass Ihre Linux-Anwendungen auf dem neuesten Stand sind.

    ```bash
    sudo apt update
    ```

1. Installieren Sie Cuda-Treiber.

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrieren Sie den Speicherort des Cuda-Treibers.

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Überprüfen Sie die Nvidia GPU-Speichergröße (erforderlich: 12 GB GPU-Speicher).

    ```bash
    nvidia-smi
    ```

1. Cache leeren: Wenn Sie PyTorch verwenden, können Sie torch.cuda.empty_cache() aufrufen, um allen ungenutzten zwischengespeicherten Speicher freizugeben, damit er von anderen GPU-Anwendungen verwendet werden kann.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Überprüfen Sie Nvidia Cuda.

    ```bash
    nvcc --version
    ```

1. Führen Sie die folgenden Aufgaben aus, um ein Hugging Face Token zu erstellen.

    - Navigieren Sie zur [Hugging Face Token Settings-Seite](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wählen Sie **Neues Token** aus.
    - Geben Sie den **Namen** des Projekts ein, das Sie verwenden möchten.
    - Wählen Sie den **Typ** auf **Schreiben**.

> **Hinweis**
>
> Wenn Sie auf den folgenden Fehler stoßen:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Um dies zu beheben, geben Sie den folgenden Befehl in Ihr Terminal ein.
>
> ```bash
> sudo ldconfig
> ```

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.