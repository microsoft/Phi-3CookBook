# **Wnioskowanie Phi-3 na Androidzie**

Przyjrzyjmy się, jak można przeprowadzić wnioskowanie z użyciem Phi-3-mini na urządzeniach z Androidem. Phi-3-mini to nowa seria modeli od Microsoftu, która umożliwia wdrażanie dużych modeli językowych (LLM) na urządzeniach brzegowych oraz IoT.

## Semantic Kernel i Wnioskowanie

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) to framework aplikacyjny, który pozwala tworzyć aplikacje kompatybilne z Azure OpenAI Service, modelami OpenAI, a nawet modelami lokalnymi. Jeśli dopiero zaczynasz pracę z Semantic Kernel, polecamy zapoznać się z [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Dostęp do Phi-3-mini za pomocą Semantic Kernel

Możesz połączyć go z Hugging Face Connector w Semantic Kernel. Zobacz ten [przykładowy kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Domyślnie odpowiada on identyfikatorowi modelu na Hugging Face. Możesz jednak również połączyć się z lokalnym serwerem modelu Phi-3-mini.

### Wywoływanie modeli skwantowanych z Ollama lub LlamaEdge

Wielu użytkowników preferuje korzystanie z modeli skwantowanych, aby uruchamiać je lokalnie. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) umożliwiają indywidualnym użytkownikom wywoływanie różnych modeli skwantowanych:

#### Ollama

Możesz bezpośrednio uruchomić `ollama run Phi-3` lub skonfigurować go w trybie offline, tworząc `Modelfile` ze ścieżką do pliku `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Przykładowy kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jeśli chcesz używać plików `.gguf` zarówno w chmurze, jak i na urządzeniach brzegowych, LlamaEdge to świetny wybór. Możesz zapoznać się z tym [przykładowym kodem](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo), aby rozpocząć.

### Instalacja i uruchamianie na telefonach z Androidem

1. **Pobierz aplikację MLC Chat** (darmową) na telefony z Androidem.
2. Pobierz plik APK (148MB) i zainstaluj go na swoim urządzeniu.
3. Uruchom aplikację MLC Chat. Zobaczysz listę modeli AI, w tym Phi-3-mini.

Podsumowując, Phi-3-mini otwiera ekscytujące możliwości dla generatywnej AI na urządzeniach brzegowych, a Ty możesz już teraz zacząć eksplorować jego możliwości na Androidzie.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.