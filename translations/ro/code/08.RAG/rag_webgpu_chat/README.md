Phi-3-mini WebGPU RAG Chatbot

## Demo pentru prezentarea WebGPU și modelul RAG
Modelul RAG cu Phi-3 Onnx Hosted utilizează abordarea Retrieval-Augmented Generation, combinând puterea modelelor Phi-3 cu hostingul ONNX pentru implementări eficiente ale AI. Acest model este esențial pentru ajustarea fină a modelelor pentru sarcini specifice domeniului, oferind un amestec de calitate, eficiență economică și înțelegere pe termen lung. Este parte din suita Azure AI, oferind o selecție largă de modele ușor de găsit, testat și utilizat, adaptate nevoilor de personalizare ale diferitelor industrii. Modelele Phi-3, inclusiv Phi-3-mini, Phi-3-small și Phi-3-medium, sunt disponibile în Azure AI Model Catalog și pot fi ajustate și implementate independent sau prin platforme precum HuggingFace și ONNX, demonstrând angajamentul Microsoft pentru soluții AI accesibile și eficiente.

## Ce este WebGPU 
WebGPU este o API modernă pentru grafică web, concepută pentru a oferi acces eficient la unitatea de procesare grafică (GPU) a unui dispozitiv direct din browserele web. Este destinat să fie succesorul WebGL, oferind mai multe îmbunătățiri esențiale:

1. **Compatibilitate cu GPU-uri moderne**: WebGPU este construit pentru a funcționa perfect cu arhitecturi GPU contemporane, utilizând API-uri de sistem precum Vulkan, Metal și Direct3D 12.
2. **Performanță îmbunătățită**: Suportă calcule GPU de uz general și operațiuni mai rapide, fiind potrivit atât pentru randarea grafică, cât și pentru sarcini de învățare automată.
3. **Funcționalități avansate**: WebGPU oferă acces la capabilități GPU mai avansate, permițând sarcini grafice și computaționale mai complexe și dinamice.
4. **Reducerea sarcinii JavaScript**: Prin delegarea mai multor sarcini către GPU, WebGPU reduce semnificativ sarcina JavaScript, conducând la performanțe mai bune și experiențe mai fluide.

WebGPU este în prezent suportat în browsere precum Google Chrome, cu lucrări în desfășurare pentru a extinde suportul pe alte platforme.

### 03.WebGPU
Mediu necesar:

**Browsere suportate:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Activarea WebGPU:

- În Chrome/Microsoft Edge 

Activează flag-ul `chrome://flags/#enable-unsafe-webgpu`.

#### Deschide browserul:
Lansează Google Chrome sau Microsoft Edge.

#### Accesează pagina Flags:
În bara de adrese, tastează `chrome://flags` și apasă Enter.

#### Caută flag-ul:
În caseta de căutare din partea de sus a paginii, tastează 'enable-unsafe-webgpu'.

#### Activează flag-ul:
Găsește flag-ul #enable-unsafe-webgpu în lista de rezultate.

Fă clic pe meniul dropdown de lângă acesta și selectează Enabled.

#### Repornește browserul:

După activarea flag-ului, va trebui să repornești browserul pentru ca modificările să intre în vigoare. Fă clic pe butonul Relaunch care apare în partea de jos a paginii.

- Pentru Linux, lansează browserul cu `--enable-features=Vulkan`.
- Safari 18 (macOS 15) are WebGPU activat implicit.
- În Firefox Nightly, introdu about:config în bara de adrese și `set dom.webgpu.enabled to true`.

### Configurarea GPU-ului pentru Microsoft Edge 

Iată pașii pentru a configura un GPU de înaltă performanță pentru Microsoft Edge pe Windows:

- **Deschide Setările:** Fă clic pe meniul Start și selectează Setări.
- **Setări de sistem:** Accesează Sistem și apoi Afișare.
- **Setări grafice:** Derulează în jos și fă clic pe Setări grafice.
- **Alege aplicația:** Sub „Alege o aplicație pentru a seta preferința,” selectează Aplicație desktop și apoi Browse.
- **Selectează Edge:** Navighează la folderul de instalare Edge (de obicei `C:\Program Files (x86)\Microsoft\Edge\Application`) și selectează `msedge.exe`.
- **Setează preferința:** Fă clic pe Opțiuni, alege Performanță înaltă și apoi Salvează.
Aceasta va asigura utilizarea GPU-ului de înaltă performanță de către Microsoft Edge pentru performanțe mai bune. 
- **Repornește** dispozitivul pentru ca aceste setări să intre în vigoare. 

### Deschide Codespace-ul tău:
Navighează la repository-ul tău pe GitHub.
Fă clic pe butonul Code și selectează Open with Codespaces.

Dacă nu ai încă un Codespace, poți crea unul făcând clic pe New codespace.

**Notă** Instalarea mediului Node în Codespace-ul tău
Rularea unui demo npm dintr-un GitHub Codespace este o modalitate excelentă de a testa și dezvolta proiectul tău. Iată un ghid pas cu pas pentru a începe:

### Configurează-ți mediul:
Odată ce Codespace-ul este deschis, asigură-te că ai Node.js și npm instalate. Poți verifica acest lucru rulând:
```
node -v
```
```
npm -v
```

Dacă nu sunt instalate, le poți instala folosind:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navighează la directorul proiectului tău:
Folosește terminalul pentru a naviga la directorul unde se află proiectul tău npm:
```
cd path/to/your/project
```

### Instalează dependențele:
Rulează următoarea comandă pentru a instala toate dependențele necesare listate în fișierul package.json:

```
npm install
```

### Rulează demo-ul:
După ce dependențele sunt instalate, poți rula scriptul demo. De exemplu, dacă scriptul demo se numește start, poți rula:

```
npm run build
```
```
npm run dev
```

### Accesează demo-ul:
Dacă demo-ul implică un server web, Codespaces va oferi un URL pentru a-l accesa. Caută o notificare sau verifică tab-ul Ports pentru a găsi URL-ul.

**Notă:** Modelul trebuie să fie cache-uit în browser, așa că poate dura ceva timp pentru a se încărca. 

### Demo RAG
Încarcă fișierul markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selectează fișierul tău:
Fă clic pe butonul „Choose File” pentru a selecta documentul pe care vrei să-l încarci.

### Încarcă documentul:
După ce ai selectat fișierul, fă clic pe butonul „Upload” pentru a încărca documentul pentru RAG (Retrieval-Augmented Generation).

### Începe conversația:
Odată ce documentul este încărcat, poți începe o sesiune de chat folosind RAG bazat pe conținutul documentului tău.

**Declinarea responsabilității**:  
Acest document a fost tradus utilizând servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa natală, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.