Phi-3-mini WebGPU RAG Chatbot

## Demo ukazujúci WebGPU a RAG vzor
RAG vzor s modelom Phi-3 Onnx Hosted využíva prístup Retrieval-Augmented Generation, ktorý kombinuje silu modelov Phi-3 s ONNX hostingom pre efektívne nasadenie AI. Tento vzor je kľúčový pri doladení modelov pre špecifické úlohy v konkrétnych oblastiach, pričom ponúka kombináciu kvality, nákladovej efektívnosti a schopnosti pracovať s dlhým kontextom. Je súčasťou Azure AI balíka, ktorý poskytuje široký výber modelov, ľahko dostupných, skúšateľných a použiteľných, vyhovujúcich potrebám prispôsobenia v rôznych odvetviach. Modely Phi-3, vrátane Phi-3-mini, Phi-3-small a Phi-3-medium, sú dostupné v Azure AI Model Catalog a môžu byť doladené a nasadené samostatne alebo cez platformy ako HuggingFace a ONNX, čím Microsoft demonštruje svoj záväzok k dostupným a efektívnym AI riešeniam.

## Čo je WebGPU 
WebGPU je moderné grafické API pre web, navrhnuté na efektívny prístup k grafickej procesorovej jednotke (GPU) zariadenia priamo z webových prehliadačov. Má byť nástupcom WebGL a ponúka niekoľko kľúčových vylepšení:

1. **Kompatibilita s modernými GPU**: WebGPU je navrhnuté na bezproblémovú prácu so súčasnými architektúrami GPU, pričom využíva systémové API ako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje všeobecné výpočty na GPU a rýchlejšie operácie, čo ho robí vhodným pre grafické vykresľovanie aj úlohy strojového učenia.
3. **Pokročilé funkcie**: WebGPU poskytuje prístup k pokročilejším schopnostiam GPU, umožňujúc zložitejšie a dynamickejšie grafické a výpočtové úlohy.
4. **Zníženie zaťaženia JavaScriptu**: Prenesením väčšiny úloh na GPU WebGPU výrazne znižuje zaťaženie JavaScriptu, čo vedie k lepšiemu výkonu a plynulejším skúsenostiam.

WebGPU je aktuálne podporované v prehliadačoch ako Google Chrome, pričom prebiehajú práce na rozšírení podpory na ďalšie platformy.

### 03.WebGPU
Požadované prostredie:

**Podporované prehliadače:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Povolenie WebGPU:

- V Chrome/Microsoft Edge 

Povoľte `chrome://flags/#enable-unsafe-webgpu` flag.

#### Otvorte svoj prehliadač:
Spustite Google Chrome alebo Microsoft Edge.

#### Prístup na stránku s flagmi:
Do adresného riadku zadajte `chrome://flags` a stlačte Enter.

#### Vyhľadajte flag:
Do vyhľadávacieho poľa v hornej časti stránky napíšte 'enable-unsafe-webgpu'.

#### Povoľte flag:
Nájdite flag #enable-unsafe-webgpu vo výsledkoch.

Kliknite na rozbaľovaciu ponuku vedľa neho a vyberte Enabled.

#### Reštartujte svoj prehliadač:

Po povolení flagu budete musieť prehliadač reštartovať, aby sa zmeny prejavili. Kliknite na tlačidlo Relaunch, ktoré sa zobrazí v dolnej časti stránky.

- Pre Linux spustite prehliadač s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU predvolene povolené.
- Vo Firefox Nightly zadajte do adresného riadku about:config a `set dom.webgpu.enabled to true`.

### Nastavenie GPU pre Microsoft Edge 

Tu sú kroky na nastavenie vysoko výkonného GPU pre Microsoft Edge vo Windows:

- **Otvorte Nastavenia:** Kliknite na ponuku Štart a vyberte Nastavenia.
- **Systémové nastavenia:** Prejdite na Systém a potom na Displej.
- **Grafické nastavenia:** Posuňte sa nadol a kliknite na Grafické nastavenia.
- **Vyberte aplikáciu:** Pod „Vybrať aplikáciu na nastavenie preferencií“ vyberte Desktop app a potom Browse.
- **Vyberte Edge:** Prejdite do inštalačného priečinka Edge (zvyčajne `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavte preferencie:** Kliknite na Možnosti, vyberte Vysoký výkon a potom kliknite na Uložiť.
Týmto zabezpečíte, že Microsoft Edge bude používať váš vysoko výkonný GPU pre lepší výkon. 
- **Reštartujte** svoje zariadenie, aby sa nastavenia prejavili.

### Otvorte svoj Codespace:
Prejdite do svojho úložiska na GitHub.
Kliknite na tlačidlo Code a vyberte Open with Codespaces.

Ak ešte nemáte Codespace, môžete ho vytvoriť kliknutím na New codespace.

**Poznámka** Inštalácia Node prostredia vo vašom Codespace
Spustenie npm dema z GitHub Codespace je skvelý spôsob, ako otestovať a vyvíjať svoj projekt. Tu je krok-za-krokom návod, ako začať:

### Nastavte svoje prostredie:
Keď je váš Codespace otvorený, uistite sa, že máte nainštalovaný Node.js a npm. Skontrolovať to môžete spustením:
```
node -v
```
```
npm -v
```

Ak nie sú nainštalované, môžete ich nainštalovať pomocou:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Prejdite do adresára svojho projektu:
Použite terminál na prechod do adresára, kde sa nachádza váš npm projekt:
```
cd path/to/your/project
```

### Nainštalujte závislosti:
Spustite nasledujúci príkaz na inštaláciu všetkých potrebných závislostí uvedených v súbore package.json:

```
npm install
```

### Spustite demo:
Keď sú závislosti nainštalované, môžete spustiť svoj demo skript. Tento skript je zvyčajne uvedený v sekcii scripts v súbore package.json. Ak je napríklad váš demo skript pomenovaný start, môžete ho spustiť:

```
npm run build
```
```
npm run dev
```

### Prístup k demu:
Ak vaše demo zahŕňa webový server, Codespaces poskytne URL na prístup k nemu. Pozrite si upozornenie alebo skontrolujte kartu Ports, kde nájdete URL.

**Poznámka:** Model musí byť načítaný do vyrovnávacej pamäte prehliadača, takže načítanie môže chvíľu trvať.

### RAG Demo
Nahrajte markdown súbor `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Vyberte svoj súbor:
Kliknite na tlačidlo „Choose File“, aby ste vybrali dokument, ktorý chcete nahrať.

### Nahrajte dokument:
Po výbere súboru kliknite na tlačidlo „Upload“, aby ste načítali svoj dokument pre RAG (Retrieval-Augmented Generation).

### Začnite chat:
Keď je dokument nahraný, môžete začať chatovaciu reláciu pomocou RAG na základe obsahu vášho dokumentu.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Aj keď sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.