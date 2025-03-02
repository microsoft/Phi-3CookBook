# **Quantizzazione di Phi-3.5 utilizzando il framework Apple MLX**

MLX è un framework array per la ricerca sull'apprendimento automatico su Apple silicon, sviluppato dal team di ricerca sull'apprendimento automatico di Apple.

MLX è progettato da ricercatori di machine learning per ricercatori di machine learning. Il framework è pensato per essere facile da usare, ma al tempo stesso efficiente per l'addestramento e l'implementazione dei modelli. Anche il design del framework è concettualmente semplice. L'obiettivo è rendere semplice per i ricercatori estendere e migliorare MLX, al fine di esplorare rapidamente nuove idee.

Gli LLM possono essere accelerati sui dispositivi Apple Silicon tramite MLX, consentendo di eseguire i modelli localmente in modo molto comodo.

Ora il framework Apple MLX supporta la conversione quantizzata di Phi-3.5-Instruct (**supporto del framework Apple MLX**), Phi-3.5-Vision (**supporto del framework MLX-VLM**) e Phi-3.5-MoE (**supporto del framework Apple MLX**). Proviamolo subito:

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

### **🤖 Esempi per Phi-3.5 con Apple MLX**

| Labs    | Introduzione | Vai |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduzione Phi-3.5 Instruct  | Scopri come utilizzare Phi-3.5 Instruct con il framework Apple MLX   |  [Vai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduzione Phi-3.5 Vision (immagini) | Scopri come utilizzare Phi-3.5 Vision per analizzare immagini con il framework Apple MLX     |  [Vai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduzione Phi-3.5 Vision (moE)   | Scopri come utilizzare Phi-3.5 MoE con il framework Apple MLX  |  [Vai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Risorse**

1. Scopri di più sul framework Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repository GitHub di Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repository GitHub di MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.