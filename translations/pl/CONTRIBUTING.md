# Współtworzenie

Ten projekt chętnie przyjmuje wkład i sugestie. Większość wkładów wymaga, abyś zgodził się na Umowę Licencyjną Współtwórcy (CLA), w której deklarujesz, że masz prawo do udzielenia nam praw do korzystania z Twojego wkładu i faktycznie to robisz. Szczegóły znajdziesz na stronie [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kiedy przesyłasz pull request, bot CLA automatycznie określi, czy musisz dostarczyć CLA, i odpowiednio oznaczy PR (np. sprawdzenie statusu, komentarz). Po prostu postępuj zgodnie z instrukcjami podanymi przez bota. Musisz to zrobić tylko raz dla wszystkich repozytoriów korzystających z naszego CLA.

## Kodeks postępowania

Ten projekt przyjął [Kodeks Postępowania Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/). Aby uzyskać więcej informacji, przeczytaj [FAQ dotyczące Kodeksu Postępowania](https://opensource.microsoft.com/codeofconduct/faq/) lub skontaktuj się z [opencode@microsoft.com](mailto:opencode@microsoft.com), jeśli masz dodatkowe pytania lub uwagi.

## Uwagi dotyczące tworzenia zgłoszeń

Prosimy nie otwierać zgłoszeń na GitHubie w sprawach ogólnych pytań dotyczących wsparcia, ponieważ lista GitHuba powinna być używana do zgłaszania propozycji funkcji i błędów. W ten sposób możemy łatwiej śledzić rzeczywiste problemy lub błędy w kodzie i oddzielić ogólną dyskusję od faktycznego kodu.

## Jak współtworzyć

### Wytyczne dotyczące pull requestów

Podczas przesyłania pull requesta (PR) do repozytorium Phi-3 CookBook, należy stosować się do następujących wytycznych:

- **Forkuj repozytorium**: Zawsze wykonaj fork repozytorium na swoje konto przed wprowadzeniem modyfikacji.

- **Oddzielne pull requesty (PR)**:
  - Każdy typ zmiany przesyłaj w osobnym pull request. Na przykład poprawki błędów i aktualizacje dokumentacji powinny być przesyłane w osobnych PR.
  - Poprawki literówek i drobne aktualizacje dokumentacji można połączyć w jeden PR, jeśli jest to odpowiednie.

- **Rozwiązywanie konfliktów scalania**: Jeśli Twój pull request pokazuje konflikty scalania, zaktualizuj swoją lokalną gałąź `main`, aby odzwierciedlała główne repozytorium przed wprowadzeniem modyfikacji.

- **Przesyłanie tłumaczeń**: Podczas przesyłania PR z tłumaczeniem upewnij się, że folder tłumaczenia zawiera tłumaczenia wszystkich plików z oryginalnego folderu.

### Wytyczne dotyczące tłumaczeń

> [!IMPORTANT]
>
> Podczas tłumaczenia tekstu w tym repozytorium nie używaj tłumaczeń maszynowych. Zgłaszaj się do tłumaczeń tylko w językach, w których jesteś biegły.

Jeśli biegle posługujesz się językiem innym niż angielski, możesz pomóc w tłumaczeniu treści. Aby Twoje wkłady tłumaczeniowe zostały poprawnie zintegrowane, postępuj zgodnie z poniższymi krokami:

- **Utwórz folder tłumaczenia**: Przejdź do odpowiedniej sekcji folderu i utwórz folder tłumaczenia dla języka, do którego wnosisz wkład. Na przykład:
  - Dla sekcji wstępu: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Dla sekcji szybkiego startu: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Kontynuuj ten wzór dla innych sekcji (03.Inference, 04.Finetuning itd.)

- **Zaktualizuj ścieżki względne**: Podczas tłumaczenia dostosuj strukturę folderów, dodając `../../` na początku ścieżek względnych w plikach markdown, aby upewnić się, że linki działają poprawnie. Na przykład zmień następująco:
  - Zmień `(../../imgs/01/phi3aisafety.png)` na `(../../../../imgs/01/phi3aisafety.png)`

- **Organizuj swoje tłumaczenia**: Każdy przetłumaczony plik powinien być umieszczony w odpowiednim folderze tłumaczeń sekcji. Na przykład, jeśli tłumaczysz sekcję wstępu na hiszpański, utwórz następująco:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Przesyłaj kompletny PR**: Upewnij się, że wszystkie przetłumaczone pliki dla sekcji są uwzględnione w jednym PR. Nie akceptujemy częściowych tłumaczeń dla sekcji. Podczas przesyłania PR z tłumaczeniem upewnij się, że folder tłumaczenia zawiera tłumaczenia wszystkich plików z oryginalnego folderu.

### Wytyczne dotyczące pisania

Aby zapewnić spójność we wszystkich dokumentach, stosuj się do następujących wytycznych:

- **Formatowanie URL**: Owiń wszystkie URL w nawiasy kwadratowe, a następnie w nawiasy okrągłe, bez dodatkowych spacji wokół lub wewnątrz nich. Na przykład: `[example](https://example.com)`.

- **Linki względne**: Używaj `./` dla linków względnych wskazujących na pliki lub foldery w bieżącym katalogu oraz `../` dla tych w katalogu nadrzędnym. Na przykład: `[example](../../path/to/file)` lub `[example](../../../path/to/file)`.

- **Unikaj lokalizacji specyficznych dla kraju**: Upewnij się, że Twoje linki nie zawierają lokalizacji specyficznych dla kraju. Na przykład, unikaj `/en-us/` lub `/en/`.

- **Przechowywanie obrazów**: Przechowuj wszystkie obrazy w folderze `./imgs`.

- **Opisowe nazwy obrazów**: Nazywaj obrazy opisowo, używając angielskich znaków, cyfr i myślników. Na przykład: `example-image.jpg`.

## Przepływy pracy GitHub

Podczas przesyłania pull requesta zostaną uruchomione następujące przepływy pracy w celu weryfikacji zmian. Postępuj zgodnie z poniższymi instrukcjami, aby upewnić się, że Twój pull request przejdzie kontrole przepływu pracy:

- [Sprawdź uszkodzone ścieżki względne](../..)
- [Sprawdź, czy URL nie mają lokalizacji](../..)

### Sprawdź uszkodzone ścieżki względne

Ten przepływ pracy zapewnia, że wszystkie ścieżki względne w Twoich plikach są poprawne.

1. Aby upewnić się, że Twoje linki działają poprawnie, wykonaj następujące zadania w VS Code:
    - Najedź kursorem na dowolny link w swoich plikach.
    - Naciśnij **Ctrl + Klik**, aby przejść do linku.
    - Jeśli klikniesz link i nie działa on lokalnie, uruchomi to przepływ pracy i nie zadziała na GitHubie.

1. Aby rozwiązać ten problem, wykonaj następujące zadania korzystając z sugestii ścieżek oferowanych przez VS Code:
    - Wpisz `./` lub `../`.
    - VS Code zasugeruje dostępne opcje w oparciu o to, co wpisałeś.
    - Podążaj za ścieżką, klikając na żądany plik lub folder, aby upewnić się, że ścieżka jest poprawna.

Po dodaniu poprawnej ścieżki względnej zapisz i wypchnij swoje zmiany.

### Sprawdź, czy URL nie mają lokalizacji

Ten przepływ pracy zapewnia, że żaden URL w Twoich plikach nie zawiera lokalizacji specyficznej dla kraju. Ponieważ to repozytorium jest dostępne globalnie, ważne jest, aby URL nie zawierały lokalizacji Twojego kraju.

1. Aby zweryfikować, że Twoje URL nie mają lokalizacji kraju, wykonaj następujące zadania:

    - Sprawdź teksty, takie jak `/en-us/`, `/en/` lub inne lokalizacje językowe w URL.
    - Jeśli te nie występują w Twoich URL, przejdziesz tę kontrolę.

1. Aby rozwiązać ten problem, wykonaj następujące zadania:
    - Otwórz ścieżkę pliku wskazaną przez przepływ pracy.
    - Usuń lokalizację kraju z URL.

Po usunięciu lokalizacji kraju zapisz i wypchnij swoje zmiany.

### Sprawdź uszkodzone URL

Ten przepływ pracy zapewnia, że każdy URL w Twoich plikach działa i zwraca kod statusu 200.

1. Aby zweryfikować, że Twoje URL działają poprawnie, wykonaj następujące zadania:
    - Sprawdź status URL w swoich plikach.

2. Aby naprawić uszkodzone URL, wykonaj następujące zadania:
    - Otwórz plik, który zawiera uszkodzony URL.
    - Zaktualizuj URL na poprawny.

Po naprawieniu URL zapisz i wypchnij swoje zmiany.

> [!NOTE]
>
> Mogą wystąpić przypadki, w których sprawdzanie URL zakończy się niepowodzeniem, mimo że link jest dostępny. Może się to zdarzyć z kilku powodów, w tym:
>
> - **Ograniczenia sieciowe:** Serwery GitHub Actions mogą mieć ograniczenia sieciowe uniemożliwiające dostęp do niektórych URL.
> - **Problemy z czasem odpowiedzi:** URL, które potrzebują zbyt dużo czasu na odpowiedź, mogą wywołać błąd przekroczenia czasu w przepływie pracy.
> - **Tymczasowe problemy serwera:** Okazjonalne przestoje serwera lub konserwacja mogą tymczasowo uniemożliwić dostęp do URL podczas walidacji.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku kluczowych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.