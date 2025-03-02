# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo pentru a prezenta WebGPU și modelul RAG

Modelul RAG cu Phi-3.5 Onnx Hosted folosește abordarea Retrieval-Augmented Generation, combinând puterea modelelor Phi-3.5 cu găzduirea ONNX pentru implementări eficiente ale inteligenței artificiale. Acest model este esențial pentru ajustarea fină a modelelor pentru sarcini specifice unui domeniu, oferind un echilibru între calitate, eficiență economică și înțelegerea contextului extins. Face parte din suita Azure AI, oferind o gamă largă de modele care sunt ușor de găsit, testat și utilizat, adaptându-se nevoilor de personalizare din diverse industrii.

## Ce este WebGPU 
WebGPU este o API modernă pentru grafică web, concepută pentru a oferi acces eficient la unitatea de procesare grafică (GPU) a unui dispozitiv direct din browserele web. Este destinată să fie succesorul WebGL, oferind mai multe îmbunătățiri cheie:

1. **Compatibilitate cu GPU-uri moderne**: WebGPU este construit pentru a funcționa fără probleme cu arhitecturi GPU contemporane, utilizând API-uri de sistem precum Vulkan, Metal și Direct3D 12.
2. **Performanță îmbunătățită**: Suportă calcule generale pe GPU și operațiuni mai rapide, fiind potrivit atât pentru redarea graficii, cât și pentru sarcini de învățare automată.
3. **Funcționalități avansate**: WebGPU oferă acces la capabilități GPU mai avansate, permițând sarcini grafice și de calcul mai complexe și mai dinamice.
4. **Reducerea încărcării JavaScript**: Prin delegarea mai multor sarcini către GPU, WebGPU reduce semnificativ încărcarea JavaScript, ducând la performanțe mai bune și experiențe mai fluide.

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

#### Accesează pagina de setări Flags:
În bara de adrese, tastează `chrome://flags` și apasă Enter.

#### Caută flag-ul:
În caseta de căutare din partea de sus a paginii, tastează 'enable-unsafe-webgpu'.

#### Activează flag-ul:
Găsește flag-ul #enable-unsafe-webgpu în lista de rezultate.

Dă clic pe meniul dropdown de lângă acesta și selectează Enabled.

#### Repornește browserul:

După activarea flag-ului, va trebui să repornești browserul pentru ca modificările să intre în vigoare. Apasă butonul Relaunch care apare în partea de jos a paginii.

- Pentru Linux, lansează browserul cu `--enable-features=Vulkan`.
- Safari 18 (macOS 15) are WebGPU activat implicit.
- În Firefox Nightly, tastează about:config în bara de adrese și `set dom.webgpu.enabled to true`.

### Configurarea GPU-ului pentru Microsoft Edge 

Iată pașii pentru a configura un GPU de înaltă performanță pentru Microsoft Edge pe Windows:

- **Deschide Setări:** Dă clic pe meniul Start și selectează Setări.
- **Setări de sistem:** Mergi la Sistem și apoi la Afișaj.
- **Setări grafice:** Derulează în jos și dă clic pe Setări grafice.
- **Alege aplicația:** Sub „Alege o aplicație pentru a seta preferința,” selectează Aplicație desktop și apoi Răsfoiește.
- **Selectează Edge:** Navighează la folderul de instalare Edge (de obicei `C:\Program Files (x86)\Microsoft\Edge\Application`) și selectează `msedge.exe`.
- **Setează preferința:** Dă clic pe Opțiuni, alege Performanță înaltă, apoi dă clic pe Salvare.
Aceasta va asigura că Microsoft Edge folosește GPU-ul tău de înaltă performanță pentru performanțe mai bune. 
- **Repornește** dispozitivul pentru ca aceste setări să intre în vigoare.

### Exemple: Te rog [apasă acest link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană realizată de profesioniști. Nu ne asumăm răspunderea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.