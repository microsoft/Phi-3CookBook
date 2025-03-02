# **Kvantizácia Phi-3.5 pomocou Apple MLX Frameworku**

MLX je framework pre strojové učenie na platforme Apple Silicon, ktorý prináša Apple machine learning research.

MLX je navrhnutý strojovými výskumníkmi pre strojových výskumníkov. Framework je navrhnutý tak, aby bol užívateľsky priateľský, ale zároveň efektívny pri trénovaní a nasadzovaní modelov. Dizajn frameworku je zároveň koncepčne jednoduchý. Naším cieľom je uľahčiť výskumníkom rozširovanie a zlepšovanie MLX, aby mohli rýchlo skúmať nové nápady.

LLM modely môžu byť na zariadeniach s Apple Silicon akcelerované prostredníctvom MLX a modely môžu byť veľmi pohodlne spúšťané lokálne.

Apple MLX Framework teraz podporuje konverziu kvantizácie pre Phi-3.5-Instruct (**podpora Apple MLX Frameworku**), Phi-3.5-Vision (**podpora MLX-VLM Frameworku**) a Phi-3.5-MoE (**podpora Apple MLX Frameworku**). Poďme si to vyskúšať:

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

### **🤖 Ukážky pre Phi-3.5 s Apple MLX**

| Laboratóriá | Popis | Odkaz |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte sa, ako používať Phi-3.5 Instruct s Apple MLX frameworkom   |  [Odkaz](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (obraz) | Naučte sa, ako používať Phi-3.5 Vision na analýzu obrázkov pomocou Apple MLX frameworku     |  [Odkaz](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Naučte sa, ako používať Phi-3.5 MoE s Apple MLX frameworkom  |  [Odkaz](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zdroje**

1. Zistite viac o Apple MLX Frameworke [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.