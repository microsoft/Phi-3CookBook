# Phi-3.5-Instruct WebGPU RAG Chatbot

## Ukážka demonštrácie WebGPU a RAG vzoru

RAG vzor s modelom Phi-3.5 Onnx Hosted využíva prístup Retrieval-Augmented Generation, ktorý kombinuje silu modelov Phi-3.5 s ONNX hostingom pre efektívne nasadenie AI. Tento vzor je kľúčový pre doladenie modelov na úlohy špecifické pre dané odvetvie, pričom ponúka kombináciu kvality, nákladovej efektívnosti a porozumenia dlhého kontextu. Je súčasťou balíka Azure AI, ktorý poskytuje široký výber modelov, ktoré sú ľahko dostupné, testovateľné a použiteľné, čím spĺňajú požiadavky na prispôsobenie pre rôzne odvetvia.

## Čo je WebGPU 
WebGPU je moderné webové grafické API navrhnuté na efektívny prístup k grafickému procesoru (GPU) zariadenia priamo z webových prehliadačov. Je určené ako nástupca WebGL a prináša niekoľko kľúčových vylepšení:

1. **Kompatibilita s modernými GPU**: WebGPU je navrhnuté na bezproblémovú spoluprácu s modernými architektúrami GPU, pričom využíva systémové API ako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje všeobecné výpočty na GPU a rýchlejšie operácie, čo ho robí vhodným pre renderovanie grafiky aj úlohy strojového učenia.
3. **Pokročilé funkcie**: WebGPU umožňuje prístup k pokročilejším schopnostiam GPU, čím umožňuje zložitejšie a dynamickejšie grafické a výpočtové úlohy.
4. **Znížené zaťaženie JavaScriptu**: Presunutím väčšieho množstva úloh na GPU WebGPU výrazne znižuje zaťaženie JavaScriptu, čo vedie k lepšiemu výkonu a plynulejším zážitkom.

WebGPU je aktuálne podporované v prehliadačoch ako Google Chrome, pričom sa pracuje na rozšírení podpory na ďalšie platformy.

### 03.WebGPU
Požadované prostredie:

**Podporované prehliadače:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Aktivácia WebGPU:

- V Chrome/Microsoft Edge 

Povoľte `chrome://flags/#enable-unsafe-webgpu` flag.

#### Otvorte svoj prehliadač:
Spustite Google Chrome alebo Microsoft Edge.

#### Prístup na stránku s nastaveniami:
Do adresného riadku zadajte `chrome://flags` a stlačte Enter.

#### Vyhľadajte nastavenie:
Do vyhľadávacieho poľa v hornej časti stránky zadajte 'enable-unsafe-webgpu'.

#### Povoľte nastavenie:
Nájdite vo výsledkoch #enable-unsafe-webgpu.

Kliknite na rozbaľovacie menu vedľa neho a vyberte Enabled.

#### Reštartujte prehliadač:

Po povolení nastavenia je potrebné reštartovať prehliadač, aby sa zmeny prejavili. Kliknite na tlačidlo Relaunch, ktoré sa zobrazí v dolnej časti stránky.

- Pre Linux spustite prehliadač s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU predvolene povolené.
- Vo Firefox Nightly zadajte do adresného riadku about:config a `set dom.webgpu.enabled to true`.

### Nastavenie GPU pre Microsoft Edge 

Tu sú kroky na nastavenie vysokovýkonného GPU pre Microsoft Edge na Windows:

- **Otvorte Nastavenia:** Kliknite na ponuku Štart a vyberte Nastavenia.
- **Systémové nastavenia:** Prejdite na Systém a potom na Displej.
- **Grafické nastavenia:** Posuňte sa nadol a kliknite na Grafické nastavenia.
- **Vyberte aplikáciu:** V sekcii „Vyberte aplikáciu na nastavenie preferencií“ vyberte Desktopová aplikácia a potom Prehľadávať.
- **Vyberte Edge:** Prejdite do priečinka s inštaláciou Edge (zvyčajne `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavte preferenciu:** Kliknite na Možnosti, vyberte Vysoký výkon a potom kliknite na Uložiť.
Týmto zabezpečíte, že Microsoft Edge bude používať váš vysokovýkonný GPU na lepší výkon. 
- **Reštartujte** svoj počítač, aby sa tieto nastavenia prejavili.

### Ukážky: Prosím [kliknite na tento odkaz](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.