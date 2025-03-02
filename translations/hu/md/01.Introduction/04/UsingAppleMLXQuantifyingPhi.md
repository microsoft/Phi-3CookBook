# **Phi-3.5 kvantálása az Apple MLX keretrendszer használatával**

Az MLX egy tömbkeretrendszer gépi tanulási kutatásokhoz Apple silicon eszközökön, amelyet az Apple gépi tanulási kutatócsapata fejlesztett ki.

Az MLX-t gépi tanulási kutatók tervezték gépi tanulási kutatók számára. A keretrendszer célja, hogy felhasználóbarát legyen, ugyanakkor hatékonyan lehessen modelleket tanítani és telepíteni. Maga a keretrendszer tervezése is koncepcionálisan egyszerű. Célunk, hogy a kutatók könnyen kiterjeszthessék és fejleszthessék az MLX-et, lehetővé téve az új ötletek gyors felfedezését.

Az LLM-ek gyorsíthatók Apple Silicon eszközökön az MLX segítségével, és a modellek helyben, nagyon kényelmesen futtathatók.

Az Apple MLX keretrendszer mostantól támogatja a Phi-3.5-Instruct (**Apple MLX Framework támogatás**), Phi-3.5-Vision (**MLX-VLM Framework támogatás**) és Phi-3.5-MoE (**Apple MLX Framework támogatás**) kvantálási átalakítását. Nézzük meg, hogyan működik:

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

### **🤖 Minták a Phi-3.5-höz az Apple MLX segítségével**

| Laborok    | Leírás | Tovább |
| -------- | ------- |  ------- |
| 🚀 Labor - Phi-3.5 Instruct bemutatása  | Tanuld meg, hogyan használd a Phi-3.5 Instructot az Apple MLX keretrendszerrel   |  [Tovább](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Labor - Phi-3.5 Vision bemutatása (kép) | Tanuld meg, hogyan használd a Phi-3.5 Visiont képelemzésre az Apple MLX keretrendszerrel     |  [Tovább](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Labor - Phi-3.5 Vision bemutatása (MoE)   | Tanuld meg, hogyan használd a Phi-3.5 MoE-t az Apple MLX keretrendszerrel  |  [Tovább](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Források**

1. Ismerd meg az Apple MLX keretrendszert: [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repó: [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repó: [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások használatával készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.