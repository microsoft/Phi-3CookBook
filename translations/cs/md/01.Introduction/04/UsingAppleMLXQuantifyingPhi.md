# **Kvantizace Phi-3.5 pomocí Apple MLX Frameworku**

MLX je framework zaměřený na práci s poli pro výzkum strojového učení na zařízeních s čipy Apple Silicon, který přináší tým Apple Machine Learning Research.

MLX byl navržen strojovými učenci pro strojové učence. Framework je koncipován tak, aby byl uživatelsky přívětivý, ale zároveň efektivní pro trénování a nasazování modelů. Samotná konstrukce frameworku je také koncepčně jednoduchá. Naším cílem je umožnit výzkumníkům snadno rozšiřovat a zlepšovat MLX, aby mohli rychle zkoumat nové nápady.

LLM modely mohou být na zařízeních s čipy Apple Silicon akcelerovány prostřednictvím MLX, což umožňuje jejich pohodlný lokální běh.

Apple MLX Framework nyní podporuje konverzi kvantizace pro Phi-3.5-Instruct (**podpora Apple MLX Frameworku**), Phi-3.5-Vision (**podpora MLX-VLM Frameworku**) a Phi-3.5-MoE (**podpora Apple MLX Frameworku**). Pojďme to vyzkoušet:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Ukázky pro Phi-3.5 s Apple MLX**

| Laboratoře | Popis | Odkaz |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte se, jak používat Phi-3.5 Instruct s Apple MLX Frameworkem   |  [Odkaz](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Naučte se, jak používat Phi-3.5 Vision pro analýzu obrázků s Apple MLX Frameworkem     |  [Odkaz](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Naučte se, jak používat Phi-3.5 MoE s Apple MLX Frameworkem  |  [Odkaz](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zdroje**

1. Více o Apple MLX Frameworku [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. GitHub repozitář Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. GitHub repozitář MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.