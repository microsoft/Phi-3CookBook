# Witaj w swoim rozszerzeniu VS Code

## Co znajduje się w folderze

* Ten folder zawiera wszystkie pliki niezbędne do działania Twojego rozszerzenia.
* `package.json` - to plik manifestu, w którym deklarujesz swoje rozszerzenie i polecenie.
  * Przykładowa wtyczka rejestruje polecenie i definiuje jego tytuł oraz nazwę. Dzięki tym informacjom VS Code może wyświetlić polecenie w palecie poleceń. Na tym etapie wtyczka nie musi być jeszcze załadowana.
* `src/extension.ts` - to główny plik, w którym implementujesz swoje polecenie.
  * Plik eksportuje jedną funkcję, `activate`, która jest wywoływana przy pierwszej aktywacji Twojego rozszerzenia (w tym przypadku przez wykonanie polecenia). Wewnątrz funkcji `activate` wywołujemy `registerCommand`.
  * Funkcję zawierającą implementację polecenia przekazujemy jako drugi parametr do `registerCommand`.

## Konfiguracja

* Zainstaluj zalecane rozszerzenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint).

## Szybki start

* Naciśnij `F5`, aby otworzyć nowe okno z załadowanym rozszerzeniem.
* Uruchom swoje polecenie z palety poleceń, naciskając (`Ctrl+Shift+P` lub `Cmd+Shift+P` na Macu) i wpisując `Hello World`.
* Ustaw punkty przerwania w swoim kodzie w pliku `src/extension.ts`, aby debugować rozszerzenie.
* Znajdź dane wyjściowe swojego rozszerzenia w konsoli debugowania.

## Wprowadzanie zmian

* Możesz ponownie uruchomić rozszerzenie z paska narzędzi debugowania po zmianie kodu w pliku `src/extension.ts`.
* Możesz również przeładować (`Ctrl+R` lub `Cmd+R` na Macu) okno VS Code z Twoim rozszerzeniem, aby załadować zmiany.

## Eksploracja API

* Możesz otworzyć pełny zestaw naszego API, otwierając plik `node_modules/@types/vscode/index.d.ts`.

## Uruchamianie testów

* Zainstaluj [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Uruchom zadanie "watch" za pomocą polecenia **Tasks: Run Task**. Upewnij się, że to zadanie jest uruchomione, w przeciwnym razie testy mogą nie zostać wykryte.
* Otwórz widok Testowania z paska aktywności i kliknij przycisk "Run Test", lub użyj skrótu `Ctrl/Cmd + ; A`.
* Wyniki testów znajdziesz w widoku Test Results.
* Wprowadzaj zmiany w `src/test/extension.test.ts` lub twórz nowe pliki testowe w folderze `test`.
  * Dostarczony runner testowy uwzględni tylko pliki pasujące do wzorca nazwy `**.test.ts`.
  * Możesz tworzyć foldery w folderze `test`, aby dowolnie organizować swoje testy.

## Dalsze kroki

* Zmniejsz rozmiar rozszerzenia i popraw czas uruchamiania, [pakując swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Opublikuj swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) w sklepie z rozszerzeniami VS Code.
* Zautomatyzuj budowanie, konfigurując [Ciągłą Integrację](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.