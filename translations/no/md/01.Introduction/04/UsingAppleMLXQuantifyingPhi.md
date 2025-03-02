# **Kvantisere Phi-3.5 med Apple MLX-rammeverket**

MLX er et array-rammeverk for maskinlæringsforskning på Apple Silicon, utviklet av Apples maskinlæringsforskningsteam.

MLX er designet av maskinlæringsforskere for maskinlæringsforskere. Rammeverket er laget for å være brukervennlig, men samtidig effektivt for trening og implementering av modeller. Selve designet av rammeverket er også konseptuelt enkelt. Vi ønsker å gjøre det lett for forskere å utvide og forbedre MLX, med mål om raskt å utforske nye ideer.

LLM-er kan akselereres på Apple Silicon-enheter gjennom MLX, og modeller kan enkelt kjøres lokalt.

Nå støtter Apple MLX Framework kvantisering av Phi-3.5-Instruct (**Apple MLX Framework-støtte**), Phi-3.5-Vision (**MLX-VLM Framework-støtte**) og Phi-3.5-MoE (**Apple MLX Framework-støtte**). La oss prøve det:

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

### **🤖 Eksempler for Phi-3.5 med Apple MLX**

| Labs    | Introduksjon | Gå til |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduksjon Phi-3.5 Instruct  | Lær hvordan du bruker Phi-3.5 Instruct med Apple MLX-rammeverket   |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduksjon Phi-3.5 Vision (bilde) | Lær hvordan du bruker Phi-3.5 Vision til å analysere bilder med Apple MLX-rammeverket     |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduksjon Phi-3.5 Vision (MoE)   | Lær hvordan du bruker Phi-3.5 MoE med Apple MLX-rammeverket  |  [Gå til](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressurser**

1. Lær om Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub-repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub-repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.