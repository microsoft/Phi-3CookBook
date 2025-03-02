# Bine ai venit la extensia ta pentru VS Code

## Ce conține acest folder

* Acest folder conține toate fișierele necesare pentru extensia ta.
* `package.json` - acesta este fișierul manifest în care declari extensia și comanda ta.
  * Pluginul de exemplu înregistrează o comandă și definește titlul și numele comenzii. Cu aceste informații, VS Code poate afișa comanda în paleta de comenzi. Nu este nevoie să încarce încă pluginul.
* `src/extension.ts` - acesta este fișierul principal unde vei furniza implementarea comenzii tale.
  * Fișierul exportă o funcție, `activate`, care este apelată prima dată când extensia ta este activată (în acest caz, prin executarea comenzii). În interiorul funcției `activate` apelăm `registerCommand`.
  * Transmitem funcția care conține implementarea comenzii ca al doilea parametru către `registerCommand`.

## Configurare

* Instalează extensiile recomandate (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner și dbaeumer.vscode-eslint)

## Pornește imediat

* Apasă `F5` pentru a deschide o fereastră nouă cu extensia ta încărcată.
* Rulează comanda ta din paleta de comenzi apăsând (`Ctrl+Shift+P` sau `Cmd+Shift+P` pe Mac) și tastând `Hello World`.
* Setează puncte de întrerupere în codul tău în interiorul `src/extension.ts` pentru a depana extensia.
* Găsește ieșirea extensiei tale în consola de depanare.

## Fă modificări

* Poți relansa extensia din bara de instrumente de depanare după ce modifici codul în `src/extension.ts`.
* Poți, de asemenea, reîncărca (`Ctrl+R` sau `Cmd+R` pe Mac) fereastra VS Code cu extensia ta pentru a încărca modificările.

## Explorează API-ul

* Poți deschide setul complet de API-uri atunci când deschizi fișierul `node_modules/@types/vscode/index.d.ts`.

## Rulează teste

* Instalează [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Rulează sarcina "watch" prin comanda **Tasks: Run Task**. Asigură-te că aceasta rulează, altfel testele ar putea să nu fie descoperite.
* Deschide vizualizarea Testing din bara de activitate și apasă pe butonul "Run Test", sau folosește scurtătura `Ctrl/Cmd + ; A`.
* Vezi rezultatul testelor în vizualizarea Test Results.
* Fă modificări în `src/test/extension.test.ts` sau creează fișiere noi de test în folderul `test`.
  * Runner-ul de test furnizat va lua în considerare doar fișierele care corespund modelului de nume `**.test.ts`.
  * Poți crea foldere în interiorul folderului `test` pentru a structura testele așa cum dorești.

## Mergi mai departe

* Reduce dimensiunea extensiei și îmbunătățește timpul de pornire prin [împachetarea extensiei](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publică extensia ta](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) pe marketplace-ul de extensii VS Code.
* Automatizează build-urile configurând [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa maternă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.