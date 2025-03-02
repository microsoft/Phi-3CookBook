# Witamy w Twoim rozszerzeniu do VS Code

## Co znajduje się w folderze

* Ten folder zawiera wszystkie pliki niezbędne do Twojego rozszerzenia.
* `package.json` - to plik manifestu, w którym deklarujesz swoje rozszerzenie i komendę.
  * Przykładowa wtyczka rejestruje komendę i definiuje jej tytuł oraz nazwę. Na podstawie tych informacji VS Code może wyświetlić komendę w palecie poleceń. Wtyczka nie musi być jeszcze załadowana.
* `src/extension.ts` - to główny plik, w którym dostarczasz implementację swojej komendy.
  * Plik eksportuje jedną funkcję, `activate`, która jest wywoływana za pierwszym razem, gdy Twoje rozszerzenie zostaje aktywowane (w tym przypadku poprzez wykonanie komendy). Wewnątrz funkcji `activate` wywołujemy `registerCommand`.
  * Przekazujemy funkcję zawierającą implementację komendy jako drugi parametr do `registerCommand`.

## Konfiguracja

* Zainstaluj zalecane rozszerzenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint).

## Szybki start

* Naciśnij `F5`, aby otworzyć nowe okno z załadowanym rozszerzeniem.
* Uruchom swoją komendę z palety poleceń, naciskając (`Ctrl+Shift+P` lub `Cmd+Shift+P` na Macu) i wpisując `Hello World`.
* Ustaw punkty przerwania w swoim kodzie w pliku `src/extension.ts`, aby debugować swoje rozszerzenie.
* Znajdź dane wyjściowe swojego rozszerzenia w konsoli debugowania.

## Wprowadzanie zmian

* Możesz ponownie uruchomić rozszerzenie z paska narzędzi debugowania po wprowadzeniu zmian w pliku `src/extension.ts`.
* Możesz także przeładować (`Ctrl+R` lub `Cmd+R` na Macu) okno VS Code z Twoim rozszerzeniem, aby załadować zmiany.

## Poznawanie API

* Możesz otworzyć pełny zestaw naszego API, otwierając plik `node_modules/@types/vscode/index.d.ts`.

## Uruchamianie testów

* Zainstaluj [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Uruchom zadanie "watch" za pomocą polecenia **Tasks: Run Task**. Upewnij się, że jest ono uruchomione, inaczej testy mogą nie zostać wykryte.
* Otwórz widok Testowanie na pasku aktywności i kliknij przycisk "Run Test" lub użyj skrótu `Ctrl/Cmd + ; A`.
* Zobacz wyniki testów w widoku wyników testów.
* Wprowadzaj zmiany w pliku `src/test/extension.test.ts` lub twórz nowe pliki testowe w folderze `test`.
  * Dostarczony runner testów uwzględni jedynie pliki pasujące do wzorca nazwy `**.test.ts`.
  * Możesz tworzyć foldery w folderze `test`, aby dowolnie organizować swoje testy.

## Sięgnij dalej

* Zmniejsz rozmiar rozszerzenia i popraw czas jego uruchamiania, [pakując swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Opublikuj swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) w sklepie rozszerzeń VS Code.
* Zautomatyzuj budowanie, konfigurując [Ciągłą Integrację](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.