# **Kvantifikace rodiny Phi**

Kvantifikace modelu znamená proces mapování parametrů (například váhy a aktivační hodnoty) v modelu neuronové sítě z velkého rozsahu hodnot (obvykle spojitého rozsahu) na menší konečný rozsah hodnot. Tato technologie může zmenšit velikost modelu, snížit jeho výpočetní složitost a zlepšit provozní efektivitu modelu v prostředích s omezenými zdroji, jako jsou mobilní zařízení nebo vestavěné systémy. Kvantifikace modelu dosahuje komprese snížením přesnosti parametrů, ale zároveň zavádí určitou ztrátu přesnosti. Proto je při procesu kvantifikace nutné vyvážit velikost modelu, výpočetní složitost a přesnost. Mezi běžné metody kvantifikace patří pevná číselná kvantifikace, kvantifikace s pohyblivou řádovou čárkou atd. Je možné zvolit vhodnou strategii kvantifikace podle konkrétního scénáře a potřeb.

Naším cílem je nasadit model GenAI na edge zařízení a umožnit většímu množství zařízení vstoupit do scénářů GenAI, jako jsou mobilní zařízení, AI PC/Copilot+PC a tradiční IoT zařízení. Prostřednictvím kvantifikovaného modelu jej můžeme nasadit na různá edge zařízení podle jejich specifikací. V kombinaci s rámcem pro akceleraci modelu a kvantifikovaným modelem poskytovaným výrobci hardwaru můžeme vytvořit lepší aplikační scénáře pro SLM.

V rámci kvantifikačních scénářů máme různé úrovně přesnosti (INT4, INT8, FP16, FP32). Níže je uvedeno vysvětlení běžně používaných úrovní kvantifikace:

### **INT4**

Kvantifikace INT4 je radikální metoda, která kvantifikuje váhy a aktivační hodnoty modelu na 4bitová celá čísla. Kvantifikace INT4 obvykle způsobuje větší ztrátu přesnosti kvůli menšímu rozsahu reprezentace a nižší přesnosti. Nicméně ve srovnání s kvantifikací INT8 může INT4 dále snížit požadavky na úložiště a výpočetní složitost modelu. Je však třeba poznamenat, že kvantifikace INT4 je v praktických aplikacích poměrně vzácná, protože příliš nízká přesnost může způsobit významné zhoršení výkonu modelu. Kromě toho ne všechna hardwarová zařízení podporují operace INT4, takže při výběru metody kvantifikace je třeba zohlednit kompatibilitu hardwaru.

### **INT8**

Kvantifikace INT8 je proces převodu vah a aktivací modelu z čísel s pohyblivou řádovou čárkou na 8bitová celá čísla. Ačkoli číselný rozsah reprezentovaný celými čísly INT8 je menší a méně přesný, může významně snížit požadavky na úložiště a výpočty. Při kvantifikaci INT8 procházejí váhy a aktivační hodnoty modelu kvantifikačním procesem, který zahrnuje škálování a posun, aby se co nejvíce zachovala původní informace s pohyblivou řádovou čárkou. Během inferencí budou tyto kvantifikované hodnoty dekvantifikovány zpět na čísla s pohyblivou řádovou čárkou pro výpočty a poté opět kvantifikovány zpět na INT8 pro další krok. Tato metoda může poskytnout dostatečnou přesnost ve většině aplikací a zároveň zachovat vysokou výpočetní efektivitu.

### **FP16**

Formát FP16, tedy 16bitová čísla s pohyblivou řádovou čárkou (float16), snižuje paměťové nároky na polovinu oproti 32bitovým číslům s pohyblivou řádovou čárkou (float32), což má významné výhody při aplikacích hlubokého učení ve velkém měřítku. Formát FP16 umožňuje načítání větších modelů nebo zpracování většího množství dat v rámci stejných paměťových omezení GPU. Jak moderní GPU hardware stále více podporuje operace FP16, použití formátu FP16 může rovněž přinést zlepšení výpočetní rychlosti. Formát FP16 má však i své inherentní nevýhody, jako je nižší přesnost, což může v některých případech vést k numerické nestabilitě nebo ztrátě přesnosti.

### **FP32**

Formát FP32 poskytuje vyšší přesnost a dokáže přesně reprezentovat široký rozsah hodnot. V situacích, kdy se provádějí složité matematické operace nebo jsou požadovány vysoce přesné výsledky, je preferován formát FP32. Vyšší přesnost však také znamená větší spotřebu paměti a delší dobu výpočtů. U modelů hlubokého učení ve velkém měřítku, zejména pokud obsahují mnoho parametrů a velké množství dat, může formát FP32 způsobit nedostatek paměti GPU nebo snížení rychlosti inferencí.

Na mobilních zařízeních nebo IoT zařízeních můžeme převést modely Phi-3.x na INT4, zatímco AI PC / Copilot PC mohou používat vyšší přesnosti, jako jsou INT8, FP16 nebo FP32.

V současné době mají různí výrobci hardwaru různé rámce na podporu generativních modelů, například OpenVINO od Intelu, QNN od Qualcommu, MLX od Applu a CUDA od Nvidie. V kombinaci s kvantifikací modelu je možné provést lokální nasazení.

Z hlediska technologie máme po kvantifikaci podporu různých formátů, jako jsou PyTorch / Tensorflow formát, GGUF a ONNX. Provedl jsem porovnání formátů GGUF a ONNX a jejich aplikačních scénářů. Zde doporučuji kvantifikační formát ONNX, který má dobrou podporu od rámců modelů až po hardware. V této kapitole se zaměříme na ONNX Runtime pro GenAI, OpenVINO a Apple MLX pro provádění kvantifikace modelů (pokud máte lepší způsob, můžete nám ho poskytnout prostřednictvím PR).

**Tato kapitola obsahuje**

1. [Kvantifikace Phi-3.5 / 4 pomocí llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifikace Phi-3.5 / 4 pomocí rozšíření Generative AI pro onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifikace Phi-3.5 / 4 pomocí Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifikace Phi-3.5 / 4 pomocí Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. I když se snažíme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Neodpovídáme za jakékoli nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.