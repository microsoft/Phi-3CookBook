# Contribuind

Acest proiect încurajează contribuțiile și sugestiile. Majoritatea contribuțiilor necesită acordul dumneavoastră pentru un Contributor License Agreement (CLA), prin care declarați că aveți dreptul de a ne acorda permisiunea de a utiliza contribuția dumneavoastră. Pentru detalii, vizitați [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Când trimiteți un pull request, un bot CLA va determina automat dacă trebuie să furnizați un CLA și va adăuga o etichetă corespunzătoare PR-ului (de exemplu, verificarea statusului, comentariu). Urmați pur și simplu instrucțiunile furnizate de bot. Acest lucru va trebui făcut o singură dată pentru toate depozitele care folosesc CLA-ul nostru.

## Cod de Conduită

Acest proiect a adoptat [Codul de Conduită Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Pentru mai multe informații, citiți [Întrebările frecvente despre Codul de Conduită](https://opensource.microsoft.com/codeofconduct/faq/) sau contactați [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Atenție la crearea problemelor

Vă rugăm să nu deschideți probleme pe GitHub pentru întrebări generale de suport, deoarece lista GitHub ar trebui utilizată pentru cereri de funcționalități și rapoarte de erori. În acest fel, putem urmări mai ușor problemele sau erorile reale din cod și putem păstra discuțiile generale separate de codul propriu-zis.

## Cum să contribuiți

### Ghiduri pentru Pull Requests

Când trimiteți un pull request (PR) către depozitul Phi-3 CookBook, vă rugăm să respectați următoarele ghiduri:

- **Fork al depozitului**: Faceți întotdeauna un fork al depozitului în contul dumneavoastră înainte de a face modificările.

- **Pull requests separate (PR)**:
  - Trimiteți fiecare tip de modificare într-un PR separat. De exemplu, corectările de erori și actualizările de documentație ar trebui trimise în PR-uri separate.
  - Corectările de greșeli de tipar și actualizările minore de documentație pot fi combinate într-un singur PR, dacă este cazul.

- **Gestionați conflictele de îmbinare**: Dacă pull request-ul dumneavoastră prezintă conflicte de îmbinare, actualizați ramura locală `main` pentru a reflecta depozitul principal înainte de a face modificările.

- **Trimiteri de traduceri**: Când trimiteți un PR de traducere, asigurați-vă că folderul de traducere include traduceri pentru toate fișierele din folderul original.

### Ghiduri pentru traduceri

> [!IMPORTANT]
>
> Când traduceți text în acest depozit, nu utilizați traducerea automată. Voluntariați doar pentru traduceri în limbile în care aveți competență.

Dacă sunteți competent într-o limbă non-engleză, puteți ajuta la traducerea conținutului. Urmați acești pași pentru a vă asigura că contribuțiile dumneavoastră de traducere sunt integrate corect, utilizând următoarele ghiduri:

- **Creați un folder de traducere**: Navigați la folderul secțiunii corespunzătoare și creați un folder de traducere pentru limba la care contribuiți. De exemplu:
  - Pentru secțiunea de introducere: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Pentru secțiunea de început rapid: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continuați acest model pentru alte secțiuni (03.Inference, 04.Finetuning, etc.)

- **Actualizați căile relative**: Când traduceți, ajustați structura folderului adăugând `../../` la începutul căilor relative din fișierele markdown pentru a vă asigura că linkurile funcționează corect. De exemplu, schimbați astfel:
  - Schimbați `(../../imgs/01/phi3aisafety.png)` în `(../../../../imgs/01/phi3aisafety.png)`

- **Organizați traducerile**: Fiecare fișier tradus trebuie plasat în folderul de traducere corespunzător secțiunii. De exemplu, dacă traduceți secțiunea de introducere în spaniolă, ar trebui să creați astfel:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Trimiteți un PR complet**: Asigurați-vă că toate fișierele traduse pentru o secțiune sunt incluse într-un singur PR. Nu acceptăm traduceri parțiale pentru o secțiune. Când trimiteți un PR de traducere, asigurați-vă că folderul de traducere include traduceri pentru toate fișierele din folderul original.

### Ghiduri pentru redactare

Pentru a asigura consistența în toate documentele, vă rugăm să utilizați următoarele ghiduri:

- **Formatul URL-urilor**: Înconjurați toate URL-urile cu paranteze pătrate urmate de paranteze rotunde, fără spații suplimentare în jur sau în interior. De exemplu: `[example](https://www.microsoft.com)`.

- **Linkuri relative**: Utilizați `./` pentru linkurile relative care indică fișiere sau foldere din directorul curent și `../` pentru cele dintr-un director părinte. De exemplu: `[example](../../path/to/file)` sau `[example](../../../path/to/file)`.

- **Fără locale specifice țării**: Asigurați-vă că linkurile dumneavoastră nu includ locale specifice țării. De exemplu, evitați `/en-us/` sau `/en/`.

- **Stocarea imaginilor**: Stocați toate imaginile în folderul `./imgs`.

- **Nume descriptive pentru imagini**: Denumiți imaginile descriptiv folosind caractere englezești, numere și cratime. De exemplu: `example-image.jpg`.

## Fluxuri de lucru GitHub

Când trimiteți un pull request, următoarele fluxuri de lucru vor fi declanșate pentru a valida modificările. Urmați instrucțiunile de mai jos pentru a vă asigura că pull request-ul dumneavoastră trece verificările fluxurilor de lucru:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Acest flux de lucru asigură că toate căile relative din fișierele dumneavoastră sunt corecte.

1. Pentru a vă asigura că linkurile dumneavoastră funcționează corect, efectuați următoarele sarcini utilizând VS Code:
    - Plasați cursorul peste orice link din fișierele dumneavoastră.
    - Apăsați **Ctrl + Click** pentru a naviga la link.
    - Dacă faceți clic pe un link și acesta nu funcționează local, fluxul de lucru va fi declanșat și nu va funcționa pe GitHub.

1. Pentru a rezolva această problemă, efectuați următoarele sarcini utilizând sugestiile de cale furnizate de VS Code:
    - Tastați `./` sau `../`.
    - VS Code vă va solicita să alegeți dintre opțiunile disponibile bazate pe ceea ce ați tastat.
    - Urmați calea făcând clic pe fișierul sau folderul dorit pentru a vă asigura că calea este corectă.

După ce ați adăugat calea relativă corectă, salvați și împingeți modificările.

### Check URLs Don't Have Locale

Acest flux de lucru asigură că orice URL web nu include un locale specific țării. Deoarece acest depozit este accesibil global, este important să vă asigurați că URL-urile nu conțin localele țării dumneavoastră.

1. Pentru a verifica că URL-urile dumneavoastră nu au locale de țară, efectuați următoarele sarcini:

    - Verificați text precum `/en-us/`, `/en/` sau orice alt locale de limbă în URL-uri.
    - Dacă acestea nu sunt prezente în URL-urile dumneavoastră, veți trece această verificare.

1. Pentru a rezolva această problemă, efectuați următoarele sarcini:
    - Deschideți calea fișierului evidențiată de fluxul de lucru.
    - Eliminați localele țării din URL-uri.

După ce eliminați localele țării, salvați și împingeți modificările.

### Check Broken Urls

Acest flux de lucru asigură că orice URL web din fișierele dumneavoastră funcționează și returnează codul de status 200.

1. Pentru a verifica că URL-urile dumneavoastră funcționează corect, efectuați următoarele sarcini:
    - Verificați statusul URL-urilor din fișierele dumneavoastră.

2. Pentru a rezolva URL-urile defecte, efectuați următoarele sarcini:
    - Deschideți fișierul care conține URL-ul defect.
    - Actualizați URL-ul la unul corect.

După ce ați corectat URL-urile, salvați și împingeți modificările.

> [!NOTE]
>
> Pot exista cazuri în care verificarea URL-urilor eșuează chiar dacă linkul este accesibil. Acest lucru se poate întâmpla din mai multe motive, inclusiv:
>
> - **Restricții de rețea:** Serverele GitHub Actions pot avea restricții de rețea care împiedică accesul la anumite URL-uri.
> - **Probleme de timeout:** URL-urile care răspund prea lent pot declanșa o eroare de timeout în fluxul de lucru.
> - **Probleme temporare ale serverului:** Opririle temporare ale serverului sau întreținerea pot face un URL indisponibil temporar în timpul validării.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.