Phi-3-mini WebGPU RAG Chatbot

## Demo prezentujący WebGPU i wzorzec RAG
Wzorzec RAG z modelem Phi-3 Onnx Hosted wykorzystuje podejście Retrieval-Augmented Generation, łącząc możliwości modeli Phi-3 z hostingiem ONNX dla efektywnego wdrażania AI. Ten wzorzec jest kluczowy w dostosowywaniu modeli do zadań specyficznych dla danej dziedziny, oferując połączenie jakości, opłacalności i zrozumienia długiego kontekstu. Jest częścią pakietu Azure AI, który zapewnia szeroki wybór modeli łatwych do znalezienia, wypróbowania i użycia, odpowiadając na potrzeby dostosowywania w różnych branżach. Modele Phi-3, w tym Phi-3-mini, Phi-3-small i Phi-3-medium, są dostępne w katalogu modeli Azure AI i mogą być dostosowywane oraz wdrażane samodzielnie lub za pośrednictwem platform takich jak HuggingFace i ONNX, co podkreśla zaangażowanie Microsoft w dostępne i wydajne rozwiązania AI.

## Czym jest WebGPU
WebGPU to nowoczesne API graficzne dla sieci, zaprojektowane w celu zapewnienia efektywnego dostępu do procesora graficznego (GPU) urządzenia bezpośrednio z przeglądarek internetowych. Jest następcą WebGL i oferuje kilka kluczowych ulepszeń:

1. **Kompatybilność z nowoczesnymi GPU**: WebGPU zostało stworzone, aby działać bezproblemowo z współczesnymi architekturami GPU, wykorzystując systemowe API, takie jak Vulkan, Metal i Direct3D 12.
2. **Zwiększona wydajność**: Obsługuje obliczenia ogólnego przeznaczenia na GPU oraz szybsze operacje, co czyni go odpowiednim zarówno do renderowania grafiki, jak i zadań związanych z uczeniem maszynowym.
3. **Zaawansowane funkcje**: WebGPU zapewnia dostęp do bardziej zaawansowanych możliwości GPU, umożliwiając bardziej złożone i dynamiczne obciążenia graficzne oraz obliczeniowe.
4. **Zmniejszenie obciążenia JavaScript**: Dzięki przeniesieniu większej liczby zadań na GPU, WebGPU znacząco redukuje obciążenie JavaScript, co prowadzi do lepszej wydajności i płynniejszych doświadczeń.

WebGPU jest obecnie obsługiwane w przeglądarkach takich jak Google Chrome, a prace nad rozszerzeniem wsparcia na inne platformy są w toku.

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

#### Otwórz przeglądarkę:
Uruchom Google Chrome lub Microsoft Edge.

#### Przejdź do strony flag:
W pasku adresu wpisz `chrome://flags` i naciśnij Enter.

#### Wyszukaj flagę:
W polu wyszukiwania u góry strony wpisz 'enable-unsafe-webgpu'.

#### Włącz flagę:
Znajdź flagę #enable-unsafe-webgpu na liście wyników.

Kliknij menu rozwijane obok niej i wybierz Enabled.

#### Uruchom ponownie przeglądarkę:

Po włączeniu flagi musisz ponownie uruchomić przeglądarkę, aby zmiany zaczęły obowiązywać. Kliknij przycisk Relaunch, który pojawi się na dole strony.

- W przypadku systemu Linux uruchom przeglądarkę z `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ma domyślnie włączone WebGPU.
- W Firefox Nightly wpisz about:config w pasku adresu i `set dom.webgpu.enabled to true`.

### Konfiguracja GPU dla Microsoft Edge 

Oto kroki, aby skonfigurować wysokowydajny GPU dla Microsoft Edge w systemie Windows:

- **Otwórz Ustawienia:** Kliknij menu Start i wybierz Ustawienia.
- **Ustawienia systemowe:** Przejdź do System, a następnie Ekran.
- **Ustawienia grafiki:** Przewiń w dół i kliknij Ustawienia grafiki.
- **Wybierz aplikację:** W sekcji „Wybierz aplikację do ustawienia preferencji” wybierz Aplikacja desktopowa, a następnie Przeglądaj.
- **Wybierz Edge:** Przejdź do folderu instalacyjnego Edge (zazwyczaj `C:\Program Files (x86)\Microsoft\Edge\Application`) i wybierz `msedge.exe`.
- **Ustaw preferencje:** Kliknij Opcje, wybierz Wysoka wydajność, a następnie kliknij Zapisz.
To zapewni, że Microsoft Edge będzie używał twojego wysokowydajnego GPU dla lepszej wydajności.
- **Uruchom ponownie** komputer, aby ustawienia zaczęły obowiązywać.

### Otwórz Codespace:
Przejdź do swojego repozytorium na GitHub.
Kliknij przycisk Code i wybierz Open with Codespaces.

Jeśli nie masz jeszcze Codespace, możesz go utworzyć, klikając New codespace.

**Uwaga** Instalacja środowiska Node w Codespace
Uruchamianie demonstracji npm z GitHub Codespace to świetny sposób na testowanie i rozwijanie projektu. Oto krok po kroku, jak to zrobić:

### Konfiguracja środowiska:
Po otwarciu Codespace upewnij się, że masz zainstalowane Node.js i npm. Możesz to sprawdzić, uruchamiając:
```
node -v
```
```
npm -v
```

Jeśli nie są zainstalowane, możesz je zainstalować za pomocą:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Przejdź do katalogu projektu:
Użyj terminala, aby przejść do katalogu, w którym znajduje się twój projekt npm:
```
cd path/to/your/project
```

### Instalacja zależności:
Uruchom następujące polecenie, aby zainstalować wszystkie niezbędne zależności wymienione w pliku package.json:

```
npm install
```

### Uruchom demonstrację:
Po zainstalowaniu zależności możesz uruchomić skrypt demonstracyjny. Zazwyczaj jest on określony w sekcji scripts pliku package.json. Na przykład, jeśli twój skrypt demonstracyjny nazywa się start, możesz go uruchomić za pomocą:

```
npm run build
```
```
npm run dev
```

### Dostęp do demonstracji:
Jeśli twoja demonstracja obejmuje serwer WWW, Codespaces udostępni URL do niej. Poszukaj powiadomienia lub sprawdź zakładkę Ports, aby znaleźć URL.

**Uwaga:** Model musi zostać zapisany w pamięci podręcznej przeglądarki, więc jego ładowanie może chwilę potrwać.

### Demonstracja RAG
Prześlij plik markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Wybierz swój plik:
Kliknij przycisk „Wybierz plik”, aby wybrać dokument, który chcesz przesłać.

### Prześlij dokument:
Po wybraniu pliku kliknij przycisk „Prześlij”, aby załadować dokument do RAG (Retrieval-Augmented Generation).

### Rozpocznij czat:
Po przesłaniu dokumentu możesz rozpocząć sesję czatu za pomocą RAG na podstawie treści swojego dokumentu.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.