# **Kvantisering af Phi-3.5 med Apple MLX Framework**

MLX er et array-framework til maskinlæringsforskning på Apple Silicon, udviklet af Apple maskinlæringsforskning.

MLX er designet af maskinlæringsforskere til maskinlæringsforskere. Frameworket er beregnet til at være brugervenligt, men stadig effektivt til at træne og implementere modeller. Designet af frameworket er også konceptuelt simpelt. Vi ønsker at gøre det nemt for forskere at udvide og forbedre MLX med målet om hurtigt at udforske nye ideer.

LLM'er kan accelereres på Apple Silicon-enheder gennem MLX, og modeller kan nemt køres lokalt.

Nu understøtter Apple MLX Framework kvantiseringskonvertering af Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**) og Phi-3.5-MoE(**Apple MLX Framework support**). Lad os prøve det næste:

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

### **🤖 Eksempler på Phi-3.5 med Apple MLX**

| Labs    | Introduktion | Gå til |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduktion til Phi-3.5 Instruct  | Lær hvordan man bruger Phi-3.5 Instruct med Apple MLX framework   |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduktion til Phi-3.5 Vision (billede) | Lær hvordan man bruger Phi-3.5 Vision til at analysere billeder med Apple MLX framework     |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduktion til Phi-3.5 Vision (moE)   | Lær hvordan man bruger Phi-3.5 MoE med Apple MLX framework  |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressourcer**

1. Lær om Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der måtte opstå ved brugen af denne oversættelse.