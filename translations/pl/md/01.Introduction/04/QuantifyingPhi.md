# **Kwantyzacja rodziny Phi**

Kwantyzacja modelu odnosi się do procesu mapowania parametrów (takich jak wagi i wartości aktywacji) w modelu sieci neuronowej z dużego zakresu wartości (zwykle ciągłego) na mniejszy, skończony zakres wartości. Technologia ta pozwala zmniejszyć rozmiar i złożoność obliczeniową modelu, a także poprawić jego efektywność w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy systemy wbudowane. Kwantyzacja modelu osiąga kompresję poprzez redukcję precyzji parametrów, ale wprowadza również pewną utratę dokładności. Dlatego w procesie kwantyzacji należy znaleźć równowagę pomiędzy rozmiarem modelu, złożonością obliczeniową a dokładnością. Do popularnych metod kwantyzacji należą kwantyzacja na liczbach stałoprzecinkowych oraz kwantyzacja na liczbach zmiennoprzecinkowych. Odpowiednią strategię kwantyzacji należy dobrać w zależności od konkretnego scenariusza i potrzeb.

Chcemy wdrożyć model GenAI na urządzeniach brzegowych, umożliwiając większej liczbie urządzeń korzystanie ze scenariuszy GenAI, takich jak urządzenia mobilne, AI PC/Copilot+PC czy tradycyjne urządzenia IoT. Dzięki kwantyzacji modelu możemy wdrożyć go na różnych urządzeniach brzegowych, w zależności od ich specyfikacji. W połączeniu z ramami przyspieszającymi działanie modelu oraz kwantyzacją oferowaną przez producentów sprzętu, możemy budować lepsze scenariusze aplikacji SLM.

W scenariuszach kwantyzacji dostępne są różne precyzje (INT4, INT8, FP16, FP32). Poniżej znajduje się opis najczęściej stosowanych precyzji kwantyzacji.

### **INT4**

Kwantyzacja INT4 to radykalna metoda kwantyzacji, która zamienia wagi i wartości aktywacji modelu na 4-bitowe liczby całkowite. Z powodu mniejszego zakresu reprezentacji i niższej precyzji, kwantyzacja INT4 zazwyczaj prowadzi do większej utraty dokładności. Jednak w porównaniu do kwantyzacji INT8, INT4 może jeszcze bardziej zmniejszyć wymagania dotyczące pamięci i złożoności obliczeniowej modelu. Należy jednak zauważyć, że kwantyzacja INT4 jest stosunkowo rzadko wykorzystywana w praktyce, ponieważ zbyt niska dokładność może powodować znaczne pogorszenie wydajności modelu. Ponadto, nie cały sprzęt obsługuje operacje INT4, więc przy wyborze metody kwantyzacji należy uwzględnić kompatybilność sprzętową.

### **INT8**

Kwantyzacja INT8 polega na konwersji wag i aktywacji modelu z liczb zmiennoprzecinkowych na 8-bitowe liczby całkowite. Chociaż zakres wartości reprezentowanych przez liczby INT8 jest mniejszy, a ich precyzja niższa, to metoda ta znacząco redukuje wymagania dotyczące pamięci i obliczeń. W kwantyzacji INT8 wagi i wartości aktywacji modelu przechodzą proces kwantyzacji, który obejmuje skalowanie i przesunięcie, aby jak najlepiej zachować oryginalne informacje zmiennoprzecinkowe. Podczas wnioskowania wartości te są dekwantyzowane z powrotem do liczb zmiennoprzecinkowych w celu przeprowadzenia obliczeń, a następnie ponownie kwantyzowane do INT8 w kolejnym kroku. Ta metoda zapewnia wystarczającą dokładność w większości zastosowań, jednocześnie utrzymując wysoką efektywność obliczeniową.

### **FP16**

Format FP16, czyli 16-bitowe liczby zmiennoprzecinkowe (float16), zmniejsza zapotrzebowanie na pamięć o połowę w porównaniu z 32-bitowymi liczbami zmiennoprzecinkowymi (float32), co jest istotną zaletą w dużych aplikacjach uczenia głębokiego. Format FP16 pozwala ładować większe modele lub przetwarzać więcej danych w ramach tych samych ograniczeń pamięci GPU. W miarę jak nowoczesny sprzęt GPU coraz częściej wspiera operacje FP16, korzystanie z tego formatu może również przyczynić się do zwiększenia szybkości obliczeń. Jednak FP16 ma swoje wady, w tym niższą precyzję, co w niektórych przypadkach może prowadzić do niestabilności numerycznej lub utraty dokładności.

### **FP32**

Format FP32 oferuje wyższą precyzję i pozwala dokładnie reprezentować szeroki zakres wartości. W scenariuszach, w których wykonywane są złożone operacje matematyczne lub wymagane są wyniki o wysokiej dokładności, preferowany jest format FP32. Jednak wyższa dokładność oznacza również większe zużycie pamięci i dłuższy czas obliczeń. W przypadku dużych modeli uczenia głębokiego, zwłaszcza gdy model ma wiele parametrów i przetwarza ogromne ilości danych, format FP32 może prowadzić do niewystarczającej pamięci GPU lub spowolnienia procesu wnioskowania.

Na urządzeniach mobilnych lub IoT możemy konwertować modele Phi-3.x na INT4, podczas gdy na AI PC / Copilot PC można stosować wyższą precyzję, taką jak INT8, FP16, FP32.

Obecnie różni producenci sprzętu oferują różne ramy wspierające modele generatywne, takie jak OpenVINO od Intela, QNN od Qualcomma, MLX od Apple czy CUDA od Nvidii, które w połączeniu z kwantyzacją modelu pozwalają na lokalne wdrożenia.

Pod względem technicznym, po kwantyzacji mamy wsparcie dla różnych formatów, takich jak PyTorch / Tensorflow, GGUF i ONNX. Przeprowadziłem porównanie formatów GGUF i ONNX oraz ich zastosowań. Polecam tutaj format kwantyzacji ONNX, który ma dobre wsparcie od ram modelowych po sprzęt. W tym rozdziale skupimy się na ONNX Runtime dla GenAI, OpenVINO i Apple MLX w celu przeprowadzenia kwantyzacji modelu (jeśli masz lepszy sposób, możesz go nam przekazać, przesyłając PR).

**Ten rozdział zawiera**

1. [Kwantyzacja Phi-3.5 / 4 za pomocą llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kwantyzacja Phi-3.5 / 4 za pomocą rozszerzeń Generative AI dla onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kwantyzacja Phi-3.5 / 4 za pomocą Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kwantyzacja Phi-3.5 / 4 za pomocą frameworka Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usług automatycznego tłumaczenia AI. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.