# **Kvantifikácia rodiny Phi**

Kvantizácia modelu znamená proces mapovania parametrov (ako sú váhy a hodnoty aktivácie) v modeli neurónovej siete z veľkého rozsahu hodnôt (zvyčajne spojitého rozsahu hodnôt) na menší, konečný rozsah hodnôt. Táto technológia dokáže zmenšiť veľkosť modelu, znížiť jeho výpočtovú zložitosť a zlepšiť jeho prevádzkovú efektivitu v prostrediach s obmedzenými zdrojmi, ako sú mobilné zariadenia alebo vstavané systémy. Kvantizácia modelu dosahuje kompresiu znížením presnosti parametrov, ale zároveň zavádza určitú stratu presnosti. Preto je počas procesu kvantizácie potrebné nájsť rovnováhu medzi veľkosťou modelu, výpočtovou zložitosťou a presnosťou. Bežné metódy kvantizácie zahŕňajú kvantizáciu s pevnou rádovou čiarkou, kvantizáciu s pohyblivou rádovou čiarkou a podobne. Môžete si zvoliť vhodnú kvantizačnú stratégiu podľa konkrétneho scenára a potrieb.

Naším cieľom je nasadiť GenAI model na edge zariadenia a umožniť viac zariadeniam vstúpiť do GenAI scenárov, ako sú mobilné zariadenia, AI PC/Copilot+PC a tradičné IoT zariadenia. Prostredníctvom kvantizácie modelu ho môžeme nasadiť na rôzne edge zariadenia na základe ich špecifík. V kombinácii s akceleračnými rámcami modelu a kvantizačnými modelmi poskytovanými výrobcami hardvéru môžeme vytvárať lepšie aplikácie SLM scenárov.

V kvantizačných scenároch máme rôzne úrovne presnosti (INT4, INT8, FP16, FP32). Nižšie je uvedené vysvetlenie bežne používaných úrovní kvantizačnej presnosti.

### **INT4**

Kvantizácia INT4 je radikálna metóda kvantizácie, ktorá kvantizuje váhy a hodnoty aktivácie modelu na 4-bitové celé čísla. Kvantizácia INT4 zvyčajne vedie k väčšej strate presnosti v dôsledku menšieho rozsahu reprezentácie a nižšej presnosti. Avšak v porovnaní s kvantizáciou INT8 dokáže INT4 ešte viac znížiť požiadavky na úložisko a výpočtovú zložitosť modelu. Treba však poznamenať, že kvantizácia INT4 je v praktických aplikáciách pomerne zriedkavá, pretože príliš nízka presnosť môže spôsobiť výrazné zhoršenie výkonu modelu. Navyše, nie všetok hardvér podporuje operácie INT4, preto je pri výbere kvantizačnej metódy potrebné zohľadniť kompatibilitu hardvéru.

### **INT8**

Kvantizácia INT8 je proces konverzie váh a aktivácií modelu z čísel s pohyblivou rádovou čiarkou na 8-bitové celé čísla. Aj keď je rozsah hodnôt reprezentovaných číslami INT8 menší a menej presný, dokáže výrazne znížiť požiadavky na úložisko a výpočty. Pri kvantizácii INT8 prechádzajú váhy a hodnoty aktivácie modelu kvantizačným procesom, ktorý zahŕňa škálovanie a posun, aby sa čo najviac zachovali pôvodné informácie s pohyblivou rádovou čiarkou. Počas inferencie sa tieto kvantizované hodnoty dekvantizujú späť na čísla s pohyblivou rádovou čiarkou na výpočet a následne sa opäť kvantizujú na INT8 pre ďalší krok. Táto metóda poskytuje dostatočnú presnosť vo väčšine aplikácií pri zachovaní vysokej výpočtovej efektivity.

### **FP16**

Formát FP16, teda 16-bitové čísla s pohyblivou rádovou čiarkou (float16), znižuje pamäťovú náročnosť na polovicu v porovnaní s 32-bitovými číslami s pohyblivou rádovou čiarkou (float32), čo prináša významné výhody v aplikáciách veľkého rozsahu hlbokého učenia. Formát FP16 umožňuje načítanie väčších modelov alebo spracovanie väčšieho množstva dát v rámci rovnakých obmedzení pamäte GPU. Keďže moderný hardvér GPU stále viac podporuje operácie FP16, použitie formátu FP16 môže tiež priniesť zlepšenie výpočtovej rýchlosti. Formát FP16 má však aj svoje inherentné nevýhody, a to nižšiu presnosť, ktorá môže v niektorých prípadoch viesť k numerickej nestabilite alebo strate presnosti.

### **FP32**

Formát FP32 poskytuje vyššiu presnosť a dokáže presne reprezentovať široký rozsah hodnôt. V scenároch, kde sa vykonávajú zložité matematické operácie alebo sú potrebné vysoko presné výsledky, sa preferuje formát FP32. Vyššia presnosť však znamená aj väčšiu pamäťovú náročnosť a dlhší čas výpočtov. Pre veľké modely hlbokého učenia, najmä keď je množstvo parametrov modelu a objem dát obrovský, môže formát FP32 spôsobiť nedostatok pamäte GPU alebo spomalenie inferencie.

Na mobilných alebo IoT zariadeniach môžeme konvertovať modely Phi-3.x na INT4, zatiaľ čo AI PC / Copilot PC môžu používať vyššiu presnosť, ako je INT8, FP16, FP32.

V súčasnosti majú rôzni výrobcovia hardvéru rôzne rámce na podporu generatívnych modelov, ako napríklad Intel OpenVINO, Qualcomm QNN, Apple MLX a Nvidia CUDA, ktoré v kombinácii s kvantizáciou modelu umožňujú lokálne nasadenie.

Z technologického hľadiska máme po kvantizácii podporu rôznych formátov, ako sú PyTorch / Tensorflow formát, GGUF a ONNX. Vykonal som porovnanie formátov a aplikačných scenárov medzi GGUF a ONNX. Tu odporúčam kvantizačný formát ONNX, ktorý má dobrú podporu od modelového rámca po hardvér. V tejto kapitole sa zameriame na ONNX Runtime pre GenAI, OpenVINO a Apple MLX na vykonanie kvantizácie modelu (ak máte lepší spôsob, môžete nám ho poskytnúť podaním PR).

**Táto kapitola obsahuje**

1. [Kvantizácia Phi-3.5 / 4 pomocou llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantizácia Phi-3.5 / 4 pomocou Generative AI rozšírení pre onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantizácia Phi-3.5 / 4 pomocou Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantizácia Phi-3.5 / 4 pomocou Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladateľských služieb založených na umelej inteligencii. Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho rodnom jazyku. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.