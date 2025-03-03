# **Quantificazione della Famiglia Phi**

La quantificazione del modello si riferisce al processo di mappatura dei parametri (come pesi e valori di attivazione) in un modello di rete neurale da un ampio intervallo di valori (di solito un intervallo continuo) a un intervallo di valori finito più piccolo. Questa tecnologia può ridurre la dimensione e la complessità computazionale del modello, migliorando l'efficienza operativa in ambienti con risorse limitate, come dispositivi mobili o sistemi embedded. La quantificazione del modello ottiene compressione riducendo la precisione dei parametri, ma introduce anche una certa perdita di precisione. Pertanto, nel processo di quantificazione è necessario bilanciare dimensione del modello, complessità computazionale e precisione. I metodi di quantificazione più comuni includono la quantificazione a punto fisso, la quantificazione a virgola mobile, ecc. È possibile scegliere la strategia di quantificazione più appropriata in base allo scenario specifico e alle esigenze.

Puntiamo a distribuire il modello GenAI su dispositivi edge, consentendo a un numero maggiore di dispositivi di entrare negli scenari GenAI, come dispositivi mobili, AI PC/Copilot+PC e dispositivi IoT tradizionali. Attraverso il modello quantizzato, possiamo distribuirlo su diversi dispositivi edge in base alle loro caratteristiche. Combinando il framework di accelerazione del modello e il modello quantizzato forniti dai produttori hardware, possiamo costruire scenari applicativi SLM migliori.

Nel contesto della quantificazione, disponiamo di diverse precisioni (INT4, INT8, FP16, FP32). Di seguito una spiegazione delle precisioni di quantificazione più comuni.

### **INT4**

La quantificazione INT4 è un metodo di quantificazione radicale che quantizza i pesi e i valori di attivazione del modello in interi a 4 bit. La quantificazione INT4 di solito comporta una maggiore perdita di precisione a causa del ridotto intervallo di rappresentazione e della minore precisione. Tuttavia, rispetto alla quantificazione INT8, INT4 può ridurre ulteriormente i requisiti di archiviazione e la complessità computazionale del modello. Va notato che la quantificazione INT4 è relativamente rara nelle applicazioni pratiche, poiché una precisione troppo bassa potrebbe causare un degrado significativo delle prestazioni del modello. Inoltre, non tutto l'hardware supporta operazioni INT4, quindi è necessario considerare la compatibilità hardware quando si sceglie un metodo di quantificazione.

### **INT8**

La quantificazione INT8 è il processo di conversione dei pesi e delle attivazioni di un modello da numeri a virgola mobile a interi a 8 bit. Sebbene l'intervallo numerico rappresentato dagli interi INT8 sia più piccolo e meno preciso, questa quantificazione può ridurre significativamente i requisiti di archiviazione e calcolo. Nella quantificazione INT8, i pesi e i valori di attivazione del modello attraversano un processo di quantificazione, che include scalatura e offset, per preservare il più possibile le informazioni originali a virgola mobile. Durante l'inferenza, questi valori quantizzati vengono dequantizzati nuovamente in numeri a virgola mobile per i calcoli, per poi essere riconvertiti in INT8 per il passaggio successivo. Questo metodo può fornire una precisione sufficiente nella maggior parte delle applicazioni mantenendo un'elevata efficienza computazionale.

### **FP16**

Il formato FP16, ovvero numeri a virgola mobile a 16 bit (float16), riduce l'utilizzo della memoria della metà rispetto ai numeri a virgola mobile a 32 bit (float32), offrendo vantaggi significativi nelle applicazioni di deep learning su larga scala. Il formato FP16 consente di caricare modelli più grandi o di elaborare più dati entro i limiti di memoria della GPU. Con il continuo supporto delle moderne GPU per le operazioni FP16, l'utilizzo del formato FP16 può anche migliorare la velocità di calcolo. Tuttavia, il formato FP16 presenta anche svantaggi intrinseci, come una precisione inferiore, che potrebbe portare a instabilità numerica o perdita di precisione in alcuni casi.

### **FP32**

Il formato FP32 offre una precisione maggiore e può rappresentare accuratamente un'ampia gamma di valori. In scenari in cui vengono eseguite operazioni matematiche complesse o sono richiesti risultati ad alta precisione, il formato FP32 è preferito. Tuttavia, l'elevata precisione comporta anche un maggiore utilizzo della memoria e tempi di calcolo più lunghi. Per i modelli di deep learning su larga scala, specialmente quando ci sono molti parametri e una grande quantità di dati, il formato FP32 potrebbe causare insufficienza di memoria GPU o una riduzione della velocità di inferenza.

Su dispositivi mobili o dispositivi IoT, possiamo convertire i modelli Phi-3.x in INT4, mentre gli AI PC / Copilot PC possono utilizzare precisioni più elevate come INT8, FP16, FP32.

Attualmente, diversi produttori di hardware offrono framework differenti per supportare i modelli generativi, come OpenVINO di Intel, QNN di Qualcomm, MLX di Apple e CUDA di Nvidia. Combinando questi framework con la quantificazione del modello, è possibile completare la distribuzione locale.

Dal punto di vista tecnologico, dopo la quantificazione, abbiamo supporto per diversi formati, come PyTorch / Tensorflow, GGUF e ONNX. Ho effettuato un confronto tra i formati GGUF e ONNX e i relativi scenari applicativi. Qui consiglio il formato di quantificazione ONNX, che gode di un buon supporto dal framework del modello all'hardware. In questo capitolo ci concentreremo su ONNX Runtime per GenAI, OpenVINO e Apple MLX per eseguire la quantificazione del modello (se hai un metodo migliore, puoi inviarcelo tramite PR).

**Questo capitolo include**

1. [Quantificazione di Phi-3.5 / 4 utilizzando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantificazione di Phi-3.5 / 4 utilizzando le estensioni Generative AI per onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantificazione di Phi-3.5 / 4 utilizzando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantificazione di Phi-3.5 / 4 utilizzando il framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.