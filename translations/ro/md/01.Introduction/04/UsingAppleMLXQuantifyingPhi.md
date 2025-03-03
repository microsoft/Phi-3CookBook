# **Cuantizarea Phi-3.5 folosind Apple MLX Framework**

MLX este un framework de array pentru cercetarea în domeniul învățării automate pe dispozitivele Apple Silicon, dezvoltat de echipa de cercetare în machine learning de la Apple.

MLX este creat de cercetători în machine learning pentru cercetători în machine learning. Framework-ul este conceput să fie ușor de utilizat, dar în același timp eficient pentru antrenarea și implementarea modelelor. Designul framework-ului este, de asemenea, simplu din punct de vedere conceptual. Ne dorim să fie ușor pentru cercetători să extindă și să îmbunătățească MLX, având ca scop explorarea rapidă a ideilor noi.

LLM-urile pot fi accelerate pe dispozitivele Apple Silicon prin MLX, iar modelele pot fi rulate local cu mare ușurință.

Acum, Apple MLX Framework suportă conversia prin cuantizare a Phi-3.5-Instruct (**suport Apple MLX Framework**), Phi-3.5-Vision (**suport MLX-VLM Framework**) și Phi-3.5-MoE (**suport Apple MLX Framework**). Haideți să încercăm:

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

### **🤖 Exemple pentru Phi-3.5 cu Apple MLX**

| Laboratoare | Introducere | Acces |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Învață cum să utilizezi Phi-3.5 Instruct cu framework-ul Apple MLX   |  [Acces](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (imagine) | Învață cum să utilizezi Phi-3.5 Vision pentru a analiza imagini cu framework-ul Apple MLX     |  [Acces](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Învață cum să utilizezi Phi-3.5 MoE cu framework-ul Apple MLX  |  [Acces](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resurse**

1. Află mai multe despre Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repository-ul GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repository-ul GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa natală, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.