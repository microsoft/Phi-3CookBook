# **Kvantizacija družine Phi**

Kvantizacija modela se nanaša na postopek preslikave parametrov (kot so uteži in aktivacijske vrednosti) v nevronskem mrežnem modelu iz velikega obsega vrednosti (običajno neprekinjenega obsega vrednosti) v manjši, končen obseg vrednosti. Ta tehnologija lahko zmanjša velikost in računsko kompleksnost modela ter izboljša delovno učinkovitost modela v okoljih z omejenimi viri, kot so mobilne naprave ali vgrajeni sistemi. Kvantizacija modela doseže kompresijo z zmanjšanjem natančnosti parametrov, vendar hkrati uvaja določeno izgubo natančnosti. Zato je v procesu kvantizacije potrebno uravnotežiti velikost modela, računsko kompleksnost in natančnost. Pogoste metode kvantizacije vključujejo kvantizacijo s fiksno točko, kvantizacijo s plavajočo točko itd. Pravilno kvantizacijsko strategijo lahko izberete glede na specifičen scenarij in potrebe.

Naš cilj je, da GenAI model implementiramo na robne naprave in omogočimo več napravam dostop do GenAI scenarijev, kot so mobilne naprave, AI PC/Copilot+PC in tradicionalne IoT naprave. S kvantiziranim modelom ga lahko implementiramo na različne robne naprave glede na posamezno napravo. V kombinaciji z okvirji za pospeševanje modelov in kvantiziranimi modeli, ki jih zagotavljajo proizvajalci strojne opreme, lahko zgradimo boljše aplikacijske scenarije za SLM.

V scenariju kvantizacije imamo različne natančnosti (INT4, INT8, FP16, FP32). Spodaj je razlaga pogosto uporabljenih natančnosti kvantizacije.

### **INT4**

INT4 kvantizacija je radikalna metoda kvantizacije, ki kvantizira uteži in aktivacijske vrednosti modela v 4-bitna cela števila. INT4 kvantizacija običajno povzroči večjo izgubo natančnosti zaradi manjšega obsega reprezentacije in nižje natančnosti. Vendar pa lahko v primerjavi z INT8 kvantizacijo INT4 kvantizacija še dodatno zmanjša zahteve po shranjevanju in računsko kompleksnost modela. Upoštevati je treba, da je INT4 kvantizacija v praksi razmeroma redka, saj lahko prenizka natančnost povzroči občutno poslabšanje zmogljivosti modela. Poleg tega ne vsa strojna oprema podpira operacije INT4, zato je treba pri izbiri metode kvantizacije upoštevati združljivost s strojno opremo.

### **INT8**

INT8 kvantizacija je postopek pretvorbe uteži in aktivacij modela iz števil s plavajočo vejico v 8-bitna cela števila. Čeprav je obseg vrednosti, ki jih predstavljajo INT8 cela števila, manjši in manj natančen, lahko ta metoda bistveno zmanjša zahteve po shranjevanju in računanju. Pri INT8 kvantizaciji uteži in aktivacijske vrednosti modela preidejo skozi proces kvantizacije, ki vključuje skaliranje in odmike, da se čim bolj ohrani izvirna informacija števil s plavajočo vejico. Med inferenco se te kvantizirane vrednosti dekvantizirajo nazaj v števila s plavajočo vejico za izračun in nato ponovno kvantizirajo nazaj v INT8 za naslednji korak. Ta metoda lahko v večini aplikacij zagotovi zadostno natančnost ob ohranjanju visoke računske učinkovitosti.

### **FP16**

Format FP16, torej 16-bitna števila s plavajočo vejico (float16), prepolovi pomnilniške zahteve v primerjavi z 32-bitnimi števili s plavajočo vejico (float32), kar prinaša pomembne prednosti v aplikacijah za obsežno globoko učenje. Format FP16 omogoča nalaganje večjih modelov ali obdelavo več podatkov v okviru enakih omejitev GPU pomnilnika. Ker sodobna GPU strojna oprema vse bolj podpira operacije FP16, lahko uporaba formata FP16 prinese tudi izboljšave hitrosti računanja. Vendar ima format FP16 tudi svoje inherentne slabosti, in sicer nižjo natančnost, kar lahko v nekaterih primerih povzroči numerično nestabilnost ali izgubo natančnosti.

### **FP32**

Format FP32 zagotavlja višjo natančnost in lahko natančno predstavlja širok obseg vrednosti. V scenarijih, kjer se izvajajo kompleksne matematične operacije ali so potrebni rezultati z visoko natančnostjo, je format FP32 prednostna izbira. Vendar pa visoka natančnost pomeni tudi večjo porabo pomnilnika in daljši čas računanja. Pri obsežnih modelih globokega učenja, še posebej, ko je veliko parametrov modela in ogromna količina podatkov, lahko format FP32 povzroči pomanjkanje GPU pomnilnika ali zmanjšanje hitrosti inferenc.

Na mobilnih napravah ali IoT napravah lahko modele Phi-3.x pretvorimo v INT4, medtem ko lahko AI PC / Copilot PC uporabljajo višje natančnosti, kot so INT8, FP16, FP32.

Trenutno imajo različni proizvajalci strojne opreme različne okvirje za podporo generativnim modelom, kot so Intelov OpenVINO, Qualcommov QNN, Applov MLX in Nvidiin CUDA itd., ki jih je mogoče kombinirati z modelno kvantizacijo za lokalno implementacijo.

Z vidika tehnologije imamo po kvantizaciji podporo za različne formate, kot so PyTorch / Tensorflow format, GGUF in ONNX. Opravil sem primerjavo formatov in aplikacijskih scenarijev med GGUF in ONNX. Tukaj priporočam ONNX kvantizacijski format, ki ima dobro podporo od modelnih okvirjev do strojne opreme. V tem poglavju se bomo osredotočili na ONNX Runtime za GenAI, OpenVINO in Apple MLX za izvajanje kvantizacije modelov (če imate boljši način, nam ga lahko pošljete s predložitvijo PR).

**To poglavje vključuje**

1. [Kvantizacija Phi-3.5 / 4 z uporabo llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantizacija Phi-3.5 / 4 z uporabo razširitev Generative AI za onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantizacija Phi-3.5 / 4 z uporabo Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantizacija Phi-3.5 / 4 z uporabo Applovega MLX okvirja](./UsingAppleMLXQuantifyingPhi.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.