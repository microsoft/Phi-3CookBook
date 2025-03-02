# Phi-3.5-Instruct WebGPU RAG Chatbot

## Ukázka předvádějící WebGPU a RAG Pattern

RAG Pattern s hostovaným modelem Phi-3.5 Onnx využívá přístup Retrieval-Augmented Generation, který kombinuje sílu modelů Phi-3.5 s hostováním přes ONNX pro efektivní nasazení AI. Tento vzor je klíčový pro doladění modelů pro úlohy specifické pro danou doménu a nabízí kombinaci kvality, nákladové efektivity a schopnosti práce s dlouhým kontextem. Je součástí Azure AI, které poskytuje široký výběr modelů snadno dostupných pro vyhledávání, vyzkoušení a použití, přizpůsobených potřebám různých odvětví.

## Co je WebGPU
WebGPU je moderní webové grafické API navržené pro efektivní přístup k grafické procesorové jednotce (GPU) zařízení přímo z webových prohlížečů. Má být nástupcem WebGL a nabízí několik klíčových vylepšení:

1. **Kompatibilita s moderními GPU**: WebGPU je navrženo tak, aby bezproblémově fungovalo s moderními architekturami GPU a využívalo systémová API jako Vulkan, Metal a Direct3D 12.
2. **Zvýšený výkon**: Podporuje obecné výpočty na GPU a rychlejší operace, což jej činí vhodným jak pro vykreslování grafiky, tak pro úlohy strojového učení.
3. **Pokročilé funkce**: WebGPU poskytuje přístup k pokročilejším schopnostem GPU, což umožňuje složitější a dynamičtější grafické a výpočetní pracovní zátěže.
4. **Snížení zátěže JavaScriptu**: Díky přenesení více úkolů na GPU WebGPU výrazně snižuje zátěž JavaScriptu, což vede k lepšímu výkonu a plynulejšímu zážitku.

WebGPU je aktuálně podporováno v prohlížečích jako Google Chrome, přičemž probíhá práce na rozšíření podpory na další platformy.

### 03.WebGPU
Požadované prostředí:

**Podporované prohlížeče:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Povolení WebGPU:

- V Chrome/Microsoft Edge 

Povolte příznak `chrome://flags/#enable-unsafe-webgpu`.

#### Otevřete svůj prohlížeč:
Spusťte Google Chrome nebo Microsoft Edge.

#### Přístup na stránku příznaků:
Do adresního řádku zadejte `chrome://flags` a stiskněte Enter.

#### Vyhledejte příznak:
Do vyhledávacího pole v horní části stránky napište 'enable-unsafe-webgpu'.

#### Povolte příznak:
Najděte příznak #enable-unsafe-webgpu ve výsledcích.

Klikněte na rozbalovací nabídku vedle něj a vyberte Enabled.

#### Restartujte prohlížeč:

Po povolení příznaku budete muset restartovat prohlížeč, aby se změny projevily. Klikněte na tlačítko Relaunch, které se objeví ve spodní části stránky.

- Pro Linux spusťte prohlížeč s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU povoleno ve výchozím nastavení.
- Ve Firefox Nightly zadejte do adresního řádku about:config a `set dom.webgpu.enabled to true`.

### Nastavení GPU pro Microsoft Edge 

Zde jsou kroky k nastavení výkonného GPU pro Microsoft Edge na Windows:

- **Otevřete Nastavení:** Klikněte na Start a vyberte Nastavení.
- **Nastavení systému:** Přejděte na Systém a poté na Displej.
- **Nastavení grafiky:** Posuňte se dolů a klikněte na Nastavení grafiky.
- **Výběr aplikace:** V části „Vyberte aplikaci pro nastavení předvoleb“ vyberte Desktopová aplikace a poté Procházet.
- **Vyberte Edge:** Najděte instalační složku Edge (obvykle `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavení předvoleb:** Klikněte na Možnosti, vyberte Vysoký výkon a poté klikněte na Uložit.
To zajistí, že Microsoft Edge bude používat váš výkonný GPU pro lepší výkon.
- **Restartujte** počítač, aby se tato nastavení projevila.

### Ukázky: Prosím [klikněte na tento odkaz](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Prohlášení:**  
Tento dokument byl přeložen pomocí strojových překladatelských služeb založených na umělé inteligenci. I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Nejsme zodpovědní za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.