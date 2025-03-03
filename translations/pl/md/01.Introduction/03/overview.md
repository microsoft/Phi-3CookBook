W kontekście Phi-3-mini, wnioskowanie odnosi się do procesu wykorzystania modelu do przewidywania lub generowania wyników na podstawie danych wejściowych. Pozwól, że przedstawię więcej szczegółów na temat Phi-3-mini i jego możliwości wnioskowania.

Phi-3-mini jest częścią serii modeli Phi-3 wydanych przez Microsoft. Modele te zostały zaprojektowane, aby na nowo zdefiniować możliwości Małych Modeli Językowych (SLM).

Oto kilka kluczowych informacji o Phi-3-mini i jego możliwościach wnioskowania:

## **Przegląd Phi-3-mini:**
- Phi-3-mini ma rozmiar parametrów wynoszący 3,8 miliarda.
- Może działać nie tylko na tradycyjnych urządzeniach obliczeniowych, ale także na urządzeniach brzegowych, takich jak urządzenia mobilne i urządzenia IoT.
- Wydanie Phi-3-mini umożliwia osobom prywatnym i przedsiębiorstwom wdrażanie SLM na różnych urządzeniach sprzętowych, zwłaszcza w środowiskach o ograniczonych zasobach.
- Obsługuje różne formaty modeli, w tym tradycyjny format PyTorch, skwantowany format gguf oraz oparty na ONNX skwantowany format.

## **Dostęp do Phi-3-mini:**
Aby uzyskać dostęp do Phi-3-mini, możesz skorzystać z [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) w aplikacji Copilot. Semantic Kernel jest ogólnie kompatybilny z Azure OpenAI Service, modelami open-source na Hugging Face i modelami lokalnymi.  
Możesz także użyć [Ollama](https://ollama.com) lub [LlamaEdge](https://llamaedge.com) do wywoływania skwantowanych modeli. Ollama pozwala użytkownikom indywidualnym na wywoływanie różnych skwantowanych modeli, podczas gdy LlamaEdge zapewnia wieloplatformową dostępność dla modeli GGUF.

## **Modele skwantowane:**
Wielu użytkowników preferuje korzystanie z modeli skwantowanych do lokalnego wnioskowania. Na przykład możesz bezpośrednio uruchomić Ollama run Phi-3 lub skonfigurować go offline za pomocą Modelfile. Modelfile określa ścieżkę do pliku GGUF oraz format promptu.

## **Możliwości generatywnej AI:**
Łączenie SLM, takich jak Phi-3-mini, otwiera nowe możliwości dla generatywnej AI. Wnioskowanie to tylko pierwszy krok; modele te mogą być wykorzystywane do różnych zadań w środowiskach o ograniczonych zasobach, niskiej latencji i ograniczonych kosztach.

## **Odblokowanie generatywnej AI za pomocą Phi-3-mini: Przewodnik po wnioskowaniu i wdrażaniu**  
Dowiedz się, jak korzystać z Semantic Kernel, Ollama/LlamaEdge i ONNX Runtime, aby uzyskać dostęp do modeli Phi-3-mini i wnioskować z ich użyciem, a także odkryj możliwości generatywnej AI w różnych scenariuszach aplikacyjnych.

**Funkcje**  
Wnioskowanie z modelem phi3-mini w:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Podsumowując, Phi-3-mini pozwala programistom na eksplorację różnych formatów modeli i wykorzystanie generatywnej AI w różnorodnych scenariuszach aplikacyjnych.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.