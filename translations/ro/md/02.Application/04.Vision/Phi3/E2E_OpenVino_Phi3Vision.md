Această demonstrație arată cum să folosești un model preantrenat pentru a genera cod Python pe baza unei imagini și a unei cereri textuale.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Iată o explicație pas cu pas:

1. **Importuri și Configurare**:
   - Sunt importate bibliotecile și modulele necesare, inclusiv `requests`, `PIL` pentru procesarea imaginilor și `transformers` pentru gestionarea modelului și procesare.

2. **Încărcarea și Afișarea Imaginilor**:
   - Un fișier imagine (`demo.png`) este deschis folosind biblioteca `PIL` și afișat.

3. **Definirea Cererii**:
   - Este creat un mesaj care include imaginea și o cerere de a genera cod Python pentru a procesa imaginea și a o salva utilizând `plt` (matplotlib).

4. **Încărcarea Procesorului**:
   - `AutoProcessor` este încărcat dintr-un model preantrenat specificat de directorul `out_dir`. Acest procesor va gestiona intrările text și imagine.

5. **Crearea Cererii**:
   - Metoda `apply_chat_template` este utilizată pentru a formata mesajul într-o cerere potrivită pentru model.

6. **Procesarea Intrărilor**:
   - Cererea și imaginea sunt procesate în tensori pe care modelul îi poate înțelege.

7. **Setarea Argumentelor de Generare**:
   - Sunt definite argumentele pentru procesul de generare al modelului, inclusiv numărul maxim de tokeni noi care trebuie generați și dacă să se utilizeze eșantionarea pentru rezultat.

8. **Generarea Codului**:
   - Modelul generează codul Python pe baza intrărilor și a argumentelor de generare. `TextStreamer` este utilizat pentru a gestiona rezultatul, sărind peste cerere și tokenii speciali.

9. **Rezultat**:
   - Codul generat este afișat, iar acesta ar trebui să includă cod Python pentru a procesa imaginea și a o salva conform cererii.

Această demonstrație ilustrează cum să folosești un model preantrenat utilizând OpenVino pentru a genera dinamic cod pe baza intrărilor utilizatorului și a imaginilor.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere automate bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.