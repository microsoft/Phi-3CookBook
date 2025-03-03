# Bine ai venit la extensia ta VS Code

## Ce conține acest folder

* Acest folder conține toate fișierele necesare pentru extensia ta.
* `package.json` - acesta este fișierul manifest în care declari extensia și comanda ta.
  * Pluginul de exemplu înregistrează o comandă și definește titlul și numele comenzii. Cu aceste informații, VS Code poate afișa comanda în paleta de comenzi. Deocamdată, nu este nevoie să încarci pluginul.
* `src/extension.ts` - acesta este fișierul principal unde vei implementa comanda ta.
  * Fișierul exportă o funcție, `activate`, care este apelată prima dată când extensia ta este activată (în acest caz, prin executarea comenzii). În interiorul funcției `activate` apelăm `registerCommand`.
  * Transmitem funcția care conține implementarea comenzii ca al doilea parametru către `registerCommand`.

## Configurare

* instalează extensiile recomandate (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner și dbaeumer.vscode-eslint)

## Începe rapid

* Apasă `F5` pentru a deschide o fereastră nouă cu extensia ta încărcată.
* Rulează comanda ta din paleta de comenzi apăsând (`Ctrl+Shift+P` sau `Cmd+Shift+P` pe Mac) și tastând `Hello World`.
* Pune puncte de întrerupere în codul tău în interiorul `src/extension.ts` pentru a depana extensia.
* Găsește ieșirea extensiei tale în consola de depanare.

## Fă modificări

* Poți relansa extensia din bara de instrumente de depanare după ce modifici codul în `src/extension.ts`.
* De asemenea, poți reîncărca (`Ctrl+R` sau `Cmd+R` pe Mac) fereastra VS Code cu extensia ta pentru a încărca modificările.

## Explorează API-ul

* Poți deschide întregul set de API-uri când deschizi fișierul `node_modules/@types/vscode/index.d.ts`.

## Rulează teste

* Instalează [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Rulează sarcina "watch" prin comanda **Tasks: Run Task**. Asigură-te că aceasta rulează, altfel testele s-ar putea să nu fie descoperite.
* Deschide vizualizarea Testing din bara de activități și apasă butonul "Run Test" sau folosește combinația de taste `Ctrl/Cmd + ; A`.
* Vezi rezultatele testelor în vizualizarea Test Results.
* Fă modificări în `src/test/extension.test.ts` sau creează fișiere noi de test în folderul `test`.
  * Runner-ul de test oferit va lua în considerare doar fișierele care se potrivesc cu modelul de nume `**.test.ts`.
  * Poți crea foldere în interiorul folderului `test` pentru a structura testele cum dorești.

## Mergi mai departe

* Reduce dimensiunea extensiei și îmbunătățește timpul de pornire prin [comprimarea extensiei](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publică extensia ta](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) pe piața de extensii VS Code.
* Automatizează construcțiile configurând [Integrarea Continuă](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși depunem eforturi pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa de bază, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.