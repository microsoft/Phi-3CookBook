Phi-3-mini WebGPU RAG Chatbot

## Demo ukazující WebGPU a RAG vzor
RAG vzor s modelem Phi-3 Onnx Hosted využívá přístup Retrieval-Augmented Generation, který kombinuje sílu modelů Phi-3 s hostingem ONNX pro efektivní nasazení AI. Tento vzor je klíčový pro doladění modelů pro úlohy specifické pro dané obory a nabízí kombinaci kvality, nákladové efektivity a schopnosti pracovat s dlouhými kontexty. Je součástí Azure AI, která poskytuje široký výběr modelů snadno dostupných, vyzkoušených a použitelných, přizpůsobených potřebám různých odvětví. Modely Phi-3, včetně Phi-3-mini, Phi-3-small a Phi-3-medium, jsou k dispozici v katalogu modelů Azure AI a lze je doladit a nasadit samostatně nebo prostřednictvím platforem jako HuggingFace a ONNX, což ukazuje závazek Microsoftu k dostupným a efektivním AI řešením.

## Co je WebGPU 
WebGPU je moderní webové grafické API navržené tak, aby poskytovalo efektivní přístup k grafickému procesoru (GPU) zařízení přímo z webových prohlížečů. Je zamýšleno jako nástupce WebGL a nabízí několik klíčových vylepšení:

1. **Kompatibilita s moderními GPU**: WebGPU je vytvořeno tak, aby bezproblémově fungovalo se současnými architekturami GPU, využívajíc systémová API jako Vulkan, Metal a Direct3D 12.
2. **Vylepšený výkon**: Podporuje výpočty na GPU pro obecné účely a rychlejší operace, což jej činí vhodným jak pro vykreslování grafiky, tak pro úlohy strojového učení.
3. **Pokročilé funkce**: WebGPU poskytuje přístup k pokročilejším schopnostem GPU, umožňující složitější a dynamické grafické a výpočetní úlohy.
4. **Snížené zatížení JavaScriptu**: Přesunem více úloh na GPU WebGPU výrazně snižuje zatížení JavaScriptu, což vede k lepšímu výkonu a plynulejšímu zážitku.

WebGPU je aktuálně podporováno v prohlížečích jako Google Chrome a probíhá práce na rozšíření podpory na další platformy.

### 03.WebGPU
Požadované prostředí:

**Podporované prohlížeče:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Povolení WebGPU:

- V Chrome/Microsoft Edge 

Povolte `chrome://flags/#enable-unsafe-webgpu` příznak.

#### Otevřete svůj prohlížeč:
Spusťte Google Chrome nebo Microsoft Edge.

#### Přístup na stránku příznaků:
Do adresního řádku zadejte `chrome://flags` a stiskněte Enter.

#### Vyhledejte příznak:
Do vyhledávacího pole nahoře zadejte 'enable-unsafe-webgpu'.

#### Povolte příznak:
Najděte příznak #enable-unsafe-webgpu ve výsledcích.

Klikněte na rozbalovací nabídku vedle něj a vyberte Enabled.

#### Restartujte prohlížeč:

Po povolení příznaku budete muset restartovat prohlížeč, aby se změny projevily. Klikněte na tlačítko Relaunch, které se objeví dole na stránce.

- Pro Linux spusťte prohlížeč s `--enable-features=Vulkan`.
- Safari 18 (macOS 15) má WebGPU povolený ve výchozím nastavení.
- Ve Firefox Nightly zadejte do adresního řádku about:config a `set dom.webgpu.enabled to true`.

### Nastavení GPU pro Microsoft Edge 

Zde jsou kroky k nastavení výkonného GPU pro Microsoft Edge ve Windows:

- **Otevřete Nastavení:** Klikněte na nabídku Start a vyberte Nastavení.
- **Systémová nastavení:** Přejděte na Systém a poté na Displej.
- **Grafická nastavení:** Sjeďte dolů a klikněte na Grafická nastavení.
- **Vyberte aplikaci:** V části „Vyberte aplikaci pro nastavení předvolby“ zvolte Desktopová aplikace a poté Procházet.
- **Vyberte Edge:** Najděte instalační složku Edge (obvykle `C:\Program Files (x86)\Microsoft\Edge\Application`) a vyberte `msedge.exe`.
- **Nastavte předvolbu:** Klikněte na Možnosti, zvolte Vysoký výkon a poté klikněte na Uložit.
Tím zajistíte, že Microsoft Edge využije váš výkonný GPU pro lepší výkon. 
- **Restartujte** zařízení, aby se nastavení projevilo.

### Otevřete svůj Codespace:
Přejděte do svého úložiště na GitHubu.
Klikněte na tlačítko Kód a vyberte Otevřít pomocí Codespaces.

Pokud ještě nemáte Codespace, můžete jej vytvořit kliknutím na Nový Codespace.

**Poznámka** Instalace Node prostředí ve vašem Codespace
Spuštění npm dema z GitHub Codespace je skvělý způsob, jak testovat a vyvíjet váš projekt. Zde je průvodce krok za krokem, jak začít:

### Nastavení prostředí:
Jakmile je váš Codespace otevřen, ujistěte se, že máte nainstalované Node.js a npm. Můžete to zkontrolovat spuštěním:
```
node -v
```
```
npm -v
```

Pokud nejsou nainstalovány, můžete je nainstalovat pomocí:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Přechod do adresáře projektu:
Použijte terminál k přechodu do adresáře, kde se nachází váš npm projekt:
```
cd path/to/your/project
```

### Instalace závislostí:
Spusťte následující příkaz pro instalaci všech nezbytných závislostí uvedených v souboru package.json:

```
npm install
```

### Spuštění dema:
Jakmile jsou závislosti nainstalovány, můžete spustit svůj demo skript. Ten je obvykle uveden v sekci scripts v souboru package.json. Například pokud je váš demo skript pojmenován start, můžete spustit:

```
npm run build
```
```
npm run dev
```

### Přístup k demu:
Pokud vaše demo zahrnuje webový server, Codespaces poskytne URL pro přístup k němu. Podívejte se na oznámení nebo zkontrolujte kartu Porty, kde najdete URL.

**Poznámka:** Model musí být uložen v mezipaměti prohlížeče, takže načítání může chvíli trvat.

### RAG Demo
Nahrajte markdown soubor `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Vyberte svůj soubor:
Klikněte na tlačítko „Vybrat soubor“ a zvolte dokument, který chcete nahrát.

### Nahrajte dokument:
Po výběru souboru klikněte na tlačítko „Nahrát“ pro načtení dokumentu pro RAG (Retrieval-Augmented Generation).

### Spusťte chat:
Jakmile je dokument nahrán, můžete zahájit chatovací relaci pomocí RAG na základě obsahu vašeho dokumentu.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladových služeb založených na umělé inteligenci. Přestože se snažíme o co největší přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální překlad provedený člověkem. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.