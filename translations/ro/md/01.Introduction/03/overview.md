În contextul Phi-3-mini, inferența se referă la procesul de utilizare a modelului pentru a face predicții sau a genera rezultate pe baza datelor de intrare. Permite-mi să-ți ofer mai multe detalii despre Phi-3-mini și capacitățile sale de inferență.

Phi-3-mini face parte din seria de modele Phi-3 lansată de Microsoft. Aceste modele sunt concepute pentru a redefini ceea ce este posibil cu Modelele de Limbaj Mici (SLM).

Iată câteva puncte cheie despre Phi-3-mini și capacitățile sale de inferență:

## **Prezentare generală Phi-3-mini:**
- Phi-3-mini are o dimensiune de 3,8 miliarde de parametri.
- Poate rula nu doar pe dispozitive de calcul tradiționale, ci și pe dispozitive de tip edge, precum dispozitive mobile și dispozitive IoT.
- Lansarea Phi-3-mini permite indivizilor și companiilor să implementeze SLM-uri pe diferite dispozitive hardware, mai ales în medii cu resurse limitate.
- Acoperă diverse formate de model, inclusiv formatul tradițional PyTorch, versiunea cuantificată a formatului gguf și versiunea cuantificată bazată pe ONNX.

## **Accesarea Phi-3-mini:**
Pentru a accesa Phi-3-mini, poți utiliza [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) într-o aplicație Copilot. Semantic Kernel este în general compatibil cu Azure OpenAI Service, modele open-source pe Hugging Face și modele locale.
De asemenea, poți utiliza [Ollama](https://ollama.com) sau [LlamaEdge](https://llamaedge.com) pentru a apela modele cuantificate. Ollama permite utilizatorilor individuali să apeleze diferite modele cuantificate, în timp ce LlamaEdge oferă disponibilitate cross-platform pentru modelele GGUF.

## **Modele cuantificate:**
Mulți utilizatori preferă să utilizeze modele cuantificate pentru inferență locală. De exemplu, poți rula direct Ollama run Phi-3 sau să-l configurezi offline utilizând un Modelfile. Modelfile specifică calea către fișierul GGUF și formatul promptului.

## **Posibilități AI generative:**
Combinarea SLM-urilor precum Phi-3-mini deschide noi posibilități pentru AI generativă. Inferența este doar primul pas; aceste modele pot fi utilizate pentru diverse sarcini în scenarii cu resurse limitate, latență scăzută și costuri reduse.

## **Dezvăluirea potențialului AI generative cu Phi-3-mini: Un ghid pentru inferență și implementare** 
Află cum să folosești Semantic Kernel, Ollama/LlamaEdge și ONNX Runtime pentru a accesa și realiza inferența cu modelele Phi-3-mini și explorează posibilitățile AI generative în diverse scenarii de aplicații.

**Funcționalități**
Realizează inferența modelului phi3-mini în:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

În concluzie, Phi-3-mini le permite dezvoltatorilor să exploreze diferite formate de model și să valorifice AI-ul generativ în diverse scenarii de aplicații.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa natală, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă utilizarea unei traduceri realizate de un profesionist uman. Nu ne asumăm răspunderea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.