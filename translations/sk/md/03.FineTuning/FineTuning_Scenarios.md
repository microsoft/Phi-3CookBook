## Scenáre jemného doladenia

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.sk.png)

**Platforma** Zahrňuje rôzne technológie ako Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito a ONNX Runtime. 

**Infraštruktúra** Obsahuje CPU a FPGA, ktoré sú kľúčové pre proces jemného doladenia. Ukážem vám ikony pre každú z týchto technológií.

**Nástroje a rámce** Zahŕňajú ONNX Runtime a ONNX Runtime. Ukážem vám ikony pre každú z týchto technológií.
[Pridať ikony pre ONNX Runtime a ONNX Runtime]

Proces jemného doladenia s technológiami Microsoft zahŕňa rôzne komponenty a nástroje. Porozumením a využívaním týchto technológií môžeme efektívne jemne doladiť naše aplikácie a vytvárať lepšie riešenia. 

## Model ako služba

Jemne doladíte model pomocou hostovaného jemného doladenia bez potreby vytvárať a spravovať výpočtové zdroje.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.sk.png)

Serverless jemné doladenie je dostupné pre modely Phi-3-mini a Phi-3-medium, čo vývojárom umožňuje rýchlo a jednoducho prispôsobiť modely pre cloudové a edge scenáre bez potreby zabezpečenia výpočtových zdrojov. Oznámili sme tiež, že model Phi-3-small je teraz dostupný prostredníctvom našej ponuky Models-as-a-Service, čo vývojárom umožňuje rýchly a jednoduchý začiatok s vývojom AI bez nutnosti spravovať podkladovú infraštruktúru.

## Model ako platforma

Používatelia si spravujú vlastné výpočtové zdroje na jemné doladenie svojich modelov.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.sk.png)

[Príklad jemného doladenia](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Scenáre jemného doladenia 

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenár|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Prispôsobenie predtrénovaných LLM pre špecifické úlohy alebo domény|Áno|Áno|Áno|Áno|Áno|Áno|
|Jemné doladenie pre NLP úlohy, ako je klasifikácia textu, rozpoznávanie pomenovaných entít a strojový preklad|Áno|Áno|Áno|Áno|Áno|Áno|
|Jemné doladenie pre úlohy otázok a odpovedí|Áno|Áno|Áno|Áno|Áno|Áno|
|Jemné doladenie na generovanie odpovedí podobných ľuďom v chatbotov|Áno|Áno|Áno|Áno|Áno|Áno|
|Jemné doladenie na generovanie hudby, umenia alebo iných foriem kreativity|Áno|Áno|Áno|Áno|Áno|Áno|
|Znižovanie výpočtových a finančných nákladov|Áno|Áno|Nie|Áno|Áno|Nie|
|Znižovanie pamäťovej náročnosti|Nie|Áno|Nie|Áno|Áno|Áno|
|Použitie menšieho počtu parametrov na efektívne jemné doladenie|Nie|Áno|Áno|Nie|Nie|Áno|
|Pamäťovo efektívna forma dátovej paralelizácie, ktorá umožňuje prístup k agregovanej GPU pamäti všetkých dostupných GPU zariadení|Nie|Nie|Nie|Áno|Áno|Áno|

## Príklady výkonu jemného doladenia

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.sk.png)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladových služieb AI. Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.