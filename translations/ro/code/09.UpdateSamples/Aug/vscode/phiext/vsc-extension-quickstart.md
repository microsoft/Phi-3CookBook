# Bine ai venit la extensia ta pentru VS Code

## Ce conține folderul

* Acest folder conține toate fișierele necesare pentru extensia ta.
* `package.json` - acesta este fișierul manifest în care declari extensia și comanda ta.
  * Plugin-ul de exemplu înregistrează o comandă și definește titlul și numele comenzii. Cu aceste informații, VS Code poate afișa comanda în paleta de comenzi. Nu este necesar încă să încarci plugin-ul.
* `src/extension.ts` - acesta este fișierul principal în care vei furniza implementarea comenzii tale.
  * Fișierul exportă o funcție, `activate`, care este apelată prima dată când extensia ta este activată (în acest caz prin executarea comenzii). În interiorul funcției `activate` apelăm `registerCommand`.
  * Transmitem funcția care conține implementarea comenzii ca al doilea parametru pentru `registerCommand`.

## Configurare

* Instalează extensiile recomandate (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner și dbaeumer.vscode-eslint)

## Începe rapid

* Apasă `F5` pentru a deschide o fereastră nouă cu extensia ta încărcată.
* Rulează comanda ta din paleta de comenzi apăsând (`Ctrl+Shift+P` sau `Cmd+Shift+P` pe Mac) și tastând `Hello World`.
* Setează puncte de întrerupere în codul tău din `src/extension.ts` pentru a depana extensia.
* Găsește ieșirea extensiei tale în consola de depanare.

## Fă modificări

* Poți relansa extensia din bara de instrumente de depanare după ce modifici codul în `src/extension.ts`.
* De asemenea, poți reîncărca (`Ctrl+R` sau `Cmd+R` pe Mac) fereastra VS Code cu extensia ta pentru a încărca modificările.

## Explorează API-ul

* Poți deschide setul complet al API-ului nostru atunci când deschizi fișierul `node_modules/@types/vscode/index.d.ts`.

## Rulează teste

* Instalează [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Rulează sarcina "watch" prin comanda **Tasks: Run Task**. Asigură-te că aceasta este în execuție, altfel testele s-ar putea să nu fie descoperite.
* Deschide vizualizarea Testing din bara de activități și apasă pe butonul "Run Test" sau folosește combinația de taste `Ctrl/Cmd + ; A`.
* Vezi rezultatul testelor în vizualizarea Test Results.
* Fă modificări în `src/test/extension.test.ts` sau creează fișiere noi de test în folderul `test`.
  * Runner-ul de test furnizat va considera doar fișierele care respectă modelul de nume `**.test.ts`.
  * Poți crea foldere în interiorul folderului `test` pentru a structura testele oricum dorești.

## Mergi mai departe

* Redu dimensiunea extensiei și îmbunătățește timpul de pornire prin [gruparea extensiei tale](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publică extensia ta](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) pe piața de extensii VS Code.
* Automatizează construcțiile configurând [Integrarea Continuă](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși depunem eforturi pentru acuratețe, vă rugăm să fiți conștienți de faptul că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa de autoritate. Pentru informații critice, se recomandă traducerea umană realizată de profesioniști. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.