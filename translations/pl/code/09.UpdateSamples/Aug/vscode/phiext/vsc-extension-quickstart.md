# Witamy w Twoim rozszerzeniu VS Code

## Co znajduje się w folderze

* Ten folder zawiera wszystkie pliki niezbędne do działania Twojego rozszerzenia.
* `package.json` - to plik manifestu, w którym deklarujesz swoje rozszerzenie i komendę.
  * Przykładowa wtyczka rejestruje komendę oraz definiuje jej tytuł i nazwę. Dzięki tym informacjom VS Code może wyświetlić komendę w palecie poleceń. Nie musi jeszcze ładować wtyczki.
* `src/extension.ts` - to główny plik, w którym dostarczasz implementację swojej komendy.
  * Plik eksportuje jedną funkcję, `activate`, która jest wywoływana za pierwszym razem, gdy Twoje rozszerzenie zostanie aktywowane (w tym przypadku przez wykonanie komendy). Wewnątrz funkcji `activate` wywołujemy `registerCommand`.
  * Przekazujemy funkcję zawierającą implementację komendy jako drugi parametr do `registerCommand`.

## Konfiguracja

* Zainstaluj zalecane rozszerzenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint).

## Szybki start

* Naciśnij `F5`, aby otworzyć nowe okno z załadowanym rozszerzeniem.
* Uruchom swoją komendę z palety poleceń, naciskając (`Ctrl+Shift+P` lub `Cmd+Shift+P` na Macu) i wpisując `Hello World`.
* Ustaw punkty przerwania w swoim kodzie wewnątrz `src/extension.ts`, aby debugować swoje rozszerzenie.
* Znajdź dane wyjściowe swojego rozszerzenia w konsoli debugowania.

## Wprowadzanie zmian

* Możesz ponownie uruchomić rozszerzenie z paska narzędzi debugowania po wprowadzeniu zmian w `src/extension.ts`.
* Możesz także przeładować (`Ctrl+R` lub `Cmd+R` na Macu) okno VS Code z Twoim rozszerzeniem, aby załadować zmiany.

## Eksploracja API

* Możesz otworzyć pełny zestaw naszego API, otwierając plik `node_modules/@types/vscode/index.d.ts`.

## Uruchamianie testów

* Zainstaluj [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Uruchom zadanie "watch" za pomocą polecenia **Tasks: Run Task**. Upewnij się, że jest uruchomione, w przeciwnym razie testy mogą nie zostać wykryte.
* Otwórz widok Testowania na pasku aktywności i kliknij przycisk "Run Test" lub użyj skrótu `Ctrl/Cmd + ; A`.
* Zobacz wyniki testów w widoku Test Results.
* Wprowadź zmiany w `src/test/extension.test.ts` lub utwórz nowe pliki testowe w folderze `test`.
  * Dostarczony runner testów będzie uwzględniał tylko pliki pasujące do wzorca nazwy `**.test.ts`.
  * Możesz tworzyć foldery wewnątrz folderu `test`, aby dowolnie zorganizować swoje testy.

## Idź dalej

* Zmniejsz rozmiar rozszerzenia i popraw czas uruchamiania, [pakując swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Opublikuj swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) w marketplace rozszerzeń VS Code.
* Zautomatyzuj budowanie, konfigurując [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.