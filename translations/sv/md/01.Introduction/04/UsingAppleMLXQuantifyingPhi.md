# **Kvantisering av Phi-3.5 med Apple MLX Framework**

MLX är ett ramverk för maskininlärning på Apple Silicon, utvecklat av Apples maskininlärningsforskningsteam.

MLX är utformat av forskare inom maskininlärning för forskare inom maskininlärning. Ramverket är tänkt att vara användarvänligt men samtidigt effektivt för att träna och distribuera modeller. Själva designen av ramverket är också konceptuellt enkel. Vi strävar efter att göra det enkelt för forskare att utöka och förbättra MLX med målet att snabbt kunna utforska nya idéer.

LLM:er kan accelereras på Apple Silicon-enheter med hjälp av MLX, och modeller kan köras lokalt på ett mycket smidigt sätt.

Nu stöder Apple MLX Framework kvantiseringskonvertering av Phi-3.5-Instruct (**Apple MLX Framework-stöd**), Phi-3.5-Vision (**MLX-VLM Framework-stöd**) och Phi-3.5-MoE (**Apple MLX Framework-stöd**). Låt oss prova:

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

### **🤖 Exempel för Phi-3.5 med Apple MLX**

| Labs    | Introduktion | Gå |
| -------- | ------------ | --- |
| 🚀 Lab-Introduktion Phi-3.5 Instruct  | Lär dig hur du använder Phi-3.5 Instruct med Apple MLX Framework   |  [Gå](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduktion Phi-3.5 Vision (bild) | Lär dig hur du använder Phi-3.5 Vision för att analysera bilder med Apple MLX Framework     |  [Gå](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduktion Phi-3.5 Vision (moE)   | Lär dig hur du använder Phi-3.5 MoE med Apple MLX Framework  |  [Gå](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resurser**

1. Läs mer om Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub-repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub-repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.