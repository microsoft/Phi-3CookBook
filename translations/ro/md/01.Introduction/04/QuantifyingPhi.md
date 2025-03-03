# **Cuantificarea Familiei Phi**

Cuantificarea modelului se referă la procesul de mapare a parametrilor (cum ar fi greutățile și valorile de activare) dintr-un model de rețea neuronală de la un interval mare de valori (de obicei un interval continuu) la un interval finit mai mic de valori. Această tehnologie poate reduce dimensiunea și complexitatea computațională a modelului și poate îmbunătăți eficiența funcționării acestuia în medii cu resurse limitate, cum ar fi dispozitivele mobile sau sistemele încorporate. Cuantificarea modelului realizează compresia prin reducerea preciziei parametrilor, dar introduce și o anumită pierdere de precizie. Prin urmare, în procesul de cuantificare, este necesar să se găsească un echilibru între dimensiunea modelului, complexitatea computațională și precizie. Metodele comune de cuantificare includ cuantificarea pe punct fix, cuantificarea pe punct flotant etc. Puteți alege strategia de cuantificare potrivită în funcție de scenariul specific și de nevoi.

Ne dorim să implementăm modelul GenAI pe dispozitive edge și să permitem accesul unui număr mai mare de dispozitive la scenarii GenAI, cum ar fi dispozitivele mobile, AI PC/Copilot+PC și dispozitivele IoT tradiționale. Prin cuantificarea modelului, îl putem implementa pe diferite dispozitive edge, în funcție de specificațiile fiecăruia. Combinând cadrul de accelerare a modelului și modelele cuantificate oferite de producătorii de hardware, putem construi scenarii mai bune de aplicații SLM.

În scenariul de cuantificare, avem diferite precizii (INT4, INT8, FP16, FP32). Mai jos este o explicație a celor mai utilizate precizii de cuantificare.

### **INT4**

Cuantificarea INT4 este o metodă radicală de cuantificare care convertește greutățile și valorile de activare ale modelului în numere întregi pe 4 biți. Cuantificarea INT4 duce de obicei la o pierdere mai mare de precizie din cauza intervalului mai mic de reprezentare și a preciziei mai reduse. Cu toate acestea, comparativ cu cuantificarea INT8, INT4 poate reduce și mai mult cerințele de stocare și complexitatea computațională a modelului. Este important de menționat că cuantificarea INT4 este relativ rar utilizată în aplicațiile practice, deoarece precizia prea scăzută poate cauza o degradare semnificativă a performanței modelului. În plus, nu toate hardware-urile suportă operațiuni INT4, așa că compatibilitatea hardware trebuie luată în considerare atunci când se alege metoda de cuantificare.

### **INT8**

Cuantificarea INT8 implică procesul de conversie a greutăților și activărilor unui model din numere pe punct flotant în numere întregi pe 8 biți. Deși intervalul numeric reprezentat de numerele întregi INT8 este mai mic și mai puțin precis, această metodă poate reduce semnificativ cerințele de stocare și calcul. În cuantificarea INT8, greutățile și valorile de activare ale modelului trec printr-un proces de cuantificare, care include scalare și offset, pentru a păstra cât mai mult informațiile inițiale pe punct flotant. În timpul inferenței, aceste valori cuantificate vor fi de-cuantificate înapoi la numere pe punct flotant pentru calcul, apoi cuantificate din nou la INT8 pentru pasul următor. Această metodă poate oferi o precizie suficientă în majoritatea aplicațiilor, menținând în același timp o eficiență computațională ridicată.

### **FP16**

Formatul FP16, adică numere pe punct flotant de 16 biți (float16), reduce consumul de memorie la jumătate comparativ cu numerele pe punct flotant de 32 biți (float32), ceea ce are avantaje semnificative în aplicațiile de învățare profundă la scară largă. Formatul FP16 permite încărcarea unor modele mai mari sau procesarea unui volum mai mare de date în limitele aceleiași memorii GPU. Pe măsură ce hardware-ul modern GPU continuă să suporte operațiuni FP16, utilizarea formatului FP16 poate aduce și îmbunătățiri în viteza de calcul. Cu toate acestea, formatul FP16 are și dezavantaje inerente, cum ar fi precizia mai redusă, care poate duce la instabilitate numerică sau pierdere de precizie în anumite cazuri.

### **FP32**

Formatul FP32 oferă o precizie mai mare și poate reprezenta cu exactitate un interval larg de valori. În scenariile în care se efectuează operațiuni matematice complexe sau sunt necesare rezultate de înaltă precizie, formatul FP32 este preferat. Totuși, precizia ridicată înseamnă și un consum mai mare de memorie și un timp de calcul mai lung. Pentru modelele de învățare profundă la scară largă, mai ales atunci când există mulți parametri ai modelului și un volum uriaș de date, formatul FP32 poate duce la insuficiență de memorie GPU sau la o scădere a vitezei de inferență.

Pe dispozitive mobile sau IoT, putem converti modelele Phi-3.x la INT4, în timp ce pe AI PC / Copilot PC putem utiliza precizii mai mari, cum ar fi INT8, FP16, FP32.

În prezent, diferiți producători de hardware au cadre diferite pentru a suporta modele generative, cum ar fi OpenVINO de la Intel, QNN de la Qualcomm, MLX de la Apple și CUDA de la Nvidia. Acestea, combinate cu cuantificarea modelului, permit implementarea locală.

Din punct de vedere tehnologic, avem suport pentru diferite formate după cuantificare, cum ar fi formatele PyTorch / Tensorflow, GGUF și ONNX. Am realizat o comparație între GGUF și ONNX și scenariile lor de aplicare. Aici recomand formatul de cuantificare ONNX, care beneficiază de un suport bun de la cadrul modelului până la hardware. În acest capitol, ne vom concentra pe utilizarea ONNX Runtime pentru GenAI, OpenVINO și Apple MLX pentru a efectua cuantificarea modelului (dacă aveți o metodă mai bună, ne puteți transmite printr-un PR).

**Acest capitol include**

1. [Cuantificarea Phi-3.5 / 4 folosind llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Cuantificarea Phi-3.5 / 4 folosind extensii Generative AI pentru onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Cuantificarea Phi-3.5 / 4 folosind Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Cuantificarea Phi-3.5 / 4 folosind cadrul Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.