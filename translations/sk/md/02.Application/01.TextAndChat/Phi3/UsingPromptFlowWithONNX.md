# Použitie Windows GPU na vytvorenie Prompt flow riešenia s Phi-3.5-Instruct ONNX

Nasledujúci dokument je príkladom, ako používať PromptFlow s ONNX (Open Neural Network Exchange) na vývoj AI aplikácií založených na modeloch Phi-3.

PromptFlow je súbor vývojárskych nástrojov navrhnutých na zjednodušenie celého vývojového cyklu AI aplikácií založených na veľkých jazykových modeloch (LLM), od nápadu a prototypovania až po testovanie a vyhodnocovanie.

Integráciou PromptFlow s ONNX môžu vývojári:

- **Optimalizovať výkon modelu:** Využiť ONNX na efektívne inferencie a nasadenie modelov.
- **Zjednodušiť vývoj:** Používať PromptFlow na správu pracovného toku a automatizáciu opakujúcich sa úloh.
- **Zlepšiť spoluprácu:** Uľahčiť spoluprácu medzi členmi tímu poskytnutím jednotného vývojového prostredia.

**Prompt flow** je súbor vývojárskych nástrojov navrhnutých na zjednodušenie celého vývojového cyklu AI aplikácií založených na LLM, od nápadu, prototypovania, testovania, vyhodnocovania až po nasadenie do produkcie a monitorovanie. Uľahčuje prácu s návrhom promptov a umožňuje vytvárať LLM aplikácie v produkčnej kvalite.

Prompt flow dokáže pracovať s OpenAI, Azure OpenAI Service a prispôsobiteľnými modelmi (Huggingface, lokálne LLM/SLM). Naším cieľom je nasadiť kvantizovaný ONNX model Phi-3.5 do lokálnych aplikácií. Prompt flow nám môže pomôcť lepšie plánovať naše podnikanie a vytvárať lokálne riešenia založené na Phi-3.5. V tomto príklade spojíme ONNX Runtime GenAI Library na vytvorenie Prompt flow riešenia na Windows GPU.

## **Inštalácia**

### **ONNX Runtime GenAI pre Windows GPU**

Prečítajte si tento návod na nastavenie ONNX Runtime GenAI pre Windows GPU [kliknite sem](./ORTWindowGPUGuideline.md)

### **Nastavenie Prompt flow vo VSCode**

1. Nainštalujte rozšírenie Prompt flow pre VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.sk.png)

2. Po inštalácii rozšírenia Prompt flow kliknite na rozšírenie a vyberte **Installation dependencies**. Postupujte podľa tohto návodu na inštaláciu Prompt flow SDK vo vašom prostredí.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.sk.png)

3. Stiahnite si [Ukážkový kód](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) a otvorte ho vo VS Code.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.sk.png)

4. Otvorte **flow.dag.yaml** a vyberte svoje Python prostredie.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.sk.png)

   Otvorte **chat_phi3_ort.py** a zmeňte umiestnenie vášho Phi-3.5-instruct ONNX modelu.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.sk.png)

5. Spustite váš prompt flow na testovanie.

Otvorte **flow.dag.yaml** a kliknite na vizuálny editor.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.sk.png)

Po kliknutí naň ho spustite na testovanie.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.sk.png)

1. Môžete spustiť dávku v termináli na kontrolu ďalších výsledkov.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Výsledky si môžete pozrieť vo vašom predvolenom prehliadači.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.sk.png)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.