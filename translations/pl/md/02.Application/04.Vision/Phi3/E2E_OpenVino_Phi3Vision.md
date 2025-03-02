Ten demo pokazuje, jak użyć wstępnie wytrenowanego modelu do generowania kodu Python na podstawie obrazu i tekstowego polecenia.

[Przykładowy kod](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Oto wyjaśnienie krok po kroku:

1. **Importy i konfiguracja**:
   - Importowane są niezbędne biblioteki i moduły, w tym `requests`, `PIL` do przetwarzania obrazów oraz `transformers` do obsługi modelu i przetwarzania.

2. **Ładowanie i wyświetlanie obrazu**:
   - Plik obrazu (`demo.png`) jest otwierany za pomocą biblioteki `PIL` i wyświetlany.

3. **Definiowanie polecenia**:
   - Tworzona jest wiadomość, która zawiera obraz i prośbę o wygenerowanie kodu Python do przetwarzania obrazu i zapisania go za pomocą `plt` (matplotlib).

4. **Ładowanie procesora**:
   - `AutoProcessor` jest ładowany z wstępnie wytrenowanego modelu określonego w katalogu `out_dir`. Procesor ten obsłuży dane tekstowe i obrazy.

5. **Tworzenie polecenia**:
   - Metoda `apply_chat_template` jest używana do sformatowania wiadomości w polecenie odpowiednie dla modelu.

6. **Przetwarzanie danych wejściowych**:
   - Polecenie i obraz są przetwarzane na tensory, które model może zrozumieć.

7. **Ustawianie parametrów generowania**:
   - Definiowane są argumenty dla procesu generowania modelu, w tym maksymalna liczba nowych tokenów do wygenerowania oraz czy wynik ma być próbkowany.

8. **Generowanie kodu**:
   - Model generuje kod Python na podstawie danych wejściowych i parametrów generowania. `TextStreamer` jest używane do obsługi wyniku, pomijając polecenie i specjalne tokeny.

9. **Wynik**:
   - Wygenerowany kod jest drukowany i powinien zawierać kod Python do przetwarzania obrazu i zapisania go zgodnie z poleceniem.

Ten demo pokazuje, jak wykorzystać wstępnie wytrenowany model z OpenVino do dynamicznego generowania kodu na podstawie danych wejściowych użytkownika i obrazów.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.