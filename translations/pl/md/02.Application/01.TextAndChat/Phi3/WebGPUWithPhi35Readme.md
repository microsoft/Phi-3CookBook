# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo prezentujący WebGPU i wzorzec RAG

Wzorzec RAG z modelem Phi-3.5 Onnx Hosted wykorzystuje podejście Retrieval-Augmented Generation, łącząc możliwości modeli Phi-3.5 z hostingiem ONNX dla efektywnego wdrażania AI. Ten wzorzec jest kluczowy dla dostrajania modeli do zadań specyficznych dla danej dziedziny, oferując połączenie jakości, opłacalności i zrozumienia długiego kontekstu. Jest częścią pakietu Azure AI, zapewniającego szeroki wybór modeli, które są łatwe do znalezienia, przetestowania i użycia, spełniając potrzeby personalizacji w różnych branżach.

## Czym jest WebGPU
WebGPU to nowoczesne API do grafiki internetowej, zaprojektowane w celu zapewnienia wydajnego dostępu do procesora graficznego (GPU) urządzenia bezpośrednio z przeglądarek internetowych. Ma być następcą WebGL i oferuje kilka kluczowych ulepszeń:

1. **Kompatybilność z nowoczesnymi GPU**: WebGPU zostało stworzone, aby działać bezproblemowo z współczesnymi architekturami GPU, wykorzystując systemowe API, takie jak Vulkan, Metal i Direct3D 12.
2. **Zwiększona wydajność**: Obsługuje ogólne obliczenia GPU i szybsze operacje, co czyni je odpowiednim zarówno do renderowania grafiki, jak i zadań związanych z uczeniem maszynowym.
3. **Zaawansowane funkcje**: WebGPU zapewnia dostęp do bardziej zaawansowanych możliwości GPU, umożliwiając bardziej złożone i dynamiczne obciążenia graficzne oraz obliczeniowe.
4. **Zmniejszenie obciążenia JavaScript**: Dzięki przeniesieniu większej liczby zadań na GPU, WebGPU znacznie zmniejsza obciążenie JavaScript, co prowadzi do lepszej wydajności i płynniejszych doświadczeń.

WebGPU jest obecnie obsługiwane w przeglądarkach takich jak Google Chrome, a prace nad wsparciem na innych platformach są w toku.

### 03.WebGPU
Wymagane środowisko:

**Obsługiwane przeglądarki:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Włączanie WebGPU:

- W Chrome/Microsoft Edge 

Włącz flagę `chrome://flags/#enable-unsafe-webgpu`.

#### Otwórz swoją przeglądarkę:
Uruchom Google Chrome lub Microsoft Edge.

#### Przejdź do strony z flagami:
W pasku adresu wpisz `chrome://flags` i naciśnij Enter.

#### Wyszukaj flagę:
W polu wyszukiwania u góry strony wpisz 'enable-unsafe-webgpu'.

#### Włącz flagę:
Znajdź flagę #enable-unsafe-webgpu na liście wyników.

Kliknij menu rozwijane obok niej i wybierz Enabled.

#### Zrestartuj przeglądarkę:

Po włączeniu flagi musisz zrestartować przeglądarkę, aby zmiany zaczęły obowiązywać. Kliknij przycisk Relaunch, który pojawi się na dole strony.

- W przypadku systemu Linux uruchom przeglądarkę z `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ma domyślnie włączony WebGPU.
- W Firefox Nightly wpisz about:config w pasku adresu i `set dom.webgpu.enabled to true`.

### Konfiguracja GPU dla Microsoft Edge 

Oto kroki konfiguracji wydajnego GPU dla Microsoft Edge w systemie Windows:

- **Otwórz Ustawienia:** Kliknij menu Start i wybierz Ustawienia.
- **Ustawienia systemowe:** Przejdź do System, a następnie Wyświetlacz.
- **Ustawienia grafiki:** Przewiń w dół i kliknij Ustawienia grafiki.
- **Wybierz aplikację:** W sekcji „Wybierz aplikację, aby ustawić preferencje” wybierz Aplikacja klasyczna, a następnie Przeglądaj.
- **Wybierz Edge:** Przejdź do folderu instalacyjnego Edge (zazwyczaj `C:\Program Files (x86)\Microsoft\Edge\Application`) i wybierz `msedge.exe`.
- **Ustaw preferencje:** Kliknij Opcje, wybierz Wysoka wydajność, a następnie kliknij Zapisz.
To zapewni, że Microsoft Edge będzie korzystać z wydajnego GPU dla lepszej wydajności. 
- **Zrestartuj** komputer, aby te ustawienia zaczęły obowiązywać.

### Przykłady: Proszę [kliknij ten link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą automatycznych usług tłumaczeniowych opartych na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.