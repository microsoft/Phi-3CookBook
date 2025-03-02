# **Het kwantiseren van Phi-3.5 met behulp van het Apple MLX Framework**

MLX is een array-framework voor machine learning-onderzoek op Apple Silicon, ontwikkeld door het machine learning-onderzoeksteam van Apple.

MLX is ontworpen door en voor machine learning-onderzoekers. Het framework is gebruiksvriendelijk, maar toch efficiënt voor het trainen en implementeren van modellen. De opzet van het framework is conceptueel eenvoudig, zodat onderzoekers MLX gemakkelijk kunnen uitbreiden en verbeteren om snel nieuwe ideeën te verkennen.

LLM's kunnen worden versneld op Apple Silicon-apparaten met behulp van MLX, en modellen kunnen lokaal zeer eenvoudig worden uitgevoerd.

Het Apple MLX Framework ondersteunt nu kwantisatieconversie van Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**) en Phi-3.5-MoE (**Apple MLX Framework support**). Laten we het eens proberen:

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

### **🤖 Voorbeelden voor Phi-3.5 met Apple MLX**

| Labs    | Introductie | Ga |
| -------- | ------- |  ------- |
| 🚀 Lab-Introductie Phi-3.5 Instruct  | Leer hoe je Phi-3.5 Instruct gebruikt met het Apple MLX framework   |  [Ga](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introductie Phi-3.5 Vision (afbeelding) | Leer hoe je Phi-3.5 Vision gebruikt om afbeeldingen te analyseren met het Apple MLX framework     |  [Ga](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introductie Phi-3.5 Vision (moE)   | Leer hoe je Phi-3.5 MoE gebruikt met het Apple MLX framework  |  [Ga](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Bronnen**

1. Meer informatie over het Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gestuurde machinevertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.